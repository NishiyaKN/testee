# Estruturas de Dados — Questões INFERIDAS (prováveis questões do banco do squad que não temos)

> ⚠️ **Atenção:** estas questões NÃO constam nos materiais. Foram elaboradas para cobrir os subtópicos do material do
> Squad 9 que não têm questão conhecida, imitando o estilo das questões do squad. Servem para estudo dirigido.
> As questões reais conhecidas estão em `../questoes_por_topico/02_Estruturas_de_Dados.md`.

**Base usada:**
| Arquivo | Páginas | O que foi aproveitado |
|---|---|---|
| `Material_Estruturas_de_Dados.pdf` | 18 (todas lidas; p. 5 e 9 renderizadas para conferir figuras) | Sumário com os **9 tópicos em 4 unidades** da Matriz de Referência (p. 2). Teoria, figuras, código em C, tabelas de complexidade e quadros "Pontos-chave" e "Erros clássicos a evitar" (p. 4–16). Quadro comparativo (p. 17) e referencial (p. 18). |
| `Questoes_ENADE_Estruturas_de_Dados.pdf` | 8 | As 6 questões conhecidas (p. 2–7) e o quadro-resumo (p. 8). Na p. 1 o squad diz que selecionou "os seis tópicos mais recorrentes" e que cada questão segue "o tipo de questão e o nível cognitivo (Taxonomia de Bloom) sugeridos pela Matriz de Referência". |
| `Apresentacao_Questoes_ENADE (1).pdf` | 22 | As mesmas 6 questões, com slides "O que a questão cobra" e "As armadilhas dos distratores". O slide 2 diz que "todas as 6 questões giram em torno de complexidade". |
| `Estrutura de Questões sob o padrão do ENADE.pdf` (guia do professor) | — | Tipologia CAT 1 / CAT 2 / CAT 3 e matriz 3 objetivos × 3 níveis (células A–I = 9 células, o que bate com os "9 tópicos" do squad). |

**Estilo identificado do squad 9 (imitado aqui):**
- Cabeçalho "QUESTÃO N — Tema", com o tipo e a categoria do guia do professor e o nível de Bloom em pares: "Asserção-Razão (CAT 3) · Nível cognitivo: Síntese / Aplicação". Os pares de Bloom usados são **Compreensão / Conhecimento**, **Avaliação / Análise** e **Síntese / Aplicação**.
- Blocos **SITUAÇÃO-PROBLEMA** (sempre um caso prático: playlist, editor de texto, indexação, rede social) → **DADOS DE SUPORTE** "quando aplicável" (código **em C**) → **COMANDO** → **ALTERNATIVAS** → **GABARITO** → **JUSTIFICATIVAS** de cada alternativa ("Incorreta: ...", "(Correta) ...").
- **4 alternativas (A–D)**. **5 alternativas (A–E) só na asserção-razão**, regra declarada pelo squad (p. 1).
- O foco é sempre o **custo das operações** (O(1), O(log n), O(n)), e os distratores exploram os erros apontados no material.
- O squad não cita referências bibliográficas dentro das questões (elas só aparecem no material, p. 18), e por isso as inferidas também não citam.

**Lógica da inferência:**
1. **Quais tópicos faltam:** a matriz tem 9 tópicos (p. 2) e o squad escolheu 6. Os 3 tópicos sem questão são **1 (Ponteiros e alocação dinâmica)**, **2 (Vetores e matrizes)** e **5 (Deques e heaps)**.
2. **Nível de Bloom:** o quadro-resumo diz que as 6 questões "cobrem os três níveis cognitivos (**duas em cada nível**)". Com 9 tópicos, o natural seria **três por nível**. Falta então **uma questão de cada nível**. A principal (Alta) de cada tópico recebeu um nível diferente: T1 = Compreensão/Conhecimento; T2 = Síntese/Aplicação; T5 = Avaliação/Análise.
3. **Tipo:** o squad usou 5 dos 10 tipos do guia (asserção-razão, ordenação, afirmativas múltiplas, afirmativa negativa, associação). As inferidas usam os **5 tipos que faltam** (interpretação, lacunas, resposta única, alternativas constantes, afirmativa incompleta), mais uma asserção-razão, o tipo que o squad já repetiu.
4. **Duas questões por tópico descoberto.** Os três tópicos são extensos e têm destaques no material: o quadro "Erros clássicos a evitar" (T1), a fórmula de endereço repetida na figura e no código (T2), e duas estruturas, com código longo e tabela própria (T5). A 1ª questão de cada tópico é a versão mais provável (Alta) e a 2ª, uma variação (Média).

