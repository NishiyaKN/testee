"""Monta ../simulado2-enade-2026.html (arquivo único, abre offline) a partir de:
  - simulado2-dados/template.html            motor do quiz (derivado de treino-enade-2026.html)
  - simulado2-dados/questoes/<slug>.json     objetivas por tópico (sem as do Simulado 1) e fg.json
  - simulado2-dados/dissertativas_provaveis.json  discursivas inéditas (temas de menor acerto no Simulado 1)
  - simulado2-dados/inferidas.json           questões inferidas antigas (extras, desmarcadas por padrão)
  - simulado2-dados/onde.json                onde estudar cada tema
  - simulado2-dados/img/*.webp               figuras recortadas (embutidas em base64)

Uso (na raiz do repositório):
    python3 simulado2-dados/build_simulado2.py
"""
import base64
import html
import json
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)
OUT = os.path.join(ROOT, 'simulado2-enade-2026.html')

# ordem, nome e desempenho da turma no Simulado 1 (Análise dos Resultados)
TOPICOS = [
    ('cx', '01 · Complexidade de Algoritmos', '43,86%', 'Médio-Alto'),
    ('ed', '02 · Estruturas de Dados', '38,60%', 'Alto'),
    ('es', '03 · Engenharia de Software', '67,54%', 'Baixo'),
    ('oo', '04 · Orientação a Objetos', '65,50%', 'Baixo'),
    ('arq', '05 · Arquitetura de Computadores', '55,26%', 'Médio-Baixo'),
    ('so', '06 · Sistemas Operacionais', '45,61%', 'Médio-Alto'),
    ('redes', '07 · Redes de Computadores', '43,27%', 'Médio-Alto'),
    ('seg', '08 · Segurança da Informação', '77,19%', 'Baixo'),
    ('grafos', '09 · Teoria dos Grafos', '41,23%', 'Alto'),
    ('tc', '10 · Teoria da Computação', '50,88%', 'Médio'),
    ('comp', '11 · Compiladores', '56,14%', 'Médio-Baixo'),
]
EIXOS = [
    ('fg-vozes', 'Vozes Negras', 'Relações étnico-raciais, racismo estrutural, ações afirmativas, representatividade.'),
    ('fg-socio', 'Socioambiental América Latina', 'Clima, Amazônia, povos indígenas e tradicionais, justiça ambiental, Agenda 2030.'),
    ('fg-conj', 'Conjuntura Internacional', 'Geopolítica, globalização, multilateralismo, conflitos, migrações, desinformação.'),
]
INF_MAP = {'cx-inf': 'cx', 'es-inf': 'es', 'oo-inf': 'oo', 'arq-inf': 'arq', 'redes-inf': 'redes',
           'seg-inf': 'seg', 'grafos-inf': 'grafos', 'tc-inf': 'tc', 'comp-inf': 'comp'}


def load(name):
    with open(os.path.join(BASE, name), encoding='utf-8') as f:
        return json.load(f)


def img_html(m):
    fname, _, alt = m.group(1).partition('|')
    path = os.path.join(BASE, 'img', fname.strip())
    with open(path, 'rb') as f:
        b64 = base64.b64encode(f.read()).decode()
    ext = os.path.splitext(fname)[1].lower().lstrip('.')
    mime = {'webp': 'image/webp', 'png': 'image/png', 'jpg': 'image/jpeg', 'jpeg': 'image/jpeg'}[ext]
    alt = html.escape(alt.strip() or 'Figura da questão', quote=True)
    return f'<figure><img src="data:{mime};base64,{b64}" alt="{alt}" loading="lazy"><figcaption>{alt}</figcaption></figure>'


def fix_html(s):
    return re.sub(r'\{\{IMG:([^}]+)\}\}', img_html, s or '')


def norm_q(q, set_id, num):
    cor = q['cor']
    tipo = q.get('tipo') or ('multi' if isinstance(cor, list) else 'mc')
    if tipo == 'mc' and isinstance(cor, list) and len(cor) == 1:
        cor = cor[0]
    return {
        'id': f'{set_id}-{num}', 'set': set_id, 'num': num,
        'ref': q.get('ref') or str(num), 'tipo': tipo,
        'enun': fix_html(q.get('enun') or q.get('enunciado')),
        'alts': [{'l': a['l'], 't': fix_html(a['t'])} for a in q['alts']],
        'cor': cor, 'just': q.get('just') or '', 'dup': None,
        'nota': q.get('nota') or None, 'tags': q.get('tags') or [],
    }


