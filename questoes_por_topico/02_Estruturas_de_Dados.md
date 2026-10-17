# Estruturas de Dados — Questões e Gabarito Comentado

**Squad responsável:** Squad 9 (Bruno da Silva · Cauã Barchi Finotti Franzol · Gustavo Grassini Calabrez · Pedro Henrique Papa Amorim dos Santos) — Prof. Fabricio Ricardo Perrella

**Materiais analisados:**
| Arquivo | Páginas | Tipo | Questões encontradas (páginas) |
|---|---|---|---|
| `Questoes_ENADE_Estruturas_de_Dados.pdf` | 8 | Arquivo oficial de questões (enunciado + gabarito + justificativas) | Q1–Q6 (p. 2–7); quadro-resumo com gabarito na p. 8 |
| `Apresentacao_Questoes_ENADE (1).pdf` | 22 | Slides ("Seis questões de múltipla escolha — da matéria ao gabarito") | Q1–Q6, as mesmas do arquivo de questões. Enunciados nas p. 5, 8, 11, 14, 17 e 20; gabaritos nas p. 6, 9, 12, 15, 18 e 21; slides de conceito nas p. 4, 7, 10, 13, 16 e 19 |
| `Material_Estruturas_de_Dados.pdf` | 18 | Material explicativo (apostila com teoria, código em C e tabelas de complexidade) | Nenhuma questão nem exercício (as 18 páginas foram lidas e renderizadas) |

**Resumo:** 6 questões encontradas. As 6 têm gabarito no próprio material (Q1 A · Q2 C · Q3 B · Q4 D · Q5 B · Q6 D), e conferi as 6 de forma independente: todas estão corretas. 0 questões sem gabarito. A apresentação reproduz as 6 questões do arquivo oficial com o **mesmo texto, as mesmas alternativas, na mesma ordem e com o mesmo gabarito**. As diferenças são só de formatação ou de pequenas palavras do comando (detalhes em cada questão). Os slides acrescentam um quadro "As armadilhas dos distratores" em cada gabarito. O material explicativo não traz questões, mas cobre a teoria de todas elas (seções 3, 4, 6, 7, 8 e 9).

> Legenda: ✅ correta · ❌ incorreta · ⚠️ ponto de atenção (gabarito do material duvidoso, ambiguidade, versão divergente)

**Gabarito rápido:**
| Q | Tema | Tipo | Gabarito |
|---|---|---|---|
| 1 | Listas encadeadas | Asserção-razão | **A** |
| 2 | Pilhas (Desfazer/Refazer) | Ordenação | **C** (2 – 4 – 3 – 1) |
| 3 | Árvores BST / AVL / rubro-negra | Afirmativas múltiplas | **B** (I, II e IV) |
| 4 | Tabela hash e colisões | Afirmativa negativa (INCORRETA) | **D** |
| 5 | Grafos: matriz × lista de adjacência | Associação | **B** (2 – 3 – 1) |
| 6 | Busca em grafos BFS × DFS | Asserção-razão | **D** |

