# Compiladores — Questões e Gabarito Comentado

**Squad responsável:** Squad 7
**Materiais analisados:**
| Arquivo | Páginas | Tipo | Questões encontradas (páginas) |
|---|---|---|---|
| `Compiladores_Roteiro_Oficial_23_Slides.pdf.pdf` | 23 | Slides ("Aula inversa"). Os enunciados estão só em imagem nas p. 4, 5, 8, 9, 12, 13, 16, 17, 20 e 21 | Q1–Q5. Enunciados nas p. 4–5, 8–9, 12–13, 16–17 e 20–21. Slides de correção com gabarito nas p. 6, 10, 14, 18 e 22. Conceitos nas p. 3, 7, 11, 15 e 19 |
| `Material_Explicativo_Compiladores.pdf` | 4 | Material explicativo (apostila) | Não reproduz enunciados nem alternativas. Traz a fundamentação de cada tema e a "Análise Crítica dos Distratores" das Questões 1–5 (p. 1–4) |

**Resumo:** 5 questões encontradas, todas objetivas no padrão ENADE (situação-problema, dados de suporte e comando), com **4 alternativas (A–D)**. As 5 têm gabarito no próprio material (slides de correção), e a análise de distratores do material explicativo confirma cada um. Nenhuma precisou ser resolvida sem gabarito. Conferi os 5 gabaritos de forma independente (inclusive simulando a Q4 em python3) e todos estão corretos. O slide 1 anuncia "Resolução comentada de 5 questões", e as 5 estão no PDF.

**Gabarito rápido:** Q1 **C** · Q2 **B** · Q3 **D** · Q4 **B** · Q5 **C**

> Legenda: ✅ correta · ❌ incorreta · ⚠️ ponto de atenção (gabarito do material duvidoso, ambiguidade, versão divergente)

