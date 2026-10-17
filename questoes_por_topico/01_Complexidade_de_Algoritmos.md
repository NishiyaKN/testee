# Complexidade de Algoritmos — Questões e Gabarito Comentado

**Squad responsável:** Squad 11
**Materiais analisados:**
| Arquivo | Páginas | Tipo | Questões encontradas (páginas) |
|---|---|---|---|
| `Resumo_ Complexidade de algoritmos (1).pdf` | 16 | Slides-resumo do Squad 11: 6 slides de conteúdo, cada um seguido de um slide "Questão N". As páginas de questão são **imagens** (sem texto extraível) e foram lidas renderizadas em 130–300 dpi | **Q1–Q6** (p. 4, 6, 8, 10, 12, 15). **Sem gabarito.** Conferi as 16 páginas: nenhuma traz resposta, "gabarito", alternativa marcada ou resolução. A p. 16 é só "Obrigado pela atenção!" |
| `Manual - Complexidade de Algoritmos.pdf` | 15 | Manual de referência / apostila do Squad 11 (só texto, lido por inteiro) | **Nenhuma questão.** Traz os estudos de caso já resolvidos dos quais as 6 questões dos slides foram tiradas (p. 4, 4–5, 6–7, 9, 10–11, 14) |
| `Estrutura de Questões sob o padrão do ENADE.pdf` (documento do professor, não é do Squad 11) | 31 | Slides do professor sobre o padrão ENADE | 1 questão-exemplo de "Estrutura de Dados e Complexidade de Algoritmos" (p. 9), aqui chamada QP1 |

**Resumo:** São **7 questões**. **6 são do Squad 11** (slides, p. 4–15), e **nenhuma delas tem gabarito no material**, então resolvi todas aqui: Q1 **D**, Q2 **D**, Q3 **A**, Q4 **A**, Q5 **A**, Q6 **C**. A 7ª é a **questão-exemplo do professor** (QP1), com gabarito dado pelo próprio documento (**C**).
Total: 1 questão com gabarito no material (QP1) e 6 sem gabarito (resolvidas aqui).

As 6 questões do squad seguem um padrão fixo: SITUAÇÃO-PROBLEMA, DADOS DE SUPORTE (sempre citando "Cormen et al. (2012)"), COMANDO DA QUESTÃO e ALTERNATIVAS DE RESPOSTA, **sempre com só 4 alternativas (A–D)**. Os enunciados usam com frequência expressões como "Modelo de Knuth", "recusando-se a confiar em intuições vagas ou estimativas superficiais", "dados de suporte", "SLA" e "alta performance". Cada questão é a versão em padrão ENADE de um estudo de caso resolvido do manual, e o desenvolvimento do manual confirma os gabaritos deste arquivo:

| Questão | Slide de conteúdo anterior | Base no manual |
|---|---|---|
| Q1 | p. 2–3 (Taxa de crescimento; Ordens assintóticas) | §2.1–2.2, p. 4–5 (prova de que n² = O(n log₂ n) é falsa) |
| Q2 | p. 5 (Modelo de Contagem de Knuth) | §3.2, p. 6–7 (busca com sentinela, pior e melhor caso) |
| Q3 | p. 7 (Variação de Comportamento Dinâmico) | Estudo de caso da p. 4 (ordenação de 5 algoritmos) |
| Q4 | p. 9 (Modelagem de Laços Iterativos) | §5.2, p. 9 (laço com PG decrescente = 2n − 1) |
| Q5 | p. 11 (Recursão e Teorema Mestre) | §6.2, p. 10–11 (Estratégias Alfa e Beta) |
| Q6 | p. 13–14 (Trade-offs de ordenação; Estruturas de dados avançadas) | §7.3, §8.2 e estudo de caso da p. 14 (Min-Heap para top-k) |

> Legenda: ✅ correta · ❌ incorreta · ⚠️ ponto de atenção (gabarito do material duvidoso, ambiguidade, versão divergente)

