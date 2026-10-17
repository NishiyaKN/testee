# Complexidade de Algoritmos — Questões INFERIDAS (prováveis questões do banco do squad que não temos)

> ⚠️ **Atenção:** estas questões NÃO constam nos materiais. Foram elaboradas para cobrir os subtópicos do material do
> Squad 11 que não têm questão conhecida, imitando o estilo das questões do squad. Servem para estudo dirigido.
> As questões reais conhecidas estão em `../questoes_por_topico/01_Complexidade_de_Algoritmos.md`.

**Base usada:**
- `Manual - Complexidade de Algoritmos.pdf` (15 p., lido por inteiro). Os subtópicos saem do sumário (p. 2): 8 capítulos e 20 seções, além dos estudos de caso das p. 4, 6–7, 8 e 14.
- `Resumo_ Complexidade de algoritmos (1).pdf` (16 p.). Os slides de conteúdo estão nas p. 2, 3, 5, 7, 9, 11, 13 e 14, e as questões Q1–Q6, em imagem, nas p. 4, 6, 8, 10, 12 e 15.
- **Estilo identificado do squad (Q1–Q6):**
  - Blocos **SITUAÇÃO-PROBLEMA / DADOS DE SUPORTE / COMANDO DA QUESTÃO / ALTERNATIVAS DE RESPOSTA**, com **sempre 4 alternativas (A–D)**.
  - Os dados de suporte abrem com "De acordo com Cormen et al. (2012)" (na Q2, "Knuth (1997) e Cormen et al. (2012)").
  - Os cenários são corporativos (SGBD, IoT, geoprocessamento, e-commerce, SLA, backend) e repetem expressões como "recusando-se a confiar em intuições vagas ou estimativas superficiais", "dados de suporte", "alta performance" e "Modelo de Knuth".
  - Tipos usados: asserção-razão (Q1); afirmativas múltiplas I–III com as alternativas fixas "I e II / I e III / II e III / I, II e III" (Q2); ordenação (Q3); resposta única com código C (Q4) e com análise (Q5); afirmativa negativa INCORRETA (Q6).
  - **Cada questão do squad converte um estudo de caso já resolvido no manual.** As inferidas fazem o mesmo com as seções do manual e dos slides que nenhuma questão conhecida usa.
- **Temas verificados e ausentes do material:** classes P/NP, backtracking, análise amortizada e uma seção própria de complexidade de espaço. O espaço aparece só como coluna de memória na Tabela 3 e no estudo de caso do top-k. O "classes de complexidade" da capa do manual se refere às classes O/Θ da Tabela 1. Por isso **não criei questões sobre esses temas**.
- Todos os cálculos foram conferidos com python3: médias, somatórios, constantes de Θ, recorrências, contagem de comparações do Quicksort, altura de ABP degenerada e percursos.

## Mapa de cobertura
| # | Subtópico (material) | Páginas | Questão conhecida | Questão inferida | Prioridade |
|---|---|---|---|---|---|
| 1 | Categorias de tempo e escala clássica (Tabela 1: denominação e comportamento típico de cada classe) | Manual p. 3 (§1.1); slides p. 2 | Q3 cobra só a **ordem** das classes | **I5** | Média |
| 2 | Regra de dominância assintótica (lim f/g = 0; desprezar constantes e termos menores) | Manual p. 3 (§1.2); slides p. 2 | Q3 (simplificações) e Q1 (limite) | — (variação provável: a Q3 com outras funções, ex. log₂(n¹⁰), n log₂(n²), 2ⁿ + n¹⁰⁰) | — |
| 3 | Estudo de caso: ordenação de 5 algoritmos concorrentes | Manual p. 4 | Q3 | — | — |
| 4 | Definições formais de O, Ω e Θ (o "sanduíche") | Manual p. 4 (§2.1); slides p. 3 | Q1 cobra só o Big-O | **I4** | Alta |
| 5 | Prova de dominância n² × n log₂ n | Manual p. 4–5 (§2.2) | Q1 | — (variação provável: inverter para "n log₂ n = O(n²)", e a resposta passa a "I e II verdadeiras, II justifica I") | — |
| 6 | Modelo de Knuth e busca sequencial com sentinela (pior e melhor caso) | Manual p. 6–7 (§3); slides p. 5 | Q2 | — (variação provável: cobrar T_melhor = c₁ + c₂ + c₄ + c₅ ou a frequência n − 1 do incremento) | — |
| 7 | Pior caso, melhor caso e caso médio | Manual p. 8 (§4.1); slides p. 7 | — (o slide p. 7 antecede a Q3, mas a Q3 cobra ordenação de funções) | **I1** | Alta |
| 8 | Trade-offs de busca (Tabela 2: linear, binária, hash) e degradação do hash | Manual p. 8 (§4.2 + quadro) | parcial: QP1 do professor (pior caso da binária) e Q6-D (hash Θ(n)) | **I2** | Média |
| 9 | Laços triangularmente aninhados (soma de Gauss) | Manual p. 9 (§5.1); slides p. 9 | — (só aparece como distrator C da Q4) | **I3** | Alta |
| 10 | Laços logarítmicos e PG decrescente (2n − 1) | Manual p. 9 (§5.2); slides p. 9 | Q4 | — (variação provável: laço interno `j < n` em vez de `j < i` dá n(log₂ n + 1), Θ(n log n)) | — |
| 11 | Teorema Mestre: estrutura e os 3 casos | Manual p. 10 (§6.1); slides p. 11 | Q5 (só Casos 1 e 3) | **I6** (Caso 2) | Média |
| 12 | Estratégias concorrentes Alfa × Beta | Manual p. 10–11 (§6.2) | Q5 | — | — |
| 13 | Paradigmas clássicos de projeto (força bruta, D&C, guloso, PD) | Manual p. 12 (§7.1); ausente dos slides | — | **I7** | Média |
| 14 | Ordenação: Tabela 3 e trade-offs Merge × Quick × Heap | Manual p. 12 (§7.2–7.3); slides p. 13 | parcial: Q6-A (Merge, memória Θ(n)) e Q6-C (Heapsort não é O(n)) | **I8, I9** | Alta |
| 15 | ABP: custo médio e degeneração sem balanceamento | Manual p. 13 (§8.1); slides p. 14 | — | **I10** | Alta |
| 16 | ABP: percursos pré-, em- e pós-ordem | Manual p. 13 (§8.1); figura da ABP no slide p. 14 | — | **I11** | Média |
| 17 | Hashing: encadeamento × endereçamento aberto, fator de carga α | Manual p. 13 (§8.2); slides p. 14 | parcial: Q6-D (só o pior caso do encadeamento) | **I12** | Média |
| 18 | Heap (Min/Max) e filtragem das k maiores | Manual p. 13–14 (§8.3); slides p. 14 | Q6 | — (variação provável: Max-Heap de tamanho k como distrator) | — |

**Resumo:** 18 subtópicos. 7 já cobertos por questões conhecidas (Q1–Q6). 12 questões inferidas para os 11 subtópicos restantes (2 para o subtópico de ordenação, enfatizado na Tabela 3, no §7.3 e no slide p. 13). Gabaritos: **A** = 3 (I4, I9, I12), **B** = 3 (I1, I3, I10), **C** = 3 (I2, I7, I11), **D** = 3 (I5, I6, I8).