## Índice
1. [Q1 — Listas encadeadas](#q1--listas-encadeadas)
2. [Q2 — Pilhas e filas](#q2--pilhas-e-filas)
3. [Q3 — Árvores de busca e balanceadas](#q3--árvores-de-busca-e-balanceadas)
4. [Q4 — Tabela hash e colisões](#q4--tabela-hash-e-colisões)
5. [Q5 — Grafos matriz e lista de adjacência](#q5--grafos-matriz-e-lista-de-adjacência)
6. [Q6 — Busca em grafos BFS e DFS](#q6--busca-em-grafos-bfs-e-dfs)

---

## Q1 — Listas encadeadas
**Fonte:** `Questoes_ENADE_Estruturas_de_Dados.pdf`, p. 2 (também em `Apresentacao_Questoes_ENADE (1).pdf`, p. 5 (enunciado) e p. 6 (gabarito), com slide de conceito na p. 4; teoria em `Material_Estruturas_de_Dados.pdf`, p. 6–7)
**Tipo ENADE:** Asserção-razão (CAT 3) · Nível cognitivo: Síntese / Aplicação

**Enunciado:**

SITUAÇÃO-PROBLEMA
Uma equipe está implementando o mecanismo de uma playlist dinâmica na qual o usuário pode remover, a qualquer momento, a faixa atualmente selecionada. A aplicação mantém sempre um ponteiro direto para o nó correspondente à faixa selecionada. A equipe precisa decidir entre implementar a playlist com uma lista simplesmente encadeada ou com uma lista duplamente encadeada, priorizando o menor custo para a operação de remoção dessa faixa.

DADOS DE SUPORTE
```c
// Nó de lista simplesmente encadeada
typedef struct No {
    int        dado;
    struct No *prox;        // referência ao próximo nó
} No;

// Nó de lista duplamente encadeada
typedef struct NoD {
    int         dado;
    struct NoD *ant, *prox; // referências ao anterior e ao próximo
} NoD;
```

COMANDO
Considerando os custos das operações em listas encadeadas, avalie as asserções a seguir e a relação proposta entre elas.

I. Para remover em tempo O(1) a faixa selecionada, da qual já se dispõe do ponteiro para o nó, a lista duplamente encadeada é mais adequada que a simplesmente encadeada.

PORQUE

II. Na lista duplamente encadeada cada nó mantém referências para o nó anterior e para o próximo, permitindo reconectar os vizinhos do nó removido sem percorrer a lista em busca do antecessor.

**Alternativas:**
- **A)** As asserções I e II são verdadeiras, e a II é uma justificativa correta da I.
- **B)** As asserções I e II são verdadeiras, mas a II não é uma justificativa correta da I.
- **C)** A asserção I é verdadeira, e a II é falsa.
- **D)** A asserção I é falsa, e a II é verdadeira.
- **E)** As asserções I e II são falsas.

**Gabarito: A** — _(origem: gabarito do próprio material, `Questoes...pdf` p. 2 e quadro-resumo p. 8; slides p. 6: "Resposta: A — I e II verdadeiras, e a II justifica a I.")_

**Julgamento das asserções:**
- **I — Verdadeira.** Já se tem o ponteiro para o nó. Na lista dupla a remoção só reajusta `p->ant->prox = p->prox` e `p->prox->ant = p->ant`, o que é O(1). Na lista simples é preciso achar o antecessor percorrendo a lista desde a cabeça, o que é O(n).
- **II — Verdadeira.** Descreve corretamente o nó `NoD`, com os ponteiros `ant` e `prox`.
- **Relação — II justifica I.** É justamente o ponteiro `ant` que dispensa a busca do antecessor e torna a remoção O(1).

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — As duas asserções são verdadeiras, e a II é a causa do desempenho afirmado na I, porque a referência ao anterior permite religar os vizinhos sem percorrer a lista.
- **B) ❌** — Reconhece que as duas são verdadeiras, mas nega o nexo causal. A estrutura descrita na II é exatamente a razão da remoção em O(1) da I.
- **C) ❌** — A II não é falsa: ela descreve corretamente a lista duplamente encadeada.
- **D) ❌** — A I não é falsa: a lista dupla realmente remove um nó conhecido em O(1). A alternativa pega quem supõe que remover em lista é sempre O(n), qualquer que seja a estrutura.
- **E) ❌** — As duas são verdadeiras. Marcar E ignora tanto o custo O(1) quanto a estrutura de dois ponteiros.

**Diferenças entre versões:** O texto do enunciado, o código, as asserções, as alternativas e o gabarito são idênticos nos dois arquivos. Mudam só os rótulos: o arquivo de questões escreve "Asserção-Razão (CAT 3) · Nível cognitivo: Síntese / Aplicação", e o slide escreve "Asserção-Razão · Síntese/Aplicação", sem o CAT. O slide 6 acrescenta o quadro "As armadilhas dos distratores" (B nega o nexo causal; C diz que II é falsa; D diz que I é falsa; E diz que ambas são falsas), com o mesmo conteúdo das justificativas.