## Índice
1. [Q1 — Big-O e prova de dominância (asserção-razão)](#q1--big-o-e-prova-de-dominância-asserção-razão)
2. [Q2 — Modelo de Knuth: busca sequencial com sentinela](#q2--modelo-de-knuth-busca-sequencial-com-sentinela)
3. [Q3 — Ordenação de cinco funções de custo](#q3--ordenação-de-cinco-funções-de-custo)
4. [Q4 — Laço com redução geométrica (PG)](#q4--laço-com-redução-geométrica-pg)
5. [Q5 — Teorema Mestre: estratégias Alfa e Beta](#q5--teorema-mestre-estratégias-alfa-e-beta)
6. [Q6 — Top-k em fluxo de dados (afirmativa INCORRETA)](#q6--top-k-em-fluxo-de-dados-afirmativa-incorreta)
7. [Questão-exemplo do professor (documento Estrutura de Questões ENADE)](#questão-exemplo-do-professor-documento-estrutura-de-questões-enade)
   - [QP1 — Busca binária: pior caso em 1.048.576 usuários](#qp1--busca-binária-pior-caso-em-1048576-usuários)
8. [Pontos do manual e dos slides com maior chance de virar questão (atualizado)](#pontos-do-manual-e-dos-slides-com-maior-chance-de-virar-questão-atualizado)

---

## Q1 — Big-O e prova de dominância (asserção-razão)
**Fonte:** `Resumo_ Complexidade de algoritmos (1).pdf`, p. 4 (slide "Questão 1", imagem). Base: `Manual - Complexidade de Algoritmos.pdf`, §2.1–2.2, p. 4–5
**Tipo ENADE:** Asserção-razão

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
No projeto de algoritmos e estruturas de dados de alta performance, a compreensão das dimensões quantitativas e dos limites teóricos de complexidade é indispensável para subsidiar decisões técnicas maduras de desenvolvimento de software. Um engenheiro de software precisa projetar um algoritmo para processar grandes volumes de dados corporativos de suporte de tamanho *n*. Para isso, ele modela analiticamente dois algoritmos concorrentes e obtém duas funções de custo temporal: *f*(*n*) = *n*² e *g*(*n*) = *n* log₂ *n*. Ao avaliar a eficiência de longo prazo das soluções sob picos críticos de processamento, o engenheiro deve classificar esses algoritmos em categorias de tempo utilizando as definições formais de limites assintóticos fornecidas pela Notação Big-O.

**DADOS DE SUPORTE**
De acordo com Cormen et al. (2012), a Notação Big-O estabelece uma ferramenta analítica fundamental para classificar o crescimento relativo de funções matemáticas. Do ponto de vista conceitual, dizemos que *f*(*n*) = *O*(*g*(*n*)) se existirem constantes reais positivas *c* e *n*₀ tais que 0 ≤ *f*(*n*) ≤ *c* · *g*(*n*) para todo *n* ≥ *n*₀. Esse formalismo é essencial para que o estudante de computação abandone intuições vagas ou estimativas superficiais e busque rigor e precisão científica em suas suposições de engenharia de software.

Considere as duas asserções a seguir e a relação proposta entre elas:

**I.** A função de complexidade temporal quadrática *f*(*n*) = *n*² é limitada assintoticamente de forma superior pela classe *O*(*n* log₂ *n*), ou seja, *f*(*n*) = *O*(*n* log₂ *n*),

**PORQUE**

**II.** para valores suficientemente grandes de *n*, a função de crescimento linearítmico *g*(*n*) = *n* log₂ *n* domina de maneira estrita a função quadrática *f*(*n*) = *n*² à medida que o tamanho da entrada cresce em direção ao infinito, satisfazendo a desigualdade *n*² ≤ *c* · (*n* log₂ *n*) para alguma constante real positiva *c*.

**COMANDO DA QUESTÃO**
A respeito dessas asserções, assinale a opção correta:

**Alternativas:**
- **A)** As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
- **B)** As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
- **C)** A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
- **D)** As asserções I e II são proposições falsas.

(Como no original, são só 4 alternativas. Falta a opção padrão do ENADE "A asserção I é falsa, e a II é verdadeira".)

**Gabarito: D** — _(não consta no material — resolvido aqui; coincide com a conclusão do manual, p. 4–5: "a proposição n² = O(n log₂ n) é falsa")_

**Julgamento das asserções:**
- **Asserção I — Falsa.** Para valer *n*² = *O*(*n* log₂ *n*), seria preciso existir *c* > 0 com *n*² ≤ *c* · *n* log₂ *n*, isto é, *n* ≤ *c* · log₂ *n*, para todo *n* ≥ *n*₀. Mas lim_{n→∞} *n*² / (*n* log₂ *n*) = lim *n* / log₂ *n* = ∞, então nenhuma constante *c* funciona. Conferi com python3: a razão *n*/log₂ *n* vale 4 para *n* = 16, 102,4 para *n* = 1.024 e ≈ 52.429 para *n* = 2²⁰, e continua crescendo sem limite.
- **Asserção II — Falsa.** Ela inverte a dominância. Pela regra do manual (p. 3), *g* domina *f* quando lim *f*/*g* = 0. Aqui lim (*n* log₂ *n*)/*n*² = lim (log₂ *n*)/*n* = 0, então é ***n*² que domina *n* log₂ *n***, e não o contrário. Além disso, a desigualdade *n*² ≤ *c* · (*n* log₂ *n*) é justamente a que **não** pode ser satisfeita para *n* grande.
- **Relação:** não se aplica, porque as duas asserções são falsas.

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Atrai quem confunde "limite superior" com "função que parece mais sofisticada" e aceita a desigualdade sem testá-la. Nenhuma das duas asserções é verdadeira.
- **B) ❌** — Também exige I e II verdadeiras.
- **C) ❌** — I é falsa. Atrai quem percebe que II está errada mas aceita I por intuição. Repare que, se II fosse reescrita corretamente ("*n*² domina *n* log₂ *n*"), ela provaria que I é **falsa**, e não verdadeira.
- **D) ✅** — As duas são falsas. O limite *n*/log₂ *n* → ∞ prova que *n*² ∉ *O*(*n* log₂ *n*) (I falsa), e a mesma conta mostra que a dominância é a inversa da afirmada em II.

**⚠️ Atenção:** Se a versão da prova trocar a ordem das funções, por exemplo "I. *n* log₂ *n* = *O*(*n*²) PORQUE II. *n*² domina estritamente *n* log₂ *n*…", as duas passam a ser verdadeiras e a II justifica a I, e a resposta vira a opção "I e II verdadeiras, e a II justifica a I". Se aparecer uma 5ª alternativa ("I falsa, II verdadeira"), ela continua errada nesta versão, porque II também é falsa.

**Conceito-chave para a prova:** *f* = *O*(*g*) exige uma constante *c* tal que *f* ≤ *c*·*g* a partir de algum *n*₀. Use o limite: se lim *f*/*g* = 0 ou é uma constante finita, então *f* = *O*(*g*); se lim *f*/*g* = ∞, então *f* ≠ *O*(*g*). Portanto *n* log *n* = *O*(*n*²), mas *n*² ≠ *O*(*n* log *n*).

---

## Q2 — Modelo de Knuth: busca sequencial com sentinela
**Fonte:** `Resumo_ Complexidade de algoritmos (1).pdf`, p. 6 (slide "Questão 2", imagem). Base: `Manual - Complexidade de Algoritmos.pdf`, §3.1–3.2, p. 6–7 (código idêntico)
**Tipo ENADE:** Afirmativas múltiplas ("é correto o que se afirma em")

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
Durante o desenvolvimento de um componente de busca e recuperação de registros para um SGBD de alta performance, uma equipe de desenvolvimento deparou-se com a necessidade de prever com precisão científica o consumo de tempo de execução de uma rotina iterativa crítica sob grandes volumes de dados. Para embasar decisões técnicas de desenvolvimento e garantir a previsibilidade operacional de tempo de resposta, o engenheiro principal aplicou o Modelo de Knuth para traduzir o algoritmo em um modelo matemático de contagem detalhada de instruções críticas, recusando-se a confiar em intuições vagas ou em estimativas superficiais comuns no desenvolvimento de software.

**DADOS DE SUPORTE**
De acordo com Knuth (1997) e Cormen et al. (2012), a modelagem formal de contagem de operações consiste em associar um custo de execução unitário *c*ᵢ a cada linha de instrução *i* e identificar a frequência exata de execução *t*ᵢ de cada uma delas em função do tamanho da entrada *n*.

Considere o algoritmo clássico de busca sequencial com sentinela implementado em linguagem C, em que o vetor *v* possui *n* elementos de dados de suporte e a posição *v*[*n* − 1] está reservada para armazenar temporariamente a sentinela:

```c
int busca_sentinela(int v[], int n, int chave) {
    int i = 0;
    v[n - 1] = chave;          // Linha 1 (custo c_1)
    while (v[i] != chave) {    // Linha 2 (custo c_2)
        i++;                   // Linha 3 (custo c_3)
    }
    if (i < n - 1) {           // Linha 4 (custo c_4)
        return i;              // Linha 5 (custo c_5)
    }
    return -1;                 // Linha 6 (custo c_6)
}
```
[No slide, o código aparece numa caixa com numeração lateral de 1 a 11. A fonte da imagem deforma alguns caracteres: `{` e `}` saem parecidos com `(` e `)`, `v[n - 1]` sai como "v[n - 1)", `while` sai como "vhile" e o comentário da linha do `while` aparece como "// Linha £ (custo c_£)". Transcrevi com os caracteres corretos de C. O "£" é o "2", como confirmam a afirmativa I e o código idêntico do manual, p. 6.]

Considere os custos de tempo *c*₁ a *c*₆ associados a cada linha *i* do código, respectivamente. Analise as seguintes afirmativas sobre a contagem exata e o crescimento assintótico desse algoritmo:

**I.** No pior caso de busca (quando a chave não está originalmente no vetor *v*, exceto na sentinela), a Linha 2 (teste do loop) executa exatamente *n* vezes com custo de tempo de execução correspondente a *n* · *c*₂.

**II.** A função de complexidade de tempo de pior caso exata desse algoritmo é expressa analiticamente por *T*_pior(*n*) = *c*₁ + *n* · *c*₂ + (*n* − 1) · *c*₃ + *c*₄ + *c*₆, o que o classifica de forma correta na ordem de complexidade linear Θ(*n*).

**III.** No melhor caso de busca (quando a chave é encontrada imediatamente na primeira posição *v*), o laço `while` executa apenas uma única comparação, resultando em tempo de execução constante de classe assintótica Θ(1).

**COMANDO DA QUESTÃO**
Considerando o Modelo de Knuth para a modelagem formal de contagem de instruções, as propriedades matemáticas de progressões e somatórios, a Notação Big-O para classes de complexidade e os limites teóricos apresentados, é correto o que se afirma em:

**Alternativas:**
- **A)** I e II, apenas.
- **B)** I e III, apenas.
- **C)** II e III, apenas.
- **D)** I, II e III.

**Gabarito: D** — _(não consta no material — resolvido aqui; coincide com o manual, p. 6–7)_

**Julgamento das afirmativas** (simulei o código em python3 contando quantas vezes cada linha executa):
- **I — Verdadeira.** No pior caso, a única ocorrência da chave é a sentinela em *v*[*n* − 1]. O teste do `while` é avaliado para *i* = 0, 1, …, *n* − 1, ou seja, *n* vezes: *n* − 1 vezes dá verdadeiro e na última dá falso. Custo: *n*·*c*₂. Na simulação com *n* = 10, foram 10 testes.
- **II — Verdadeira.** No pior caso as frequências são *t*₁ = 1, *t*₂ = *n*, *t*₃ = *n* − 1 (o incremento roda uma vez a menos que o teste), *t*₄ = 1 (com *i* = *n* − 1, o teste `i < n - 1` dá falso), *t*₅ = 0 e *t*₆ = 1. A soma fica *T*_pior(*n*) = *c*₁ + *n*·*c*₂ + (*n* − 1)·*c*₃ + *c*₄ + *c*₆. O maior termo em *n* é de 1º grau, portanto Θ(*n*). A simulação deu (1, *n*, *n* − 1, 1, 0, 1) para *n* = 5, 10 e 100.
- **III — Verdadeira.** Com a chave em *v*[0], o `while` testa uma vez e já sai, o `i++` não executa, o `if` executa uma vez (0 < *n* − 1 dá verdadeiro) e o `return i` executa uma vez. Fica *T*_melhor(*n*) = *c*₁ + *c*₂ + *c*₄ + *c*₅, constante, portanto Θ(1). A simulação deu (1, 1, 0, 1, 1, 0).

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Deixa de fora a III. Atrai quem acha que toda busca sequencial é "sempre linear", esquecendo que a análise de melhor caso existe e aqui é Θ(1).
- **B) ❌** — Deixa de fora a II. Atrai quem conta o incremento (Linha 3) também *n* vezes (resultaria em *n*·*c*₃) ou quem quer incluir a Linha 5 no pior caso. A contagem correta do incremento é *n* − 1.
- **C) ❌** — Deixa de fora a I. Atrai quem erra por um: acha que o teste do laço roda *n* − 1 vezes, como o incremento, ou *n* + 1 vezes, como num `for` com teste de limite. Com sentinela, são exatamente *n* testes.
- **D) ✅** — As três afirmativas reproduzem exatamente a análise do manual (p. 6–7).

