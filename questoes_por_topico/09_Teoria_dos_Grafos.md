# Teoria dos Grafos — Questões e Gabarito Comentado

**Squad responsável:** Squad 2 (Davi Valdez Rodrigues · Gabriel Carvalho Bielawski · Gustavo Almeida de Moura · Larissa Pereira Ibiapino · Kauê Sanches Barbi)
**Materiais analisados:**
| Arquivo | Páginas | Tipo | Questões encontradas (páginas) |
|---|---|---|---|
| `Teoria dos Grafos.pdf` | 54 | Slides | Q1–Q4 objetivas padrão ENADE com gabarito (p. 16–18, 27–28, 42–43, 51–52); Q5–Q6 perguntas discursivas com resposta (p. 15; p. 31 com respostas nas p. 33, 35, 41) |
| `TEORIA_DOS_GRAFOS - MATERIAL EXPLICATIVO.pdf` | 38 | Material explicativo (apostila) | Nenhuma questão objetiva. Exemplos resolvidos formulados como pergunta: Q7 (p. 15, item 3.4), Q8 (p. 15, item 3.6), Q9 (p. 20, item 4.6) |

**Resumo:** 9 itens encontrados.
- 4 questões objetivas no padrão ENADE (Q1–Q4), todas nos slides e todas com gabarito e comentário de cada alternativa no próprio material. Conferi as quatro e concordo com todas.
- 5 perguntas discursivas ou exemplos resolvidos (Q5–Q9), todos com resposta no próprio material. Conferi todas as respostas.
- Nenhum item ficou sem gabarito.
- As questões objetivas têm só **4 alternativas (A–D)**, não 5.
- A apostila não traz questões, só teoria e exemplos. O apêndice no fim deste arquivo traz os dados de todas as figuras (grafos, pesos, matrizes), com os algoritmos refeitos, para o caso de a prova usar uma dessas figuras.

> Legenda: ✅ correta · ❌ incorreta · ⚠️ ponto de atenção (gabarito do material duvidoso, ambiguidade, versão divergente)

