# Teoria da Computação — Questões INFERIDAS (prováveis questões do banco do squad que não temos)

> ⚠️ **Atenção:** estas questões NÃO constam nos materiais. Foram elaboradas para cobrir os subtópicos do material do
> Squad 3 que não têm questão conhecida, imitando o estilo das questões do squad. Servem para estudo dirigido.
> As questões reais conhecidas estão em `../questoes_por_topico/10_Teoria_da_Computacao.md`.

**Base usada:**
- `Teoria da Computação - Revisão ENADE.pdf` (slides, 50 p.): 5 unidades (capas nas p. 3, 14, 24, 32, 38). Todas as páginas foram lidas, e as que têm diagrama foram renderizadas (p. 19, 27, 28, 29, 33, 34, 35, 41, 43, 44, 20, 21). As 6 questões conhecidas (Q1–Q6) ficam nas p. 12, 22, 30, 36, 45–46 e 48, com gabarito nas p. 13, 23, 31, 37, 47 e 49.
- `Material de Estudos - Teoria da Computação.pdf` (apostila, 60 p.): Unidade 1 (p. 2–12), Unidade 2 (p. 13–25), Unidade 3 (p. 26–35), Unidade 4 (p. 36–46), Unidade 5 (p. 47–58), referências (p. 59–60). Todas as páginas foram lidas, e as figuras foram renderizadas (p. 3, 5, 28, 37, 38, 40, 42, 48, 51). Questões conhecidas na apostila: Q12 (V/F "estilo ENADE", p. 11), Q27 (exercício resolvido, p. 43–44) e as fixações discursivas (p. 11, 25, 35, 46, 57–58).
- **Estilo identificado do squad:** sempre **4 alternativas (A)–(D)**. Estrutura: **Texto-Base** (citação entre aspas, geralmente tirada do próprio material) + **Situação-Problema** contextualizada (banco de dados, protocolo/handshake, parser JSON-like, compilador) + **Comando**. Tipos usados: V/F com sequência (Q1), afirmativas múltiplas I–III/I–IV ("É correto apenas o que se afirma em", Q2 e Q5), resposta única (Q3), asserção-razão com 4 alternativas, sem a opção "ambas falsas" (Q4), e associação de colunas (Q6). Cada questão tem um slide "Gabarito Oficial e Análise" com "Justificativa da resposta correta" e "Análise dos Distratores". Gabaritos conhecidos: A, A, C, A, D, D.
- As inferidas abaixo seguem esse formato e acrescentam os tipos do guia que o squad ainda não usou (afirmativa negativa/INCORRETA, lacunas, ordenação), para variar.
- Todos os autômatos, gramáticas, expressões regulares e relações foram conferidos em Python (scripts em `/tmp/agent_work/tc2_py/`): força bruta até comprimento 8–10 e simulação não determinística (BFS) dos autômatos de pilha.

## Mapa de cobertura
| # | Subtópico (material) | Páginas | Questão conhecida | Questão inferida | Prioridade |
|---|---|---|---|---|---|
| 1 | U1 · Conjuntos: definição, notação, ∈/∉, elemento × conjunto | Ap. p. 2–3; Sl. p. 4 | — (só fixação Q9, relacionada) | **I1** (agrupado com o nº 2) | Média |
| 2 | U1 · Subconjuntos e conjunto das partes P(A) (2ⁿ) | Ap. p. 3–4; Sl. p. 5 | — (fixação Q9) | **I1** | Média |
| 3 | U1 · Conjunto vazio (∅ ⊆ A; ∅ ≠ {∅}) | Ap. p. 4; Sl. p. 6 | Q1 (item 1); fixação Q8 | — · variação provável: "∅ ∈ {∅} e ∅ ⊆ {∅}" | — |
| 4 | U1 · Operações: união, interseção, diferença (A − B ≠ B − A) | Ap. p. 4–6; Sl. p. 7 | Q12 (itens I–III); fixação Q7 | — · variação provável: pedir B − A = {4} | — |
| 5 | U1 · Conjunto universo e complemento | Ap. p. 6–7; Sl. p. 8 | Q1 (item 2) | — · variação provável: "sem U definido não se lista A'" | — |
| 6 | U1 · Relações binárias, pares ordenados e produto cartesiano | Ap. p. 7–8; Sl. p. 9 | — | **I2** | Média |
| 7 | U1 · Propriedades reflexiva, simétrica, antissimétrica e transitiva | Ap. p. 8–10; Sl. p. 10–11 | Q1 (itens 3–4), Q12 (IV–VI); fixação Q10–Q11 | — · I2 reaproveita os exemplos do slide 11 | — |
| 8 | U2 · Alfabeto, palavra, comprimento, ε, linguagem (L ⊆ Σ*) | Ap. p. 13–14, 17–18; Sl. p. 15 | — (fixação Q13–Q14) | **I3** (agrupado com o nº 10) | Alta |
| 9 | U2 · Gramáticas formais G = (V, Σ, P, S), derivação, L(G) | Ap. p. 15–16; Sl. p. 16 | — (Q2 só cobra a forma Tipo 2; fixação Q19–Q20) | **I4** | Alta |
| 10 | U2 · Operações com palavras: concatenação, potência, w⁰ = ε | Ap. p. 16–17; Sl. p. 17 | — | **I3** | Alta |
| 11 | U2 · Operações sobre linguagens: ∪, ∩, −, concatenação, Lⁿ, L*, L⁺, complemento | Ap. p. 18–20; Sl. p. 17–18 | — (fixação Q15–Q17) | **I5** | Alta |
| 12 | U2 · Hierarquia de Chomsky | Ap. p. 20–21; Sl. p. 19 | Q6; Q2 | — · variação provável: ordem de inclusão Tipo 3 ⊂ Tipo 2 ⊂ Tipo 1 ⊂ Tipo 0 | — |
| 13 | U2 · Expressões regulares: operadores (│, *, +, (), ε, ∅) e ε × ∅ | Ap. p. 21–22; Sl. p. 20 | — | **I6** | Média |
| 14 | U2 · Interpretação de ER: (a│b)*(01│10)+ e método de resolução | Ap. p. 23–24; Sl. p. 21 | — (fixação Q18) | **I7** | Alta |
| 15 | U3 · Autômato finito: conceito, 5-upla, δ, AFD completo | Ap. p. 26–28; Sl. p. 25–27 | — (fixação Q21) | **I8** | Alta |
| 16 | U3 · Execução passo a passo, configurações, L(M), estado final ≠ parada | Ap. p. 28–29, 31–32 | — (fixação Q23–Q24) | **I9** | Alta |
| 17 | U3 · AFD × AFND e critério de aceitação do AFND | Ap. p. 29–31; Sl. p. 28 | — (Q6 só cita "AF (Det. ou Não)"; fixação Q22) | **I10** | Alta |
| 18 | U3 · Conversão AFND → AFD (construção dos subconjuntos, até 2ⁿ estados) | Ap. p. 31 | — | **I11** | Média |
| 19 | U3 · Memória e limitações do AFD (aⁿbⁿ, argumento dos estados finitos, a*b* × aⁿbⁿ) | Ap. p. 32–34; Sl. p. 29 | Q3; Q2 (item I); fixação Q25–Q26 | — · variação provável: "a*b* é regular, aⁿbⁿ não"; paridade cabe em 2 estados | — |
| 20 | U4 · Pilha LIFO e definição formal (7-upla, Γ, Z₀) | Ap. p. 36–37; Sl. p. 33–34 | — (fixação Q28–Q29) | **I12** | Alta |
| 21 | U4 · Transições do AP: push, pop, manter, transição ε | Ap. p. 37 | — (fixação Q30) | **I13** | Média |
| 22 | U4 · Exemplo aⁿbⁿ (Figura 2 = diagrama do slide 34) e evolução da pilha | Ap. p. 38–39; Sl. p. 34 | — (fixação Q31) | **I14** | Alta |
| 23 | U4 · LLC e parênteses balanceados | Ap. p. 39–41; Sl. p. 35–36 | Q4; fixação Q32 | — · variação provável: simular "(()" ou "())" (p. 40–41) | — |
| 24 | U4 · Limitação aⁿbⁿcⁿ e regra prática "AP compara dois grupos" | Ap. p. 41–42, 44–45; Sl. p. 35 | parcial: só Q5 (item III); fixação Q33 | **I15** | Alta |
| 25 | U4 · Roteiro de construção e exercício resolvido aⁿb²ⁿ | Ap. p. 42–44 | — (só o exercício resolvido Q27, discursivo) | **I16** | Alta |
| 26 | U5 · MT: componentes, 6-upla, Σ × Γ, branco, ausência de Z₀ | Ap. p. 47–49; Sl. p. 39–40 | — (fixação Q34–Q35) | **I17** | Alta |
| 27 | U5 · Transições "lido → escrito, movimento" e configurações | Ap. p. 49–50; Sl. p. 41 | Q5 (simulação); fixação Q40 | — · variação provável: MT que inverte bits 0↔1 | — |
| 28 | U5 · Exemplo aⁿbⁿcⁿ (marcação X, Y, Z) | Ap. p. 50–52; Sl. p. 43, 45–47 | Q5; fixação Q38–Q39 | — · variação provável: simular aabc ou abcc (rejeita); n ≥ 0 × n ≥ 1 | — |
| 29 | U5 · Aceitar × rejeitar × não parar (loop) | Ap. p. 52; Sl. p. 42 | parcial: só Q5 (item II); fixação Q36 | **I18** (agrupado com o nº 30) | Alta |
| 30 | U5 · Reconhecer × decidir; RE × recursivas; inclusões | Ap. p. 53; Sl. p. 43–44 | — (fixação Q37) | **I18** | Alta |
| 31 | U5 · Papel da fita, variantes da MT, Tese de Church-Turing, MT Universal | Ap. p. 54, 57 | — | **I19** | Alta |
| 32 | U5 · Indecidibilidade e problema da parada (HALT, prova por contradição, enumerabilidade) | Ap. p. 54–55; Sl. p. 44 | — (fixação Q41) | **I20**, **I21** | Alta |
| 33 | U5 · Consequências: redução, Teorema de Rice, aplicações | Ap. p. 55–57 | — (fixação Q42) | **I22** | Média |

Itens que o orquestrador citou como possíveis lacunas e que **não são subtópicos do material**:
- **Lema do bombeamento:** a apostila só o menciona ("pode ser estudado posteriormente", p. 34; p. 42, 45), e ele aparece no gabarito da Q2 (slide 23). Sem questão própria; a ideia (casa dos pombos) entra na Q3 conhecida.
- **Gramáticas regulares:** não há seção sobre elas. A gramática da fixação Q19 (S → 0A │ ε; A → 1S) é regular e é usada na I4.
- **Classes P e NP:** só há uma frase (p. 57: "o número de passos de uma MT é a base das classes P e NP"). Sem questão; citada no conceito-chave da I19.
- **AFND × AFD / equivalência**, **expressões regulares**, **decidibilidade/problema da parada** e **Church-Turing** são subtópicos de verdade e não tinham questão objetiva. Receberam I6–I7, I10–I11 e I18–I22.

**Resumo:** 33 subtópicos. 9 estão cobertos por questões conhecidas (nº 3, 4, 5, 7, 12, 19, 23, 27, 28). 2 estão só parcialmente cobertos (um item de afirmativa da Q5, nº 24 e 29) e receberam questão inferida. Os outros 22 não tinham questão objetiva. No total são **22 questões inferidas** (I1–I22): três agrupam dois subtópicos pequenos (I1, I3, I18) e o problema da parada ganhou duas (I20, I21). Gabaritos: **A = 5** (I4, I8, I13, I16, I20), **B = 6** (I1, I5, I9, I12, I17, I21), **C = 6** (I2, I6, I11, I15, I19, I22), **D = 5** (I3, I7, I10, I14, I18).