**⚠️ Atenção:**
1. A "Linha 2" das afirmativas é a numeração dos **comentários** (Linha 1 a 6), e não a numeração lateral da caixa de código (1 a 11, na qual o `while` está na linha 4). A instrução `int i = 0;` não recebe custo nem no slide nem no manual.
2. Como *v*[*n* − 1] é reservada para a sentinela, os dados reais ocupam *v*[0..*n* − 2]. Se a chave estiver em *v*[*n* − 2], o teste roda *n* − 1 vezes. O pior caso, que maximiza a contagem, é mesmo o da chave ausente.

**Conceito-chave para a prova:** No Modelo de Knuth, *T*(*n*) = Σ *c*ᵢ·*t*ᵢ (custo × frequência de cada linha). O teste de um laço executa uma vez a mais que o corpo. A sentinela elimina o teste de limite de índice (`i < n`) de dentro do laço e deixa uma única comparação por iteração. Pior caso: Θ(*n*). Melhor caso: Θ(1), com *T* = *c*₁ + *c*₂ + *c*₄ + *c*₅.

---

## Q3 — Ordenação de cinco funções de custo
**Fonte:** `Resumo_ Complexidade de algoritmos (1).pdf`, p. 8 (slide "Questão 3", imagem). Base: `Manual - Complexidade de Algoritmos.pdf`, "Estudo de Caso: Ordenação Assintótica de Algoritmos Concorrentes", p. 4 (mesmas cinco funções)
**Tipo ENADE:** Ordenação

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
No desenvolvimento de sistemas de software crítico de alto desempenho — como motores de bancos de dados relacionais e indexadores de busca *web* —, a escolha adequada de estruturas lógicas de armazenamento e processamento de dados deve ser apoiada por análises teóricas rigorosas, recusando-se a confiar em estimativas superficiais ou intuições vagas. Durante a otimização de um microsserviço de análise de dados estruturados de larga escala, um cientista da computação precisa classificar e ordenar cinco algoritmos concorrentes em termos de eficiência de pior caso. O engenheiro aplica o Modelo de Knuth para modelar analiticamente a contagem exata das instruções dominantes, obtendo cinco funções de custo de tempo de execução denominadas de *T*_I(*n*) a *T*_V(*n*).

**DADOS DE SUPORTE**
De acordo com Cormen et al. (2012), a modelagem matemática das classes de complexidade representada pela Notação Big-O permite abstrair o comportamento das funções de custo sob picos de carregamento de dados e prever formalmente os limites de tempo de execução quando o tamanho da entrada *n* cresce de forma ilimitada para o infinito.

Considere as cinco funções de contagem de operações dominantes obtidas analiticamente para as instruções críticas de cada algoritmo, operando sob uma entrada de tamanho *n* (onde *n* ≥ 2):
- **Algoritmo I:** *T*_I(*n*) = 100*n* + 15
- **Algoritmo II:** *T*_II(*n*) = log₂(*n*⁵)
- **Algoritmo III:** *T*_III(*n*) = Σ_{i=1}^{n} *i*
- **Algoritmo IV:** *T*_IV(*n*) = *n* log₂(*n*³)
- **Algoritmo V:** *T*_V(*n*) = 2ⁿ + *n*⁴

Para fins de ordenação e seleção de projeto, os algoritmos devem ser listados em **ordem crescente** da taxa de crescimento de suas funções de complexidade assintótica de tempo de pior caso, ou seja, partindo do algoritmo de **maior eficiência** (menor taxa de crescimento) para o de **menor eficiência** (maior taxa de crescimento).

**COMANDO DA QUESTÃO**
A partir da simplificação analítica de cada modelo de contagem estruturado e aplicando as definições formais de limites assintóticos da Notação Big-O, assinale a alternativa que apresenta a ordenação correta das funções de custo de tempo, do algoritmo mais eficiente ao menos eficiente:

**Alternativas:**
- **A)** II – I – IV – III – V, representando as classes de complexidade Θ(log *n*), Θ(*n*), Θ(*n* log *n*), Θ(*n*²) e Θ(2ⁿ), do mais eficiente ao menos eficiente.
- **B)** II – IV – I – III – V, representando as classes de complexidade Θ(log *n*), Θ(*n* log *n*), Θ(*n*), Θ(*n*²) e Θ(2ⁿ), do mais eficiente ao menos eficiente.
- **C)** I – II – IV – III – V, representando as classes de complexidade Θ(*n*), Θ(log *n*), Θ(*n* log *n*), Θ(*n*²) e Θ(2ⁿ), do mais eficiente ao menos eficiente.
- **D)** II – I – III – IV – V, representando as classes de complexidade Θ(log *n*), Θ(*n*), Θ(*n*²), Θ(*n* log *n*) e Θ(2ⁿ), do mais eficiente ao menos eficiente.