## Índice
1. [Q1 — Handshake Lemma e planaridade](#q1--handshake-lemma-e-planaridade)
2. [Q2 — Matriz x Lista de adjacência](#q2--matriz-x-lista-de-adjacência)
3. [Q3 — BFS e menor número de arestas](#q3--bfs-e-menor-número-de-arestas)
4. [Q4 — Dijkstra, Bellman-Ford e Prim](#q4--dijkstra-bellman-ford-e-prim)
5. [Q5 — Kuratowski: conclusão sobre planaridade (discursiva)](#q5--kuratowski-conclusão-sobre-planaridade-discursiva)
6. [Q6 — Ordem de visita DFS e BFS a partir de A (discursiva)](#q6--ordem-de-visita-dfs-e-bfs-a-partir-de-a-discursiva)
7. [Q7 — Número de arestas pela sequência de graus (exemplo resolvido)](#q7--número-de-arestas-pela-sequência-de-graus-exemplo-resolvido)
8. [Q8 — Sequência de graus impossível (exemplo de diagnóstico)](#q8--sequência-de-graus-impossível-exemplo-de-diagnóstico)
9. [Q9 — Não planaridade de K5 e K3,3 pela fórmula de Euler (exemplo de diagnóstico)](#q9--não-planaridade-de-k5-e-k33-pela-fórmula-de-euler-exemplo-de-diagnóstico)
10. [Apêndice — Figuras e exemplos numéricos do material (conferidos)](#apêndice--figuras-e-exemplos-numéricos-do-material-conferidos)

---

## Q1 — Handshake Lemma e planaridade
**Fonte:** `Teoria dos Grafos.pdf`, p. 16 (enunciado), p. 17–18 (gabarito comentado)
**Tipo ENADE:** Resposta única (interpretação)

**Enunciado:**
SITUAÇÃO-PROBLEMA
Uma equipe de desenvolvimento está modelando uma rede de comunicação entre diferentes pontos de uma infraestrutura computacional. Para representar a rede, foi utilizado um grafo não direcionado G=(V,E), no qual os vértices representam os pontos da rede e as arestas representam as conexões entre eles.
Durante a análise da representação, a equipe identificou que o grafo possui 10 vértices e 15 arestas. Além disso, após reorganizar visualmente os vértices e as arestas, foi identificada uma subdivisão de K3,3 na estrutura do grafo.

COMANDO
Considerando os conceitos de grau dos vértices, Handshake Lemma e planaridade, analise a situação apresentada e assinale a alternativa que apresenta a conclusão correta.

**Alternativas:**
- **A)** A soma dos graus dos vértices é 15, e o grafo pode ser planar, pois os cruzamentos das arestas podem ser eliminados pela reorganização dos vértices.
- **B)** A soma dos graus dos vértices é 30, e o grafo é não planar devido à presença de uma subdivisão de K3,3.
- **C)** A soma dos graus dos vértices é 25, e o grafo é não planar porque possui número ímpar de arestas.
- **D)** A soma dos graus dos vértices é 30, porém não é possível determinar a planaridade do grafo apenas pela identificação de uma subdivisão de K3,3.

**Gabarito: B** — _(origem: gabarito do próprio material, p. 17 (alternativa B destacada em verde) e p. 18 ("Gabarito: B"))_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Confunde a soma dos graus com o número de arestas. Cada aresta contribui com 2 para a soma, então a soma é 2·15 = 30, e não 15 (material, p. 17). A segunda parte também está errada: a subdivisão de K3,3 foi achada *depois* de reorganizar o desenho. Planaridade é uma propriedade do grafo, não do desenho, e nenhum redesenho elimina um K3,3 subdividido.
- **B) ✅** — Pelo Handshake Lemma, Σ grau(v) = 2|E| = 2(15) = 30. Pelo Teorema de Kuratowski, um grafo que contém uma subdivisão de K5 ou de K3,3 é não planar (material, p. 18).
- **C) ❌** — 25 nem é possível, porque a soma dos graus é sempre par (é igual a 2|E|). Além disso, a paridade do número de arestas não tem relação com planaridade (material, p. 17). Contraexemplo: o triângulo K3 tem 3 arestas e é planar.
- **D) ❌** — A soma 30 está certa, mas a conclusão está errada. Pelo Teorema de Kuratowski, conter uma subdivisão de K5 ou K3,3 é condição *suficiente* (e também necessária) para a não planaridade. Logo, essa identificação basta para determinar a planaridade (material, p. 17).

**Conceito-chave para a prova:**
- A soma dos graus é sempre 2|E|. O número de vértices (10) é distrator e não entra na conta.
- Kuratowski: o grafo é planar se, e somente se, não contém uma subdivisão de K5 nem de K3,3.
- Possível pegadinha em versões alteradas: com 10 vértices e 15 arestas, a desigualdade |E| ≤ 3|V| − 6 é satisfeita (15 ≤ 24). Isso **não** prova que o grafo é planar, porque a desigualdade é só condição necessária. Quem decide aqui é a subdivisão de K3,3.
- Os dados são consistentes: o grafo de Petersen tem exatamente 10 vértices e 15 arestas e contém uma subdivisão de K3,3.

---

## Q2 — Matriz x Lista de adjacência
**Fonte:** `Teoria dos Grafos.pdf`, p. 27 (enunciado), p. 28 (gabarito comentado)
**Tipo ENADE:** Julgamento de afirmativas V/F (sequência correta)

**Enunciado:**
SITUAÇÃO-PROBLEMA
Uma equipe de engenharia de software está projetando o módulo de conexões e rotas de uma aplicação. O sistema precisa armazenar e manipular um grafo na memória, onde as interseções representam vértices e as rotas representam arestas direcionadas. Diante da preocupação com a alocação de memória e com a velocidade de acesso às conexões, a equipe analisa a adoção de Matrizes de Adjacência ou Listas de Adjacência.

COMANDO
Analise as afirmações a seguir sobre as estruturas de representação computacional de grafos e a tomada de decisão da equipe, identificando-as como Verdadeiras (V) ou Falsas (F):

( ) A Matriz de Adjacência aloca uma tabela com dimensão fixa proporcional a V x V (onde V é o número de vértices), reservando espaço na memória para todas as conexões possíveis, existam elas ou não.

( ) Em grafos direcionados, a Matriz de Adjacência é naturalmente simétrica, de modo que a posição (Linha A, Coluna B) terá sempre o mesmo valor que a posição (Linha B, Coluna A).

( ) A Lista de Adjacência é mais eficiente em termos de armazenamento quando o grafo é esparso (possui poucas conexões em relação ao número de vértices), pois guarda apenas os vértices vizinhos com os quais realmente existe conexão.

( ) A verificação direta da existência de uma conexão entre dois vértices específicos é operacionalmente mais rápida em uma Lista de Adjacência do que em uma Matriz de Adjacência, pois a lista permite acesso indexado direto em tempo constante O(1).

Assinale a alternativa com a sequência correta.

**Julgamento das afirmativas:**
- **1ª — Verdadeira.** A matriz tem dimensão |V|×|V| e ocupa O(|V|²) de memória, qualquer que seja o número de arestas.
- **2ª — Falsa.** Em grafo direcionado, a[i][j] = 1 indica o arco i→j, o que não implica j→i. A matriz em geral é **assimétrica**. Exemplo do próprio slide (p. 22): (A,B) = 1, mas (B,A) = 0. Simetria é característica de grafo não direcionado. O "naturalmente" e o "sempre" tornam a afirmativa falsa.
- **3ª — Verdadeira.** A lista ocupa O(|V| + |E|) porque guarda só as conexões que existem. Por isso é a melhor escolha para grafos esparsos.
- **4ª — Falsa.** A afirmativa inverte as estruturas. O teste de aresta em O(1), por acesso indexado a[u][v], é vantagem da **matriz**. Na lista, é preciso percorrer os vizinhos de u, o que custa O(grau(u)) (apostila, p. 23).

**Alternativas:**
- **A)** V – F – V – F
- **B)** V – V – V – F
- **C)** F – F – V – V
- **D)** V – F – F – V