## Índice
**Unidade 1 — Conjuntos e Relações**
1. [I1 — Elemento × conjunto, ∈ × ⊆ e conjunto das partes](#i1--elemento--conjunto---e-conjunto-das-partes)
2. [I2 — Produto cartesiano e propriedades das relações do slide 11](#i2--produto-cartesiano-e-propriedades-das-relações-do-slide-11)

**Unidade 2 — Linguagens Formais e Expressões**

3. [I3 — Palavras: comprimento, concatenação e potência (V/F)](#i3--palavras-comprimento-concatenação-e-potência-vf)
4. [I4 — Gramática formal: componentes, derivação e L(G)](#i4--gramática-formal-componentes-derivação-e-lg)
5. [I5 — Operações sobre linguagens e fechos de Kleene/positivo (INCORRETA)](#i5--operações-sobre-linguagens-e-fechos-de-kleenepositivo-incorreta)
6. [I6 — Operadores de expressões regulares e ε × ∅](#i6--operadores-de-expressões-regulares-e-ε--)
7. [I7 — Interpretação da expressão (a│b)*(01│10)+](#i7--interpretação-da-expressão-ab0110)

**Unidade 3 — Autômatos Finitos**

8. [I8 — 5-upla e o autômato do slide 27 (linguagem ab*a)](#i8--5-upla-e-o-autômato-do-slide-27-linguagem-aba)
9. [I9 — Execução passo a passo do AFD que reconhece "aa"](#i9--execução-passo-a-passo-do-afd-que-reconhece-aa)
10. [I10 — AFD × AFND: poder de reconhecimento (asserção-razão)](#i10--afd--afnd-poder-de-reconhecimento-asserção-razão)
11. [I11 — AFND e construção dos subconjuntos](#i11--afnd-e-construção-dos-subconjuntos)

**Unidade 4 — Autômatos de Pilha**

12. [I12 — Definição formal do AP, Γ, Z₀ e memória LIFO](#i12--definição-formal-do-ap-γ-z-e-memória-lifo)
13. [I13 — Transições do AP: push, pop e manter (associação)](#i13--transições-do-ap-push-pop-e-manter-associação)
14. [I14 — AP do slide 34 / Figura 2 (aⁿbⁿ, n ≥ 1)](#i14--ap-do-slide-34--figura-2-aⁿbⁿ-n--1)
15. [I15 — Quais linguagens um AP reconhece ("compara dois grupos")](#i15--quais-linguagens-um-ap-reconhece-compara-dois-grupos)
16. [I16 — Exercício resolvido aⁿb²ⁿ (lacunas)](#i16--exercício-resolvido-aⁿbⁿ-lacunas)

**Unidade 5 — Máquinas de Turing**

17. [I17 — Definição formal da MT: Σ × Γ, branco e ausência de Z₀ (V/F)](#i17--definição-formal-da-mt-σ--γ-branco-e-ausência-de-z-vf)
18. [I18 — Rejeitar × loop; reconhecer × decidir](#i18--rejeitar--loop-reconhecer--decidir)
19. [I19 — Variantes da MT, Tese de Church-Turing e MT Universal (INCORRETA)](#i19--variantes-da-mt-tese-de-church-turing-e-mt-universal-incorreta)
20. [I20 — Problema da parada: reconhecível, mas não decidível (asserção-razão)](#i20--problema-da-parada-reconhecível-mas-não-decidível-asserção-razão)
21. [I21 — Ordenação da prova de indecidibilidade de HALT](#i21--ordenação-da-prova-de-indecidibilidade-de-halt)
22. [I22 — Consequências da indecidibilidade: redução, Rice e o "erro do colega"](#i22--consequências-da-indecidibilidade-redução-rice-e-o-erro-do-colega)

---

# UNIDADE 1 — Conjuntos e Relações

## I1 — Elemento × conjunto, ∈ × ⊆ e conjunto das partes
**Subtópico coberto:** Conjuntos: definição, notação, pertinência; elemento × conjunto; subconjuntos e conjunto das partes (apostila p. 2–4; slides p. 4–5).
**Por que é provável:** a apostila dedica a seção 2.1 ("Elemento não é a mesma coisa que conjunto"), uma tabela ∈ / ∉ / ⊆ (p. 3) e a seção 3.1 (conjunto das partes, 2ⁿ) a isso. O 1º item dos "Erros frequentes" (p. 10) é "Confundir ∈ com ⊆", e a fixação Q3 pede os 2³ subconjuntos. A Q1 conhecida só cobra ∅ ⊆ A e {∅} ≠ {}.
**Prioridade:** Média
**Tipo ENADE:** Afirmativas múltiplas (I–IV)

**Enunciado:**
**Texto-Base:** "Para indicar que um objeto pertence a um conjunto, utiliza-se o símbolo ∈. [...] É importante distinguir um objeto de um conjunto que contém esse objeto. Por exemplo, 1 é um número, enquanto {1} é um conjunto cujo único elemento é o número 1."

**Situação-Problema:** Ao modelar o conjunto de estados de um autômato, um estudante definiu A = {1, 2, 3} e registrou as afirmações a seguir.

I. 2 ∈ A e {1, 2} ⊆ A.

II. {3, 2, 1, 1} = A.

III. {1} ∈ A.

IV. O conjunto das partes P(A) possui 2³ = 8 elementos, entre eles ∅ e o próprio A.

**Comando:** É correto o que se afirma em:

**Alternativas:**
- **A)** I e III, apenas
- **B)** I, II e IV, apenas
- **C)** II, III e IV, apenas
- **D)** I, II, III e IV

**Gabarito: B**

**Julgamento das afirmativas:**
- **I — Verdadeira.** 2 é elemento de A (∈), e todo elemento de {1, 2} está em A (⊆).
- **II — Verdadeira.** A ordem dos elementos não importa e repetições não criam novos elementos (apostila p. 2; slide 4). Logo {3, 2, 1, 1} = {1, 2, 3}.
- **III — Falsa.** {1} é um **conjunto**, não um elemento de A. O correto é 1 ∈ A ou {1} ⊆ A. É o erro "confundir ∈ com ⊆" (p. 10).
- **IV — Verdadeira.** P(A) = {∅, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}}, 8 = 2³ subconjuntos. ∅ ⊆ A e A ⊆ A sempre (p. 3–4).

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Inclui a III, que confunde pertinência com inclusão, e deixa de fora II e IV, que são verdadeiras.
- **B) ✅** — I, II e IV são verdadeiras; só a III é falsa.
- **C) ❌** — Inclui a III e exclui a I, que é verdadeira.
- **D) ❌** — "Todas" inclui a III, que é falsa.

**Base no material:** p. 2 (ordem e repetição não importam; ∈ e ∉), p. 3 (tabela "x ∈ A / x ∉ A / B ⊆ A"; "Todo conjunto é subconjunto dele mesmo"; "∅ ⊆ A"), p. 4 ("Um conjunto com n elementos possui 2ⁿ subconjuntos"), p. 10 (erro frequente "Confundir ∈ com ⊆").
**Conceito-chave para a prova:** ∈ liga elemento a conjunto e ⊆ liga conjunto a conjunto: 1 ∈ A e {1} ⊆ A, mas {1} ∉ A. |P(A)| = 2ⁿ, e ∅ e A sempre estão em P(A).

---

## I2 — Produto cartesiano e propriedades das relações do slide 11
**Subtópico coberto:** Relações binárias, pares ordenados e produto cartesiano (apostila p. 7–8; slide p. 9), aplicados às relações do slide 11.
**Por que é provável:** produto cartesiano e "R ⊆ A × A" (p. 7–8) não aparecem em nenhuma questão conhecida. O slide 11 se chama **"Exemplos Estilo ENADE"** e traz relações prontas, e duas delas são pegadinhas de transitividade: o exemplo de antissimétrica e o de simétrica **não** são transitivos. A apostila alerta: "Verificar transitividade observando apenas uma cadeia" é erro frequente (p. 10).
**Prioridade:** Média
**Tipo ENADE:** Resposta única

**Enunciado:**
**Texto-Base:** "Formalmente, uma relação de A em B pode ser entendida como um subconjunto do produto cartesiano A × B. Quando a relação é definida sobre um único conjunto A, temos R ⊆ A × A."

**Situação-Problema:** Em um banco de dados relacional, a tabela *Matrícula* associa alunos do conjunto A = {1, 2} a turmas do conjunto B = {a, b}. Em outra parte do sistema, sobre o conjunto de estados S = {1, 2, 3}, foram definidas duas relações de transição:

- R₁ = {(1,1), (1,2), (2,3)}
- R₂ = {(1,2), (2,1), (3,3)}

**Comando:** Considerando as definições de produto cartesiano e das propriedades das relações binárias, assinale a alternativa correta.

**Alternativas:**
- **A)** A × B = {(1,a), (1,b), (2,a), (2,b)} e, como em um par ordenado a ordem dos componentes não importa, também (a,1) ∈ A × B.
- **B)** R₁ é antissimétrica e transitiva, pois não há pares de ida e volta entre elementos distintos e o caminho 1 → 2 → 3 está representado.
- **C)** R₁ é antissimétrica, mas não é transitiva, pois contém (1,2) e (2,3) e não contém (1,3).
- **D)** R₂ é simétrica e transitiva, pois todo par (x,y) de R₂ possui o seu inverso (y,x) em R₂.

**Gabarito: C**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — O produto A × B está correto (4 = 2 · 2 pares), mas em par ordenado **a ordem importa**: "(1, 2) e (2, 1) não são, em geral, o mesmo par" (p. 7). (a,1) pertence a B × A, não a A × B.
- **B) ❌** — R₁ é antissimétrica, mas a cadeia (1,2), (2,3) **exige** (1,3), que não está em R₁. Ter os dois pares do caminho não basta; o "atalho" (1,3) precisa estar na relação, como no exemplo de transitiva do slide 11: {(1,2), (2,3), (1,3)}.
- **C) ✅** — Antissimétrica: não existe (x,y) e (y,x) com x ≠ y. Não transitiva: (1,2) ∈ R₁ e (2,3) ∈ R₁, mas (1,3) ∉ R₁. (R₁ também não é reflexiva, pois faltam (2,2) e (3,3).) Conferido em Python.
- **D) ❌** — R₂ é simétrica, mas **não** é transitiva: (1,2) e (2,1) exigem (1,1), que não está em R₂, e (2,1) e (1,2) exigem (2,2), que também não está. Compare com a relação da p. 10, {(1,1),(2,2),(3,3),(1,2),(2,1)}, que é transitiva justamente porque contém (1,1) e (2,2).

**Base no material:** p. 7–8 (relação como subconjunto de A × B; exemplo A = {1,2}, B = {a,b}); p. 9 ("Se R fosse apenas {(1,2), (2,3)}, ela não seria transitiva, porque faltaria o par (1,3)"); p. 10 (verificar todas as cadeias); slide p. 11 (R₁ como exemplo de "Antissimétrica" e R₂ como exemplo de "Simétrica").
**Conceito-chave para a prova:** |A × B| = |A| · |B|, e a ordem do par importa. Qualquer subconjunto de A × A é uma relação; as propriedades são características dela, não exigências para que ela exista. Na transitividade, confira **todas** as cadeias, inclusive as de ida e volta, como (1,2),(2,1) ⇒ (1,1).

---

# UNIDADE 2 — Linguagens Formais e Expressões

## I3 — Palavras: comprimento, concatenação e potência (V/F)
**Subtópico coberto:** Alfabeto, palavra, comprimento, ε e linguagem (apostila p. 13–14, 17–18; slide p. 15), mais operações com palavras (apostila p. 16–17; slide p. 17).
**Por que é provável:** os slides 15 e 17 tratam disso, e o 17 tem destaque "Importante: W⁰ = ε". A apostila destaca "não confundir ε com ∅" (p. 14) e "Uma palavra não é um conjunto" (p. 13). A U2 tem duas fixações sobre o tema (Q13, Q14), e a questão de fechamento da U2 (Q2) não cobra nada disso.
**Prioridade:** Alta
**Tipo ENADE:** Julgamento V/F com sequência (mesmo formato da Q1 do squad)

**Enunciado:**
**Texto-Base:** "Uma palavra não é um conjunto. Em uma palavra, a ordem e a repetição importam. Assim, 01, 10 e 001 são palavras diferentes, embora utilizem os mesmos símbolos."

**Situação-Problema:** Um analisador léxico trabalha sobre o alfabeto Σ = {a, b, c, d, e}. Para testar o módulo de concatenação, a equipe usa as palavras u = abc, v = de e w = ab.

**Analise as afirmações (V ou F):**

( ) uv = abcde e vu = deabc; logo, em geral, a concatenação de palavras não é comutativa.

( ) |uv| = |u| + |v| = 5 e |w³| = 6.

( ) w⁰ = ∅, pois a potência zero de uma palavra não produz palavra alguma.

( ) Como ab e ba são formadas pelos mesmos símbolos de Σ, elas representam a mesma palavra.

Sequência correta de cima para baixo:

**Alternativas:**
- **A)** V – V – V – F
- **B)** V – F – F – V
- **C)** F – V – F – F
- **D)** V – V – F – F

**Gabarito: D**

**Julgamento das afirmações:**
- **1 — Verdadeira.** uv = abcde ≠ vu = deabc (p. 17: "em geral, uv ≠ vu").
- **2 — Verdadeira.** |abcde| = 3 + 2 = 5 (p. 17: |uv| = |u| + |v|). w³ = ababab tem 6 símbolos (|wⁿ| = n·|w|).
- **3 — Falsa.** Por definição, **w⁰ = ε**, a palavra vazia de comprimento 0, e não ∅, que é a linguagem sem palavras (p. 14, 17; slide 17).
- **4 — Falsa.** A ordem importa nas palavras; ab ≠ ba (p. 13).

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Considera o item 3 verdadeiro, confundindo a palavra vazia ε com a linguagem vazia ∅.
- **B) ❌** — Nega o item 2 (soma de comprimentos) e aceita o item 4, tratando a palavra como conjunto.
- **C) ❌** — Nega o item 1, como se a concatenação fosse comutativa igual à união de conjuntos.
- **D) ✅** — V–V–F–F.