## Índice
1. [Q1 — Análise léxica: identificadores x palavras reservadas](#q1--análise-léxica-identificadores-x-palavras-reservadas)
2. [Q2 — Análise sintática: lista recursiva de argumentos](#q2--análise-sintática-lista-recursiva-de-argumentos)
3. [Q3 — Análise semântica: incompatibilidade de tipos](#q3--análise-semântica-incompatibilidade-de-tipos)
4. [Q4 — Geração de código: alocação de registradores e spill](#q4--geração-de-código-alocação-de-registradores-e-spill)
5. [Q5 — Ambiguidade, precedência e associatividade (Bison)](#q5--ambiguidade-precedência-e-associatividade-bison)

---

## Q1 — Análise léxica: identificadores x palavras reservadas
**Fonte:** `Compiladores_Roteiro_Oficial_23_Slides.pdf.pdf`: situação-problema e dados de suporte na p. 4 (imagem), comando e alternativas na p. 5 (imagem), correção na p. 6 e conceitos na p. 3. Também em `Material_Explicativo_Compiladores.pdf`, p. 1–2 ("Tema 1" e "Análise Crítica dos Distratores (Questão 1)").
**Tipo ENADE:** Resposta única (diagnóstico da causa + estratégia de correção)

**Enunciado:**

**QUESTÃO 1 – ANÁLISE LÉXICA**

Uma equipe de desenvolvimento está implementando o analisador léxico de uma nova linguagem de programação. A especificação da linguagem determina que os identificadores sejam reconhecidos pela seguinte regra:

```
IDENTIFICADOR → letra (letra | dígito)*
```

Durante os testes, o analisador reconheceu corretamente nomes como valor, resultado e contador1. Entretanto, também classificou os lexemas if, while e return como identificadores, embora eles estejam definidos como palavras reservadas da linguagem.

Para facilitar a manutenção do compilador, a equipe mantém as palavras reservadas em uma tabela própria, permitindo que novas palavras sejam adicionadas sem modificar a regra geral de formação dos identificadores.

A equipe precisa identificar a causa da classificação incorreta e definir uma estratégia de reconhecimento que diferencie os identificadores comuns das palavras reservadas.

**DADOS DE SUPORTE**

Tabela 1 – Palavras reservadas definidas pela linguagem

| Lexema | Token definido |
|---|---|
| if | KW_IF |
| while | KW_WHILE |
| return | KW_RETURN |

Regra geral de reconhecimento de identificadores:

```
IDENTIFICADOR → letra (letra | dígito)*
```

Durante um teste, foi processado o trecho:

```c
if (contador1 >= 10)
    return resultado;
```

Tabela 2 – Saída produzida pelo analisador léxico

| Lexema | Token produzido |
|---|---|
| if | IDENTIFICADOR |
| ( | ABRE_PARENTESE |
| contador1 | IDENTIFICADOR |
| >= | OPERADOR_RELACIONAL |
| 10 | NUMERO |
| ) | FECHA_PARENTESE |
| return | IDENTIFICADOR |
| resultado | IDENTIFICADOR |
| ; | PONTO_E_VIRGULA |

_Fonte: elaboração própria, adaptada conceitualmente de LLVM Project, "My First Language Frontend with LLVM Tutorial", capítulo 5 – Lexer Extensions for If/Then/Else. llvm.org/docs/tutorial/MyFirstLanguageFrontend/LangImpl05.html_

**Considerando a regra de formação de identificadores, a tabela de palavras reservadas e a saída produzida pelo analisador léxico, assinale a alternativa que identifica corretamente a causa da classificação inadequada de if e return e apresenta uma estratégia adequada para corrigir o reconhecimento desses lexemas.**

**Alternativas:**
- **A)** O analisador deve manter if e return como identificadores durante a etapa léxica e permitir que o analisador sintático determine posteriormente se esses lexemas exercem funções reservadas conforme sua posição no programa.
- **B)** O padrão de identificadores deve ser reformulado para impedir que qualquer sequência correspondente a uma palavra reservada seja reconhecida inicialmente, eliminando a necessidade de consultar a tabela mantida pela linguagem durante a análise léxica.
- **C)** O analisador deve reconhecer inicialmente a sequência compatível com identificadores e, em seguida, consultar a tabela de palavras reservadas, atribuindo prioridade ao token específico sempre que o lexema estiver registrado nessa tabela.
- **D)** O analisador deve conservar a classificação de identificador e registrar na tabela de símbolos que determinados nomes possuem uso especial, permitindo que a análise semântica determine posteriormente sua função na linguagem.

**Gabarito: C** — _(origem: gabarito do próprio material, slide p. 6, "RESPOSTA C". O material explicativo, p. 2, trata A, B e D como distratores)_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Transfere uma decisão léxica para o parser e viola a separação de fases. O parser precisa receber os tokens já discriminados (KW_IF, KW_RETURN), porque a gramática é escrita em termos deles. Com IDENTIFICADOR no lugar de KW_IF, a regra do `if` nem casa. (slide p. 6: "A transfere uma decisão lexical para o parser"; material p. 2)
- **B) ❌** — Reescrever a expressão regular para excluir as palavras reservadas abandona a tabela de keywords e contraria o requisito de manutenção do enunciado ("novas palavras adicionadas sem modificar a regra geral"). Também "engessa" a especificação: cada nova palavra reservada exigiria mudar a ER. (slide p. 6: "B abandona a tabela e contraria o requisito de manutenção"; material p. 2)
- **C) ✅** — A **causa** é que `if` e `return` casam com o padrão geral `letra (letra | dígito)*` e o lexer emite IDENTIFICADOR sem consultar a tabela de reservadas. A **estratégia** tem duas etapas: (1) reconhecer a sequência alfanumérica pelo padrão geral; (2) consultar logo em seguida a tabela de palavras reservadas. Se o lexema estiver lá, o lexer emite o token específico (KW_IF, KW_RETURN), que tem prioridade; se não estiver, emite IDENTIFICADOR. Isso preserva a regra geral e permite incluir novas keywords só acrescentando linhas na tabela. (slide p. 6; material p. 2, "Estratégia de Correção Adequada")
- **D) ❌** — Mantém a classificação léxica incorreta e adia a decisão para a semântica, o que é tarde demais: o parser já teria recebido IDENTIFICADOR no lugar de KW_IF e falharia antes da semântica (o material diz que "a classificação lexical incorreta já teria corrompido o parser"). Além disso, a tabela de símbolos guarda nomes do programa (variáveis, funções), não serve para reclassificar tokens. (slide p. 6: "D mantém a classificação lexical incorreta e empurra a decisão para a semântica"; material p. 2)

**Diferenças entre versões:** O material explicativo não traz o enunciado nem as alternativas. Ele resume o problema dizendo que a regra "reconhece perfeitamente nomes como valor e contador1, mas também aceita incorretamente sequências como if e return". O enunciado dos slides cita ainda `resultado` e `while`. O gabarito (C) é o mesmo nas duas fontes.