**⚠️ Atenção:** Há uma sutileza que não muda o gabarito. Numa lista **simples**, existe o truque de "copiar o próximo": copia-se o dado de `p->prox` para `p` e remove-se o próximo, o que também é O(1). O truque não funciona para o último nó e invalida ponteiros externos para o nó seguinte, por isso não é uma remoção genérica. No padrão ENADE e no material, a resposta esperada continua sendo **A**.

**Conceito-chave para a prova:** Remover um nó **já conhecido** custa O(1) na lista **duplamente** encadeada (tem `ant`) e O(n) na **simplesmente** encadeada (precisa achar o antecessor). Variações possíveis: se a I disser "lista simples é mais adequada" ou "a remoção custa O(n) na lista dupla", a I fica falsa e a II continua verdadeira, e o gabarito vira **D**. Se a II for trocada por um fato verdadeiro sem relação com a I (ex.: "a lista circular liga o último nó ao primeiro"), o gabarito vira **B**.

---

## Q2 — Pilhas e filas
**Fonte:** `Questoes_ENADE_Estruturas_de_Dados.pdf`, p. 3 (também em `Apresentacao_Questoes_ENADE (1).pdf`, p. 8 (enunciado) e p. 9 (gabarito), com slide de conceito na p. 7; teoria em `Material_Estruturas_de_Dados.pdf`, p. 8–9)
**Tipo ENADE:** Ordenação (CAT 3) · Nível cognitivo: Avaliação / Análise

**Enunciado:**

SITUAÇÃO-PROBLEMA
Um editor de texto implementa as funções Desfazer (Undo) e Refazer (Redo) utilizando duas pilhas: a pilha de Desfazer, que armazena as ações já executadas, e a pilha de Refazer. Ao acionar o Desfazer, o sistema precisa reverter a última ação executada e prepará-la para um eventual Refazer.

COMANDO
Considerando o comportamento LIFO das pilhas e o uso das duas estruturas, ordene as etapas que o sistema deve executar, na sequência correta, ao acionar a função Desfazer:

1. Empilhar (push) na pilha de Refazer a ação que foi retirada.
2. Verificar se a pilha de Desfazer não está vazia; se estiver, encerrar (não há o que desfazer).
3. Aplicar ao documento a operação inversa da ação retirada.
4. Retirar (pop) a ação do topo da pilha de Desfazer.

**Alternativas:**
- **A)** 4 – 2 – 3 – 1
- **B)** 2 – 4 – 1 – 3
- **C)** 2 – 4 – 3 – 1
- **D)** 4 – 3 – 1 – 2

**Gabarito: C** — _(origem: gabarito do próprio material, `Questoes...pdf` p. 3 e quadro-resumo p. 8; slides p. 9: "Resposta: C — 2 – 4 – 3 – 1")_

**Raciocínio:** Primeiro checa-se se há o que desfazer (2), para evitar *underflow*. Depois retira-se a ação do topo da pilha de Desfazer com `pop` (4). Em seguida aplica-se a operação inversa ao documento, o que efetiva o desfazer (3). Por último empilha-se a ação na pilha de Refazer com `push` (1), para permitir o Refazer. Resultado: **2 – 4 – 3 – 1**.

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Faz o `pop` (4) antes de verificar se a pilha de Desfazer está vazia (2), arriscando *underflow* (remoção em pilha vazia).
- **B) ❌** — Empilha a ação na pilha de Refazer (1) antes de aplicar a operação inversa (3). A ação ficaria disponível para refazer sem ter sido efetivamente desfeita.
- **C) ✅** — Verifica (2) → `pop` (4) → aplica o inverso (3) → `push` no Refazer (1). É a ordem segura e lógica.
- **D) ❌** — Deixa a verificação de pilha vazia (2) por último, quando já desempilhou e alterou o documento. Inverte a ordem de segurança da operação.