## Índice
1. [I1 — Pior caso, melhor caso e caso médio](#i1--pior-caso-melhor-caso-e-caso-médio)
2. [I2 — Trade-offs de busca: linear, binária e hash](#i2--trade-offs-de-busca-linear-binária-e-hash)
3. [I3 — Laço triangular e soma de Gauss](#i3--laço-triangular-e-soma-de-gauss)
4. [I4 — Definições formais de O, Ω e Θ](#i4--definições-formais-de-o-ω-e-θ)
5. [I5 — Escala clássica de complexidade (associação)](#i5--escala-clássica-de-complexidade-associação)
6. [I6 — Teorema Mestre: Caso 2 no Merge Sort (lacunas)](#i6--teorema-mestre-caso-2-no-merge-sort-lacunas)
7. [I7 — Paradigmas de projeto de algoritmos (associação)](#i7--paradigmas-de-projeto-de-algoritmos-associação)
8. [I8 — Escolha do algoritmo de ordenação sob restrição de memória](#i8--escolha-do-algoritmo-de-ordenação-sob-restrição-de-memória)
9. [I9 — Pior caso do Quicksort (asserção-razão)](#i9--pior-caso-do-quicksort-asserção-razão)
10. [I10 — Degeneração da ABP (asserção-razão)](#i10--degeneração-da-abp-asserção-razão)
11. [I11 — Percursos em ABP: serialização e liberação](#i11--percursos-em-abp-serialização-e-liberação)
12. [I12 — Tabelas hash: colisões e fator de carga (V/F)](#i12--tabelas-hash-colisões-e-fator-de-carga-vf)

---

## I1 — Pior caso, melhor caso e caso médio
**Subtópico coberto:** Cenários de desempenho computacional (manual §4.1, p. 8; slide "Variação de Comportamento Dinâmico", p. 7)
**Por que é provável:** Dos 6 slides de conteúdo, este é o único cuja questão seguinte (Q3) não o cobra. O manual dedica uma seção inteira ao tema e o associa explicitamente a SLA e a sistemas de tempo real, vocabulário recorrente nas questões do squad.
**Prioridade:** Alta
**Tipo ENADE:** Afirmativas múltiplas (mesmo formato da Q2)

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
Uma instituição financeira está desenvolvendo um motor de autorização de pagamentos instantâneos que precisa responder a cada requisição dentro de um acordo de nível de serviço (SLA) de latência máxima rigorosamente contratado. Um dos componentes críticos localiza o cadastro do cliente por meio de uma busca linear em um vetor não ordenado de *n* registros de dados de suporte. Antes de homologar o componente, o engenheiro responsável precisa decidir qual cenário de análise deve fundamentar o dimensionamento da infraestrutura do backend, recusando-se a confiar em intuições vagas ou em medições superficiais feitas com poucas entradas favoráveis.

**DADOS DE SUPORTE**
De acordo com Cormen et al. (2012), o comportamento assintótico de um algoritmo não é estático: ele varia dinamicamente em função do estado inicial e da distribuição dos dados de suporte da entrada. Por essa razão, a análise de algoritmos é estruturada em três cenários fundamentais: pior caso, melhor caso e caso médio.

Considere que, na busca linear, cada comparação entre a chave procurada e um registro tem custo constante e que, no caso médio, a chave está presente e é igualmente provável em qualquer uma das *n* posições (distribuição uniforme). Analise as afirmativas a seguir:

**I.** A análise de pior caso define o limite superior de tempo para qualquer entrada de tamanho *n* e, por isso, é o critério adequado para garantir o cumprimento do SLA em sistemas críticos de tempo real; na busca linear, esse limite é Θ(*n*), atingido quando a chave está na última posição ou ausente.

**II.** A análise de melhor caso é a mais indicada para dimensionar o backend sob picos de carga, pois, como a busca linear encontra a chave em tempo Θ(1) quando ela está na primeira posição, garante-se que nenhuma requisição excederá tempo constante.

**III.** A análise de caso médio modela estatisticamente o comportamento do algoritmo sob todas as entradas possíveis de tamanho *n*; com a chave equiprovável entre as *n* posições, o número esperado de comparações é (*n* + 1)/2, o que mantém a busca linear na classe Θ(*n*).

**COMANDO DA QUESTÃO**
Considerando os cenários de desempenho computacional e as classes de complexidade da Notação Big-O, é correto o que se afirma em:

**Alternativas:**
- **A)** I e II, apenas.
- **B)** I e III, apenas.
- **C)** II e III, apenas.
- **D)** I, II e III.

**Gabarito: B**

**Julgamento das afirmativas:**
- **I — Verdadeira.** O pior caso "garante que o algoritmo nunca demandará mais recursos do que o limite calculado, o que é vital para acordos de nível de serviço (SLA) e sistemas críticos de tempo real" (manual p. 8). Na Tabela 2, o pior caso da busca linear é Θ(*n*), com "chave na última posição ou ausente".
- **II — Falsa.** O melhor caso descreve o cenário **mais favorável**, não uma garantia. Uma requisição cuja chave esteja no fim do vetor custa Θ(*n*). Segundo o manual (p. 8) e o slide p. 7, o melhor caso serve para "validar otimizações lógicas e … caminhos rápidos (fast-paths)", e não para dimensionar picos de carga.
- **III — Verdadeira.** Com a chave equiprovável, a média de comparações é (1 + 2 + … + *n*)/*n* = (*n* + 1)/2. Conferi em python3: 5,5 para *n* = 10 e 500,5 para *n* = 1.000. A constante 1/2 não muda a classe, que continua Θ(*n*), o mesmo caso médio da Tabela 2.

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Inclui a II, que confunde "cenário mais favorável" com "garantia de tempo".
- **B) ✅** — Só I e III são verdadeiras.
- **C) ❌** — Inclui a II e exclui a I, que é exatamente a definição do manual para o pior caso.
- **D) ❌** — A II é falsa.

**Base no material:** manual p. 8, §4.1: pior caso = "limite superior… vital para SLA e sistemas críticos de tempo real"; melhor caso = "fast-paths"; caso médio = "distribuição de probabilidade (comumente uniforme)". Tabela 2 (busca linear: Θ(1), Θ(*n*), Θ(*n*)). Slide p. 7: "Pior Caso… Vital para SLAs e sistemas de tempo real críticos".
**Conceito-chave para a prova:** O pior caso dá a garantia (SLA), o caso médio supõe uma distribuição (uniforme) e reflete o uso cotidiano, e o melhor caso só serve para validar fast-paths. Na busca linear, a média de (*n*+1)/2 comparações continua sendo Θ(*n*).

---

## I2 — Trade-offs de busca: linear, binária e hash
**Subtópico coberto:** Trade-offs em algoritmos fundamentais de busca, Tabela 2 e "Análise de Degradação Crítica: Tabelas Hash com Colisões" (manual §4.2, p. 8)
**Por que é provável:** A Tabela 2 é a única tabela comparativa do capítulo 4 e vem acompanhada de um quadro de destaque sobre a degradação do hash. A questão-exemplo do professor (QP1) só cobra o pior caso da busca binária.
**Prioridade:** Média
**Tipo ENADE:** Resposta única (interpretação de tabela)

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
Uma empresa de logística está reestruturando o serviço de rastreamento de encomendas, que precisa localizar registros pelo código de rastreio entre *n* pacotes ativos. Três equipes propuseram estruturas concorrentes: (i) busca linear em uma lista não ordenada; (ii) busca binária em um vetor mantido ordenado pelo código; e (iii) tabela de dispersão (hash) com resolução de colisões por encadeamento. Para escolher a solução sem se apoiar em estimativas superficiais, o arquiteto de software exige a comparação formal dos três cenários de desempenho de cada proposta.

**DADOS DE SUPORTE**
De acordo com Cormen et al. (2012), o desempenho de um algoritmo de busca depende da organização dos dados de suporte e da distribuição das chaves de entrada. A tabela de dispersão com encadeamento simples apresenta tempo de busca estatisticamente ideal sob um fator de carga estável α = *n*/*m*; contudo, se a função de espalhamento não for uniformemente distribuída e ocorrerem colisões críticas, todas as *n* chaves podem ser mapeadas para a mesma posição da tabela, e a estrutura degenera em uma lista encadeada linear simples.

**COMANDO DA QUESTÃO**
Assinale a alternativa que apresenta corretamente, para cada proposta, as complexidades de tempo de busca no melhor caso, no caso médio e no pior caso, nessa ordem:

**Alternativas:**
- **A)** Busca linear: Θ(1), Θ(*n*), Θ(*n*); busca binária: Θ(log *n*), Θ(log *n*), Θ(log *n*); tabela hash: Θ(1), Θ(1), Θ(1).
- **B)** Busca linear: Θ(*n*), Θ(*n*), Θ(*n*); busca binária: Θ(1), Θ(log *n*), Θ(*n*); tabela hash: Θ(1), Θ(log *n*), Θ(*n*).
- **C)** Busca linear: Θ(1), Θ(*n*), Θ(*n*); busca binária: Θ(1), Θ(log *n*), Θ(log *n*); tabela hash: Θ(1), Θ(1), Θ(*n*).
- **D)** Busca linear: Θ(1), Θ(log *n*), Θ(*n*); busca binária: Θ(1), Θ(1), Θ(log *n*); tabela hash: Θ(1), Θ(1), Θ(log *n*).

**Gabarito: C**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Erra em dois pontos. O melhor caso da busca binária é Θ(1), quando a chave é o elemento do meio e é achada na 1ª comparação. E o pior caso do hash é Θ(*n*), não Θ(1). Explora a intuição vaga de que "hash é sempre O(1)".
- **B) ❌** — O melhor caso da busca linear é Θ(1) (chave na 1ª posição). O pior caso da binária em vetor ordenado é Θ(log *n*): vetor ordenado não "degenera", o que só acontece com a ABP sem balanceamento. E o caso médio do hash é Θ(1), não Θ(log *n*).
- **C) ✅** — Reproduz a Tabela 2 do manual: linear Θ(1)/Θ(*n*)/Θ(*n*), binária Θ(1)/Θ(log *n*)/Θ(log *n*) e hash com encadeamento Θ(1)/Θ(1)/Θ(*n*). O pior caso do hash é a colisão de todas as chaves.
- **D) ❌** — O caso médio da busca linear é Θ(*n*) ((*n*+1)/2 comparações), não Θ(log *n*). O caso médio da binária é Θ(log *n*). E o hash degenerado vira lista encadeada (Θ(*n*)), não árvore (Θ(log *n*)).

**Base no material:** manual p. 8, Tabela 2 e o quadro "Análise de Degradação Crítica" ("a tabela de dispersão degenera em uma lista encadeada linear simples… degrada de… Θ(1) para… Θ(*n*)"). Slide p. 14: "Acesso em Θ(1). A degradação via alta colisão (encadeamento saturado) pode forçar buscas para Θ(*n*) absoluto".
**Conceito-chave para a prova:** Linear: 1 / *n* / *n*. Binária: 1 / log *n* / log *n*. Hash com encadeamento: 1 / 1 / *n*. ⚠️ A Tabela 2 do manual dá como causa do pior caso da binária "chave na raiz ou folha". Na raiz (o meio do vetor) é o **melhor** caso. O pior caso é a chave numa folha ou ausente.

---

## I3 — Laço triangular e soma de Gauss
**Subtópico coberto:** Laços triangularmente aninhados e somatórios aritméticos (manual §5.1, p. 9; slide "Modelagem de Laços Iterativos", p. 9, caixa da esquerda)
**Por que é provável:** O slide p. 9 tem duas caixas lado a lado, "Laços Triangularmente Aninhados" e "Redução Geométrica de Escopo". A Q4 cobra só a segunda, e a fórmula n(n+1)/2 = Θ(n²) da primeira aparece apenas como distrator. Seria natural o banco ter a questão "irmã" da Q4.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única (cálculo / análise de código, mesmo formato da Q4)

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
Uma equipe de engenharia de uma operadora de telecomunicações desenvolve um módulo de correlação de sinais para detectar interferências entre antenas. O módulo processa cada par de leituras (*i*, *j*) com *j* ≤ *i*, em uma janela de *n* amostras, por meio de dois laços de repetição aninhados cujo laço interno depende dinamicamente do laço externo. Antes de liberar o módulo para produção, os engenheiros precisam determinar com rigor a contagem exata das operações críticas executadas, recusando-se a confiar na intuição vaga de que "dois laços aninhados sempre executam *n* × *n* vezes".

**DADOS DE SUPORTE**
De acordo com Cormen et al. (2012), a análise de laços aninhados com dependências de controle exige traduzir as condições lógicas e especificações de repetição em somatórios matemáticos rigorosos.

Considere o seguinte trecho de código-fonte em linguagem C:

```c
int correlacionar_sinais(int n) {
    int total = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            total++; // processar_sinal(i, j): operacao critica de custo constante
        }
    }
    return total;
}
```

Considere também a fórmula da soma dos *n* primeiros termos de uma progressão aritmética (PA):

*S*ₙ = *n* · (*a*₁ + *a*ₙ) / 2

**COMANDO DA QUESTÃO**
A partir da análise do fluxo lógico de repetição do algoritmo e aplicando as propriedades de somatórios, assinale a alternativa que apresenta a contagem exata do número de operações críticas realizadas e sua respectiva classificação assintótica de pior caso:

**Alternativas:**
- **A)** A contagem exata é expressa por *n*² operações críticas, pois o laço interno executa *n* vezes para cada iteração do laço externo, estabelecendo uma classe de complexidade de tempo quadrática de ordem Θ(*n*²).
- **B)** A contagem exata é expressa por *n*(*n* + 1)/2 operações críticas (500.500 para *n* = 1.000), estabelecendo uma classe de complexidade de tempo quadrática de ordem Θ(*n*²).
- **C)** A contagem exata é expressa por 2*n* − 1 operações críticas, pois o escopo do laço interno é limitado pelo laço externo, estabelecendo uma classe de complexidade de tempo linear de ordem Θ(*n*).
- **D)** A contagem exata é expressa por *n* log₂ *n* operações críticas, pois o laço interno percorre, em média, metade do laço externo, estabelecendo uma classe de complexidade de tempo linearítmica de ordem Θ(*n* log *n*).