**Base no material:** p. 13 (palavra não é conjunto), p. 14 (|ε| = 0; wε = εw = w; "não confundir ε com ∅"), p. 17 (uv ≠ vu; |uv| = |u| + |v|; w⁰ = ε), slide p. 15 e p. 17.
**Conceito-chave para a prova:** ε é **palavra** (|ε| = 0, elemento neutro da concatenação) e ∅ é **linguagem** (zero palavras), então {ε} ≠ ∅. Concatenação não é comutativa, e w⁰ = ε. Σ\* é infinito, contém ε, e toda linguagem L sobre Σ satisfaz L ⊆ Σ\*.

---

## I4 — Gramática formal: componentes, derivação e L(G)
**Subtópico coberto:** Gramáticas formais G = (V, Σ, P, S), produções, derivação e linguagem gerada (apostila p. 15–16; slide p. 16).
**Por que é provável:** o slide 16 inteiro e as seções 5.1–5.5 da apostila tratam disso, e duas fixações (Q7 e Q8 da U2) pedem exatamente para identificar V, Σ, P, S **nesta** gramática e para mostrar derivações. A Q2 conhecida só cobra a forma das regras Tipo 2.
**Prioridade:** Alta
**Tipo ENADE:** Afirmativas múltiplas (I–IV)

**Enunciado:**
**Texto-Base:** "Uma derivação é uma sequência de substituições que parte de S e aplica produções até restarem somente terminais. [...] Uma palavra só pertence a L(G) se existir ao menos uma derivação que a produza; formas intermediárias, como aSb, contêm variáveis e por isso não são palavras da linguagem."

**Situação-Problema:** Para descrever o protocolo de um sensor que transmite pares "0 seguido de 1", um estudante propôs a gramática G = ({S, A}, {0, 1}, P, S), com as produções:

- S → 0A │ ε
- A → 1S

Avalie as afirmações do estudante:

I. Em G, V = {S, A} é o conjunto de variáveis, Σ = {0, 1} é o conjunto de terminais e S é o símbolo inicial, sendo V ∩ Σ = ∅.

II. A palavra 0101 pertence a L(G), pois S ⇒ 0A ⇒ 01S ⇒ 010A ⇒ 0101S ⇒ 0101.

III. A cadeia 01S pertence a L(G), pois é obtida a partir de S pela aplicação das produções de P.

IV. A palavra 0110 pertence a L(G), pois contém o mesmo número de símbolos 0 e 1.

**Comando:** É correto o que se afirma em:

**Alternativas:**
- **A)** I e II, apenas
- **B)** I, II e III, apenas
- **C)** II e IV, apenas
- **D)** I, III e IV, apenas

**Gabarito: A**

**Julgamento das afirmativas:**
- **I — Verdadeira.** É a leitura da quádrupla G = (V, Σ, P, S). Variáveis e terminais são disjuntos (p. 15).
- **II — Verdadeira.** Duas vezes S → 0A e A → 1S, e por fim S → ε. Restam só terminais, então a derivação termina.
- **III — Falsa.** 01S é **forma intermediária**: contém a variável S. Só pertencem a L(G) cadeias formadas apenas por terminais (p. 16: L(G) = { w ∈ Σ\* │ S ⇒\* w }).
- **IV — Falsa.** L(G) = {ε, 01, 0101, 010101, ...} = (01)\* (conferido em Python até comprimento 8). Todo 0 é seguido obrigatoriamente de 1 (A → 1S), e depois de cada 1 só se pode recomeçar com 0 ou terminar. "0110" contém "11", que é impossível. Ter #0 = #1 não basta.

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — Só I e II são verdadeiras.
- **B) ❌** — Inclui a III, tratando forma sentencial com variável como palavra da linguagem (erro frequente, p. 24).
- **C) ❌** — Exclui a I e inclui a IV. Confunde L(G) com a linguagem "#0 = #1".
- **D) ❌** — Inclui III e IV, ambas falsas.

**Base no material:** p. 15 (G = (V, Σ, P, S); V e Σ disjuntos), p. 16 (derivação; L(G) = { w ∈ Σ\* │ S ⇒\* w }; formas intermediárias não são palavras), p. 24 (erro frequente "tratar formas intermediárias da derivação como palavras"), p. 25 (fixação Q7, mesma gramática).
**Conceito-chave para a prova:** a derivação termina quando restam só terminais. Esta gramática (S → 0A │ ε; A → 1S) gera (01)\*, uma linguagem regular, porque cada regra tem um terminal seguido de no máximo uma variável à direita. Já S → aSb │ ε gera aⁿbⁿ, que é livre de contexto e não regular.

---

## I5 — Operações sobre linguagens e fechos de Kleene/positivo (INCORRETA)
**Subtópico coberto:** Operações sobre linguagens: união, interseção, diferença, concatenação, potência Lⁿ, fecho de Kleene, fecho positivo e complemento (apostila p. 18–20; slides p. 17–18).
**Por que é provável:** o slide 18 inteiro trata disso. A apostila marca como "ampliação importante em relação à forma resumida apresentada nos slides" que L\* não é só {ε, a, b} (p. 20), e os "Erros frequentes" (p. 24) trazem dois itens sobre L\* e L⁺. São três fixações (Q15, Q16, Q17).
**Prioridade:** Alta
**Tipo ENADE:** Afirmativa negativa (INCORRETA)

**Enunciado:**
**Texto-Base:** "O fecho de Kleene de uma linguagem L, representado por L\*, reúne todas as palavras que podem ser obtidas concatenando zero ou mais palavras de L. L\* = L⁰ ∪ L¹ ∪ L² ∪ L³ ∪ ..."

**Situação-Problema:** Em uma aula de Linguagens Formais, o professor apresentou, sobre Σ = {a, b}, as linguagens L = {a, b}, L₁ = {a, ab, b} e L₂ = {b, ba}, e pediu que a turma avaliasse as conclusões escritas por um colega.

**Comando:** Assinale a alternativa **INCORRETA**.

**Alternativas:**
- **A)** L₁ ∩ L₂ = {b} e L₁ − L₂ = {a, ab}, pois ab e ba são palavras distintas.
- **B)** L\* = {ε, a, b}, isto é, o fecho de Kleene reúne apenas a palavra vazia e as palavras de L.
- **C)** L² = LL = {aa, ab, ba, bb}, e L⁰ = {ε} para qualquer linguagem L.
- **D)** Como ε ∉ L, vale L\* = L⁺ ∪ {ε}: L\* admite zero concatenações, e L⁺ exige pelo menos uma.

**Gabarito: B**

**Por que cada alternativa está certa ou errada:**
- **A) ❌ (afirmação correta)** — A única palavra comum é b. Em L₁ e fora de L₂ ficam a e ab, porque ab ≠ ba.
- **B) ✅ (é a INCORRETA)** — L\* contém **todas** as concatenações finitas: L\* = {ε, a, b, aa, ab, ba, bb, aaa, aab, ...}, um conjunto infinito. "L\* = L ∪ {ε}" é exatamente o erro listado na p. 24.
- **C) ❌ (afirmação correta)** — L² = LL = {aa, ab, ba, bb} (p. 19), e L⁰ = {ε} por definição.
- **D) ❌ (afirmação correta)** — p. 20: "Quando ε não pertence originalmente a L [...] L\* = L⁺ ∪ {ε}". A diferença central é zero × pelo menos uma concatenação.

**⚠️ Atenção:** o slide 18 resume o fecho positivo como "Todas as palavras de uma linguagem, exceto a vazia", com o exemplo "L = {ε, a, b} → L⁺ = {a, b...}". A apostila corrige isso: "Achar que L⁺ significa simplesmente 'L sem ε'" é erro, pois **L⁺ = L¹ ∪ L² ∪ ...** (p. 20, 24). Se ε ∈ L, então ε ∈ L¹ ⊆ L⁺. Se a prova trouxer "L⁺ = L\* − {ε}", isso só vale quando ε ∉ L.

**Base no material:** p. 18–19 (união, interseção, diferença, concatenação de linguagens, Lⁿ), p. 19–20 (fecho de Kleene e positivo; L\* = L⁺ ∪ {ε}), p. 20 (complemento Lᶜ = Σ\* − L), p. 24 (erros frequentes), p. 25 (fixações Q15–Q17).
**Conceito-chave para a prova:** \* = zero ou mais (sempre contém ε; até ∅\* = {ε}). ⁺ = uma ou mais. L\* é infinito sempre que L tem alguma palavra não vazia. O complemento depende do universo Σ\*.

---

## I6 — Operadores de expressões regulares e ε × ∅
**Subtópico coberto:** Expressões regulares: definição, operadores básicos e diferença entre ε e ∅ (apostila p. 21–22; slide p. 20).
**Por que é provável:** o slide 20 é dedicado à ER. A apostila tem a tabela de operadores (p. 22) e a seção 16.1 "Diferença entre ε e ∅", com a frase "Essa distinção é fundamental". Os "Erros frequentes" (p. 24) incluem "Interpretar \* como 'uma ou mais vezes'" e "Ignorar os parênteses".
**Prioridade:** Média
**Tipo ENADE:** Afirmativas múltiplas (I–IV)

**Enunciado:**
**Texto-Base:** "Uma expressão regular é uma representação formal usada para descrever uma linguagem regular sem precisar enumerar individualmente todas as suas palavras."

**Situação-Problema:** Ao configurar um validador de formatos, um desenvolvedor precisa interpretar corretamente os operadores básicos das expressões regulares sobre Σ = {a, b}. Ele anotou as seguintes conclusões:

I. A expressão a∅ não gera palavra alguma, enquanto a │ ε descreve a linguagem {a, ε}.

