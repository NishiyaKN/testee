# Compiladores — Questões INFERIDAS (prováveis questões do banco do squad que não temos)

> ⚠️ **Atenção:** estas questões NÃO constam nos materiais. Foram elaboradas para cobrir os subtópicos do material do
> Squad 7 que não têm questão conhecida, imitando o estilo das questões do squad. Servem para estudo dirigido.
> As questões reais conhecidas estão em `../questoes_por_topico/11_Compiladores.md`.

**Base usada:**
- `Material_Explicativo_Compiladores.pdf` (4 p.): seção 1, "Visão Geral da Arquitetura de Compiladores", com a tabela de fases (Léxica, Sintática, Semântica, Representação Intermediária, Geração de Código) e seus artefatos (p. 1). Seções 2 a 6 = Temas 1 a 5, um por questão conhecida (p. 1–4).
- `Compiladores_Roteiro_Oficial_23_Slides.pdf.pdf` (23 p.): p. 2, "Fluxo de compilação" (6 etapas: código-fonte, léxica, sintática, semântica, "IR e otimizações", geração de código; front-end × back-end). Blocos de conceitos nas p. 3, 7, 11, 15 e 19. Questões nas p. 4–5, 8–9, 12–13, 16–17 e 20–21, todas em imagem, que renderizei para conferir o estilo. Correções nas p. 6, 10, 14, 18 e 22. p. 23, "Resumo integrado", com uma pergunta-chave por fase.
- Questões conhecidas: Q1 léxica (C), Q2 sintática (B), Q3 semântica (D), Q4 geração de código/spill (B), Q5 ambiguidade/Bison (C).

**Estilo identificado do squad (seguido aqui):**
- **4 alternativas (A–D)**. As 5 questões conhecidas são do tipo **resposta única** e pedem duas coisas: o diagnóstico (causa do erro) e a estratégia de correção.
- Título "QUESTÃO N – TEMA". A situação-problema começa com "Uma equipe (de desenvolvimento) está implementando/testando…" e termina com "A equipe precisa identificar/diagnosticar… e definir/indicar uma correção…".
- "DADOS DE SUPORTE" com código, gramática ou tabelas ("Tabela 1 –", "Tabela 2 –"), seguido de "Fonte: elaboração própria, adaptada conceitualmente de…". O squad cita o LLVM Tutorial, o LLVM Code Generator, o GNU Bison 3.8.1 e a Oracle JLS SE 26. As fontes das questões inferidas imitam esse padrão e são **referências sugeridas**, que não constam no material.
- Comando no formato "Considerando…, assinale a alternativa que identifica corretamente… e apresenta…".
- Os distratores repetem quatro padrões: (1) empurrar a decisão para a fase errada (parser, semântica ou gerador de código); (2) uma solução que só serve para o caso testado; (3) violar uma restrição dada (por exemplo, usar R3); (4) inverter precedência ou associatividade.
- Para variar os tipos, como pede o guia do professor, 5 questões inferidas são de resposta única, 1 é de associação, 1 de asserção-razão e 1 de afirmativas múltiplas.

## Mapa de cobertura
| # | Subtópico (material) | Páginas | Questão conhecida | Questão inferida | Prioridade |
|---|---|---|---|---|---|
| 1 | Visão geral: o compilador como tradutor; front-end × back-end intermediados por IR independente de máquina | Material p. 1 (seção 1); Slides p. 2 | — | **I1** | Alta |
| 2 | Fases do compilador e responsabilidade de cada uma: tabela de fases e "Resumo integrado", com uma pergunta-chave por fase | Material p. 1 (tabela); Slides p. 2 e 23 | — (cada questão conhecida trata **uma** fase; nenhuma pede para distinguir as fases entre si) | **I2** | Alta |
| 3 | Léxica: lexema × token, conflito entre identificador e palavra reservada, tabela de keywords | Material p. 1–2; Slides p. 3–6 | **Q1** | — (variação provável: em Flex/Lex, declarar as regras das keywords antes da regra de ID) | — |
| 4 | Léxica: padrões de tokens definidos por ER e implementados por AFD | Material p. 1 (tabela: "Expressões regulares, autômatos finitos") e p. 1 (Tema 1, "Fundamentação Teórica") | — (a Q1 usa a ER de identificador, mas cobra a tabela de keywords) | **I3** | Média |
| 5 | Sintática: GLC, terminal / não-terminal / produção, lista recursiva | Material p. 2; Slides p. 7–10 | **Q2** | — (variação provável: a versão com recursão à direita, `<lista> → <argumento> \| <argumento> ',' <lista>`, citada no título "Recursão Esquerda/Direita") | — |
| 6 | Sintática × léxica: linguagem regular × GLC (hierarquia de Chomsky, Tipo 3 × Tipo 2); parser constrói a AST | Material p. 2 ("Enquanto a análise léxica lida com sequências regulares, a análise sintática opera sobre GLC… (Tipo 2)"); p. 1 | — | **I4** | Média |
| 7 | Semântica: verificação de tipos e conversão explícita | Material p. 3; Slides p. 11–14 | **Q3** | — | — |
| 8 | Semântica: declaração, escopo e resolução de nomes com a tabela de símbolos | Material p. 1 ("Tabela de Símbolos enriquecida… checagem de fluxo") e p. 3 ("escopo de variáveis, o controle de fluxo e a resolução de nomes"); Slides p. 11 ("Declaração de variáveis · Escopo · Tabela de símbolos: nomes, tipos e permissões") | — | **I5** | Alta |
| 9 | Representação intermediária: código de três endereços (TAC) e temporários virtuais | Material p. 1 (linha "4. Representação Intermediária") e p. 3; Slides p. 2 e 15 | — (a Q4 usa a IR pronta, apenas como dado) | **I6** | Alta |
| 10 | Representação intermediária: SSA (Static Single Assignment) | Material p. 1 (tabela) | — | **I7** | Média |
| 11 | Otimizações sobre a IR (independentes de máquina) | Material p. 1 ("Fornece código independente de máquina para otimização"); Slides p. 2 ("IR e otimizações") | — | **I8** | Média |
| 12 | Geração de código: seleção de instruções, alocação de registradores, liveness, spill/reload | Material p. 3; Slides p. 15–18 | **Q4** | — (variação provável: outra expressão ou outra quantidade de registradores, ou trocar MUL por SUB) | — |
| 13 | Ambiguidade, precedência, associatividade, conflitos shift/reduce, diretivas `%left` do Bison | Material p. 4; Slides p. 19–22 | **Q5** | — (variação provável: outra expressão, `%right`, ou reescrever a gramática em níveis expr/termo/fator, que o material cita como alternativa "sem reescrever a gramática em múltiplos níveis") | — |
| — | **Fora do material:** recuperação/tratamento de erros, análise LL × LR, First/Follow, compilador × interpretador, autômatos com pilha | Não constam no material nem nos slides. O Bison e os conflitos shift/reduce só aparecem dentro do Tema 5 | — | — (sem questão: o material não dá base) | Baixa |

