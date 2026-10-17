# Teoria dos Grafos — Questões INFERIDAS (prováveis questões do banco do squad que não temos)

> ⚠️ **Atenção:** estas questões NÃO constam nos materiais. Foram elaboradas para cobrir os subtópicos do material do
> Squad 2 que não têm questão conhecida, imitando o estilo das questões do squad. Servem para estudo dirigido.
> As questões reais conhecidas estão em `../questoes_por_topico/09_Teoria_dos_Grafos.md`.

**Base usada:**
- `TEORIA_DOS_GRAFOS - MATERIAL EXPLICATIVO.pdf` (38 p., lido inteiro, com as figuras renderizadas). O Sumário (p. 2) tem 8 Unidades:
  1. Definição de Grafos, Vértices e Arestas (p. 3–6)
  2. Funções Sobrejetora, Injetora e Bijetora (p. 7–11)
  3. Handshake Lemma (p. 12–15)
  4. Planaridade, Isomorfismo e Teorema de Kuratowski (p. 16–20)
  5. Matriz e Lista de adjacência (p. 21–24)
  6. DFS e BFS (p. 25–28)
  7. Dijkstra e Bellman-Ford (p. 29–33)
  8. Prim (p. 34–37)
- `Teoria dos Grafos.pdf` (54 slides, lidos inteiros, com as páginas-imagem renderizadas). A "MATRIZ CURRICULAR" (p. 2) tem 4 capítulos:
  - Cap. 1 — Fundamentos e Propriedades: vértices, arestas, funções, Handshake, planaridade e isomorfismo
  - Cap. 2 — Representação Computacional: matriz e lista de adjacência
  - Cap. 3 — Algoritmos de Percurso: DFS, BFS e conectividade
  - Cap. 4 — Algoritmos de Otimização: Dijkstra, Bellman-Ford e Prim
- `Estrutura de Questões sob o padrão do ENADE.pdf` (guia do professor). O prompt-modelo pede "4 alternativas de resposta, sendo uma correta e três distratores plausíveis", com justificativa de cada alternativa.

**Estilo identificado do squad (Q1–Q4 dos slides):**
- Questões no formato **SITUAÇÃO-PROBLEMA → COMANDO → ALTERNATIVAS**, sempre com **4 alternativas (A–D)**.
- Uma questão por capítulo. O gabarito vem comentado alternativa por alternativa ("Incorreta porque...").
- Os contextos são de computação: rede de comunicação, módulo de rotas, rede de estações, microsserviços em nuvem.
- Tipos que o squad já usou: resposta única/interpretação (Q1), V/F em sequência (Q2), asserção-razão (Q3) e associação (Q4).
- Nas questões inferidas variei os tipos, acrescentando os que o squad ainda não usou: afirmativas múltiplas, afirmativa negativa ("INCORRETA"), lacunas, afirmativa incompleta e ordenação.
- Os grafos usados são os do próprio material, quase sempre as figuras sem resolução nos slides ou as figuras resolvidas na apostila. Todo grafo está descrito por completo (vértices, arestas e pesos).
- Todos os gabaritos foram conferidos com python3 (scripts em `/tmp/agent_work/grafos2_py/`).

**Fora do material (sem questão inferida):** o material não traz Kruskal, caminhos/circuitos de Euler e Hamilton, coloração, nem árvores como unidade própria (só aparece a árvore geradora, na Unidade 8). "Euler" no material é apenas a fórmula V − E + F = 2. A ordenação topológica não tem unidade própria, mas aparece nos slides p. 37, 38 e 40 e na apostila p. 28, por isso entrou.

## Mapa de cobertura
| # | Subtópico (material) | Páginas | Questão conhecida | Questão inferida | Prioridade |
|---|---|---|---|---|---|
| 1 | Definição G=(V,E), ordem e tamanho, modelagem, adjacência, incidência, vizinhança N(v), grafo simples, direcionado × não direcionado | Apostila U1 p. 3–6; slides p. 4 | — | **I1** | Média |
| 2 | Funções: definição e regras fundamentais (domínio, contradomínio, imagem); injetora, sobrejetora e bijetora; teste de classificação; inversa e \|A\| = \|B\| | Apostila U2 p. 7–11; slides p. 7–12 | — | **I2**, **I3** (2 questões: tema de 6 slides + unidade inteira + tabela-resumo) | Alta |
| 3 | Handshake Lemma (Σ graus = 2\|E\|) | Apostila 3.1–3.4 p. 13–15; slides p. 5–6 | Q1 (+ exemplo Q7) | — (variação provável: dada uma sequência de graus, calcular \|E\|) | — |
| 4 | Consequência: o nº de vértices de grau ímpar é par; sequência de graus impossível | Apostila 3.5–3.6 p. 15 | Q8 (exemplo discursivo); Q1-C toca no tema | — (variação: "3, 3, 2, 2, 1 é realizável?" → não, a soma é 11) | — |
| 5 | Handshake em grafo direcionado (Σ deg⁺ = Σ deg⁻ = \|E\|) | Apostila 3.7 p. 15 | — | **I7** (agrupado com a matriz de grafo direcionado) | Média |
| 6 | Isomorfismo: bijeção que preserva adjacências | Apostila 2.6 p. 10 (Fig. 4), 4.1 p. 17 (Fig. 7); slides p. 13 | — | **I4** | Alta |
| 7 | Invariantes do isomorfismo (são necessários, mas não suficientes) | Apostila 4.2 p. 17–18 ("Importante") | — | **I5** | Média |
| 8 | Planaridade como propriedade do grafo, não do desenho (K4 "cruzado") | Apostila 4.3 p. 18; slides p. 14 | Q1 (alternativa A), Q5 | — (variação: "um desenho com cruzamento prova não planaridade?" → não) | — |
| 9 | Fórmula de Euler V − E + F = 2 e as desigualdades \|E\| ≤ 3\|V\|−6 e \|E\| ≤ 2\|V\|−4 | Apostila 4.4 e 4.6 p. 19–20 (tabela + "Não confunda") | Q9 (exemplo discursivo, só as desigualdades) | **I6** | Média |
| 10 | K5, K3,3 e Teorema de Kuratowski | Apostila 4.5 p. 19–20; slides p. 15 | Q1, Q5 | — | — |
| 11 | Matriz × lista: memória, teste de aresta, grafos densos/esparsos, (as)simetria | Apostila 5.1–5.4 p. 22–24; slides p. 20–26 | Q2 | — (variação: enumerar vizinhos custa O(\|V\|) na matriz e O(deg) na lista) | — |
| 12 | Construir e ler a matriz e a lista de um grafo direcionado (linha = saída, coluna = entrada) | Apostila 5.2–5.3 p. 22–23; slides p. 22 e 25 | — (Q2 é só conceitual) | **I7** | Média |
| 13 | Grafos ponderados: matriz de pesos (0 × ∞), lista de pares (vizinho, peso), 2\|E\| entradas na lista | Apostila 5.3 e 5.5 p. 23–24; slides p. 23 e 46 | — | **I8** | Baixa |
| 14 | BFS: fila, níveis, menor caminho em nº de arestas | Apostila 6.2 p. 26–27; slides p. 32, 35–36 | Q3 | — | — |
| 15 | DFS: pilha/recursão, backtracking, ordem de visita (DFS × BFS no mesmo grafo) | Apostila 6.1 e 6.3 p. 26–27 (Fig. 11); slides p. 30–34, 37, 41 | Q6 (só discursiva) | **I9** | Alta |
| 16 | Conectividade (componentes), detecção de ciclos (aresta de retorno), complexidade O(V+E) × O(V²) | Apostila 6.4–6.5 p. 27–28; slides p. 37–39 | — | **I10** | Alta |
| 17 | Ordenação topológica em DAG (pós-ordem invertida da DFS) | Apostila 6.4 p. 28; slides p. 37, 38, 40 | — | **I11** | Média |
| 18 | Relaxamento e execução do Dijkstra | Apostila 7.1–7.2 p. 30–31 (Fig. 12); slides p. 46 | — (Q4 só pede a escolha do algoritmo) | **I12** | Alta |
| 19 | Bellman-Ford: \|V\|−1 rodadas, rodada extra, ciclo negativo | Apostila 7.3 p. 31–32 (Fig. 13); slides p. 47 | — (Q4 só pede a escolha) | **I13** | Média |
| 20 | Dijkstra × Bellman-Ford: quando usar cada um | Apostila 7.4 p. 32; slides p. 48 | Q4 | — (variação: complexidades O((V+E) log V) × O(VE)) | — |
| 21 | AGM e execução do Prim (propriedade do corte) | Apostila 8.1–8.3 p. 35–36 (Fig. 14); slides p. 49–50 | — (Q4 só pede a escolha) | **I14** | Alta |
| 22 | "Prim não é Dijkstra"; a AGM não garante caminho mínimo; \|V\|−1 arestas; floresta geradora; pesos negativos | Apostila 8.1, 8.4–8.5 p. 35–37 | Q4-D toca no tema | **I15** | Média |

**Resumo:**
- 22 subtópicos no total.
- 7 já cobertos por questões conhecidas: #3, #4, #8, #10, #11, #14 e #20.
- 15 subtópicos sem questão objetiva conhecida, cobertos por **15 questões inferidas (I1–I15)**:
  - o subtópico #2 ganhou duas questões (I2 e I3);
  - os subtópicos #5 e #12 foram agrupados na I7.
- Gabaritos: **A = 4** (I4, I8, I10, I14), **B = 4** (I1, I7, I9, I15), **C = 4** (I5, I6, I11, I13), **D = 3** (I2, I3, I12).