**Conceito-chave para a prova:** Lexema é o texto concreto (`if`, `contador1`); token é a categoria atribuída a ele (KW_IF, IDENTIFICADOR). Quando palavras reservadas também casam com a ER de identificador, a correção é **léxica**: casar o padrão geral, consultar a tabela de keywords e emitir o token específico, que tem prioridade. A decisão não cabe ao parser nem à semântica. (Observação: em geradores como Flex, um resultado equivalente vem de declarar as regras das keywords antes da regra de ID. Mas, no cenário da questão, a exigência é manter a tabela própria.)

---

## Q2 — Análise sintática: lista recursiva de argumentos
**Fonte:** `Compiladores_Roteiro_Oficial_23_Slides.pdf.pdf`: situação-problema e dados de suporte na p. 8 (imagem), comando e alternativas na p. 9 (imagem), correção na p. 10 e conceitos na p. 7. Também em `Material_Explicativo_Compiladores.pdf`, p. 2 ("Tema 2" e "Análise Crítica dos Distratores (Questão 2)").
**Tipo ENADE:** Resposta única (diagnóstico da causa + correção da gramática)

**Enunciado:**

**QUESTÃO 2 – ANÁLISE SINTÁTICA**

Uma equipe de desenvolvimento está implementando o analisador sintático (parser) de uma nova linguagem destinada à automação de processos. A especificação da linguagem permite chamadas de funções com um ou mais argumentos, separados por vírgulas.

Durante os testes, o analisador léxico reconheceu corretamente todos os elementos do código. Entretanto, o parser rejeitou uma chamada de função ao encontrar a primeira vírgula entre os argumentos. A equipe precisa verificar se a falha está na sequência de tokens produzida ou nas regras da gramática e definir uma correção que não limite a quantidade de argumentos permitidos.

**DADOS DE SUPORTE**

Trecho de código analisado

```c
registrarVenda(cliente, total, 10);
```

Gramática utilizada pelo parser

```
<chamada>   → IDENTIFICADOR '(' <argumento> ')' ';'
<argumento> → IDENTIFICADOR | NUMERO
```

Sequência de tokens produzida pelo analisador léxico

| Lexema | Token produzido |
|---|---|
| registrarVenda | IDENTIFICADOR |
| ( | ABRE_PARENTESE |
| cliente | IDENTIFICADOR |
| , | VIRGULA |
| total | IDENTIFICADOR |
| , | VIRGULA |
| 10 | NUMERO |
| ) | FECHA_PARENTESE |
| ; | PONTO_E_VIRGULA |

_Fonte: elaboração própria, adaptada conceitualmente de GNU Project, "Bison 3.8.1 Manual", seções 3.3.1 – Syntax of Grammar Rules e 3.3.3 – Recursive Rules. https://www.gnu.org/software/bison/manual/html_node/Recursion.html_

**Considerando o trecho de código, a sequência de tokens e as produções da gramática, analise a causa do erro sintático e assinale a alternativa que identifica corretamente a limitação da gramática e apresenta uma alteração capaz de reconhecer chamadas com um ou mais argumentos separados por vírgulas.**

**Alternativas:**
- **A)** A sequência de tokens está inadequada porque as vírgulas deveriam ser descartadas pelo analisador léxico. Mantendo a produção de chamada inalterada, o parser poderia processar os argumentos consecutivos como uma única construção sintática.
- **B)** O erro ocorre porque a produção de chamada admite apenas um argumento. Deve-se introduzir uma lista recursiva, como `<lista> → <argumento> | <lista> ',' <argumento>`, e usar `<lista>` no interior dos parênteses da produção `<chamada>`.
- **C)** O erro ocorre porque a produção atual não prevê três argumentos. Deve-se substituir `<chamada>` por uma produção contendo exatamente três `<argumento>` separados por vírgulas, permitindo que o trecho apresentado seja reconhecido pelo parser.
- **D)** A gramática da chamada pode permanecer inalterada, desde que o parser aceite os tokens existentes entre parênteses e transfira à análise semântica a tarefa de separar os argumentos e verificar sua quantidade conforme a função utilizada.