**Resumo:** 13 subtópicos no material; 5 já cobertos por questões conhecidas (Q1–Q5); **8 questões inferidas** (I1–I8).
**Gabarito rápido das inferidas:** I1 **A** · I2 **C** · I3 **B** · I4 **A** · I5 **C** · I6 **D** · I7 **B** · I8 **D** (A2 · B2 · C2 · D2).

> Observação: o material explicativo traz uma "Análise Crítica dos Distratores" só para as Questões 1–5, e o slide 1 anuncia "5 questões". Por isso, é provável que o banco do squad tenha **apenas** as 5 questões conhecidas. As inferidas abaixo cobrem o que o material apresenta (tabela de fases, IR, otimização, escopo, ER/AFD) sem questão própria. Se a prova trouxer algo novo de Compiladores, o mais provável é que venha daqui.

## Índice
1. [I1 — Arquitetura do compilador: front-end, IR e back-end](#i1--arquitetura-do-compilador-front-end-ir-e-back-end)
2. [I2 — Fases do compilador: qual fase detecta cada problema](#i2--fases-do-compilador-qual-fase-detecta-cada-problema)
3. [I3 — Análise léxica: expressão regular e AFD do token NUMERO](#i3--análise-léxica-expressão-regular-e-afd-do-token-numero)
4. [I4 — Linguagem regular × livre de contexto (lexer × parser)](#i4--linguagem-regular--livre-de-contexto-lexer--parser)
5. [I5 — Análise semântica: escopo e tabela de símbolos](#i5--análise-semântica-escopo-e-tabela-de-símbolos)
6. [I6 — Representação intermediária: código de três endereços](#i6--representação-intermediária-código-de-três-endereços)
7. [I7 — Representação intermediária: forma SSA](#i7--representação-intermediária-forma-ssa)
8. [I8 — Otimização da IR: dobramento de constantes, subexpressões comuns e código morto](#i8--otimização-da-ir-dobramento-de-constantes-subexpressões-comuns-e-código-morto)

---

## I1 — Arquitetura do compilador: front-end, IR e back-end
**Subtópico coberto:** visão geral da arquitetura: front-end e back-end intermediados por IR (Material p. 1, seção 1; Slides p. 2).
**Por que é provável:** é a primeira seção do material e o slide de abertura ("Fluxo de compilação", com "Front-end: análise do código" e "Back-end: IR e recursos da arquitetura"). Nenhuma das 5 questões conhecidas cobra essa divisão.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única

**Enunciado:**

**QUESTÃO I1 – ARQUITETURA DO COMPILADOR (FRONT-END, IR E BACK-END)**

SITUAÇÃO-PROBLEMA
Uma software house mantém três linguagens próprias (automação comercial, scripts de integração e relatórios) e gera código para dois processadores, x86-64 e ARM. Hoje existe um compilador completo e independente para cada par linguagem–processador. Por isso, um defeito na análise de uma linguagem precisa ser corrigido em vários compiladores.

A empresa passará a atender também processadores RISC-V e decidiu reorganizar os compiladores segundo a arquitetura clássica, em que um front-end e um back-end se comunicam por uma representação intermediária (IR) comum. A equipe precisa definir em qual módulo fica cada responsabilidade e quantos módulos serão necessários após a expansão.

DADOS DE SUPORTE

Tabela 1 – Responsabilidades a distribuir

| Código | Responsabilidade |
|---|---|
| (1) | Converter a cadeia de caracteres em tokens e reconhecer palavras reservadas |
| (2) | Validar a sequência de tokens pela gramática e construir a AST |
| (3) | Verificar tipos, declarações e escopo com a tabela de símbolos |
| (4) | Selecionar as instruções da arquitetura-alvo |
| (5) | Alocar registradores físicos e tratar spill |

Tabela 2 – Cenário

| Item | Quantidade |
|---|---|
| Linguagens-fonte | 3 |
| Processadores atendidos hoje | 2 (x86-64 e ARM) |
| Processadores após a expansão | 3 (x86-64, ARM e RISC-V) |

IR adotada: código de três endereços com temporários virtuais (t1, t2, …), sem referência a registradores físicos.

_Fonte: elaboração própria, adaptada conceitualmente de LATTNER, C. "LLVM". In: BROWN, A.; WILSON, G. (org.). The Architecture of Open Source Applications, v. 1, cap. 11 – A Quick Introduction to Classical Compiler Design._

COMANDO
**Considerando as responsabilidades listadas, a IR adotada e a expansão para três processadores, assinale a alternativa que distribui corretamente as responsabilidades entre front-end e back-end e indica a quantidade de módulos necessária.**

**Alternativas:**
- **A)** (1), (2) e (3) ficam no front-end, que depende apenas da linguagem-fonte e produz a IR; (4) e (5) ficam no back-end, que depende apenas do processador. Com a IR comum, bastam 3 front-ends e 3 back-ends (6 módulos), e o suporte ao RISC-V exige apenas um novo back-end.
- **B)** (1), (2), (3) e (5) ficam no front-end, pois a análise semântica já conhece os tipos e pode associar cada variável a um registrador físico na própria IR; (4) fica no back-end. Assim, o suporte ao RISC-V exige ajustar os 3 front-ends e criar 1 novo back-end.
- **C)** (1) e (2) ficam no front-end, e (3), (4) e (5) no back-end, pois a verificação de tipos depende do tamanho dos registradores de cada processador; como a IR passa a ser específica de cada processador, são necessários 3 × 3 = 9 tradutores para a IR.
- **D)** Como as fases de análise trabalham com tokens e AST genéricos, um único front-end atende às três linguagens; já o back-end, responsável por (4) e (5), precisa ser específico para cada par linguagem–processador, totalizando 1 + 9 = 10 módulos.

**Gabarito: A**

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — O front-end faz a "análise do código: caracteres, estrutura, tipos e escopo" (slide p. 2), ou seja, léxica, sintática e semântica. Essas fases dependem da linguagem-fonte, já que cada uma tem suas keywords (Q1), sua gramática (Q2) e suas regras de tipo (Q3). O back-end "recebe a representação intermediária" (material p. 3) e cuida da "seleção de instruções e alocação de registradores" (slide p. 2), o que depende do processador. Como a IR é **independente de máquina** (material p. 1), qualquer front-end conversa com qualquer back-end. São 3 + 3 = **6 módulos**, contra 3 × 3 = 9 compiladores completos sem IR. Para o RISC-V basta escrever 1 back-end, e os 3 front-ends não mudam.
- **B) ❌** — Alocar registradores físicos é tarefa do back-end. A IR usa temporários virtuais "sem correspondência direta com registradores físicos" (slide p. 15). Se a IR já trouxesse registradores, ficaria presa a um processador, e cada nova arquitetura obrigaria a mexer em todos os front-ends, que é justamente o problema que a arquitetura quer evitar.
- **C) ❌** — A compatibilidade de tipos é uma regra **da linguagem** (na Q3, "regras semânticas da linguagem"), não do processador. Uma IR específica por processador perde a independência de máquina e volta ao esquema M × N (9 tradutores).
- **D) ❌** — Inverte as dependências. As análises léxica, sintática e semântica são próprias de cada linguagem (keywords, gramática e regras de tipo diferentes), então não existe um front-end único para as três. O back-end, por sua vez, não deve depender da linguagem, porque trabalha só com a IR. O resultado, 10 módulos, é pior que os 6 da arquitetura correta.

**Base no material:** p. 1 — "transforma um programa fonte escrito em uma linguagem de alto nível… em um programa equivalente de baixo nível (como código de máquina ou bytecode intermediário). A arquitetura clássica divide esse processo em duas grandes fases estruturais: o Front-end e o Back-end, intermediados por uma ou mais Representações Intermediárias (IR)"; tabela: IR "Fornece código independente de máquina". Slide p. 2: "Front-end → IR → Back-end".
**Conceito-chave para a prova:** front-end = análise (léxica, sintática, semântica), depende da **linguagem**; back-end = seleção de instruções e alocação de registradores, depende da **máquina**; a IR independente de máquina liga os dois. Com M linguagens e N máquinas, são necessários M + N módulos em vez de M × N compiladores.

---

## I2 — Fases do compilador: qual fase detecta cada problema
**Subtópico coberto:** responsabilidade de cada fase (Material p. 1, tabela de fases; Slides p. 2 e p. 23, "Resumo integrado").
**Por que é provável:** o slide de encerramento resume as cinco fases com uma pergunta-chave para cada ("Lexema → token correto?", "A sequência é derivável pela gramática?", "Tipos, declarações e usos são compatíveis?", "Temporários cabem nos recursos físicos?"). Além disso, todos os distratores do squad exploram a troca de fase. Uma questão integradora de associação é o passo natural.
**Prioridade:** Alta
**Tipo ENADE:** Associação

**Enunciado:**

**QUESTÃO I2 – FASES DO COMPILADOR**

SITUAÇÃO-PROBLEMA
A equipe de testes do compilador de uma linguagem estaticamente tipada para automação comercial está montando um relatório para os desenvolvedores. Cada trecho testado contém uma única situação que o compilador precisa tratar. Para encaminhar o trabalho ao módulo certo, o relatório deve indicar a fase do compilador responsável por detectar ou resolver cada situação.

DADOS DE SUPORTE

Trechos testados

```
// Trecho I
inteiro total = 5;
saldo = total + 1;

// Trecho II
inteiro total = 5$;

// Trecho III
se (total > 10 {
    total = 0;
}

// Trecho IV
resultado = (a + b) * (c + d) * (e + f);
```

Observações da equipe de testes:
- Trecho I: `saldo` não consta na tabela de símbolos.
- Trecho II: o caractere `$` não pertence a nenhum padrão de token da linguagem.
- Trecho III: os tokens foram todos reconhecidos.
- Trecho IV: o trecho está correto, e todas as variáveis estão declaradas como `inteiro`. O processador-alvo tem só dois registradores físicos (R1 e R2), e a tradução precisa manter vivos, ao mesmo tempo, mais valores do que esses dois registradores comportam.

Fases do compilador

| Código | Fase |
|---|---|
| 1 | Análise léxica |
| 2 | Análise sintática |
| 3 | Análise semântica |
| 4 | Geração de código |

_Fonte: elaboração própria, adaptada conceitualmente de LLVM Project, "My First Language Frontend with LLVM Tutorial", capítulos 1 (Lexer), 2 (Parser and AST) e 3 (Code generation to LLVM IR). llvm.org/docs/tutorial/MyFirstLanguageFrontend/_

COMANDO
**Considerando os trechos testados, as observações da equipe e as fases do compilador, assinale a alternativa que associa corretamente cada trecho à fase responsável por detectar ou resolver a situação descrita.**

**Alternativas:**
- **A)** I – 2; II – 1; III – 2; IV – 4.
- **B)** I – 3; II – 2; III – 2; IV – 4.
- **C)** I – 3; II – 1; III – 2; IV – 4.
- **D)** I – 3; II – 1; III – 2; IV – 3.