## Índice
1. [I1 — Definição de grafo, adjacência, incidência e vizinhança](#i1--definição-de-grafo-adjacência-incidência-e-vizinhança)
2. [I2 — Classificação de funções injetora, sobrejetora e bijetora](#i2--classificação-de-funções-injetora-sobrejetora-e-bijetora)
3. [I3 — Função não injetora e não sobrejetora, bijeção e inversa](#i3--função-não-injetora-e-não-sobrejetora-bijeção-e-inversa)
4. [I4 — Isomorfismo por bijeção que preserva adjacências](#i4--isomorfismo-por-bijeção-que-preserva-adjacências)
5. [I5 — Invariantes de isomorfismo](#i5--invariantes-de-isomorfismo)
6. [I6 — Fórmula de Euler e condições necessárias de planaridade](#i6--fórmula-de-euler-e-condições-necessárias-de-planaridade)
7. [I7 — Matriz de adjacência de grafo direcionado e graus de entrada e saída](#i7--matriz-de-adjacência-de-grafo-direcionado-e-graus-de-entrada-e-saída)
8. [I8 — Representação de grafos ponderados](#i8--representação-de-grafos-ponderados)
9. [I9 — Ordem de visita DFS e BFS](#i9--ordem-de-visita-dfs-e-bfs)
10. [I10 — Conectividade, componentes e detecção de ciclos](#i10--conectividade-componentes-e-detecção-de-ciclos)
11. [I11 — Ordenação topológica em DAG](#i11--ordenação-topológica-em-dag)
12. [I12 — Execução do Dijkstra](#i12--execução-do-dijkstra)
13. [I13 — Execução do Bellman-Ford e ciclo negativo](#i13--execução-do-bellman-ford-e-ciclo-negativo)
14. [I14 — Execução do Prim](#i14--execução-do-prim)
15. [I15 — Prim não é Dijkstra](#i15--prim-não-é-dijkstra)

---

## I1 — Definição de grafo, adjacência, incidência e vizinhança
**Subtópico coberto:** Unidade 1: definição G=(V,E), ordem e tamanho, adjacência, incidência, vizinhança, grafo simples, direcionado × não direcionado (apostila p. 4–6; slides p. 4).
**Por que é provável:** "Vértices, arestas" é o primeiro item do Capítulo 1 na matriz curricular, e a apostila dedica a ele a Unidade 1 inteira, com um exemplo de servidores S1–S4 (item 1.6) já em formato de enunciado. A Q1 conhecida não cobra nenhum desses conceitos.
**Prioridade:** Média
**Tipo ENADE:** Afirmativas múltiplas

**Enunciado:**
SITUAÇÃO-PROBLEMA
Uma equipe de infraestrutura precisa documentar a topologia de um pequeno cluster antes de automatizar seu monitoramento. Para isso, modela os quatro servidores como vértices e as conexões físicas diretas entre eles como arestas de um grafo simples não direcionado G = (V, E).

DADOS DE SUPORTE
V = {S1, S2, S3, S4}
E = {{S1,S2}, {S1,S3}, {S2,S3}, {S3,S4}}
[Grafo: triângulo S1–S2–S3 com o vértice S4 ligado apenas a S3 (aresta S3–S4). São 4 vértices e 4 arestas, sem pesos.]
"Em um grafo simples, não há laços e não há arestas paralelas entre o mesmo par de vértices." (com base em ROSEN, 2019)

COMANDO
Considerando os conceitos de ordem, tamanho, adjacência, incidência, vizinhança e orientação das arestas, avalie as afirmações a seguir.

I. O grafo tem ordem |V| = 4 e tamanho |E| = 4, e a aresta {S3,S4} é incidente aos vértices S3 e S4.

II. A vizinhança de S3 é N(S3) = {S1, S2, S4}; S1 e S2 têm S3 como vizinho comum; e S4 possui uma única conexão direta.

III. Para registrar dois cabos redundantes entre S1 e S2, basta incluir a aresta {S1,S2} duas vezes em E, e G continua sendo um grafo simples.

IV. Se a relação modelada passar a ser "Si replica dados para Sj", que nem sempre é recíproca, o modelo adequado é um grafo direcionado, no qual (S1,S2) e (S2,S1) podem representar relações diferentes.

É correto o que se afirma em

**Julgamento das afirmativas:**
- **I — Verdadeira.** A ordem é a quantidade de vértices (4) e o tamanho é a quantidade de arestas (4). Uma aresta é incidente aos vértices de suas extremidades.
- **II — Verdadeira.** S3 é adjacente a S1, S2 e S4. S1 e S2 compartilham o vizinho S3. S4 só aparece na aresta {S3,S4}, logo tem grau 1 (apostila p. 6: "S4 possui apenas uma conexão direta; S1 e S2 compartilham um vizinho").
- **III — Falsa.** Duas arestas entre o mesmo par de vértices são arestas paralelas, o que já não é permitido em grafo simples (o resultado seria um multigrafo). Além disso, E é um conjunto: repetir {S1,S2} não cria uma segunda aresta.
- **IV — Verdadeira.** Relação com sentido pede grafo direcionado: "A segue B" não implica "B segue A", e (u,v) e (v,u) podem representar relações diferentes (apostila p. 5–6).

**Alternativas:**
- **A)** I e III, apenas.
- **B)** I, II e IV, apenas.
- **C)** II e III, apenas.
- **D)** III e IV, apenas.

**Gabarito: B**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Inclui a III, que é falsa (arestas paralelas não existem em grafo simples), e deixa de fora a II e a IV, que são verdadeiras.
- **B) ✅** — I, II e IV estão corretas pelas definições de ordem, tamanho, incidência, vizinhança e orientação. A III viola a definição de grafo simples.
- **C) ❌** — A II está certa, mas a III não. Também omite a I e a IV, que são verdadeiras.
- **D) ❌** — A IV está certa, mas a III é falsa. Também omite a I e a II.

**Base no material:** apostila p. 4–6, itens 1.2 (definição formal, ordem |V| e tamanho |E|), 1.4 (direcionado × não direcionado), 1.5 (adjacência, incidência, N(v), grafo simples sem laços nem arestas paralelas) e 1.6 (exemplo S1–S4).
**Conceito-chave para a prova:**
- Ordem = |V|; tamanho = |E|.
- Adjacência é uma relação entre vértices; incidência é uma relação entre uma aresta e os vértices de suas extremidades.
- Grafo simples não tem laços nem arestas paralelas.
- Relação com sentido pede grafo direcionado.

---

## I2 — Classificação de funções injetora, sobrejetora e bijetora
**Subtópico coberto:** Unidade 2: definição de função, regras fundamentais e classificação (apostila p. 8–10; slides p. 7–12).
**Por que é provável:** "funções" aparece explicitamente na matriz curricular do Capítulo 1. O tema ocupa 6 slides (p. 7–12), com a tabela-resumo "Injetora, Sobrejetora e Bijetora", e uma unidade inteira da apostila, com os exemplos numéricos usados aqui (p. 9). Nenhuma questão conhecida cobra o tema.
**Prioridade:** Alta
**Tipo ENADE:** Associação

**Enunciado:**
SITUAÇÃO-PROBLEMA
Durante a revisão de um módulo de integração, uma desenvolvedora encontrou quatro correspondências entre conjuntos usadas para mapear identificadores internos (domínio) em códigos externos (contradomínio). Antes de usá-las como base para uma tabela de conversão reversível, ela precisa classificá-las.

DADOS DE SUPORTE
- **P:** A = {1, 2, 3} → B = {a, b, c, d}, com 1 → a, 2 → b, 3 → c.
- **Q:** A = {1, 2, 3, 4} → B = {a, b, c}, com 1 → a, 2 → b, 3 → c, 4 → c.
- **R:** A = {1, 2, 3} → B = {a, b, c}, com 1 → b, 2 → c, 3 → a.
- **S:** A = {1, 2, 3} → B = {a, b, c}, com 1 → a, 1 → b, 3 → c (o elemento 2 não tem seta).

Classificações:
1. Função injetora, mas não sobrejetora.
2. Função sobrejetora, mas não injetora.
3. Função bijetora.
4. Não é função.

COMANDO
Assinale a alternativa que associa corretamente cada correspondência à sua classificação.

**Alternativas:**
- **A)** P–3; Q–2; R–1; S–4.
- **B)** P–1; Q–4; R–3; S–2.
- **C)** P–2; Q–1; R–3; S–4.
- **D)** P–1; Q–2; R–3; S–4.

**Gabarito: D**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Classifica P como bijetora só porque nenhuma imagem se repete. Mas "d" não é atingido, então P não é sobrejetora. Também classifica R como apenas injetora, quando todo elemento de B é atingido exatamente uma vez.
- **B) ❌** — Diz que Q "não é função" porque 3 e 4 têm a mesma imagem. Repetir imagem é permitido: "vários elementos de A podem apontar para o mesmo elemento de B" (slides p. 8). Também diz que S é sobrejetora por atingir a, b e c. Mas S nem é função: o elemento 1 tem duas imagens e o elemento 2 não tem nenhuma.
- **C) ❌** — Inverte as definições. P (sem colisão, com sobra em B) é injetora. Q (com colisão, sem sobra em B) é sobrejetora.
- **D) ✅** — P: nenhuma colisão e "d" sobra → injetora, não sobrejetora. Q: 3 e 4 colidem em "c", mas todo B é atingido → sobrejetora, não injetora. R: correspondência um a um, sem colisão e sem sobra → bijetora. S: viola as duas regras fundamentais ("todo elemento de A precisa ter uma seta" e "um elemento de A não pode apontar para dois elementos diferentes de B") → não é função. Conferido com python3.

**Base no material:**
- Apostila p. 9: os exemplos "A={1,2,3}, B={a,b,c,d}" (injetora, não sobrejetora) e "A={1,2,3,4}, B={a,b,c}, f(4)=c" (sobrejetora, não injetora); tabela "Pode repetir imagem? / Pode sobrar elemento em B?".
- Apostila p. 10: roteiro de teste (item 2.5).
- Slides p. 8: as três correspondências das "Regras Fundamentais", entre elas a correspondência S.
- Slides p. 12: tabela-resumo.

**Conceito-chave para a prova:**
- Injetora: proíbe colisão; pode sobrar elemento em B.
- Sobrejetora: proíbe sobra em B; pode haver colisão.
- Bijetora: nenhuma colisão e nenhuma sobra.
- Antes de classificar, confira se é função: cada elemento do domínio deve ter exatamente uma imagem.

---

## I3 — Função não injetora e não sobrejetora, bijeção e inversa
**Subtópico coberto:** Unidade 2: teste de injeção e sobrejeção, bijeção entre conjuntos finitos (|A| = |B|) e função inversa (apostila p. 9–10).
**Por que é provável:** a apostila destaca que "uma bijeção entre A e B implica |A| = |B|" e que "toda função bijetora possui inversa". O prompt-modelo do professor (`Estrutura de Questões sob o padrão do ENADE.pdf`, p. 26) usa justamente "Matemática Discreta / teoria dos conjuntos" como exemplo, e o tema tem peso grande no Capítulo 1.
**Prioridade:** Média
**Tipo ENADE:** Afirmativa negativa (INCORRETA)

**Enunciado:**
SITUAÇÃO-PROBLEMA
O sistema de agendamento de uma universidade associa cada reserva do conjunto R = {r1, r2, r3, r4} a uma sala do conjunto S = {s1, s2, s3} por meio da função f: R → S. A equipe de desenvolvimento quer saber se essa associação pode ser invertida, isto é, se a partir de uma sala é possível recuperar uma única reserva.

DADOS DE SUPORTE
f(r1) = s1, f(r2) = s2, f(r3) = s1, f(r4) = s2.
"Se os conjuntos são finitos, uma bijeção entre A e B implica |A| = |B|. Além disso, toda função bijetora possui função inversa f⁻¹: B → A." (com base em ROSEN, 2019)

COMANDO
Com base nos conceitos de função injetora, sobrejetora e bijetora, assinale a alternativa **INCORRETA**.

**Alternativas:**
- **A)** f é uma função, pois cada reserva do domínio R está associada a exatamente uma sala de S.
- **B)** f não é injetora, pois as reservas distintas r1 e r3 possuem a mesma imagem, s1.
- **C)** f não é sobrejetora, pois sua imagem é {s1, s2} e a sala s3 não é atingida.
- **D)** Trocando apenas f(r4) para s3, f passaria a ser bijetora e admitiria inversa f⁻¹: S → R.