II. As linguagens {ε} e ∅ são iguais, pois nenhuma delas contém símbolos do alfabeto.

III. As expressões a+ e aa\* descrevem a mesma linguagem: uma ou mais ocorrências consecutivas de a.

IV. A expressão (ab)\* gera a palavra aabb, pois permite repetir a e b zero ou mais vezes.

**Comando:** É correto apenas o que se afirma em:

**Alternativas:**
- **A)** I
- **B)** II e IV
- **C)** I e III
- **D)** I, III e IV

**Gabarito: C**

**Julgamento das afirmativas:**
- **I — Verdadeira.** Tabela da p. 22: "a∅ — não gera palavra alguma" (concatenar com a linguagem vazia dá ∅) e "a│ε — aceita a ou palavra vazia".
- **II — Falsa.** {ε} tem **uma** palavra (a vazia) e ∅ tem **zero** palavras: {ε} ≠ ∅ (p. 22).
- **III — Verdadeira.** aa\* = um a obrigatório seguido de zero ou mais a's, que é o mesmo que a+ (conferido em Python).
- **IV — Falsa.** Os parênteses agrupam: (ab)\* repete o **bloco** ab e gera ε, ab, abab, ... (p. 22). aabb não pertence (conferido com `re.fullmatch`).

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Omite a III, que é verdadeira.
- **B) ❌** — Reúne as duas falsas: confunde ε com ∅ e ignora o agrupamento.
- **C) ✅** — I e III são verdadeiras.
- **D) ❌** — Inclui a IV, ignorando os parênteses.

**Base no material:** p. 21 (definição e exemplo a+), p. 22 (tabela de operadores; 16.1 ε × ∅), p. 24 (erros frequentes), slide p. 20.
**Conceito-chave para a prova:** │ = alternativa; justaposição = concatenação; \* = zero ou mais; + = uma ou mais; () agrupa. ε é palavra e ∅ é linguagem vazia (a∅ = ∅, mas aε = a). ER descreve exatamente as linguagens regulares (Tipo 3).

---

## I7 — Interpretação da expressão (a│b)*(01│10)+
**Subtópico coberto:** Interpretação de expressão regular e método de resolução (apostila p. 23–24; slide p. 21 "Aplicação Prática — Interpretando uma Expressão").
**Por que é provável:** é o único exemplo de ER trabalhado no slide e na apostila, com lista de aceitos e não aceitos (p. 23) e roteiro "Como resolver exercícios" (p. 24). A fixação Q6 da U2 testa justamente palavras nessa expressão.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única (interpretação)

**Enunciado:**
**Texto-Base:** "A palavra aceita pode iniciar com qualquer texto (a/b) ou vazio, mas obrigatoriamente termina com pelo menos um par numérico válido (01 ou 10)." (slide 21)

**Situação-Problema:** Um sistema de rastreamento gera códigos sobre o alfabeto Σ = {a, b, 0, 1}. Um código só é considerado válido se pertencer à linguagem descrita pela expressão regular

**(a │ b)\* (01 │ 10)+**

A equipe de testes montou quatro lotes de códigos para validar o sistema.

**Comando:** Assinale a alternativa que apresenta um lote formado **apenas** por códigos válidos.

**Alternativas:**
- **A)** ε, 01, ba1010
- **B)** aab, a01, 10
- **C)** 001, bb10, a11
- **D)** 1010, bb0110, b1001

**Gabarito: D**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — ε é inválida: o bloco (01│10)+ exige **pelo menos uma** ocorrência (p. 23). 01 e ba1010 são válidas.
- **B) ❌** — aab é inválida: não termina com bloco 01 ou 10. a01 e 10 são válidas.
- **C) ❌** — 001 é inválida: depois de um "0" isolado não há como decompor em blocos 01/10. a11 é inválida: 11 não é 01 nem 10. bb10 é válida.
- **D) ✅** — 1010 = ε + 10 + 10; bb0110 = bb + 01 + 10; b1001 = b + 10 + 01. Todas foram conferidas com `re.fullmatch` em Python.

**Base no material:** p. 23 (blocos; aceitos: 01, 10, a01, bb10, ab0110, ba1010; não aceitos: aab, ε, 001, a11), p. 24 (roteiro: identificar blocos, ver o que pode gerar ε, decompor a palavra), slide p. 21.
**Conceito-chave para a prova:** decomponha a palavra bloco a bloco. O 1º bloco (a│b)\* pode ser vazio; o 2º, (01│10)+, é obrigatório e só aceita pares exatos. Letras depois dos dígitos (ex.: ab01a) invalidam a palavra.

---

# UNIDADE 3 — Autômatos Finitos

## I8 — 5-upla e o autômato do slide 27 (linguagem ab*a)
**Subtópico coberto:** Autômato finito: conceito, 5-upla, função de transição, AFD completo (apostila p. 26–28; slides p. 25–27).
**Por que é provável:** os slides 26–27 apresentam a 5-upla e um "Exemplo de Autômato Finito" com só três transições, e a apostila comenta que elas "não formam a tabela completa de um AFD" (p. 27–28). O autômato do slide 27 reconhece **exatamente ab\*a**, a "Funcionalidade X" da questão de fechamento da U3 (Q3). É provável que o squad tenha ligado as duas. Há ainda a fixação Q1 (5-upla).
**Prioridade:** Alta
**Tipo ENADE:** Afirmativas múltiplas (I–IV)

**Enunciado:**
**Texto-Base:** "Regra fundamental: a palavra só é aceita se toda a entrada for consumida e o estado final for de aceitação." (slide 26)

**Situação-Problema:** O slide de revisão apresenta o autômato M = (Q, Σ, δ, q₀, F), com Q = {q₀, q₁, q₂}, Σ = {a, b}, estado inicial q₀, F = {q₂} e as transições δ(q₀, a) = q₁, δ(q₁, a) = q₂ e δ(q₁, b) = q₁.

**Dados de suporte:** [Diagrama: seta de entrada em q₀; q₀ —a→ q₁; laço em q₁ com rótulo b; q₁ —a→ q₂; q₂ em círculo duplo (aceitação). Nenhuma outra transição.] Considere que, quando não há transição definida para o par (estado, símbolo), a palavra é rejeitada.

I. Na 5-upla, δ é a função de transição, q₀ ∈ Q é o estado inicial e F = {q₂} ⊆ Q é o conjunto de estados de aceitação.

II. Tomadas isoladamente, as três transições não formam um AFD formalmente completo, pois faltam regras para pares de Q × Σ, como (q₀, b), (q₂, a) e (q₂, b).

III. A palavra abba é aceita, e a palavra aab é rejeitada, embora o autômato passe pelo estado q₂ durante a leitura de aab.

IV. A linguagem reconhecida por M é a das palavras sobre {a, b} que contêm a subcadeia aa.

**Comando:** É correto o que se afirma em:

**Alternativas:**
- **A)** I, II e III, apenas
- **B)** I e IV, apenas
- **C)** II e III, apenas
- **D)** I, II, III e IV

**Gabarito: A**

**Julgamento das afirmativas:**
- **I — Verdadeira.** É a leitura direta da 5-upla (slide 26; apostila p. 27).
- **II — Verdadeira.** Num AFD completo, δ: Q × Σ → Q tem **exatamente uma** transição por par. Aqui faltam (q₀, b), (q₂, a) e (q₂, b). A apostila diz isso na p. 28.
- **III — Verdadeira.** abba: q₀ —a→ q₁ —b→ q₁ —b→ q₁ —a→ q₂, e a entrada acaba em q₂ ∈ F, então **aceita**. aab: q₀ —a→ q₁ —a→ q₂, e em q₂ lendo b **não há transição**, então **rejeita**. Ter passado por q₂ não basta, porque a entrada não foi toda consumida (slide 26; p. 26, 32).
- **IV — Falsa.** L(M) = **ab\*a**: um a, zero ou mais b, um a (conferido por força bruta até comprimento 9). A linguagem "contém aa" é a do exemplo **completado** da apostila (p. 28), que tem δ(q₁, b) = q₀ e laços em q₂. Aqui baa, aaa e abab são rejeitadas.

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — I, II e III são verdadeiras.
- **B) ❌** — Inclui a IV, confundindo com o exemplo completo "aa", e omite II e III.
- **C) ❌** — Omite a I, que é a definição correta da 5-upla.
- **D) ❌** — Inclui a IV, que é falsa.

**Base no material:** slide p. 26–27 (5-upla; diagrama q₀ —a→ q₁ (laço b) —a→ q₂); apostila p. 27 (δ: Q × Σ → Q), p. 28 ("tomadas isoladamente, não formam a tabela completa de um AFD"), p. 34 (erro frequente "Confundir ausência de transição em um desenho parcial com comportamento formal de um AFD completo").
**Conceito-chave para a prova:** AF = (Q, Σ, δ, q₀, F). Num AFD completo há uma transição para **cada** par estado-símbolo. Num desenho parcial, a falta de transição significa rejeição. O AF do slide 27 reconhece ab\*a, a mesma expressão da Q3: é linguagem regular e cabe em AFD.

---

## I9 — Execução passo a passo do AFD que reconhece "aa"
**Subtópico coberto:** Execução passo a passo, configurações, linguagem reconhecida L(M) e "estado final não significa parada imediata" (apostila p. 28–29, 31–32).
**Por que é provável:** a apostila tem a tabela de transição (5.1), a execução de abaa (seção 6), a configuração (seção 7) e a seção 14 ("Estado final não significa parada imediata"). Há duas fixações (Q3 e Q4 da U3) sobre esse AFD e sobre passar por estado final.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única

**Enunciado:**
**Texto-Base:** "Uma máquina pode entrar em um estado final no meio da palavra e depois sair dele. Nesse caso, o que importa é o estado em que termina após a leitura completa."

**Situação-Problema:** Um analisador de logs usa o AFD abaixo para sinalizar registros que contêm a sequência aa (dois alertas consecutivos). Q = {q₀, q₁, q₂}, Σ = {a, b}, estado inicial q₀ e F = {q₂}.

**Dados de suporte:**

| Estado atual | Lê a | Lê b | Observação |
|---|---|---|---|
| q₀ | q₁ | q₀ | Ainda não encontramos 'aa'. |
| q₁ | q₂ | q₀ | Já vimos um 'a'; outro 'a' completa 'aa'. |
| q₂ | q₂ | q₂ | A sequência 'aa' já ocorreu; continuamos aceitando. |

**Comando:** Ao processar a palavra w = babaab, assinale a alternativa correta.

**Alternativas:**
- **A)** A palavra é rejeitada, pois, no estado q₁, ao ler b, o autômato permanece em q₁ e nunca alcança q₂.
- **B)** A palavra é aceita: a sequência de estados é q₀, q₀, q₁, q₀, q₁, q₂, q₂, e o autômato termina em q₂ ∈ F após consumir toda a entrada.
- **C)** A palavra é aceita no instante em que o autômato atinge q₂, ao ler o quinto símbolo, e o último b deixa de ser processado.
- **D)** A palavra é rejeitada, pois termina com o símbolo b, e o autômato só aceita palavras terminadas em aa.

**Gabarito: B**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Aqui δ(q₁, b) = q₀, não q₁. Confunde a tabela com o δ(q₁, b) = q₁ do slide 27.
- **B) ✅** — Configurações: (q₀, babaab) → (q₀, abaab) → (q₁, baab) → (q₀, aab) → (q₁, ab) → (q₂, b) → (q₂, ε). Toda a entrada foi consumida e q₂ ∈ F, então aceita. Simulado em Python.
- **C) ❌** — O resultado (aceita) coincide, mas o raciocínio está errado. Um AF **não para** ao atingir estado final; ele lê a entrada inteira (p. 26). Aqui q₂ "segura" a aceitação só porque tem laços em a e b, o que é "uma escolha do exemplo, não uma regra geral" (p. 32).
- **D) ❌** — L(M) é o conjunto das palavras que **contêm** aa em qualquer ponto, como bbaabb (p. 32), e não só as terminadas em aa.