**Gabarito: B**

**Cálculo:** Para cada *i* de 1 a *n*, o laço interno executa *i* vezes. Então *S* = 1 + 2 + … + *n*, uma PA com *a*₁ = 1 e *a*ₙ = *n*: *S* = *n*(1 + *n*)/2 = 0,5*n*² + 0,5*n*, e o termo de 2º grau domina, portanto **Θ(*n*²)**. Simulei em python3: *n* = 10 dá 55 e *n* = 1.000 dá 500.500.

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — A classe está certa, mas a contagem está errada. É a "intuição vaga" citada no próprio enunciado: o laço interno executa *i* vezes, não *n*. Para *n* = 1.000, seriam 1.000.000 operações, contra as 500.500 reais.
- **B) ✅** — Soma de Gauss exata, com a classe quadrática.
- **C) ❌** — 2*n* − 1 é a soma da PG do laço em que *i* é **dividido por 2** (Q4). Aqui *i* cresce de 1 em 1, então a soma é aritmética.
- **D) ❌** — "Metade em média" dá *n* · *n*/2, que é quadrático. A metade é só uma constante e não gera fator logarítmico. Para *n* = 1.000, *n* log₂ *n* ≈ 9.966, longe de 500.500.

**Base no material:** manual p. 9, §5.1: `for (int i = 1; i <= n; i++) { for (int j = 1; j <= i; j++) { processar_sinal(i, j); } }`, *S* = *n*(*n*+1)/2 = 0,5*n*² + 0,5*n*, Θ(*n*²). Slide p. 9: "O laço interno depende dinamicamente do laço externo. Solucionado via Soma de Gauss (Progressão Aritmética)", Σ *i* = *n*(*n*+1)/2 = Θ(*n*²).
**Conceito-chave para a prova:** Com o laço interno de 1 até *i* (inclusivo), a contagem é *n*(*n*+1)/2. Com `j < i` (de 0 ou de 1 até *i* − 1), é *n*(*n*−1)/2, que dá 499.500 para *n* = 1.000. As duas são Θ(*n*²). Se o escopo for dividido por 2 a cada volta, a contagem é 2*n* − 1, Θ(*n*).

---

## I4 — Definições formais de O, Ω e Θ
**Subtópico coberto:** Definições matemáticas formais de limites assintóticos (manual §2.1, p. 4; slide "Ordens Assintóticas e Limites", p. 3)
**Por que é provável:** O slide p. 3 dedica um cartão a cada notação (O, Θ e Ω), com a desigualdade de cada uma, mas a Q1 só usa a definição de Big-O. Θ ("sanduíche") e Ω ficaram sem questão.
**Prioridade:** Alta
**Tipo ENADE:** Afirmativas múltiplas

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
Durante a revisão técnica de um serviço de indexação de documentos para um mecanismo de busca corporativo, um engenheiro obteve, por meio do Modelo de Knuth, a função de custo exata *f*(*n*) = 3*n*² + 10*n* para a rotina de montagem do índice invertido sobre *n* documentos. O relatório de homologação exige que o desempenho seja classificado com as três notações assintóticas formais, e não com estimativas superficiais, apresentando as constantes que satisfazem cada definição.