**Gabarito: D**

**Por que cada alternativa está certa ou errada:**
- **A) ❌ (afirmação correta)** — Cada elemento do domínio tem exatamente uma imagem. Repetir imagens não impede que seja função.
- **B) ❌ (afirmação correta)** — f(r1) = f(r3) = s1 com r1 ≠ r3. É uma colisão, logo f não é injetora (o mesmo vale para r2 e r4 em s2).
- **C) ❌ (afirmação correta)** — A imagem é {s1, s2} ≠ S. A sala s3 fica sem seta, logo f não é sobrejetora. Ou seja, f não é nem injetora nem sobrejetora.
- **D) ✅ (afirmação INCORRETA)** — Com f(r4) = s3, a função passa a ser sobrejetora, porque s1, s2 e s3 são atingidas. Mas r1 e r3 continuam colidindo em s1, então ela segue não injetora e, portanto, não bijetora. Na verdade, nenhuma f: R → S pode ser bijetora, porque |R| = 4 ≠ |S| = 3. Sem bijeção, não existe inversa. Conferido com python3.

**Base no material:** apostila p. 9–10: itens 2.2–2.4 (definições; "Bijetora = Injetora + Sobrejetora"; "uma bijeção entre A e B implica |A| = |B|"; "toda função bijetora possui função inversa") e item 2.5 (roteiro: procurar colisões e elementos não atingidos).
**Conceito-chave para a prova:** Em conjuntos finitos, uma bijeção exige |A| = |B|. Se |A| > |B|, nenhuma função de A em B é injetora (há colisão garantida). Corrigir a sobrejeção não corrige a injeção.

---

## I4 — Isomorfismo por bijeção que preserva adjacências
**Subtópico coberto:** Unidade 4: isomorfismo (apostila p. 10, Fig. 4; p. 17, Fig. 7; slides p. 13).
**Por que é provável:** "isomorfismo" está na matriz curricular do Capítulo 1, e a apostila traz duas figuras de pares de grafos isomorfos com a bijeção dada (Fig. 4 e Fig. 7). A Q1 conhecida cobra Handshake e planaridade, mas não isomorfismo.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única

**Enunciado:**
SITUAÇÃO-PROBLEMA
Duas equipes desenharam, de forma independente, o diagrama de comunicação entre quatro microsserviços. A equipe 1 nomeou os serviços com letras (grafo G) e a equipe 2 com números (grafo H). Os desenhos parecem diferentes, e o arquiteto quer saber se representam a mesma estrutura de conexões.

DADOS DE SUPORTE
- **Grafo G** (não direcionado, sem pesos): V(G) = {A, B, C, D}; E(G) = {A–B, A–C, A–D, B–C, C–D}.
  [Desenho: quadrado com A no canto superior esquerdo, B no superior direito, C no inferior direito e D no inferior esquerdo. Os lados são A–B, B–C, C–D e D–A, mais a diagonal A–C.]
- **Grafo H** (não direcionado, sem pesos): V(H) = {1, 2, 3, 4}; E(H) = {1–2, 1–3, 1–4, 2–3, 2–4}.
  [Desenho: triângulo com 1 no topo, 3 embaixo à esquerda e 2 embaixo à direita (arestas 1–3, 3–2, 1–2), e o vértice 4 no interior, ligado a 1 e a 2.]
- "f: V(G) → V(H) é uma bijeção que preserva adjacências: {u,v} ∈ E(G) ⇔ {f(u),f(v)} ∈ E(H)." (BONDY; MURTY, 2008)

COMANDO
Assinale a alternativa que apresenta uma bijeção f: V(G) → V(H) que comprova que G e H são isomorfos.

**Alternativas:**
- **A)** f(A)=1, f(B)=3, f(C)=2, f(D)=4.
- **B)** f(A)=1, f(B)=2, f(C)=3, f(D)=4.
- **C)** f(A)=3, f(B)=1, f(C)=4, f(D)=2.
- **D)** f(A)=1, f(B)=3, f(C)=4, f(D)=2.

**Gabarito: A**

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — As cinco arestas de G são levadas em arestas de H: A–B→1–3 ✓, A–C→1–2 ✓, A–D→1–4 ✓, B–C→3–2 ✓, C–D→2–4 ✓. Os graus também batem: A e C têm grau 3 e vão para 1 e 2, que têm grau 3. B e D têm grau 2 e vão para 3 e 4, que têm grau 2. É a correspondência da própria apostila (p. 17).
- **B) ❌** — É a associação "na ordem", sem checar a estrutura. A aresta C–D seria levada em 3–4, que não existe em H. Além disso, B, de grau 2, iria para 2, de grau 3.
- **C) ❌** — Manda A, de grau 3, para 3, de grau 2. A aresta A–C seria levada em 3–4, que não existe em H.
- **D) ❌** — Manda C, de grau 3, para 4, de grau 2. A aresta B–C seria levada em 3–4, que não existe em H.

Conferido com python3: apenas a alternativa A preserva as arestas. Existem 4 bijeções válidas no total ({A,C}→{1,2} e {B,D}→{3,4}), e só uma delas aparece entre as alternativas.

**Base no material:** apostila p. 17, item 4.1 e Figura 7 (G: A–B, A–C, A–D, B–C, C–D; H: 1–2, 1–3, 1–4, 2–3, 2–4; "a correspondência A→1, B→3, C→2 e D→4 preserva todas as cinco arestas"). Também a apostila p. 10 (item 2.6, "a bijeção é a base para formalizar isomorfismos") e os slides p. 13.
**Conceito-chave para a prova:**
- Isomorfismo é uma bijeção que leva aresta em aresta e não aresta em não aresta.
- Atalho: vértices só podem ser associados a vértices de mesmo grau.
- Depois, teste aresta por aresta. Uma única aresta que falhe derruba a bijeção.

---

## I5 — Invariantes de isomorfismo
**Subtópico coberto:** Unidade 4, item 4.2: invariantes úteis no diagnóstico de isomorfismo (apostila p. 17–18).
**Por que é provável:** a apostila tem uma caixa "Importante" dizendo que ter os mesmos |V|, |E| e a mesma sequência de graus "é necessário, mas não é suficiente". É a "pegadinha" clássica do tema e combina com o formato asserção-razão que o squad já usou (Q3).
**Prioridade:** Média
**Tipo ENADE:** Asserção-razão

**Enunciado:**
SITUAÇÃO-PROBLEMA
Uma empresa possui duas filiais, cada uma com seis roteadores. Um analista comparou as topologias e notou que ambas têm 6 roteadores e 6 links, e que todos os roteadores têm exatamente 2 links. Ele então registrou no relatório que as duas redes "têm a mesma estrutura".

DADOS DE SUPORTE
- **Rede X:** V = {X1, X2, X3, X4, X5, X6}; E = {X1–X2, X2–X3, X3–X4, X4–X5, X5–X6, X6–X1}. É um único ciclo com os 6 vértices.
- **Rede Y:** V = {Y1, Y2, Y3, Y4, Y5, Y6}; E = {Y1–Y2, Y2–Y3, Y3–Y1, Y4–Y5, Y5–Y6, Y6–Y4}. São dois triângulos separados, sem link entre eles.

[As duas redes são grafos não direcionados e sem pesos.]

COMANDO
Considerando o conceito de isomorfismo de grafos e seus invariantes, avalie as asserções a seguir e a relação proposta entre elas.

I. As redes X e Y são isomorfas, pois possuem o mesmo número de vértices, o mesmo número de arestas e a mesma sequência de graus (2, 2, 2, 2, 2, 2).

PORQUE

II. Ter os mesmos valores de |V|, |E| e a mesma sequência de graus é condição necessária, mas não suficiente, para que dois grafos sejam isomorfos.