**Gabarito: A** — _(origem: gabarito do próprio material, p. 28, alternativa A destacada em verde)_

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — "A matriz aloca tamanho V x V fixo; grafos direcionados geram matrizes assimétricas; a lista economiza memória em grafos esparsos ao guardar só o que existe; e o acesso direto O(1) é vantagem da matriz, não da lista." (material, p. 28)
- **B) ❌** — Marca a 2ª afirmativa como verdadeira e ignora a assimetria criada pelos arcos direcionados. Segundo o material, esse é "o erro conceitual mais frequente do tópico": achar que o sentido da seta não altera a posição na matriz.
- **C) ❌** — Marca como falsa a 1ª afirmativa, que descreve corretamente a estrutura V×V. Também aceita a 4ª, confundindo o acesso indexado O(1) da matriz com a busca sequencial na lista.
- **D) ❌** — Acerta as duas primeiras, mas inverte as duas últimas: nega a economia de memória da lista em grafos esparsos e aceita a consulta em tempo constante na lista encadeada.

**Conceito-chave para a prova:** Matriz: memória O(V²), teste de aresta O(1), boa para grafos densos; é simétrica só se o grafo for não direcionado. Lista: memória O(V + E), teste de aresta O(grau), boa para grafos esparsos e para percursos (BFS/DFS em O(V + E)).

---

## Q3 — BFS e menor número de arestas
**Fonte:** `Teoria dos Grafos.pdf`, p. 42 (enunciado), p. 43 (gabarito comentado)
**Tipo ENADE:** Asserção-razão

**Enunciado:**
SITUAÇÃO-PROBLEMA
Uma empresa de transporte deseja analisar uma rede de estações representada por um grafo não ponderado, no qual cada vértice representa uma estação e cada aresta representa uma conexão direta entre duas estações.
Para determinar a menor quantidade de conexões necessárias para chegar de uma estação de origem S até uma estação de destino T, um analista decide utilizar o algoritmo Breadth-First Search (BFS).

COMANDO
Considerando o funcionamento da BFS em grafos não ponderados, analise as asserções a seguir.

I. A BFS pode ser utilizada para determinar um caminho entre S e T que contenha o menor número possível de arestas.

PORQUE