**Gabarito: B** — _(origem: gabarito do próprio material, slide p. 10, "RESPOSTA B". O material explicativo, p. 2, trata A, C e D como distratores)_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Os tokens estão corretos (o enunciado diz que o léxico reconheceu tudo), e a vírgula é um separador sintático necessário. Descartá-la também não resolve: depois de `<argumento>` a produção espera `')'`, e o parser encontraria outro IDENTIFICADOR (`total`). A regra continua limitada a um argumento. (slide p. 10: "A remove uma vírgula que é separador sintático necessário"; material p. 2: "destrói separadores sintáticos vitais e mantém a regra restrita a um argumento")
- **B) ✅** — A limitação está na gramática: `<chamada>` deriva exatamente um `<argumento>`, por isso o parser falha na primeira VIRGULA. A correção é um não-terminal recursivo com caso-base (1 argumento) e passo recursivo (que amplia a lista), usado entre os parênteses: `<chamada> → IDENTIFICADOR '(' <lista> ')' ';'`. A derivação do teste fica: `<lista> ⇒ <lista> , <argumento> ⇒ <lista> , <argumento> , <argumento> ⇒ <argumento> , <argumento> , <argumento> ⇒ cliente , total , 10`. A gramática passa a aceitar 1, 2, 3, … argumentos sem limite artificial. (slide p. 10; material p. 2, "Solução Formal via Recursão")
- **C) ❌** — Uma produção com exatamente três argumentos só resolve aquele teste. Falha para 1, 2 ou 4 ou mais argumentos e contraria o requisito de "não limitar a quantidade". (slide p. 10; material p. 2)
- **D) ❌** — A rejeição ocorre na barreira sintática. Sem uma produção que derive a lista, o parser não tem como "aceitar os tokens existentes", e a análise semântica não substitui uma estrutura que falta na gramática. (slide p. 10: "a análise semântica não substitui uma estrutura ausente na gramática"; material p. 2)

**Diferenças entre versões:** O material explicativo não reproduz o enunciado nem as alternativas. Ele apresenta a mesma solução (`<lista> → <argumento> | <lista> ',' <argumento>` e `<chamada> → IDENTIFICADOR '(' <lista> ')' ';'`) e a chama de "Solução Formal via Recursão Esquerda/Direita", citando o GNU Bison. O slide de conceitos (p. 7) abrevia IDENTIFICADOR como `ID`. O gabarito (B) é o mesmo nas duas fontes.

**Conceito-chave para a prova:** Em uma GLC, uma lista de tamanho arbitrário exige um **não-terminal recursivo** com caso-base. Terminal é o símbolo da entrada (ID, NUMERO, vírgula, parênteses), não-terminal é uma categoria (`<chamada>`, `<lista>`) e produção é uma regra de formação. A recursão à esquerda (`<lista> → <lista> ',' <argumento>`) é a forma usual no Bison, que é LR. Se a prova falar em parser descendente (LL/recursivo), a recursão à esquerda precisa ser eliminada, e o equivalente é a recursão à direita: `<lista> → <argumento> | <argumento> ',' <lista>`.

---

## Q3 — Análise semântica: incompatibilidade de tipos
**Fonte:** `Compiladores_Roteiro_Oficial_23_Slides.pdf.pdf`: situação-problema e dados de suporte na p. 12 (imagem), comando e alternativas na p. 13 (imagem), correção na p. 14 e conceitos na p. 11. Também em `Material_Explicativo_Compiladores.pdf`, p. 3 ("Tema 3" e "Análise Crítica dos Distratores (Questão 3)").
**Tipo ENADE:** Resposta única (diagnóstico do erro + correção)

**Enunciado:**

**QUESTÃO 3 – ANÁLISE SEMÂNTICA**

Uma equipe de desenvolvimento está testando o compilador de uma linguagem estaticamente tipada utilizada em um sistema de automação comercial. O trecho abaixo foi aceito pelas etapas de análise léxica e sintática, mas a análise semântica identificou uma inconsistência na expressão atribuída à variável quantidade.

A linguagem não realiza conversão implícita entre texto e inteiro em operações aritméticas. Quando um valor textual representa um número e precisa participar de uma operação numérica, a especificação exige o uso explícito da função de conversão paraInteiro(texto). A equipe precisa diagnosticar a inconsistência e indicar uma correção compatível com essas regras.

**DADOS DE SUPORTE**

Trecho de código analisado

```
inteiro quantidade = 10;
texto produto = "25";
quantidade = produto - 5;
```

Tabela de símbolos

| Identificador | Tipo declarado |
|---|---|
| quantidade | inteiro |
| produto | texto |

Regras semânticas relevantes da linguagem
1. O operador de subtração (-) exige operandos do tipo inteiro.
2. Uma variável inteira só pode receber uma expressão cujo resultado seja inteiro.
3. A conversão de texto numérico para inteiro deve ser explícita por meio de paraInteiro(texto).

_Fonte: elaboração própria, adaptada conceitualmente de Oracle, Java Language Specification, Java SE 26, seções 5.2 (Assignment Contexts) e 15.18 (Additive Operators). https://docs.oracle.com/javase/specs/jls/se26/html/_