Assinale a alternativa correta.

**Julgamento:**
- **Asserção I — Falsa.** O número de componentes conexas é um invariante: todo isomorfismo o preserva. X é conexa (1 componente) e Y tem 2 componentes. Outro invariante que difere é a quantidade de triângulos: X tem 0 e Y tem 2. Logo, não existe bijeção que preserve adjacências.
- **Asserção II — Verdadeira.** É exatamente o que diz a caixa "Importante" da apostila (p. 18). Os invariantes servem para descartar candidatos, e o critério decisivo é a bijeção.
- **Relação:** como a I é falsa, não há justificativa a avaliar. Note que a II, na verdade, explica por que a conclusão da I é inválida.

**Alternativas:**
- **A)** As asserções I e II são verdadeiras, e a II justifica corretamente a I.
- **B)** A asserção I é verdadeira, mas a II é falsa, pois a mesma sequência de graus garante o isomorfismo.
- **C)** A asserção I é falsa, e a II é verdadeira, pois Y tem duas componentes conexas e X apenas uma.
- **D)** As asserções I e II são verdadeiras, mas a II não justifica corretamente a I.

**Gabarito: C**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — A I é falsa. Mesmo |V|, |E| e mesma sequência de graus não garantem isomorfismo, como a própria II afirma.
- **B) ❌** — Inverte a avaliação. A II é verdadeira, e a ideia de que "a mesma sequência de graus garante o isomorfismo" é justamente o erro que a apostila aponta.
- **C) ✅** — A I é falsa, porque as redes diferem num invariante preservado por qualquer isomorfismo (componentes conexas: 1 × 2). A II é verdadeira. Conferido com python3: nenhuma das 720 bijeções preserva as arestas.
- **D) ❌** — Considera a I verdadeira, mas X e Y não são isomorfas.

**Base no material:** apostila p. 17–18, item 4.2: a lista de invariantes (|V|, |E|, sequência de graus, "quantidade de componentes conexas", "existência e quantidade de estruturas específicas, como triângulos") e a caixa "Importante: ... é necessário, mas não é suficiente".
**Conceito-chave para a prova:** Se um invariante difere, os grafos com certeza não são isomorfos. Se todos os invariantes coincidem, ainda não se pode concluir nada: é preciso exibir a bijeção.

---

## I6 — Fórmula de Euler e condições necessárias de planaridade
**Subtópico coberto:** Unidade 4, itens 4.4 e 4.6: fórmula de Euler e as desigualdades |E| ≤ 3|V| − 6 e |E| ≤ 2|V| − 4 (apostila p. 19–20).
**Por que é provável:** a apostila traz uma tabela-resumo com as três condições e a caixa "Não confunda" ("satisfazer a desigualdade não garante planaridade"). A Q1 conhecida usa exatamente 10 vértices e 15 arestas, os números em que a desigualdade é satisfeita e mesmo assim o grafo é não planar. A Q9 só traz o exemplo discursivo de K5 e K3,3.
**Prioridade:** Média
**Tipo ENADE:** Afirmativas múltiplas

**Enunciado:**
SITUAÇÃO-PROBLEMA
Uma empresa de hardware projeta placas de circuito impresso de uma única camada, nas quais as trilhas não podem se cruzar. Cada circuito é modelado como um grafo simples, com os componentes como vértices e as trilhas como arestas, e só pode ser fabricado nessa placa se o grafo for planar. Antes de tentar desenhar os circuitos, a equipe analisou quatro deles usando apenas suas contagens.

DADOS DE SUPORTE
- Fórmula de Euler, para grafo planar conexo: |V| − |E| + |F| = 2 (a face externa também conta).
- Condições necessárias (WEST, 2001):
  - grafo planar simples com |V| ≥ 3 ⇒ |E| ≤ 3|V| − 6;
  - grafo planar e bipartido com |V| ≥ 3 ⇒ |E| ≤ 2|V| − 4.

COMANDO
Avalie as afirmações a seguir.

I. O circuito P é conexo e planar e tem 8 vértices e 12 arestas. Em qualquer desenho sem cruzamentos, o plano fica dividido em 6 faces, contando a externa.

II. O circuito Q tem 10 vértices e 15 arestas. Como 15 ≤ 3·10 − 6 = 24, conclui-se que Q é planar e pode ser fabricado na placa.

III. O circuito R tem 6 vértices e 13 arestas. Mesmo sem desenhá-lo, conclui-se que R não é planar, pois 13 > 3·6 − 6 = 12.

IV. O circuito T é bipartido e tem 6 vértices e 9 arestas. Embora satisfaça 9 ≤ 3·6 − 6 = 12, T não é planar, pois 9 > 2·6 − 4 = 8.

É correto o que se afirma em

**Julgamento das afirmativas:**
- **I — Verdadeira.** 8 − 12 + F = 2 ⇒ F = 6. Exemplo: o grafo do cubo tem 8 vértices, 12 arestas e 6 faces.
- **II — Falsa.** A desigualdade é só condição **necessária**: satisfazê-la não prova planaridade. Contraexemplo: o grafo de Petersen tem 10 vértices e 15 arestas, contém uma subdivisão de K3,3 e é não planar. É exatamente a situação da Q1 conhecida.
- **III — Verdadeira.** 13 > 12 viola uma condição necessária, logo R não pode ser planar. Esse grafo existe, pois um grafo simples com 6 vértices admite até 15 arestas.
- **IV — Verdadeira.** Grafo bipartido não tem triângulos, então vale a condição mais forte |E| ≤ 2|V| − 4 = 8, e 9 > 8. (Com 6 vértices e 9 arestas, o único bipartido possível é o próprio K3,3.)

**Alternativas:**
- **A)** I e II, apenas.
- **B)** II e IV, apenas.
- **C)** I, III e IV, apenas.
- **D)** I, II, III e IV.

**Gabarito: C**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Aceita a II, que trata uma condição necessária como se fosse suficiente. E omite a III e a IV, que são verdadeiras.
- **B) ❌** — Aceita a II e omite a I (aplicação direta de Euler) e a III.
- **C) ✅** — A I aplica a fórmula de Euler corretamente. A III e a IV usam a violação de uma condição necessária para provar não planaridade. A II é a falácia "satisfaz, logo é planar".
- **D) ❌** — Inclui a II, que é falsa.

**Base no material:** apostila p. 19, item 4.4 (fórmula, tabela "Situação / Condição necessária / Uso", caixa "Não confunda"), e p. 20, item 4.6 (K5: 10 ≤ 9 é falso; K3,3: 9 ≤ 8 é falso). Contas conferidas com python3.
**Conceito-chave para a prova:**
- Violar |E| ≤ 3|V| − 6 (ou |E| ≤ 2|V| − 4 em bipartido) prova que o grafo é não planar.
- Satisfazer essas desigualdades não prova nada. Quem caracteriza a planaridade é Kuratowski.
- F = 2 − |V| + |E|, e a face externa conta.

---

## I7 — Matriz de adjacência de grafo direcionado e graus de entrada e saída
**Subtópico coberto:** Unidade 5, itens 5.2–5.3 (construção e leitura de matriz e lista; grafo direcionado), agrupado com a Unidade 3, item 3.7 (Handshake em grafo direcionado). Apostila p. 15 e 22–23; slides p. 22 e 25.
**Por que é provável:** o slide p. 22 mostra a matriz de um grafo direcionado sem nenhuma pergunta sobre ela, e o gabarito da Q2 diz que confundir simetria em grafo direcionado é "o erro conceitual mais frequente do tópico". A Q2 conhecida é só conceitual: nenhuma questão pede para ler uma matriz concreta.
**Prioridade:** Média
**Tipo ENADE:** Resposta única (interpretação)

**Enunciado:**
SITUAÇÃO-PROBLEMA
Um serviço de mensageria interna registra, em uma matriz de adjacência, quais filas encaminham mensagens para quais outras. Como o encaminhamento tem sentido, o grafo é direcionado: a posição (linha i, coluna j) vale 1 quando existe o arco i → j. A equipe precisa migrar essa estrutura para listas de adjacência e calcular o volume de conexões de cada fila.

DADOS DE SUPORTE
Matriz de adjacência do grafo direcionado (vértices A, B, C, D, E; sem pesos):

|   | A | B | C | D | E |
|---|---|---|---|---|---|
| **A** | 0 | 1 | 0 | 0 | 0 |
| **B** | 0 | 0 | 0 | 1 | 0 |
| **C** | 1 | 0 | 0 | 0 | 1 |
| **D** | 0 | 0 | 1 | 0 | 1 |
| **E** | 0 | 0 | 0 | 1 | 0 |

"Em grafos direcionados, a soma dos graus de saída é igual ao número de arcos, e a soma dos graus de entrada também é igual ao número de arcos: Σ deg⁺(v) = |E| = Σ deg⁻(v)." (com base em ROSEN, 2019)

COMANDO
Com base na matriz apresentada, assinale a alternativa correta.

**Alternativas:**
- **A)** Como a posição (D,E) tem o mesmo valor que a posição (E,D), a matriz é simétrica e o grafo pode ser tratado como não direcionado.
- **B)** A lista de adjacência é A:[B]; B:[D]; C:[A,E]; D:[C,E]; E:[D], e a soma dos graus de saída é 7, igual à soma dos graus de entrada.
- **C)** A matriz possui 7 entradas iguais a 1; logo, há 7 arcos e, pelo Handshake Lemma, a soma dos graus de saída é 14.
- **D)** O grau de entrada de C é 2, obtido pela soma da linha C, e o vértice com maior grau de entrada é o vértice A.