**Diferenças entre versões:** Texto, etapas 1–4, alternativas e gabarito idênticos nos dois arquivos. O rótulo do slide é "Ordenação · Avaliação/Análise" (sem "CAT 3"). O slide 9 acrescenta "As armadilhas dos distratores": A) 4-2-3-1 faz o pop antes de checar a pilha vazia, com risco de underflow; B) 2-4-1-3 empilha no Refazer antes de aplicar o inverso, deixando uma ação "refazível" que não foi desfeita; D) 4-3-1-2 deixa a checagem de pilha vazia por último, depois de já alterar o documento.

**⚠️ Atenção:** B e C diferem **só** na ordem entre as etapas 3 e 1. A rejeição da B é mais um argumento de boa prática do que de correção: se aplicar o inverso falhar, a pilha de Refazer ficaria com uma ação que não foi desfeita. Numa execução sem falhas, B também chegaria ao mesmo estado final. O gabarito do material (**C**) é a resposta esperada. Na prova, o ponto decisivo é: **verificar antes do pop** e **empilhar no Refazer por último**.

**Conceito-chave para a prova:** Pilha é LIFO, com `push` e `pop` só no topo, ambos O(1). Antes de todo `pop`, verifique se a pilha está vazia (evita *underflow*). No Desfazer, a ação sai da pilha Desfazer, é revertida e vai para a pilha Refazer. No Refazer o caminho é espelhado: verifica Refazer → `pop` do Refazer → reaplica a ação → `push` no Desfazer.

---

## Q3 — Árvores de busca e balanceadas
**Fonte:** `Questoes_ENADE_Estruturas_de_Dados.pdf`, p. 4 (também em `Apresentacao_Questoes_ENADE (1).pdf`, p. 11 (enunciado) e p. 12 (gabarito), com slide de conceito na p. 10; teoria em `Material_Estruturas_de_Dados.pdf`, p. 11–12)
**Tipo ENADE:** Afirmativas múltiplas (CAT 2) · Nível cognitivo: Avaliação / Análise

**Enunciado:**

SITUAÇÃO-PROBLEMA
Uma equipe precisa escolher a estrutura para indexar registros que sofrem muitas inserções e remoções, exigindo busca eficiente e com desempenho previsível no pior caso. Foram consideradas a árvore binária de busca (BST) comum e as árvores balanceadas AVL e rubro-negra.

COMANDO
Considerando as propriedades das árvores de busca, analise as afirmativas a seguir:

I. Em uma BST comum, a inserção de chaves em ordem crescente pode degenerar a árvore, elevando o custo da busca a O(n).

II. A árvore AVL mantém, para todo nó, a diferença de altura entre as subárvores esquerda e direita limitada a, no máximo, 1 em módulo, recorrendo a rotações após inserções e remoções.

III. A árvore rubro-negra garante busca em O(1) no pior caso, pois a coloração dos nós elimina a necessidade de percorrer a altura da árvore.

IV. Tanto a AVL quanto a rubro-negra asseguram busca, inserção e remoção em O(log n) no pior caso, diferindo no rigor do balanceamento e, portanto, na frequência de rotações.

É correto apenas o que se afirma em:

**Julgamento das afirmativas:**
- **I — Verdadeira.** Inserir 1, 2, 3, 4, 5 em ordem numa BST cria uma "escada" (cada nó só tem filho à direita). A altura vira n e a busca, O(h) = O(n).
- **II — Verdadeira.** É a definição do fator de balanceamento da AVL: |altura(esq) − altura(dir)| ≤ 1 em todo nó, ou seja, fator −1, 0 ou +1. Ele é restaurado com rotações simples ou duplas após inserções e remoções.
- **III — Falsa.** A rubro-negra garante **O(log n)**, não O(1). As regras de cor limitam a altura a cerca de 2·log n (formalmente h ≤ 2·log₂(n+1)), mas a busca ainda desce pela altura da árvore. Nenhuma árvore de busca por comparação faz busca em O(1).
- **IV — Verdadeira.** As duas garantem O(log n) no pior caso para busca, inserção e remoção. A AVL é balanceada com mais rigor (altura ≈ 1,44·log n), o que dá buscas um pouco mais rápidas e mais rotações nas atualizações. A rubro-negra é mais "frouxa" (altura ≤ 2·log n) e faz menos rotações (no máximo 2 na inserção e 3 na remoção).