**Gabarito: C**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Considera o uso de variável não declarada um erro sintático. `saldo = total + 1;` é derivável pela gramática (é uma atribuição bem formada). A falha está na **resolução de nomes**: `saldo` não está na tabela de símbolos, e essa verificação é da análise semântica (slide p. 11: "Declaração de variáveis"; slide p. 23: "Tipos, declarações e usos são compatíveis?").
- **B) ❌** — Considera `$` um erro sintático. O lexer converte caracteres em tokens. Se um caractere não casa com nenhum padrão (ER) de token, o erro aparece **antes** de existir uma sequência de tokens para o parser analisar. É um erro léxico (slide p. 23: "Lexema → token correto?").
- **C) ✅** — I: o identificador não declarado é detectado pela **semântica** (3), consultando a tabela de símbolos. II: o caractere fora do alfabeto de tokens é detectado pela **léxica** (1). III: os tokens estão corretos, mas falta o `)` antes de `{`, e a sequência não é derivável pela gramática, então é a **sintática** (2) que detecta. IV: não é erro. Os valores vivos superam os registradores, e a **geração de código** (4) resolve com spill e reload, como na Questão 4 (slide p. 23: "Temporários cabem nos recursos físicos? Spill / reload").
- **D) ❌** — Trata o trecho IV como erro semântico. O trecho tem tipos compatíveis e não deve ser rejeitado. A falta de registradores físicos é uma restrição da arquitetura, tratada no back-end pela alocação de registradores e pelo spill (material p. 3).