**Gabarito: A** — _(não consta no material — resolvido aqui; coincide com o manual, p. 4: "a ordenação de eficiência rigorosa é: II – I – IV – III – V")_

**Simplificação de cada função:**
- *T*_II = log₂(*n*⁵) = 5 log₂ *n* → **Θ(log *n*)**. O expoente dentro do log vira constante multiplicativa.
- *T*_I = 100*n* + 15 → **Θ(*n*)**. Constantes são desprezadas.
- *T*_IV = *n* log₂(*n*³) = 3*n* log₂ *n* → **Θ(*n* log *n*)**.
- *T*_III = Σ *i* = *n*(*n*+1)/2 = 0,5*n*² + 0,5*n* → **Θ(*n*²)** (soma de Gauss).
- *T*_V = 2ⁿ + *n*⁴ → **Θ(2ⁿ)**, porque lim *n*⁴/2ⁿ = 0 e a exponencial domina qualquer polinômio.

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — Segue a escala do slide p. 2 e da Tabela 1 do manual: Θ(1) < Θ(log *n*) < Θ(*n*) < Θ(*n* log *n*) < Θ(*n*²) < Θ(*n*³) < Θ(2ⁿ).
- **B) ❌** — Põe Θ(*n* log *n*) antes de Θ(*n*). Atrai quem se impressiona com o 100 de *T*_I e compara valores numéricos em vez de taxas de crescimento. Para *n* → ∞, *n* log *n* cresce mais rápido que *n*.
- **C) ❌** — Põe Θ(*n*) antes de Θ(log *n*), invertendo a base da escala. Atrai quem lê log₂(*n*⁵) como se fosse *n*⁵ ou acha que o expoente 5 torna a função "grande". Na verdade é só 5·log₂ *n*.
- **D) ❌** — Põe Θ(*n*²) antes de Θ(*n* log *n*). Atrai quem não simplifica log₂(*n*³) e lê *n* log₂(*n*³) como "*n*·*n*³" ou como "cúbica". É o mesmo erro de inversão da asserção II da Q1.

**⚠️ Atenção:** Por causa das constantes, a ordem dos **valores numéricos** em tamanhos práticos não é a ordem assintótica. Calculei em python3: 3*n* log₂ *n* (IV) só ultrapassa 100*n* + 15 (I) a partir de *n* ≈ 1,08 × 10¹⁰ (≈ 2^33,3), e *n*(*n*+1)/2 (III) só ultrapassa 100*n* + 15 a partir de *n* = 200. Para *n* = 1.000, a ordem real dos custos é II, IV, I, III, V. A questão pede a taxa de crescimento quando *n* → ∞, então a resposta continua sendo A. Uma versão alterada pode cobrar exatamente essa diferença entre "custo para *n* pequeno" e "classe assintótica".

**Conceito-chave para a prova:** Simplifique antes de comparar. log(*n*ᵏ) = *k* log *n* fica em Θ(log *n*), *n* log(*n*ᵏ) fica em Θ(*n* log *n*), Σ *i* = *n*(*n*+1)/2 fica em Θ(*n*²) e 2ⁿ + polinômio fica em Θ(2ⁿ). Constantes multiplicativas e termos de menor ordem são desprezados (regra de dominância, slide p. 2 e manual p. 3).

---

## Q4 — Laço com redução geométrica (PG)
**Fonte:** `Resumo_ Complexidade de algoritmos (1).pdf`, p. 10 (slide "Questão 4", imagem). Base: `Manual - Complexidade de Algoritmos.pdf`, §5.2, p. 9 (mesmo laço). O slide p. 9 traz a fórmula Σ_{k=0}^{log₂ n} n/2ᵏ = 2n − 1 = Θ(n)
**Tipo ENADE:** Resposta única (cálculo / análise de código)

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
Uma equipe de desenvolvimento está otimizando um algoritmo de compressão de imagens em tons de cinza para dispositivos de Internet das Coisas (IoT), que possuem restrições rígidas de consumo de energia e memória. Um dos submódulos críticos reduz sequencialmente a resolução de uma matriz de pixels de tamanho *n* (onde *n* é uma potência de 2) através de um laço de repetição aninhado. Para evitar estimativas vagas e intuitivas, os engenheiros precisam analisar matematicamente a contagem exata das instruções críticas executadas, garantindo que o tempo de resposta se mantenha dentro de limites estáveis e escaláveis para a infraestrutura do backend.

**DADOS DE SUPORTE**
De acordo com Cormen et al. (2012), a análise matemática de laços aninhados com dependências de controle exige a modelagem analítica da soma acumulada de suas iterações, expressa na forma de somatórios matemáticos ou séries geométricas decrescentes.

Considere o seguinte trecho de código-fonte estruturado em linguagem C em que *n* representa o tamanho do vetor de pixels de entrada:

```c
int processar_matriz(int n) {
    int count = 0;
    for (int i = n; i > 0; i /= 2) {
        for (int j = 0; j < i; j++) {
            count++; // Operacao critica de custo constante \Theta(1)
        }
    }
    return count;
}
```
[Como na Q2, a fonte da imagem deforma caracteres: o nome da função aparece como "processar_natriz" e as chaves `{ }` saem parecidas com `( )`. Transcrevi em C correto. O comentário `\Theta(1)` está literalmente assim no slide, como código LaTeX não renderizado.]

Considere também a fórmula da soma de uma progressão geométrica (PG) finita de razão *q* ≠ 1:

*S*ₖ = *a*₁ · (1 − *q*ᵏ) / (1 − *q*)

[No slide, o "≠" está deformado e aparece como "q/ = 1".]

**COMANDO DA QUESTÃO**
A partir da análise do fluxo lógico de repetição do algoritmo e aplicando as propriedades matemáticas de séries geométricas, assinale a alternativa que apresenta a simplificação fechada exata do número de operações críticas realizadas e sua respectiva classificação assintótica de pior caso:

**Alternativas:**
- **A)** A contagem exata é expressa por 2*n* − 1 operações críticas, estabelecendo uma classe de complexidade de tempo linear de ordem Θ(*n*).
- **B)** A contagem exata é expressa por *n* log₂ *n* operações críticas, estabelecendo uma classe de complexidade de tempo linearítmica de ordem Θ(*n* log *n*).
- **C)** A contagem exata é expressa por *n*(*n* + 1)/2 operações críticas, estabelecendo uma classe de complexidade de tempo quadrática de ordem Θ(*n*²).
- **D)** A contagem exata é expressa por 2ⁿ − 1 operações críticas, estabelecendo uma classe de complexidade de tempo exponencial de ordem Θ(2ⁿ).

**Gabarito: A** — _(não consta no material — resolvido aqui; coincide com o manual, p. 9)_