**DADOS DE SUPORTE**
De acordo com Cormen et al. (2012), dizemos que:
- *f*(*n*) = *O*(*g*(*n*)) se existirem constantes reais positivas *c* e *n*₀ tais que 0 ≤ *f*(*n*) ≤ *c* · *g*(*n*) para todo *n* ≥ *n*₀ (limite superior);
- *f*(*n*) = Ω(*g*(*n*)) se existirem constantes reais positivas *c* e *n*₀ tais que 0 ≤ *c* · *g*(*n*) ≤ *f*(*n*) para todo *n* ≥ *n*₀ (limite inferior);
- *f*(*n*) = Θ(*g*(*n*)) se existirem constantes reais positivas *c*₁, *c*₂ e *n*₀ tais que 0 ≤ *c*₁ · *g*(*n*) ≤ *f*(*n*) ≤ *c*₂ · *g*(*n*) para todo *n* ≥ *n*₀ (limite estrito ou firme, que opera como um "sanduíche" funcional).

Analise as afirmativas a seguir sobre a função *f*(*n*) = 3*n*² + 10*n*:

**I.** *f*(*n*) = Θ(*n*²), pois as constantes *c*₁ = 3, *c*₂ = 4 e *n*₀ = 10 satisfazem 3*n*² ≤ 3*n*² + 10*n* ≤ 4*n*² para todo *n* ≥ 10.

**II.** *f*(*n*) = Ω(*n*), pois, com *c* = 1 e *n*₀ = 1, tem-se 0 ≤ *n* ≤ 3*n*² + 10*n* para todo *n* ≥ 1; esse limite inferior é válido, embora não seja firme, já que *f*(*n*) não é *O*(*n*).

**III.** *f*(*n*) = *O*(*n*), pois, pela regra de dominância assintótica, retém-se o termo de maior coeficiente multiplicativo, e o termo linear 10*n* possui coeficiente maior que o do termo quadrático 3*n*².

**COMANDO DA QUESTÃO**
Considerando as definições formais de limites assintóticos e a regra de dominância assintótica, é correto o que se afirma em:

**Alternativas:**
- **A)** I e II, apenas.
- **B)** I e III, apenas.
- **C)** II e III, apenas.
- **D)** I, II e III.

**Gabarito: A**

**Julgamento das afirmativas:**
- **I — Verdadeira.** O limite inferior 3*n*² ≤ 3*n*² + 10*n* vale para todo *n* ≥ 0. O superior vale assim: 3*n*² + 10*n* ≤ 4*n*² ⇔ 10*n* ≤ *n*² ⇔ *n* ≥ 10. Conferi em python3 que vale para todo *n* de 10 a 10⁵ e falha em *n* = 9 (333 > 324), então *n*₀ = 10 é o menor possível com *c*₂ = 4.
- **II — Verdadeira.** *n* ≤ 3*n*² + 10*n* para todo *n* ≥ 1, logo *f* = Ω(*n*). Mas *f*(*n*)/*n* = 3*n* + 10 → ∞, então *f* ≠ *O*(*n*) e Ω(*n*) é só um limite inferior "frouxo", não firme.
- **III — Falsa.** A regra de dominância (manual p. 3) retém o termo de maior **ordem** (grau), e não o de maior coeficiente. Os coeficientes são justamente o que se despreza. Como lim (3*n*² + 10*n*)/*n* = ∞, *f* ≠ *O*(*n*).

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — Só I e II são verdadeiras.
- **B) ❌** — Inclui a III, que confunde "maior coeficiente" com "maior ordem".
- **C) ❌** — Exclui a I, cujas constantes estão corretas, e inclui a III.
- **D) ❌** — A III é falsa.

**Base no material:** manual p. 4, §2.1 (definições com *c* > 0, *n*₀ ≥ 1, e Θ com *c*₁, *c*₂). Manual p. 3, §1.2 ("termos de menor ordem e as constantes multiplicativas e aditivas são desprezados, retendo-se apenas o termo de maior grau"). Slide p. 3 (O "tempo máximo garantido", Θ "sanduíche funcional", Ω "requererá pelo menos este tempo").
**Conceito-chave para a prova:** Θ = O e Ω ao mesmo tempo. Para provar Θ, mostre as duas constantes e o *n*₀. Um limite inferior verdadeiro, como Ω(*n*) para *n*², pode não ser firme. A dominância é pelo **grau**, nunca pelo coeficiente.

---

## I5 — Escala clássica de complexidade (associação)
**Subtópico coberto:** Categorias de tempo de execução e escala de crescimento, Tabela 1 (manual §1.1, p. 3; slide "Taxa de Crescimento Assintótico", p. 2)
**Por que é provável:** A Tabela 1 é a primeira tabela do manual e associa cada classe a um comportamento típico. A Q3 cobra só a ordem das classes, não o significado de cada uma.
**Prioridade:** Média
**Tipo ENADE:** Associação

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
Uma consultoria de software foi contratada para auditar o desempenho de quatro rotinas de um sistema de gestão empresarial (ERP) que apresentam lentidão sob grandes volumes de dados corporativos. Para fundamentar o relatório técnico e afastar intuições vagas, o auditor precisa associar cada classe de complexidade identificada na modelagem analítica das rotinas ao comportamento típico que ela descreve à medida que o tamanho da entrada *n* tende ao infinito.

**DADOS DE SUPORTE**
De acordo com Cormen et al. (2012), a taxa de crescimento determina quão rápido o consumo de tempo se eleva à medida que *n* → ∞, compondo uma escala clássica de ordens de eficiência, do algoritmo de maior eficiência ao de menor eficiência: Θ(1) < Θ(log *n*) < Θ(*n*) < Θ(*n* log *n*) < Θ(*n*²) < Θ(*n*³) < Θ(2ⁿ).

Relacione as classes de complexidade da Coluna 1 às descrições da Coluna 2.

| Coluna 1 | Coluna 2 |
|---|---|
| 1. Θ(log *n*) | ( ) Característico de laços triplos aninhados ou da multiplicação ingênua de matrizes. |
| 2. Θ(*n* log *n*) | ( ) Crescimento extremamente lento; típico de divisões sucessivas do espaço de busca. |
| 3. Θ(*n*³) | ( ) Inviável para entradas de média ou larga escala; típico de busca por força bruta. |
| 4. Θ(2ⁿ) | ( ) Eficiência típica de algoritmos ótimos de ordenação baseados em divisão e conquista. |

**COMANDO DA QUESTÃO**
Assinale a alternativa que apresenta a sequência correta da Coluna 2, de cima para baixo:

**Alternativas:**
- **A)** 1 – 3 – 4 – 2.
- **B)** 3 – 1 – 2 – 4.
- **C)** 4 – 1 – 3 – 2.
- **D)** 3 – 1 – 4 – 2.

**Gabarito: D**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Atribui Θ(log *n*) aos laços triplos e Θ(*n*³) às divisões sucessivas, trocando a classe mais lenta de crescer pela mais rápida das polinomiais.
- **B) ❌** — Inverte as duas últimas: coloca Θ(*n* log *n*) como força bruta inviável e Θ(2ⁿ) como ordenação ótima.
- **C) ❌** — Atribui Θ(2ⁿ) aos laços triplos e Θ(*n*³) à força bruta. Confunde crescimento polinomial com exponencial.
- **D) ✅** — Laços triplos e multiplicação ingênua de matrizes são Θ(*n*³) (3). Divisões sucessivas, Θ(log *n*) (1). Força bruta, Θ(2ⁿ) (4). Ordenação ótima por divisão e conquista, Θ(*n* log *n*) (2).

**Base no material:** manual p. 3, Tabela 1 ("Escala Clássica de Complexidade e Ordens de Crescimento"). As descrições da Coluna 2 são transcrições quase literais da coluna "Comportamento sob Crescimento da Entrada". Slide p. 2: Θ(1) < Θ(log n) < Θ(n) < Θ(n log n) < Θ(n²) < Θ(n³) < Θ(2ⁿ).
**Conceito-chave para a prova:** Θ(1) não depende de *n*. Θ(log *n*) vem de divisões sucessivas (busca binária). Θ(*n*) cresce proporcionalmente à entrada. Θ(*n* log *n*) é a ordenação ótima (Merge Sort). Θ(*n*²) vem de laços duplos simples ou triangulares. Θ(*n*³), de laços triplos e multiplicação ingênua de matrizes. Θ(2ⁿ), de força bruta.

---

## I6 — Teorema Mestre: Caso 2 no Merge Sort (lacunas)
**Subtópico coberto:** A estrutura das recorrências e os três casos do Teorema Mestre (manual §6.1, p. 10; slide "Recursão e Teorema Mestre", p. 11)
**Por que é provável:** O slide p. 11 lista os três casos ("Recursão domina", "Equilíbrio", "Combinação domina"), mas a Q5 só exercita os Casos 1 e 3. O Caso 2 ("o custo logarítmico é incorporado") aparece apenas em distratores.
**Prioridade:** Média
**Tipo ENADE:** Lacunas (afirmativa incompleta)

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
Uma equipe de engenharia de dados de uma corretora de valores precisa ordenar diariamente milhões de registros de operações para fins de auditoria regulatória. O algoritmo escolhido foi o Merge Sort, que divide o vetor em duas metades, ordena cada metade recursivamente e intercala os resultados em tempo linear. Antes de assumir compromissos de prazo com o órgão regulador, o líder técnico exige que a complexidade seja demonstrada formalmente pela equação de recorrência, recusando-se a confiar na estimativa intuitiva de que "dividir o problema ao meio sempre gera tempo logarítmico".

**DADOS DE SUPORTE**
De acordo com Cormen et al. (2012), algoritmos de divisão e conquista são modelados por equações de recorrência do tipo *T*(*n*) = *aT*(*n*/*b*) + *f*(*n*), em que *a* ≥ 1 é o número de subproblemas recursivos, *b* > 1 é o fator de divisão e *f*(*n*) é o custo de dividir e combinar os resultados. O Teorema Mestre compara *f*(*n*) com a função de fronteira *n*^(log_b a):
- **Caso 1 (recursão domina):** se *f*(*n*) = *O*(*n*^(log_b a − ε)) para algum ε > 0, então *T*(*n*) = Θ(*n*^(log_b a)); a complexidade é governada pelas folhas da árvore de chamadas.
- **Caso 2 (equilíbrio):** se *f*(*n*) = Θ(*n*^(log_b a)), então *T*(*n*) = Θ(*n*^(log_b a) · log *n*); o custo logarítmico é incorporado.
- **Caso 3 (combinação domina):** se *f*(*n*) = Ω(*n*^(log_b a + ε)) para algum ε > 0 e *a* · *f*(*n*/*b*) ≤ *c* · *f*(*n*) para alguma constante *c* < 1, então *T*(*n*) = Θ(*f*(*n*)).

A recorrência do Merge Sort é *T*(*n*) = 2*T*(*n*/2) + Θ(*n*).