**Base no material:** tabela da p. 1 (função de cada fase: tokens válidos → hierarquia estrutural → tipos, escopos e consistência → IR → alocação de registradores e spill); slides p. 2 e 23.
**Conceito-chave para a prova:** caractere ou lexema sem token → **léxica**; sequência de tokens que não deriva da gramática → **sintática**; nome não declarado, tipo incompatível ou uso fora do escopo → **semântica**; falta de registradores → **geração de código** (spill), o que não é erro do programa.

---

## I3 — Análise léxica: expressão regular e AFD do token NUMERO
**Subtópico coberto:** padrões de tokens definidos por expressões regulares e implementados por AFD (Material p. 1, tabela e "Fundamentação Teórica" do Tema 1).
**Por que é provável:** o material diz que "os padrões dos lexemas são definidos por Expressões Regulares (ER) e implementados computacionalmente por Autômatos Finitos Determinísticos (AFD)". A Q1 usa uma ER, mas não cobra a construção ou correção de uma ER. Uma "Q1 versão 2" faria isso, com a fonte que o squad já usa (LLVM Tutorial).
**Prioridade:** Média
**Tipo ENADE:** Resposta única

**Enunciado:**

**QUESTÃO I3 – ANÁLISE LÉXICA (EXPRESSÕES REGULARES E AUTÔMATOS)**

SITUAÇÃO-PROBLEMA
Uma equipe de desenvolvimento definiu o token NUMERO do analisador léxico de uma nova linguagem pela expressão regular abaixo, implementada por um autômato finito determinístico (AFD). Nos testes, `10` e `3.14` foram reconhecidos corretamente. O analisador, porém, também emitiu NUMERO para os lexemas `1.2.3`, `.` e `7.`. O problema só apareceu mais tarde, quando o valor convertido não correspondia ao texto digitado.

A especificação da linguagem diz que um número é formado por um ou mais dígitos, opcionalmente seguidos de um ponto e de um ou mais dígitos (a parte fracionária). A equipe precisa identificar a falha na definição do token e escolher uma nova expressão regular que continue implementável por um AFD.

DADOS DE SUPORTE

Regra atual do token:

```
NUMERO → (dígito | '.')+
```

Tabela 1 – Resultado dos testes do analisador léxico

| Lexema | Token produzido | Esperado pela especificação |
|---|---|---|
| 10 | NUMERO | NUMERO |
| 3.14 | NUMERO | NUMERO |
| 1.2.3 | NUMERO | não é um NUMERO |
| . | NUMERO | não é um NUMERO |
| 7. | NUMERO | não é um NUMERO |

_Fonte: elaboração própria, adaptada conceitualmente de LLVM Project, "My First Language Frontend with LLVM Tutorial", capítulo 1 – Kaleidoscope Introduction and the Lexer. llvm.org/docs/tutorial/MyFirstLanguageFrontend/LangImpl01.html_

COMANDO
**Considerando a regra atual, os resultados dos testes e a especificação do token, assinale a alternativa que identifica corretamente a falha e apresenta uma expressão regular adequada para NUMERO.**

**Alternativas:**
- **A)** A regra atual pode ser mantida, pois o lexer deve aceitar qualquer sequência de dígitos e pontos; cabe à análise semântica, ao converter o lexema em valor numérico, verificar a quantidade e a posição dos pontos e rejeitar os casos inválidos.
- **B)** A regra atual aceita o ponto em qualquer posição e quantidade. Deve-se usar `NUMERO → dígito+ ('.' dígito+)?`, cujo AFD tem um estado não final logo após o ponto, de modo que 10 e 3.14 são aceitos e 1.2.3, . e 7. deixam de formar um único NUMERO.
- **C)** A regra atual falha apenas por permitir que o lexema termine em ponto. Deve-se usar `NUMERO → (dígito | '.')* dígito`, que rejeita . e 7. e mantém a aceitação de 10 e 3.14, atendendo integralmente à especificação da linguagem.
- **D)** A regra atual falha por não exigir a parte fracionária. Deve-se usar `NUMERO → dígito+ '.' dígito+`, que rejeita 1.2.3, . e 7. e simplifica o AFD, já que todo número passa a ter exatamente um ponto entre dígitos.

**Gabarito: B**

**Por que cada alternativa está certa ou errada:** (conferido em python3 com `re.fullmatch` e simulação do AFD)
- **A) ❌** — Mesmo erro do distrator D da Q1: deixa a classificação léxica errada e adia a decisão. A forma do lexema é regra **léxica**. Se o lexer emite NUMERO para `.`, o parser recebe um token falso e a semântica chega tarde demais.
- **B) ✅** — `(dígito | '.')+` aceita qualquer mistura de dígitos e pontos (inclusive `.`, `7.`, `1.2.3`, `.5`, `1..2`). A ER `dígito+ ('.' dígito+)?` corresponde exatamente à especificação. O AFD é:

  | Estado | dígito | '.' | Final? |
  |---|---|---|---|
  | q0 (inicial) | q1 | — | não |
  | q1 (parte inteira) | q1 | q2 | **sim** |
  | q2 (leu o ponto) | q3 | — | **não** |
  | q3 (parte fracionária) | q3 | — | **sim** |

  Como q2 não é final, `7.` e `.` não formam NUMERO. Em `1.2.3`, o AFD aceita `1.2` e para no segundo ponto, então o lexema inteiro não é um único NUMERO. Com a regra do maior lexema (*longest match*), a saída seria NUMERO(1.2), erro léxico em `.` e depois NUMERO(3). Resultado da simulação: 10 → S, 3.14 → S, 0 → S, 1.2.3 → N, . → N, 7. → N.
- **C) ❌** — Corrige só o ponto final. `(dígito | '.')* dígito` ainda aceita `1.2.3`, `.5` e `1..2`, então **não** atende integralmente à especificação. É o padrão "resolve só o caso testado", como o distrator C da Q2.
- **D) ❌** — Restritiva demais: torna a parte fracionária obrigatória e passa a rejeitar inteiros como `10` e `0`, o que contraria a especificação ("opcionalmente seguidos de um ponto…").