**Base no material:** p. 28 (tabela 5.1), p. 29 (execução de abaa; abab rejeitada; configuração (q, entrada restante)), p. 31–32 (L(M); exemplos aa, aab, baa, abaa, bbaabb), p. 32 (seção 14).
**Conceito-chave para a prova:** aceitação em AF = entrada **toda** consumida **e** estado atual ∈ F. Nesse AFD, ler b em q₁ "zera" a busca (volta a q₀). Rejeitadas: bbb, abab, baba, ababa.

---

## I10 — AFD × AFND: poder de reconhecimento (asserção-razão)
**Subtópico coberto:** AFD × AFND e critério de aceitação do AFND (apostila p. 29–31; slide p. 28).
**Por que é provável:** o slide 28 é dedicado a isso, com o destaque "Equivalência Teórica". A apostila tem a tabela AFD × AFND (p. 31) e o erro frequente "Pensar que AFND reconhece mais linguagens que AFD" (p. 34), além da fixação Q2. O contraste com a Q4 (onde o AP **não determinístico** é o modelo exato das LLC) torna a pegadinha natural.
**Prioridade:** Alta
**Tipo ENADE:** Asserção-razão (4 alternativas, como na Q4 do squad)

**Enunciado:**
**Texto-Base:** "Equivalência Teórica: AFD e AFND têm o mesmo poder de reconhecimento. Um AFND pode ser convertido em um AFD equivalente, embora o AFD resultante possa ter mais estados." (slide 28)

**Situação-Problema:** Em um projeto de analisador léxico, um integrante da equipe propõe substituir todos os AFDs por AFNDs, argumentando que, por admitirem múltiplos caminhos, os AFNDs permitiriam reconhecer padrões de tokens que nenhum AFD reconhece.

Avalie as asserções a seguir e a relação proposta entre elas:

I. O AFND reconhece uma classe de linguagens mais ampla que a do AFD, pois pode explorar vários caminhos de execução para uma mesma entrada.

**PORQUE**

II. No AFND, uma palavra é aceita se pelo menos um caminho possível consumir toda a entrada e terminar em um estado de aceitação, mesmo que outros caminhos travem ou terminem em estados não finais.

A respeito dessas asserções, assinale a opção correta:

**Alternativas:**
- **A)** As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
- **B)** As asserções I e II são verdadeiras, mas a II não é justificativa da I.
- **C)** A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
- **D)** A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.

**Gabarito: D**

**Julgamento:**
- **Asserção I — Falsa.** AFD e AFND reconhecem **exatamente** as linguagens regulares. Todo AFND pode ser convertido em AFD equivalente (construção dos subconjuntos). O não determinismo dá compacidade, não poder (p. 31).
- **Asserção II — Verdadeira.** É o critério de aceitação do AFND (p. 30; slide 28).
- **Relação:** como I é falsa, não há justificativa a avaliar.

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Aceita a I, que é exatamente o erro frequente da p. 34.
- **B) ❌** — Também considera a I verdadeira.
- **C) ❌** — Inverte: a II é a definição correta de aceitação no AFND.
- **D) ✅** — I falsa (mesmo poder) e II verdadeira (critério "pelo menos um caminho").

**Base no material:** p. 29–30 (AFD: exatamente uma transição; AFND: δ: Q × Σ → P(Q)), p. 30 (seção 10, critério de aceitação), p. 31 (tabela; "ambos reconhecem exatamente as linguagens regulares"), p. 34 (erro frequente), slide p. 28.
**Conceito-chave para a prova:** em **autômato finito**, o não determinismo não aumenta o poder (AFD ≡ AFND ≡ ER). Em **autômato de pilha** é diferente: o modelo exato das LLC é o AP **não determinístico** (Q4, Q6).

---

## I11 — AFND e construção dos subconjuntos
**Subtópico coberto:** Conversão de AFND para AFD (construção dos subconjuntos, até 2ⁿ estados) e aceitação no AFND (apostila p. 30–31).
**Por que é provável:** a apostila dedica a seção 12 à conversão, com o exemplo do estado composto {q₁, q₂} e o limite 2ⁿ, e o slide 28 diz que "o AFD resultante possa ter mais estados". O squad gosta de questões com simulação (Q5).
**Prioridade:** Média
**Tipo ENADE:** Resposta única

**Enunciado:**
**Texto-Base:** "A ideia é que um estado do AFD resultante represente um conjunto de estados que o AFND poderia ocupar simultaneamente. [...] Como um conjunto com n estados possui até 2ⁿ subconjuntos, a conversão pode aumentar bastante o número de estados."

**Situação-Problema:** Para detectar quadros de dados que terminam com a sequência 01, um engenheiro desenhou o AFND N = ({p, q, r}, {0, 1}, δ, p, {r}).

**Dados de suporte:**

| Estado | Lê 0 | Lê 1 |
|---|---|---|
| p (inicial) | {p, q} | {p} |
| q | ∅ | {r} |
| r (final) | ∅ | ∅ |

[Diagrama: laço em p com 0 e 1; p —0→ q; q —1→ r; r em círculo duplo.]

**Comando:** Considerando o critério de aceitação do AFND e a construção dos subconjuntos, assinale a alternativa correta.

**Alternativas:**
- **A)** A palavra 1001 é rejeitada, pois existe um caminho de execução em que N permanece no estado p ao final da leitura.
- **B)** O AFD equivalente obtido pela construção dos subconjuntos terá obrigatoriamente 2³ = 8 estados.
- **C)** Após ler 0 a partir do estado inicial, o AFD equivalente passa ao estado composto {p, q}, e a palavra 1001 é aceita, pois algum caminho de N termina em r.
- **D)** N não é um autômato finito válido, pois para alguns pares estado-símbolo não há nenhuma transição definida.

**Gabarito: C**

**Resolução (conferida em Python):** conjuntos de estados ao ler 1001: {p} —1→ {p} —0→ {p, q} —0→ {p, q} —1→ {p, r}. Como r está no conjunto final, a palavra é **aceita**. AFD obtido (só estados alcançáveis): {p} (0 → {p,q}; 1 → {p}), {p,q} (0 → {p,q}; 1 → {p,r}), {p,r} (final; 0 → {p,q}; 1 → {p}). São **3** dos 8 subconjuntos possíveis. L(N) = (0│1)\*01.

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — No AFND basta **um** caminho aceitar. Caminhos que terminam em estado não final "não impedem a aceitação" (p. 30).
- **B) ❌** — 2ⁿ é o limite máximo ("até 2ⁿ"), não uma obrigação. Só os subconjuntos alcançáveis são necessários, e aqui são 3.
- **C) ✅** — δ(p, 0) = {p, q} vira o estado composto {p, q}, como no exemplo {q₁, q₂} da p. 31. 1001 é aceita pelo caminho p, p, p, q, r.
- **D) ❌** — No AFND um par estado-símbolo pode ter **zero**, uma ou várias transições (p. 30; tabela p. 31).

**Base no material:** p. 30 (δ: Q × Σ → P(Q); critério de aceitação), p. 31 (construção dos subconjuntos; estado composto {q₁, q₂}; até 2ⁿ estados), slide p. 28.
**Conceito-chave para a prova:** cada estado do AFD é um **conjunto** de estados do AFND, e é final se contém algum estado final. O tamanho pode chegar a 2ⁿ, mas não precisa. O AFND aceita se **algum** caminho aceitar.

---

# UNIDADE 4 — Autômatos de Pilha

## I12 — Definição formal do AP, Γ, Z₀ e memória LIFO
**Subtópico coberto:** Pilha LIFO e definição formal M = (Q, Σ, Γ, δ, q₀, Z₀, F) (apostila p. 36–37; slides p. 33–34).
**Por que é provável:** os slides 33 e 34 tratam disso. A apostila tem a tabela da 7-upla (p. 36) e os erros frequentes "Σ ≠ Γ → entrada ≠ pilha" e "Não usar Z₀ → perde controle do fim" (p. 45), além de duas fixações (Q1 e Q2 da U4: definição e sequência push/pop).
**Prioridade:** Alta
**Tipo ENADE:** Afirmativas múltiplas (I–IV)

**Enunciado:**
**Texto-Base:** "O símbolo Z₀ é colocado na pilha no início da computação e costuma funcionar como marcador de fundo. A função δ determina, a partir do estado atual, do símbolo lido e do símbolo no topo da pilha, qual será o próximo estado e o que será feito com o topo da pilha."

**Situação-Problema:** Um estudante revisa o modelo de autômato de pilha M = (Q, Σ, Γ, δ, q₀, Z₀, F) e testa a memória LIFO. Com a pilha contendo apenas Z₀, ele executa a sequência push A, push B, pop, push C, push A, pop (topo representado à esquerda). Em seguida, escreve:

I. Ao final da sequência de operações, a pilha contém CAZ₀, com C no topo.

II. Σ e Γ são necessariamente o mesmo alfabeto, pois os símbolos empilhados são sempre os próprios símbolos lidos da entrada.

III. Z₀ ∈ Γ é colocado na pilha no início da computação e funciona como marcador de fundo, o que permite ao autômato perceber quando a pilha voltou ao estado inicial.

IV. A pilha, por não ter tamanho limitado, permite registrar informações que um autômato finito não consegue reter, como a quantidade de símbolos já lidos.

**Comando:** É correto o que se afirma em:

**Alternativas:**
- **A)** I e II, apenas
- **B)** I, III e IV, apenas
- **C)** II e IV, apenas
- **D)** I, II, III e IV

**Gabarito: B**

**Julgamento das afirmativas:**
- **I — Verdadeira.** Z₀ → push A: AZ₀ → push B: BAZ₀ → pop: AZ₀ → push C: CAZ₀ → push A: ACAZ₀ → pop: **CAZ₀**. LIFO: o pop remove o último inserido.
- **II — Falsa.** Σ é o alfabeto de **entrada** e Γ o da **pilha**. Em geral são diferentes: nos exemplos se empilham A, P e Z₀, que não estão em Σ = {a, b} ou {(, )} (erro frequente "Σ ≠ Γ", p. 45).
- **III — Verdadeira.** É a definição de Z₀ (p. 36; slide 34: "Símbolo inicial na pilha (∈ Γ)"). A aceitação nos exemplos ocorre quando o topo volta a Z₀.
- **IV — Verdadeira.** p. 36: "A pilha, por não ter tamanho limitado, permite ao autômato registrar informações que um autômato finito não consegue reter, como a quantidade de símbolos já lidos."

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Inclui a II (confunde Σ com Γ) e omite III e IV.
- **B) ✅** — I, III e IV são verdadeiras.
- **C) ❌** — Inclui a II e omite I e III.
- **D) ❌** — "Todas" inclui a II, que é falsa.

**Base no material:** p. 36 (7-upla; Z₀ como marcador de fundo; pilha sem tamanho limitado), slide p. 33 (LIFO, push/pop), slide p. 34 (definição), p. 45 (erros frequentes), p. 46 (fixações Q1–Q2).
**Conceito-chave para a prova:** AP = 7-upla, que acrescenta ao AF **Γ** (alfabeto da pilha) e **Z₀** (fundo). Convenção da apostila: topo à esquerda. MT **não** tem Z₀.

---

## I13 — Transições do AP: push, pop e manter (associação)
**Subtópico coberto:** Transições do autômato de pilha na notação "entrada, topo → substituição": push, pop, manter, transição ε (apostila p. 37; aplicadas nas p. 38–44).
**Por que é provável:** a apostila tem a tabela "3.1 O que a substituição pode representar" (push/pop/manter) e a fixação Q3 da U4 pede exatamente para interpretar b, A → ε; a, Z₀ → AZ₀; ε, A → A. O squad já usou associação na Q6.
**Prioridade:** Média
**Tipo ENADE:** Associação de colunas