**COMANDO DA QUESTÃO**
Assinale a alternativa que preenche corretamente as lacunas do texto a seguir:

"A recorrência do Merge Sort enquadra-se no Caso ____ do Teorema Mestre, pois o custo de combinação *f*(*n*) = Θ(*n*) ____ função de fronteira *n*^(log_b a) = ____; portanto, a complexidade de tempo do algoritmo é ____."

**Alternativas:**
- **A)** 2 — é assintoticamente equivalente à — *n* — Θ(*n*).
- **B)** 1 — é polinomialmente menor que a — *n*² — Θ(*n*²).
- **C)** 3 — é polinomialmente maior que a — log *n* — Θ(*n*).
- **D)** 2 — é assintoticamente equivalente à — *n* — Θ(*n* log *n*).

**Gabarito: D**

**Cálculo:** *a* = 2, *b* = 2, então *n*^(log₂ 2) = *n*¹ = *n*. Como *f*(*n*) = Θ(*n*) = Θ(*n*^(log_b a)), cai no **Caso 2**: *T*(*n*) = Θ(*n* · log *n*). Conferi em python3 com *T*(1) = 1 e *f*(*n*) = *n*: *T*(*n*)/(*n* log₂ *n*) tende a 1 (1,033 para *n* = 2³⁰).

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — O caso e a fronteira estão certos, mas esquece o fator log *n*. É exatamente o que o slide p. 11 alerta: no equilíbrio, "o custo logarítmico é incorporado".
- **B) ❌** — Usa a fronteira *n*² da Estratégia Alfa (4*T*(*n*/2) + Θ(*n*), Q5), como se *a* fosse 4. Com *a* = 2, a fronteira é *n*.
- **C) ❌** — Confunde o expoente log_b *a* com "log *n*" e aplica o Caso 3 sem verificar a regularidade. Θ(*n*) seria também uma estimativa superficial: ignora os log₂ *n* níveis da árvore de recursão, cada um com custo Θ(*n*).
- **D) ✅** — Caso 2, fronteira *n* e resultado Θ(*n* log *n*).

**Base no material:** manual p. 10, §6.1 (forma *T*(*n*) = *aT*(*n*/*b*) + *f*(*n*) e os três casos com ε e regularidade). Manual p. 12, §7.1 e §7.3 (Merge Sort como divisão e conquista ótima, Θ(*n* log *n*)). Slide p. 11 (descrição dos três casos).
**Conceito-chave para a prova:** 2*T*(*n*/2) + *n* dá Θ(*n* log *n*) (Caso 2, Merge Sort). *T*(*n*/2) + 1 dá Θ(log *n*) (Caso 2, busca binária). 4*T*(*n*/2) + *n* dá Θ(*n*²) (Caso 1). 2*T*(*n*/2) + *n*² dá Θ(*n*²) (Caso 3). O primeiro passo é sempre calcular *n*^(log_b a).

---

## I7 — Paradigmas de projeto de algoritmos (associação)
**Subtópico coberto:** Paradigmas clássicos de projeto: força bruta, divisão e conquista, método guloso e programação dinâmica (manual §7.1, p. 12)
**Por que é provável:** É uma seção inteira do capítulo 7 do manual sem nenhuma questão. Não aparece nos slides-resumo, por isso a prioridade é menor que a dos subtópicos com slide.
**Prioridade:** Média
**Tipo ENADE:** Associação

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
Uma startup de logística urbana está projetando a plataforma de software que gerencia sua frota de entregas. O arquiteto de soluções identificou quatro módulos com problemas computacionais de naturezas distintas e precisa selecionar, para cada um, o paradigma de projeto de algoritmos mais adequado, com base no comportamento de tempo de execução e no consumo de memória adicional, evitando soluções redundantes ou escolhas intuitivas sem fundamentação analítica.

**DADOS DE SUPORTE**
De acordo com Cormen et al. (2012), projetar algoritmos eficientes exige selecionar o paradigma correto com base no comportamento de tempo de execução e no consumo de memória adicional. São paradigmas clássicos de projeto: a força bruta, a divisão e conquista, o método guloso e a programação dinâmica.

Relacione os paradigmas da Coluna 1 aos módulos descritos na Coluna 2.

| Coluna 1 | Coluna 2 |
|---|---|
| 1. Força bruta | ( ) **Módulo de roteamento:** calcula caminhos mínimos entre centros de distribuição escolhendo, a cada passo, o vértice de menor distância provisória, sem jamais rever as escolhas já feitas, como no algoritmo de Dijkstra. |
| 2. Divisão e conquista | ( ) **Módulo de tarifação:** o cálculo do custo ótimo recorre repetidamente aos mesmos subproblemas (subproblemas sobrepostos com subestrutura ótima); cada subproblema é resolvido uma única vez e seu resultado é armazenado em tabela para consulta direta. |
| 3. Método guloso | ( ) **Módulo de auditoria de configurações:** testa exaustivamente todas as combinações viáveis de parâmetros de um roteador legado, o que é robusto, mas pode gerar custo exponencial. |
| 4. Programação dinâmica | ( ) **Módulo de consulta de pedidos:** localiza pedidos em um vetor ordenado por busca binária e reordena os lotes diários com Merge Sort, dividindo o problema recursivamente em subproblemas independentes e combinando os resultados. |

**COMANDO DA QUESTÃO**
Assinale a alternativa que apresenta a sequência correta da Coluna 2, de cima para baixo:

**Alternativas:**
- **A)** 4 – 3 – 1 – 2.
- **B)** 3 – 1 – 4 – 2.
- **C)** 3 – 4 – 1 – 2.
- **D)** 2 – 4 – 1 – 3.