II. Durante sua execução, a BFS visita os vértices em níveis de distância crescente a partir da origem, utilizando uma fila para garantir que os vértices descobertos em uma determinada distância sejam processados antes dos vértices de distâncias maiores.

Assinale a alternativa correta.

**Julgamento:**
- **Asserção I — Verdadeira.** Em grafo não ponderado, a BFS calcula o caminho com menos arestas da origem até cada vértice alcançável.
- **Asserção II — Verdadeira.** A BFS usa uma fila (FIFO) e processa os vértices por camadas: primeiro os de distância 1, depois os de distância 2, e assim por diante.
- **Relação — II justifica I.** É justamente a exploração por camadas que garante a propriedade da asserção I: a primeira vez que um vértice é descoberto já corresponde à menor distância em número de arestas (apostila, p. 27).

**Alternativas:**
- **A)** A asserção I é verdadeira, mas a II é falsa, pois a BFS utiliza uma pilha para determinar a ordem de visitação.
- **B)** As asserções I e II são verdadeiras, mas a II não justifica corretamente a I.
- **C)** As asserções I e II são verdadeiras, e a II justifica corretamente a I.
- **D)** A asserção I é falsa, mas a II é verdadeira, pois a BFS não garante o menor número de arestas entre dois vértices.

**Gabarito: C** — _(origem: gabarito do próprio material, p. 43, alternativa C destacada em verde)_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — A II é verdadeira. A BFS usa fila FIFO, e não pilha. Pilha (ou recursão) é característica da DFS.
- **B) ❌** — As duas são verdadeiras, mas a II justifica a I, sim: a exploração em camadas com fila FIFO é o que garante o menor número de arestas.
- **C) ✅** — A BFS explora os vértices em camadas de distância crescente usando uma fila FIFO. Os vértices mais próximos são processados antes dos mais distantes, e por isso o caminho encontrado tem o menor número possível de arestas em um grafo não ponderado.
- **D) ❌** — A I é verdadeira. Em grafo não ponderado, a BFS garante o caminho com o menor número de arestas entre a origem e os demais vértices alcançáveis.

**Conceito-chave para a prova:** BFS = fila e camadas, e dá o caminho mínimo em **número de arestas** só em grafo **não ponderado** (ou com todos os pesos iguais). DFS = pilha ou recursão e **não** garante caminho mínimo. Se uma versão alterada falar em "grafo ponderado" ou "menor custo", a asserção I passa a ser falsa: o algoritmo certo seria Dijkstra (pesos ≥ 0) ou Bellman-Ford (pesos negativos).

---

## Q4 — Dijkstra, Bellman-Ford e Prim
**Fonte:** `Teoria dos Grafos.pdf`, p. 51 (enunciado), p. 52 (gabarito comentado)
**Tipo ENADE:** Associação (resposta única)

**Enunciado:**
SITUAÇÃO-PROBLEMA
Uma equipe de engenharia de software está arquitetando a infraestrutura de rede para um ecossistema de microsserviços em nuvem, semelhante a ambientes AWS com contêineres Docker. Durante o planejamento, os engenheiros de backend identificaram três desafios distintos de otimização de rede que precisam ser resolvidos de forma automatizada:

- **Desafio 1:** Encontrar a rota de menor latência (tempo de resposta) entre o API Gateway (nó de origem) e todos os outros microsserviços da rede. Sabe-se que todos os links possuem latência estritamente positiva.
- **Desafio 2:** Calcular o custo de roteamento de sincronização de um banco de dados relacional distribuído. Devido a acordos de tráfego com provedores, alguns links geram "créditos" de banda, operando efetivamente como arestas de peso negativo. É necessário encontrar o menor custo a partir do nó primário e garantir que não existam ciclos de retroalimentação infinita (ciclos negativos).
- **Desafio 3:** Interligar fisicamente todos os servidores de um novo data center com cabos de fibra óptica. O objetivo não é a velocidade entre dois pontos específicos, mas sim garantir que todos os servidores estejam conectados na mesma rede gastando o mínimo possível em metros de cabo.

COMANDO
Considerando os algoritmos clássicos de otimização em Teoria dos Grafos, assinale a alternativa que indica a escolha tecnicamente correta para resolver os Desafios 1, 2 e 3, respectivamente.

