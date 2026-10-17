# Questões INFERIDAS: prováveis questões dos squads que não temos

> ⚠️ **Estas questões não constam nos materiais.** Elas foram elaboradas para cobrir os subtópicos do material explicativo e dos slides de cada squad que **não têm nenhuma questão conhecida**. As questões reais estão em [`../questoes_por_topico/`](../questoes_por_topico/README.md).

## Por que inferir
- **Premissa:** cada subtópico do material de um squad provavelmente tem pelo menos uma questão no banco desse squad. Temos só parte delas.
- **Padrão dos squads:** todo o material e as questões foram gerados com IA a partir do prompt-modelo do professor (documento *Estrutura de Questões sob o padrão do ENADE*). Por isso as questões seguem um padrão bem regular:
  - estrutura **situação-problema + dados de suporte (com fonte citada) + comando**;
  - 4 alternativas com uma correta e três distratores plausíveis de tamanho parecido (alguns squads usam 5);
  - tipos variados (resposta única, afirmativas múltiplas, asserção-razão, associação, ordenação, lacunas, afirmativa negativa etc.).
- **Como as inferidas imitam esse padrão:** usam a estrutura, o número de alternativas, o tom e as referências **de cada squad**. São construídas com os exemplos, números, tabelas e "pegadinhas" do próprio material, com a página citada.

## Como cada arquivo está organizado
1. **Mapa de cobertura:** cada subtópico do material, a questão conhecida que já o cobre (se houver) e a questão inferida criada para ele, com prioridade Alta, Média ou Baixa.
2. **As questões inferidas (I1, I2, …):** cada uma com gabarito, explicação de por que cada alternativa está certa ou errada, a base no material (página) e o conceito-chave.

Todas as contas, códigos, autômatos e grafos foram conferidos com Python (e Java, no caso de OO).

## Arquivos

| Arquivo | Questões inferidas | Observação |
|---|---|---|
| [01_Complexidade_de_Algoritmos.md](01_Complexidade_de_Algoritmos.md) | 12 | O material não tem P/NP, backtracking nem análise amortizada, então não há questão desses temas |
| [02_Estruturas_de_Dados.md](02_Estruturas_de_Dados.md) | 6 | **Fora do quiz:** o arquivo de questões do squad parece ser o banco completo (6 questões) |
| [03_Engenharia_de_Software.md](03_Engenharia_de_Software.md) | 36 | Os módulos 5 (POO/arquitetura) e 6 (testes) da apostila não têm questão conhecida |
| [04_Orientacao_a_Objetos.md](04_Orientacao_a_Objetos.md) | 18 | Inclui o Tópico 8 (Observer, Mediator, Singleton) |
| [05_Arquitetura_de_Computadores.md](05_Arquitetura_de_Computadores.md) | 23 | 13 dos 16 tópicos da revisão estavam sem questão |
| — Sistemas Operacionais | 0 | Não precisa: o caderno tem as 12 questões, cobrindo os 9 tópicos da matriz |
| [07_Redes_de_Computadores.md](07_Redes_de_Computadores.md) | 35 | I1–I6 são as prováveis **Questões 2, 3, 4, 7, 9 e 10** que faltam nos slides; I7–I35 cobrem o restante do Manual |
| [08_Seguranca_da_Informacao.md](08_Seguranca_da_Informacao.md) | 22 | |
| [09_Teoria_dos_Grafos.md](09_Teoria_dos_Grafos.md) | 15 | O material não tem Kruskal, Euler/Hamilton nem coloração |
| [10_Teoria_da_Computacao.md](10_Teoria_da_Computacao.md) | 22 | Expressões regulares, AFND, decidibilidade, problema da parada, Church-Turing |
| [11_Compiladores.md](11_Compiladores.md) | 8 | O material explicativo só analisa as Questões 1–5, então talvez o banco real seja só esse |
| **Total** | **197** | (191 no quiz, sem as 6 de Estruturas de Dados) |

**Como estudar:** comece pelas questões de prioridade **Alta** de cada mapa de cobertura. As inferidas são apostas fundamentadas: o conteúdo cobrado está no material, mas o enunciado real do squad pode ser diferente.