**Enunciado:**
**Texto-Base:** "Nesta unidade adota-se a notação informal acima, em que a cadeia à direita da seta substitui o símbolo do topo. Quando a entrada é ε, a transição ocorre sem consumir símbolo da palavra."

**Situação-Problema:** Ao implementar o validador de um protocolo com autômato de pilha, um desenvolvedor precisa documentar o efeito de cada transição usada no código (topo da pilha à esquerda).

**Comando:** Relacione cada transição da Coluna 1 ao seu efeito na Coluna 2:

| Coluna 1 (Transição: entrada, topo → substituição) | Coluna 2 (Efeito) |
|---|---|
| (1) a, Z₀ → AZ₀ | (P) Lê a e acrescenta dois símbolos A à pilha (o topo A é trocado por AAA). |
| (2) b, A → ε | (Q) Não consome símbolo da entrada e preserva o topo A. |
| (3) ε, A → A | (R) Lê b, exige A no topo e o remove da pilha (pop). |
| (4) a, A → AAA | (S) Lê a com o marcador de fundo no topo e empilha A sobre ele (push). |

Assinale a opção que apresenta a associação correta:

**Alternativas:**
- **A)** 1-S, 2-R, 3-Q, 4-P
- **B)** 1-P, 2-R, 3-S, 4-Q
- **C)** 1-S, 2-Q, 3-R, 4-P
- **D)** 1-R, 2-S, 3-Q, 4-P

**Gabarito: A**

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — (1) push: Z₀ é trocado por AZ₀, isto é, A fica sobre Z₀ (S). (2) pop: A é trocado por ε, isto é, removido (R). (3) entrada ε: não consome símbolo e o topo continua A (Q). (4) A é trocado por AAA, o que acrescenta dois A (P), como no exercício aⁿb²ⁿ da p. 43.
- **B) ❌** — Associa a, Z₀ → AZ₀ a "acrescenta dois A" e ε, A → A a um push. Ignora que a cadeia à direita **substitui** o topo.
- **C) ❌** — Troca pop por "não consome entrada": b, A → ε **lê b**. O ε à direita é que significa remover o topo.
- **D) ❌** — Inverte push e pop entre (1) e (2).

**Base no material:** p. 37 (notação; exemplo b, A → ε; tabela Push a, Z₀ → AZ₀ / Pop b, A → ε / Manter ε, A → A), p. 43 (a, A → AAA "acrescenta dois A"), p. 45 (erros "ε ≠ esvaziar tudo → remove só o topo"; "Transição ε não consome entrada").
**Conceito-chave para a prova:** ε **à direita** = pop (remove só o topo). ε **na entrada** = não consome símbolo. A cadeia à direita substitui o topo, então "X, T → YT" empilha Y.

---

## I14 — AP do slide 34 / Figura 2 (aⁿbⁿ, n ≥ 1)
**Subtópico coberto:** Exemplo de AP para aⁿbⁿ e evolução da pilha (apostila p. 38–39; diagrama do slide 34).
**Por que é provável:** é o único AP desenhado nos slides (slide 34, "Definição Formal e Exemplo") e a Figura 2 da apostila, com a tabela de transições, a evolução da pilha para aabb e os casos aab e abb (p. 38–39). A fixação Q4 da U4 pede justamente aaabbb, aab, abb, ba e ε.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única

**Enunciado:**
**Texto-Base:** "Autômatos de pilha não determinísticos reconhecem exatamente as linguagens livres de contexto. A pilha permite lidar com certas dependências que exigem memória não limitada, como comparar a quantidade de símbolos de duas partes da entrada." (slide 35)

**Situação-Problema:** Um analista modelou o autômato de pilha abaixo para validar sessões em que cada requisição (a) recebe exatamente uma resposta (b), na mesma ordem.

**Dados de suporte:** [Diagrama (slide 34 = Figura 2 da apostila, p. 38), notação "entrada, topo; substituição", com λ = ε e Z = Z₀: seta de entrada em q₀; q₀ —(λ, Z; Z)→ q₁; laço em q₁: (a, Z; AZ) e (a, A; AA); q₁ —(b, A; λ)→ q₂; laço em q₂: (b, A; λ); q₂ —(λ, Z; Z)→ q₃; q₃ em círculo duplo (estado final). Não há outras transições.]

**Comando:** Assinale a alternativa correta.

**Alternativas:**
- **A)** A palavra vazia é aceita, pois a transição λ, Z; Z leva de q₀ a q₁ sem consumir símbolo da entrada.
- **B)** Para a palavra aab, a entrada termina em q₂ com AZ na pilha, e a palavra é aceita, pois todos os símbolos foram lidos.
- **C)** A palavra abb é aceita, pois, após a leitura de ab, a pilha volta a Z e o autômato pode transitar para q₃ antes de ler o último b.
- **D)** Para aaabbb, após a leitura dos três a a pilha é AAAZ; cada b remove um A e, com Z novamente no topo, a transição λ, Z; Z leva a q₃, e a palavra é aceita.

**Gabarito: D**

**Simulação (conferida em Python com busca não determinística):** (q₀, aaabbb, Z) → (q₁, aaabbb, Z) → (q₁, aabbb, AZ) → (q₁, abbb, AAZ) → (q₁, bbb, AAAZ) → (q₂, bb, AAZ) → (q₂, b, AZ) → (q₂, ε, Z) → (q₃, ε, Z), **aceita**.

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — De q₁ não há transição λ para q₃. O autômato reconhece aⁿbⁿ com **n ≥ 1** (legenda da Figura 2). Para aceitar ε seria preciso acrescentar λ, Z; Z de q₁ para q₃ (p. 38).
- **B) ❌** — Sobra um A no topo, e λ, Z; Z exige Z. Não se chega a q₃, então **rejeita** (p. 39: "Para aab restaria um A na pilha"). Ler a entrada toda não basta.
- **C) ❌** — Chegar a q₃ com "b" ainda não lido não é aceitação; q₃ não tem transições. Na leitura, o 2º b encontra Z no topo em q₂ e não há transição b, Z: **rejeita** (p. 39).
- **D) ✅** — É exatamente a simulação acima.

**Base no material:** p. 38 (Figura 2, tabela de transições, observação n ≥ 1), p. 38–39 (evolução da pilha para aabb; rejeição de aab e abb), slide p. 34 (diagrama), p. 46 (fixação Q4).
**Conceito-chave para a prova:** o AP aceita quando a entrada acabou **e** se chega ao estado final, aqui com o topo voltando a Z. A sobra de A indica excesso de a; um b lido com Z no topo indica excesso de b. Este AP rejeita ε (n ≥ 1).

---

## I15 — Quais linguagens um AP reconhece ("compara dois grupos")
**Subtópico coberto:** Limitação dos AP (aⁿbⁿcⁿ) e regra prática para decidir se uma linguagem é reconhecida por AP (apostila p. 41–42, 44–45; slide p. 35).
**Por que é provável:** a apostila traz a explicação "Porque a pilha não basta" (p. 41), a Figura 4 e a lista "Alternativas que não resolvem o problema" (p. 42), além da tabela-resumo e do "Resumo mental: AP = 'compara dois grupos' e 3 grupos → não dá" (p. 44–45). A fixação Q6 da U4 pede exatamente isso. Hoje o tema só aparece num item da Q5.
**Prioridade:** Alta
**Tipo ENADE:** Afirmativas múltiplas (I–IV)

**Enunciado:**
**Texto-Base:** "Regra prática: Um autômato de pilha (AP) consegue comparar até duas quantidades. Se precisar comparar três ou mais, geralmente não é reconhecível."

**Situação-Problema:** A equipe de um compilador avalia se três formatos de bloco podem ser validados por um módulo baseado em autômato de pilha com uma única pilha:

- L₁ = { aⁿbᵐcⁿ │ n, m ≥ 0 }
- L₂ = { aⁿbᵐ │ m ≥ n ≥ 0 }
- L₃ = { aⁿbⁿcⁿ │ n ≥ 0 }

Avalie as afirmações:

I. L₁ pode ser reconhecida por AP: empilha-se um símbolo para cada a, os b são lidos sem alterar a pilha e desempilha-se um símbolo para cada c.

II. L₂ não pode ser reconhecida por AP, pois os b excedentes encontrariam Z₀ no topo e a computação seria necessariamente interrompida.

III. L₃ não pode ser reconhecida por AP: para comparar a quantidade de a com a de b é preciso desempilhar e, ao término dos b, a informação sobre n foi perdida, nada restando para comparar com os c.

IV. O uso de uma segunda pilha permitiria reconhecer L₃, mas o modelo deixaria de ser o autômato de pilha considerado, que possui uma única pilha.

**Comando:** É correto o que se afirma em:

**Alternativas:**
- **A)** I e III, apenas
- **B)** II e III, apenas
- **C)** I, III e IV, apenas
- **D)** I, II, III e IV

**Gabarito: C**

**Julgamento das afirmativas:**
- **I — Verdadeira.** Só se compara a com c; os b "não interferem" (tabela da p. 44: "aⁿbᵐcⁿ — Sim — compara a com c").
- **II — Falsa.** Basta prever a transição b, Z₀ → Z₀: quando a pilha volta a Z₀, os b excedentes são lidos sem desempilhar (p. 44: "aⁿbᵐ, com m ≥ n — Sim — b excedente não interfere"). Um AP assim foi conferido em Python até comprimento 9.
- **III — Verdadeira.** É o argumento da p. 41 ("Porque a pilha não basta") e da Figura 4 (p. 42).
- **IV — Verdadeira.** p. 42: "Usar uma segunda pilha: resolveria o problema, mas o modelo deixaria de ser o autômato de pilha considerado nesta unidade, que possui uma única pilha."

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Omite a IV, que é verdadeira.
- **B) ❌** — Inclui a II, sem notar que os b excedentes podem ser consumidos com Z₀ no topo, e omite I e IV.
- **C) ✅** — I, III e IV são verdadeiras.
- **D) ❌** — Inclui a II, que é falsa.

**Base no material:** p. 41 (seção 4.4, limitação e explicação), p. 42 (Figura 4; alternativas que não resolvem: não desempilhar, guardar n nos estados, segunda pilha), p. 44–45 (regra prática, tabela-resumo, "prova formal usa lema do bombeamento (CFL)"), slide p. 35.
**Conceito-chave para a prova:** com uma pilha dá para confrontar **duas** quantidades (aⁿbⁿ, aⁿb²ⁿ, aⁿbᵐcⁿ, aⁿbᵐ com m ≥ n), mas não **três** (aⁿbⁿcⁿ, que exige MT). A prova formal usa o lema do bombeamento para LLC.

---

## I16 — Exercício resolvido aⁿb²ⁿ (lacunas)
**Subtópico coberto:** Roteiro de construção de AP e exercício resolvido L = { aⁿb²ⁿ │ n ≥ 0 } (apostila p. 42–44).
**Por que é provável:** é o único "Exercício resolvido" do material, com roteiro, estratégia, tabela de transições, simulação de aabbbb e dois casos rejeitados (aabbb, abbb). Exercício resolvido costuma virar questão objetiva com pequena variação.
**Prioridade:** Alta
**Tipo ENADE:** Lacunas

**Enunciado:**
**Texto-Base:** "Identificar a dependência. Determinar qual informação precisa ser lembrada sem limite [...]. Definir a estratégia da pilha. [...] Conferir as transições ausentes. Quando não existe transição aplicável, a computação é interrompida e a palavra é rejeitada."

**Situação-Problema:** Um protocolo exige que cada requisição (a) seja seguida de exatamente duas confirmações (b), isto é, L = { aⁿb²ⁿ │ n ≥ 0 }. Na construção do autômato de pilha (estados q₀, q₁ e q₂ final; topo à esquerda), um estudante redigiu o texto a seguir.