**Gabarito: B**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — (D,E) = (E,D) = 1 só porque existem os dois arcos, D→E e E→D. Uma coincidência pontual não torna a matriz simétrica: (A,B) = 1 mas (B,A) = 0, e (C,A) = 1 mas (A,C) = 0. Este é o "erro mais frequente" citado no gabarito da Q2.
- **B) ✅** — Lendo as linhas, os arcos são A→B, B→D, C→A, C→E, D→C, D→E e E→D, o que dá exatamente essa lista. Os graus de saída (somas das linhas) são A1, B1, C2, D2, E1, total 7. Os graus de entrada (somas das colunas) são A1, B1, C1, D2, E2, total 7. Nos dois casos o total é |E| = 7. Conferido com python3.
- **C) ❌** — Acerta os 7 arcos, mas aplica a fórmula de grafo não direcionado (2|E|). Em grafo direcionado, cada arco soma 1 só no grau de saída da origem: Σ deg⁺ = |E| = 7. O valor 14 é a soma de entrada mais saída.
- **D) ❌** — A soma da linha C (= 2) é o grau de **saída** de C (C→A e C→E). O grau de entrada vem da **coluna** C e vale 1 (só D→C). Os maiores graus de entrada são de D e de E (2 cada); A tem grau de entrada 1.

**Base no material:**
- Slides p. 22: esta matriz direcionada.
- Apostila p. 23: "a_ij registra o arco que sai de i e chega a j"; "a soma dos valores de uma linha é o grau do vértice" (no não direcionado).
- Apostila p. 15, item 3.7: Σ deg⁺ = |E| = Σ deg⁻.
- Slides p. 25: lista de adjacência de grafo direcionado.

**Conceito-chave para a prova:**
- Em grafo direcionado, a linha i dá o grau de saída e a coluna j dá o grau de entrada.
- Σ deg⁺ = Σ deg⁻ = |E|. O "dobro" vale só em grafo não direcionado.
- Em grafo direcionado, a matriz em geral não é simétrica.

---

## I8 — Representação de grafos ponderados
**Subtópico coberto:** Unidade 5, item 5.5 (matrizes e listas em grafos ponderados) e item 5.3 (em grafo não direcionado, cada aresta aparece duas vezes nas listas). Apostila p. 23–24; slides p. 23 e 46.
**Por que é provável:** os slides mostram o mesmo grafo ponderado duas vezes, uma com 0 (p. 23) e outra com ∞ (p. 46) para "sem conexão", e a apostila tem um "Ponto de atenção" exatamente sobre isso. Nenhuma questão conhecida cobra grafos ponderados na representação.
**Prioridade:** Baixa
**Tipo ENADE:** Lacunas

**Enunciado:**
SITUAÇÃO-PROBLEMA
Uma operadora logística representa sua rede de centros de distribuição como um grafo não direcionado ponderado, em que o peso de cada aresta é o custo (em R$ mil) do transporte entre dois centros. A primeira versão do sistema usava 0 para indicar "sem conexão". Como a empresa passará a ter rotas internas com custo zero, a equipe precisa revisar a representação.

DADOS DE SUPORTE
Grafo: V = {A, B, C, D, E}; arestas (custo): A–B 8, A–C 4, A–D 10, B–D 3, B–E 6, C–D 5, D–E 7.
[Figura: A em cima à esquerda, B em cima à direita, C embaixo à esquerda, D embaixo no centro e E embaixo à direita, com os pesos acima nas arestas.]

Matriz de pesos atual:

|   | A | B | C | D | E |
|---|---|---|---|---|---|
| **A** | 0 | 8 | 4 | 10 | ? |
| **B** | 8 | 0 | ? | 3 | 6 |
| **C** | 4 | ? | 0 | 5 | ? |
| **D** | 10 | 3 | 5 | 0 | 7 |
| **E** | ? | 6 | ? | 7 | 0 |

("?" = posição sem conexão, cujo valor está em revisão.)

COMANDO
Preencha as lacunas do texto a seguir.

"Na nova versão, a ausência de conexão entre A e E deve ser registrada na matriz com ______(I)______. Na lista de adjacência ponderada, o centro D fica armazenado como ______(II)______. Somando todas as listas, o número total de pares (vizinho, peso) armazenados é ______(III)______."

Assinale a alternativa que preenche corretamente as lacunas.

**Alternativas:**
- **A)** (I) um valor especial, como ∞ — (II) D → [(A,10), (B,3), (C,5), (E,7)] — (III) 14
- **B)** (I) o valor 0, como na diagonal — (II) D → [A, B, C, E] — (III) 7
- **C)** (I) um valor especial, como ∞ — (II) D → [(A,10), (B,3), (C,5), (E,7)] — (III) 7
- **D)** (I) o valor 0, como na diagonal — (II) D → [(A,10), (B,3), (C,5), (D,0), (E,7)] — (III) 14

**Gabarito: A**

**Por que cada alternativa está certa ou errada:**
- **A) ✅**
  - (I): se custo zero passa a ser permitido, usar 0 para "sem aresta" torna as duas situações indistinguíveis. Por isso usa-se um valor especial, como ∞, como no slide p. 46 (apostila p. 24, "Ponto de atenção").
  - (II): a lista ponderada guarda pares (vizinho, peso), e os vizinhos de D são A (10), B (3), C (5) e E (7).
  - (III): em grafo não direcionado, cada aresta aparece duas vezes nas listas, uma em cada extremidade. Logo, 2·|E| = 2·7 = 14 pares.
  - Conferido com python3.
- **B) ❌** — (I) volta ao problema original: 0 confunde ausência de rota com rota de custo zero. (II) perde os pesos, porque lista ponderada precisa guardar o valor. (III) 7 é |E|, não o total de entradas nas listas.
- **C) ❌** — (I) e (II) estão certas, mas (III) conta cada aresta uma única vez. Na lista de um grafo não direcionado, cada aresta {u,v} aparece na lista de u e na lista de v (apostila p. 23: "o tamanho total das listas é proporcional a 2|E|").
- **D) ❌** — (I) está errada pelo mesmo motivo da B. (II) inclui o par (D,0), como se a diagonal fosse uma aresta. A diagonal é 0 porque não há laços, e um grafo simples não tem laço D–D.

**Base no material:**
- Apostila p. 24, item 5.5: "Em uma lista, cada vizinho pode ser armazenado junto com seu peso"; "Usar 0 para representar 'sem aresta' pode ser inadequado quando peso zero é permitido".
- Apostila p. 23: "cada aresta aparece duas vezes nas listas".
- Slides p. 23 (versão com 0) e p. 46 (versão com ∞).

**Conceito-chave para a prova:**
- Matriz ponderada: guarda o peso em a_ij e usa um sentinela (∞) para "sem aresta".
- Lista ponderada: guarda pares (vizinho, peso).
- Em grafo não direcionado, a lista tem 2|E| entradas.

---

## I9 — Ordem de visita DFS e BFS
**Subtópico coberto:** Unidade 6: DFS (pilha/recursão, backtracking) comparada à BFS no mesmo grafo (apostila p. 26–27, Fig. 11; slides p. 30–36 e 41).
**Por que é provável:** é o tema com mais slides do Capítulo 3 ("Como percorrer?", DFS, pilha, BFS, fila, "Agora, na prática. Mesmo grafo. Duas estratégias."). A Q3 conhecida só cobra a BFS, e a Q6 é discursiva. Uma versão objetiva com a Fig. 11 da apostila (que tem um vértice G a mais) é muito provável.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única

**Enunciado:**
SITUAÇÃO-PROBLEMA
Um crawler interno precisa visitar as páginas de um portal corporativo a partir da página inicial A. As páginas são vértices, e os links, navegáveis nos dois sentidos, são arestas de um grafo não direcionado. A equipe vai comparar duas estratégias de varredura: busca em profundidade (DFS), implementada com pilha/recursão, e busca em largura (BFS), implementada com fila. Sempre que houver mais de um vizinho não visitado, considera-se a ordem alfabética.

DADOS DE SUPORTE
V = {A, B, C, D, E, F, G}
E = {A–B, A–C, B–D, B–E, C–F, E–G}
[Figura: árvore com raiz A. A tem os filhos B e C; B tem os filhos D e E; C tem o filho F; E tem o filho G. Sem pesos.]
Lista de adjacência: A:[B, C]; B:[A, D, E]; C:[A, F]; D:[B]; E:[B, G]; F:[C]; G:[E].

COMANDO
Assinale a alternativa que apresenta, respectivamente, a ordem de visita da DFS e da BFS a partir de A.

**Alternativas:**
- **A)** DFS: A, B, C, D, E, F, G; BFS: A, B, D, E, G, C, F.
- **B)** DFS: A, B, D, E, G, C, F; BFS: A, B, C, D, E, F, G.
- **C)** DFS: A, B, D, E, C, F, G; BFS: A, B, C, D, E, F, G.
- **D)** DFS: A, B, D, E, G, C, F; BFS: A, B, C, D, E, G, F.

**Gabarito: B**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Troca as estratégias. A sequência por níveis é a da BFS, e a sequência que "mergulha" no ramo de B é a da DFS.
- **B) ✅**
  - DFS: A → B → D. D não tem vizinho novo, então volta a B (backtracking) → E → G. Volta a E, B e A → C → F.
  - BFS: fila [A] → B, C entram → [B, C]. Sai B: entram D, E → [C, D, E]. Sai C: entra F → [D, E, F]. Sai D: nada. Sai E: entra G → [F, G].
  - Níveis da BFS: {A}, {B, C}, {D, E, F}, {G}.
  - Conferido com python3.
- **C) ❌** — A BFS está certa, mas na DFS G aparece no fim. Ao chegar em E, a DFS continua para G (mais fundo no mesmo ramo) antes de voltar a A e seguir para C.
- **D) ❌** — A DFS está certa, mas na BFS G (nível 3) aparece antes de F (nível 2). A BFS processa todo um nível antes do seguinte, e F foi descoberto (a partir de C) antes de G (a partir de E).

**Base no material:**
- Apostila p. 27: "uma BFS com vizinhos em ordem alfabética visita A, B, C, D, E, F, G. Os níveis são {A}, {B,C}, {D,E,F} e {G}"; "uma DFS possível é A, B, D, E, G, C, F".
- Slides p. 33, 35 e 41 (mesmo grafo sem o G: DFS A→B→D→E→C→F; BFS A→B→C→D→E→F).

