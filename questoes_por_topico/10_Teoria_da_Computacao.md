# Teoria da Computação — Questões e Gabarito Comentado

**Squad responsável:** Squad 3 (Eder Vanzei, Gabriel Campari, Gabriel Imolene, Glenda Carvalho, João Maximiano, Lívia Mezashi)
**Materiais analisados:**
| Arquivo | Páginas | Tipo | Questões encontradas (páginas) |
|---|---|---|---|
| `Teoria da Computação - Revisão ENADE.pdf` | 50 | Slides | Q1–Q6: 6 questões objetivas ENADE, uma por unidade + 1 de síntese (enunciados nas p. 12, 22, 30, 36, 45–46, 48; gabarito oficial comentado nas p. 13, 23, 31, 37, 47, 49) |
| `Material de Estudos - Teoria da Computação.pdf` | 60 | Apostila / material de estudos | Q7–Q42: 1 questão "estilo ENADE" V/F (p. 11), 1 exercício resolvido (p. 43–44) e 34 questões de fixação discursivas (p. 11, 25, 35, 46, 57–58) |

**Resumo:** 42 questões encontradas: 6 objetivas no padrão ENADE nos slides, todas com 4 alternativas (A–D) e com gabarito oficial comentado; 36 na apostila (1 V/F estilo ENADE com gabarito, 1 exercício resolvido com solução, 34 questões de fixação discursivas). **8 têm gabarito ou solução dados pelo próprio material** (Q1–Q6, Q12, Q27). **34 não têm gabarito no material** e foram resolvidas aqui (Q7–Q11, Q13–Q26, Q28–Q42). Em várias delas a resposta está num exemplo da própria apostila, e isso está indicado em cada caso. Nenhum gabarito oficial está errado: todos foram conferidos de forma independente, com simulação em Python das Máquinas de Turing, dos autômatos de pilha, do AFD e da expressão regular, e com contagem de árvores de derivação da gramática da Q2. Os ⚠️ apontam imprecisões de redação, erros de digitação e pegadinhas.
As páginas só com imagem (slides p. 3, 14, 24, 32, 38) são capas de unidade ("UNIDADE 1 – Fundamentos de Conjuntos e Relações", "UNIDADE 2 – Linguagens Formais e Expressões", "UNIDADE 3 – Autômatos Finitos", "UNIDADE 4 – Autômatos de Pilha", "UNIDADE 5 – Máquinas de Turing") e não têm questões. O slide p. 11 ("Exemplos Estilo ENADE") traz só exemplos de relações reflexiva, simétrica, antissimétrica e transitiva, sem pergunta.

> Legenda: ✅ correta · ❌ incorreta · ⚠️ ponto de atenção (gabarito do material duvidoso, ambiguidade, versão divergente)

## Índice
**Parte A — Questões objetivas ENADE (slides)**