## Mapa de cobertura
| # | Subtópico (material) | Páginas | Questão conhecida | Questão inferida | Prioridade |
|---|---|---|---|---|---|
| U1-1 | Ponteiros e alocação dinâmica de memória (`&`, `*`, pilha × heap, `malloc`/`free`, memory leak, dangling pointer) | p. 4–5 | — | **I1** (interpretação de código com vazamento) e **I2** (lacunas pilha/heap/leak/dangling) | **Alta** (I1) / Média (I2) |
| U1-2 | Vetores e matrizes contíguas (acesso O(1), row-major, cache, inserir no meio O(n)) | p. 5–6 | — | **I3** (cálculo de endereço row-major) e **I4** (ordem de percurso × cache) | **Alta** (I3) / Média (I4) |
| U1-3 | Listas encadeadas (simples, duplas e circulares) | p. 6–7 | **Q1** (asserção-razão, gab. A) | — · _variação provável: lista circular no round-robin, ou inserção no início O(1) × acesso ao n-ésimo O(n)_ | — |
| U2-4 | Pilhas (LIFO) e filas (FIFO) | p. 8–9 | **Q2** (ordenação, gab. C) — cobra só a pilha (Desfazer/Refazer) | — · _variação provável: fila circular com `% MAX`, enqueue/dequeue O(1), fila usada no escalonamento e na BFS_ | — |
| U2-5 | Deques e filas de prioridade (heaps) | p. 9–10 | — | **I5** (V/F sobre heap e deque) e **I6** (rastreio de `inserir` no min-heap) | **Alta** (I5) / Média (I6) |
| U3-6 | Árvores de busca (BST) e balanceadas (AVL / rubro-negra) | p. 11–12 | **Q3** (afirmativas múltiplas, gab. B) | — · _variação provável: inserir 1, 2, 3, 4, 5 numa BST gera uma "escada" com busca O(n)_ | — |
| U3-7 | Tabela hash e tratamento de colisões | p. 12–13 | **Q4** (afirmativa negativa, gab. D) | — · _variação provável: endereçamento aberto exige α baixo; rehash custa O(n); tamanho primo (M = 101)_ | — |
| U4-8 | Grafos (matriz e lista de adjacência) | p. 14–15 | **Q5** (associação, gab. B) | — · _variação provável: grafo denso → matriz, esparso → lista; percorrer vizinhos custa O(V) na matriz_ | — |
| U4-9 | Algoritmos de busca em grafos (BFS e DFS) | p. 15–16 | **Q6** (asserção-razão, gab. D) | — · _variação provável: "BFS é adequada PORQUE explora por níveis" → A; DFS serve a ciclos e ordenação topológica_ | — |
| (transversal) | Introdução/Big-O (p. 3; slide 2) e Quadro comparativo (p. 17) | p. 3, 17 | Q1–Q6 cobram complexidade de forma transversal | — (fora dos 9 tópicos da matriz) | — |

**Resumo:** 9 subtópicos (os 9 tópicos da Matriz de Referência); 6 já cobertos por questões conhecidas (Q1–Q6); 3 descobertos, que geram **6 questões inferidas** (I1–I6, duas por subtópico). Gabaritos das inferidas: **A** (I1, I6) · **B** (I5) · **C** (I2, I4) · **D** (I3). Somados aos das 6 conhecidas (A, C, B, D, B, D), dão 3 de cada letra A–D.

**Quadro-resumo das inferidas (no formato do quadro da p. 8 do squad):**
| ID | Tema | Tipo de questão | Nível (Bloom) | Gab. |
|---|---|---|---|---|
| I1 | Ponteiros e alocação dinâmica | Interpretação (CAT 1) | Compreensão / Conhecimento | A |
| I2 | Ponteiros e alocação dinâmica | Lacunas (CAT 1) | Compreensão / Conhecimento | C |
| I3 | Vetores e matrizes | Resposta única (CAT 1) | Síntese / Aplicação | D |
| I4 | Vetores e matrizes | Asserção-Razão (CAT 3) | Avaliação / Análise | C |
| I5 | Deques e heaps | Alternativas constantes (CAT 2) | Avaliação / Análise | B |
| I6 | Deques e heaps | Afirmativa incompleta (CAT 1) | Síntese / Aplicação | A |