"Para reconhecer L, empilham-se ______ símbolo(s) A para cada a lido e desempilha-se ______ A para cada b lido. Na palavra aabbbb, após a leitura dos dois a, a pilha contém ______. Já a palavra abbb é ______."

**Comando:** Assinale a alternativa que preenche corretamente as lacunas.

**Alternativas:**
- **A)** dois – um – AAAAZ₀ – rejeitada, pois o terceiro b encontra Z₀ no topo
- **B)** dois – um – AAZ₀ – aceita, pois a pilha volta a Z₀
- **C)** um – dois – AAZ₀ – rejeitada, pois sobra um A na pilha
- **D)** um – um – AAZ₀ – rejeitada, pois falta um b

**Gabarito: A**

**Simulação (solução da apostila, conferida em Python para todas as palavras sobre {a, b} até comprimento 9):**

| Passo | Estado | Entrada restante | Pilha | Transição |
|---|---|---|---|---|
| 0 | q₀ | aabbbb | Z₀ | início |
| 1 | q₀ | abbbb | AAZ₀ | a, Z₀ → AAZ₀ |
| 2 | q₀ | bbbb | **AAAAZ₀** | a, A → AAA |
| 3–6 | q₁ | bbb → ε | AAAZ₀ → Z₀ | b, A → ε (4 vezes) |
| 7 | q₂ | ε | Z₀ | ε, Z₀ → Z₀ → aceita |

abbb: (q₀, abbb, Z₀) → (q₀, bbb, AAZ₀) → (q₁, bb, AZ₀) → (q₁, b, Z₀). O 3º b encontra Z₀ e não há transição b, Z₀, então **rejeita** (excesso de b).

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — Dois A por a e um pop por b; após aa a pilha é AAAAZ₀; abbb é rejeitada por excesso de b (p. 44).
- **B) ❌** — Com dois A por a, a pilha após aa tem **quatro** A. E abbb não é aceita, porque tem 3 b para n = 1.
- **C) ❌** — "Um por a, dois por b" verificaria b = a/2, ou seja, a linguagem a²ⁿbⁿ, e não aⁿb²ⁿ.
- **D) ❌** — "Um por a, um por b" reconhece aⁿbⁿ. Além disso, abbb tem b demais, não de menos.

**Base no material:** p. 42–43 (roteiro 5.1), p. 43 (estratégia, estados, tabela de transições), p. 44 (simulação de aabbbb; aabbb rejeitada por falta de b; abbb rejeitada por excesso de b).
**Conceito-chave para a prova:** para aⁿbᵏⁿ, empilhe k símbolos por a e desempilhe 1 por b. A transição ε, Z₀ → Z₀ que sai de q₀ aceita n = 0. A rejeição é falta de transição; não há "estado de erro" (p. 45).

---

# UNIDADE 5 — Máquinas de Turing

## I17 — Definição formal da MT: Σ × Γ, branco e ausência de Z₀ (V/F)
**Subtópico coberto:** Máquina de Turing: componentes (controle finito, fita, cabeça), 6-upla, Σ × Γ, branco, δ (apostila p. 47–49; slides p. 39–40).
**Por que é provável:** os slides 39 e 40 tratam disso, e a apostila traz as tabelas de componentes e de definição, a observação "diferentemente do autômato de pilha, a MT não tem símbolo inicial de pilha (Z₀)" (p. 49) e os erros frequentes "Σ ≠ Γ", "Branco (␣) não está em Σ" e "Não existe Z₀ na MT" (p. 57). Há duas fixações (Q1 e Q2 da U5).
**Prioridade:** Alta
**Tipo ENADE:** Julgamento V/F com sequência

**Enunciado:**
**Texto-Base:** "A MT elimina essas restrições: sua fita é ilimitada e pode ser lida, escrita e percorrida nos dois sentidos, o que a torna capaz de executar qualquer algoritmo (SIPSER, 2007; HOPCROFT; MOTWANI; ULLMAN, 2002)."

**Situação-Problema:** Ao comparar os modelos estudados no semestre, um estudante descreveu a Máquina de Turing M = (Q, Σ, Γ, δ, q₀, F) por meio das afirmações abaixo.

**Analise as afirmações (V ou F):**

( ) Γ é o alfabeto da fita, com Σ ⊆ Γ, e o símbolo branco ␣ pertence a Γ, mas não a Σ.

( ) Assim como no autômato de pilha, a MT possui um símbolo inicial Z₀, que marca o fundo da fita.

( ) A função de transição tem a forma δ: Q × Γ → Q × Γ × {L, R}: em cada passo, a máquina lê um símbolo, escreve um símbolo, move a cabeça e muda de estado.

( ) Diferentemente da pilha, cujo acesso é só ao topo, a fita pode ser lida, reescrita e percorrida nos dois sentidos pela cabeça de leitura e escrita.

Sequência correta de cima para baixo:

**Alternativas:**
- **A)** V – V – V – F
- **B)** V – F – V – V
- **C)** F – F – V – V
- **D)** V – F – F – V

**Gabarito: B**

**Julgamento das afirmações:**
- **1 — Verdadeira.** Tabela da p. 48: "Γ: alfabeto da fita, com Σ ⊆ Γ e ␣ ∈ Γ \ Σ". Γ também contém marcas auxiliares, como X, Y, Z.
- **2 — Falsa.** "A MT não tem símbolo inicial de pilha (Z₀): a entrada já ocupa a fita" (p. 49; erro frequente p. 57).
- **3 — Verdadeira.** δ: Q × Γ → Q × Γ × {L, R} (p. 48). A ordem é lê → escreve → move (p. 49, 56).
- **4 — Verdadeira.** p. 54: "Diferentemente da pilha, cujo acesso é só ao topo, na MT os símbolos marcados [...] permanecem na fita e a cabeça pode voltar para relê-los."

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Aceita o Z₀ na MT (confusão com o AP) e nega o acesso bidirecional à fita.
- **B) ✅** — V–F–V–V.
- **C) ❌** — Nega o item 1, a relação correta entre Σ, Γ e o branco.
- **D) ❌** — Nega o item 3, a forma correta de δ.

**Base no material:** p. 47–48 (componentes: controle finito, fita, cabeça), p. 48 (tabela da definição; convenções de fita), p. 49 (sem Z₀; transição "lido → escrito, movimento"), p. 54 (papel da fita), p. 57 (erros frequentes), slides p. 39–41.
**Conceito-chave para a prova:** AF = 5-upla; AP = 7-upla (Γ = pilha, Z₀); MT = 6-upla (Γ = fita, com ␣ ∈ Γ \ Σ, e sem Z₀). Fita infinita só à direita ou nos dois sentidos dá o mesmo poder.

---

## I18 — Rejeitar × loop; reconhecer × decidir
**Subtópico coberto:** Aceitar, rejeitar e não parar (apostila p. 52; slide p. 42) e reconhecer × decidir, RE × recursivas (apostila p. 53; slides p. 43–44).
**Por que é provável:** a apostila destaca que "Essa distinção sustenta toda a teoria de decidibilidade" (p. 52), traz a tabela "Reconhecer / Decidir" (p. 53) e quatro "Erros frequentes" sobre isso (p. 56). Há duas fixações (Q3 e Q4 da U5). Hoje o tema só aparece no item II da Q5.
**Prioridade:** Alta
**Tipo ENADE:** Afirmativas múltiplas (I–IV)

**Enunciado:**
**Texto-Base:** "Dizer que rejeitar é 'não terminar em um estado de aceitação' é ambíguo, pois também descreve o loop. Rejeitar é parar sem aceitar; o loop é nunca parar. Essa distinção sustenta toda a teoria de decidibilidade."

**Situação-Problema:** Um professor apresentou duas Máquinas de Turing:

- **M₁**, sobre Σ = {a}, com as regras δ(q, a) = (q, a, R) e δ(q, ␣) = (q, ␣, R) e nenhum estado de aceitação alcançável;
- **M₂**, a MT da apostila para aⁿbⁿcⁿ, que a cada rodada marca um a como X, um b como Y e um c como Z, e na qual "qualquer situação não listada leva à rejeição".

Avalie as afirmações:

I. Para qualquer entrada, M₁ nunca para; por isso, tecnicamente, M₁ não rejeita as palavras — ela entra em loop.

II. Quando uma MT não possui transição definida para o par (estado, símbolo) atual, ela entra em loop.

III. M₂ decide a linguagem aⁿbⁿcⁿ, pois aceita toda palavra da linguagem, rejeita as demais e sempre para.

IV. Uma MT que aceita exatamente as palavras de L, mas entra em loop em algumas palavras fora de L, reconhece L, embora não a decida.

**Comando:** É correto o que se afirma em:

**Alternativas:**
- **A)** I e III, apenas
- **B)** II e IV, apenas
- **C)** I, II e III, apenas
- **D)** I, III e IV, apenas

**Gabarito: D**

**Julgamento das afirmativas:**
- **I — Verdadeira.** É o exemplo de loop da p. 52: a máquina percorre a fita para a direita indefinidamente. Rejeitar exige **parar**.
- **II — Falsa.** Sem transição definida, a MT **para e rejeita** (p. 52: "por atingir um estado de rejeição ou por não haver transição definida"). É a mesma pegadinha do item II da Q5.
- **III — Verdadeira.** p. 52–53: "Como cada rodada marca um símbolo de cada tipo e a fita usada é finita, a máquina termina para qualquer entrada"; "a linguagem é decidível, e não apenas reconhecível, pois a máquina sempre para".
- **IV — Verdadeira.** Definição de reconhecer (p. 53): aceita exatamente as palavras de L, e "nas demais, a máquina pode rejeitar ou entrar em loop".

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Omite a IV, que é a definição de reconhecer.
- **B) ❌** — Inclui a II (confunde falta de transição com loop) e omite I e III.
- **C) ❌** — Inclui a II, que é falsa, e omite a IV.
- **D) ✅** — I, III e IV são verdadeiras.

**Base no material:** p. 52 (tabela aceitar/rejeitar/não parar; observação sobre a ambiguidade; exemplo de loop), p. 53 (reconhecer × decidir; RE e recursivas; Regulares ⊂ LLC ⊂ Sensíveis ao contexto ⊂ Recursivas ⊂ RE), p. 56 (erros frequentes: "Rejeitar ≠ loop", "Nem toda não aceita é rejeitada", "Decidível ≠ reconhecível"), slides p. 42–44.
**Conceito-chave para a prova:** aceitar = entrar em estado de aceitação; rejeitar = **parar** sem aceitar; loop = **nunca parar**. Decidível ⊂ reconhecível (RE): toda linguagem decidível é reconhecível, mas a recíproca é falsa (HALT).

---

## I19 — Variantes da MT, Tese de Church-Turing e MT Universal (INCORRETA)
**Subtópico coberto:** Papel da fita, variantes da MT, Tese de Church-Turing e Máquina de Turing Universal (apostila p. 54; aplicações p. 57).
**Por que é provável:** a seção 4.3 da apostila é toda sobre isso, e os "Erros frequentes" (p. 57) listam "Variações da MT → mesmo poder (só muda eficiência)" e "Church-Turing = tese (não teorema)". Nenhuma questão conhecida cobra esse conteúdo; a Q6 só cita "MT Universal" como reconhecedor do Tipo 0.
**Prioridade:** Alta
**Tipo ENADE:** Afirmativa negativa (INCORRETA)

**Enunciado:**
**Texto-Base:** "[A Máquina de Turing] foi proposta por Alan Turing em 1936, no artigo em que ele respondeu negativamente ao Entscheidungsproblem (problema da decisão) de Hilbert, e formaliza a noção intuitiva de 'procedimento efetivo': uma sequência finita e mecânica de passos que transforma uma entrada em um resultado (TURING, 1936)."

**Situação-Problema:** Em um seminário sobre os fundamentos da computação, um grupo de estudantes apresentou conclusões sobre o alcance da Máquina de Turing e dos modelos equivalentes a ela.