**Gabarito: C**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Troca o guloso pela programação dinâmica. Dijkstra faz escolhas locais definitivas (guloso, como diz o manual), e a tabela de subproblemas sobrepostos é marca da PD.
- **B) ❌** — Troca a PD pela força bruta. Guardar resultados de subproblemas não é "testar todas as soluções". É justamente o que **evita** o recálculo exaustivo.
- **C) ✅** — Roteamento/Dijkstra é guloso (3). Tarifação com tabelamento ou memorização é PD (4). Teste exaustivo é força bruta (1). Busca binária e Merge Sort são divisão e conquista (2).
- **D) ❌** — Atribui Dijkstra à divisão e conquista e a busca binária/Merge Sort ao método guloso. Os subproblemas da divisão e conquista são **independentes**, e o guloso não divide o problema recursivamente.

**Base no material:** manual p. 12, §7.1. Força bruta "testa todas as soluções viáveis… complexidades… exponenciais catastróficas". Divisão e conquista: "subproblemas independentes… busca binária… Merge Sort". Guloso: "escolhas locais… sem retornar atrás… exige prova rigorosa… (ex.: algoritmo de Dijkstra)". PD: "subproblemas sobrepostos e subestrutura ótima… armazena os resultados (tabelamento ou memorização)".
**Conceito-chave para a prova:** Subproblemas **independentes** indicam divisão e conquista. Subproblemas **sobrepostos** com subestrutura ótima indicam programação dinâmica (memorização). Escolha local sem retrocesso, que exige prova de otimalidade, é o método guloso (Dijkstra). Testar tudo é força bruta, frequentemente exponencial.

---

## I8 — Escolha do algoritmo de ordenação sob restrição de memória
**Subtópico coberto:** Análise comparativa de algoritmos de ordenação, Tabela 3, e trade-offs entre Merge, Quick e Heapsort (manual §7.2–7.3, p. 12; slide "Trade-offs em Algoritmos de Ordenação", p. 13)
**Por que é provável:** O slide p. 13 é inteiro uma tabela de trade-offs, e o manual dedica uma tabela e uma seção de três parágrafos ao tema. A Q6 toca o assunto só lateralmente, dentro do problema do top-k.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única (análise de trade-off)

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
Uma fabricante de equipamentos médicos desenvolve o firmware de um monitor cardíaco que precisa ordenar, a cada ciclo, um vetor com *n* leituras de sinais vitais para calcular medianas e percentis. O microcontrolador possui memória RAM extremamente restrita, e as normas de certificação exigem um limite de tempo garantido para qualquer entrada, inclusive vetores que já chegam ordenados ou em ordem inversa. A estabilidade da ordenação não é necessária, pois as leituras são valores numéricos simples. A equipe precisa escolher o algoritmo com base em uma análise rigorosa de trade-offs, e não na fama de "algoritmo mais rápido na prática".

**DADOS DE SUPORTE**
De acordo com Cormen et al. (2012), decidir qual método de ordenação de vetores de tamanho *n* deve ser acoplado a um sistema de alta performance requer comparar analiticamente seus limites de tempo no melhor caso, no caso médio e no pior caso, o consumo de memória auxiliar e a estabilidade, uma vez que nenhum dos algoritmos clássicos é superior em todos os critérios simultaneamente.

**COMANDO DA QUESTÃO**
Considerando os requisitos de projeto do firmware e os custos assintóticos dos algoritmos clássicos de ordenação, assinale a alternativa que indica o algoritmo mais adequado e a justificativa correta:

**Alternativas:**
- **A)** Merge Sort, pois garante tempo Θ(*n* log *n*) em todos os casos e é estável, além de operar com memória auxiliar constante Θ(1), o que o torna ideal para o microcontrolador.
- **B)** Quicksort, pois é o algoritmo mais rápido na prática no caso médio e, por operar sobre o próprio vetor, garante tempo Θ(*n* log *n*) no pior caso, inclusive para vetores pré-ordenados.
- **C)** Insertion Sort, pois opera in-place e é estável, com tempo Θ(*n*) no melhor caso, o que assegura o limite de tempo certificado para qualquer entrada.
- **D)** Heapsort, pois garante tempo Θ(*n* log *n*) no pior, no melhor e no caso médio, com memória auxiliar Θ(1), embora seja instável e apresente pior localidade de cache que o Quicksort.

**Gabarito: D**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Merge Sort garante Θ(*n* log *n*) e é estável, mas a intercalação exige vetor auxiliar de memória **Θ(*n*)**. O manual diz que isso o inviabiliza "sob restrições físicas severas de hardware" (p. 12).
- **B) ❌** — No pior caso, com vetor pré-ordenado e pivô no menor ou maior elemento, o Quicksort degrada para **Θ(*n*²)** e pode usar Θ(*n*) de pilha. Ser "mais rápido na prática" não é garantia certificável.
- **C) ❌** — Θ(*n*) é só o **melhor** caso (vetor já ordenado). Com vetor em ordem inversa, que o enunciado inclui, o Insertion Sort é Θ(*n*²). Usar o melhor caso como garantia é o erro conceitual explorado.
- **D) ✅** — O Heapsort é o único que reúne pior caso Θ(*n* log *n*) garantido e memória auxiliar Θ(1). As ressalvas citadas (instabilidade e cache) estão no manual e não violam os requisitos, porque a estabilidade é dispensável.

**Base no material:** manual p. 12, Tabela 3. Insertion: Θ(*n*)/Θ(*n*²)/Θ(*n*²), Θ(1), estável. Merge: Θ(*n* log *n*) sempre, Θ(*n*), estável. Quick: Θ(*n* log *n*)/Θ(*n* log *n*)/Θ(*n*²), Θ(log *n*) de pilha, instável. Heap: Θ(*n* log *n*) sempre, Θ(1), instável. §7.3, trade-offs (Merge "inviabilizando-o sob restrições físicas severas de hardware"; Heapsort "pior localidade de referência na cache"). Slide p. 13 (mesma comparação, sem o Insertion Sort).
**Conceito-chave para a prova:** Com pouca memória e garantia de pior caso, escolha o Heapsort. Se precisar de estabilidade e garantia, o Merge Sort, pagando Θ(*n*) de memória. Para o caso médio mais rápido, o Quicksort, com risco de Θ(*n*²). Para vetor quase ordenado, o Insertion Sort, Θ(*n*) no melhor caso.

---

## I9 — Pior caso do Quicksort (asserção-razão)
**Subtópico coberto:** Trade-offs do Quicksort: pior caso com vetor pré-ordenado e pivô extremo (manual §7.3, p. 12; slide p. 13, "Quicksort: Θ(n²) Pior Caso")
**Por que é provável:** Na tabela do slide p. 13, o "Θ(n²) Pior Caso" do Quicksort é a única célula das colunas de **tempo** destacada em vermelho, e o manual descreve a causa exata (vetores pré-ordenados com pivô no menor ou maior elemento). O squad já usou asserção-razão (Q1).
**Prioridade:** Alta
**Tipo ENADE:** Asserção-razão (mesmo formato da Q1)

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
Um sistema de gestão hospitalar recebe, a cada madrugada, lotes de *n* prontuários exportados de um sistema legado. Na maior parte das noites, esses lotes já chegam ordenados pelo código do paciente, mas o sistema precisa garantir a ordenação antes da carga no banco de dados. Para isso, a equipe utilizou uma implementação didática do Quicksort que escolhe sempre o primeiro elemento do subvetor como pivô. Após a implantação, o processamento noturno passou a violar a janela de manutenção, e a equipe decidiu investigar a causa com rigor analítico, recusando-se a atribuir a lentidão a "instabilidades do servidor".

**DADOS DE SUPORTE**
De acordo com Cormen et al. (2012), o Quicksort é o algoritmo mais rápido na prática, em termos de fatores constantes, no caso médio, com tempo Θ(*n* log *n*). Contudo, seu desempenho depende do equilíbrio das partições produzidas pela escolha do pivô.

Considere as duas asserções a seguir e a relação proposta entre elas:

**I.** Nos lotes que já chegam ordenados, a implementação adotada executa em tempo de ordem Θ(*n*²), e não Θ(*n* log *n*),

**PORQUE**

