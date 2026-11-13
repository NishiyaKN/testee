# Fontes do Simulado 2 (`../simulado2-enade-2026.html`)

| Arquivo | Conteúdo |
|---|---|
| `questoes/<slug>.json` | Objetivas de cada tópico tiradas dos cadernos e gabaritos dos squads (e das questões extras: manual de Redes, ENADE na apostila de Segurança, exemplos do professor), **sem as que caíram no Simulado 1**. A lista do que ficou de fora está em `excluidas_simulado1`. |
| `questoes/fg.json` | Formação Geral sobre os temas do ENADE Talks de 11/11 (Vozes Negras; Desafios Socioambientais da América Latina; Conjuntura Internacional): questões reais de provas anteriores do ENADE e questões inéditas no mesmo formato. |
| `dissertativas_provaveis.json` | Discursivas inéditas sobre os temas de menor acerto no Simulado 1 (ranking da "Análise dos Resultados"). |
| `inferidas.json` | As questões inferidas do treino antigo, que entram como extras desmarcados por padrão. |
| `onde.json` | Onde estudar cada tema (aparece na aba Revisar). |
| `img/` | Figuras recortadas dos cadernos, embutidas em base64 no HTML. |
| `template.html` | O motor do quiz, derivado de `treino-enade-2026.html`, com as 3 seções e o simulado sorteado. |
| `build_simulado2.py` | Script que monta o HTML. |

Para regerar o HTML, rode na raiz do repositório:

```bash
python3 simulado2-dados/build_simulado2.py
```