**Considerando o trecho de código, a tabela de símbolos e as regras semânticas apresentadas, analise a inconsistência e assinale a alternativa que identifica corretamente o erro e propõe uma correção que torne o trecho semanticamente válido.**

**Alternativas:**
- **A)** A inconsistência é lexical, pois o literal "25" contém apenas dígitos e deveria ser classificado como número mesmo entre aspas; reconhecendo-o como NUMERO, a operação com produto poderia ser mantida sem conversão adicional.
- **B)** A inconsistência é sintática, pois a gramática não deveria permitir a subtração entre um identificador textual e um número; acrescentando uma produção específica para texto - inteiro, a expressão passaria a ser semanticamente válida.
- **C)** A expressão pode ser mantida, pois o gerador de código deve detectar que o conteúdo de produto é numérico e realizar automaticamente a conversão para inteiro antes da subtração, preservando o tipo da variável de destino.
- **D)** A análise semântica deve rejeitar produto - 5 porque produto é texto e a subtração exige inteiros; para atender às regras, a expressão pode ser corrigida para quantidade = paraInteiro(produto) - 5, tornando os tipos compatíveis.

**Gabarito: D** — _(origem: gabarito do próprio material, slide p. 14, "RESPOSTA D". O material explicativo, p. 3, trata A, B e C como distratores)_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — `"25"` entre aspas é um literal de texto e continua sendo texto. Além disso, `produto` foi **declarada** como texto, e reclassificar o literal no léxico violaria essa declaração. O erro também não é léxico: o enunciado diz que as análises léxica e sintática aceitaram o trecho. (slide p. 14: "A — '25' entre aspas continua sendo texto"; material p. 3: "viola a declaração da variável como texto")
- **B) ❌** — O trecho é sintaticamente válido, e a gramática nem trabalha com tipos. Acrescentar uma produção "texto - inteiro" faria o parser aceitar a expressão, mas a incompatibilidade de tipos continuaria violando a regra 1. (slide p. 14: "B mudar a gramática não torna tipos incompatíveis válidos"; material p. 3: "resolve o parser, mas perpetua a falha de tipos na semântica")
- **C) ❌** — Uma conversão automática feita pelo gerador de código é coerção implícita, e isso contraria tanto a regra 3 quanto o enunciado ("a linguagem não realiza conversão implícita"). Além disso, a geração de código vem depois da análise semântica, que já deve ter rejeitado o trecho. (slide p. 14: "C conversão automática no gerador contraria a especificação"; material p. 3)
- **D) ✅** — Pela tabela de símbolos, `produto` é texto e `5` é inteiro. A subtração exige dois inteiros (regra 1), então a análise semântica rejeita `produto - 5`. Na correção `quantidade = paraInteiro(produto) - 5`, `paraInteiro(produto)` é inteiro, logo inteiro − inteiro = inteiro (regra 1). O resultado é atribuído a uma variável inteira (regra 2), e a conversão é explícita (regra 3). O valor final seria 20. (slide p. 14; material p. 3)

**Diferenças entre versões:** O material explicativo (p. 3) fala em "linguagens fortemente tipadas sem coerção implícita", enquanto o enunciado diz "linguagem estaticamente tipada" que "não realiza conversão implícita". Exemplo, correção e gabarito (D) são os mesmos. O slide de conceitos (p. 11) resume: "produto: texto · Subtração: inteiros · Conversão explícita: paraInteiro(produto) - 5".

**Conceito-chave para a prova:** Sintaxe correta não garante significado válido. A verificação de tipos, declarações e escopo é feita na **análise semântica**, com a tabela de símbolos (nomes, tipos, permissões). Em uma linguagem sem coerção implícita, a correção é a **conversão explícita**. O erro não está no léxico, no parser nem no gerador de código.

---

## Q4 — Geração de código: alocação de registradores e spill
**Fonte:** `Compiladores_Roteiro_Oficial_23_Slides.pdf.pdf`: situação-problema e dados de suporte na p. 16 (imagem), comando e alternativas na p. 17 (imagem), correção com tabela de simulação na p. 18 e conceitos na p. 15. Também em `Material_Explicativo_Compiladores.pdf`, p. 3 ("Tema 4", "Simulação Correta da Sequência (Alternativa B)" e "Análise Crítica dos Distratores (Questão 4)").
**Tipo ENADE:** Resposta única (avaliação/simulação de sequências de instruções)

**Enunciado:**

**QUESTÃO 4 – GERAÇÃO DE CÓDIGO**