**II.** com o vetor pré-ordenado e o pivô sempre igual ao menor elemento do subvetor, cada partição separa apenas o pivô do restante dos elementos, de modo que o algoritmo realiza (*n* − 1) + (*n* − 2) + … + 1 = *n*(*n* − 1)/2 comparações, além de empilhar até Θ(*n*) chamadas recursivas.

**COMANDO DA QUESTÃO**
A respeito dessas asserções, assinale a opção correta:

**Alternativas:**
- **A)** As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
- **B)** As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
- **C)** A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
- **D)** As asserções I e II são proposições falsas.

**Gabarito: A**

**Julgamento:**
- **I — Verdadeira.** É o pior caso descrito no manual: "vetores pré-ordenados onde o menor ou maior elemento é escolhido como pivô… elevando o tempo para a ordem quadrática Θ(*n*²)".
- **II — Verdadeira.** Com pivô mínimo, a partição de um subvetor de tamanho *k* faz *k* − 1 comparações e gera um lado vazio e outro com *k* − 1 elementos. O total é a soma aritmética *n*(*n*−1)/2. Simulei em python3 com pivô no 1º elemento e vetor ordenado: 4.950 comparações para *n* = 100 e 499.500 para *n* = 1.000, exatamente *n*(*n*−1)/2. Numa implementação didática, que recursa nos dois lados, a profundidade da recursão chega a *n*, o que dá Θ(*n*) de pilha (manual: "consumir Θ(*n*) de memória na pilha de chamadas se não for adequadamente optimizado").
- **Relação:** A II explica **por que** a I acontece (partições totalmente desbalanceadas geram uma soma aritmética quadrática). Logo, justifica a I.

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — As duas são verdadeiras e a II é a causa da I.
- **B) ❌** — Haveria "não justificativa" se a II trouxesse um fato verdadeiro sem relação causal (ex.: "o Quicksort é instável"). Aqui a relação é direta.
- **C) ❌** — A contagem da II está correta, conforme a simulação.
- **D) ❌** — O pior caso Θ(*n*²) está no manual (p. 12) e no slide p. 13.

**Base no material:** manual p. 12, Tabela 3 (Quicksort, pior caso Θ(*n*²), pilha Θ(log *n*)) e §7.3 (causa do pior caso e Θ(*n*) de pilha sem otimização). Slide p. 13 ("Θ(n²) Pior Caso", "Excelente" no caso médio). A soma (*n*−1) + … + 1 usa a mesma soma de Gauss do §5.1 (p. 9).
**Conceito-chave para a prova:** O Quicksort é Θ(*n* log *n*) no caso médio e Θ(*n*²) no pior caso, que ocorre quando as partições ficam desbalanceadas (vetor ordenado com pivô extremo). A pilha usa Θ(log *n*) com otimização e Θ(*n*) sem ela. ⚠️ O slide p. 13 diz que a memória do Quicksort é "Θ(1) In-place", mas o manual corrige para pilha Θ(log *n*) a Θ(*n*).

---

## I10 — Degeneração da ABP (asserção-razão)
**Subtópico coberto:** ABP, custo de operação e degeneração sem balanceamento (manual §8.1, p. 13; slide "Estruturas de Dados Avançadas", p. 14, cartão "Árvore Binária de Pesquisa")
**Por que é provável:** Dos três cartões do slide p. 14, o hash e o Min-Heap são cobrados na Q6. Só a ABP ficou sem questão. A frase do slide ("Se degenerar em inserção sequencial sem balanceamento, as buscas decaem para complexidade linear Θ(n)") tem o formato típico de asserção.
**Prioridade:** Alta
**Tipo ENADE:** Asserção-razão

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
Um sistema de controle acadêmico armazena as matrículas dos alunos em uma Árvore Binária de Pesquisa (ABP) sem mecanismo de balanceamento automático. Na migração de dados do semestre, as *n* matrículas foram inseridas em ordem crescente, exatamente como estavam no arquivo exportado pelo sistema anterior. Desde então, as consultas ao histórico tornaram-se lentas nos horários de pico. O analista responsável precisa explicar o fenômeno com fundamentação analítica, e não por meio de estimativas superficiais.

**DADOS DE SUPORTE**
De acordo com Cormen et al. (2012), uma ABP organiza os dados de suporte de forma hierárquica recursiva: as chaves da subárvore esquerda são estritamente menores que a raiz, e as da subárvore direita são maiores ou iguais à raiz. As operações de inserção, busca e remoção têm custo proporcional à altura da árvore, e árvores com balanceamento automático, como AVL ou Red-Black, mantêm essa altura logarítmica.

Considere as duas asserções a seguir e a relação proposta entre elas:

**I.** Na ABP do sistema acadêmico, as buscas degradaram do tempo médio Θ(log *n*) para o tempo de pior caso Θ(*n*), idêntico ao de uma lista encadeada,

**PORQUE**

**II.** em uma ABP, o percurso em-ordem (subárvore esquerda, raiz, subárvore direita) processa obrigatoriamente as chaves em ordem crescente.

**COMANDO DA QUESTÃO**
A respeito dessas asserções, assinale a opção correta:

**Alternativas:**
- **A)** As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
- **B)** As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
- **C)** A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
- **D)** As asserções I e II são proposições falsas.

**Gabarito: B**

**Julgamento:**
- **I — Verdadeira.** Com inserção em ordem crescente, cada nova chave é maior que todas as anteriores e vira sempre filho direito do último nó. A árvore degenera numa "linha" de altura *n*. Simulei em python3 a inserção de 1 a 1.000: altura 1.000. A busca passa a Θ(*n*), "idêntico ao de uma lista encadeada" (manual p. 13).
- **II — Verdadeira.** É a propriedade do percurso em-ordem citada no manual (p. 13).
- **Relação:** A II é verdadeira, mas **não explica** a I. A causa da degradação é a altura linear criada pela ordem de inserção sem balanceamento. O percurso em-ordem não interfere na forma da árvore nem no custo da busca.

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Atrai quem associa "ordem crescente" (palavra presente nas duas asserções) a uma relação causal. A justificativa correta seria "a inserção sequencial sem balanceamento gera uma árvore degenerada de altura linear".
- **B) ✅** — As duas são verdadeiras e independentes.
- **C) ❌** — A II é verdadeira, porque em-ordem numa ABP sempre produz as chaves ordenadas.
- **D) ❌** — A I é exatamente o pior caso descrito no manual e no slide p. 14.

**Base no material:** manual p. 13, §8.1 ("na ausência de mecanismos de balanceamento automático (como em árvores AVL ou Red-Black), a inserção sequencial de dados em ordem linear… gera uma árvore degenerada… as operações de busca degradam para o tempo linear Θ(*n*), idêntico ao de uma lista encadeada"; "o percurso em-ordem processa obrigatoriamente as chaves em ordem crescente"). Slide p. 14 (cartão da ABP).
**Conceito-chave para a prova:** Na ABP, o custo médio é Θ(log *n*). Inserir em ordem crescente ou decrescente sem balanceamento gera altura *n* e custo Θ(*n*), e AVL ou Red-Black evitam isso. Na asserção-razão, duas verdades sobre o mesmo assunto não implicam justificativa: procure a **causa**.

---

## I11 — Percursos em ABP: serialização e liberação
**Subtópico coberto:** Tipos de percurso em ABP: pré-ordem (clonagem/serialização), em-ordem (ordem crescente) e pós-ordem (liberação de memória) (manual §8.1, p. 13; figura da ABP no slide p. 14)
**Por que é provável:** O manual lista os três percursos com o uso prático de cada um, e o slide p. 14 traz uma ABP concreta (40; 30, 50; 25, 35, 45, 60) que pode servir de dado de suporte.
**Prioridade:** Média
**Tipo ENADE:** Resposta única (aplicação)

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
Um serviço de catálogo de um varejista mantém em memória uma ABP de códigos de produtos. Antes de uma atualização do servidor, a equipe precisa executar duas tarefas sobre a árvore: (1) serializá-la em arquivo, de modo que, ao reinserir os códigos na mesma ordem em que foram gravados, a estrutura original seja reconstruída de forma idêntica (clonagem); e (2) em seguida, liberar fisicamente todos os nós da memória, garantindo que nenhum nó seja destruído antes de seus filhos. O engenheiro deve escolher o percurso adequado a cada tarefa com rigor analítico, sem recorrer a escolhas intuitivas.