## Índice
1. [I1 — Ponteiros e vazamento de memória](#i1--ponteiros-e-vazamento-de-memória)
2. [I2 — Pilha heap leak e dangling pointer](#i2--pilha-heap-leak-e-dangling-pointer)
3. [I3 — Endereço de elemento em matriz row-major](#i3--endereço-de-elemento-em-matriz-row-major)
4. [I4 — Ordem de percurso de matriz e cache](#i4--ordem-de-percurso-de-matriz-e-cache)
5. [I5 — Fila de prioridade heap e deque](#i5--fila-de-prioridade-heap-e-deque)
6. [I6 — Inserção em min-heap com sift-up](#i6--inserção-em-min-heap-com-sift-up)

---

## I1 — Ponteiros e vazamento de memória
**Subtópico coberto:** Tópico 1, Ponteiros e alocação dinâmica de memória (Unidade 1, `Material_Estruturas_de_Dados.pdf`, p. 4–5)
**Por que é provável:** é o 1º tópico da matriz, e o material o chama de "a base de tudo" (p. 3). A p. 5 tem um quadro destacado, "ERROS CLÁSSICOS A EVITAR" (memory leak, dangling pointer, não checar o retorno de `malloc`), que se transforma em distratores com facilidade. O squad costuma pôr código C nos DADOS DE SUPORTE (Q1).
**Prioridade:** Alta
**Tipo ENADE:** Interpretação (CAT 1) · Nível cognitivo: Compreensão / Conhecimento

**Enunciado:**

SITUAÇÃO-PROBLEMA
Durante a revisão de código de um equipamento de monitoramento que funciona ininterruptamente e dispõe de pouca memória, a equipe analisa a rotina que lê, a cada ciclo, cinco amostras de um sensor e as guarda em um vetor alocado dinamicamente. Antes de liberar a versão, é preciso entender exatamente o que acontece com a memória a cada ciclo.

DADOS DE SUPORTE
```c
#include <stdio.h>
#include <stdlib.h>

int *criar_vetor(int n) {
    int *v = malloc(n * sizeof(int));   /* (L1) */
    for (int i = 0; i < n; i++)
        v[i] = i * 10;                  /* (L2) */
    return v;                           /* (L3) */
}

int main(void) {
    for (int k = 0; k < 1000; k++) {
        int *dados = criar_vetor(5);
        printf("%d\n", dados[2]);       /* (L4) */
    }                                   /* (L5) */
    return 0;
}
```

COMANDO
Considerando o gerenciamento de memória em C (pilha, heap e alocação dinâmica), assinale a alternativa que interpreta corretamente o comportamento desse código.

**Alternativas:**
- **A)** A cada iteração é impresso o valor 20, mas os blocos alocados em (L1) nunca são liberados com `free`; ao fim de cada iteração perde-se o único ponteiro para o bloco, o que caracteriza vazamento de memória (memory leak).
- **B)** O código gera um ponteiro solto (dangling pointer) em (L3), pois o bloco reservado por `malloc` dentro de `criar_vetor` é descartado da pilha assim que a função retorna, como ocorre com as variáveis locais.
- **C)** Não há desperdício de memória, pois o bloco apontado por `dados` é liberado automaticamente em (L5), quando a variável local `dados` deixa de existir ao final de cada iteração do laço.
- **D)** A linha (L4) é inválida em C, pois a indexação com colchetes só se aplica a vetores declarados estaticamente; para acessar o bloco por meio de um ponteiro seria obrigatório escrever `*(dados + 2)`.

**Gabarito: A**

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — `criar_vetor(5)` reserva no **heap** um bloco de 5 inteiros e o preenche com 0, 10, 20, 30, 40, então `dados[2]` vale **20**. O bloco nunca é liberado. Quando a iteração termina, some a variável `dados`, que está na pilha, e com ela o único endereço do bloco: a memória fica inacessível e não é devolvida ao sistema. É o **memory leak** do quadro da p. 5 ("alocar e nunca chamar `free`"). Em 1000 iterações perdem-se 1000 blocos de 20 bytes, ou 20.000 bytes (conferido com valgrind: "definitely lost: 20,000 bytes in 1,000 blocks"). A correção é chamar `free(dados); dados = NULL;` ao fim de cada iteração. (O código também não checa se `malloc` retornou `NULL` em (L1), que é o terceiro "erro clássico" do material.)
- **B) ❌** — Confunde **pilha** com **heap**. Retornar o endereço de uma variável local (ex.: `int a[5]; return a;`) geraria um ponteiro solto. Mas o bloco de `malloc` está no heap e continua existindo após o retorno da função, até que alguém chame `free`. Só o ponteiro `v` é local; o valor que ele devolve, o endereço no heap, continua válido.
- **C) ❌** — C não tem coleta automática de lixo. O que deixa de existir no fim do escopo é a **variável ponteiro** `dados`, que está na pilha, e não o **bloco apontado**, que está no heap e é "controlado manualmente pelo programador" (p. 4). É justamente isso que causa o vazamento.
- **D) ❌** — Em C, `v[i]` equivale a `*(v + i)` (comentário do código da p. 4). A indexação funciona com qualquer ponteiro, por aritmética de ponteiros, e custa O(1) (tabela da p. 5: "Acesso v[i] em bloco alocado — O(1)").

**Base no material:** p. 4 ("A alocação dinâmica (`malloc`, `calloc`, `realloc`) reserva blocos no heap... Todo bloco alocado deve ser liberado com `free`, senão ocorre vazamento de memória"; "`v[i]` equivale a `*(v + i)`"); p. 5, quadro "ERROS CLÁSSICOS A EVITAR".
**Conceito-chave para a prova:** variável local fica na **pilha** e some no fim do escopo. Bloco de `malloc` fica no **heap** e só sai com `free`. Os três erros clássicos são: não chamar `free` (**memory leak**); usar o ponteiro após `free` (**dangling pointer**, por isso faça `p = NULL`); não checar se `malloc` retornou `NULL`. Variação provável: acrescentar `free(dados);` e depois `printf("%d", dados[2]);`, caso em que a resposta passa a ser **dangling pointer**.