**Conceito-chave para a prova:**
- DFS (pilha) esgota um ramo antes de voltar.
- BFS (fila) esgota um nível antes de descer.
- A ordem exata depende da ordem dos vizinhos na lista (normalmente a alfabética).

---

## I10 — Conectividade, componentes e detecção de ciclos
**Subtópico coberto:** Unidade 6, itens 6.4–6.5 (aplicações e complexidade) e os slides "Conectividade e Detecção de Ciclos" e "Para que servem?" (apostila p. 27–28; slides p. 37–39).
**Por que é provável:** "conectividade" está escrito na matriz curricular do Capítulo 3 ("DFS, BFS e conectividade"), e os slides p. 38–39 têm três cards de aplicação (componentes conexos, arestas de retorno, ordenação topológica) sem nenhuma questão associada. A apostila tem a caixa "Rigor metodológico" sobre O(V+E) × O(V²).
**Prioridade:** Alta
**Tipo ENADE:** Julgamento V/F (sequência correta)

**Enunciado:**
SITUAÇÃO-PROBLEMA
Após uma falha elétrica, o time de redes de um laboratório quer descobrir quais computadores ainda conseguem se comunicar e se há laços redundantes na rede. A rede foi modelada como um grafo não direcionado e será analisada com BFS/DFS. Considere que os vértices são percorridos em ordem crescente de índice e que a DFS é implementada por recursão.

DADOS DE SUPORTE
V = {P1, P2, P3, P4, P5, P6, P7, P8}
E = {P1–P2, P1–P3, P2–P3, P4–P5, P6–P7} (P8 não possui nenhum link ativo)
[Figura: triângulo P1–P2–P3; aresta P4–P5 isolada; aresta P6–P7 isolada; vértice P8 isolado. Sem pesos.]
"Conectividade — Implementação: disparo de DFS/BFS múltiplos a partir de nós não visitados." / "Detecção de ciclos — Identificar laços onde um vértice aponta para um ancestral já presente na pilha de recursão atual." (slides p. 39)

COMANDO
Julgue as afirmações a seguir como Verdadeiras (V) ou Falsas (F).

( ) Disparando uma nova BFS/DFS a partir de cada vértice ainda não visitado, de P1 a P8, serão feitos 4 disparos, um para cada componente conexa.

( ) Se a rede for armazenada em matriz de adjacência, BFS e DFS continuam custando O(|V| + |E|), pois só os vizinhos existentes são examinados.

( ) Na DFS iniciada em P1 (P1 → P2 → P3), ao examinar P3 encontra-se uma aresta para P1, ancestral na pilha de recursão que não é o pai de P3. Isso revela o ciclo P1–P2–P3.

( ) Uma BFS iniciada em P4 visita todos os oito computadores, pois a BFS só termina quando todos os vértices do grafo tiverem sido visitados.

Assinale a alternativa com a sequência correta.

**Julgamento das afirmativas:**
- **1ª — Verdadeira.** Os disparos começam em P1 (visita P1, P2, P3), P4 (visita P4, P5), P6 (visita P6, P7) e P8 (visita só P8). São 4 disparos e 4 componentes. O vértice isolado também é uma componente. Conferido com python3.
- **2ª — Falsa.** Com matriz, examinar os vizinhos de um vértice exige percorrer a linha inteira (|V| posições), e o custo total passa a O(|V|²). O(|V| + |E|) pressupõe lista de adjacência (apostila p. 28, "Rigor metodológico").
- **3ª — Verdadeira.** A pilha de recursão é [P1, P2, P3]. Em P3, o vizinho P1 já foi visitado, está na pilha e não é o pai imediato (o pai é P2): é uma aresta de retorno, e ela fecha o ciclo P1–P2–P3.
- **4ª — Falsa.** A BFS termina quando a **fila** esvazia, e visita só os vértices **alcançáveis** a partir da origem: aqui, P4 e P5. Para cobrir o grafo inteiro, é preciso disparar uma nova busca a partir de cada vértice não visitado (1ª afirmativa).

**Alternativas:**
- **A)** V – F – V – F
- **B)** F – V – V – F
- **C)** V – V – F – F
- **D)** V – F – F – V

**Gabarito: A**

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — Componentes contadas pelos disparos (V); custo O(V²) com matriz (F); aresta de retorno indica ciclo (V); BFS só alcança a componente da origem (F).
- **B) ❌** — Nega a contagem de componentes por disparos múltiplos, que é exatamente a implementação dos slides. E aceita O(V+E) com matriz, ignorando que a complexidade depende da representação.
- **C) ❌** — Aceita O(V+E) com matriz e nega a detecção de ciclo pela aresta de retorno, que é o critério do slide p. 39.
- **D) ❌** — Nega a detecção de ciclo e aceita que uma BFS a partir de P4 alcance vértices de outras componentes, o que é impossível sem caminho até eles.

**Base no material:**
- Slides p. 37: tabela DFS × BFS (conectividade ✓/✓; detecção de ciclos ✓/✓).
- Slides p. 38: "Conectividade: existe caminho entre dois vértices?" e "Ciclos: o caminho retorna a um vértice?".
- Slides p. 39: componentes conexos; arestas de retorno.
- Apostila p. 27–28: tabela do item 6.4 ("Detecção de componentes: Sim / Sim") e item 6.5 (O(|V|+|E|) com lista e O(|V|²) com matriz).

**Conceito-chave para a prova:**
- Número de componentes conexas = número de buscas disparadas a partir de vértices ainda não visitados.
- Aresta de retorno (para um ancestral na pilha) indica ciclo. Em grafo não direcionado, ignore a aresta para o pai.
- BFS e DFS custam O(V+E) com lista e O(V²) com matriz.

---

## I11 — Ordenação topológica em DAG
**Subtópico coberto:** ordenação topológica (slides p. 37, 38 e 40; apostila p. 28, tabela do item 6.4).
**Por que é provável:** os slides dedicam um slide inteiro ("ORDENAR DEPENDÊNCIAS", p. 40, com "Precedência de Tarefas", "Restrição: só é possível em grafos sem ciclos (DAG)" e "Pós-Ordem Invertida") e um exemplo de DAG com A → B/C → D → E (p. 38). Nenhuma questão conhecida cobra o tema.
**Prioridade:** Média
**Tipo ENADE:** Ordenação (resposta única)

**Enunciado:**
SITUAÇÃO-PROBLEMA
Um pipeline de CI/CD executa seis tarefas, e algumas só podem começar depois que outras terminam. A equipe modelou as dependências como um grafo direcionado em que o arco U → V significa "U deve ser concluída antes de V". Antes de automatizar o pipeline, é preciso obter uma ordem linear de execução que respeite todas as dependências.

DADOS DE SUPORTE
Tarefas:
- T1: clonar repositório
- T2: compilar biblioteca base
- T3: gerar esquema do banco
- T4: compilar API
- T5: executar testes unitários
- T6: empacotar e implantar

Arcos: T1 → T2, T1 → T3, T2 → T4, T3 → T4, T2 → T5, T4 → T6, T5 → T6.
[Figura: DAG com T1 no topo, apontando para T2 e T3. T2 e T3 apontam para T4, e T2 também aponta para T5. T4 e T5 apontam para T6. Sem ciclos e sem pesos.]
"Se existe uma aresta direcionada de U para V, U deve aparecer antes de V na sequência linear resultante. Restrição: só é possível em grafos sem ciclos (DAG)." (slides p. 40)

COMANDO
Assinale a alternativa que apresenta uma ordem de execução válida (ordenação topológica) para as seis tarefas.

**Alternativas:**
- **A)** T1, T2, T4, T3, T5, T6.
- **B)** T2, T1, T3, T4, T5, T6.
- **C)** T1, T3, T2, T5, T4, T6.
- **D)** T1, T2, T5, T6, T3, T4.

**Gabarito: C**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Viola T3 → T4: a API (T4) seria compilada antes de o esquema do banco (T3) existir. T4 depende de T2 **e** de T3.
- **B) ❌** — Viola T1 → T2: compila a biblioteca antes de clonar o repositório.
- **C) ✅** — Todos os 7 arcos são respeitados. T1 vem primeiro; T3 e T2 dependem só de T1; T5 vem depois de T2; T4 vem depois de T2 e T3; T6 vem por último, depois de T4 e T5. É exatamente a **pós-ordem invertida** da DFS a partir de T1 com vizinhos em ordem crescente: a pós-ordem é T6, T4, T5, T2, T3, T1, e invertida dá T1, T3, T2, T5, T4, T6. Conferido com python3.
- **D) ❌** — Viola T4 → T6: implanta (T6) antes de compilar a API (T4) e de gerar o esquema (T3).

**Base no material:**
- Slides p. 40: princípio de dependência; restrição a DAG; "Resolução com DFS: Pós-Ordem Invertida — adiciona os vértices a uma lista à medida que a recursão DFS é concluída (pós-ordem), invertendo o resultado ao final"; aplicações em compiladores, gerenciamento de pacotes e árvore de build.
- Slides p. 38: DAG A → B, A → C, B → D, C → D, D → E com a ordem A, B/C, D, E.

**⚠️ Atenção:** um DAG pode ter várias ordens topológicas válidas. Aqui, T1, T2, T3, T5, T4, T6 (obtida pelo método de Kahn, com fila e graus de entrada) também seria válida, mas não está entre as alternativas. O slide p. 37 marca a BFS com ✗ em "Ordenação topológica", enquanto a apostila (p. 28) diz "não na forma básica". Se a prova afirmar que "só a DFS permite ordenação topológica", lembre que a versão com fila (Kahn) existe.
**Conceito-chave para a prova:**
- Uma ordem topológica é válida quando, para todo arco U → V, U vem antes de V.
- Só existe ordem topológica em DAG: um ciclo torna a ordenação impossível.
- Pela DFS, a ordem é a pós-ordem invertida.

