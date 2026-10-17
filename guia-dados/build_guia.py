#!/usr/bin/env python3
"""Monta o guia de estudos (HTML único) a partir dos fragmentos por tópico.

Uso: python3 -I build_guia.py <dir_frag> <dir_img> <saida.html> [--so NN,NN]

Fragmento = HTML com <section class="topico|sub" id="..." data-titulo="..."> aninhadas.
O script insere os títulos (h2/h3/h4/h5), monta o menu em árvore, embute as imagens
(src="img/arquivo") como WebP em data URI e embrulha tabelas para rolar no celular.
"""
import base64, html, io, re, sys
from pathlib import Path
from PIL import Image

frag_dir, img_dir, saida = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
so = None
if '--so' in sys.argv:
    so = sys.argv[sys.argv.index('--so') + 1].split(',')

erros, avisos = [], []
TAG = re.compile(r'(<section\b[^>]*>)|(</section>)', re.I)
ATTR = lambda tag, nome: (re.search(rf'\b{nome}\s*=\s*"([^"]*)"', tag) or [None, None])[1]

def processa(texto, origem):
    """Insere títulos e devolve (html, nós). Nó = dict(id, titulo, filhos)."""
    out, pos, pilha, raiz = [], 0, [], []
    for m in TAG.finditer(texto):
        out.append(texto[pos:m.start()]); pos = m.end()
        if m.group(1):
            tag = m.group(1)
            sid, tit, cls = ATTR(tag, 'id'), ATTR(tag, 'data-titulo'), ATTR(tag, 'class') or ''
            if not sid or not tit:
                erros.append(f'{origem}: <section> sem id ou data-titulo: {tag[:80]}')
            depth = len(pilha)
            if depth == 0 and 'topico' not in cls:
                erros.append(f'{origem}: seção de nível 0 deve ter class="topico": {sid}')
            if depth > 3:
                erros.append(f'{origem}: aninhamento profundo demais em {sid}')
            no = {'id': sid, 'titulo': tit or '?', 'filhos': []}
            (pilha[-1]['filhos'] if pilha else raiz).append(no)
            pilha.append(no)
            n = min(depth + 2, 5)
            out.append(tag + f'<h{n} class="sec-h"><a href="#{sid}">{html.escape(tit or "?")}</a></h{n}>')
        else:
            if not pilha:
                erros.append(f'{origem}: </section> sem abertura'); continue
            pilha.pop(); out.append(m.group(2))
    out.append(texto[pos:])
    if pilha:
        erros.append(f'{origem}: <section> sem fechamento: {[p["id"] for p in pilha]}')
    return ''.join(out), raiz

def arvore(nos, nivel=0):
    h = ['<ul>' if nivel else '<ul class="tree" id="tree">']
    for n in nos:
        tem = bool(n['filhos'])
        h.append(f'<li class="{"has" if tem else "leaf"}" data-id="{n["id"]}">'
                 f'<div class="row">'
                 + (f'<button class="tg" aria-label="Abrir ou fechar"></button>' if tem else '<span class="tg-sp"></span>')
                 + f'<a href="#{n["id"]}">{html.escape(n["titulo"])}</a></div>')
        if tem:
            h.append(arvore(n['filhos'], nivel + 1))
        h.append('</li>')
    h.append('</ul>')
    return ''.join(h)

cache_img, total_img = {}, [0]
def embute(m):
    nome = m.group(1)
    if nome in cache_img:
        return f'src="{cache_img[nome]}"'
    p = img_dir / nome
    if not p.exists() and (img_dir / (Path(nome).stem + '.webp')).exists():
        p = img_dir / (Path(nome).stem + '.webp')
    if not p.exists():
        erros.append(f'imagem não encontrada: {nome}'); return m.group(0)
    im = Image.open(p)
    if im.mode not in ('RGB', 'RGBA'):
        im = im.convert('RGBA' if 'A' in im.getbands() else 'RGB')
    if im.width > 1100:
        im = im.resize((1100, round(im.height * 1100 / im.width)), Image.LANCZOS)
    buf = io.BytesIO(); im.save(buf, 'WEBP', quality=72, method=6)
    total_img[0] += buf.tell()
    if buf.tell() > 250_000:
        avisos.append(f'imagem grande ({buf.tell()//1024} KB): {nome}')
    uri = 'data:image/webp;base64,' + base64.b64encode(buf.getvalue()).decode()
    cache_img[nome] = uri
    return f'src="{uri}"'

corpo, nos, ids = [], [], set()
frags = sorted(frag_dir.glob('[0-9][0-9].html'))
if so:
    frags = [f for f in frags if f.stem in so]
for f in frags:
    t = f.read_text(encoding='utf-8')
    if re.search(r'<h[1-4][\s>]', t, re.I):
        avisos.append(f'{f.name}: usa <h1>–<h4> no conteúdo (os títulos são gerados pelo data-titulo; use <h5> para subtítulos internos)')
    t, raiz = processa(t, f.name)
    t = re.sub(r'src="img/([^"]+)"', embute, t)
    t = re.sub(r'(?<!<div class="tw">)(<table\b.*?</table>)', r'<div class="tw">\1</div>', t, flags=re.S | re.I)
    corpo.append(t); nos += raiz
def coleta(ns):
    for n in ns:
        if n['id'] in ids: erros.append(f'id repetido: {n["id"]}')
        ids.add(n['id']); coleta(n['filhos'])
coleta(nos)
for href in re.findall(r'href="#([^"]+)"', ''.join(corpo)):
    if href not in ids:
        avisos.append(f'link interno para id inexistente: #{href}')

if erros:
    print('ERROS:'); [print('  -', e) for e in erros]; sys.exit(1)

tpl = (Path(__file__).parent / 'guia_template.html').read_text(encoding='utf-8')
final = tpl.replace('<!--ARVORE-->', arvore(nos)).replace('<!--CONTEUDO-->', '\n'.join(corpo))
saida.write_text(final, encoding='utf-8')
for a in avisos: print('  aviso:', a)
print(f'ok: {saida} ({len(final)//1024} KB; imagens {total_img[0]//1024} KB em {len(cache_img)} arquivos; {len(ids)} seções)')
