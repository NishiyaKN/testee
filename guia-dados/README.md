# Fontes do guia de estudos

Arquivos usados para gerar `../guia-estudos-enade-2026.html`:

- `frag/NN.html`: conteúdo de cada tópico (seções aninhadas com `data-titulo`);
- `img/`: figuras recortadas dos materiais dos squads;
- `guia_template.html` e `build_guia.py`: layout e script de montagem.

Para regerar (na raiz do repositório):

```bash
python3 guia-dados/build_guia.py guia-dados/frag guia-dados/img guia-estudos-enade-2026.html
```