Uma equipe está implementando o back-end de um compilador para um processador simples que dispõe de apenas dois registradores físicos de uso geral, R1 e R2. A representação intermediária do programa utiliza temporários virtuais sem essa limitação, mas a etapa de geração de código precisa produzir uma sequência válida para a arquitetura de destino.

Durante a tradução, os dois resultados intermediários t1 e t2 precisam ser preservados até a multiplicação final. Como não há registradores físicos suficientes para manter simultaneamente todos os valores necessários, a arquitetura permite armazenar temporariamente um valor na posição de memória TEMP.

**DADOS DE SUPORTE**

Representação intermediária

```
t1 = a + b
t2 = c + d
t3 = t1 * t2
resultado = t3
```

Instruções disponíveis na arquitetura

| Instrução | Efeito |
|---|---|
| LOAD Rn, X | Rn <- valor de X |
| STORE X, Rn | X <- valor de Rn |
| ADD Rd, Rs | Rd <- Rd + Rs |
| MUL Rd, Rs | Rd <- Rd * Rs |

Restrições: somente R1 e R2 existem como registradores físicos; qualquer uso de R3 é inválido. A posição TEMP pode ser utilizada para spill temporário em memória.

_Fonte: elaboração própria, adaptada conceitualmente de LLVM Project, "The LLVM Target-Independent Code Generator", seções Instruction Selection e Register Allocation. https://llvm.org/docs/CodeGenerator.html_

**Considerando a representação intermediária, o conjunto de instruções e as restrições da arquitetura, avalie as estratégias abaixo e assinale a sequência que preserva corretamente a semântica do programa e utiliza apenas os recursos disponíveis no processador.**

**Alternativas:**
- **A)** LOAD R1,a; LOAD R2,b; ADD R1,R2; LOAD R3,c; LOAD R2,d; ADD R3,R2; MUL R1,R3; STORE resultado,R1. A sequência preserva t1 e t2 em registradores e evita acesso temporário à memória.
- **B)** LOAD R1,a; LOAD R2,b; ADD R1,R2; STORE TEMP,R1; LOAD R1,c; LOAD R2,d; ADD R1,R2; LOAD R2,TEMP; MUL R2,R1; STORE resultado,R2. A sequência usa TEMP para preservar t1 e respeita os dois registradores disponíveis.
- **C)** LOAD R1,a; LOAD R2,b; ADD R1,R2; STORE TEMP,R1; LOAD R2,TEMP; LOAD R1,c; LOAD R2,d; ADD R1,R2; MUL R2,R1; STORE resultado,R2. A sequência realiza spill, mas reutiliza R2 antes da multiplicação final.
- **D)** LOAD R1,a; LOAD R2,b; ADD R1,R2; STORE TEMP,R1; LOAD R1,c; LOAD R2,d; ADD R1,R2; LOAD R2,TEMP; ADD R2,R1; STORE resultado,R2. A sequência respeita os registradores e combina os dois resultados intermediários ao final.

**Gabarito: B** — _(origem: gabarito do próprio material, slide p. 18, "Alternativa B · simulação de R1, R2 e TEMP", e material explicativo p. 3, "Simulação Correta da Sequência (Alternativa B)")_

Simulação da alternativa B, reproduzida do slide p. 18:

| Passo | Instrução | R1 | R2 | TEMP |
|---|---|---|---|---|
| 1 | LOAD R1, a | a | — | — |
| 2 | LOAD R2, b | a | b | — |
| 3 | ADD R1, R2 | t1 = a + b | b | — |
| 4 | STORE TEMP, R1 | t1 | b | t1 (spill) |
| 5 | LOAD R1, c | c | b | t1 |
| 6 | LOAD R2, d | c | d | t1 |
| 7 | ADD R1, R2 | t2 = c + d | d | t1 |
| 8 | LOAD R2, TEMP | t2 | t1 | t1 |
| 9 | MUL R2, R1 | t2 | t3 = t1 * t2 | t1 |
| 10 | STORE resultado, R2 | t2 | t3 | t1 |

_(Slide: "Passo 4: spill · Passo 8: reload · Passo 9: multiplicação · R3 nunca pode ser usado")_