---

## I2 — Pilha heap leak e dangling pointer
**Subtópico coberto:** Tópico 1, Ponteiros e alocação dinâmica de memória (Unidade 1, p. 4–5)
**Por que é provável:** o texto da p. 4 é praticamente uma sequência de definições (`&`, `*`, pilha × heap, `malloc`/`free`, leak), e a Figura 1 opõe "PILHA (stack)" e "HEAP (malloc)". Esse conteúdo encaixa num tipo CAT 1 de conhecimento (lacunas), que o squad ainda não usou.
**Prioridade:** Média
**Tipo ENADE:** Lacunas (CAT 1) · Nível cognitivo: Compreensão / Conhecimento

**Enunciado:**

SITUAÇÃO-PROBLEMA
Um estudante prepara um resumo sobre o uso de memória em C para explicar à equipe por que um programa que manipula listas e árvores precisa de ponteiros e de alocação dinâmica. Ele utiliza o trecho de código a seguir como exemplo.

DADOS DE SUPORTE
```c
int x = 42;                        /* variavel local              */
int *p = &x;                       /* p guarda o ENDERECO de x    */
printf("valor : %d\n", *p);        /* *p desreferencia -> 42      */

int *v = malloc(5 * sizeof(int));  /* bloco reservado em execucao */
if (v == NULL) return 1;           /* SEMPRE checar o retorno     */
/* ... uso de v ... */
free(v);                           /* devolve o bloco ao sistema  */
v = NULL;
```

COMANDO
Complete as lacunas do resumo do estudante:

"A variável local `x` fica armazenada na ______(I)______, região com tempo de vida automático, enquanto o bloco obtido com `malloc` fica no ______(II)______, região controlada manualmente pelo programador. Se o programa deixar de usar o bloco sem chamar `free`, ocorre ______(III)______; se, após `free(v)`, o programa continuar acessando `v[0]`, estará usando um ______(IV)______ — por isso se recomenda fazer `v = NULL` logo após a liberação."

Assinale a alternativa que preenche corretamente as lacunas I, II, III e IV, nessa ordem:

**Alternativas:**
- **A)** heap — pilha (stack) — ponteiro solto (dangling pointer) — vazamento de memória (memory leak)
- **B)** pilha (stack) — heap — ponteiro solto (dangling pointer) — vazamento de memória (memory leak)
- **C)** pilha (stack) — heap — vazamento de memória (memory leak) — ponteiro solto (dangling pointer)
- **D)** heap — pilha (stack) — vazamento de memória (memory leak) — ponteiro solto (dangling pointer)

**Gabarito: C**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Erra os dois pares: põe a variável local no heap e o bloco de `malloc` na pilha, e troca os dois erros entre si.
- **B) ❌** — Acerta as regiões, mas troca os erros. Deixar de chamar `free` é **vazamento**: a memória fica reservada sem uso. Usar o ponteiro **depois** de `free` é **ponteiro solto**: o endereço aponta para memória que já não pertence ao programa.
- **C) ✅** — I: **pilha**, onde "ficam as variáveis locais com tempo de vida automático". II: **heap**, a "região controlada manualmente pelo programador", onde `malloc` reserva blocos. III: **memory leak**, ou seja, "alocar e nunca chamar `free`". IV: **dangling pointer**, ou seja, "usar ponteiro após `free` — sempre faça `p = NULL`".
- **D) ❌** — Acerta os erros, mas troca as regiões. Variáveis locais não ficam no heap, e `malloc` não reserva memória na pilha: reserva no heap "em tempo de execução, quando não se sabe de antemão quanta memória será necessária".

**Base no material:** p. 4 (parágrafos sobre ponteiros, pilha × heap e `malloc`/`free`; Figura 1, "Ponteiro na pilha referenciando dados; bloco alocado no heap"); p. 5, quadro "ERROS CLÁSSICOS A EVITAR".
**Conceito-chave para a prova:** `&x` dá o endereço de `x`, e `*p` dá o valor no endereço guardado em `p`. Variáveis locais ficam na pilha (stack); `malloc`, `calloc` e `realloc` reservam no heap. Esquecer o `free` causa **leak**; usar a memória depois do `free` gera **dangling pointer**. Desreferenciar, `malloc`/`free` (amortizado) e `v[i]` custam O(1). Numa versão alterada, a lacuna pode pedir o operador: `&` obtém o endereço, `*` desreferencia.

---