---

## I12 — Execução do Dijkstra
**Subtópico coberto:** Unidade 7, itens 7.1–7.2: relaxamento e execução passo a passo do Dijkstra (apostila p. 30–31; slides p. 46).
**Por que é provável:** o slide p. 46 traz uma figura e uma matriz ponderada para o Dijkstra **sem resolver o exemplo**, o que é um candidato natural a questão. A Q4 conhecida só pede a escolha do algoritmo, não a execução.
**Prioridade:** Alta
**Tipo ENADE:** Afirmativa incompleta

**Enunciado:**
SITUAÇÃO-PROBLEMA
Uma empresa de streaming precisa calcular a menor latência entre o servidor de origem A e os demais pontos de presença (PoPs) da sua rede. Os enlaces são bidirecionais e todas as latências (em ms) são positivas, por isso a equipe aplicará o algoritmo de Dijkstra a partir de A.

DADOS DE SUPORTE
Grafo não direcionado ponderado: V = {A, B, C, D, E}.
Arestas (latência em ms): A–B 8, A–C 4, A–D 10, B–D 3, B–E 6, C–D 5, D–E 7.
[Figura: A em cima à esquerda, B em cima à direita, C embaixo à esquerda, D embaixo no centro e E embaixo à direita. A matriz equivalente usa ∞ para "sem enlace": A–E, B–C e C–E não existem.]

|   | A | B | C | D | E |
|---|---|---|---|---|---|
| **A** | 0 | 8 | 4 | 10 | ∞ |
| **B** | 8 | 0 | ∞ | 3 | 6 |
| **C** | 4 | ∞ | 0 | 5 | ∞ |
| **D** | 10 | 3 | 5 | 0 | 7 |
| **E** | ∞ | 6 | ∞ | 7 | 0 |

Relaxamento: para a aresta (u, v) de peso w, se d[u] + w < d[v], então d[v] ← d[u] + w (CORMEN et al., 2022).

COMANDO
Ao final da execução do Dijkstra a partir de A, a menor latência de A até E, o caminho correspondente e a ordem em que os vértices são finalizados são, respectivamente,

**Alternativas:**
- **A)** 16 ms, pelo caminho A–C–D–E; ordem de finalização: A, C, D, E, B.
- **B)** 17 ms, pelo caminho A–D–E; ordem de finalização: A, B, C, D, E.
- **C)** 14 ms, pelo caminho A–B–E; ordem de finalização: A, B, C, D, E.
- **D)** 14 ms, pelo caminho A–B–E; ordem de finalização: A, C, B, D, E.

**Gabarito: D**

**Rastreamento (conferido com python3):**
| Etapa | Finaliza | d[A] | d[B] | d[C] | d[D] | d[E] |
|---|---|---|---|---|---|---|
| 0 | — | 0 | ∞ | ∞ | ∞ | ∞ |
| 1 | A (0) | 0 | 8 | 4 | 10 | ∞ |
| 2 | C (4) | 0 | 8 | 4 | **9** (4+5) | ∞ |
| 3 | B (8) | 0 | 8 | 4 | 9 (8+3=11 não melhora) | **14** (8+6) |
| 4 | D (9) | 0 | 8 | 4 | 9 | 14 (9+7=16 não melhora) |
| 5 | E (14) | 0 | 8 | 4 | 9 | 14 |

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Segue a escolha gulosa "do vizinho mais barato a partir do último vértice" (A→C→D→E), que não é o critério do Dijkstra. O Dijkstra escolhe, entre **todos** os vértices não finalizados, o de menor d. Por isso B (8) é finalizado antes de D (9) e de E. O caminho A–C–D–E custa 16 > 14.
- **B) ❌** — Usa a aresta direta A–D (10) e finaliza em ordem alfabética. Mas d[D] cai para 9 via C, e A–D–E custa 17.
- **C) ❌** — A distância e o caminho estão certos, mas a ordem de finalização está errada. A ordem é definida pela menor distância provisória: C (4) é finalizado antes de B (8).
- **D) ✅** — d[E] = 14 via A–B–E. A ordem de finalização segue as distâncias crescentes: A (0), C (4), B (8), D (9), E (14). Os outros caminhos simples de A até E custam 16, 17, 18, 18 e 19.

**Base no material:**
- Slides p. 46: esta figura e esta matriz, com o texto "Utiliza uma estratégia gulosa baseada na menor distância provisória" e "Funciona apenas com pesos não negativos".
- Apostila p. 30–31: item 7.1 (relaxamento) e item 7.2 (passos 1–4; exemplo da Fig. 12, em que C melhora B e D).

**Conceito-chave para a prova:**
- O Dijkstra finaliza o vértice não finalizado de **menor d global**, e não o vizinho do último vértice.
- Ao finalizar, relaxa as arestas que saem do vértice. Um d só diminui.
- A ordem de finalização segue as distâncias crescentes.

---

## I13 — Execução do Bellman-Ford e ciclo negativo
**Subtópico coberto:** Unidade 7, item 7.3: Bellman-Ford, com |V|−1 rodadas, rodada adicional e ciclo negativo (apostila p. 31–32, Fig. 13; slides p. 47–48).
**Por que é provável:** a apostila resolve passo a passo o exemplo da Fig. 13 (com arcos negativos e o ciclo B→C→D→B) e tem a caixa "Por que detectar ciclo negativo?". A Q4 conhecida só pede para reconhecer quando usar Bellman-Ford.
**Prioridade:** Média
**Tipo ENADE:** Afirmativas múltiplas

**Enunciado:**
SITUAÇÃO-PROBLEMA
Em uma rede de distribuição de conteúdo, alguns enlaces geram créditos de tráfego por acordos com provedores e, por isso, são modelados como arcos de peso negativo. A equipe executará o algoritmo de Bellman-Ford a partir do nó S para obter o menor custo até cada nó e verificar se há ciclo negativo.

DADOS DE SUPORTE
Grafo direcionado ponderado: V = {S, A, B, C, D}.
Arcos (custo): S→A 4, S→B 5, A→C −3, B→C 6, C→D 2, D→B −1.
[Figura: S aponta para A (4) e para B (5); A aponta para C (−3); B aponta para C (6); C aponta para D (2); D aponta para B (−1). Há um único ciclo: B→C→D→B.]
Procedimento (CORMEN et al., 2022):
1. Inicializar d[S] = 0 e os demais com ∞.
2. Repetir |V| − 1 vezes o relaxamento de todos os arcos.
3. Fazer uma rodada adicional: se alguma distância ainda diminuir, existe ciclo de peso negativo alcançável a partir da origem.

COMANDO
Avalie as afirmações a seguir.

I. Ao final, as distâncias a partir de S são S = 0, A = 4, B = 2, C = 1 e D = 3, e o menor custo até B usa o caminho S→A→C→D→B.

II. Bastam |V| − 1 = 4 rodadas de relaxamento para fixar as distâncias porque, sem ciclo negativo alcançável, todo caminho mínimo pode ser tomado simples, com no máximo |V| − 1 arcos.

III. Se o peso do arco D→B fosse alterado para −9, o ciclo B→C→D→B passaria a pesar −1, e a rodada adicional ainda reduziria alguma distância, indicando ciclo negativo.

IV. Assim como o Dijkstra, o Bellman-Ford finaliza cada vértice uma única vez, escolhendo gulosamente o de menor distância provisória.

É correto o que se afirma em

**Julgamento das afirmativas:**
- **I — Verdadeira.** d[A] = 4 e d[B] = 5 inicialmente. A→C dá d[C] = 4 + (−3) = 1. C→D dá d[D] = 3. D→B melhora d[B] de 5 para 3 + (−1) = 2. O caminho até B é S→A→C→D→B, de custo 4 − 3 + 2 − 1 = 2. O ciclo B→C→D→B pesa 6 + 2 − 1 = 7 ≥ 0, e a rodada extra não altera nada (apostila p. 32).
- **II — Verdadeira.** "Em um caminho simples, podem existir no máximo |V|−1 arestas. Por isso, após |V|−1 rodadas completas de relaxamento, todas as menores distâncias estão determinadas" (apostila p. 32). Aqui |V| = 5, então são 4 rodadas.
- **III — Verdadeira.** 6 + 2 + (−9) = −1 < 0. O ciclo é alcançável a partir de S (por S→B ou S→A→C), e, a cada volta, o custo diminui sem limite. Conferido com python3: após 4 rodadas, a rodada extra ainda reduz distâncias.
- **IV — Falsa.** Essa é a estratégia do **Dijkstra**. O Bellman-Ford não "finaliza" vértices: ele relaxa **todos** os arcos em cada rodada, e um mesmo vértice pode ter a distância atualizada várias vezes. Por isso custa O(VE) (apostila p. 31–32; slides p. 48).

**Alternativas:**
- **A)** I e IV, apenas.
- **B)** II e III, apenas.
- **C)** I, II e III, apenas.
- **D)** I, II, III e IV.

**Gabarito: C**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Inclui a IV, que atribui ao Bellman-Ford a estratégia gulosa do Dijkstra, e omite a II e a III.
- **B) ❌** — A II e a III estão certas, mas a alternativa omite a I, cujas distâncias são exatamente as calculadas na apostila.
- **C) ✅** — I (distâncias e caminho), II (justificativa das |V|−1 rodadas) e III (detecção de ciclo negativo na rodada extra) estão corretas. A IV confunde os algoritmos.
- **D) ❌** — Inclui a IV, que é falsa.

**Base no material:**
- Apostila p. 31–32, item 7.3: passos 1–4; "Na Figura 13, a partir de S: d[A] = 4 e d[B] = 5; ... D→B melhora d[B] de 5 para 3 + (−1) = 2. O ciclo B→C→D→B tem peso 6 + 2 − 1 = 7"; caixa "Por que detectar ciclo negativo?".
- Apostila p. 32, item 7.4 (tabela).
- Slides p. 47–48 ("Realiza até |V|-1 passadas"; "Detecta ciclos de peso negativo alcançáveis a partir da origem").