def main():
    sets, questions, diss = [], [], []
    resumo = []
    onde = load('onde.json')

    # 1 · Conhecimento Específico (squads)
    for slug, nome, acerto, nivel in TOPICOS:
        path = os.path.join(BASE, 'questoes', f'{slug}.json')
        if not os.path.exists(path):
            print('AVISO: falta', path)
            continue
        d = load(os.path.join('questoes', f'{slug}.json'))
        sid = f'ce-{slug}'
        qs = [norm_q(q, sid, i + 1) for i, q in enumerate(d['questoes'])]
        exc = d.get('excluidas_simulado1') or []
        exc_txt = ', '.join(re.sub(r'\s*\([^)]*reais-[^)]*\)', '', str(e.get('banco'))) + f" (Sim. {e.get('simulado')})" for e in exc)
        crit = nivel in ('Alto', 'Crítico')
        sets.append({
            'id': sid, 'grupo': 'ce', 'nome': nome, 'item': 'questão',
            'acerto': f"Simulado 1: <b class=\"{'crit' if crit else ''}\">{acerto}</b> de acerto (dificuldade {nivel.lower()})",
            'desc': f"{len(qs)} questões dos materiais do squad." + (f" Fora por terem caído no Simulado 1: {exc_txt}." if exc else ''),
        })
        questions += qs
        for k, dd in enumerate(d.get('dissertativas') or []):
            diss.append(dict(dd, id=f'mat-{slug}-{k + 1}', grupo='materiais'))
        resumo.append((nome, len(qs), len(exc), len(d.get('dissertativas') or [])))

    # extras: inferidas (desmarcadas por padrão)
    inf = load('inferidas.json')
    for old_set, slug in INF_MAP.items():
        qs_old = [q for q in inf if q['set'] == old_set]
        if not qs_old:
            continue
        nome = dict((s, n) for s, n, _, _ in TOPICOS)[slug]
        sid = f'inf-{slug}'
        sets.append({'id': sid, 'grupo': 'ce', 'extra': True, 'item': 'questão',
                     'sub': 'Extras: questões inferidas (criadas para cobrir subtópicos; não são dos squads)',
                     'nome': nome.split(' · ', 1)[1] + ' (inferidas)',
                     'desc': 'Não constam nos materiais; servem para revisar subtópicos sem questão do squad.'})
        for i, q in enumerate(qs_old):
            nq = dict(q, id=f'{sid}-{i + 1}', set=sid, num=i + 1, dup=None)
            nq['ref'] = 'Inferida ' + str(q.get('ref') or i + 1)
            questions.append(nq)

    # 2 · Formação Geral (ENADE Talks)
    fg_path = os.path.join(BASE, 'questoes', 'fg.json')
    fg = load(fg_path) if os.path.exists(fg_path) else {'questoes': []}
    for sid, eixo, desc in EIXOS:
        qs_e = [q for q in fg['questoes'] if q.get('eixo') == eixo]
        reais = sum(1 for q in qs_e if q.get('origem') == 'enade')
        sets.append({'id': sid, 'grupo': 'fg', 'nome': eixo, 'item': 'questão',
                     'desc': f"{desc} {reais} de provas anteriores do ENADE e {len(qs_e) - reais} inéditas."})
        questions += [norm_q(q, sid, i + 1) for i, q in enumerate(qs_e)]
        resumo.append(('FG · ' + eixo, len(qs_e), 0, 0))

    # 3 · Dissertativas
    prov = load('dissertativas_provaveis.json')
    diss = [dict(d, id=f'prov-{i + 1}', grupo='provaveis') for i, d in enumerate(prov)] + diss
    for d in diss:
        for k in ('caso', 'enun', 'exemplo'):
            if d.get(k):
                d[k] = fix_html(d[k])
    diss_grupos = [
        {'id': 'provaveis', 'titulo': 'Prováveis: temas de menor acerto no Simulado 1',
         'desc': 'Inéditas, no formato das discursivas do ENADE (texto-base e itens a, b e c com valor). Ordenadas pela prioridade: a de Arquiteturas de Software (Q14, 15,79%) e a de BFS × DFS (Q6, 17,54%) foram as piores questões da prova.'},
        {'id': 'materiais', 'titulo': 'Dos materiais dos squads',
         'desc': 'Discursivas, exercícios e exemplos resolvidos que aparecem nos slides, cadernos e apostilas.'},
    ]

    # checagens
    ids = [q['id'] for q in questions]
    assert len(ids) == len(set(ids)), 'ids duplicados'
    for q in questions:
        letters = [a['l'] for a in q['alts']]
        for c in (q['cor'] if isinstance(q['cor'], list) else [q['cor']]):
            assert c in letters, (q['id'], q['cor'], letters)
        assert q['enun'] and q['just'], q['id']
        for t in q['tags']:
            onde.setdefault(t, '')

    padrao = [s['id'] for s in sets if not s.get('extra')]
    data = {'meta': {'titulo': 'Simulado 2 ENADE 2026 — Ciência da Computação (USCS)',
                     'chave': 'enade-2026-cc-uscs-simulado2', 'conjuntosPadrao': padrao},
            'sets': sets, 'questions': questions, 'onde': {k: v for k, v in onde.items() if v},
            'dissertativas': diss, 'dissGrupos': diss_grupos}

    tpl = open(os.path.join(BASE, 'template.html'), encoding='utf-8').read()
    js = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
    out = tpl.replace('/*__DATA__*/null', js, 1)
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(out)

    print(f'{OUT}: {len(out) / 1024:.0f} KB')
    for nome, n, e, dd in resumo:
        print(f'  {nome:42s} {n:3d} questões  (excluídas: {e}, discursivas: {dd})')
    print('  inferidas (extras):', sum(1 for q in questions if q['set'].startswith('inf-')))
    print('  dissertativas:', len(diss))


if __name__ == '__main__':
    main()