**Cálculo:** O laço externo assume os valores *i* = *n*, *n*/2, *n*/4, …, 2, 1, que são log₂ *n* + 1 valores. Para cada *i*, o laço interno executa *i* vezes. Então
*S* = *n* + *n*/2 + *n*/4 + … + 1 = Σ_{k=0}^{log₂ n} *n*/2ᵏ.
É uma PG com *a*₁ = *n*, *q* = 1/2 e log₂ *n* + 1 termos:
*S* = *n* · (1 − (1/2)^(log₂ n + 1)) / (1 − 1/2) = 2*n* · (1 − 1/(2*n*)) = **2*n* − 1** → **Θ(*n*)**.
Simulei em python3: *n* = 16 dá 31, *n* = 1.024 dá 2.047 e *n* = 2²⁰ dá 2.097.151, sempre igual a 2*n* − 1.

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — É a soma exata da PG decrescente. Apesar de os laços serem aninhados, o total é limitado por 2*n*.
- **B) ❌** — É a "intuição mecânica" de multiplicar log₂ *n* iterações externas por *n* iterações internas, como se o laço interno sempre rodasse *n* vezes. Para *n* = 1.024 isso daria 10.240 operações, contra as 2.047 reais. O manual (p. 9) cita exatamente esta armadilha: estimativas "que sugeriam tempo linearítmico".
- **C) ❌** — É a soma de Gauss do laço **triangular** (slide p. 9, caixa da esquerda; manual §5.1), que vale quando *i* cresce de 1 em 1. Aqui *i* é dividido por 2. O slide p. 9 diz que a PG "derruba a intuição quadrática".
- **D) ❌** — Confunde com a soma 1 + 2 + 4 + … + 2ⁿ⁻¹ = 2ⁿ − 1, que tem *n* termos. A PG do código tem só log₂ *n* + 1 termos. Uma contagem exponencial é impossível aqui, porque cada termo é no máximo *n*.

**⚠️ Atenção:** Os dois materiais apontam distratores diferentes: o slide (p. 9) fala em "intuição quadrática" (alternativa C) e o manual (p. 9) em estimativa "linearítmica" (alternativa B). Se *n* não for potência de 2, com divisão inteira, o total fica abaixo de 2*n* − 1 (por exemplo, *n* = 1.000 dá 1.994), mas a classe continua Θ(*n*).

**Conceito-chave para a prova:** Num laço aninhado em que o escopo interno é dividido por 2 a cada volta, o total é *n* + *n*/2 + … + 1 = 2*n* − 1, que é Θ(*n*) e não Θ(*n* log *n*). Já o laço triangular (interno de 1 até *i*) dá *n*(*n*+1)/2, que é Θ(*n*²).

---

## Q5 — Teorema Mestre: estratégias Alfa e Beta
**Fonte:** `Resumo_ Complexidade de algoritmos (1).pdf`, p. 12 (slide "Questão 5", imagem). Base: `Manual - Complexidade de Algoritmos.pdf`, §6.1–6.2, p. 10–11 (mesmas estratégias e recorrências)
**Tipo ENADE:** Resposta única (interpretação / análise)

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
Uma equipe de engenharia de software de uma empresa de geoprocessamento está desenvolvendo um sistema de renderização de mapas de alta resolução. O módulo principal processa matrizes de elevação de terreno de dimensão *n* × *n* (onde *n* é uma potência de 2). Para otimizar o tempo de renderização, dois engenheiros seniores propuseram estratégias de projeto distintas baseadas no paradigma de divisão e conquista para realizar o processamento das matrizes. A escolha da estratégia correta requer uma análise crítico-reflexiva rigorosa para antecipar possíveis cenários de gargalo temporal em ambiente de produção sob cargas de trabalho extremas.

**DADOS DE SUPORTE**
De acordo com Cormen et al. (2012), a análise de algoritmos recursivos baseados em divisão e conquista fundamenta-se na modelagem de equações de recorrência do tipo *T*(*n*) = *aT*(*n*/*b*) + *f*(*n*). A resolução analítica dessas recorrências pelo Teorema Mestre permite classificar e comparar a eficiência assintótica de diferentes abordagens.

Considere as duas estratégias de divisão e conquista propostas pela equipe de engenharia:
- **Estratégia Alfa (Algoritmo A):** Divide a matriz de dimensão *n* × *n* em 4 submatrizes quadradas de tamanho *n*/2 × *n*/2. Cada submatriz é processada recursivamente e a combinação dos resultados é feita por uma varredura linear que consome tempo de execução de ordem Θ(*n*) nas bordas das submatrizes.
- **Estratégia Beta (Algoritmo B):** Divide o problema em apenas 2 subproblemas recursivos de tamanho *n*/2, mas exige um processamento de combinação quadrático que consome tempo de execução de ordem Θ(*n*²) para correlacionar os elementos de suporte da entrada.

As equações de recorrência para os algoritmos A e B são dadas, respectivamente, por:
- *T*_A(*n*) = 4*T*_A(*n*/2) + Θ(*n*)
- *T*_B(*n*) = 2*T*_B(*n*/2) + Θ(*n*²)

**COMANDO DA QUESTÃO**
A partir da modelagem matemática das equações de recorrência de ambos os algoritmos e aplicando as definições e os casos do Teorema Mestre, analise as afirmações sobre a eficiência assintótica das duas estratégias propostas e assinale a alternativa correta:

**Alternativas:**
- **A)** Ambas as estratégias apresentam a mesma complexidade assintótica de pior caso *T*(*n*) = Θ(*n*²), indicando que os algoritmos possuem o mesmo comportamento de desempenho em escala, sendo indiferente a escolha técnica sob o ponto de vista de eficiência de hardware.
- **B)** A Estratégia Alfa é assintoticamente superior à Estratégia Beta, pois a recorrência *T*_A(*n*) = 4*T*_A(*n*/2) + Θ(*n*) resulta em complexidade de tempo de execução *O*(*n* log *n*) pelo Caso 2 do Teorema Mestre, enquanto a recorrência *T*_B(*n*) = 2*T*_B(*n*/2) + Θ(*n*²) resulta em complexidade quadrática *O*(*n*²).
- **C)** A Estratégia Beta é assintoticamente superior à Estratégia Alfa, uma vez que realiza apenas 2 chamadas recursivas, gerando uma equação de recorrência que resulta em complexidade logarítmica *O*(log *n*) pelo Caso 2 do Teorema Mestre, enquanto o Algoritmo A apresenta complexidade cúbica *O*(*n*³).
- **D)** A Estratégia Alfa apresenta complexidade exponencial *T*(*n*) = *O*(2ⁿ) pelo Caso 1 do Teorema Mestre, enquanto a Estratégia Beta apresenta complexidade polinomial *T*(*n*) = *O*(*n*⁴), evidenciando a instabilidade crítica de laços recursivos que dependem de divisões de escopo fracionárias.

**Gabarito: A** — _(não consta no material — resolvido aqui; coincide com o manual, p. 10–11)_