**Alternativas:**
- **A)** 1 - Bellman-Ford; 2 - Dijkstra; 3 - Prim.
- **B)** 1 - Dijkstra; 2 - Bellman-Ford; 3 - Prim.
- **C)** 1 - Dijkstra; 2 - Prim; 3 - Bellman-Ford.
- **D)** 1 - Prim; 2 - Bellman-Ford; 3 - Dijkstra.

**Gabarito: B** — _(origem: gabarito do próprio material, p. 52, alternativa B destacada em verde)_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — O Bellman-Ford até resolve o Desafio 1, mas é menos eficiente: O(V·E), contra O((V+E) log V) do Dijkstra com heap. O erro decisivo está no Desafio 2: Dijkstra não serve com arestas de peso negativo e não detecta ciclos negativos. Ali o correto é Bellman-Ford.
- **B) ✅** — Desafio 1: caminhos mínimos de fonte única com pesos positivos → Dijkstra. Desafio 2: pesos negativos e necessidade de detectar ciclo negativo alcançável → Bellman-Ford, que faz |V|−1 rodadas de relaxamento e mais uma rodada extra; se alguma distância ainda diminuir, existe ciclo negativo. Desafio 3: conectar todos os vértices com custo total mínimo → Árvore Geradora Mínima → Prim.
- **C) ❌** — O Dijkstra no Desafio 1 está certo, mas o Prim no Desafio 2 não: Prim gera uma AGM, não caminhos mínimos, e não detecta ciclos negativos. Além disso, o Bellman-Ford não constrói Árvore Geradora Mínima (Desafio 3).
- **D) ❌** — Usa Prim no Desafio 1. Uma AGM não garante caminhos mínimos a partir de uma origem (apostila, p. 37: "Prim não é Dijkstra"). E usa Dijkstra no Desafio 3, que é um problema de AGM, não de caminho mínimo.

**Conceito-chave para a prova:**
- "A partir de uma origem" com pesos ≥ 0 → **Dijkstra** (guloso, escolhe a menor distância provisória).
- Pesos negativos, "créditos" ou "detectar ciclo negativo" → **Bellman-Ford** (até |V|−1 passadas, O(VE)).
- "Conectar todos com custo mínimo", cabos, sem ciclos → **AGM: Prim** (ou Kruskal, caso apareça numa versão alterada).
- Grafo não ponderado e menor número de saltos → **BFS**.
- Observação técnica que não altera o gabarito: arestas negativas para caminho mínimo pressupõem arcos direcionados, porque em grafo não direcionado uma aresta negativa já forma, sozinha, um ciclo negativo u–v–u.

---

## Q5 — Kuratowski: conclusão sobre planaridade (discursiva)
**Fonte:** `Teoria dos Grafos.pdf`, p. 15 (a mesma ideia é cobrada na Q1 e explicada na apostila, p. 20, item 4.5)
**Tipo ENADE:** Pergunta discursiva curta (com resposta no slide)

**Enunciado:**
[Figura: K5 (pentágono com todas as 10 arestas entre os 5 vértices) e K3,3 (dois grupos de 3 vértices, com cada vértice de um grupo ligado aos 3 do outro, 9 arestas).]
"Um grafo possui uma **estrutura equivalente a uma subdivisão de K5 ou K3,3.** O que podemos concluir sobre sua planaridade?"

**Resposta esperada:** "Ele é não planar." _(resposta dada no próprio slide, p. 15)_
Justificativa: pelo Teorema de Kuratowski, um grafo finito é planar se, e somente se, não contém como subgrafo uma subdivisão de K5 ou de K3,3. Subdividir uma aresta é trocá-la por um caminho, inserindo vértices de grau 2. Portanto, conter um K5 ou K3,3 "disfarçado" já basta para que o grafo seja não planar.

**Conceito-chave para a prova:** Uma subdivisão de K5 ou K3,3 é condição necessária e suficiente para a não planaridade. Um cruzamento num desenho específico não prova nada; o que importa é se existe *algum* desenho sem cruzamentos.

---