**DADOS DE SUPORTE**
De acordo com Cormen et al. (2012), há três percursos clássicos em profundidade de uma árvore binária: pré-ordem (raiz, subárvore esquerda, subárvore direita), em-ordem (subárvore esquerda, raiz, subárvore direita) e pós-ordem (subárvore esquerda, subárvore direita, raiz).

Considere a ABP a seguir:

[Figura: ABP com raiz **40**. Filho esquerdo **30**, com filho esquerdo **25** e filho direito **35**. Filho direito **50**, com filho esquerdo **45** e filho direito **60**. É a mesma árvore da figura "Binary Search Tree" do slide p. 14.]

```
            40
          /    \
        30      50
       /  \    /  \
     25   35  45   60
```

**COMANDO DA QUESTÃO**
Assinale a alternativa que indica o percurso adequado a cada tarefa e a sequência de visita correspondente:

**Alternativas:**
- **A)** Serialização: em-ordem (25, 30, 35, 40, 45, 50, 60); liberação: pré-ordem (40, 30, 25, 35, 50, 45, 60).
- **B)** Serialização: pós-ordem (25, 35, 30, 45, 60, 50, 40); liberação: pré-ordem (40, 30, 25, 35, 50, 45, 60).
- **C)** Serialização: pré-ordem (40, 30, 25, 35, 50, 45, 60); liberação: pós-ordem (25, 35, 30, 45, 60, 50, 40).
- **D)** Serialização: pré-ordem (40, 30, 50, 25, 35, 45, 60); liberação: pós-ordem (25, 35, 45, 60, 30, 50, 40).

**Gabarito: C**

**Percursos (conferidos em python3):** pré-ordem 40, 30, 25, 35, 50, 45, 60. Em-ordem 25, 30, 35, 40, 45, 50, 60. Pós-ordem 25, 35, 30, 45, 60, 50, 40.

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Reinserir na ordem em-ordem, que é crescente, produz justamente a **ABP degenerada** de altura 7 (ver I10), e não a árvore original. Liberar em pré-ordem destrói a raiz antes dos filhos e perde os ponteiros para as subárvores.
- **B) ❌** — Reinserir em pós-ordem começa pelo 25, que vira a raiz, e reconstrói outra árvore. Liberar em pré-ordem tem o mesmo problema da A.
- **C) ✅** — A pré-ordem grava cada raiz antes de suas subárvores, então a reinserção na mesma ordem recria a forma original (é o percurso "útil para clonagem e serialização"). A pós-ordem visita os filhos antes do pai (é "essencial para liberação e destruição física de nós"). As duas sequências estão corretas.
- **D) ❌** — Os nomes dos percursos estão certos, mas as sequências não: 40, 30, 50, 25, 35, 45, 60 é o percurso **por níveis** (largura), não a pré-ordem, e 25, 35, 45, 60, 30, 50, 40 também não é a pós-ordem. O comando pede a sequência correspondente ao percurso indicado.

**Base no material:** manual p. 13, §8.1, "Tipos de Percurso": pré-ordem "útil para clonagem e serialização da árvore", em-ordem "processa obrigatoriamente as chaves em ordem crescente" e pós-ordem "essencial para liberação e destruição física de nós na memória". Slide p. 14 (figura da ABP).
**Conceito-chave para a prova:** Pré-ordem = raiz primeiro, para clonar ou serializar. Em-ordem = raiz no meio, dá as chaves ordenadas. Pós-ordem = raiz por último, para liberar memória. Nesta árvore: pré 40-30-25-35-50-45-60, em 25-30-35-40-45-50-60, pós 25-35-30-45-60-50-40.

---

## I12 — Tabelas hash: colisões e fator de carga (V/F)
**Subtópico coberto:** Tabelas de dispersão: função de espalhamento, fator de carga α = n/m, encadeamento × endereçamento aberto (manual §8.2, p. 13; slide p. 14, cartão "Tabelas de Dispersão (Hash)")
**Por que é provável:** O manual descreve as duas estratégias de resolução de colisões, com as sondagens linear, quadrática e duplo hashing, e o fator de carga. A Q6 só usa o pior caso do encadeamento (alternativa D).
**Prioridade:** Média
**Tipo ENADE:** Alternativas constantes (julgamento V/F)

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
Uma plataforma de streaming utiliza uma tabela de dispersão (hash) para manter as sessões ativas de usuários, mapeando o identificador de cada sessão para um índice de um vetor de *m* posições. Durante a transmissão ao vivo de um grande evento esportivo, o número de sessões *n* cresceu muito acima do previsto, e a equipe de confiabilidade observou picos de latência nas consultas. Para decidir entre manter a resolução de colisões por encadeamento ou migrar para endereçamento aberto, o engenheiro precisa avaliar com rigor analítico os custos de cada estratégia, recusando-se a aceitar a intuição vaga de que "hash é sempre O(1)".

**DADOS DE SUPORTE**
De acordo com Cormen et al. (2012), tabelas hash realizam o mapeamento de chaves de tamanho arbitrário para índices de um vetor de tamanho finito *m* por meio de uma função de espalhamento *h*(*k*), e o fator de carga α = *n*/*m* mede a ocupação média da tabela. Quando duas ou mais chaves resultam no mesmo índice, ocorre uma colisão, que pode ser resolvida por encadeamento (*chaining*) ou por endereçamento aberto (*open addressing*).

Julgue as afirmativas a seguir como verdadeiras (V) ou falsas (F):

( ) Com uma função de espalhamento uniforme e um fator de carga α = *n*/*m* estável, as operações de busca e inserção têm custo médio constante Θ(1).

( ) No encadeamento, os elementos colididos permanecem no próprio vetor da tabela, e novos índices livres são procurados sistematicamente por sondagem linear, sondagem quadrática ou duplo hashing.

( ) No encadeamento, se todas as *n* chaves colidirem no mesmo índice, a tabela degenera em uma lista encadeada linear e a busca passa a custar Θ(*n*) no pior caso.

( ) No endereçamento aberto, por não haver listas externas, as colisões nunca degradam o tempo de inserção, que permanece Θ(1) mesmo no pior caso de sobrecarga da tabela.

**COMANDO DA QUESTÃO**
Assinale a alternativa que apresenta a sequência correta, de cima para baixo:

**Alternativas:**
- **A)** V – F – V – F.
- **B)** V – V – V – F.
- **C)** F – F – V – V.
- **D)** V – F – F – F.

**Gabarito: A**

**Julgamento:**
- **1ª — V.** "Sob condições médias e um bom fator de carga α = *n*/*m*, a complexidade de busca e inserção é constante de classe Θ(1)" (manual p. 13).
- **2ª — F.** Essa é a descrição do **endereçamento aberto**. No encadeamento, os colididos ficam em listas encadeadas **externas** associadas a cada índice.
- **3ª — V.** É o pior caso do encadeamento (manual p. 8 e p. 13; slide p. 14, "encadeamento saturado").
- **4ª — F.** No endereçamento aberto, a colisão "degrada o tempo de inserção para pior caso de classe Θ(*n*)" (manual p. 13), porque a sondagem pode percorrer quase toda a tabela.

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — V – F – V – F.
- **B) ❌** — Marca a 2ª como V, trocando encadeamento por endereçamento aberto.
- **C) ❌** — Nega o Θ(1) médio (1ª) e aceita a ideia de que o endereçamento aberto é imune a colisões (4ª).
- **D) ❌** — Nega o pior caso Θ(*n*) do encadeamento (3ª), repetindo a intuição de que "hash é sempre O(1)".

**Base no material:** manual p. 13, §8.2 (função *h*(*k*), α = *n*/*m*, encadeamento com listas externas e pior caso Θ(*n*), endereçamento aberto com sondagem linear, quadrática ou duplo hashing e pior caso Θ(*n*)). Manual p. 8 (quadro sobre a degradação). Slide p. 14 (cartão do hash).
**Conceito-chave para a prova:** Hash tem custo **médio** Θ(1), com boa função e α controlado, e **pior caso** Θ(*n*) nas duas estratégias. Encadeamento usa listas fora do vetor. Endereçamento aberto procura outra posição dentro do vetor (sondagem linear, quadrática ou duplo hashing).