**⚠️ Atenção (para versões alteradas):** conferi com python3 que, **neste grafo específico**, um Dijkstra clássico chegaria por acaso às mesmas distâncias (S=0, A=4, C=1, D=3, B=2). Por isso, uma afirmação como "o Dijkstra necessariamente erraria neste grafo" seria **falsa**. O correto é dizer que o Dijkstra **não garante** resultado correto com pesos negativos e **não detecta** ciclo negativo.
**Conceito-chave para a prova:**
- Bellman-Ford = |V|−1 rodadas relaxando todos os arcos, mais 1 rodada de verificação.
- Se alguma distância ainda diminuir na rodada extra, há ciclo negativo alcançável e não existe distância mínima finita.
- Custo O(VE).

---

## I14 — Execução do Prim
**Subtópico coberto:** Unidade 8, itens 8.1–8.3: árvore geradora mínima e execução do Prim (apostila p. 35–36, Fig. 14; slides p. 49–50).
**Por que é provável:** tanto os slides (p. 50, "Prim na Prática: Rastreamento", custo 6) quanto a apostila (p. 36, tabela passo a passo, peso 10) trazem um rastreamento completo do Prim. A Q4 conhecida só pede para reconhecer que o problema é de AGM.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única

**Enunciado:**
SITUAÇÃO-PROBLEMA
Uma universidade vai interligar seis prédios (A a F) com fibra óptica. Os pesos representam o custo (em R$ mil) de instalar cada trecho possível. O objetivo é conectar todos os prédios com o menor custo total, sem trechos redundantes. A equipe aplicará o algoritmo de Prim a partir do prédio A.

DADOS DE SUPORTE
Grafo não direcionado ponderado e conexo: V = {A, B, C, D, E, F}.
Arestas (custo): A–B 3, A–C 1, B–C 2, B–D 4, C–D 5, C–E 6, D–E 2, D–F 3, E–F 1.
[Figura: A à esquerda; B em cima; C embaixo de B; D à direita de B; E embaixo de D; F na extrema direita. As arestas são as listadas acima.]
Regra do Prim: a cada etapa, escolher a aresta de menor peso que liga um vértice já na árvore a um vértice ainda fora dela (CORMEN et al., 2022).

COMANDO
Assinale a alternativa que apresenta a sequência de arestas escolhidas pelo Prim, a partir de A, e o custo total da árvore geradora mínima.

**Alternativas:**
- **A)** A–C, C–B, B–D, D–E, E–F; custo total 10.
- **B)** A–C, E–F, C–B, D–E, B–D; custo total 10.
- **C)** A–C, A–B, C–D, C–E, E–F; custo total 16.
- **D)** A–C, C–B, B–D, D–F, D–E; custo total 12.

**Gabarito: A**

**Rastreamento (conferido com python3):**
| Etapa | Vértices na árvore | Arestas na fronteira (corte) | Escolhida |
|---|---|---|---|
| 1 | {A} | A–B 3, A–C 1 | **A–C (1)** |
| 2 | {A, C} | A–B 3, C–B 2, C–D 5, C–E 6 | **C–B (2)** |
| 3 | {A, B, C} | B–D 4, C–D 5, C–E 6 (A–B descartada: formaria ciclo) | **B–D (4)** |
| 4 | {A, B, C, D} | D–E 2, D–F 3, C–E 6 | **D–E (2)** |
| 5 | {A, B, C, D, E} | E–F 1, D–F 3 | **E–F (1)** |
| Fim | todos | — | **custo 1+2+4+2+1 = 10** |

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — É a sequência da tabela, igual à da apostila (p. 36). A AGM desse grafo é única (conferido com python3), com peso 10.
- **B) ❌** — Tem o mesmo conjunto de arestas e o mesmo custo, mas a **sequência** não é a do Prim. Escolher "a menor aresta do grafo inteiro que não forma ciclo" (E–F na 2ª etapa) é outro critério (o do algoritmo de Kruskal, que não é tratado no material). O Prim mantém **uma única árvore** a partir de A, e E–F não toca a árvore {A, C} na 2ª etapa.
- **C) ❌** — Esta é a árvore de **caminhos mínimos** do Dijkstra a partir de A (d: C=1, B=3, D=6, E=7, F=8), e não a AGM. O custo total é 16 > 10. É a confusão que a apostila nomeia "Prim não é Dijkstra".
- **D) ❌** — Na 4ª etapa escolhe D–F (3), embora D–E (2) seja mais leve. Depois de D–E entrar, E–F (1) é melhor que D–F. O custo 12 > 10 mostra que essa árvore não é mínima.

**Base no material:**
- Apostila p. 35–36: itens 8.1–8.3 (definição de AGM com |V|−1 arestas; passos do Prim; tabela "Etapa / Aresta escolhida / Peso / Vértices na árvore"; "Peso total = 1 + 2 + 4 + 2 + 1 = 10"; propriedade do corte).
- Slides p. 49–50 (rastreamento com "A-C (descarta, gera ciclo)", custo total 6).

**Conceito-chave para a prova:**
- O Prim cresce **uma** árvore e só considera arestas que cruzam o corte entre a árvore e o restante do grafo.
- Uma aresta com as duas pontas já na árvore é descartada, porque formaria ciclo.
- Ao final, são |V| − 1 arestas.

---

## I15 — Prim não é Dijkstra
**Subtópico coberto:** Unidade 8, itens 8.1, 8.4 e 8.5: diferenças entre AGM e caminhos mínimos, |V| − 1 arestas, floresta geradora mínima e pesos negativos (apostila p. 35–37).
**Por que é provável:** a apostila dedica uma seção inteira ("8.4 Prim não é Dijkstra"), com tabela comparativa e caixa "Não confunda: uma AGM não garante que o caminho entre dois vértices dentro da árvore seja o caminho de menor custo". O gabarito da Q4-D toca nessa confusão, mas nenhuma questão a cobra diretamente.
**Prioridade:** Média
**Tipo ENADE:** Afirmativa negativa (INCORRETA)

**Enunciado:**
SITUAÇÃO-PROBLEMA
Um campus interligou seis prédios (A a F) com fibra óptica usando a árvore geradora mínima obtida pelo algoritmo de Prim a partir de A. Na reunião de encerramento, um gestor sugeriu usar essa mesma árvore para definir a rota de menor custo de transmissão entre A e F, argumentando que "Prim e Dijkstra fazem a mesma coisa, pois ambos escolhem sempre o menor valor".

DADOS DE SUPORTE
Grafo não direcionado ponderado: V = {A, B, C, D, E, F}.
Arestas (custo): A–B 3, A–C 1, B–C 2, B–D 4, C–D 5, C–E 6, D–E 2, D–F 3, E–F 1.
AGM obtida pelo Prim a partir de A: {A–C 1, C–B 2, B–D 4, D–E 2, E–F 1}, com custo total 10.

| Aspecto | Prim | Dijkstra |
|---|---|---|
| Objetivo | Minimizar o peso total da árvore | Minimizar a distância desde uma fonte |
| Chave de um vértice | Menor aresta que o conecta à árvore | Menor distância conhecida desde a fonte |
| Pesos negativos | Podem existir em MST | Não são permitidos no algoritmo clássico |

(tabela da apostila, p. 37)

COMANDO
Considerando as diferenças entre árvore geradora mínima e caminhos mínimos, assinale a alternativa **INCORRETA**.

**Alternativas:**
- **A)** A AGM possui exatamente 5 arestas, pois toda árvore geradora de um grafo conexo com 6 vértices tem |V| − 1 arestas.
- **B)** Como no Dijkstra, a chave de cada vértice no Prim é a distância acumulada desde A; por isso, o Prim não admite pesos negativos.
- **C)** Na AGM, o caminho de A até F custa 10, mas o menor caminho no grafo, A–C–E–F, custa 8; logo, a AGM não garante caminhos mínimos.
- **D)** Se a rede fosse desconexa, aplicar o procedimento em cada componente conexa produziria uma floresta geradora mínima.

**Gabarito: B**

**Por que cada alternativa está certa ou errada:**
- **A) ❌ (afirmação correta)** — "Toda árvore com |V| vértices possui exatamente |V|−1 arestas" (apostila p. 35): 6 − 1 = 5.
- **B) ✅ (afirmação INCORRETA)** — No Prim, a chave de um vértice é o **peso da menor aresta** que o liga à árvore atual, e não a distância acumulada desde a origem. Essa é a chave do Dijkstra. Além disso, pesos negativos **podem existir** em uma AGM (tabela da apostila, p. 37). Quem não os admite é o Dijkstra clássico.
- **C) ❌ (afirmação correta)** — Na AGM, o único caminho A–C–B–D–E–F custa 1 + 2 + 4 + 2 + 1 = 10. No grafo original, A–C–E–F custa 1 + 6 + 1 = 8, que é o mínimo (Dijkstra a partir de A dá d[F] = 8, conferido com python3). Isso mostra, com números, a caixa "Não confunda" da apostila.
- **D) ❌ (afirmação correta)** — "Se o grafo for desconexo, ... executar o procedimento em cada componente produz uma floresta geradora mínima" (apostila p. 37).

**Base no material:** apostila p. 35 (item 8.1: |E(T)| = |V| − 1; exemplo dos prédios e cabos "sem exigir caminhos mínimos individuais"), p. 36–37 (item 8.4, tabela "Prim × Dijkstra" e caixa "Não confunda") e p. 37 (item 8.5: complexidade O(|E| log |V|) com heap ou O(|V|²) com matriz; floresta geradora mínima).
**Conceito-chave para a prova:**
- AGM minimiza a **soma total** das arestas. Dijkstra minimiza a **distância** desde uma fonte.
- A AGM não dá caminhos mínimos entre pares de vértices.
- Prim aceita pesos negativos. Em grafo desconexo, o resultado é uma floresta geradora mínima.