**Cálculo:**
- **Alfa:** *a* = 4, *b* = 2, *f*(*n*) = Θ(*n*). A fronteira é *n*^(log₂ 4) = *n*². Como *f*(*n*) = *O*(*n*^(2−ε)) com ε = 1, cai no **Caso 1** (a recursão domina, o custo vem das folhas): *T*_A = **Θ(*n*²)**.
- **Beta:** *a* = 2, *b* = 2, *f*(*n*) = Θ(*n*²). A fronteira é *n*^(log₂ 2) = *n*. Como *f*(*n*) = Ω(*n*^(1+ε)) com ε = 1, testa-se a regularidade: 2·(*n*/2)² = *n*²/2 ≤ *c*·*n*² com *c* = 1/2 < 1. Cai no **Caso 3** (a combinação domina): *T*_B = **Θ(*n*²)**.
- Conferi em python3 com *T*(1) = 1: as razões *T*_A(*n*)/*n*² e *T*_B(*n*)/*n*² tendem a 2 (≈ 1,999 para *n* = 2¹⁰), o que confirma Θ(*n*²) para as duas.

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — As duas estratégias são Θ(*n*²). A frase final reproduz a conclusão do manual (p. 11): "a escolha entre as duas abordagens … torna-se tecnicamente indiferente sob o ponto de vista de eficiência de hardware".
- **B) ❌** — Alfa não está no Caso 2. O Caso 2 exigiria *f*(*n*) = Θ(*n*²), e aqui *f*(*n*) = Θ(*n*). O erro típico é calcular a fronteira como *n*^(log₂ 2) = *n* em vez de *n*^(log₂ 4) = *n*². O resultado de Beta (*O*(*n*²)) está certo, mas a conclusão de que Alfa é superior é falsa.
- **C) ❌** — Ter menos chamadas recursivas não significa ter menor complexidade. Beta é dominada pela combinação Θ(*n*²) (Caso 3), e não *O*(log *n*); só *T*(*n*) = *T*(*n*/2) + Θ(1) daria Θ(log *n*). Alfa também não é *O*(*n*³); isso seria, por exemplo, 8*T*(*n*/2) + Θ(*n*²).
- **D) ❌** — O Teorema Mestre, com *a* e *b* constantes, nunca produz tempo exponencial. Exponenciais surgem em recorrências subtrativas como *T*(*n*) = 2*T*(*n* − 1) + … . Beta é Θ(*n*²), e não *n*⁴. A frase sobre "instabilidade crítica" não tem base.

**⚠️ Atenção:**
1. Formalmente, Θ(*n*²) ⊂ *O*(*n*⁴) ⊂ *O*(2ⁿ), porque Big-O é só um limite superior. Mesmo assim, D está errada: atribui ao Teorema Mestre a classe exponencial e opõe "exponencial" a "polinomial", e ambas as afirmações são falsas como classificação.
2. A expressão "indiferente … eficiência de hardware" em A é um exagero na prática, porque constantes, uso de cache e memória diferem. Ainda assim, é a conclusão literal do manual, e dentro da análise assintótica pedida A é a única correta.
3. Na Estratégia Alfa, *n* é a **dimensão** da matriz. Θ(*n*²) significa tempo linear no número de elementos (*n*²).

**Conceito-chave para a prova:** Para *T*(*n*) = *aT*(*n*/*b*) + *f*(*n*), compare *f*(*n*) com *n*^(log_b a). Caso 1 (*f* menor): Θ(*n*^(log_b a)). Caso 2 (iguais): Θ(*n*^(log_b a) · log *n*). Caso 3 (*f* maior, com regularidade *a*·*f*(*n*/*b*) ≤ *c*·*f*(*n*), *c* < 1): Θ(*f*(*n*)). Pode decorar: 4*T*(*n*/2) + *n* dá Θ(*n*²) e 2*T*(*n*/2) + *n*² também dá Θ(*n*²).

---

## Q6 — Top-k em fluxo de dados (afirmativa INCORRETA)
**Fonte:** `Resumo_ Complexidade de algoritmos (1).pdf`, p. 15 (slide "Questão 6", imagem). Base: `Manual - Complexidade de Algoritmos.pdf`, p. 8 (degradação do hash), p. 12 (Tabela 3 e §7.3), p. 13 (§8.2) e "Estudo de Caso: Filtragem das k Maiores Transações", p. 14. Slides p. 13–14
**Tipo ENADE:** Afirmativa negativa ("assinale a alternativa … INCORRETA")

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
Uma grande plataforma de comércio eletrônico precisa otimizar seu sistema de recomendação de produtos com base no histórico de cliques dos usuários em tempo real. O sistema processa um fluxo contínuo de *n* dados de interações. Para cada categoria de produto, o sistema deve manter uma coleção de dados de suporte contendo os *k* itens mais acessados (com *k* ≪ *n*) para sugerir dinamicamente aos usuários. Para assegurar o cumprimento de acordos de nível de serviço (SLA) de baixíssima latência sob condições de pico, a equipe de desenvolvimento propôs diferentes arquiteturas de software baseadas no acoplamento de estruturas de dados avançadas e algoritmos de ordenação e busca.

**DADOS DE SUPORTE**
Cormen et al. (2012) destacam que o projeto de algoritmos e estruturas de dados de alta performance exige uma postura crítica para comparar trade-offs de tempo e espaço, refutando escolhas intuitivas ou coleções genéricas sem fundamentação analítica.

Considere as propostas concebidas pela equipe de desenvolvimento:
- **Abordagem I (Merge Sort & Vetor):** Acumula todas as *n* interações em um arranjo dinâmico contíguo e, a cada intervalo de tempo, aplica o algoritmo Merge Sort para reordenar o vetor e recuperar os *k* maiores elementos.
- **Abordagem II (Min-Heap de tamanho k):** Mantém um Heap Mínimo na memória com exatamente *k* elementos do fluxo. Cada novo elemento é comparado com o mínimo (raiz). Se for maior, a raiz é substituída por ele e a propriedade de Heap é restaurada via a função auxiliar `heapify`.
- **Abordagem III (Tabela Hash & Heapsort):** Insere todas as *n* chaves em uma Tabela Hash com resolução por encadeamento. Quando o painel solicita a exibição, extraem-se os elementos em um vetor e ordena-se o vetor via Heapsort para obter os *k* maiores.

**COMANDO DA QUESTÃO**
Considerando a aplicação prática dessas abordagens, os custos assintóticos associados aos algoritmos de ordenação e às estruturas de dados, assinale a alternativa que apresenta uma análise de projeto de software **INCORRETA**:

**Alternativas:**
- **A)** A Abordagem I é ineficiente para fluxos de dados de grande escala, pois demanda uma complexidade de tempo de pior caso de *O*(*n* log *n*) em cada reordenação periódica e exige espaço de memória auxiliar de ordem *O*(*n*) devido ao uso do algoritmo Merge Sort.
- **B)** A Abordagem II é a solução mais escalável sob a ótica de usabilidade e restrição de recursos, visto que o seu tempo de processamento total é limitado a *O*(*n* log *k*) e o consumo de memória adicional é restrito a *O*(*k*) para manter o Heap Mínimo.
- **C)** A Abordagem III apresenta excelente desempenho em tempo de pior caso, pois o Heapsort realiza a ordenação das chaves em tempo *O*(*n*) sem consumir espaço de memória adicional, superando a latência de reorganização e inserção dinâmica gerada pelo Min-Heap.
- **D)** O acoplamento de uma Tabela Hash na Abordagem III resulta em complexidade de tempo de pior caso de busca de *O*(*n*) em caso de colisões críticas, violando os princípios de previsibilidade de latência e estabilidade exigidos para sistemas de alta performance.

**Gabarito: C** — _(não consta no material — resolvido aqui)_