## Q6 — Ordem de visita DFS e BFS a partir de A (discursiva)
**Fonte:** `Teoria dos Grafos.pdf`, p. 31 (pergunta); respostas nas p. 33 (DFS), 35 (BFS) e 41 (as duas lado a lado). Versão com um vértice a mais na apostila, p. 26–27 (Figura 11).
**Tipo ENADE:** Pergunta-guia discursiva (rastreamento de algoritmo)

**Enunciado:**
"A PERGUNTA: COMO PERCORRER? A partir de A, qual caminho devemos seguir?"
[Figura (slides p. 30–36 e 41): árvore com 6 vértices. A ligado a B e C; B ligado a D e E; C ligado a F. Arestas: A–B, A–C, B–D, B–E, C–F. Vizinhos considerados em ordem alfabética.]

**Resposta esperada:** _(dada no próprio material)_
- **DFS (profundidade, pilha ou recursão):** A → B → D → E → C → F (p. 33 e 41). Vai até D, volta a B, visita E, volta a A e então segue para C e F. A p. 34 mostra a pilha: [A] → empilha B → empilha D → desempilha D → empilha E...
- **BFS (largura, fila):** A → B → C → D → E → F (p. 35 e 41). Níveis: {A}, {B, C}, {D, E, F}. A p. 36 mostra a fila: B, C, D, E, F.
- Conferido por simulação com vizinhos em ordem alfabética: DFS = A, B, D, E, C, F; BFS = A, B, C, D, E, F. ✅

**Diferenças entre versões:** A apostila (p. 26–27, Figura 11) usa o mesmo grafo **com um vértice extra G ligado a E** (arestas A–B, A–C, B–D, B–E, E–G, C–F). Nela:
- BFS = A, B, C, D, E, F, G, com níveis {A}, {B, C}, {D, E, F}, {G};
- DFS = A, B, D, E, **G**, C, F (G entra logo depois de E, antes de voltar para C).

Conferi as duas ordens. A apostila avisa que outra ordem dos vizinhos na lista de adjacência pode gerar outra sequência válida.

**Conceito-chave para a prova:** DFS aprofunda um ramo inteiro antes de voltar (backtracking). BFS completa um nível inteiro antes de descer. Os dois custam O(V + E) com lista de adjacência e O(V²) com matriz. Na prova, confira qual ordem de vizinhos o enunciado assume (normalmente a alfabética).

---

## Q7 — Número de arestas pela sequência de graus (exemplo resolvido)
**Fonte:** `TEORIA_DOS_GRAFOS - MATERIAL EXPLICATIVO.pdf`, p. 15 (item 3.4 "Exemplo resolvido")
**Tipo ENADE:** Exercício resolvido (cálculo)

**Enunciado:**
"Suponha que uma rede simples tenha seis vértices com graus 3, 2, 4, 1, 2 e 4. Quantas arestas existem?"

**Resposta esperada:** **8 arestas.** _(resolvido no próprio material)_
Σ deg(v) = 3 + 2 + 4 + 1 + 2 + 4 = 16 = 2|E| ⇒ |E| = 8.
Conferência extra: a sequência é realizável como grafo simples. Pelo algoritmo de Havel-Hakimi: 4,4,3,2,2,1 → 3,2,1,1,1 → 1,0,0,1 → 0,0,0. ✅

**Conceito-chave para a prova:** |E| = (soma dos graus)/2. Não é preciso desenhar o grafo.

---

## Q8 — Sequência de graus impossível (exemplo de diagnóstico)
**Fonte:** `TEORIA_DOS_GRAFOS - MATERIAL EXPLICATIVO.pdf`, p. 15 (item 3.6 "Exemplo de diagnóstico"; ver também o item 3.5)
**Tipo ENADE:** Exercício resolvido (diagnóstico)

**Enunciado:**
"Uma pessoa afirma ter construído um grafo simples com cinco vértices cujos graus são 3, 3, 2, 2 e 1. Antes mesmo de desenhar o grafo, podemos testar a consistência da sequência."

**Resposta esperada:** **A sequência é impossível.** _(resolvido no próprio material)_
3 + 3 + 2 + 2 + 1 = 11, que é ímpar. O Handshake Lemma exige soma = 2|E|, que é sempre par. De forma equivalente, há 3 vértices de grau ímpar, e em qualquer grafo não direcionado finito o número de vértices de grau ímpar é par (item 3.5).