**Base no material:** p. 1 — "os padrões dos lexemas são definidos por Expressões Regulares (ER) e implementados computacionalmente por Autômatos Finitos Determinísticos (AFD)"; tabela da p. 1: Léxica → "Expressões regulares, autômatos finitos". O slide p. 3 traz a ER `letra (letra | dígito)*` como exemplo de padrão.
**Conceito-chave para a prova:** a ER define a forma do lexema, e o AFD a implementa (estados finais = lexema completo). Os operadores `+` (uma ou mais), `*` (zero ou mais) e `?` (opcional) determinam o que é aceito. Confira sempre os casos de borda (ponto inicial, ponto final, dois pontos, inteiro sem parte fracionária). Erro de formação de token é **léxico**.

---

## I4 — Linguagem regular × livre de contexto (lexer × parser)
**Subtópico coberto:** a análise léxica trabalha com linguagens regulares e a sintática com GLC (Tipo 2 na hierarquia de Chomsky); o parser constrói a AST (Material p. 2, "Fundamentação Teórica" do Tema 2; p. 1, tabela).
**Por que é provável:** é a frase de abertura do Tema 2, com menção explícita à hierarquia de Chomsky. A Q2 cobra a lista recursiva, mas não a razão teórica para a separação lexer/parser.
**Prioridade:** Média
**Tipo ENADE:** Asserção-razão

**Enunciado:**

**QUESTÃO I4 – ANÁLISE LÉXICA × ANÁLISE SINTÁTICA**

SITUAÇÃO-PROBLEMA
Para reduzir o tamanho do compilador de uma linguagem de automação de processos, um integrante da equipe propõe validar as chamadas de função diretamente no analisador léxico, com uma única expressão regular, e retirar do parser as regras dessas chamadas. A validação deve aceitar argumentos com parênteses aninhados em qualquer profundidade, como nos testes abaixo. Outro integrante afirma que a proposta é inviável e defende manter as regras na gramática do parser.

DADOS DE SUPORTE

Testes de aceitação

| Trecho | Resultado esperado |
|---|---|
| `registrarVenda(cliente, (total + 10));` | aceitar |
| `registrarVenda(((total)));` | aceitar |
| `registrarVenda((total);` | rejeitar (parêntese sem fechamento) |

Gramática atual do parser (trecho)

```
<chamada> → IDENTIFICADOR '(' <lista> ')' ';'
<lista>   → <expr> | <lista> ',' <expr>
<expr>    → <termo> | <expr> '+' <termo>
<termo>   → IDENTIFICADOR | NUMERO | '(' <expr> ')'
```

_Fonte: elaboração própria, adaptada conceitualmente de GNU Project, "Bison 3.8.1 Manual", seção 1.1 – Languages and Context-Free Grammars. https://www.gnu.org/software/bison/manual/_

COMANDO
**Considerando a proposta, os testes e a gramática apresentada, avalie as asserções a seguir e a relação proposta entre elas.**

I. A validação de chamadas com parênteses aninhados em profundidade arbitrária deve permanecer no analisador sintático, descrita pela gramática livre de contexto, e não ser transferida para uma expressão regular do analisador léxico.

**PORQUE**

II. Expressões regulares e os autômatos finitos que as implementam descrevem apenas linguagens regulares (Tipo 3 na hierarquia de Chomsky) e têm um número finito de estados, sem como registrar quantos parênteses ainda faltam fechar; já uma produção recursiva como `<termo> → '(' <expr> ')'`, de uma GLC (Tipo 2), gera esse aninhamento.

A respeito dessas asserções, assinale a opção correta.

**Alternativas:**
- **A)** As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
- **B)** As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
- **C)** A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
- **D)** A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.

**Gabarito: A**

**Julgamento das asserções:**
- **I — Verdadeira.** Parênteses balanceados em profundidade arbitrária não são uma linguagem regular. A gramática dada reconhece os dois primeiros testes e rejeita o terceiro (conferido com um parser descendente em python3: o terceiro falha com "esperado `)`, achou `;`"). O lexer continua emitindo os tokens `(` e `)`, e quem verifica o aninhamento é o parser.
- **II — Verdadeira.** Um AFD com k estados não distingue k + 1 níveis de aninhamento, porque precisaria "contar" sem limite. A recursão `<termo> → '(' <expr> ')'` gera qualquer profundidade. É a distinção da p. 2: "a análise léxica lida com sequências regulares, a análise sintática opera sobre GLC… (Tipo 2)".
- **Relação:** a II explica por que a I é necessária (a limitação teórica das ERs obriga a deixar o aninhamento para a GLC), então **justifica** a I.

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — As duas são verdadeiras, e a II é a causa (o limite das linguagens regulares) que fundamenta a decisão da I.
- **B) ❌** — A II não é um fato solto: é exatamente o motivo pelo qual a proposta de ER única é inviável.
- **C) ❌** — A II é verdadeira. Confundir "ER aceita repetição (`*`, `+`)" com "ER aceita aninhamento balanceado" é o erro que este distrator explora.
- **D) ❌** — A I é verdadeira. Uma ER pode aceitar parênteses até uma profundidade fixa, mas a especificação pede profundidade arbitrária.

**Base no material:** p. 2 — "Enquanto a análise léxica lida com sequências regulares, a análise sintática (parser) opera sobre Gramáticas Livres de Contexto (GLC) definidas na hierarquia de Chomsky (Tipo 2). O parser valida a hierarquia de tokens e constrói a Árvore Sintática Abstrata (AST)"; tabela p. 1 (Léxica: ER/autômatos finitos; Sintática: GLC/AST).
**Conceito-chave para a prova:** lexer = linguagens **regulares** (ER/AFD, Tipo 3), que reconhecem a forma de cada token; parser = **GLC** (Tipo 2), que reconhece estrutura aninhada ou recursiva e monta a AST. Repetição simples cabe em ER; aninhamento balanceado exige GLC.

---

## I5 — Análise semântica: escopo e tabela de símbolos
**Subtópico coberto:** declaração, escopo e resolução de nomes (Material p. 1 e p. 3; Slides p. 11).
**Por que é provável:** o slide de conceitos da semântica lista três verificações ("Compatibilidade de tipos · Declaração de variáveis · Escopo") e a "Tabela de símbolos: nomes, tipos e permissões", mas a Q3 só cobra tipos. Escopo é o subtópico semântico seguinte mais citado.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única

**Enunciado:**

**QUESTÃO I5 – ANÁLISE SEMÂNTICA (ESCOPO E TABELA DE SÍMBOLOS)**

SITUAÇÃO-PROBLEMA
Uma equipe de desenvolvimento recebeu o chamado de um programador que afirma ter encontrado um defeito no compilador de uma linguagem estaticamente tipada. O trecho abaixo foi aceito pelas análises léxica e sintática, mas o compilador o rejeitou com a mensagem "linha 6: identificador 'valorFinal' não declarado", embora `valorFinal` tenha sido declarado na linha 3.