**Por que cada alternativa está certa ou errada** (aqui ✅ marca a alternativa a assinalar, que é a afirmação INCORRETA):
- **A) ❌ (afirmação correta, não é a resposta)** — Merge Sort é Θ(*n* log *n*) em todos os casos e precisa de vetor auxiliar Θ(*n*) para a intercalação (manual p. 12, Tabela 3 e §7.3; slide p. 13). Repetir a ordenação total a cada intervalo é justamente o "uso ingênuo" que o manual rejeita (p. 14).
- **B) ❌ (afirmação correta, não é a resposta)** — É o estudo de caso do manual (p. 14) e do slide p. 14: construção Θ(*k*), uma comparação Θ(1) com a raiz por elemento e `heapify` Θ(log *k*) quando há substituição. Total *O*(*n* log *k*) de tempo e Θ(*k*) de espaço. Simulei em python3 com *n* = 100.000 e *k* = 100: o Min-Heap terminou exatamente com os 100 maiores.
- **C) ✅ (é a INCORRETA, gabarito)** — O Heapsort é Θ(*n* log *n*) no pior, médio e melhor caso (manual p. 12; slide p. 13), e não *O*(*n*). Nenhuma ordenação por comparação fica abaixo de Ω(*n* log *n*). Além disso, embora o Heapsort em si seja in-place (Θ(1) auxiliar), a Abordagem III guarda as *n* chaves na tabela hash e as copia para um vetor, o que consome Θ(*n*) de memória. E ordenar tudo para pegar *k* itens (Θ(*n* log *n*)) é pior que o Min-Heap (Θ(*n* log *k*)), então ela não "supera" a Abordagem II.
- **D) ❌ (afirmação correta, não é a resposta)** — Com encadeamento, se todas as chaves colidirem a tabela degenera em lista encadeada e a busca vira Θ(*n*). É a "Análise de Degradação Crítica" do manual (p. 8, com a mesma frase sobre violar a previsibilidade de latência), repetida no §8.2 (p. 13) e no slide p. 14 ("encadeamento saturado").

**⚠️ Atenção:** O slide p. 13 dá ao Quicksort memória auxiliar "Θ(1) In-place", mas o manual (Tabela 3, p. 12) diz "Θ(log *n*) (Pilha)" e o §7.3 diz Θ(*n*) de pilha sem otimização. Isso não afeta a Q6, mas pode aparecer numa versão alterada. Nesse caso, o valor tecnicamente correto é o do manual (pilha de recursão Θ(log *n*) a Θ(*n*)).

**Conceito-chave para a prova:** Para obter as *k* maiores de um fluxo de *n* itens, use um **Min-Heap de tamanho *k***: a raiz é o menor dos *k* maiores, o tempo é Θ(*n* log *k*) e o espaço é Θ(*k*). Merge Sort: Θ(*n* log *n*), memória Θ(*n*), estável. Heapsort: Θ(*n* log *n*) sempre, memória Θ(1), instável. Hash com encadeamento: Θ(1) em média e Θ(*n*) no pior caso, com todas as chaves colidindo.

---

## Questão-exemplo do professor (documento Estrutura de Questões ENADE)

O professor usa esta questão no documento sobre o padrão ENADE para ilustrar distratores (seção "4 – Alternativas de respostas · Exemplos de Distratores"). Ela não foi produzida pelo Squad 11, mas trata do mesmo tema.

### QP1 — Busca binária: pior caso em 1.048.576 usuários
**Fonte:** `Estrutura de Questões sob o padrão do ENADE.pdf`, p. 9 ("Exemplo 1: Estrutura de Dados e Complexidade de Algoritmos")
**Tipo ENADE:** Resposta única (cálculo / aplicação)

**Enunciado:**

**Situação-Problema:**
Um desenvolvedor precisa implementar um mecanismo de busca de usuários em uma plataforma de streaming. O sistema armazena uma lista de **1.048.576 usuários** ordenados alfabeticamente pelo ID. Para otimizar o tempo de resposta, o desenvolvedor optou por utilizar o algoritmo de **Busca Binária** para localizar um ID específico.

**Comando:**
No **pior cenário possível**, qual é o número máximo de comparações que o algoritmo realizará para encontrar o usuário ou determinar que ele não está na lista?

**Alternativas:**
- **A)** 1.048.576 comparações.
- **B)** 524.288 comparações.
- **C)** 20 comparações.
- **D)** 10 comparações.

(Como no original, são só 4 alternativas.)

**Gabarito: C** — _(origem: gabarito do próprio documento do professor, p. 9, marcado como "(Gabarito Correto)")_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Segundo o professor, é o pior caso da **busca sequencial (linear)**, com n comparações. O distrator explora a confusão entre O(log n), da busca binária, e O(n), da busca linear.
- **B) ❌** — Segundo o professor, é exatamente a metade do vetor (n/2). Atrai quem lembra vagamente que a busca binária "divide o problema ao meio", mas aplica a divisão de forma linear, uma única vez, em vez de logarítmica. Complemento: n/2 também é o número **médio** de comparações da busca linear, o que torna o distrator ainda mais plausível.
- **C) ✅** — A busca binária divide o espaço de busca pela metade a cada passo, então o número de comparações no pior caso é dado por log₂(n). Como 2²⁰ = 1.048.576, log₂(1.048.576) = 20. Passo a passo, o intervalo cai de 1.048.576 para 524.288, 262.144, …, 2 e 1, o que dá 20 divisões ao meio.
- **D) ❌** — Segundo o professor, é um erro de aproximação matemática rápida (pensar que 10⁶ resulta em 10 por causa da base decimal, ou confundir com log₁₀), ou um chute que divide a resposta certa (20) por dois. Complemento: log₁₀(1.048.576) ≈ 6, não 10. A origem mais provável do "10" é confundir 1.048.576 (= 1024² = 2²⁰) com 1.024 = 2¹⁰.

**⚠️ Atenção:** Pela contagem rigorosa, a busca binária clássica faz no pior caso **⌊log₂ n⌋ + 1 = ⌈log₂(n+1)⌉** comparações. Para n = 2²⁰ isso dá **21**: 20 divisões do intervalo mais a comparação com o último elemento que sobra. Conferi com uma simulação em python3: buscar uma chave maior que todas leva 21 iterações. O "20" do gabarito conta as divisões ao meio (log₂ n). Como 21 não está entre as alternativas, **C continua sendo a única resposta aceitável**, e é o gabarito do professor. Se uma versão alterada trouxer 20 e 21 ao mesmo tempo, saiba que o modelo do professor usa log₂(n) e que o valor tecnicamente rigoroso é ⌊log₂ n⌋ + 1.

Para versões com outro n (modelo do professor = log₂ n; rigoroso = ⌊log₂ n⌋ + 1):

| n | log₂ n (modelo do professor) | ⌊log₂ n⌋ + 1 (rigoroso) |
|---|---|---|
| 1.024 = 2¹⁰ | 10 | 11 |
| 65.536 = 2¹⁶ | 16 | 17 |
| 1.000.000 | ≈ 19,93 → 20 | 20 |
| 1.048.576 = 2²⁰ | 20 | 21 |
| 16.777.216 = 2²⁴ | 24 | 25 |
| 1.073.741.824 = 2³⁰ | 30 | 31 |
| 1.000.000.000 | ≈ 29,9 → 30 | 30 |