**Alternativas:**
- **A)** I e II.
- **B)** I, II e IV.
- **C)** III e IV.
- **D)** II e III.

**Gabarito: B** — _(origem: gabarito do próprio material, `Questoes...pdf` p. 4 e quadro-resumo p. 8; slides p. 12: "Resposta: B — apenas I, II e IV estão corretas.")_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Deixa de fora a afirmativa IV, que é verdadeira.
- **B) ✅** — Reúne exatamente as três verdadeiras: I (a BST degenera com inserção em ordem crescente, levando a busca a O(n)), II (definição do fator de balanceamento da AVL, mantido por rotações) e IV (AVL e rubro-negra garantem O(log n) no pior caso e diferem no rigor do balanceamento).
- **C) ❌** — Inclui a III, que é falsa, e exclui I e II, que são verdadeiras.
- **D) ❌** — Inclui a III, que é falsa, e exclui I e IV, que são verdadeiras.

**Diferenças entre versões:** Situação-problema, afirmativas I–IV, alternativas e gabarito idênticos. Diferenças: o rótulo do slide é "Afirmativas Múltiplas · Avaliação/Análise" (sem "CAT 2"), e o cabeçalho da justificativa é "JUSTIFICATIVA:" no slide e "JUSTIFICATIVAS" no arquivo. O quadro "armadilhas" do slide 12 diz que a coloração "limita a altura a 2·log n". O texto principal, nos dois arquivos, diz "a cerca de 2·log n", que é a forma mais precisa.

**Conceito-chave para a prova:** BST custa O(h). Balanceada, O(log n); degenerada (dados em ordem), O(n). AVL e rubro-negra garantem **O(log n) no pior caso**, **nunca O(1)**. A AVL é mais rígida (|fator| ≤ 1, mais rotações). A rubro-negra é mais frouxa (altura ≤ ~2·log n, menos rotações). Se a prova trocar a III por algo verdadeiro, ou a IV por algo falso, refaça a contagem das afirmativas.

---

## Q4 — Tabela hash e colisões
**Fonte:** `Questoes_ENADE_Estruturas_de_Dados.pdf`, p. 5 (também em `Apresentacao_Questoes_ENADE (1).pdf`, p. 14 (enunciado) e p. 15 (gabarito), com slide de conceito na p. 13; teoria em `Material_Estruturas_de_Dados.pdf`, p. 12–13)
**Tipo ENADE:** Afirmativa negativa — "INCORRETA" (CAT 1) · Nível cognitivo: Compreensão / Conhecimento

**Enunciado:**

SITUAÇÃO-PROBLEMA
Um desenvolvedor implementa uma tabela hash para armazenar pares chave-valor em uma aplicação com alto volume de consultas. Ele analisa o papel da função hash, do fator de carga e das técnicas de tratamento de colisões.

COMANDO
Sobre tabelas hash e o tratamento de colisões, assinale a alternativa **INCORRETA**:

**Alternativas:**
- **A)** No tratamento por encadeamento separado, cada posição da tabela referencia uma lista que reúne todas as chaves que colidiram naquele índice.
- **B)** O fator de carga é a razão entre o número de elementos armazenados e o número de posições da tabela, e o seu aumento tende a elevar o número de colisões.
- **C)** Uma função hash bem projetada distribui as chaves de maneira uniforme pelas posições, reduzindo a probabilidade de colisões.
- **D)** Com uma função hash adequada, a busca em uma tabela hash tem custo O(log n) no caso médio, pois as chaves são mantidas internamente ordenadas para permitir busca binária.

**Gabarito: D** — _(origem: gabarito do próprio material, `Questoes...pdf` p. 5 e quadro-resumo p. 8; slides p. 15: "Resposta: D — é a afirmação INCORRETA (o que se pede).")_