A especificação da linguagem adota escopo de bloco. A equipe precisa verificar se o compilador agiu corretamente e orientar uma correção compatível com as regras da linguagem.

DADOS DE SUPORTE

Trecho de código analisado

```
1  inteiro desconto = 5;
2  se (desconto > 0) {
3      inteiro valorFinal = 100 - desconto;
4      desconto = desconto + 1;
5  }
6  imprimir(valorFinal);
```

Regras semânticas relevantes da linguagem
1. Todo identificador deve ser declarado antes de ser usado.
2. Uma variável declarada dentro de um bloco `{ }` só é visível do ponto da declaração até o fim desse bloco.
3. Um bloco interno pode usar e alterar as variáveis dos blocos que o envolvem.

Tabela de símbolos (organizada como pilha de escopos), estado ao processar a linha 4

| Nível | Escopo | Identificador | Tipo |
|---|---|---|---|
| 0 | global | desconto | inteiro |
| 1 | bloco do `se` (linhas 2–5) | valorFinal | inteiro |

Ao encerrar o bloco (linha 5), o nível 1 é removido da pilha.

_Fonte: elaboração própria, adaptada conceitualmente de Oracle, Java Language Specification, Java SE 26, seção 6.3 (Scope of a Declaration). https://docs.oracle.com/javase/specs/jls/se26/html/_

COMANDO
**Considerando o trecho de código, as regras de escopo e a tabela de símbolos, assinale a alternativa que avalia corretamente a mensagem emitida pelo compilador e propõe uma correção compatível com as regras da linguagem.**

**Alternativas:**
- **A)** O compilador está incorreto, pois a tabela de símbolos deveria manter todos os identificadores em um único escopo global até o fim do programa; assim, valorFinal continuaria visível na linha 6, e o trecho seria aceito sem nenhuma alteração.
- **B)** O erro é léxico, pois, após o fechamento do bloco, valorFinal deixa de ser reconhecido como IDENTIFICADOR; a correção consiste em registrar valorFinal na tabela de palavras reservadas, garantindo seu reconhecimento em todo o programa.
- **C)** O compilador agiu corretamente: na linha 6, a resolução de nomes não encontra valorFinal, pois seu escopo terminou com o bloco; uma correção é declarar valorFinal antes do `se`, no nível global, e apenas atribuir seu valor dentro do bloco.
- **D)** O erro está na linha 4, e não na linha 6: ao alterar desconto dentro do bloco, o programa viola o escopo global, e o compilador deveria indicar a linha 4; removendo-se essa linha, valorFinal passa a ser visível na linha 6.

**Gabarito: C**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Contraria a regra 2 (escopo de bloco). Uma tabela de símbolos única e global ignora a estrutura de escopos que a especificação exige. O compilador seguiu a especificação, não errou.
- **B) ❌** — Confunde a tabela de **palavras reservadas** (usada pelo lexer, Q1) com a **tabela de símbolos** (usada pela semântica). O lexer continua emitindo IDENTIFICADOR para `valorFinal` na linha 6. A falha está na resolução do nome, e transformar uma variável em palavra reservada impediria seu uso como identificador.
- **C) ✅** — A busca por `valorFinal` na linha 6 percorre a pilha de escopos e só encontra o nível 0, porque o nível 1 foi removido na linha 5. Então a regra 1 é violada nesse ponto, e quem detecta é a **análise semântica**. Correção válida pelas regras 1–3:
  ```
  inteiro desconto = 5;
  inteiro valorFinal = 0;
  se (desconto > 0) {
      valorFinal = 100 - desconto;
      desconto = desconto + 1;
  }
  imprimir(valorFinal);
  ```
- **D) ❌** — A linha 4 é válida pela regra 3, porque um bloco interno pode alterar variáveis de blocos externos. Além disso, apagar a linha 4 não muda o escopo de `valorFinal`, e a linha 6 continuaria inválida.

**Base no material:** p. 3 — "A análise semântica examina a consistência de tipos, o escopo de variáveis, o controle de fluxo e a resolução de nomes utilizando a Tabela de Símbolos"; tabela p. 1 ("Tabela de Símbolos enriquecida"); slide p. 11 ("Declaração de variáveis · Escopo · Tabela de símbolos: nomes, tipos e permissões"); slide p. 23 ("Tipos, declarações e usos são compatíveis?").
**Conceito-chave para a prova:** declaração ausente e uso fora do escopo são erros **semânticos**, detectados pela tabela de símbolos (em geral uma pilha de escopos: entra no bloco, empilha; sai do bloco, desempilha). Não confunda tabela de símbolos (nomes, tipos, escopo) com tabela de palavras reservadas (lexer).

---

## I6 — Representação intermediária: código de três endereços
**Subtópico coberto:** IR em código de três endereços (TAC) com temporários virtuais, independente de máquina (Material p. 1 e p. 3; Slides p. 2 e p. 15).
**Por que é provável:** a IR é uma das cinco fases da tabela do material ("4. Representação Intermediária (IR)", com TAC, SSA e temporários virtuais) e uma etapa própria no slide 2 ("IR e otimizações"). Na Q4 ela já vem pronta, e nenhuma questão pede para gerá-la.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única

**Enunciado:**

**QUESTÃO I6 – REPRESENTAÇÃO INTERMEDIÁRIA (CÓDIGO DE TRÊS ENDEREÇOS)**

SITUAÇÃO-PROBLEMA
Uma equipe está implementando o módulo que traduz a árvore sintática para a representação intermediária (IR) do compilador. A IR adotada é código de três endereços: cada instrução tem no máximo um operador do lado direito (até dois operandos e um destino), e os resultados intermediários são guardados em temporários virtuais t1, t2, …, sem referência a registradores físicos, porque a mesma IR será usada por back-ends de processadores diferentes.

Na linguagem, `*` e `/` têm precedência maior que `+` e `-`, e todos esses operadores são associativos à esquerda. A equipe precisa escolher uma tradução que preserve a semântica da expressão e respeite as regras da IR.

DADOS DE SUPORTE

Comando da linguagem-fonte

```
total = subtotal - desconto * taxa + frete;
```

Valores usados no teste: subtotal = 100, desconto = 10, taxa = 2, frete = 15. Valor esperado: total = 95.

_Fonte: elaboração própria, adaptada conceitualmente de LLVM Project, "My First Language Frontend with LLVM Tutorial", capítulo 3 – Code generation to LLVM IR. llvm.org/docs/tutorial/MyFirstLanguageFrontend/LangImpl03.html_

