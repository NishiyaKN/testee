# Complexidade de Algoritmos — Questões e Gabarito Comentado

**Squad responsável:** Squad 11
**Materiais analisados:**
| Arquivo | Páginas | Tipo | Questões encontradas (páginas) |
|---|---|---|---|
| `Manual - Complexidade de Algoritmos.pdf` | 15 | Manual de referência / apostila (só texto, sem imagens; lido por inteiro) | **Nenhuma questão.** Só teoria e três "Estudos de Caso" já resolvidos no texto (p. 4, 8 e 14), sem comando nem alternativas |
| `Estrutura de Questões sob o padrão do ENADE.pdf` (documento do professor, não é do Squad 11) | 31 | Slides do professor sobre o padrão ENADE | 1 questão-exemplo de "Estrutura de Dados e Complexidade de Algoritmos" (p. 9) |

**Resumo:** ⚠️ **O material do Squad 11 não contém nenhuma questão.** O manual de 15 páginas não tem enunciado com alternativas, exercício, quiz, gabarito, asserção-razão nem pergunta discursiva. No repositório também não há slides nem arquivo de questões do Squad 11, embora o Plano de Ações peça a cada squad slides e questões no padrão ENADE. Este arquivo traz a **1 questão-exemplo do professor** (gabarito dado pelo próprio documento: **C**) e, no fim, os pontos do manual com maior chance de virar questão.
Total: 1 questão, com gabarito no material. Nenhuma foi resolvida sem gabarito.

> Legenda: ✅ correta · ❌ incorreta · ⚠️ ponto de atenção (gabarito do material duvidoso, ambiguidade, versão divergente)