## I3 — Endereço de elemento em matriz row-major
**Subtópico coberto:** Tópico 2, Vetores e matrizes contíguas (Unidade 1, p. 5–6)
**Por que é provável:** a fórmula `end. m[i][j] = base + (i * NCOLS + j) * sizeof(int)` aparece **duas vezes**, na Figura 2 e no comentário do código (p. 5), junto com o exemplo `int m[3][4]` e o destaque "row-major, padrão do C". É o conteúdo mais "calculável" do tópico e combina com o nível Síntese/Aplicação, o nível que falta.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única (CAT 1) · Nível cognitivo: Síntese / Aplicação

**Enunciado:**

SITUAÇÃO-PROBLEMA
Um sistema de processamento de imagens em C armazena pequenos blocos de pixels em matrizes de inteiros. Para depurar um erro de leitura, um desenvolvedor precisa descobrir, sem executar o programa, em qual endereço de memória está um determinado pixel.

DADOS DE SUPORTE
```c
#define NLIN  3
#define NCOLS 4

int m[NLIN][NCOLS];                 /* matriz 3x4 de inteiros */
for (int i = 0; i < NLIN; i++)
    for (int j = 0; j < NCOLS; j++)
        m[i][j] = i * NCOLS + j;    /* valores de 0 a 11 */
```
Considere que o endereço-base da matriz (endereço de `m[0][0]`) é **1000**, que `sizeof(int) = 4` bytes, que os endereços são expressos em decimal e que o compilador segue o padrão de armazenamento de matrizes da linguagem C.

COMANDO
Qual é o endereço de memória do elemento `m[2][1]`?

**Alternativas:**
- **A)** 1009
- **B)** 1020
- **C)** 1028
- **D)** 1036

**Gabarito: D**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Calcula o deslocamento em **elementos**, i·NCOLS + j = 2·4 + 1 = 9, e esquece de multiplicar por `sizeof(int)`, somando 9 como se fossem bytes. A pegadinha fica mais forte porque o **valor** guardado em `m[2][1]` também é 9.
- **B) ❌** — Usa a ordem **column-major** (coluna a coluna, padrão de Fortran/MATLAB): (j·NLIN + i)·4 = (1·3 + 2)·4 = 20, o que dá 1020. Em C a ordem é **row-major**.
- **C) ❌** — Multiplica `i` pelo número de **linhas** (3), quando o certo é o de **colunas** (4): (2·3 + 1)·4 = 28, o que dá 1028. Cada linha inteira tem NCOLS elementos, e é esse o tamanho que se pula para avançar uma linha.
- **D) ✅** — Em C, a matriz é armazenada linha a linha (row-major): end. = base + (i·NCOLS + j)·sizeof(int) = 1000 + (2·4 + 1)·4 = 1000 + 36 = **1036**. Antes de `m[2][1]` vêm as linhas 0 e 1 inteiras (8 elementos) e mais 1 elemento da linha 2, totalizando 9 elementos × 4 bytes = 36 bytes. (Conferido em C: `&m[2][1] − &m[0][0]` = 36 bytes.) O cálculo é direto, por isso o acesso custa O(1).

**Base no material:** p. 5 ("Em C, matrizes são guardadas em ordem row-major (linha a linha): toda a linha 0 vem antes da linha 1"; Figura 2, "Matriz 3x4 (row-major em C)", com valores 0–11; comentário "endereco de m[i][j] = base + (i * NCOLS + j) * sizeof(int)"); tabela da p. 6 ("Acesso v[i] / m[i][j] — O(1) — cálculo direto do endereço").
**Conceito-chave para a prova:** **vetor**: end(v[i]) = base + i·sizeof. **Matriz em C (row-major)**: end(m[i][j]) = base + (i·**NCOLS** + j)·sizeof. É sempre o número de **colunas** que multiplica i, e no fim multiplica-se por **sizeof**. Se a prova mudar os números, refaça a conta. Ex.: `int m[4][5]`, base 2000, `m[3][2]` dá 2000 + (3·5 + 2)·4 = 2068.

---

## I4 — Ordem de percurso de matriz e cache
**Subtópico coberto:** Tópico 2, Vetores e matrizes contíguas (Unidade 1, p. 5–6)
**Por que é provável:** o material faz uma afirmação de causa e efeito pronta para asserção-razão: "**Por isso** percorrer a matriz na ordem `[i][j]` (linha externa, coluna interna) aproveita melhor a cache do processador do que o contrário" (p. 5). O quadro "Pontos-chave" repete "Contiguidade = acesso O(1) e ótimo aproveitamento de cache" (p. 6). Asserção-razão é o tipo que o squad mais usa (Q1, Q6).
**Prioridade:** Média
**Tipo ENADE:** Asserção-Razão (CAT 3) · Nível cognitivo: Avaliação / Análise

**Enunciado:**