**Conceito-chave para a prova:** Uma soma de graus ímpar, ou uma quantidade ímpar de vértices de grau ímpar, torna a sequência impossível. O lema **não** diz que cada vértice tem grau par; diz que a **soma** é par. Em grafo direcionado: Σ grau de saída = Σ grau de entrada = |E| (item 3.7).

---

## Q9 — Não planaridade de K5 e K3,3 pela fórmula de Euler (exemplo de diagnóstico)
**Fonte:** `TEORIA_DOS_GRAFOS - MATERIAL EXPLICATIVO.pdf`, p. 20 (item 4.6 "Exemplo de diagnóstico rápido"; base teórica no item 4.4, p. 19)
**Tipo ENADE:** Exercício resolvido (diagnóstico)

**Enunciado:**
"Considere K₅. Ele possui |V|=5 e |E|=10. [...] Já K₃,₃ possui 6 vértices e 9 arestas [...]" (mostrar que ambos são não planares usando as condições derivadas da fórmula de Euler).

**Resposta esperada:** _(resolvido no próprio material)_
- **K5:** se fosse planar simples com |V| ≥ 3, valeria |E| ≤ 3|V| − 6, ou seja, 10 ≤ 9, o que é falso. Logo, K5 é não planar.
- **K3,3:** a desigualdade geral não o elimina (9 ≤ 3·6 − 6 = 12). Mas ele é bipartido, sem triângulos, e então valeria |E| ≤ 2|V| − 4, ou seja, 9 ≤ 8, o que é falso. Logo, K3,3 é não planar.

Contas conferidas. ✅

**Conceito-chave para a prova:** Fórmula de Euler para grafo planar conexo: V − E + F = 2 (a face externa conta). As desigualdades |E| ≤ 3|V| − 6 (simples) e |E| ≤ 2|V| − 4 (bipartido) são condições **necessárias**: violá-las prova que o grafo não é planar, mas satisfazê-las **não** prova que é planar.

---

## Apêndice — Figuras e exemplos numéricos do material (conferidos)

Estes itens **não são questões**. São as figuras e os exemplos do material, com os dados transcritos e os algoritmos refeitos (também em python), caso a prova use alguma dessas figuras.