**Por que cada alternativa está certa ou errada** (lembre que se pede a **INCORRETA**):
- **A) ❌ (não é a resposta: afirmação verdadeira)** — Descreve com precisão o encadeamento separado: cada balde guarda uma lista ligada com as chaves que colidiram ali.
- **B) ❌ (não é a resposta: afirmação verdadeira)** — Define corretamente o fator de carga, α = nº de elementos ÷ nº de posições. Quanto maior o α, mais colisões, e por isso se faz *rehash* quando ele cresce demais.
- **C) ❌ (não é a resposta: afirmação verdadeira)** — A distribuição uniforme é a principal qualidade de uma boa função hash.
- **D) ✅ (é a resposta: afirmação falsa)** — Tem dois erros. (1) A busca em tabela hash custa **O(1) no caso médio**, não O(log n). O pior caso é O(n), quando muitas chaves caem no mesmo balde. (2) A tabela hash **não mantém as chaves ordenadas** nem faz busca binária: ela calcula o índice direto pela função hash. Ordem e O(log n) são características de estruturas ordenadas (árvores balanceadas, vetor ordenado com busca binária). A alternativa confunde a hash com uma estrutura ordenada.

**Diferenças entre versões:** Situação-problema, comando, alternativas A–D e gabarito idênticos. Diferenças: o slide não tem o cabeçalho "ALTERNATIVAS" (as alternativas vêm logo após o comando), e o rótulo do slide é "Afirmativa Negativa · Compreensão/Conhecimento" (sem "CAT 1"). O slide 15 acrescenta "Armadilhas": A, B e C são afirmações verdadeiras (encadeamento, fator de carga e uniformidade da função hash) e por isso não são a resposta.

**Conceito-chave para a prova:** Na hash, inserção, busca e remoção custam **O(1) no caso médio** e **O(n) no pior caso**. **Não há ordem**: quem precisa de ordenação usa árvore balanceada. Os dois tratamentos de colisão são o encadeamento separado (lista no balde, tolera α > 1) e o endereçamento aberto (sondagem linear, quadrática ou hash duplo, exige α baixo). Fator de carga α = n/m. Atenção ao comando "INCORRETA": a resposta é a afirmação **falsa**.

---

## Q5 — Grafos matriz e lista de adjacência
**Fonte:** `Questoes_ENADE_Estruturas_de_Dados.pdf`, p. 6 (também em `Apresentacao_Questoes_ENADE (1).pdf`, p. 17 (enunciado) e p. 18 (gabarito), com slide de conceito na p. 16; teoria em `Material_Estruturas_de_Dados.pdf`, p. 14–15)
**Tipo ENADE:** Associação (CAT 2) · Nível cognitivo: Compreensão / Conhecimento

**Enunciado:**

SITUAÇÃO-PROBLEMA
Ao modelar diferentes sistemas como grafos, um analista precisa escolher a representação mais adequada — matriz de adjacência ou lista de adjacência — conforme a densidade do grafo e as operações mais frequentes.

COMANDO
Relacione cada necessidade da Coluna 1 à representação de grafos mais adequada, descrita na Coluna 2.

**Coluna 1 — Necessidade**
1. Consultar em tempo O(1) se existe a aresta entre dois vértices dados.
2. Minimizar o uso de memória em um grafo esparso (poucas arestas).
3. Iterar eficientemente sobre os vizinhos de um vértice.

**Coluna 2 — Representação adequada (e razão)**
- ( ) Lista de adjacência — o espaço cresce com O(V + E), evitando desperdício.
- ( ) Lista de adjacência — percorre-se apenas a lista do próprio vértice, em O(grau(v)).
- ( ) Matriz de adjacência — o acesso direto à célula [u][v] responde em O(1).

Assinale a alternativa com a associação correta, de cima para baixo:

**Alternativas:**
- **A)** 1 – 2 – 3
- **B)** 2 – 3 – 1
- **C)** 3 – 2 – 1
- **D)** 1 – 3 – 2