SITUAÇÃO-PROBLEMA
O mesmo sistema de processamento de imagens precisa somar a intensidade de todos os pixels de uma imagem grande, armazenada como matriz `int img[N][N]` (N = 4096). Dois desenvolvedores propuseram versões diferentes do laço, e a equipe precisa decidir qual adotar, sabendo que ambas realizam exatamente N² acessos à matriz.

DADOS DE SUPORTE
```c
/* Versao 1 — linha externa, coluna interna */
for (int i = 0; i < N; i++)
    for (int j = 0; j < N; j++)
        soma += img[i][j];

/* Versao 2 — coluna externa, linha interna */
for (int j = 0; j < N; j++)
    for (int i = 0; i < N; i++)
        soma += img[i][j];
```

COMANDO
Considerando a forma de armazenamento de matrizes em C e o seu efeito sobre o desempenho, avalie as asserções a seguir e a relação proposta entre elas.

I. A versão 1 tende a executar mais rápido que a versão 2, embora ambas tenham complexidade O(N²) e cada acesso individual `img[i][j]` custe O(1).

PORQUE

II. Em C, as matrizes são armazenadas em ordem column-major (coluna a coluna), de modo que os elementos de uma mesma coluna ocupam posições contíguas de memória.

**Alternativas:**
- **A)** As asserções I e II são verdadeiras, e a II é uma justificativa correta da I.
- **B)** As asserções I e II são verdadeiras, mas a II não é uma justificativa correta da I.
- **C)** A asserção I é verdadeira, e a II é falsa.
- **D)** A asserção I é falsa, e a II é verdadeira.
- **E)** As asserções I e II são falsas.

**Gabarito: C**

**Julgamento das asserções:**
- **I — Verdadeira.** As duas versões são O(N²), mas a versão 1 percorre endereços **consecutivos**. Cada linha de cache carregada já traz os próximos elementos que serão usados (localidade espacial). A versão 2 salta NCOLS·sizeof(int) = 4096·4 = 16 KB a cada acesso e provoca muito mais faltas de cache. (Medição local com N = 2048: versão 1 em ≈ 0,05 s, versão 2 em ≈ 0,27 s, cerca de 5× mais lenta.)
- **II — Falsa.** C usa **row-major**, linha a linha (p. 5: "toda a linha 0 vem antes da linha 1 na memória"). Column-major é o padrão de Fortran/MATLAB. Se C fosse column-major, a versão **2** é que seria a mais rápida, então a II contradiz a própria I.
- **Relação:** como a II é falsa, não justifica a I. A justificativa correta seria "em C as matrizes são row-major, e a versão 1 acessa posições contíguas".

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Considera a II verdadeira. Pega quem lembra que "a ordem de armazenamento afeta a cache", mas não lembra qual ordem o C usa.
- **B) ❌** — Também considera a II verdadeira e ainda nega o nexo, que de fato existiria se a II falasse em row-major.
- **C) ✅** — I verdadeira (a versão 1 aproveita a contiguidade e a cache) e II falsa (C é row-major, não column-major).
- **D) ❌** — Considera a I falsa. Pega quem raciocina só pela notação O: "ambas são O(N²), logo têm o mesmo desempenho". A análise assintótica ignora constantes como o custo das faltas de cache.
- **E) ❌** — A I é verdadeira, então as duas não são falsas.

**Base no material:** p. 5 ("Em C, matrizes são guardadas em ordem row-major (linha a linha)... Por isso percorrer a matriz na ordem `[i][j]` (linha externa, coluna interna) aproveita melhor a cache do processador do que o contrário"); p. 6, Pontos-chave ("Contiguidade = acesso O(1) e ótimo aproveitamento de cache"); p. 7 ("Sem contiguidade, [a lista] aproveita pior a cache do que o vetor").
**Conceito-chave para a prova:** C é **row-major**: percorra com `i` (linha) no laço externo e `j` (coluna) no interno. Mesma complexidade O(N²) não significa mesmo tempo real, porque a contiguidade melhora o uso da cache. Variações prováveis: se a II disser "row-major... posições contíguas", o gabarito vira **A**; se a I disser que a versão 2 é mais rápida e a II for a frase correta sobre row-major, vira **D**. Relacionados: o vetor não verifica limites (acesso fora é comportamento indefinido), e inserir ou remover no meio custa O(n).

---

## I5 — Fila de prioridade heap e deque
**Subtópico coberto:** Tópico 5, Deques e filas de prioridade (heaps) (Unidade 2, p. 9–10)
**Por que é provável:** o tópico tem figura própria (Figura 5, min-heap como árvore e vetor), código C longo (`inserir`/`extrair_min`), tabela de complexidade e Pontos-chave com a frase-pegadinha "O heap **não é totalmente ordenado** — só garante a relação pai/filho" (p. 10). É o tópico descoberto com mais conteúdo, e o nível Avaliação/Análise é o que falta para fechar 3 por nível.
**Prioridade:** Alta
**Tipo ENADE:** Alternativas constantes (V/F) (CAT 2) · Nível cognitivo: Avaliação / Análise