**Conceito-chave para a prova:** A busca binária exige vetor **ordenado** com acesso direto por índice. Ela divide o intervalo ao meio a cada comparação, com pior caso Θ(log n) ≈ log₂ n comparações, enquanto a busca linear tem pior caso n. Vale decorar as potências 2¹⁰ ≈ mil, 2²⁰ ≈ 1 milhão e 2³⁰ ≈ 1 bilhão. No manual do Squad 11 (p. 8, Tabela 2), a busca binária aparece com melhor caso Θ(1), caso médio Θ(log n) e pior caso Θ(log n).

---


## Pontos do manual e dos slides com maior chance de virar questão (atualizado)

Não são questões do material, e nenhuma questão foi inventada nesta seção. A tabela mostra quais pontos do `Manual - Complexidade de Algoritmos.pdf` e dos slides já são cobrados por Q1–Q6 e quais ainda não têm questão conhecida. As questões inferidas para os pontos descobertos estão em `../questoes_inferidas/01_Complexidade_de_Algoritmos.md`.

| # | Ponto do material | Manual | Slides | Questão conhecida |
|---|---|---|---|---|
| 1 | Escala clássica de crescimento (Tabela 1) e regra de dominância | p. 3 | p. 2 | Q3 (ordem das classes); Q1 (limite) |
| 2 | Ordenação das funções I–V (II – I – IV – III – V) | p. 4 | — | **Q3** |
| 3 | Definições formais de O, Ω e Θ | p. 4 | p. 3 | Q1 cobra só o Big-O |
| 4 | n² = O(n log₂ n) é falsa (prova por limite) | p. 4–5 | — | **Q1** |
| 5 | Modelo de Knuth e busca com sentinela | p. 6–7 | p. 5 | **Q2** |
| 6 | Pior, melhor e caso médio; Tabela 2 de buscas; degradação do hash | p. 8 | p. 7 | parcial: QP1 (pior caso da binária) e Q6-D (hash Θ(n)) |
| 7 | Laço triangular (soma de Gauss) | p. 9 | p. 9 | — (só aparece como distrator C da Q4) |
| 8 | Laço com PG decrescente = 2n − 1 | p. 9 | p. 9 | **Q4** |
| 9 | Teorema Mestre (3 casos) e Alfa × Beta | p. 10–11 | p. 11 | **Q5** (Casos 1 e 3; o Caso 2 não é exercitado) |
| 10 | Paradigmas de projeto (força bruta, D&C, guloso, PD) | p. 12 | — | — |
| 11 | Ordenação: Insertion, Merge, Quick, Heap (Tabela 3 e §7.3) | p. 12 | p. 13 | parcial: Q6 (Merge Θ(n) de memória; Heapsort não é O(n)) |
| 12 | ABP: custo, degeneração e percursos | p. 13 | p. 14 | — |
| 13 | Hashing: encadeamento × endereçamento aberto, fator de carga α | p. 13 | p. 14 | parcial: Q6-D |
| 14 | Heap e as k maiores (Min-Heap de tamanho k) | p. 13–14 | p. 14 | **Q6** |

Resumo do que o material afirma nos pontos ainda não cobertos (ou só parcialmente cobertos):

1. **Definições formais (manual p. 4, slide p. 3).** O é o limite superior (0 ≤ f(n) ≤ c·g(n) ∀n ≥ n₀), Ω é o limite inferior (0 ≤ c·g(n) ≤ f(n)) e Θ é o limite firme, o "sanduíche" (c₁·g ≤ f ≤ c₂·g). Pela Tabela 1 (p. 3): Θ(log n) é típico de divisões sucessivas do espaço de busca; Θ(n log n), de ordenação ótima por divisão e conquista; Θ(n²), de laços duplos simples ou triangulares; Θ(n³), de laços triplos ou multiplicação ingênua de matrizes; Θ(2ⁿ), de força bruta. Se lim f/g = 0, então g domina f.
2. **Melhor, médio e pior caso (manual p. 8, Tabela 2; slide p. 7).** O pior caso dá a garantia (SLA, tempo real). O caso médio supõe uma distribuição de probabilidade, comumente uniforme. O melhor caso serve para validar fast-paths. Busca linear: Θ(1), Θ(n), Θ(n). Busca binária: Θ(1), Θ(log n), Θ(log n). Hash com encadeamento: Θ(1), Θ(1), Θ(n), com o pior caso quando todas as chaves colidem e a tabela degenera em lista encadeada. ⚠️ A Tabela 2 aponta como "causa do pior caso" da busca binária "chave na raiz ou folha da árvore de busca". Chave na raiz (o elemento do meio) é o **melhor** caso, Θ(1). O pior caso é a chave numa folha (último nível) ou ausente.
3. **Laço triangular (manual p. 9, slide p. 9).** `for i=1..n { for j=1..i }` executa n(n+1)/2 = 0,5n² + 0,5n vezes, portanto Θ(n²) (soma de Gauss/PA).
4. **Caso 2 do Teorema Mestre (manual p. 10, slide p. 11: "Equilíbrio: combinação e divisão empatam. O custo logarítmico é incorporado").** Se f(n) = Θ(n^(log_b a)), então T(n) = Θ(n^(log_b a) · log n). Exemplo clássico: Merge Sort, 2T(n/2) + Θ(n), dá Θ(n log n).
5. **Paradigmas (manual p. 12; não aparecem nos slides).** Força bruta testa todas as soluções e pode ser exponencial. Divisão e conquista usa subproblemas independentes (busca binária, Merge Sort). O método guloso faz escolhas locais sem voltar atrás e exige prova de otimalidade global (ex.: Dijkstra). A programação dinâmica serve para subproblemas sobrepostos + subestrutura ótima, com tabelamento/memorização.
6. **Ordenação (manual p. 12, Tabela 3; slide p. 13).** Insertion Sort: Θ(n) / Θ(n²) / Θ(n²), memória Θ(1), estável. Merge Sort: Θ(n log n) sempre, memória Θ(n), estável. Quicksort: Θ(n log n) no caso médio e **Θ(n²) no pior caso** (vetor pré-ordenado com pivô no menor/maior elemento), instável, o mais rápido na prática. Heapsort: Θ(n log n) sempre, memória Θ(1), instável, com pior localidade de cache que o Quicksort. ⚠️ Há divergência sobre a memória do Quicksort: o slide p. 13 diz "Θ(1) In-place", e o manual diz "Θ(log n) (Pilha)" na Tabela 3 e Θ(n) de pilha sem otimização no §7.3. O slide também não traz o Insertion Sort.
7. **ABP (manual p. 13, slide p. 14).** Esquerda < raiz ≤ direita. Busca, inserção e remoção custam Θ(log n) em média. Com inserção em ordem crescente ou decrescente e sem balanceamento (AVL ou Red-Black), a árvore degenera em altura linear e as operações passam a Θ(n). A **pré-ordem** serve para clonagem/serialização, a **em-ordem** produz as chaves em ordem crescente e a **pós-ordem** serve para liberar os nós da memória. A figura do slide p. 14 é uma ABP com raiz 40, filhos 30 e 50 e folhas 25, 35, 45 e 60.
8. **Hashing (manual p. 13).** O fator de carga é α = n/m. Com boa função e α estável, as operações custam Θ(1) em média. No **encadeamento**, as colisões vão para listas externas. No **endereçamento aberto**, os elementos ficam no próprio vetor e a posição é procurada por sondagem linear, quadrática ou duplo hashing. Os dois têm pior caso Θ(n).