**Gabarito: B** — _(origem: gabarito do próprio material, `Questoes...pdf` p. 6 e quadro-resumo p. 8; slides p. 18: "Resposta: B — 2 – 3 – 1")_

**Raciocínio (preenchendo a Coluna 2 de cima para baixo):**
- ( **2** ) Lista de adjacência, espaço O(V + E): é a que economiza memória em grafo esparso. A matriz gasta O(V²) mesmo com poucas arestas.
- ( **3** ) Lista de adjacência, percorre só a lista do vértice em O(grau(v)): é a melhor para iterar sobre vizinhos. Na matriz isso custa O(V), porque se varre a linha inteira.
- ( **1** ) Matriz de adjacência, acesso direto a [u][v] em O(1): só a matriz responde em O(1) se a aresta existe. Na lista isso custa O(grau).

Sequência **2 – 3 – 1**.

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — 1 – 2 – 3 erra as três posições. Coloca a consulta de aresta em O(1) (necessidade da matriz) na lista de economia de memória, o que é falso porque a matriz consome O(V²). Também troca as demais.
- **B) ✅** — 2 – 3 – 1, conforme a análise acima.
- **C) ❌** — 3 – 2 – 1 troca entre si as duas vantagens da lista: põe "iterar vizinhos" no item do espaço O(V+E) e "memória" no item de O(grau). A matriz continua corretamente com a necessidade 1.
- **D) ❌** — 1 – 3 – 2 põe a necessidade 1 (consulta de aresta) no item de economia de memória da lista e a necessidade 2 (memória) na matriz. O item do meio (3) está certo, mas a sequência como um todo está errada.

**Diferenças entre versões:**
- Título: no arquivo de questões é "Grafos: Matriz e Lista de **Adjacência**"; no slide, "Grafos: Matriz e Lista".
- Cabeçalho da Coluna 2: no arquivo é "Coluna 2 — Representação **adequada (e razão)**"; no slide, "Coluna 2 — Representação (razão)".
- O arquivo tem a frase "Assinale a alternativa com a associação correta, de cima para baixo:". No slide ela não existe e foi trocada pelo cabeçalho "ALTERNATIVAS (de cima para baixo)".
- O comando termina em "Coluna 2." no arquivo e "Coluna 2" (sem ponto) no slide. No slide, as Colunas 1 e 2 ficam lado a lado.
- Necessidades, itens da Coluna 2, alternativas e gabarito são idênticos. O slide 18 acrescenta "Armadilhas": A e D colocam a necessidade 1 na lista de economia de memória; C troca entre si as duas vantagens da lista.

**⚠️ Atenção:** Isto não afeta o gabarito, mas algumas justificativas do material são imprecisas.
- **C)** Os dois arquivos dizem que a C "troca entre si as duas vantagens da lista **e desloca a matriz de posição**". A segunda parte está errada: em 3 – 2 – 1 a matriz continua associada à necessidade 1, que é o correto. A C erra **só** a troca das duas vantagens da lista. O quadro "armadilhas" do slide 18 descreve a C corretamente, sem falar da matriz.
- **D)** O material diz que a D erra "desalinhando toda a sequência", mas a posição do meio (3) está correta. Ela erra a 1ª e a 3ª posições.

O gabarito **B** está correto.

**Conceito-chave para a prova:** A **matriz** ocupa O(V²) de espaço e responde se há aresta em O(1), mas percorrer os vizinhos custa O(V); serve para grafos **densos**. A **lista** ocupa O(V + E) de espaço, consulta aresta em O(grau) e percorre vizinhos em O(grau); serve para grafos **esparsos**. Se a ordem dos itens da Coluna 2 mudar na prova, refaça a leitura de cima para baixo.

---

## Q6 — Busca em grafos BFS e DFS
**Fonte:** `Questoes_ENADE_Estruturas_de_Dados.pdf`, p. 7 (também em `Apresentacao_Questoes_ENADE (1).pdf`, p. 20 (enunciado) e p. 21 (gabarito), com slide de conceito na p. 19; teoria em `Material_Estruturas_de_Dados.pdf`, p. 15–16)
**Tipo ENADE:** Asserção-razão (CAT 3) · Nível cognitivo: Síntese / Aplicação