**Enunciado:**

SITUAÇÃO-PROBLEMA
Um pronto-atendimento atribui a cada paciente um código numérico de prioridade (quanto **menor** o código, mais urgente) e deseja que o próximo chamado seja sempre o paciente mais urgente, independentemente da ordem de chegada. A equipe de TI avalia implementar essa fila de prioridade com um **min-heap binário armazenado em vetor** e, para o painel que exibe o histórico de chamadas, utilizar um **deque**.

DADOS DE SUPORTE
Estado atual do min-heap (códigos dos pacientes aguardando):

```
            3
          /   \
         5     8
        / \   /
      10   7 12

heap[] = | 3 | 5 | 8 | 10 | 7 | 12 |
          [0] [1] [2] [3]  [4] [5]

/* filhos de i: 2i+1 e 2i+2 ;  pai de i: (i-1)/2 */
```

COMANDO
Avalie as afirmações a seguir, marcando V para as verdadeiras e F para as falsas.

( ) O min-heap mantém sempre o paciente de menor código (o mais urgente) na raiz, em `heap[0]`, de modo que consultar quem será o próximo chamado custa O(1).
( ) Os filhos do nó armazenado na posição i ficam nas posições 2i+1 e 2i+2; assim, os filhos do paciente de código 5 (posição [1]) são os pacientes de códigos 10 e 7.
( ) Como o heap mantém o vetor totalmente ordenado, o painel pode listar todos os pacientes em ordem de urgência simplesmente percorrendo `heap[0]` até `heap[n−1]`.
( ) Inserir um novo paciente e remover o mais urgente custam O(log n), pois o elemento sobe (sift-up) ou desce (sift-down) no máximo a altura da árvore.
( ) O deque usado no painel só permite inserir em uma extremidade e remover na outra, comportando-se exatamente como uma fila FIFO comum.

A sequência correta, de cima para baixo, é:

**Julgamento das afirmações:**
- **1ª — V.** No min-heap "o pai é sempre menor ou igual aos filhos (a raiz é o menor elemento)". Consultar o topo (peek) custa O(1) (tabela da p. 10).
- **2ª — V.** Com i = 1, os filhos ficam em 2·1+1 = 3 e 2·1+2 = 4, ou seja, `heap[3]` = 10 e `heap[4]` = 7, exatamente como na figura (o nó 5 tem filhos 10 e 7).
- **3ª — F.** O heap **não** é totalmente ordenado: só garante a relação pai/filho. No próprio vetor, o 10 (posição [3]) vem antes do 7 (posição [4]). Para obter a ordem completa é preciso extrair o mínimo repetidamente, que é a ideia do heapsort, em O(n log n).
- **4ª — V.** "Inserção e remoção do topo custam O(log n) porque um elemento 'sobe' ou 'desce' no máximo a altura da árvore" (p. 9). A árvore é completa, então a altura é ≈ log n.
- **5ª — F.** O deque (*double-ended queue*) permite inserir **e** remover nas **duas** extremidades em O(1), generalizando pilha e fila. O comportamento descrito é o de uma fila FIFO comum.

**Alternativas:**
- **A)** V – F – F – V – V
- **B)** V – V – F – V – F
- **C)** F – V – V – V – F
- **D)** V – V – V – F – F

**Gabarito: B**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Erra a 2ª (marca F, como quem usaria filhos em 2i e 2i+1, a fórmula de vetor indexado a partir de 1) e a 5ª (aceita o deque como fila FIFO comum).
- **B) ✅** — V – V – F – V – F, conforme o julgamento acima.
- **C) ❌** — Erra a 1ª (nega que a raiz do min-heap é o menor elemento) e a 3ª (aceita o heap como totalmente ordenado, o distrator central da questão).
- **D) ❌** — Erra a 3ª (heap "totalmente ordenado") e a 4ª (nega o custo O(log n) de inserção e remoção, confundindo-o talvez com O(1) ou O(n)).

**Base no material:** p. 9 (definição de deque: "inserir e remover em ambas as extremidades em O(1)"; fila de prioridade: "os elementos saem por prioridade, não por ordem de chegada"; min-heap e índices 2i+1/2i+2; Figura 5); p. 10 (tabela: inserir O(log n), remover o de maior prioridade O(log n), peek O(1), construir heap O(n); Pontos-chave: "O heap não é totalmente ordenado — só garante a relação pai/filho").
**Conceito-chave para a prova:** a **fila de prioridade** sai por importância, e não pela ordem de chegada. Sua implementação clássica é o **heap binário** num vetor: filhos em **2i+1 e 2i+2**, pai em **(i−1)/2**. Peek custa **O(1)**, inserir e extrair custam **O(log n)** e **construir o heap (heapify) custa O(n)**, não O(n log n). O heap **não** é ordenado por inteiro. O **deque** opera nas duas pontas em O(1). O heap é a base do heapsort e de Dijkstra. Variação provável: trocar uma afirmação por "construir o heap a partir de n itens custa O(n log n) obrigatoriamente" (F).