## Índice
1. [Questão-exemplo do professor (documento Estrutura de Questões ENADE)](#questão-exemplo-do-professor-documento-estrutura-de-questões-enade)
   - [QP1 — Busca binária: pior caso em 1.048.576 usuários](#qp1--busca-binária-pior-caso-em-1048576-usuários)
2. [Pontos do material com maior chance de virar questão](#pontos-do-material-com-maior-chance-de-virar-questão)

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

## Pontos do material com maior chance de virar questão

Não são questões do material, e nenhuma questão foi inventada aqui. São os resultados e afirmações que o `Manual - Complexidade de Algoritmos.pdf` mais enfatiza, com a página, e que podem servir de base para questões.

1. **Ordenação assintótica de funções de custo (p. 3–4, "Estudo de Caso").** TI = 100n + 15 → Θ(n); TII = log₂(n⁵) = 5 log₂ n → Θ(log n); TIII = Σᵢ₌₁ⁿ i = n(n+1)/2 → Θ(n²); TIV = n log₂(n³) = 3n log₂ n → Θ(n log n); TV = 2ⁿ + n⁴ → Θ(2ⁿ). A ordem, do mais eficiente ao menos eficiente, é **II – I – IV – III – V**. As pegadinhas: o expoente dentro do log vira constante multiplicativa, e 2ⁿ domina n⁴. A escala da p. 3 vai de 1 a log n, n, n log n, n², n³ e 2ⁿ.
2. **Definições formais e dominância (p. 3–5).** O é o limite superior (0 ≤ f(n) ≤ c·g(n) ∀n ≥ n₀), Ω é o limite inferior e Θ é o limite firme (c₁·g ≤ f ≤ c₂·g). Se lim f(n)/g(n) = 0, então g domina f. A afirmação **n² = O(n log₂ n) é FALSA**, porque lim n²/(n log₂ n) = lim n/log₂ n = ∞.
3. **Modelo de Knuth e busca com sentinela (p. 6–7).** T(n) = Σ cᵢ·tᵢ (custo × frequência de cada linha). No pior caso (chave ausente), T = c₁ + n·c₂ + (n−1)·c₃ + c₄ + c₆ → **Θ(n)**: o teste do `while` executa n vezes e o incremento n−1 vezes. No melhor caso (chave em v[0]), T = c₁ + c₂ + c₄ + c₅ → **Θ(1)**. A sentinela elimina o teste de limite de índice e reduz pela metade as verificações lógicas do laço.
4. **Melhor, médio e pior caso das buscas (p. 8, Tabela 2).** Busca linear: Θ(1), Θ(n), Θ(n). Busca binária: Θ(1), Θ(log n), Θ(log n). Hash com encadeamento: Θ(1), Θ(1), Θ(n), e o pior caso ocorre quando todas as chaves colidem e a tabela degenera em lista encadeada. O pior caso dá a garantia (SLA, tempo real), e o caso médio supõe uma distribuição de probabilidade, comumente uniforme. ⚠️ A Tabela 2 aponta como "causa do pior caso" da busca binária "chave na raiz ou folha da árvore de busca". Chave na raiz (o elemento do meio) é o **melhor** caso, Θ(1). O pior caso é a chave numa folha (último nível) ou ausente.
5. **Laços aninhados (p. 9).** O laço triangular `for i=1..n { for j=1..i }` executa n(n+1)/2 = 0,5n² + 0,5n vezes → **Θ(n²)**. O laço `for (i=n; i>0; i/=2) { for (j=0; j<i; j++) }` executa n + n/2 + … + 1 = **2n − 1** vezes (PG de razão ½) → **Θ(n)**, e **não** Θ(n log n). O manual destaca essa armadilha explicitamente.
6. **Teorema Mestre (p. 10–11).** Para T(n) = aT(n/b) + f(n), compara-se f(n) com n^(log_b a). Caso 1 (f menor): Θ(n^(log_b a)). Caso 2 (iguais): Θ(n^(log_b a) · log n). Caso 3 (f maior e com a condição de regularidade a·f(n/b) ≤ c·f(n), c < 1): Θ(f(n)). Os exemplos do manual: **Alfa**, 4T(n/2) + Θ(n), cai no Caso 1 e dá Θ(n²); **Beta**, 2T(n/2) + Θ(n²), cai no Caso 3 (regularidade com c = ½) e também dá Θ(n²). Por isso o manual conclui que as duas estratégias são assintoticamente equivalentes.
7. **Paradigmas de projeto (p. 12).** Força bruta testa todas as soluções e pode chegar a custo exponencial. Divisão e conquista divide em subproblemas independentes (busca binária, Merge Sort). O método guloso faz escolhas locais sem voltar atrás e exige prova de que elas levam ao ótimo global (exemplo: Dijkstra). A programação dinâmica serve para **subproblemas sobrepostos + subestrutura ótima**, resolvendo cada subproblema uma vez e guardando o resultado (tabelamento/memorização).
8. **Ordenação (p. 12, Tabela 3 e §7.3).** Insertion Sort: Θ(n) / Θ(n²) / Θ(n²), memória Θ(1), estável. Merge Sort: Θ(n log n) em todos os casos, memória Θ(n) (vetor auxiliar), estável. Quicksort: Θ(n log n) no caso médio e **Θ(n²) no pior caso** (vetor pré-ordenado com pivô no menor/maior elemento), pilha Θ(log n) ou Θ(n) sem otimização, instável, e é o mais rápido na prática. Heapsort: Θ(n log n) em todos os casos, memória Θ(1), instável, com pior localidade de cache que o Quicksort.
9. **ABP e hashing (p. 13).** Na ABP, busca, inserção e remoção custam Θ(log n) em média. Com inserção em ordem crescente ou decrescente e sem balanceamento (AVL ou Red-Black), a árvore degenera e as operações passam a Θ(n). O percurso **em-ordem** produz as chaves em ordem crescente, a **pré-ordem** serve para clonagem/serialização e a **pós-ordem** para liberar os nós da memória. No hash, o fator de carga é α = n/m. As colisões se resolvem por **encadeamento** (listas externas) ou por **endereçamento aberto** (sondagem linear, quadrática ou duplo hashing), e ambos têm pior caso Θ(n).
10. **Heap e as k maiores transações (p. 13–14, "Estudo de Caso").** No Min-Heap a raiz é o menor elemento; no Max-Heap, o maior. Para manter as k maiores de n transações (k ≪ n) usa-se um **Min-Heap de tamanho k**, porque a raiz é o menor dos k maiores. Construir o heap custa Θ(k), e cada um dos n − k elementos seguintes é comparado com a raiz em Θ(1). Se x > raiz, x substitui a raiz e o heapify custa Θ(log k). O total é **Θ(n log k)** de tempo e **Θ(k)** de espaço auxiliar.