**Por que cada alternativa está certa ou errada:** (conferido em python3 com a=2, b=3, c=5, d=7, cujo resultado esperado é (a+b)·(c+d) = 60)
- **A) ❌** — Usa R3, e a restrição diz que "qualquer uso de R3 é inválido". O valor calculado seria 60, mas o código não roda na arquitetura de destino. O "evita acesso à memória" é justamente o atrativo do distrator. (slide p. 18: "R3 nunca pode ser usado"; material p. 3: "viola a restrição física de que apenas R1 e R2 existem")
- **B) ✅** — Calcula t1 em R1, faz o spill de t1 para TEMP, reaproveita R1 e R2 para calcular t2 em R1, recarrega t1 de TEMP para R2 (reload) e multiplica: R2 ← t1 · t2. Resultado: 60. Usa apenas R1, R2 e TEMP e preserva a semântica `resultado = (a+b)*(c+d)`.
- **C) ❌** — Faz o spill, mas recarrega t1 em R2 **cedo demais** (logo após o STORE), e o `LOAD R2,d` seguinte sobrescreve esse valor. No MUL, R2 contém `d`, então resultado = d·(c+d) = 7·12 = **84** ≠ 60. (material p. 3: "Sobrescreve incorretamente o registrador recuperado antes da multiplicação"; a própria alternativa admite que "reutiliza R2 antes da multiplicação final". O slide de conceitos p. 15 define liveness como "valor ainda necessário em uma operação futura", e t1 recarregado em R2 ainda estava vivo)
- **D) ❌** — A sequência de spill e reload está certa, mas a combinação final usa `ADD R2,R1` em vez de `MUL`. O resultado vira (a+b)+(c+d) = **17** ≠ 60, o que altera a semântica do programa. (material p. 3: "Utiliza a instrução ADD em vez de MUL na combinação final")

**Diferenças entre versões:** O material explicativo (p. 3) mostra a mesma sequência da alternativa B agrupada em 6 passos ("1. LOAD R1, a; LOAD R2, b; ADD R1, R2 (Calcula t1 em R1); 2. STORE TEMP, R1 (spill); 3. LOAD R1, c; LOAD R2, d; ADD R1, R2 (Calcula t2 em R1); 4. LOAD R2, TEMP (Recupera t1 para R2); 5. MUL R2, R1; 6. STORE resultado, R2"). O slide p. 18 mostra a mesma sequência em 10 passos, com o estado de R1/R2/TEMP. Não há divergência.

**Conceito-chave para a prova:** A IR usa temporários virtuais ilimitados (t1, t2, …), enquanto o processador tem poucos registradores físicos. Quando os valores **vivos** (liveness: ainda necessários em uma operação futura) superam os registradores, o compilador faz **spill** (STORE em memória) e depois **reload** (LOAD) imediatamente antes do uso. Na prova, confira três pontos: (1) se a sequência só usa os registradores existentes; (2) se nenhum valor vivo é sobrescrito antes do uso; (3) se a operação final é a da IR (MUL, não ADD).

---

## Q5 — Ambiguidade, precedência e associatividade (Bison)
**Fonte:** `Compiladores_Roteiro_Oficial_23_Slides.pdf.pdf`: situação-problema e dados de suporte na p. 20 (imagem), comando e alternativas na p. 21 (imagem), correção na p. 22 e conceitos na p. 19. Também em `Material_Explicativo_Compiladores.pdf`, p. 4 ("Tema 5" e "Análise Crítica dos Distratores (Questão 5)").
**Tipo ENADE:** Resposta única (identificação de ambiguidade + interpretação + configuração do parser)

**Enunciado:**

**QUESTÃO 5 – AMBIGUIDADE, PRECEDÊNCIA E ASSOCIATIVIDADE**

Uma equipe está desenvolvendo o parser de uma linguagem para expressões aritméticas. Durante a geração do analisador sintático, a gramática abaixo produz conflitos porque uma mesma expressão pode admitir diferentes árvores sintáticas. O problema tornou-se evidente ao testar a expressão a + b * c - d.

A especificação da linguagem estabelece que multiplicação possui precedência maior que adição e subtração, enquanto adição e subtração têm a mesma precedência e são associativas à esquerda. A equipe precisa escolher a interpretação correta e uma estratégia de configuração do parser que elimine o conflito de acordo com essas regras.

**DADOS DE SUPORTE**

Gramática utilizada

```
expr -> expr '+' expr
      | expr '-' expr
      | expr '*' expr
      | ID
```

Precedência e associatividade definidas pela linguagem

| Operadores | Precedência | Associatividade |
|---|---|---|
| + - | menor | esquerda |
| * | maior | esquerda |

Interpretações possíveis para a expressão

I. ((a + b) * c) - d
II. (a + (b * c)) - d
III. a + (b * (c - d))

_Fonte: elaboração própria, adaptada conceitualmente de GNU Project, "Bison 3.8.1 Manual", seções 5.3.2 – Specifying Operator Precedence, 5.3.3 – Specifying Precedence Only e 5.3.4 – Precedence Examples. https://www.gnu.org/software/bison/manual/_