---

## I6 — Inserção em min-heap com sift-up
**Subtópico coberto:** Tópico 5, Deques e filas de prioridade (heaps) (Unidade 2, p. 9–10)
**Por que é provável:** o squad pôs na p. 10 a implementação completa de `inserir` (sift-up) num vetor, e a p. 9 traz o heap de exemplo [3, 5, 8, 10, 7, 12]. Rastrear o código sobre o exemplo do próprio material é o jeito mais direto de cobrar o tópico no nível Síntese/Aplicação, como o squad faz com código C nos DADOS DE SUPORTE.
**Prioridade:** Média
**Tipo ENADE:** Afirmativa incompleta (CAT 1) · Nível cognitivo: Síntese / Aplicação

**Enunciado:**

SITUAÇÃO-PROBLEMA
No sistema de triagem do pronto-atendimento, a fila de prioridade é um min-heap armazenado em vetor (quanto menor o código, mais urgente). Neste momento o vetor contém `heap[] = {3, 5, 8, 10, 7, 12}` (n = 6), e chega um novo paciente com código **4**, inserido pela função a seguir.

DADOS DE SUPORTE
```c
/* MIN-HEAP em vetor: pai(i)=(i-1)/2 ; filhos=2i+1, 2i+2 */
int heap[MAX] = {3, 5, 8, 10, 7, 12}, n = 6;

void inserir(int x) {                                   /* O(log n) */
    heap[n] = x; int i = n++;
    while (i > 0 && heap[(i-1)/2] > heap[i]) {          /* sobe (sift-up) */
        int t = heap[i]; heap[i] = heap[(i-1)/2]; heap[(i-1)/2] = t;
        i = (i-1)/2;
    }
}
```

COMANDO
Após a execução de `inserir(4)`, exatamente como implementada acima, o vetor `heap`, da posição [0] à posição [6], passa a conter a sequência

**Alternativas:**
- **A)** 3, 5, 4, 10, 7, 12, 8
- **B)** 3, 4, 5, 7, 8, 10, 12
- **C)** 3, 5, 8, 10, 7, 12, 4
- **D)** 3, 4, 8, 5, 7, 12, 10

**Gabarito: A**

**Rastreamento:** `heap[6] = 4`, com i = 6 e n = 7. O pai de 6 é (6−1)/2 = 2, e `heap[2]` = 8 > 4, então **troca**, deixando {3, 5, 4, 10, 7, 12, 8}, e i passa a 2. O pai de 2 é (2−1)/2 = 0 (divisão inteira), e `heap[0]` = 3 < 4, então **para**. Houve uma única troca, e o resultado é **3, 5, 4, 10, 7, 12, 8** (conferido compilando e executando o código).

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — Resultado do sift-up: o 4 sobe uma posição, trocando com o pai 8, e para abaixo da raiz 3. A propriedade pai ≤ filhos vale em todo o vetor.
- **B) ❌** — É o vetor **totalmente ordenado**. Ele até seria um min-heap válido, mas não é o que a função produz. O sift-up só troca elementos no caminho da nova folha até a raiz (no máximo ≈ log n trocas) e não reordena o vetor inteiro. É o erro "heap = vetor ordenado" que o material aponta (p. 10).
- **C) ❌** — Ignora o sift-up e deixa o 4 na última posição. Ele ficaria como filho do 8 (posição [2]), violando a regra "todo pai ≤ filhos".
- **D) ❌** — Usa a fórmula de pai **i/2**, própria de heap indexado a partir de 1, num vetor indexado a partir de 0. O 4 seria comparado com `heap[3]` = 10 (troca) e depois com `heap[1]` = 5 (troca). O vetor resultante até satisfaz a propriedade de heap, mas não é o que o código, com pai **(i−1)/2**, executa.

**Base no material:** p. 9 (Figura 5: heap {3, 5, 8, 10, 7, 12}; "filhos de i: 2i+1 e 2i+2 · pai de i: (i−1)/2"); p. 10 (código `inserir` com sift-up, "O(log n)"; Pontos-chave: "O heap não é totalmente ordenado").
**Conceito-chave para a prova:** na **inserção**, o elemento entra na **última** posição e **sobe** (sift-up), trocando com o pai **(i−1)/2** enquanto for menor que ele. Na **extração do mínimo**, a raiz sai, o **último** elemento vai para a raiz e **desce** (sift-down), trocando com o **menor** filho (2i+1 ou 2i+2). Ambas custam O(log n). Variação provável: extrair o mínimo do heap original {3, 5, 8, 10, 7, 12} retorna 3 e deixa {5, 7, 8, 10, 12} (o 12 vai para a raiz e desce trocando com 5 e depois com 7).