COMANDO
**Considerando o comando da linguagem-fonte, as regras de precedência e associatividade e as restrições da IR, assinale a alternativa que apresenta uma tradução que preserva a semântica do programa e respeita as regras da representação intermediária adotada.**

**Alternativas:**
- **A)** `t1 = subtotal - desconto; t2 = t1 * taxa; t3 = t2 + frete; total = t3`. A tradução segue a ordem em que os operadores aparecem na cadeia de entrada, usando um único operador por instrução.
- **B)** `t1 = desconto * taxa; t2 = t1 + frete; t3 = subtotal - t2; total = t3`. A tradução calcula primeiro o produto e agrupa os termos à direita do primeiro operando antes da subtração.
- **C)** `R1 = desconto * taxa; R2 = subtotal - R1; R2 = R2 + frete; total = R2`. A tradução usa diretamente os registradores físicos, dispensando a alocação de registradores no back-end.
- **D)** `t1 = desconto * taxa; t2 = subtotal - t1; t3 = t2 + frete; total = t3`. A tradução aplica a precedência de `*` e a associatividade à esquerda de `-` e `+`, com um operador por instrução.

**Gabarito: D**

**Por que cada alternativa está certa ou errada:** (conferido em python3 com os valores do teste)
- **A) ❌** — Ignora a precedência de `*` e calcula `((subtotal - desconto) * taxa) + frete` = (100 − 10) · 2 + 15 = **195** ≠ 95. É o erro da interpretação I da Q5 (todos os operadores no mesmo nível).
- **B) ❌** — Respeita a precedência, mas troca a associatividade: calcula `subtotal - ((desconto * taxa) + frete)` = 100 − (20 + 15) = **65** ≠ 95. Como `-` e `+` associam à esquerda, a subtração tem de ser feita antes da soma.
- **C) ❌** — O valor (95) está certo, mas a tradução viola a IR adotada: usa registradores físicos (R1, R2) em vez de temporários virtuais. Isso prende a IR a uma máquina e antecipa um trabalho que é do back-end (slide p. 15: temporários virtuais "sem correspondência direta com registradores físicos").
- **D) ✅** — `desconto * taxa` primeiro (precedência), depois `subtotal - t1` e por fim `+ frete` (associatividade à esquerda): 100 − 20 + 15 = **95**. Cada instrução tem um operador e no máximo três endereços, e os temporários são virtuais.

**Base no material:** p. 3 — "representação intermediária (IR) — tipicamente expressa em código de três endereços com temporários virtuais ilimitados (ex: t1 = a + b, t2 = c + d, t3 = t1 * t2)"; tabela p. 1 ("Fornece código independente de máquina… Código de 3 endereços (TAC)… temporários virtuais"); slide p. 15 ("IR: t1, t2, t3, …"). Precedência e associatividade: p. 4 e slide p. 19.
**Conceito-chave para a prova:** TAC = **uma operação por instrução**, resultado em temporário virtual. A ordem das instruções segue a árvore sintática (precedência e associatividade). Registradores físicos só aparecem no back-end.

---

## I7 — Representação intermediária: forma SSA
**Subtópico coberto:** SSA (Static Single Assignment) como forma de IR (Material p. 1, tabela).
**Por que é provável:** a SSA aparece explicitamente entre os artefatos da fase de IR e não é cobrada em nenhuma questão. O squad usa o LLVM como fonte, e a IR do LLVM é SSA.
**Prioridade:** Média
**Tipo ENADE:** Afirmativas múltiplas

**Enunciado:**

**QUESTÃO I7 – REPRESENTAÇÃO INTERMEDIÁRIA (FORMA SSA)**

SITUAÇÃO-PROBLEMA
Para facilitar as otimizações, uma equipe decidiu converter o código de três endereços gerado pelo front-end para a forma SSA (Static Single Assignment), a mesma usada pela IR do LLVM. Um estagiário produziu a versão SSA abaixo para um trecho sem desvios, e a equipe precisa revisá-la antes de integrá-la ao compilador.

DADOS DE SUPORTE

Código de três endereços original

```
1: x = a + b
2: y = x * 2
3: x = y - c
4: z = x + y
```

Versão SSA proposta pelo estagiário

```
1: x1 = a + b
2: y1 = x1 * 2
3: x2 = y1 - c
4: z1 = x2 + y1
```

Valores usados no teste: a = 3, b = 4, c = 5. No código original, ao final, x = 9, y = 14 e z = 23.

_Fonte: elaboração própria, adaptada conceitualmente de LLVM Project, "My First Language Frontend with LLVM Tutorial", capítulo 7 – Extending the Language: Mutable Variables, e "LLVM Language Reference Manual". llvm.org/docs/tutorial/MyFirstLanguageFrontend/LangImpl07.html_

COMANDO
**Considerando o código original, a versão SSA proposta e os valores de teste, avalie as afirmativas.**

I. A versão proposta respeita a forma SSA, pois cada nome (x1, y1, x2, z1) recebe valor uma única vez; por isso, a segunda atribuição a x, na linha 3, gerou a nova versão x2.

II. A versão proposta preserva a semântica do código original, pois, na linha 4, o uso de x refere-se à definição mais recente (x2) e o uso de y à sua única definição (y1), resultando em z1 = 23 para os valores de teste.

III. Por ser a etapa final da tradução, a forma SSA exige que cada versão (x1, y1, x2, z1) corresponda a um registrador físico distinto, o que dispensa a alocação de registradores no back-end.

É correto o que se afirma em

**Alternativas:**
- **A)** I, apenas.
- **B)** I e II, apenas.
- **C)** II e III, apenas.
- **D)** I, II e III.

**Gabarito: B**

**Julgamento das afirmativas:** (conferido em python3)
- **I — Verdadeira.** Na SSA, cada variável é atribuída exatamente uma vez. A reatribuição de `x` (linha 3) gera uma nova versão, `x2`, e nenhum nome da versão proposta é atribuído duas vezes.
- **II — Verdadeira.** x1 = 7, y1 = 14, x2 = 14 − 5 = 9, z1 = 9 + 14 = **23**, igual ao original. Se a linha 4 usasse `x1`, o resultado seria 7 + 14 = 21, e a semântica mudaria (é o erro típico de renomeação).
- **III — Falsa.** A SSA é uma **IR**, independente de máquina, e seus nomes são temporários virtuais ilimitados. O mapeamento para registradores físicos (e o spill, quando faltam registradores) continua no back-end (material p. 3; Q4).

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Deixa de fora a II, que é verdadeira: a renomeação preserva o resultado (23).
- **B) ✅** — I e II verdadeiras, III falsa.
- **C) ❌** — Inclui a III, que confunde temporário virtual com registrador físico, e exclui a I, que é verdadeira.
- **D) ❌** — Inclui a III, que é falsa.