**Considerando a gramática, as regras de precedência e associatividade e as interpretações apresentadas, avalie o conflito e assinale a alternativa que identifica corretamente a ambiguidade, seleciona a interpretação prevista pela linguagem e apresenta uma estratégia adequada para configurar o parser.**

**Alternativas:**
- **A)** A gramática é ambígua e a interpretação I deve ser escolhida, pois a associatividade à esquerda determina a redução de todos os operadores na ordem em que aparecem; declarar `%left '+' '-' '*'` em um único nível resolve o conflito.
- **B)** A gramática não é ambígua, pois a ordem dos operadores na cadeia de entrada determina uma única derivação; a interpretação II surge automaticamente e, por isso, não é necessário declarar precedência nem associatividade no gerador do parser.
- **C)** A gramática é ambígua e a interpretação II deve prevalecer; no Bison, pode-se declarar `%left '+' '-'` e, em uma declaração posterior, `%left '*'`, atribuindo maior precedência à multiplicação e associatividade à esquerda.
- **D)** A gramática é ambígua e a interpretação III deve prevalecer, pois a multiplicação deve incorporar toda a expressão à sua direita; declarar `%right '+' '-'` antes de `%left '*'` garante essa associação e elimina os conflitos.

**Gabarito: C** — _(origem: gabarito do próprio material, slide p. 22, "Alternativa C · multiplicação com precedência maior". O material explicativo, p. 4, trata A, B e D como distratores e diz que a configuração "garante que a expressão seja interpretada corretamente como (a + (b * c)) - d (Interpretação II)")_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — A gramática é mesmo ambígua, mas colocar `+`, `-` e `*` no mesmo nível `%left` iguala as prioridades e força a leitura estritamente da esquerda para a direita: ((a + b) * c) - d, que é a interpretação I. Isso remove os conflitos do Bison, mas com a semântica errada, porque contraria a regra de que `*` tem precedência maior. (slide p. 22: "A mesmo nível para +, - e *"; material p. 4)
- **B) ❌** — A gramática **é** ambígua: a mesma cadeia admite mais de uma árvore (I, II e III são todas deriváveis por `expr → expr op expr`). A ordem dos tokens não elimina a ambiguidade, e sem declarações de precedência o Bison reporta conflitos shift/reduce. (slide p. 22: "B ordem dos tokens não elimina a ambiguidade"; material p. 4)
- **C) ✅** — A gramática é ambígua. Pela especificação, `*` agrupa primeiro: `a + (b * c)`. Depois, `+` e `-` estão no mesmo nível e associam à esquerda: `(a + (b * c)) - d`, a interpretação II. No Bison, cada linha `%left`/`%right` é um nível, e **declarações posteriores têm maior precedência**: `%left '+' '-'` seguido de `%left '*'` dá a `*` precedência maior, com todos associativos à esquerda. (slide p. 22; material p. 4)
- **D) ❌** — A interpretação III, a + (b * (c - d)), exigiria `-` agrupando antes de `*` e associação à direita, o que contraria a especificação (`*` > `-`, associatividade à esquerda). Além disso, a configuração proposta é incoerente com a própria alternativa: `%right '+' '-'` antes de `%left '*'` ainda daria `*` como maior precedência e produziria `a + ((b * c) - d)`, que não é a III. (slide p. 22: "D interpretação III + associatividade à direita contrariam as regras"; material p. 4)

**Diferenças entre versões:** O material explicativo (p. 4) usa a mesma expressão, a mesma configuração (`%left '+' '-'` / `%left '*'`) e a mesma interpretação II, e descreve o distrator B como "Supor que a gramática não é ambígua ignora o fato de que produções genéricas geram múltiplos conflitos estruturais". O slide de conceitos (p. 19) traz o exemplo de associatividade `a - b - c → (a - b) - c` e "* antes de +". Não há divergência de gabarito.

**Conceito-chave para a prova:** Uma gramática é ambígua quando há duas ou mais árvores sintáticas para a mesma cadeia. A **precedência** decide entre operadores diferentes (`*` antes de `+`), e a **associatividade** decide no mesmo nível (`a - b - c = (a - b) - c` com `%left`). No Bison/Yacc, operadores na mesma linha têm a mesma precedência, e a linha declarada **depois** tem precedência **maior**. Essas diretivas resolvem os conflitos shift/reduce sem reescrever a gramática em níveis (a alternativa clássica é `expr → expr + termo | termo; termo → termo * fator | fator`).