**Comando:** Assinale a alternativa **INCORRETA**.

**Alternativas:**
- **A)** Variantes da MT — com várias fitas, com fita bidimensional, com cabeça que pode ficar parada ou com não determinismo — têm o mesmo poder computacional do modelo básico, embora possam diferir em eficiência.
- **B)** O cálculo lambda, as funções recursivas e as linguagens de programação usuais são equivalentes à MT, e essa convergência de modelos independentes sustenta a Tese de Church-Turing.
- **C)** A Tese de Church-Turing é um teorema formalmente demonstrado, pois a equivalência entre a MT e o cálculo lambda prova que a noção intuitiva de algoritmo coincide com o que uma MT executa.
- **D)** A Máquina de Turing Universal recebe a descrição de uma MT M e uma palavra w e simula M sobre w, ideia que antecipa o computador de programa armazenado.

**Gabarito: C**

**Por que cada alternativa está certa ou errada:**
- **A) ❌ (afirmação correta)** — p. 54: "Todas têm o mesmo poder computacional que o modelo básico, embora possam diferir em eficiência".
- **B) ❌ (afirmação correta)** — p. 54: "Essa convergência sustenta a Tese de Church-Turing".
- **C) ✅ (é a INCORRETA)** — "Por envolver uma noção intuitiva, a tese não é um teorema demonstrável, mas é amplamente aceita" (p. 54). A equivalência entre modelos formais é demonstrável, mas a identificação com a noção **intuitiva** de algoritmo não é. Erro frequente: "Church-Turing = tese (não teorema)" (p. 57).
- **D) ❌ (afirmação correta)** — p. 54 (TURING, 1936). A p. 57 acrescenta que ela antecipa interpretadores e máquinas virtuais.

**Base no material:** p. 47 (origem da MT), p. 54 (seções 4.2 e 4.3), p. 57 (erros frequentes e aplicações).
**Conceito-chave para a prova:** variantes da MT têm o mesmo poder e só mudam a eficiência. Church-Turing é **tese**, não teorema. A MT Universal simula qualquer MT a partir da descrição ⟨M⟩. O número de passos de uma MT é a base das classes P e NP (p. 57), o que é eficiência e não computabilidade.

---

## I20 — Problema da parada: reconhecível, mas não decidível (asserção-razão)
**Subtópico coberto:** Indecidibilidade e problema da parada (apostila p. 54–55; slide p. 44 "Linguagens Indecidíveis").
**Por que é provável:** o slide 44 é dedicado a isso, com destaque em caixa ("Indecidibilidade da Parada (Halting Problem)"). A apostila tem a seção 5.2 com a observação "HALT é reconhecível [...] não é decidível", e os erros frequentes trazem "Indecidível ≠ não reconhecível → problema da parada é reconhecível" (p. 56). Há a fixação Q8 da U5.
**Prioridade:** Alta
**Tipo ENADE:** Asserção-razão (4 alternativas, como na Q4 do squad)

**Enunciado:**
**Texto-Base:** "HALT = { ⟨M, w⟩ │ M é uma MT que para com a entrada w }. Não existe algoritmo geral que responda corretamente a essa pergunta para todos os programas e entradas possíveis: HALT é indecidível (TURING, 1936)."

**Situação-Problema:** Um juiz online (sistema de correção automática de programas) precisa saber se a submissão de um aluno termina para a entrada de teste. Um desenvolvedor propõe simplesmente executar (simular) o programa e aguardar o resultado.

Avalie as asserções a seguir e a relação proposta entre elas:

I. O problema da parada é reconhecível por Turing, mas não é decidível.

**PORQUE**

II. Simular M sobre w e aceitar quando a simulação parar garante a resposta "sim" sempre que M para; porém, quando M entra em loop, a simulação também não termina, e não há resposta "não" garantida.

A respeito dessas asserções, assinale a opção correta:

**Alternativas:**
- **A)** As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
- **B)** As asserções I e II são verdadeiras, mas a II não é justificativa da I.
- **C)** A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
- **D)** A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.

**Gabarito: A**

**Julgamento:**
- **Asserção I — Verdadeira.** HALT ∈ RE \ Recursivas (p. 55: "HALT é, portanto, um exemplo de linguagem reconhecível e não decidível").
- **Asserção II — Verdadeira.** É o raciocínio da p. 55: "basta simular M sobre w e aceitar se a simulação parar. Ele não é decidível porque, quando M entra em loop, a simulação também não termina."
- **Relação — II justifica I.** A primeira metade de II explica o "reconhecível" e a segunda explica por que a simulação não decide. (Que **nenhum** outro método decide é o que prova a contradição da I21.)

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — Ambas verdadeiras, e II é exatamente a explicação dada pelo material para I.
- **B) ❌** — II não é uma verdade isolada; é o motivo do "reconhecível, mas não decidível".
- **C) ❌** — Nega II, que é a descrição correta do comportamento da simulação.
- **D) ❌** — Nega I, que é o erro "indecidível ≠ não reconhecível" (p. 56).

**Base no material:** p. 54 (decidível × indecidível), p. 55 (HALT; observação final), p. 56 (erros frequentes), p. 57 ("é por isso que servidores e juízes online impõem limites de tempo"), slide p. 44.
**Conceito-chave para a prova:** HALT é **reconhecível** (simula e aceita se parar), mas **não decidível** (não há como garantir o "não"). Por isso juízes online usam limite de tempo. Existem ainda linguagens que **nem são reconhecíveis**: há uma quantidade enumerável de MTs e uma quantidade não enumerável de linguagens (p. 55).

---

## I21 — Ordenação da prova de indecidibilidade de HALT
**Subtópico coberto:** Prova por contradição (diagonalização) da indecidibilidade do problema da parada (apostila p. 55, tabela "Passo / Argumento").
**Por que é provável:** a apostila apresenta a prova numa tabela de 4 passos numerados, formato que se presta diretamente a uma questão de **ordenação** (tipo previsto no guia ENADE e ainda não usado pelo squad).
**Prioridade:** Média
**Tipo ENADE:** Ordenação

**Enunciado:**
**Texto-Base:** "A ideia da demonstração, por contradição, é a seguinte: [...]" (apostila, seção 5.2)

**Situação-Problema:** Para demonstrar que o problema da parada (HALT) é indecidível, um estudante escreveu as etapas da prova por contradição, mas fora de ordem:

1. Executar D sobre a sua própria descrição ⟨D⟩: se D para, H diz que D para e, por construção, D entra em loop; se D não para, H diz que D não para e, por construção, D para.
2. Concluir que a máquina H não existe e que, portanto, HALT é indecidível.
3. Supor que exista uma MT H que decida HALT: H aceita ⟨M, w⟩ se M para com w, rejeita caso contrário, e sempre para.
4. Construir uma máquina D que recebe ⟨M⟩, executa H sobre ⟨M, ⟨M⟩⟩ e faz o oposto do que H responde.
5. Constatar que os dois casos possíveis levam a uma contradição.

**Comando:** Assinale a alternativa que apresenta a ordem correta das etapas.

**Alternativas:**
- **A)** 3 – 1 – 4 – 5 – 2
- **B)** 3 – 4 – 1 – 5 – 2
- **C)** 4 – 3 – 1 – 2 – 5
- **D)** 4 – 1 – 3 – 5 – 2

**Gabarito: B**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Executa D (1) antes de construí-la (4).
- **B) ✅** — Hipótese (3) → construção de D a partir de H (4) → execução de D sobre ⟨D⟩ (1) → contradição nos dois casos (5) → H não existe (2). É a sequência dos passos 1–4 da tabela da p. 55.
- **C) ❌** — D depende de H, então não pode ser construída antes da hipótese de que H existe. E a conclusão (2) não pode vir antes da contradição (5).
- **D) ❌** — Constrói e executa D antes de supor a existência de H.

**Base no material:** p. 55 (tabela da prova: 1. suponha H; 2. construa D; 3. execute D sobre ⟨D⟩; 4. contradição, logo H não existe).
**Conceito-chave para a prova:** prova por contradição: supõe-se o decisor H, constrói-se D que "faz o oposto" e aplica-se D a ⟨D⟩. Qualquer resposta de H se contradiz, então H não existe.

---

## I22 — Consequências da indecidibilidade: redução, Rice e o "erro do colega"
**Subtópico coberto:** Consequências: redução, Teorema de Rice e aplicações em computação (apostila p. 55–57).
**Por que é provável:** a apostila tem a seção 5.3 "Consequências", a observação de que "o resultado não diz que é impossível saber se algum programa específico termina" (p. 55), as aplicações (compiladores, antivírus, C/Java/Python) na p. 57 e o erro frequente "não dá pra prever todos os programas, mas alguns sim". A fixação Q9 da U5 é exatamente o "erro do colega".
**Prioridade:** Média
**Tipo ENADE:** Afirmativas múltiplas (I–IV)

**Enunciado:**
**Texto-Base:** "Na prática, ferramentas de análise de programas precisam abrir mão de exatidão total, por aproximações ou por restrição a classes de programas."

**Situação-Problema:** Uma startup anuncia dois produtos: (1) um verificador que, para **qualquer** programa e **qualquer** entrada, informa com exatidão se o programa termina; (2) um comparador que decide se dois programas quaisquer são equivalentes. Ao comentar o anúncio, um colega afirma: "Como o problema da parada é indecidível, é impossível verificar se qualquer programa termina."

Avalie as afirmações:

I. Como C, Java e Python são mais poderosas que a Máquina de Turing, o verificador (1) seria viável se implementado nessas linguagens e executado com memória suficiente.

II. O verificador (1), na forma geral anunciada, não pode existir, pois decidiria HALT; o comparador (2) também é impossível em geral, o que se demonstra por redução.

III. A frase do colega é imprecisa: a indecidibilidade diz que não existe um único algoritmo geral que acerte para todos os casos, mas muitos programas específicos são analisáveis.

IV. O Teorema de Rice generaliza esses resultados: toda propriedade não trivial da linguagem reconhecida por uma MT é indecidível.

**Comando:** É correto o que se afirma em:

**Alternativas:**
- **A)** I e II, apenas
- **B)** III e IV, apenas
- **C)** II, III e IV, apenas
- **D)** I, II, III e IV

**Gabarito: C**

**Julgamento das afirmativas:**
- **I — Falsa.** "Linguagens como C, Java e Python têm o mesmo poder da MT e herdam suas limitações" (p. 57). Mais memória não resolve um problema indecidível.
- **II — Verdadeira.** Um verificador geral e exato seria um decisor de HALT, que não existe. "Assim se prova, por exemplo, que não é possível decidir se dois programas são equivalentes" (p. 56).
- **III — Verdadeira.** p. 55: "o resultado não diz que é impossível saber se algum programa específico termina; muitos são analisáveis. Ele diz que não existe um único algoritmo geral que acerte para todos." Um programa sem laços, por exemplo, termina.
- **IV — Verdadeira.** Enunciado do Teorema de Rice na p. 56 (HOPCROFT; MOTWANI; ULLMAN, 2002).

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Inclui a I (linguagens usuais têm o mesmo poder da MT) e omite III e IV.
- **B) ❌** — Omite a II, que é a consequência direta da indecidibilidade de HALT.
- **C) ✅** — II, III e IV são verdadeiras.
- **D) ❌** — "Todas" inclui a I, que é falsa.

**Base no material:** p. 55 (observação sobre programas específicos), p. 56 (5.3 Consequências: redução, equivalência de programas, Teorema de Rice, aproximações), p. 57 (aplicações; erro frequente "não dá pra prever todos os programas, mas alguns sim"), p. 58 (fixação Q9).
**Conceito-chave para a prova:** "indecidível" significa que não há algoritmo **geral**, e não que nenhum caso possa ser decidido. A indecidibilidade se propaga por redução (equivalência de programas; Rice). Ferramentas reais usam aproximações ou se restringem a classes de programas.