1. [Q1 — Conjuntos e relações: julgamento V/F](#q1--conjuntos-e-relações-julgamento-vf)
2. [Q2 — Linguagem com número igual de a e b: AFD, Tipo 2 e ambiguidade](#q2--linguagem-com-número-igual-de-a-e-b-afd-tipo-2-e-ambiguidade)
3. [Q3 — Limites do AFD: padrão ab*a × contagem aⁿbⁿ](#q3--limites-do-afd-padrão-aba--contagem-aⁿbⁿ)
4. [Q4 — Autômato de pilha para delimitadores aninhados (JSON-like)](#q4--autômato-de-pilha-para-delimitadores-aninhados-json-like)
5. [Q5 — Máquina de Turing para aⁿbⁿcⁿ: simulação de "aabbcc"](#q5--máquina-de-turing-para-aⁿbⁿcⁿ-simulação-de-aabbcc)
6. [Q6 — Hierarquia de Chomsky × modelo reconhecedor (associação)](#q6--hierarquia-de-chomsky--modelo-reconhecedor-associação)

**Parte B — Apostila (estilo ENADE, exercício resolvido e questões de fixação)**

7. [Q7 — Operações entre conjuntos A = {1,2,3} e B = {2,3,4}](#q7--operações-entre-conjuntos-a--123-e-b--234)
8. [Q8 — Por que ∅ e {∅} são diferentes](#q8--por-que--e--são-diferentes)
9. [Q9 — Subconjuntos de {a,b,c} (conjunto das partes)](#q9--subconjuntos-de-abc-conjunto-das-partes)
10. [Q10 — Propriedades de R = {(1,1),(2,2),(3,3),(1,2),(2,1)}](#q10--propriedades-de-r--1122331221)
11. [Q11 — Exemplo de relação antissimétrica e não simétrica](#q11--exemplo-de-relação-antissimétrica-e-não-simétrica)
12. [Q12 — Questão estilo ENADE (Unidade 1): conjuntos e propriedades de R](#q12--questão-estilo-enade-unidade-1-conjuntos-e-propriedades-de-r)
13. [Q13 — Palavras de comprimento 4 sobre Σ = {0,1}](#q13--palavras-de-comprimento-4-sobre-σ--01)
14. [Q14 — Diferença entre Σ, Σ*, ε e ∅](#q14--diferença-entre-σ-σ-ε-e-)
15. [Q15 — L² e exemplos de L* para L = {a,b}](#q15--l-e-exemplos-de-l-para-l--ab)
16. [Q16 — União, interseção e diferença de linguagens](#q16--união-interseção-e-diferença-de-linguagens)
17. [Q17 — Por que ε sempre pertence a L*](#q17--por-que-ε-sempre-pertence-a-l)
18. [Q18 — Pertinência à linguagem de (a|b)*(01|10)+](#q18--pertinência-à-linguagem-de-ab0110)
19. [Q19 — Componentes da gramática G = ({S,A},{0,1},P,S)](#q19--componentes-da-gramática-g--sa01ps)
20. [Q20 — Derivação de aaabbb em S → aSb | ε](#q20--derivação-de-aaabbb-em-s--asb--ε)
21. [Q21 — Componentes da 5-upla de um autômato finito](#q21--componentes-da-5-upla-de-um-autômato-finito)
22. [Q22 — AFD × AFND](#q22--afd--afnd)
23. [Q23 — Simulação do AFD que reconhece palavras com "aa"](#q23--simulação-do-afd-que-reconhece-palavras-com-aa)
24. [Q24 — Passar por estado final não basta para aceitar](#q24--passar-por-estado-final-não-basta-para-aceitar)
25. [Q25 — Por que {aⁿbⁿ | n ≥ 0} não é reconhecida por AFD](#q25--por-que-aⁿbⁿ--n--0-não-é-reconhecida-por-afd)
26. [Q26 — Informação finita × ilimitada na memória do AFD](#q26--informação-finita--ilimitada-na-memória-do-afd)
27. [Q27 — Exercício resolvido: autômato de pilha para L = { aⁿb²ⁿ | n ≥ 0 }](#q27--exercício-resolvido-autômato-de-pilha-para-l---aⁿbⁿ--n--0-)
28. [Q28 — Definição formal do autômato de pilha (papel de Γ e Z₀)](#q28--definição-formal-do-autômato-de-pilha-papel-de-γ-e-z)
29. [Q29 — Conteúdo da pilha após sequência de push/pop](#q29--conteúdo-da-pilha-após-sequência-de-pushpop)
30. [Q30 — Interpretar as transições b, A → ε; a, Z₀ → AZ₀; ε, A → A](#q30--interpretar-as-transições-b-a--ε-a-z--az-ε-a--a)
31. [Q31 — AP da Figura 2 (aⁿbⁿ, n ≥ 1): aaabbb, aab, abb, ba e ε](#q31--ap-da-figura-2-aⁿbⁿ-n--1-aaabbb-aab-abb-ba-e-ε)
32. [Q32 — AP de parênteses balanceados (Figura 3): (()) e )(](#q32--ap-de-parênteses-balanceados-figura-3--e-)
33. [Q33 — Quais linguagens são reconhecidas por autômato de pilha](#q33--quais-linguagens-são-reconhecidas-por-autômato-de-pilha)
34. [Q34 — Os três componentes de uma Máquina de Turing](#q34--os-três-componentes-de-uma-máquina-de-turing)
35. [Q35 — Definição formal da MT e diferença entre Σ e Γ](#q35--definição-formal-da-mt-e-diferença-entre-σ-e-γ)
36. [Q36 — Rejeitar × entrar em loop](#q36--rejeitar--entrar-em-loop)
37. [Q37 — Reconhecer × decidir uma linguagem](#q37--reconhecer--decidir-uma-linguagem)
38. [Q38 — Simular aabbcc na MT da Seção 2.3 (aⁿbⁿcⁿ)](#q38--simular-aabbcc-na-mt-da-seção-23-aⁿbⁿcⁿ)
39. [Q39 — Simular abcc na mesma MT (rejeição)](#q39--simular-abcc-na-mesma-mt-rejeição)
40. [Q40 — Construir MT que inverte bits (0↔1)](#q40--construir-mt-que-inverte-bits-01)
41. [Q41 — Problema da parada: reconhecível, mas não decidível](#q41--problema-da-parada-reconhecível-mas-não-decidível)
42. [Q42 — Erro na afirmação "é impossível verificar se qualquer programa termina"](#q42--erro-na-afirmação-é-impossível-verificar-se-qualquer-programa-termina)

---

# PARTE A — Questões objetivas ENADE (slides)

## Q1 — Conjuntos e relações: julgamento V/F
**Fonte:** `Teoria da Computação - Revisão ENADE.pdf`, p. 12 (enunciado) e p. 13 (gabarito oficial e análise)
**Tipo ENADE:** Julgamento V/F com sequência (resposta única)

**Enunciado:**
**Texto-Base:** "Na Teoria dos Conjuntos e Relações Binárias, a rigorosa formalização matemática de elementos, subconjuntos e propriedades constitui a base fundamental para a modelagem do espaço de estados em computação."

**Situação-Problema:** No estudo sobre um conjunto A = {1, 2, 3}, um estudante precisa avaliar o comportamento formal de diferentes relações e operações com conjuntos para validar a modelagem de um banco de dados relacional.

**Analise as afirmações (V ou F):**
[No slide as 4 afirmações estão numa grade 2×2. A ordem "de cima para baixo" usada no gabarito é a leitura linha a linha: 1 = superior esquerda, 2 = superior direita, 3 = inferior esquerda, 4 = inferior direita.]

( ) 1. O vazio ∅ é subconjunto de qualquer A (∅ ⊆ A). Mas a relação entre o vazio e o conjunto que o contém é de diferença: {∅} ≠ {}.

( ) 2. Seja U = {1, 2, 3, 4} o universo e A = {1, 4}. O complemento de A, dado por A' = U − A, resulta no conjunto {2, 3}.

( ) 3. Uma relação R definida em A é dita simétrica quando, para todo (x, y) ∈ R, obrigatoriamente se tem x = y.

( ) 4. Uma relação R em A é transitiva quando a ocorrência de (x, y) ∈ R e (y, z) ∈ R implica necessariamente que (x, z) ∈ R.

Sequência correta de cima para baixo:

**Alternativas:**
- **A)** V – V – F – V
- **B)** V – F – F – V
- **C)** F – V – V – F
- **D)** V – V – V – F

**Gabarito: A** — _(origem: gabarito do próprio material, slide p. 13)_

**Julgamento das afirmações:**
- **1 — Verdadeira.** O vazio é subconjunto de qualquer conjunto (não existe elemento de ∅ fora de A). Além disso, {} é o conjunto vazio (cardinalidade 0) e {∅} é um conjunto unitário cujo único elemento é o vazio (cardinalidade 1). Logo {∅} ≠ {}.
- **2 — Verdadeira.** A' = U − A = {1, 2, 3, 4} − {1, 4} = {2, 3}.
- **3 — Falsa.** Simetria exige (x, y) ∈ R ⇒ (y, x) ∈ R. Exigir x = y em todo par é outra condição (a relação ficaria contida na identidade/diagonal), não a definição de simetria. Contraexemplo: R = {(1,2), (2,1)} é simétrica e tem 1 ≠ 2.
- **4 — Verdadeira.** É a definição exata: (x,y) ∈ R ∧ (y,z) ∈ R ⇒ (x,z) ∈ R.

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — V–V–F–V coincide com o julgamento acima.
- **B) ❌** — Marca o item 2 como falso, contrariando a conta direta U − A = {2, 3}.
- **C) ❌** — Inverte quase tudo: nega que ∅ ⊆ A, aceita a definição errada de simetria e nega a definição correta de transitividade.
- **D) ❌** — Considera o item 3 verdadeiro (confunde simetria com igualdade x = y) e o item 4 falso.

**⚠️ Atenção:** (1) A ordem dos itens depende de ler a grade 2×2 linha a linha. Lida coluna a coluna (vazio, simétrica, complemento, transitiva), a sequência seria V–F–V–V, que não está entre as alternativas, o que confirma a leitura linha a linha. Na prova a ordem pode vir trocada; julgue cada afirmação pelo conteúdo. (2) A questão tem só 4 alternativas (A–D), enquanto o ENADE costuma usar 5.

**Conceito-chave para a prova:** ∅ ⊆ A sempre; ∅ ≠ {∅}; A' = U − A; simétrica: (x,y) ⇒ (y,x); antissimétrica: (x,y) e (y,x) ⇒ x = y; transitiva: (x,y) e (y,z) ⇒ (x,z).

---

## Q2 — Linguagem com número igual de a e b: AFD, Tipo 2 e ambiguidade
**Fonte:** `Teoria da Computação - Revisão ENADE.pdf`, p. 22 (enunciado) e p. 23 (gabarito oficial e análise)
**Tipo ENADE:** Afirmativas múltiplas (I, II, III)

**Enunciado:**
**Texto-Base:** A Hierarquia de Chomsky classifica as linguagens formais segundo a restrição de suas regras gramaticais. Linguagens que exigem a verificação de propriedades não locais ou contagens dependentes ultrapassam os limites do modelo regular, exigindo gramáticas mais expressivas ou gerando problemas inerentes de ambiguidade sintática.

**Situação-Problema:** Um estudante propôs a caracterização da linguagem L = { w ∈ {a,b}* | o número de 'a' em w é igual ao de 'b' } a fim de classificá-la formalmente. Para isso, ele elaborou as seguintes afirmações abaixo.

Avalie as afirmações do estudante:

I. A linguagem L pode ser reconhecida por um Autômato Finito Determinístico, pois basta alternar entre dois estados de contagem de paridade.

II. A linguagem L pertence à classe do Tipo 2 da Hierarquia de Chomsky, podendo ser gerada por regras de produção da forma V → w, onde V é um único símbolo não terminal e w(V)*.

III. Existe uma Gramática Livre de Contexto G = (V, Σ, R, S) não ambígua que gera a linguagem L.

Assinale a opção correta:

**Alternativas:**
- **A)** II e III, apenas
- **B)** I e III, apenas
- **C)** II, apenas
- **D)** I, II e III

**Gabarito: A** — _(origem: gabarito do próprio material, slide p. 23)_

**Julgamento das afirmações:**
- **I — Falsa.** Reconhecer L exige guardar a diferença #a − #b, que cresce sem limite. Um AFD tem memória finita, e dois estados de paridade só dizem se uma quantidade é par ou ímpar, sem comparar as duas. Pelo Lema do Bombeamento, a palavra aᵖbᵖ ∈ L bombeada dentro do bloco de a's dá palavras com mais a's que b's, fora de L. Logo L não é regular.
- **II — Verdadeira.** L é livre de contexto (Tipo 2): é gerada por regras com um único não terminal à esquerda, por exemplo S → aSbS | bSaS | ε (gramática do próprio slide). Conferido por força bruta até |w| = 10: essa gramática gera exatamente L.
- **III — Verdadeira.** O slide p. 23 dá uma GLC não ambígua, que decompõe cada palavra no primeiro ponto em que o saldo (#a − #b) volta a zero:
  - S → aBS | bAS | ε
  - A → a | bAA  (A gera palavras com um a a mais que b)
  - B → b | aBB  (B gera palavras com um b a mais que a)

  [Na p. 23 essas três regras saíram "espalhadas" pela diagramação; a transcrição acima é a leitura correta.] Conferido por força bruta: gera exatamente L e toda palavra de L até comprimento 10 tem **uma única** árvore de derivação. Já S → aSbS | bSaS | ε é ambígua (abab tem 2 árvores). Ou seja, a ambiguidade é da gramática, não da linguagem: L **não** é inerentemente ambígua.

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — Só II e III são verdadeiras.
- **B) ❌** — Inclui a I, ignorando que um AFD não mantém contagem ilimitada.
- **C) ❌** — Deixa de fora a III. A gramática mais comum (com "SS", ou S → aSbS | bSaS | ε) é ambígua, mas existe outra não ambígua para L.
- **D) ❌** — Inclui a I, que é falsa.

**⚠️ Atenção:** Na afirmativa II a notação saiu truncada ("w(V)*"). O correto é **w ∈ (V ∪ Σ)\***, isto é, w é qualquer cadeia de variáveis e terminais. O texto-base fala em "problemas inerentes de ambiguidade", mas L **não** é inerentemente ambígua, porque existe gramática não ambígua. Esse é o ponto da afirmativa III.

**Conceito-chave para a prova:** #a = #b (em qualquer ordem) e aⁿbⁿ não são regulares (AFD não conta sem limite), mas são livres de contexto (Tipo 2, reconhecidas por autômato de pilha). Ambiguidade é propriedade da gramática; uma linguagem só é "inerentemente ambígua" se todas as suas GLCs forem ambíguas.

---

## Q3 — Limites do AFD: padrão ab*a × contagem aⁿbⁿ
**Fonte:** `Teoria da Computação - Revisão ENADE.pdf`, p. 30 (enunciado) e p. 31 (gabarito oficial e análise)
**Tipo ENADE:** Resposta única

**Enunciado:**
**Texto-Base:** Os Autômatos Finitos Determinísticos (AFD) são modelos computacionais sem memória auxiliar, cujo poder de reconhecimento se limita às Linguagens Regulares. Qualquer validação sintática que exija armazenamento e comparação de contagens arbitrárias não pode ser resolvida exclusivamente por variações na quantidade finita de estados de um AFD.

**Situação-Problema:** Um engenheiro projetou um protocolo (handshake) com um AFD de 8 estados. Durante a validação, pediram-lhe duas novas funcionalidades:
- **Funcionalidade X:** Garantir que o protocolo rejeite mensagens com cabeçalho contendo sequências de controle malformadas do tipo **ab\*a** (um símbolo a, seguido de zero ou mais símbolos b, finalizado por um símbolo a).
- **Funcionalidade Y:** Garantir que o protocolo verifique se o número total de pacotes de dados enviados (**a**) é igual ao número total de confirmações de recebimento (**b**) recebidas ao longo de uma sessão de tamanho indeterminado, ou seja, validar palavras da forma **aⁿbⁿ** para qualquer **n ≥ 0**.

**Comando:** Considerando as limitações teóricas dos Autômatos Finitos e exigindo rigor técnico na modelagem, analise o cenário apresentado e avalie qual é a conclusão correta em relação às funcionalidades X e Y:

**Alternativas:**
- **A)** Ambas as funcionalidades (X e Y) podem ser implementadas expandindo o conjunto finito de estados do AFD atual.
- **B)** A funcionalidade X exige a transição do sistema para uma Máquina de Turing, enquanto a funcionalidade Y pode ser resolvida mantendo o AFD original.
- **C)** A funcionalidade X pode ser implementada diretamente pelo AFD atual, enquanto a funcionalidade Y não pode ser implementada por nenhum AFD, exigindo uma estrutura com memória de pilha.
- **D)** Nenhuma das duas funcionalidades (X ou Y) pode ser reconhecida por um autômato finito, pois ambas exigem contagem de símbolos.

**Gabarito: C** — _(origem: gabarito do próprio material, slide p. 31)_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Mais estados só permitem contar até um limite fixo. Para n indeterminado seriam necessários infinitos estados, então Y não se resolve assim.
- **B) ❌** — Inverte a complexidade: ab\*a é uma expressão regular simples (não precisa de MT), e aⁿbⁿ não pode ser resolvida por AFD.
- **C) ✅** — X: ab\*a é expressão regular, a linguagem é regular (Tipo 3) e um AFD resolve sem memória auxiliar. Rejeitar mensagens que contenham ab\*a também é regular, porque linguagens regulares são fechadas sob complemento e interseção. Y: aⁿbⁿ exige comparar duas contagens ilimitadas, não é regular, é livre de contexto e exige autômato de pilha.
- **D) ❌** — X não faz contagem comparativa: o "b\*" aceita qualquer quantidade sem comparar com nada.

**⚠️ Atenção:** (1) A expressão "implementada **diretamente pelo AFD atual**" na alternativa C é imprecisa. Na prática o AFD de 8 estados teria de ser modificado (produto com o AFD que detecta ab\*a, possivelmente com mais estados). O ponto cobrado é que **um AFD** basta, e C continua sendo a única correta. (2) O texto de Y diz "número de a igual ao de b", que em geral é a linguagem da Q2, mas depois fixa a forma aⁿbⁿ. Nos dois casos a linguagem não é regular, então a conclusão não muda. (3) No slide de resolução (p. 31) as fórmulas (ab\*a e aⁿbⁿ) não foram renderizadas e aparecem espaços em branco no texto.

**Conceito-chave para a prova:** Padrões descritos por expressão regular (inclusive com \*) são regulares e cabem em AFD. Comparar duas quantidades ilimitadas (aⁿbⁿ) exige pilha. Comparar três (aⁿbⁿcⁿ) exige Máquina de Turing.

---

## Q4 — Autômato de pilha para delimitadores aninhados (JSON-like)
**Fonte:** `Teoria da Computação - Revisão ENADE.pdf`, p. 36 (enunciado) e p. 37 (gabarito oficial e análise)
**Tipo ENADE:** Asserção-razão

**Enunciado:**
**Texto-Base:** "Autômatos de Pilha associam um controle finito de estados a uma estrutura de memória do tipo LIFO (Last In, First Out). Essa arquitetura permite o reconhecimento das Linguagens Livres de Contexto, essenciais para a verificação de estruturas aninhadas e balanceamento sintático em linguagens de programação e formatos de dados."

**Situação-Problema:** Uma equipe desenvolve o parser de um formato JSON-like que exige: 1. Todo { tem um }. 2. Todo [ tem um ]. 3. Delimitadores podem ser aninhados (ex.: {[[]]}), respeitando a ordem LIFO (o último aberto é o primeiro fechado).

Avalie as asserções a seguir e a relação proposta entre elas:

I. O módulo validador de delimitadores aninhados pode ser implementado por meio de um Autômato de Pilha Não Determinístico, pois a memória de pilha permite empilhar os símbolos de abertura ({ ou [) e desempilhá-los na ordem inversa conforme os símbolos de fechamento correspondentes são lidos.

PORQUE

II. O Autômato de Pilha é o modelo computacional exato que reconhece a classe das Linguagens Livres de Contexto, permitindo tratar dependências com memória ilimitada sob a regra LIFO, o que o torna ideal para a validação de parênteses, chaves e colchetes balanceados.

A respeito dessas asserções, assinale a opção correta:

**Alternativas:**
- **A)** As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
- **B)** As asserções I e II são verdadeiras, mas a II não é justificativa da I.
- **C)** A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
- **D)** A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.

**Gabarito: A** — _(origem: gabarito do próprio material, slide p. 37)_

**Julgamento:**
- **Asserção I — Verdadeira.** É assim que se validam estruturas aninhadas: cada abertura ({ ou [) é empilhada (push) e cada fechamento confere e desempilha o topo correspondente (pop). Ao final, a pilha deve estar só com o marcador de fundo.
- **Asserção II — Verdadeira.** Autômatos de pilha (não determinísticos) reconhecem exatamente as LLC, e a pilha dá memória ilimitada com disciplina LIFO.
- **Relação — II justifica I.** Estruturas balanceadas formam uma LLC, cujo reconhecedor equivalente é o autômato de pilha. Por isso a pilha consegue fazer a validação descrita em I.

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — Ambas verdadeiras e II é o fundamento teórico de I.
- **B) ❌** — II não é uma verdade isolada: é exatamente a razão formal pela qual a arquitetura de I funciona.
- **C) ❌** — Nega a equivalência AP ↔ LLC, que é um resultado clássico.
- **D) ❌** — Nega a mecânica padrão de push/pop para balanceamento.

**⚠️ Atenção:** (1) Só há 4 alternativas. Falta a usual "E) As asserções I e II são falsas". (2) Rigorosamente, a linguagem de delimitadores balanceados é **livre de contexto determinística**, então um AP **determinístico** também resolve. A asserção I continua verdadeira porque diz "pode ser implementado" com APN. A equivalência exata com as LLC vale para o AP **não determinístico**.

**Conceito-chave para a prova:** Aninhamento e balanceamento ({[()]}) ⇒ pilha (LIFO) ⇒ LLC (Tipo 2). APN ≡ GLC. Ver também Q32 (simulação do AP de parênteses da apostila).

---

## Q5 — Máquina de Turing para aⁿbⁿcⁿ: simulação de "aabbcc"
**Fonte:** `Teoria da Computação - Revisão ENADE.pdf`, p. 45 (texto-base, situação-problema e diagrama), p. 46 (comando, afirmativas e alternativas) e p. 47 (gabarito oficial). Relacionada às Q38 e Q39 da apostila, com uma MT quase idêntica (ver "Diferenças entre versões").
**Tipo ENADE:** Afirmativas múltiplas (I–IV)

**Enunciado:**
**Texto-Base:** "Uma Máquina de Turing de Fita Única é formalizada como uma 6-tupla M=(Q, Σ, Γ, δ, q0, F). A função de transição determina o determinismo da execução, modificando o símbolo da fita e deslocando a cabeça de leitura/escrita. Estruturas sintáticas que exigem verificação de contagens cruzadas do tipo aⁿbⁿcⁿ excedem a capacidade de Autômatos de Pilha, exigindo o poder computacional irrestrito de uma Máquina de Turing"

**Situação-Problema:** Um analista de sistemas está a projetar um reconhecedor para a linguagem dependente do contexto L = { aⁿbⁿcⁿ | n ≥ 1} sobre o alfabeto ={a,b,c}. O diagrama a seguir representa o autômato de controle da Máquina de Turing M modelada para esta tarefa:

[Figura — diagrama de estados da MT M. Estados q0 (inicial, seta de entrada), q1, q2, q3, q4 e qf (círculo duplo = aceitação). Rótulos no formato "lido/escrito, direção":
- q0 → q1: **a/X, D**
- q1 → q1 (laço): **a/a, D** e **Y/Y, D**
- q1 → q2: **b/Y, D**
- q2 → q2 (laço): **b/b, D** e **Z/Z, D**
- q2 → q3: **c/Z, E**
- q3 → q3 (laço): **a/a, E | b/b, E | Y/Y, E | Z/Z, E**
- q3 → q0 (arco superior de volta): **X/X, D**
- q0 → q4: **Y/Y, D**
- q4 → q4 (laço): **Y/Y, D** e **Z/Z, D**
- q4 → qf: **B/B, D**

Não há nenhuma outra transição: q0 não tem transição para B, e q1 não tem transição para X, Z, c ou B.]

| Estado | a | b | c | X | Y | Z | B |
|---|---|---|---|---|---|---|---|
| q0 | X, D, q1 | — | — | — | Y, D, q4 | — | — |
| q1 | a, D, q1 | Y, D, q2 | — | — | Y, D, q1 | — | — |
| q2 | — | b, D, q2 | Z, E, q3 | — | — | Z, D, q2 | — |
| q3 | a, E, q3 | b, E, q3 | — | X, D, q0 | Y, E, q3 | Z, E, q3 | — |
| q4 | — | — | — | — | Y, D, q4 | Z, D, q4 | B, D, qf |
| qf | (aceitação) | | | | | | |

**Observação (do slide):** As transições seguem o formato "SímboloLido / SímboloEscrito, Direção", onde D representa deslocamento para a direita e E para a esquerda. O símbolo B representa Branco ou Blank. Considere que a fita de M é inicializada com a palavra "aabbcc" seguida de infinitos símbolos brancos B, e que a cabeça de leitura encontra-se posicionada no primeiro caractere 'a'.

**Comando:** Com base no funcionamento da Máquina de Turing M, avalie as afirmações a seguir:

I. Após a primeira transição de retorno ao estado q0 (conclusão do primeiro ciclo completo), a fita conterá a sequência "XaYbZc".

II. Na entrada "aabbcc", a máquina M entrará em ciclo infinito (loop) ao tentar processar o segundo símbolo 'a', pois não há transição definida para o caractere 'X' no estado q1.

III. A linguagem reconhecida por M não pode ser reconhecida por nenhum Autômato de Pilha Determinístico ou Não Determinístico.

IV. A máquina M aceitará com sucesso a palavra "aabbcc", terminando a sua execução no estado final de aceitação qf.

É correto apenas o que se afirma em:

**Alternativas:**
- **A)** I e ll _(sic)_
- **B)** I e III, apenas
- **C)** Todas as alternativas _(sic)_
- **D)** I, III e IV

**Gabarito: D** — _(origem: gabarito do próprio material, slide p. 47)_

**Simulação completa (conferida em Python; cabeça entre colchetes):**

| Passo | Estado | Fita | Passo | Estado | Fita |
|---|---|---|---|---|---|
| 0 | q0 | [a]abbcc | 12 | q2 | XXYY[Z]c |
| 1 | q1 | X[a]bbcc | 13 | q2 | XXYYZ[c] |
| 2 | q1 | Xa[b]bcc | 14 | q3 | XXYY[Z]Z |
| 3 | q2 | XaY[b]cc | 15 | q3 | XXY[Y]ZZ |
| 4 | q2 | XaYb[c]c | 16 | q3 | XX[Y]YZZ |
| 5 | q3 | XaY[b]Zc | 17 | q3 | X[X]YYZZ |
| 6 | q3 | Xa[Y]bZc | 18 | q0 | XX[Y]YZZ |
| 7 | q3 | X[a]YbZc | 19 | q4 | XXY[Y]ZZ |
| 8 | q3 | [X]aYbZc | 20 | q4 | XXYY[Z]Z |
| 9 | **q0** | **X[a]YbZc** ← fim do 1º ciclo | 21 | q4 | XXYYZ[Z] |
| 10 | q1 | XX[Y]bZc | 22 | q4 | XXYYZZ[B] |
| 11 | q1 | XXY[b]Zc | 23 | **qf** | XXYYZZB[B] → ACEITA |

**Julgamento das afirmações:**
- **I — Verdadeira.** No passo 9 a máquina volta a q0 com a fita XaYbZc (primeiro a → X, primeiro b → Y, primeiro c → Z) e a cabeça sobre o segundo a.
- **II — Falsa.** Depois do retorno (q3 → q0) a cabeça está sobre o segundo a **em q0**, não em q1, então a máquina nunca lê X em q1. Além disso, ausência de transição faz a MT **parar e rejeitar**; não causa loop.
- **III — Verdadeira.** L(M) = {aⁿbⁿcⁿ | n ≥ 1}. Conferido por força bruta para todas as palavras sobre {a,b,c} até comprimento 9: M aceita exatamente essas e sempre para. Essa linguagem não é livre de contexto (lema do bombeamento para LLC). Uma única pilha compara duas quantidades, não três. Logo nenhum AP, determinístico ou não, a reconhece.
- **IV — Verdadeira.** Após dois ciclos a fita fica XXYYZZ. Em q0, lendo Y, vai a q4, percorre Y e Z e, ao ler B, vai a qf (passo 23).

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Inclui a II, que é falsa.
- **B) ❌** — Omite a IV, que é verdadeira.
- **C) ❌** — "Todas" incluiria a II, que é falsa.
- **D) ✅** — I, III e IV são verdadeiras e II é falsa.

**Diferenças entre versões:** A MT da apostila (Seção 2.3, p. 50–51, usada nas Q38/Q39) é **a mesma** desta questão, com quatro diferenças de notação ou detalhe: (1) usa R/L em vez de D/E; (2) usa ␣ para o branco em vez de B; (3) chama o estado de aceitação de **qacc** em vez de qf; (4) tem uma transição a mais, **q0: ␣ → ␣, R (qacc)**, que aceita a palavra vazia. Assim, a apostila decide aⁿbⁿcⁿ com **n ≥ 0**, enquanto o slide reconhece só **n ≥ 1** (a palavra vazia é rejeitada por falta de transição em q0 lendo B). As duas simulações de aabbcc são idênticas passo a passo (23 passos, aceita).

**⚠️ Atenção:** (1) Alternativa A está escrita "I e ll" (com letras L minúsculas e sem "apenas"). Alternativa C diz "Todas as alternativas" quando deveria ser "afirmativas", e contradiz o comando "É correto **apenas**...". (2) O enunciado traz "sobre o alfabeto ={a,b,c}" (falta o Σ). (3) Pegadinha frequente: "não há transição" ≠ "loop". Numa MT, ausência de transição é parada com rejeição. (4) Só 4 alternativas.

**Conceito-chave para a prova:** A MT para aⁿbⁿcⁿ marca a→X, b→Y, c→Z por rodada e volta até o X. Quando q0 lê Y, confere que só restam Y/Z até o branco. aⁿbⁿcⁿ é sensível ao contexto (Tipo 1), não é LLC, e é decidível.

---

## Q6 — Hierarquia de Chomsky × modelo reconhecedor (associação)
**Fonte:** `Teoria da Computação - Revisão ENADE.pdf`, p. 48 (enunciado) e p. 49 (gabarito oficial e análise)
**Tipo ENADE:** Associação de colunas

**Enunciado:**
**Dado de Suporte (Texto-Base):** "A Hierarquia de Chomsky organiza as linguagens formais em quatro níveis de complexidade sintática (Tipo 3, Tipo 2, Tipo 1 e Tipo 0), estabelecendo uma correspondência biunívoca entre a gramática geradora e a classe do autômato reconhecedor associado."

**Situação-Problema:** Um arquiteto de linguagens de programação precisa selecionar o modelo de autômato adequado para cada etapa do processamento de um compilador, correlacionando os níveis da Hierarquia de Chomsky aos seus respectivos modelos computacionais.

**Comando:** Relacione a classe de linguagem da Coluna 1 ao seu respectivo autômato/reconhecedor exato na Coluna 2:

| Coluna 1 (Classe da Linguagem) | Coluna 2 (Modelo Reconhecedor) |
|---|---|
| (1) Linguagens Regulares (Tipo 3) | (A) Autômato de Pilha Não Determinístico |
| (2) Linguagens Livres de Contexto (Tipo 2) | (B) Máquina de Turing com Limite Linear (LBA) |
| (3) Linguagens Sensíveis ao Contexto (Tipo 1) | (C) Autômato Finito (Determinístico ou Não) |
| (4) Linguagens Recursivamente Enumeráveis (Tipo 0) | (D) Máquina de Turing Universal |

Assinale a opção que apresenta a associação correta:

**Alternativas:**
- **A)** 1-A, 2-C, 3-D, 4-B
- **B)** 1-B, 2-A, 3-C, 4-D
- **C)** 1-C, 2-D, 3-B, 4-A
- **D)** 1-C, 2-A, 3-B, 4-D

**Gabarito: D** — _(origem: gabarito do próprio material, slide p. 49)_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Troca os reconhecedores do Tipo 3 (põe AP) e do Tipo 2 (põe AF), e também troca LBA e MT.
- **B) ❌** — Associa regulares a LBA e sensíveis ao contexto a autômato finito.
- **C) ❌** — Associa LLC à Máquina de Turing e Tipo 0 a autômato de pilha.
- **D) ✅** — 1-C (regulares ↔ AFD/AFND), 2-A (LLC ↔ AP não determinístico), 3-B (sensíveis ao contexto ↔ autômato linearmente limitado, LBA), 4-D (recursivamente enumeráveis ↔ Máquina de Turing).

**⚠️ Atenção:** (1) As letras da Coluna 2 (A–D) coincidem com as letras das alternativas (A–D). Não confunda "4-D" com "alternativa D". (2) "Máquina de Turing **Universal**" para o Tipo 0 é impreciso: as linguagens RE são as reconhecidas por **alguma** Máquina de Turing (padrão, sem restrição). A MT Universal é uma MT específica que simula outras. A apostila (p. 21) usa só "Máquinas de Turing". (3) LBA = autômato linearmente limitado, que o slide chama de "Máquina de Turing com Limite Linear". (4) Só 4 alternativas.

**Conceito-chave para a prova:** Tipo 3 ↔ AF/ER; Tipo 2 ↔ AP (não determinístico)/GLC; Tipo 1 ↔ LBA; Tipo 0 ↔ MT. Inclusões: Regulares ⊂ LLC ⊂ Sensíveis ao contexto ⊂ Recursivas ⊂ RE.

---

# PARTE B — Apostila: questões estilo ENADE, exercício resolvido e questões de fixação

## Q7 — Operações entre conjuntos A = {1,2,3} e B = {2,3,4}
**Fonte:** `Material de Estudos - Teoria da Computação.pdf`, p. 11 (Unidade 1, "13. Questões de fixação", Questão 1)
**Tipo ENADE:** Discursiva / exercício de fixação

**Enunciado:**
Questão 1. Considere A = {1,2,3} e B = {2,3,4}. Determine A ∪ B, A ∩ B, A − B e B − A.

**Resposta esperada:** _(não consta no material — resolvido aqui)_
- A ∪ B = {1, 2, 3, 4}
- A ∩ B = {2, 3}
- A − B = {1}
- B − A = {4}

A diferença não é comutativa (A − B ≠ B − A), enquanto união e interseção são.

**Conceito-chave para a prova:** União = está em A ou em B; interseção = está nos dois; diferença A − B = está em A e não em B (a ordem importa). Ver também a Q12 (mesmos conjuntos).

---

## Q8 — Por que ∅ e {∅} são diferentes
**Fonte:** `Material de Estudos - Teoria da Computação.pdf`, p. 11 (Unidade 1, Questões de fixação, Questão 2)
**Tipo ENADE:** Discursiva

**Enunciado:**
Questão 2. Explique por que ∅ e {∅} não representam o mesmo conjunto.

**Resposta esperada:** _(não consta no material — resolvido aqui; base na apostila p. 4)_
∅ = {} não tem nenhum elemento (|∅| = 0). {∅} é um conjunto com **um** elemento, e esse elemento é o próprio conjunto vazio (|{∅}| = 1). Como têm cardinalidades diferentes, não são iguais. Vale ∅ ∈ {∅} e ∅ ⊆ {∅}, mas ∅ ∉ ∅.

**Conceito-chave para a prova:** ∅ ≠ {∅}; ∅ é subconjunto de qualquer conjunto, mas só é **elemento** de conjuntos que o contêm explicitamente (cobrado também na Q1, item 1).

---

## Q9 — Subconjuntos de {a,b,c} (conjunto das partes)
**Fonte:** `Material de Estudos - Teoria da Computação.pdf`, p. 11 (Unidade 1, Questões de fixação, Questão 3)
**Tipo ENADE:** Discursiva

**Enunciado:**
Questão 3. Se A = {a,b,c}, liste todos os subconjuntos de A e confirme que a quantidade é 2³.

**Resposta esperada:** _(não consta no material — resolvido aqui)_
P(A) = { ∅, {a}, {b}, {c}, {a,b}, {a,c}, {b,c}, {a,b,c} }: são 8 subconjuntos = 2³ (cada elemento está ou não está no subconjunto, 2 escolhas por elemento).

**Conceito-chave para a prova:** |P(A)| = 2ⁿ para |A| = n; ∅ e o próprio A estão sempre em P(A).

---

## Q10 — Propriedades de R = {(1,1),(2,2),(3,3),(1,2),(2,1)}
**Fonte:** `Material de Estudos - Teoria da Computação.pdf`, p. 11 (Unidade 1, Questões de fixação, Questão 4). A mesma relação aparece no "10. Exemplo completo de análise" (p. 10) e na Q12.
**Tipo ENADE:** Discursiva

**Enunciado:**
Questão 4. Considere A = {1,2,3} e R = {(1,1),(2,2),(3,3),(1,2),(2,1)}. Classifique R quanto às propriedades reflexiva, simétrica, antissimétrica e transitiva.

**Resposta esperada:** _(sem gabarito na seção de questões; a resposta está no exemplo resolvido da p. 10)_
- **Reflexiva: sim.** Contém (1,1), (2,2) e (3,3).
- **Simétrica: sim.** (1,2) tem o inverso (2,1); os pares (x,x) são seus próprios inversos.
- **Antissimétrica: não.** (1,2) e (2,1) estão em R com 1 ≠ 2.
- **Transitiva: sim.** (1,2),(2,1) ⇒ (1,1) ∈ R; (2,1),(1,2) ⇒ (2,2) ∈ R. As demais cadeias envolvem pares (x,x) e não geram exigência ausente.

Conclusão: R é reflexiva, simétrica e transitiva (relação de equivalência), mas não antissimétrica.

**Conceito-chave para a prova:** Para a transitividade, confira **todas** as cadeias (x,y),(y,z). Um par de ida e volta com x ≠ y derruba a antissimetria.

---

## Q11 — Exemplo de relação antissimétrica e não simétrica
**Fonte:** `Material de Estudos - Teoria da Computação.pdf`, p. 11 (Unidade 1, Questões de fixação, Questão 5)
**Tipo ENADE:** Discursiva

**Enunciado:**
Questão 5. Dê um exemplo de uma relação que seja antissimétrica, mas não simétrica.

**Resposta esperada:** _(não consta no material — resolvido aqui)_
Em A = {1,2,3}: R = {(1,1), (2,2), (3,3), (1,2)}, exemplo da própria apostila na p. 9. É antissimétrica porque não há par de ida e volta com elementos diferentes, e não é simétrica porque (1,2) ∈ R mas (2,1) ∉ R. Outro exemplo é a relação ≤ nos números. Exemplo mínimo: R = {(1,2)}.

**Conceito-chave para a prova:** Antissimétrica não é o mesmo que "não simétrica". Uma relação só com pares (x,x) é simétrica **e** antissimétrica ao mesmo tempo.

---

## Q12 — Questão estilo ENADE (Unidade 1): conjuntos e propriedades de R
**Fonte:** `Material de Estudos - Teoria da Computação.pdf`, p. 11 (Unidade 1, "14. Questão estilo ENADE")
**Tipo ENADE:** Julgamento V/F de afirmativas (sem alternativas A–E)

**Enunciado:**
Considere os conjuntos A = {1,2,3}, B = {2,3,4} e a relação R = {(1,1),(2,2),(3,3),(1,2),(2,1)} definida sobre A. Analise as afirmações:
- I. A ∪ B = {1,2,3,4}.
- II. A ∩ B = {2,3}.
- III. A − B = {1}.
- IV. R é reflexiva.
- V. R é simétrica.
- VI. R é antissimétrica.

**Gabarito (sequência): V, V, V, V, V, F** — _(origem: gabarito do próprio material, p. 11)_

**Julgamento das afirmações (conferido):**
- **I — Verdadeira.** {1,2,3} ∪ {2,3,4} = {1,2,3,4}.
- **II — Verdadeira.** Elementos comuns: 2 e 3.
- **III — Verdadeira.** Em A e não em B: só o 1.
- **IV — Verdadeira.** Contém (1,1), (2,2), (3,3).
- **V — Verdadeira.** (1,2) e (2,1) aparecem juntos.
- **VI — Falsa.** (1,2) e (2,1) com 1 ≠ 2 violam a antissimetria.

**Justificativa do material:** "As três primeiras afirmações seguem diretamente das operações entre conjuntos. R é reflexiva porque contém (1,1), (2,2) e (3,3). É simétrica porque (1,2) e (2,1) aparecem simultaneamente. Não é antissimétrica porque 1 ≠ 2 e, mesmo assim, os dois sentidos da relação estão presentes."

**⚠️ Atenção:** A questão não tem alternativas. Na prova deve virar algo como "é correto o que se afirma em I, II, III, IV e V, apenas" ou uma sequência V/F. Se a prova trocar III para "A − B = {1, 4}" ou VI para "transitiva", a resposta muda: A − B = {1}, e R **é** transitiva (ver Q10).

**Conceito-chave para a prova:** Mesmos dados das Q7 e Q10: A∪B = {1,2,3,4}, A∩B = {2,3}, A−B = {1}, B−A = {4}; R é de equivalência e não é antissimétrica.

---

## Q13 — Palavras de comprimento 4 sobre Σ = {0,1}
**Fonte:** `Material de Estudos - Teoria da Computação.pdf`, p. 25 (Unidade 2, "21. Questões de fixação", Questão 1)
**Tipo ENADE:** Discursiva

**Enunciado:**
Questão 1. Considere Σ = {0,1}. Dê três palavras de comprimento 4 pertencentes a Σ* e determine o comprimento de cada uma.

**Resposta esperada:** _(não consta no material — resolvido aqui)_
Por exemplo, w₁ = 0000, w₂ = 0101, w₃ = 1101, com |w₁| = |w₂| = |w₃| = 4. Existem 2⁴ = 16 palavras de comprimento 4 sobre {0,1}.

**Conceito-chave para a prova:** |w| = número de símbolos (com repetição); há |Σ|ⁿ palavras de comprimento n.

---

## Q14 — Diferença entre Σ, Σ*, ε e ∅
**Fonte:** `Material de Estudos - Teoria da Computação.pdf`, p. 25 (Unidade 2, Questões de fixação, Questão 2)
**Tipo ENADE:** Discursiva

**Enunciado:**
Questão 2. Explique a diferença entre Σ, Σ*, ε e ∅.

**Resposta esperada:** _(não consta no material — resolvido aqui; base nas p. 13–14, 17–18 e 22)_
- **Σ:** alfabeto, um conjunto **finito e não vazio de símbolos** (ex.: {0,1}).
- **Σ\*:** conjunto (infinito) de **todas as palavras finitas** sobre Σ, incluindo ε (ex.: {ε, 0, 1, 00, 01, ...}). Toda linguagem L sobre Σ satisfaz L ⊆ Σ\*.
- **ε:** a **palavra** vazia, de comprimento 0 (|ε| = 0). É elemento neutro da concatenação (wε = εw = w).
- **∅:** a **linguagem** (conjunto) vazia, sem nenhuma palavra. {ε} ≠ ∅, porque {ε} tem uma palavra e ∅ não tem nenhuma.

**Conceito-chave para a prova:** ε é palavra e ∅ é linguagem; Σ contém símbolos e Σ\* contém palavras.

---

## Q15 — L² e exemplos de L* para L = {a,b}
**Fonte:** `Material de Estudos - Teoria da Computação.pdf`, p. 25 (Unidade 2, Questões de fixação, Questão 3)
**Tipo ENADE:** Discursiva

**Enunciado:**
Questão 3. Se L = {a,b}, escreva L² e dê cinco exemplos de palavras pertencentes a L*.

**Resposta esperada:** _(não consta no material — resolvido aqui; L² aparece na p. 19)_
L² = LL = {aa, ab, ba, bb}. Exemplos em L\*: ε, a, b, ab, bba (qualquer palavra finita sobre {a,b}, inclusive ε).

**Conceito-chave para a prova:** L\* = L⁰ ∪ L¹ ∪ L² ∪ ..., com L⁰ = {ε}. L\* contém **todas** as concatenações finitas, não só "L ∪ {ε}".

---

## Q16 — União, interseção e diferença de linguagens
**Fonte:** `Material de Estudos - Teoria da Computação.pdf`, p. 25 (Unidade 2, Questões de fixação, Questão 4)
**Tipo ENADE:** Discursiva

**Enunciado:**
Questão 4. Considere L₁ = {a,ab,b} e L₂ = {b,ba}. Calcule L₁ ∪ L₂, L₁ ∩ L₂ e L₁ − L₂.

**Resposta esperada:** _(não consta no material — resolvido aqui)_
- L₁ ∪ L₂ = {a, ab, b, ba}
- L₁ ∩ L₂ = {b}
- L₁ − L₂ = {a, ab}

(ab e ba são palavras **diferentes**: a ordem dos símbolos importa.)

**Conceito-chave para a prova:** Linguagens são conjuntos de palavras, e as operações de conjunto valem palavra a palavra.

---

## Q17 — Por que ε sempre pertence a L*
**Fonte:** `Material de Estudos - Teoria da Computação.pdf`, p. 25 (Unidade 2, Questões de fixação, Questão 5)
**Tipo ENADE:** Discursiva

**Enunciado:**
Questão 5. Explique por que ε sempre pertence a L*.

**Resposta esperada:** _(não consta no material — resolvido aqui; base na p. 19)_
Por definição, L\* = L⁰ ∪ L¹ ∪ L² ∪ ..., e L⁰ = {ε} (concatenar zero palavras dá a palavra vazia). Logo ε ∈ L\* para qualquer L, inclusive L = ∅ (∅\* = {ε}). Já L⁺ = L¹ ∪ L² ∪ ... só contém ε se ε ∈ L.

**Conceito-chave para a prova:** \* = zero ou mais (inclui ε); + = uma ou mais. L\* = L⁺ ∪ {ε}.

---

## Q18 — Pertinência à linguagem de (a|b)*(01|10)+
**Fonte:** `Material de Estudos - Teoria da Computação.pdf`, p. 25 (Unidade 2, Questões de fixação, Questão 6). A mesma expressão é explicada nos slides p. 21 e na apostila p. 23–24.
**Tipo ENADE:** Discursiva

**Enunciado:**
Questão 6. Para Σ={a,b,0,1}, determine se as palavras 01, a10, bb0110, aab e 1010 pertencem à linguagem descrita por (a|b)*(01|10)+.

**Resposta esperada:** _(não consta no material — resolvido aqui; conferido com `re.fullmatch` em Python)_

| Palavra | Pertence? | Decomposição / motivo |
|---|---|---|
| 01 | Sim | ε + 01 |
| a10 | Sim | a + 10 |
| bb0110 | Sim | bb + 01 + 10 |
| aab | **Não** | não termina com bloco 01 ou 10 (o + exige pelo menos um bloco) |
| 1010 | Sim | ε + 10 + 10 |

**Conceito-chave para a prova:** O 1º bloco (a|b)\* pode ser vazio; o 2º bloco (01|10)⁺ é obrigatório e só aceita pares exatos 01/10. Outros exemplos da apostila: ε, 001 e a11 são rejeitados.

---

## Q19 — Componentes da gramática G = ({S,A},{0,1},P,S)
**Fonte:** `Material de Estudos - Teoria da Computação.pdf`, p. 25 (Unidade 2, Questões de fixação, Questão 7)
**Tipo ENADE:** Discursiva

**Enunciado:**
Questão 7. Identifique V, Σ, P e S na gramática G = ({S, A}, {0, 1}, P, S), com P: S → 0A | ε e A → 1S.

**Resposta esperada:** _(não consta no material — resolvido aqui)_
- **V** (variáveis/não terminais) = {S, A}
- **Σ** (terminais) = {0, 1}
- **P** (produções) = { S → 0A, S → ε, A → 1S }
- **S** (símbolo inicial) = S

Extra: a gramática gera L(G) = {ε, 01, 0101, ...} = (01)\*. Exemplo: S ⇒ 0A ⇒ 01S ⇒ 010A ⇒ 0101S ⇒ 0101. É uma gramática regular (Tipo 3).

**Conceito-chave para a prova:** G = (V, Σ, P, S), com V ∩ Σ = ∅ e S ∈ V.

---

## Q20 — Derivação de aaabbb em S → aSb | ε
**Fonte:** `Material de Estudos - Teoria da Computação.pdf`, p. 25 (Unidade 2, Questões de fixação, Questão 8)
**Tipo ENADE:** Discursiva

**Enunciado:**
Questão 8. Mostre uma derivação da palavra aaabbb na gramática S → aSb | ε e explique a diferença entre variável e símbolo terminal.

**Resposta esperada:** _(não consta no material — resolvido aqui; modelo da derivação de aabb na p. 16)_
S ⇒ aSb ⇒ aaSbb ⇒ aaaSbbb ⇒ aaabbb (três vezes S → aSb e, por fim, S → ε).
**Variável** (não terminal, ex.: S) é símbolo auxiliar, só aparece durante a derivação e deve ser substituída. **Terminal** (a, b) é símbolo do alfabeto que forma a palavra final. Formas intermediárias como aaSbb não são palavras da linguagem. L(G) = {aⁿbⁿ | n ≥ 0}.

**Conceito-chave para a prova:** A derivação termina quando restam só terminais. S → aSb | ε gera aⁿbⁿ (LLC não regular).

---

## Q21 — Componentes da 5-upla de um autômato finito
**Fonte:** `Material de Estudos - Teoria da Computação.pdf`, p. 35 (Unidade 3, "22. Questões de fixação", Questão 1)
**Tipo ENADE:** Discursiva

**Enunciado:**
Questão 1. Explique, com suas palavras, o papel de cada componente da 5-upla M = (Q, Σ, δ, q₀, F).

**Resposta esperada:** _(não consta no material — resolvido aqui; base na p. 27)_
- **Q:** conjunto finito de estados (a "memória" do autômato).
- **Σ:** alfabeto de entrada (símbolos que podem aparecer na palavra).
- **δ:** função de transição, que diz para qual estado ir ao ler um símbolo. No AFD é δ: Q × Σ → Q.
- **q₀ ∈ Q:** estado inicial.
- **F ⊆ Q:** estados finais/de aceitação. A palavra é aceita se, **após consumir toda a entrada**, o estado atual estiver em F.

**Conceito-chave para a prova:** AF = 5-upla; AP = 7-upla (acrescenta Γ e Z₀); MT = 6-upla (Γ é o alfabeto da fita).

---

## Q22 — AFD × AFND
**Fonte:** `Material de Estudos - Teoria da Computação.pdf`, p. 35 (Unidade 3, Questões de fixação, Questão 2)
**Tipo ENADE:** Discursiva

**Enunciado:**
Questão 2. Qual é a diferença essencial entre AFD e AFND? Essa diferença altera a classe de linguagens reconhecidas?

**Resposta esperada:** _(não consta no material — resolvido aqui; base nas p. 29–31)_
No AFD há **exatamente uma** transição para cada par (estado, símbolo) e o caminho é único. No AFND pode haver **zero, uma ou várias** transições (δ: Q × Σ → P(Q), às vezes com transições ε), e a palavra é aceita se **pelo menos um** caminho consumir toda a entrada e terminar em estado final. **Não** altera a classe: ambos reconhecem exatamente as linguagens regulares. Todo AFND vira AFD pela construção dos subconjuntos, possivelmente com até 2ⁿ estados.

**Conceito-chave para a prova:** Não determinismo em AF dá compacidade, não poder. (Em autômato de pilha, ao contrário, APN é mais poderoso que APD.)

---

## Q23 — Simulação do AFD que reconhece palavras com "aa"
**Fonte:** `Material de Estudos - Teoria da Computação.pdf`, p. 35 (Unidade 3, Questões de fixação, Questão 3); o AFD está na p. 28 (5.1 Tabela de transição do exemplo)
**Tipo ENADE:** Discursiva / simulação

**Enunciado:**
Questão 3. No AFD do exemplo que reconhece palavras contendo 'aa', determine se as palavras bbb, baa, abab, aaaa e baba são aceitas.

[Dados de suporte (apostila p. 28): Q = {q₀, q₁, q₂}, Σ = {a,b}, estado inicial q₀, F = {q₂}. Diagrama: q₀ com laço em b; q₀ –a→ q₁; q₁ –b→ q₀; q₁ –a→ q₂; q₂ com laço em a, b (final, círculo duplo).]

| Estado atual | Lê a | Lê b | Observação |
|---|---|---|---|
| q₀ | q₁ | q₀ | Ainda não encontramos 'aa'. |
| q₁ | q₂ | q₀ | Já vimos um 'a'; outro 'a' completa 'aa'. |
| q₂ | q₂ | q₂ | A sequência 'aa' já ocorreu; continuamos aceitando. |

**Resposta esperada:** _(não consta no material — resolvido aqui; simulado em Python)_

| Palavra | Caminho | Resultado |
|---|---|---|
| bbb | q₀ → q₀ → q₀ → q₀ | Rejeita (q₀ ∉ F) |
| baa | q₀ → q₀ → q₁ → q₂ | **Aceita** |
| abab | q₀ → q₁ → q₀ → q₁ → q₀ | Rejeita |
| aaaa | q₀ → q₁ → q₂ → q₂ → q₂ | **Aceita** |
| baba | q₀ → q₀ → q₁ → q₀ → q₁ | Rejeita (termina em q₁) |

**Conceito-chave para a prova:** Aceita se e somente se a palavra contém "aa" como substring. Em q₁, ler b "zera" a busca (volta a q₀).

---

## Q24 — Passar por estado final não basta para aceitar
**Fonte:** `Material de Estudos - Teoria da Computação.pdf`, p. 35 (Unidade 3, Questões de fixação, Questão 4)
**Tipo ENADE:** Discursiva

**Enunciado:**
Questão 4. Explique por que uma palavra não pode ser considerada aceita apenas porque o autômato passou por um estado final durante a leitura.

**Resposta esperada:** _(não consta no material — resolvido aqui; base nas p. 26 e 32)_
O critério de aceitação de um AF é o estado em que ele **termina depois de consumir toda a entrada**. O autômato pode entrar num estado final no meio da palavra e sair dele depois. Exemplo: num AFD que aceita palavras terminadas em a, a palavra "ab" passa por estado final após o "a", mas termina em estado não final e é rejeitada. No exemplo "aa" (Q23) isso não acontece só porque q₂ tem laços em a e b, uma escolha do exemplo e não uma regra geral.

**Conceito-chave para a prova:** Aceitação em AF = entrada toda consumida **e** estado atual ∈ F. (Na MT é diferente: entrar em estado de aceitação faz parar e aceitar.)

---

## Q25 — Por que {aⁿbⁿ | n ≥ 0} não é reconhecida por AFD
**Fonte:** `Material de Estudos - Teoria da Computação.pdf`, p. 35 (Unidade 3, Questões de fixação, Questão 5). Mesmo conceito da Q3 (slides) e do slide p. 29.
**Tipo ENADE:** Discursiva

**Enunciado:**
Questão 5. Por que a linguagem {aⁿbⁿ | n ≥ 0} não pode ser reconhecida por um AFD?

**Resposta esperada:** _(não consta no material — resolvido aqui; base nas p. 33–34)_
Para aceitar só aⁿbⁿ, a máquina precisa lembrar quantos a leu (n arbitrário) e comparar com a quantidade de b. Um AFD com k estados, ao ler mais de k símbolos a, repete algum estado (princípio da casa dos pombos). Então duas quantidades diferentes de a levam ao mesmo estado, e o AFD aceitaria (ou rejeitaria) igualmente aⁱbⁱ e aʲbⁱ com i ≠ j, o que é absurdo. A formalização é o Lema do Bombeamento para linguagens regulares. A ordem (a\*b\*) é regular; o problema é **igualar as quantidades**.

**Conceito-chave para a prova:** aⁿbⁿ não é regular, mas é livre de contexto (AP / S → aSb | ε).

---

## Q26 — Informação finita × ilimitada na memória do AFD
**Fonte:** `Material de Estudos - Teoria da Computação.pdf`, p. 35 (Unidade 3, Questões de fixação, Questão 6)
**Tipo ENADE:** Discursiva

**Enunciado:**
Questão 6. Dê um exemplo de uma informação finita que um AFD consegue memorizar e de uma informação ilimitada que ele não consegue memorizar.

**Resposta esperada:** _(não consta no material — resolvido aqui; base na p. 32)_
- **Finita (consegue):** paridade da quantidade de a's (2 estados); os dois últimos símbolos lidos; se a substring "aa" já apareceu; resto da divisão do número lido por 3.
- **Ilimitada (não consegue):** a contagem exata de a's para comparar com a de b's (aⁿbⁿ, #a = #b), ou guardar uma palavra arbitrariamente longa para compará-la depois (ex.: wwᴿ).

**Conceito-chave para a prova:** Um AFD "conta" módulo uma constante (paridade etc.), mas não mantém contador ilimitado. Ver a pegadinha da Q2, item I.

---

## Q27 — Exercício resolvido: autômato de pilha para L = { aⁿb²ⁿ | n ≥ 0 }
**Fonte:** `Material de Estudos - Teoria da Computação.pdf`, p. 43–44 (Unidade 4, "5.2 Exercício resolvido")
**Tipo ENADE:** Discursiva / construção de autômato (exercício resolvido)

**Enunciado:**
Construir um autômato de pilha que reconheça as palavras formadas por n símbolos a seguidos de exatamente 2n símbolos b.

**Resposta esperada:** _(solução dada pelo próprio material, p. 43–44; conferida em Python para todas as palavras sobre {a,b} até comprimento 9)_
- **Dependência:** a quantidade de b é o dobro da quantidade de a.
- **Estratégia:** empilhar dois A para cada a lido e desempilhar um A para cada b lido. Se a entrada terminar com apenas Z₀ na pilha, a quantidade de b é exatamente 2n.
- **Estados:** q₀ (leitura dos a), q₁ (leitura dos b) e q₂ (final).

| Transição | Origem → destino | Efeito |
|---|---|---|
| a, Z₀ → AAZ₀ | q₀ → q₀ | primeiro a: empilha dois A sobre Z₀ |
| a, A → AAA | q₀ → q₀ | demais a: troca o topo A por três A, isto é, acrescenta dois A |
| b, A → ε | q₀ → q₁ | primeiro b: remove um A |
| b, A → ε | q₁ → q₁ | demais b: remove um A |
| ε, Z₀ → Z₀ | q₀ → q₂ | aceita a palavra vazia (n = 0) |
| ε, Z₀ → Z₀ | q₁ → q₂ | pilha reduzida a Z₀: aceita |

Simulação de aabbbb (aceita), topo à esquerda: (q₀, aabbbb, Z₀) → (q₀, abbbb, AAZ₀) → (q₀, bbbb, AAAAZ₀) → (q₁, bbb, AAAZ₀) → (q₁, bb, AAZ₀) → (q₁, b, AZ₀) → (q₁, ε, Z₀) → (q₂, ε, Z₀).
Rejeitadas: **aabbb** (falta um b: termina em q₁ com AZ₀ e a transição ε, Z₀ não se aplica); **abbb** (excesso de b: o 3º b encontra Z₀ no topo e não há transição).

**Conceito-chave para a prova:** Para aⁿbᵏⁿ, empilhe k símbolos por a e desempilhe 1 por b (ou 1 por a e 1 a cada k b's). Rejeição = falta de transição aplicável, sem "estado de erro".

---

## Q28 — Definição formal do autômato de pilha (papel de Γ e Z₀)
**Fonte:** `Material de Estudos - Teoria da Computação.pdf`, p. 46 (Unidade 4, "8. Questões de fixação", Questão 1)
**Tipo ENADE:** Discursiva

**Enunciado:**
Questão 1. Escreva a definição formal de um autômato de pilha e explique a função de cada componente, destacando o papel de Γ e de Z₀.

**Resposta esperada:** _(não consta no material — resolvido aqui; base na p. 36)_
M = (Q, Σ, Γ, δ, q₀, Z₀, F): Q = estados (finito); Σ = alfabeto de entrada; **Γ = alfabeto da pilha** (símbolos que podem ser empilhados, em geral diferente de Σ, ex.: A, P, Z₀); δ = função de transição, que a partir de (estado, símbolo lido ou ε, topo da pilha) dá o próximo estado e a cadeia que substitui o topo; q₀ = estado inicial; **Z₀ ∈ Γ = símbolo inicial da pilha**, marcador de fundo que permite detectar "pilha vazia" (ex.: aceitar quando o topo volta a Z₀); F = estados finais.

**Conceito-chave para a prova:** AP = 7-upla; Σ ≠ Γ (entrada ≠ pilha); Z₀ não existe na MT.

---

## Q29 — Conteúdo da pilha após sequência de push/pop
**Fonte:** `Material de Estudos - Teoria da Computação.pdf`, p. 46 (Unidade 4, Questões de fixação, Questão 2)
**Tipo ENADE:** Discursiva / simulação

**Enunciado:**
Questão 2. A pilha contém apenas Z₀. Determine o conteúdo da pilha (topo à esquerda) após a sequência de operações: push A, push B, pop, push C, push A, pop.

**Resposta esperada:** _(não consta no material — resolvido aqui; simulado)_
Z₀ → push A: AZ₀ → push B: BAZ₀ → pop: AZ₀ → push C: CAZ₀ → push A: ACAZ₀ → pop: **CAZ₀** (topo = C).

**Conceito-chave para a prova:** LIFO: o pop remove o último inserido. Convenção da apostila: topo à esquerda.

---

## Q30 — Interpretar as transições b, A → ε; a, Z₀ → AZ₀; ε, A → A
**Fonte:** `Material de Estudos - Teoria da Computação.pdf`, p. 46 (Unidade 4, Questões de fixação, Questão 3)
**Tipo ENADE:** Discursiva

**Enunciado:**
Questão 3. Interprete as transições b, A → ε, a, Z₀ → AZ₀ e ε, A → A, indicando, para cada uma, se há consumo de entrada e qual operação ocorre na pilha (push, pop ou manter).

**Resposta esperada:** _(não consta no material — resolvido aqui; base na p. 37)_

| Transição | Consome entrada? | Operação na pilha |
|---|---|---|
| b, A → ε | Sim (lê b) | **Pop**: exige A no topo e o remove |
| a, Z₀ → AZ₀ | Sim (lê a) | **Push**: com Z₀ no topo, coloca A sobre Z₀ |
| ε, A → A | **Não** (transição ε) | **Manter**: topo A continua A (só muda de estado) |

**Conceito-chave para a prova:** Notação "entrada, topo → substituição": a cadeia à direita substitui o topo. ε à direita = pop; ε na entrada = não consome símbolo.

---

## Q31 — AP da Figura 2 (aⁿbⁿ, n ≥ 1): aaabbb, aab, abb, ba e ε
**Fonte:** `Material de Estudos - Teoria da Computação.pdf`, p. 46 (Unidade 4, Questões de fixação, Questão 4); a Figura 2 está na p. 38. Também há um diagrama equivalente nos slides p. 34.
**Tipo ENADE:** Discursiva / simulação

**Enunciado:**
Questão 4. Considere o autômato da Figura 2, que utiliza a notação das figuras (λ = ε e Z = Z₀). Determine se ele aceita as palavras aaabbb, aab, abb, ba e a palavra vazia, justificando cada resposta.

[Figura 2 (p. 38) — "Autômato de pilha para aⁿbⁿ (n ≥ 1)". Notação "entrada, topo; substituição" (λ = ε, Z = Z₀). Estados q₀ (inicial), q₁, q₂, q₃ (final, círculo duplo). Transições:
- q₀ → q₁: **λ, Z; Z** (não lê símbolo e mantém Z)
- q₁ → q₁ (laço): **a, Z; AZ** (primeiro a) e **a, A; AA** (demais a)
- q₁ → q₂: **b, A; λ** (primeiro b: remove um A)
- q₂ → q₂ (laço): **b, A; λ** (demais b)
- q₂ → q₃: **λ, Z; Z** (pilha reduzida a Z: vai ao final)

Observação da apostila: "o autômato da figura reconhece aⁿbⁿ com n ≥ 1. Para incluir também a palavra vazia (n = 0) [...] basta acrescentar uma transição λ, Z; Z de q₁ para q₃."]

**Resposta esperada:** _(não consta no material — resolvido aqui; simulado em Python com busca não determinística)_
- **aaabbb — aceita.** (q₀,aaabbb,Z) → (q₁,aaabbb,Z) → (q₁,aabbb,AZ) → (q₁,abbb,AAZ) → (q₁,bbb,AAAZ) → (q₂,bb,AAZ) → (q₂,b,AZ) → (q₂,ε,Z) → (q₃,ε,Z).
- **aab — rejeita.** Termina em q₂ com AZ na pilha; com topo A não há transição λ para q₃ (sobrou um A).
- **abb — rejeita.** Após "ab" a pilha volta a Z em q₂; o segundo b encontra Z no topo e não há transição b, Z. A transição λ, Z; Z leva a q₃ com "b" ainda não lido, e q₃ não tem transições.
- **ba — rejeita.** Em q₁, com Z no topo, lendo b: não há transição (b, A; λ exige A no topo).
- **ε (palavra vazia) — rejeita.** q₀ → q₁ por λ, mas de q₁ não existe transição para q₃ sem ler símbolos. A figura reconhece só n ≥ 1.

**⚠️ Atenção:** Pegadinha: o título da seção é "reconhecimento de aⁿbⁿ" e a linguagem costuma ser definida com n ≥ 0, mas **este autômato rejeita ε** (legenda "n ≥ 1"). Para aceitar ε seria preciso λ, Z; Z de q₁ para q₃.

**Conceito-chave para a prova:** AP aceita se a entrada acabou e há um caminho até estado final. Faltar transição = rejeição. Sobra de A = excesso de a; Z no topo lendo b = excesso de b.

---

## Q32 — AP de parênteses balanceados (Figura 3): (()) e )(
**Fonte:** `Material de Estudos - Teoria da Computação.pdf`, p. 46 (Unidade 4, Questões de fixação, Questão 5); a Figura 3 e as tabelas de transição estão nas p. 39–40. Mesmo tema da Q4 (slides).
**Tipo ENADE:** Discursiva / simulação

**Enunciado:**
Questão 5. No autômato da Figura 3, simule o processamento das palavras (()) e )(, indicando o conteúdo da pilha em cada passo e o resultado.

[Figura 3 (p. 40) — "Autômato de pilha para parênteses balanceados". Notação "entrada, topo; substituição" (P = abertura pendente). Estados q₀ (inicial) e q₁ (final). Transições:
- q₀ → q₀ (laço): **(, Z; PZ** (primeira abertura: empilha P sobre Z), **(, P; PP** (nova abertura: empilha mais um P), **), P; λ** (fechamento: remove um P)
- q₀ → q₁: **λ, Z; Z** (pilha reduzida a Z: vai ao estado final q₁)]

**Resposta esperada:** _(não consta no material — resolvido aqui; simulado em Python)_

Palavra **(())** — **aceita**:

| Passo | Estado | Entrada restante | Pilha (topo à esquerda) | Transição |
|---|---|---|---|---|
| 0 | q₀ | (()) | Z | início |
| 1 | q₀ | ()) | PZ | (, Z; PZ |
| 2 | q₀ | )) | PPZ | (, P; PP |
| 3 | q₀ | ) | PZ | ), P; λ |
| 4 | q₀ | λ | Z | ), P; λ |
| 5 | q₁ | λ | Z | λ, Z; Z → aceita |

Palavra **)(** — **rejeitada**:

| Passo | Estado | Entrada restante | Pilha | Transição |
|---|---|---|---|---|
| 0 | q₀ | )( | Z | início |
| — | q₀ | )( | Z | não existe ), Z (fechamento sem abertura). A única opção é λ, Z; Z para q₁, que não tem transições e deixa ")(" sem ler → rejeita |

**Conceito-chave para a prova:** Abertura = push P; fechamento = pop P; aceita quando a entrada acaba e o topo é Z. Ler ")" com Z no topo = fechamento sem abertura; terminar com P na pilha = abertura sem fechamento (ex.: "(()" na p. 40–41).

---

## Q33 — Quais linguagens são reconhecidas por autômato de pilha
**Fonte:** `Material de Estudos - Teoria da Computação.pdf`, p. 46 (Unidade 4, Questões de fixação, Questão 6)
**Tipo ENADE:** Discursiva

**Enunciado:**
Questão 6. Indique quais das linguagens abaixo podem ser reconhecidas por um autômato de pilha e justifique.
(a) { aⁿbⁿ | n ≥ 0 }
(b) { aⁿbᵐcⁿ | n, m ≥ 0 }
(c) { aⁿbⁿcⁿ | n ≥ 0 }
(d) { aⁿbᵐ | m ≥ n ≥ 0 }

**Resposta esperada:** _(não consta no material — resolvido aqui; coerente com a tabela-resumo da p. 44)_
- **(a) Sim.** Empilha um A por a e desempilha um por b; aceita com Z₀ no topo.
- **(b) Sim.** Empilha por a, lê os b sem mexer na pilha e desempilha por c. Compara só a com c.
- **(c) Não.** Exige duas igualdades (a = b e b = c). Ao desempilhar para comparar a com b, a informação de n se perde e não há como comparar com c. Não é livre de contexto (lema do bombeamento para LLC); precisa de MT.
- **(d) Sim.** Empilha por a, desempilha por b; quando a pilha chega a Z₀, os b excedentes são lidos sem desempilhar (m ≥ n).

**Conceito-chave para a prova:** Regra prática da apostila: "AP compara dois grupos; três grupos → não dá".

---

## Q34 — Os três componentes de uma Máquina de Turing
**Fonte:** `Material de Estudos - Teoria da Computação.pdf`, p. 57 (Unidade 5, "9. Questões de fixação", Questão 1)
**Tipo ENADE:** Discursiva

**Enunciado:**
Questão 1. Quais são os três componentes de uma Máquina de Turing? Explique a função de cada um.

**Resposta esperada:** _(não consta no material — resolvido aqui; base nas p. 47–48 e slide p. 40)_
- **Controle finito:** mantém o estado atual e contém as regras de transição.
- **Fita (ilimitada):** guarda a entrada e serve de memória de leitura e escrita; células fora da entrada contêm branco (␣).
- **Cabeça de leitura e escrita:** lê e modifica o símbolo da posição atual e se move uma célula para a esquerda ou para a direita.

**Conceito-chave para a prova:** Diferente da pilha (acesso só ao topo), a fita pode ser relida e reescrita nos dois sentidos.

---

## Q35 — Definição formal da MT e diferença entre Σ e Γ
**Fonte:** `Material de Estudos - Teoria da Computação.pdf`, p. 57 (Unidade 5, Questões de fixação, Questão 2)
**Tipo ENADE:** Discursiva

**Enunciado:**
Questão 2. Escreva a definição formal M = (Q, Σ, Γ, δ, q₀, F) e explique a diferença entre Σ e Γ.

**Resposta esperada:** _(não consta no material — resolvido aqui; base na p. 48)_
Q = estados; Σ = alfabeto de entrada (não contém o branco); Γ = alfabeto da fita, com Σ ⊆ Γ e ␣ ∈ Γ \ Σ; δ: Q × Γ → Q × Γ × {L, R}; q₀ ∈ Q inicial; F ⊆ Q estados de aceitação. **Σ** são os símbolos em que a entrada pode ser escrita. **Γ** são todos os símbolos que podem aparecer na fita: os de Σ, o branco e marcas auxiliares (ex.: X, Y, Z na MT de aⁿbⁿcⁿ).

**Conceito-chave para a prova:** Σ ⊂ Γ; branco ∈ Γ e ∉ Σ; MT não tem Z₀.

---

## Q36 — Rejeitar × entrar em loop
**Fonte:** `Material de Estudos - Teoria da Computação.pdf`, p. 57 (Unidade 5, Questões de fixação, Questão 3)
**Tipo ENADE:** Discursiva

**Enunciado:**
Questão 3. Explique a diferença entre rejeitar e entrar em loop. Dê um exemplo de máquina que entra em loop.

**Resposta esperada:** _(não consta no material — resolvido aqui; base na p. 52)_
**Rejeitar** é **parar sem aceitar**, por atingir um estado de rejeição ou por não haver transição definida. **Loop** é **nunca parar**: a máquina executa transições indefinidamente e não dá resposta. Exemplo de loop (apostila p. 52): δ(q, a) = (q, a, R) e δ(q, ␣) = (q, ␣, R). A máquina anda para a direita para sempre, qualquer que seja a entrada.

**⚠️ Atenção:** A apostila (p. 52) observa que definir rejeição só como "não terminar em um estado de aceitação" é ambíguo, porque também descreveria o loop. O slide p. 42 diz "Finaliza o processamento sem terminar em um estado de aceitação", e o "finaliza" é o que separa rejeição de loop. Rejeitar exige parar.

**Conceito-chave para a prova:** Falta de transição ⇒ para e rejeita (não é loop). Ver a afirmativa II da Q5.

---

## Q37 — Reconhecer × decidir uma linguagem
**Fonte:** `Material de Estudos - Teoria da Computação.pdf`, p. 57 (Unidade 5, Questões de fixação, Questão 4)
**Tipo ENADE:** Discursiva

**Enunciado:**
Questão 4. Explique a diferença entre reconhecer e decidir uma linguagem.

**Resposta esperada:** _(não consta no material — resolvido aqui; base na p. 53)_
**Reconhecer:** a MT aceita exatamente as palavras da linguagem; nas outras pode rejeitar **ou entrar em loop**. Essa é a classe RE (recursivamente enumeráveis / Turing-reconhecíveis). **Decidir:** a MT aceita toda palavra da linguagem, rejeita toda palavra fora dela e **sempre para**. Essa é a classe das recursivas/decidíveis. Toda linguagem decidível é reconhecível, mas não vale a recíproca: HALT é reconhecível e não decidível.

**Conceito-chave para a prova:** Decidível ⊂ Reconhecível (RE). A diferença está na garantia de parada.

---

## Q38 — Simular aabbcc na MT da Seção 2.3 (aⁿbⁿcⁿ)
**Fonte:** `Material de Estudos - Teoria da Computação.pdf`, p. 58 (Unidade 5, Questões de fixação, Questão 5); a MT está na p. 50 (tabela) e na p. 51 (Figura 2). Mesma MT da Q5 (slides), com diferenças de notação.
**Tipo ENADE:** Discursiva / simulação

**Enunciado:**
Questão 5. Usando a MT da Seção 2.3, simule a palavra aabbcc e indique se ela é aceita.

[Dados de suporte — MT da Seção 2.3 (p. 50–51): estados q₀ a q₄ e qacc (aceitação), Σ = {a, b, c}, Γ = Σ ∪ {X, Y, Z, ␣}. "Qualquer situação não listada leva à rejeição."]

| Estado | Transições | Papel |
|---|---|---|
| q₀ | a → X, R (q₁); Y → Y, R (q₄); ␣ → ␣, R (qacc) | início de rodada: marca um a; se não há mais a's, vai conferir o resto; fita vazia é aceita (n = 0) |
| q₁ | a → a, R (q₁); Y → Y, R (q₁); b → Y, R (q₂) | procura o primeiro b não marcado e o marca |
| q₂ | b → b, R (q₂); Z → Z, R (q₂); c → Z, L (q₃) | procura o primeiro c não marcado e o marca |
| q₃ | a, b, Y, Z → mesmo símbolo, L (q₃); X → X, R (q₀) | volta à esquerda até o último X e reinicia |
| q₄ | Y → Y, R (q₄); Z → Z, R (q₄); ␣ → ␣, R (qacc) | confere que só restam Y's e Z's |

[Figura 2 (p. 51) — "Diagrama de estados da MT que decide aⁿbⁿcⁿ (n ≥ 0)": mesmos arcos da tabela. q₀→q₁ (a → X, R); laço em q₁ (a → a, R; Y → Y, R); q₁→q₂ (b → Y, R); laço em q₂ (b → b, R; Z → Z, R); q₂→q₃ (c → Z, L); laço em q₃ (a, b, Y, Z → mesmo, L); q₃→q₀ (X → X, R); q₀→q₄ (Y → Y, R); q₀→qacc (␣ → ␣, R); laço em q₄ (Y → Y, R; Z → Z, R); q₄→qacc (␣ → ␣, R).]

**Resposta esperada:** _(não consta no material — resolvido aqui; simulado em Python)_ **Aceita**, em 23 passos:

| Passo | Estado | Fita | Passo | Estado | Fita |
|---|---|---|---|---|---|
| 0 | q₀ | [a]abbcc | 12 | q₂ | XXYY[Z]c |
| 1 | q₁ | X[a]bbcc | 13 | q₂ | XXYYZ[c] |
| 2 | q₁ | Xa[b]bcc | 14 | q₃ | XXYY[Z]Z |
| 3 | q₂ | XaY[b]cc | 15 | q₃ | XXY[Y]ZZ |
| 4 | q₂ | XaYb[c]c | 16 | q₃ | XX[Y]YZZ |
| 5 | q₃ | XaY[b]Zc | 17 | q₃ | X[X]YYZZ |
| 6 | q₃ | Xa[Y]bZc | 18 | q₀ | XX[Y]YZZ |
| 7 | q₃ | X[a]YbZc | 19 | q₄ | XXY[Y]ZZ |
| 8 | q₃ | [X]aYbZc | 20 | q₄ | XXYY[Z]Z |
| 9 | q₀ | X[a]YbZc | 21 | q₄ | XXYYZ[Z] |
| 10 | q₁ | XX[Y]bZc | 22 | q₄ | XXYYZZ[␣] |
| 11 | q₁ | XXY[b]Zc | 23 | qacc | XXYYZZ␣[␣] → aceita |

**Diferenças entre versões:** Ver a Q5. A MT do slide usa D/E, B e qf, não tem a transição q₀: ␣ → qacc e por isso reconhece n ≥ 1. A da apostila reconhece n ≥ 0. Para aabbcc o comportamento é idêntico.

**Conceito-chave para a prova:** Fim do 1º ciclo: fita XaYbZc com cabeça no 2º a em q₀. Fim: XXYYZZ, q₀ lê Y → q₄ → branco → aceita.

---

## Q39 — Simular abcc na mesma MT (rejeição)
**Fonte:** `Material de Estudos - Teoria da Computação.pdf`, p. 58 (Unidade 5, Questões de fixação, Questão 6); MT da p. 50–51 (transcrita na Q38)
**Tipo ENADE:** Discursiva / simulação

**Enunciado:**
Questão 6. Usando a mesma MT, simule abcc e explique por que ela é rejeitada.

**Resposta esperada:** _(não consta no material — resolvido aqui; simulado em Python)_

| Passo | Estado | Fita | Transição |
|---|---|---|---|
| 0 | q₀ | [a]bcc | início |
| 1 | q₁ | X[b]cc | a → X, R |
| 2 | q₂ | XY[c]c | b → Y, R |
| 3 | q₃ | X[Y]Zc | c → Z, L |
| 4 | q₃ | [X]YZc | Y → Y, L |
| 5 | q₀ | X[Y]Zc | X → X, R |
| 6 | q₄ | XY[Z]c | Y → Y, R |
| 7 | q₄ | XYZ[c] | Z → Z, R |

Em q₄ lendo c **não há transição**: a máquina para sem aceitar e **rejeita**. Sobrou um c sem par: há 1 a, 1 b e 2 c.

**Conceito-chave para a prova:** q₄ só aceita Y, Z e ␣. Qualquer a, b ou c restante após acabar os a's provoca rejeição.

---

## Q40 — Construir MT que inverte bits (0↔1)
**Fonte:** `Material de Estudos - Teoria da Computação.pdf`, p. 58 (Unidade 5, Questões de fixação, Questão 7)
**Tipo ENADE:** Discursiva / construção

**Enunciado:**
Questão 7. Construa uma MT que troque cada 0 por 1 e cada 1 por 0 em uma cadeia de {0,1}* e pare ao encontrar o branco.

**Resposta esperada:** _(não consta no material — resolvido aqui)_
M = ({q₀, q_f}, {0,1}, {0,1,␣}, δ, q₀, {q_f}), com:
- δ(q₀, 0) = (q₀, 1, R)
- δ(q₀, 1) = (q₀, 0, R)
- δ(q₀, ␣) = (q_f, ␣, R) _(ou L; o que importa é parar)_

Exemplo: 0110 → (q₀,[0]110) → (q₀,1[1]10) → (q₀,10[1]0) → (q₀,100[0]) → (q₀,1001[␣]) → (q_f, 1001␣) → para com 1001 na fita. Sempre para, porque percorre a entrada uma vez.

**Conceito-chave para a prova:** Notação "lido → escrito, movimento"; uma MT também calcula funções (transdutora), não só aceita linguagens.

---

## Q41 — Problema da parada: reconhecível, mas não decidível
**Fonte:** `Material de Estudos - Teoria da Computação.pdf`, p. 58 (Unidade 5, Questões de fixação, Questão 8)
**Tipo ENADE:** Discursiva

**Enunciado:**
Questão 8. Explique por que o problema da parada é reconhecível, mas não decidível.

**Resposta esperada:** _(não consta no material — resolvido aqui; base nas p. 55–56)_
HALT = { ⟨M, w⟩ | M é uma MT que para com a entrada w }.
- **Reconhecível:** uma MT (universal) simula M sobre w e aceita se a simulação parar. Se M para, a resposta "sim" sempre chega.
- **Não decidível:** se M entra em loop, a simulação também não termina e não há resposta "não" garantida. Prova por contradição (diagonalização): suponha uma MT H que decide HALT. Construa D que, com entrada ⟨M⟩, executa H sobre ⟨M, ⟨M⟩⟩ e faz o oposto (entra em loop se H diz "para"; para se H diz "não para"). Executando D sobre ⟨D⟩: se D para, H diz que para e D entra em loop; se D não para, H diz que não para e D para. Contradição nos dois casos, logo H não existe.

**Conceito-chave para a prova:** HALT ∈ RE \ Recursivas. Por redução, outros problemas (equivalência de programas, Teorema de Rice) também são indecidíveis.

---

## Q42 — Erro na afirmação "é impossível verificar se qualquer programa termina"
**Fonte:** `Material de Estudos - Teoria da Computação.pdf`, p. 58 (Unidade 5, Questões de fixação, Questão 9)
**Tipo ENADE:** Discursiva / interpretação

**Enunciado:**
Questão 9. Um colega afirma: "Como o problema da parada é indecidível, é impossível verificar se qualquer programa termina." Aponte o erro.

**Resposta esperada:** _(não consta no material — resolvido aqui; base na observação da p. 55)_
A indecidibilidade diz que **não existe um único algoritmo geral** que acerte para **todos** os pares (programa, entrada). Ela não diz que é impossível analisar **um programa específico**: muitos são analisáveis (ex.: um programa sem laços, ou um laço `for` com limite fixo, claramente termina). Além disso, HALT é reconhecível: se o programa para, a simulação confirma. Na prática, ferramentas usam aproximações ou se restringem a classes de programas.

**Conceito-chave para a prova:** "Indecidível" = não há algoritmo geral, não "nenhum caso pode ser decidido". Lista de erros da apostila: "não dá pra prever todos os programas, mas alguns sim".