**Base no material:** tabela p. 1 — "Representação Intermediária (IR): Fornece código independente de máquina para otimização · Código de 3 endereços (TAC), SSA (Static Single Assignment), temporários virtuais"; p. 3 e slide p. 15 (temporários virtuais × registradores físicos).
**Conceito-chave para a prova:** SSA = **cada nome é atribuído uma única vez**. Toda reatribuição gera nova versão (x1, x2…), e cada uso aponta para a definição que o alcança. Fora do material, mas útil: com desvios (if/else), a SSA usa funções φ (phi) para unir versões vindas de caminhos diferentes. A SSA continua sendo IR, e a alocação de registradores fica no back-end.

---

## I8 — Otimização da IR: dobramento de constantes, subexpressões comuns e código morto
**Subtópico coberto:** otimizações independentes de máquina sobre a IR (Material p. 1; Slides p. 2).
**Por que é provável:** o slide 2 nomeia a etapa "IR e otimizações", e a tabela do material diz que a IR "fornece código independente de máquina **para otimização**". Nenhuma questão conhecida cobra otimização. O capítulo 4 do tutorial do LLVM, fonte que o squad já cita, trata exatamente de dobramento de constantes e eliminação de redundâncias.
**Prioridade:** Média
**Tipo ENADE:** Resposta única (avaliação de versões de código, no mesmo molde da Q4)

**Enunciado:**

**QUESTÃO I8 – OTIMIZAÇÃO DA REPRESENTAÇÃO INTERMEDIÁRIA**

SITUAÇÃO-PROBLEMA
Antes de enviar a IR ao back-end, uma equipe quer incluir no compilador uma etapa de otimização independente de máquina com três transformações: dobramento de constantes (calcular em tempo de compilação operações cujos operandos são constantes conhecidas), eliminação de subexpressões comuns (reaproveitar o resultado de uma expressão já calculada com os mesmos operandos) e eliminação de código morto (remover instruções cujo resultado nunca é usado). A otimização não pode alterar o valor devolvido pela função.

DADOS DE SUPORTE

IR da função `calcular(preco)`

```
1: t1 = 2 * 3
2: t2 = preco * t1
3: t3 = preco * 6
4: aux = preco * 100
5: t4 = t2 + t3
6: resultado = t4
```

Observações:
- `preco` é parâmetro da função, e seu valor só é conhecido em tempo de execução.
- `aux` é variável local e não é usada depois da linha 4.
- A função devolve `resultado`.
- Teste: para preco = 10, o resultado esperado é 120.

_Fonte: elaboração própria, adaptada conceitualmente de LLVM Project, "My First Language Frontend with LLVM Tutorial", capítulo 4 – Adding JIT and Optimizer Support (seções Trivial Constant Folding e LLVM Optimization Passes). llvm.org/docs/tutorial/MyFirstLanguageFrontend/LangImpl04.html_

COMANDO
**Considerando a IR, as transformações desejadas e a restrição de preservar o valor devolvido, avalie as versões abaixo e assinale a que aplica corretamente as três otimizações e preserva a semântica da função.**

**Alternativas:**
- **A)** `t2 = preco * 6; resultado = t2`. Como t2 e t3 calculam a mesma expressão, a segunda ocorrência e a soma que a utiliza podem ser descartadas como código morto.
- **B)** `resultado = 12`. O dobramento de constantes calcula toda a expressão em tempo de compilação, pois 2 * 3 e 6 são constantes e a função envolve apenas multiplicações e somas.
- **C)** `t1 = 2 * 3; t2 = preco * t1; t3 = preco * 6; t4 = t2 + t3; resultado = t4`. As operações são mantidas, pois otimizações só podem ser feitas no back-end, após a alocação de registradores; apenas aux é removido.
- **D)** `t2 = preco * 6; t4 = t2 + t2; resultado = t4`. Dobra 2 * 3 em 6, reaproveita em t2 o valor de preco * 6 no lugar de t3 e remove aux, cujo valor nunca é usado.

**Gabarito: D**

**Por que cada alternativa está certa ou errada:** (conferido em python3 com preco = 10, 1 e 7)
- **A) ❌** — Confunde subexpressão comum com código morto. `t3` é igual a `t2`, mas **é usado** na soma. Eliminar a subexpressão comum significa reaproveitar o valor (`t2 + t2`), não descartá-lo. Resultado: 6 · preco = **60** ≠ 120 (altera a semântica, como o distrator D da Q4).
- **B) ❌** — O dobramento de constantes só vale para operandos conhecidos em tempo de compilação. `preco` só é conhecido na execução, então `preco * 6` não pode ser dobrado. `resultado = 12` só coincide com o correto quando preco = 1 (para preco = 10, dá 12 ≠ 120).
- **C) ❌** — O valor (120) está certo, mas a justificativa contraria o material: a IR existe justamente para ser otimizada de forma **independente de máquina**, antes da geração de código (slide p. 2: "IR e otimizações" vem antes de "Geração de código"). Além disso, deixa de aplicar o dobramento e a eliminação de subexpressões pedidos.
- **D) ✅** — (1) **Dobramento**: `t1 = 2 * 3` vira `t1 = 6`. Propagando a constante, `t2 = preco * 6`, e `t1` deixa de ser usado. (2) **Subexpressão comum**: `t3 = preco * 6` repete `t2`, então `t4 = t2 + t2`. (3) **Código morto**: `aux` nunca é usado e é removido (assim como `t1` após a propagação). Para preco = 10: t2 = 60, t4 = 120 = resultado esperado.

**Base no material:** tabela p. 1 — IR "Fornece código independente de máquina para otimização"; slide p. 2 — etapa 05 "IR e otimizações", antes de 06 "Geração de código". O material não detalha as técnicas de otimização. Os nomes e definições usados aqui são conhecimento padrão, explicados no próprio enunciado.
**Conceito-chave para a prova:** otimização na IR é **independente de máquina** e não pode mudar o resultado. Dobramento de constantes só vale para operandos conhecidos em compilação. Subexpressão comum **reaproveita** o valor, não o descarta. Código morto é o que **nunca é usado** depois.