**Enunciado:**

SITUAÇÃO-PROBLEMA
Um desenvolvedor júnior sugeriu implementar o recurso "grau de conexão" de uma rede social — que informa o menor número de intermediários entre dois usuários, em um grafo não ponderado (cada amizade tem o mesmo peso) — utilizando a busca em profundidade (DFS). A equipe precisa avaliar criticamente essa proposta.

COMANDO
Considerando os algoritmos de busca em grafos, avalie as asserções a seguir e a relação proposta entre elas.

I. Para encontrar o menor caminho em número de arestas entre dois usuários em um grafo não ponderado, a busca em profundidade (DFS) é a escolha adequada.

PORQUE

II. A DFS percorre o grafo aprofundando-se ao máximo em um ramo antes de retroceder (backtracking) para explorar caminhos alternativos.

**Alternativas:**
- **A)** As asserções I e II são verdadeiras, e a II é uma justificativa correta da I.
- **B)** As asserções I e II são verdadeiras, mas a II não é uma justificativa correta da I.
- **C)** A asserção I é verdadeira, e a II é falsa.
- **D)** A asserção I é falsa, e a II é verdadeira.
- **E)** As asserções I e II são falsas.

**Gabarito: D** — _(origem: gabarito do próprio material, `Questoes...pdf` p. 7 e quadro-resumo p. 8; slides p. 21: "Resposta: D — a asserção I é falsa e a II é verdadeira.")_

**Julgamento das asserções:**
- **I — Falsa.** A DFS não garante o menor caminho em número de arestas: ela pode seguir um ramo longo e achar o destino por um caminho comprido. Quem resolve isso em grafo não ponderado é a **BFS**, que usa fila e explora por níveis (distância 1, depois 2, ...), em O(V + E). O primeiro encontro com o destino já é pela menor distância.
- **II — Verdadeira.** Descreve corretamente a DFS: vai o mais fundo possível e depois faz *backtracking*, usando pilha ou recursão.
- **Relação:** Como a I é falsa, não há justificativa a avaliar. Aliás, o comportamento descrito na II é justamente o motivo de a DFS **não** servir para o menor caminho.

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Supõe a I verdadeira, mas a I é falsa.
- **B) ❌** — Também supõe a I verdadeira.
- **C) ❌** — Inverte tudo: diz que a I é verdadeira e a II é falsa, mas a II descreve corretamente a DFS.
- **D) ✅** — I falsa (menor caminho não ponderado se resolve com BFS) e II verdadeira (descrição correta da DFS).
- **E) ❌** — A II é verdadeira, logo as duas não são falsas.

**Diferenças entre versões:** Situação-problema, asserções, alternativas e gabarito idênticos. Diferenças: o comando do slide termina em "...a relação proposta entre elas" sem ponto final, e o rótulo do slide é "Asserção-Razão · Síntese/Aplicação" (sem "CAT 3"). O slide 21 acrescenta "Armadilhas": A e B assumem a I como verdadeira, mas a DFS não serve para menor caminho; C diz que a II é falsa, mas ela descreve corretamente a DFS; E diz que ambas são falsas, mas a II é verdadeira. O slide de conceito (p. 19) mostra a árvore A→{B, C}, B→{D, E}, C→{F}, com ordem BFS A→B→C→D→E→F e ordem DFS A→B→D→E→C→F. A mesma figura está no material, p. 15.

**Conceito-chave para a prova:** **Menor caminho em grafo não ponderado = BFS** (fila, por níveis). **DFS** (pilha ou recursão, *backtracking*) serve para detectar ciclos, ordenação topológica e componentes conexas. As duas custam O(V + E) com lista de adjacência. Variação provável: "I. A BFS é adequada ao menor caminho PORQUE II. A BFS explora por níveis" dá **A**. Para grafo **ponderado** com pesos não negativos, usa-se Dijkstra, não BFS.