| Local | Figura (dados completos) | Resultado no material | Conferência |
|---|---|---|---|
| Slides p. 5–6 | Grafo não dirigido A–B, A–C, B–C, B–D | Graus A=2, B=3, C=2, D=1; soma 8 = 2·4 | ✅ |
| Slides p. 13 | Triângulos A–B–C e 1–2–3 | Isomorfos (A↔1, B↔2, C↔3) | ✅ |
| Slides p. 21 | Não dirigido: A–B, A–C, B–D, B–E, C–D, C–E, D–E | Matriz simétrica (linhas A:01100, B:10011, C:10011, D:01101, E:01110) | ✅ |
| Slides p. 22 | Dirigido: A→B, B→D, C→A, C→E, D→C, D→E, E→D | Matriz assimétrica (A:01000, B:00010, C:10001, D:00101, E:00010) | ✅ |
| Slides p. 23 e p. 46 | Ponderado não dirigido: A–B 8, A–C 4, A–D 10, B–D 3, B–E 6, C–D 5, D–E 7 | Matriz de pesos (a p. 23 usa 0 para "sem aresta"; a p. 46 usa ∞) | ✅. Os slides não calculam Dijkstra para essa figura. Calculado aqui, a partir de A: A=0, C=4, B=8, D=9 (A–C–D), E=14 (A–B–E). AGM (Prim/Kruskal) = B–D 3 + A–C 4 + C–D 5 + B–E 6 = **18** |
| Slides p. 24 | Não dirigido A–B, A–D, B–C, C–D | Lista A:[B,D], B:[A,C], C:[B,D], D:[A,C] | ✅ |
| Slides p. 25 | Dirigido A→B, A→C, A→D, B→C, D→C | Lista A:[B,D,C], B:[C], C:[ ], D:[C] | ✅ |
| Slides p. 47 | Dirigido A→B 4, A→C 5, B→C −2 | Bellman-Ford (sem resultado no slide) | Calculado aqui: d(A)=0, d(B)=4, d(C)=min(5, 4−2)=**2**; sem ciclo negativo |
| Slides p. 49–50 | Não dirigido A–B 2, A–C 4, B–C 1, B–D 5, C–D 3 | Prim a partir de A: A–B(2), B–C(1), C–D(3); A–C descartada (ciclo); **custo 6** | ✅ (Kruskal também dá 6) |
| Apostila p. 4–6, 22–23 (Fig. 1/10) | A–B, A–C, B–C, B–D, C–E | \|V\|=5, \|E\|=5; N(B)={A,C,D}; matriz A:01100, B:10110, C:11001, D:01000, E:00100; lista A:[B,C], B:[A,C,D], C:[A,B,E], D:[B], E:[C] | ✅ |
| Apostila p. 10 (Fig. 4) | G: 1–2, 1–3, 1–4, 2–3, 3–4; H: a–b, a–c, a–d, b–d, c–d | Isomorfos por 1↦a, 2↦b, 3↦d, 4↦c | ✅ (as 5 arestas se correspondem) |
| Apostila p. 13 (Fig. 5) | A–B, A–C, A–D, B–C, B–E, C–D, C–E, D–E | Graus 3,3,4,3,3; soma 16 = 2·8 | ✅ |
| Apostila p. 17 (Fig. 7) | G: A–B, A–C, A–D, B–C, C–D; H: 1–2, 1–3, 1–4, 2–3, 2–4 | Isomorfos por A→1, B→3, C→2, D→4 | ✅ |
| Apostila p. 30–31 (Fig. 12) | Não dirigido: A–B 4, A–C 1, B–C 2, B–D 1, B–E 7, C–D 5, C–E 8, D–E 3 | Dijkstra a partir de A: A=0, C=1 (A–C), B=3 (A–C–B), D=4 (A–C–B–D), E=7 (A–C–B–D–E) | ✅ (ordem de finalização: A, C, B, D, E) |
| Apostila p. 31–32 (Fig. 13) | Dirigido: S→A 4, S→B 5, A→C −3, B→C 6, C→D 2, D→B −1 | Bellman-Ford: S=0, A=4, C=1, D=3, B=2; ciclo B→C→D→B = 6+2−1 = 7 (não negativo) | ✅ |
| Apostila p. 36 (Fig. 14) | Não dirigido: A–B 3, A–C 1, B–C 2, B–D 4, C–D 5, C–E 6, D–E 2, D–F 3, E–F 1 | Prim a partir de A: A–C 1, C–B 2, B–D 4, D–E 2, E–F 1; **peso total 10** | ✅ (Kruskal também dá 10) |
| Apostila p. 24 | Lista ponderada da Fig. 12 | B → [(A,4), (C,2), (D,1), (E,7)] | ✅ |

**Pontos de atenção do material (não afetam nenhum gabarito):**
- ⚠️ Slide p. 37 (tabela DFS vs BFS) marca a BFS com ✗ em "Ordenação topológica". A apostila (p. 28) é mais precisa: "Não na forma básica". O algoritmo de Kahn, que usa fila e graus de entrada, faz ordenação topológica com estratégia em largura. Se a prova afirmar que "somente a DFS permite ordenação topológica", desconfie.
- ⚠️ Os slides p. 23 e p. 46 representam o mesmo grafo ponderado, uma vez com 0 e outra com ∞ para "sem aresta". A apostila (p. 24) alerta que usar 0 é inadequado quando peso zero é permitido.
- Comparações cobradas (slides p. 48 e apostila p. 32 e 37):
  - Dijkstra: guloso, não admite pesos negativos, não detecta ciclo negativo, O((V+E) log V) com heap.
  - Bellman-Ford: relaxa todas as arestas até |V|−1 vezes, admite pesos negativos, detecta ciclo negativo alcançável, O(VE).
  - Prim: AGM, O(E log V) com heap ou O(V²) com matriz, admite pesos negativos. Em grafo desconexo, gera uma floresta geradora mínima.
  - A AGM não garante caminhos mínimos entre pares de vértices.
