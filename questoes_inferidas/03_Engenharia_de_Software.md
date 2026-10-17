# Engenharia de Software — Questões INFERIDAS (prováveis questões do banco do squad que não temos)

> ⚠️ **Atenção:** estas questões NÃO constam nos materiais. Foram elaboradas para cobrir os subtópicos do material do
> Squad 8 que não têm questão conhecida, imitando o estilo das questões do squad. Servem para estudo dirigido.
> As questões reais conhecidas estão em `../questoes_por_topico/03_Engenharia_de_Software.md`.

**Base usada:**
- `APOSTILA DE ESTUDO PARA O ENADE SOBRE ENGENHARIA DE SOFTWARE.pdf` (106 p.): sumário na p. 2 com 7 módulos e 32 subseções (1.1 a 7.5). Li todas as páginas. As páginas-imagem 6 (tabela RF × RNF), 28 (mapa mental das técnicas de elicitação), 42 (gráfico "Fases do RUP"), 66 (modelo V), 89–90 e 95–96 (tabelas de símbolos) foram renderizadas e lidas.
- `ENGENHARIA DE SOFTWARE.pdf` (slides, 106 p.): índice na p. 3 com 4 blocos (Metodologia Ágil, Fluxo de Software, Elicitação de Requisitos, UML). Li todas as páginas. Renderizei as p. 26 (fases do Cascata), 43 (hierarquia da ISO/IEC 25010:2023), 77 (fragmentos alt/opt/loop) e 95 (interfaces fornecida/necessária).
- Questões conhecidas: Q1–Q4 (slides p. 19, 35, 53 e 103), exercício Q5 (slides p. 61) e QP (exemplo do professor sobre o padrão Observer).

**Estilo identificado do squad (copiado nas inferidas):**
- **5 alternativas (A–E)** em todas as questões.
- O enunciado é um parágrafo corrido de situação-problema (empresa/equipe/sistema fictício, às vezes com nomes de pessoas), seguido dos dados (afirmativas, asserções, lista de cenários) e de um comando curto. O squad **não** escreve os rótulos "Situação-problema / Dados de suporte / Comando"; por isso as inferidas também não usam esses rótulos.
- Tipos usados pelo squad: resposta única com "respectivamente" (Q1), afirmativas I–III e I–IV com "É correto o que se afirma em" (Q2 e Q4) e asserção-razão com "PORQUE" e as 5 alternativas padrão do ENADE (Q3). Para variar, como pede o guia do professor, as inferidas também usam associação, ordenação, lacunas, afirmativa negativa (INCORRETA) e cálculo (valor-limite).
- Os distratores do squad trocam papéis/conceitos vizinhos (PO × SM, include × extend, generalização × associação, ator humano × sistema externo). As inferidas seguem a mesma lógica, usando as confusões que o próprio material deixa possíveis.

## Mapa de cobertura
| # | Subtópico (material) | Páginas | Questão conhecida | Questão inferida | Prioridade |
|---|---|---|---|---|---|
| 1 | 1.1 Requisitos funcionais e não funcionais (tipos, RNF mensuráveis, tabela RF × RNF) | Apostila p. 3–7; slides p. 41–42 | **Q3** (asserção-razão RNF) | — _(variação provável: lista de requisitos para classificar em RF/RNF, ou RNF de produto/organizacional/externo, p. 5)_ | — |
| 2 | 1.1 (cont.) As 5 etapas da análise de requisitos e a documentação na prática | Apostila p. 8–13 | — | I1 | Média |
| 3 | 1.2 Stakeholders | Apostila p. 13–14 | — | I2 | Média |
| 4 | 1.3 Princípios da Engenharia de Requisitos (9 princípios do IREB) | Apostila p. 14–19 | — | I3 | Alta |
| 5 | 1.4 Especificação, validação, gerenciamento de mudanças (CCB) e rastreabilidade | Apostila p. 20–22 | — | I4 | Alta |
| 6 | 2.1 Técnicas de elicitação (tradicionais, de grupo, prototipação, cognitivas, contextuais) | Apostila p. 23–28; slides p. 37–40 | — | I5, I6 | Alta |
| 7 | 2.2 UML: o que é, 14 diagramas, estruturais × comportamentais, modelos funcional/objeto/dinâmico | Apostila p. 29–33; slides p. 55–57 | — | I7 | Alta |
| 8 | ISO/IEC 25010:2023, 9 características de qualidade (só nos slides) | Slides p. 41, 43–52 | — _(Q3 só cita a norma)_ | I8, I9 | Alta |
| 9 | 3.1 Fluxos de software (linear, iterativo, evolucionário, paralelo) | Apostila p. 34–35; slides p. 22–23 | **Q2** (parcial: só o evolucionário) | I10 (fluxo paralelo) | Média |
| 10 | 3.2 Modelos de processo (Cascata, Incremental, Prototipação, Espiral, Reuso) | Apostila p. 35–39; slides p. 24–33 | **Q2** (parcial: Cascata e Prototipação) | I10 (Incremental, Espiral, Reuso) | Média |
| 11 | 3.3 RUP | Apostila p. 40–42; slides p. 34 | — | I11 | Alta |
| 12 | 4.1 Metodologia Ágil × fluxo tradicional | Apostila p. 43–44; slides p. 5–6 | — | I12 | Média |
| 13 | 4.2 Frameworks e práticas ágeis (Kanban, Lean, Scrum, Scrumban, XP, TDD, FDD, ASD, SAFe) | Apostila p. 44–45; slides p. 7–15 | — | I13, I14 | Alta |
| 14 | 4.3 Scrum e seus papéis | Apostila p. 46; slides p. 9, 16 | **Q1** | — _(variação provável: descrições trocadas entre as pessoas; papel dos Desenvolvedores auto-organizados)_ | — |
| 15 | 4.4 PMBOK (não é metodologia; 6 princípios da 8ª ed.) | Apostila p. 47–48; slides p. 17–18 | — | I15 | Alta |
| 16 | 5.1 POO: abstração, encapsulamento, herança e polimorfismo | Apostila p. 49–54 | — | I16 | Média |
| 17 | 5.2 SOLID | Apostila p. 55–57 | — | I17, I18 | Alta |
| 18 | 5.3 Arquitetura em camadas | Apostila p. 57–59 | — | I19 | Média |
| 19 | 5.4 Cliente-servidor e microsserviços | Apostila p. 59–61 | — | I20 | Média |
| 20 | 5.5 Design Patterns e GoF | Apostila p. 62–63 | **QP** (parcial: exemplo do professor sobre o Observer, não é do squad) | I21 | Média |
| 21 | 5.6 ADR e análise de trade-offs | Apostila p. 64–65 | — | I22 | Média |
| 22 | 6.1 Verificação × validação | Apostila p. 66–68 | — | I23 | Alta |
| 23 | 6.2 Testes unitários, de integração, de sistema e de aceitação | Apostila p. 68–70 | — | I24 | Alta |
| 24 | 6.3 Caixa-preta, caixa-branca e caixa-cinza | Apostila p. 70–73 | — | I25, I26 | Alta |
| 25 | 6.4 Casos de teste + 6.5 Testes automatizados _(agrupados: cerca de 1 página cada)_ | Apostila p. 74–76 | — | I27 | Média |
| 26 | 6.6 Defeitos e rastreamento (ciclo de vida, severidade × prioridade, bug report) | Apostila p. 76–77 | — | I28, I29 | Alta |
| 27 | 7.1 Diagrama de casos de uso | Apostila p. 78–80; slides p. 58–61 | **Q4, Q5** | — _(variação provável: seta do include/extend; caixa de limite do sistema; pacote)_ | — |
| 28 | 7.2 Diagrama de classes (seções, visibilidade, escopo, herança, associações, multiplicidade) | Apostila p. 81–86; slides p. 62–69 | — | I30, I31 | Alta |
| 29 | 7.3 Diagrama de sequência (símbolos, mensagens, fragmentos, DSS) | Apostila p. 87–92; slides p. 70–78 | — | I32, I33 | Alta |
| 30 | Diagrama de atividades (só nos slides; a apostila só o cita em 2.2) | Slides p. 79–87; apostila p. 31 | — | I34 | Alta |
| 31 | 7.4 Diagrama de componentes | Apostila p. 93–98; slides p. 88–96 | — | I35 | Média |
| 32 | 7.5 Diagrama de implementação (implantação) | Apostila p. 98–103; slides p. 97–102 | — | I36 | Média |

**Resumo:** 32 subtópicos. 3 estão cobertos por questões conhecidas (1.1 RF/RNF por Q3, 4.3 Scrum por Q1 e 7.1 casos de uso por Q4/Q5). Outros 3 têm só cobertura parcial (3.1 e 3.2 por Q2; 5.5 pela QP do professor). As inferidas cobrem a parte que falta deles. **36 questões inferidas** cobrem os 29 subtópicos restantes. Recebem 2 questões os subtópicos que o material mais enfatiza: elicitação, ISO 25010, frameworks ágeis, SOLID, caixa-preta/branca, defeitos, diagrama de classes e diagrama de sequência.

**Critério de prioridade:** **Alta** = o tema está nos slides (de onde saíram as 4 questões conhecidas) ou tem tabela comparativa/exemplo resolvido na apostila. **Média** = o tema aparece só na apostila, sem destaque especial.

**Distribuição dos gabaritos:** A = 7 · B = 7 · C = 7 · D = 8 · E = 7.

## Índice
1. [I1 — Etapas da análise de requisitos (ordenação)](#i1--etapas-da-análise-de-requisitos)
2. [I2 — Stakeholders](#i2--stakeholders)
3. [I3 — Princípios da Engenharia de Requisitos (IREB)](#i3--princípios-da-engenharia-de-requisitos-ireb)
4. [I4 — Especificação, validação, mudanças e rastreabilidade](#i4--especificação-validação-mudanças-e-rastreabilidade)
5. [I5 — Técnicas de elicitação e suas categorias](#i5--técnicas-de-elicitação-e-suas-categorias)
6. [I6 — Detalhes das técnicas de elicitação (INCORRETA)](#i6--detalhes-das-técnicas-de-elicitação)
7. [I7 — UML: visão geral e tipos de diagramas](#i7--uml-visão-geral-e-tipos-de-diagramas)
8. [I8 — ISO/IEC 25010:2023: classificação de requisitos](#i8--isoiec-250102023-classificação-de-requisitos)
9. [I9 — ISO/IEC 25010:2023: Safety × Security](#i9--isoiec-250102023-safety--security)
10. [I10 — Modelos de processo e fluxo paralelo](#i10--modelos-de-processo-e-fluxo-paralelo)
11. [I11 — Fases do RUP](#i11--fases-do-rup)
12. [I12 — Ágil × tradicional](#i12--ágil--tradicional)
13. [I13 — Frameworks ágeis](#i13--frameworks-ágeis)
14. [I14 — TDD e XP](#i14--tdd-e-xp)
15. [I15 — PMBOK: princípios da 8ª edição](#i15--pmbok-princípios-da-8ª-edição)
16. [I16 — Pilares da POO](#i16--pilares-da-poo)
17. [I17 — SOLID: identificação dos princípios](#i17--solid-identificação-dos-princípios)
18. [I18 — SOLID: inversão de dependência em código](#i18--solid-inversão-de-dependência-em-código)
19. [I19 — Arquitetura em camadas](#i19--arquitetura-em-camadas)
20. [I20 — Cliente-servidor e microsserviços](#i20--cliente-servidor-e-microsserviços)
21. [I21 — Padrões GoF: famílias e exemplos](#i21--padrões-gof-famílias-e-exemplos)
22. [I22 — ADR e trade-offs](#i22--adr-e-trade-offs)
23. [I23 — Verificação × validação](#i23--verificação--validação)
24. [I24 — Níveis de teste](#i24--níveis-de-teste)
25. [I25 — Particionamento por equivalência e valor-limite](#i25--particionamento-por-equivalência-e-valor-limite)
26. [I26 — Caixa-branca, caixa-preta e caixa-cinza](#i26--caixa-branca-caixa-preta-e-caixa-cinza)
27. [I27 — Casos de teste e testes automatizados](#i27--casos-de-teste-e-testes-automatizados)
28. [I28 — Severidade × prioridade de defeitos](#i28--severidade--prioridade-de-defeitos)
29. [I29 — Ciclo de vida do defeito (ordenação)](#i29--ciclo-de-vida-do-defeito)
30. [I30 — Diagrama de classes: visibilidade e escopo (lacunas)](#i30--diagrama-de-classes-visibilidade-e-escopo)
31. [I31 — Diagrama de classes: herança e multiplicidade](#i31--diagrama-de-classes-herança-e-multiplicidade)
32. [I32 — Diagrama de sequência: fragmentos alt, opt e loop](#i32--diagrama-de-sequência-fragmentos-alt-opt-e-loop)
33. [I33 — Diagrama de sequência: símbolos e DSS](#i33--diagrama-de-sequência-símbolos-e-dss)
34. [I34 — Diagrama de atividades](#i34--diagrama-de-atividades)
35. [I35 — Diagrama de componentes](#i35--diagrama-de-componentes)
36. [I36 — Diagrama de implementação](#i36--diagrama-de-implementação)

---

## I1 — Etapas da análise de requisitos
**Subtópico coberto:** 1.1, "Quais são as 5 etapas da análise de requisitos?" (apostila p. 8–12)
**Por que é provável:** a apostila numera as 5 etapas em ordem (levantamento, documentação, validação, gerenciamento, verificação e aprovação) e descreve cada uma com técnicas e ferramentas. Lista numerada assim costuma virar questão de ordenação.
**Prioridade:** Média
**Tipo ENADE:** Ordenação

**Enunciado:**
Uma software house foi contratada por uma rede de clínicas para desenvolver um sistema de agendamento de consultas. Para reduzir o retrabalho, o gerente do projeto organizou a análise de requisitos nas cinco etapas fundamentais descritas pela Engenharia de Software. As atividades realizadas pela equipe estão listadas abaixo, fora de ordem:

1. Revisão final dos requisitos e aprovação formal pelos stakeholders, para garantir que tudo está correto, completo e alinhado às expectativas antes do início do desenvolvimento.
2. Entrevistas com recepcionistas e médicos, workshops com a diretoria e observação do uso da agenda de papel nas recepções.
3. Controle das alterações solicitadas ao longo do projeto: cada mudança é registrada, avaliada e aprovada antes de ser adotada, com rastreabilidade no Jira.
4. Elaboração do documento de requisitos de software (SRS) e de diagramas e modelos que descrevem os requisitos funcionais e não funcionais.
5. Revisões das especificações com os Tech Leads e protótipos no Figma para que os usuários confirmem se o que foi documentado está correto, completo e compreendido por todos.

Assinale a alternativa que apresenta a sequência correta dessas atividades, conforme as cinco etapas da análise de requisitos.

**Alternativas:**
- **A)** 2 – 5 – 4 – 1 – 3
- **B)** 4 – 2 – 5 – 3 – 1
- **C)** 2 – 4 – 3 – 5 – 1
- **D)** 2 – 4 – 5 – 3 – 1
- **E)** 1 – 2 – 4 – 5 – 3

**Gabarito: D**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Coloca a validação (5) antes da documentação (4). Não dá para validar uma especificação que ainda não foi escrita. Também inverte gerenciamento e aprovação.
- **B) ❌** — Começa pela documentação (4). Sem levantamento não há o que documentar.
- **C) ❌** — Põe o gerenciamento de mudanças (3) antes da validação (5). Na apostila, a validação é a 3ª etapa e o gerenciamento é a 4ª.
- **D) ✅** — Levantamento (2) → Documentação (4) → Validação (5) → Gerenciamento (3) → Verificação e aprovação (1). É exatamente a ordem numerada da apostila (p. 8).
- **E) ❌** — Põe a aprovação formal no início. Na apostila ela é a última etapa, a revisão final antes de desenvolver.

**Base no material:** p. 8 ("1. Levantamento; 2. Documentação; 3. Validação; 4. Gerenciamento; 5. Verificação e aprovação"). As técnicas vêm das p. 8–12: entrevistas, workshops, questionários e observação; SRS/FSD, diagramas e modelos; revisões, prototipagem (Figma, Adobe XD) e simulações; controle de mudanças com Jira, Azure DevOps e IBM DOORS; revisão final e aprovação formal.
**Conceito-chave para a prova:** ordem **L-D-V-G-V/A**. Não confunda **validação** (3ª etapa: requisitos corretos, completos e compreendidos, via revisões e protótipos) com **verificação e aprovação** (5ª etapa: revisão final e assinatura). A apostila também traz um segundo roteiro prático (p. 12–13): Concepção → Elicitação → Elaboração → Negociação (MVP) → Especificação → Validação (cliente assina o escopo) → Gerenciamento. Uma versão alterada da questão pode usar esse roteiro.
**⚠️ Atenção:** a apostila põe o "gerenciamento" (contínuo) antes da "verificação e aprovação" (que ocorre "antes de iniciar o desenvolvimento"). A ordem cobrada é a da numeração do material, não uma cronologia rigorosa.

---

## I2 — Stakeholders
**Subtópico coberto:** 1.2, Stakeholders e seu impacto (apostila p. 13–14)
**Por que é provável:** a seção traz uma classificação em 4 categorias (internos, externos, primários, secundários) e 3 abordagens de identificação. Esse tipo de lista vira afirmativas facilmente.
**Prioridade:** Média
**Tipo ENADE:** Afirmativas múltiplas (I–IV)

**Enunciado:**
Uma fintech iniciou o desenvolvimento de um aplicativo de empréstimos. Na primeira semana, a gerente de projetos Carla reuniu a equipe para identificar as partes interessadas: os desenvolvedores, o gerente de produto e a diretora de tecnologia da empresa; os clientes que usarão o aplicativo; a empresa fornecedora do gateway de pagamentos; os acionistas; e o diretor financeiro, que aprova o orçamento e pode cancelar o projeto. Com base nos conceitos de stakeholders, avalie as afirmações a seguir.

I. Os desenvolvedores, o gerente de produto e a diretora de tecnologia são stakeholders internos, pois são funcionários, gerentes e diretores envolvidos diretamente no projeto.

II. Os clientes do aplicativo, o fornecedor do gateway de pagamentos e os acionistas são exemplos de stakeholders externos.

III. O diretor financeiro deve ser classificado como stakeholder secundário, pois os stakeholders secundários são aqueles que têm influência direta sobre os resultados do projeto.

IV. O mapeamento de stakeholders, que reúne e classifica as partes interessadas em um diagrama, e a análise de influência, que as classifica pelo nível de influência e de interesse no projeto, são abordagens para identificar os stakeholders.

É correto o que se afirma em:

**Julgamento das afirmativas:**
- **I — Verdadeira.** Definição literal de stakeholders internos (p. 13).
- **II — Verdadeira.** A apostila lista como externos "clientes, fornecedores, acionistas e a comunidade em geral" (p. 13).
- **III — Falsa.** Quem tem **influência direta** sobre os resultados é o stakeholder **primário**. O **secundário** tem interesse **indireto**. O diretor que aprova o orçamento e pode cancelar o projeto é primário.
- **IV — Verdadeira.** Mapeamento, análise de influência e entrevistas/feedback são as 3 abordagens de identificação (p. 14).

**Alternativas:**
- **A)** I e II, apenas.
- **B)** II e III, apenas.
- **C)** I, II e IV, apenas.
- **D)** I, III e IV, apenas.
- **E)** I, II, III e IV.

**Gabarito: C**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Omite a IV, que também é verdadeira.
- **B) ❌** — Inclui a III (falsa) e omite I e IV.
- **C) ✅** — I, II e IV são verdadeiras. A III troca primário por secundário.
- **D) ❌** — Inclui a III e omite a II. Acionistas são externos, segundo o material.
- **E) ❌** — A III é falsa.

**Base no material:** p. 13: "Stakeholders primários: aqueles que têm uma influência direta... Stakeholders secundários: aqueles que têm um interesse indireto". p. 14: mapeamento, análise de influência, entrevistas e feedback.
**Conceito-chave para a prova:** **interno × externo** depende de a pessoa estar dentro ou fora da organização. **Primário × secundário** depende de a influência ser direta ou o interesse ser indireto. Os critérios são independentes: um cliente pode ser externo **e** primário. Pegadinha provável: acionista é **externo** na apostila.

---

## I3 — Princípios da Engenharia de Requisitos (IREB)
**Subtópico coberto:** 1.3, os 9 princípios fundamentais da ER segundo o IREB/CPRE (apostila p. 14–19)
**Por que é provável:** são 5 páginas com 9 princípios, cada um com exemplo concreto (zoom × colunas colapsadas; "falso entendimento"; custo 10 a 100 vezes maior). É a seção mais longa do Módulo 1.
**Prioridade:** Alta
**Tipo ENADE:** Associação

**Enunciado:**
Em um projeto de modernização do sistema de gestão de uma rede de hospitais, o engenheiro de requisitos registrou as quatro situações a seguir:

I. A equipe estimou que o requisito "exportar relatórios em 12 formatos diferentes" exigiria grande esforço para ser elicitado, validado, documentado e gerenciado, mas traria benefício mínimo aos usuários, e decidiu não investir nele.

II. Os médicos pediram botões de zoom para um relatório que não cabia na tela do tablet. O analista, em vez de apenas registrar o pedido, propôs eliminar e colapsar colunas e otimizar a interação para o dispositivo.

III. Uma versão anterior do sistema funcionava tecnicamente, mas falhou em produção porque não considerou as normas sanitárias vigentes nem os sistemas legados de laboratório com os quais precisava se integrar.

IV. Na homologação, descobriu-se que diretoria, faturamento e equipe técnica acreditavam ter a mesma visão sobre o termo "paciente ativo", mas cada grupo o interpretava de forma diferente.

Associe cada situação ao princípio da Engenharia de Requisitos (IREB) que ela melhor exemplifica:

1. Orientação para o valor
2. Entendimento comum
3. Contexto
4. Inovação

Assinale a alternativa que apresenta a associação correta.

**Alternativas:**
- **A)** I-1, II-2, III-3, IV-4.
- **B)** I-1, II-4, III-3, IV-2.
- **C)** I-4, II-1, III-2, IV-3.
- **D)** I-3, II-4, III-1, IV-2.
- **E)** I-1, II-3, III-4, IV-2.

**Gabarito: B**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Associação "em ordem" que ninguém justifica: zoom × colunas não é entendimento comum, e "paciente ativo" não é inovação.
- **B) ✅** — **I-1:** valor = benefício − custo; requisito de baixo benefício e alto custo não deve receber investimento (p. 15). **II-4:** é o exemplo literal de inovação em **pequena escala** (p. 19); o engenheiro de requisitos não é um "gravador de voz". **III-3:** ignorar o ambiente social/legal e o técnico (sistemas existentes) gera "sistemas que funcionam tecnicamente, mas falham em se integrar ao ambiente" (p. 16–17). **IV-2:** é o **"falso entendimento"**, um dos maiores desafios do princípio do entendimento comum (p. 16).
- **C) ❌** — Troca todas as associações.
- **D) ❌** — Associa a falha de integração com normas e legado (III) a "valor" e a decisão de custo-benefício (I) a "contexto".
- **E) ❌** — Associa o zoom a "contexto" e a falha de integração a "inovação".

**Base no material:** p. 15 ("O valor de um requisito é definido como seu benefício menos seu custo"); p. 16 ("O risco do 'falso entendimento'..."); p. 16–17 (contexto organizacional, técnico, social e legal); p. 18–19 (inovação: "não são meros 'gravadores de voz'"; exemplo do zoom).
**Conceito-chave para a prova:** os 9 princípios são **Valor, Stakeholders, Entendimento comum, Contexto, Problema-requisito-solução, Validação, Evolução, Inovação e Trabalho sistemático**. Frases que caem: corrigir um requisito errado na implementação/operação custa **10 a 100 vezes** mais; "requisitos não validados são inúteis"; "a mudança de requisitos é o caso normal" (evolução); "agilidade não é desculpa para trabalho ad hoc" (trabalho sistemático).

---

## I4 — Especificação, validação, mudanças e rastreabilidade
**Subtópico coberto:** 1.4, Especificação, Validação, Gerenciamento de Mudanças e Rastreabilidade (apostila p. 20–22)
**Por que é provável:** a seção traz definições contrastantes que dão boas afirmativas: "requisitos corretamente" × "requisitos certos", backward × forward, as 4 etapas do CCB, gold plating.
**Prioridade:** Alta
**Tipo ENADE:** Afirmativas múltiplas (I–IV)

**Enunciado:**
Durante uma auditoria no sistema de crédito de um banco digital, a equipe de qualidade encontrou dois problemas: (a) um módulo de "cashback por indicação" totalmente implementado, mas sem vínculo com nenhum requisito de negócio; e (b) o requisito RF-17 ("o sistema deve bloquear propostas de clientes com CPF irregular"), que não tinha nenhum caso de teste nem commit associado. A equipe decidiu reforçar as práticas de Engenharia de Requisitos. Sobre esse cenário, avalie as afirmações a seguir.

I. Uma matriz de rastreabilidade que cruzasse os IDs dos requisitos com os IDs de módulos de arquitetura, commits e cenários de teste permitiria detectar os dois problemas: o RF-17 seria um requisito esquecido, e o módulo de cashback caracterizaria gold plating.

II. A rastreabilidade para trás (backward) liga o requisito aos artefatos de design, código e casos de teste e responde a perguntas como "onde este requisito foi implementado?".

III. Enquanto a especificação garante que os requisitos foram escritos corretamente, a validação garante que foram escritos os requisitos certos. A geração de casos de teste a partir dos requisitos, antes da codificação, é uma técnica de validação.

IV. No gerenciamento de mudanças tradicional com Change Control Board (CCB), a análise de impacto ocorre depois de o comitê aprovar a mudança e serve apenas para atualizar a documentação.

É correto o que se afirma em:

**Julgamento das afirmativas:**
- **I — Verdadeira.** A matriz cruza requisitos com arquitetura, commits e testes. Requisito sem teste ou código vinculado "foi esquecido", e código sem requisito vinculado é **gold plating** (p. 22).
- **II — Falsa.** A afirmativa descreve a rastreabilidade **para frente (forward)**. A rastreabilidade **para trás** liga o requisito à sua **origem**: por que existe, quem pediu, que regra de negócio atende.
- **III — Verdadeira.** É a frase da p. 21. Revisões (walkthroughs), prototipagem e geração de casos de teste são as técnicas de validação. "Se um requisito for muito difícil de testar, ele provavelmente está mal especificado."
- **IV — Falsa.** A ordem é Solicitação → **Análise de impacto** → Aprovação/Rejeição → Atualização (p. 21–22). A análise de impacto **subsidia** a decisão do comitê, então vem antes dela.

**Alternativas:**
- **A)** I e III, apenas.
- **B)** I e IV, apenas.
- **C)** II e III, apenas.
- **D)** I, II e IV, apenas.
- **E)** II, III e IV, apenas.

**Gabarito: A**

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — Só I e III são verdadeiras.
- **B) ❌** — Inclui a IV, que inverte a ordem do CCB.
- **C) ❌** — Inclui a II, que troca backward por forward.
- **D) ❌** — Inclui II e IV, ambas falsas, e omite a III.
- **E) ❌** — Inclui II e IV e omite a I.

**Base no material:** p. 20 (boa especificação: clareza/ausência de ambiguidade, completude, consistência, testabilidade; artefato SRS ou Product Backlog); p. 21 (validação × especificação; técnicas); p. 21–22 (CCB e perspectiva ágil: refinamento/grooming do backlog); p. 22 (backward × forward, matriz, gold plating).
**Conceito-chave para a prova:** **Backward = origem** (por quê? quem pediu?). **Forward = destino** (onde foi implementado? qual teste prova?). **Requisito sem teste = esquecido. Código sem requisito = gold plating.** CCB: **S-A-A-A** (Solicitação, Análise de impacto, Aprovação/Rejeição, Atualização). No ágil, a mudança é vista como vantagem competitiva e é tratada no refinamento do backlog.

---

## I5 — Técnicas de elicitação e suas categorias
**Subtópico coberto:** 2.1, Técnicas de elicitação de requisitos (apostila p. 23–28; slides p. 38–40)
**Por que é provável:** a própria apostila avisa: "A banca não costuma aprofundar muito nesse assunto, sendo suficiente conhecer o conceito de cada técnica e **a categoria em que se encontra**" (p. 23). Há síntese por categoria e mapa mental (p. 28), e os slides dedicam 3 páginas ao tema.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única ("respectivamente")

**Enunciado:**
A equipe de requisitos de um hospital universitário planejou quatro atividades para levantar os requisitos de um novo sistema de prontuário:

1. Enfermeiros receberão cartões com nomes de funcionalidades e informações do sistema e deverão agrupá-los conforme o seu próprio entendimento, para orientar a arquitetura de informação das telas.
2. Usuários finais, gerentes, analistas e desenvolvedores participarão de sessões intensivas durante três dias, conduzidas por um facilitador experiente, com agenda definida, documentação dos requisitos em tempo real e aprovação dos requisitos pelos presentes ao final.
3. Uma pesquisadora passará semanas imersa no pronto-socorro, observando e interagindo com a equipe em sua rotina para compreender a cultura, as práticas e os desafios do ambiente.
4. Um formulário padronizado será enviado a 2.000 pacientes para coletar informações de forma estruturada.

As técnicas descritas em 1, 2, 3 e 4 e as categorias às quais pertencem são, respectivamente:

**Alternativas:**
- **A)** card sorting (técnica de grupo); RAD (técnica tradicional); observação (técnica contextual); questionário (técnica de grupo).
- **B)** repertory grids (técnica cognitiva); brainstorming (técnica de grupo); análise social (técnica contextual); entrevista (técnica tradicional).
- **C)** card sorting (técnica contextual); JAD (técnica de grupo); análise de protocolo (técnica cognitiva); questionário (técnica tradicional).
- **D)** laddering (técnica cognitiva); workshop (técnica tradicional); etnografia (técnica contextual); questionário (técnica de grupo).
- **E)** card sorting (técnica cognitiva); JAD (técnica de grupo); etnografia (técnica contextual); questionário (técnica tradicional).

**Gabarito: E**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Erra as categorias: card sorting é **cognitiva**, RAD é de **grupo** e questionário é **tradicional**. Na 3, "imersão" e "cultura" indicam etnografia, não a simples observação.
- **B) ❌** — As categorias citadas estão certas, mas as técnicas não. Repertory grids pede para **comparar e contrastar** elementos, não agrupar cartões. Brainstorming não tem as marcas da 2 (vários dias, facilitador, documentação em tempo real, aprovação ao final), que são da **JAD**. Análise social estuda comunicações e redes, não imersão. O formulário para 2.000 pessoas é questionário, não entrevista.
- **C) ❌** — Card sorting não é contextual, e o item 3 não é análise de protocolo (registro de ações e pensamentos durante uma tarefa).
- **D) ❌** — Laddering é a "escada" de perguntas "por quê?". Workshop é técnica de **grupo**, e questionário é **tradicional**.
- **E) ✅** — Card sorting = agrupar cartões → **cognitiva**. JAD = facilitador, sessões intensivas, documentação em tempo real e aprovação → **de grupo**. Etnografia = imersão profunda, de origem antropológica → **contextual**. Questionário = grande volume, padronizado → **tradicional** (p. 23–28).

**Base no material:** p. 28, síntese: "Tradicionais: entrevistas, questionários e observações. Grupo: workshops, brainstorming, JAD e RAD. Prototipação. Cognitivas: análise de protocolo, laddering, card sorting e repertory grids. Contextuais: etnografia e análise social". Slides p. 39–40.
**Conceito-chave para a prova:** decore as **5 categorias e quem está em cada uma**. Sinais da **JAD**: facilitador, sessões intensivas, documentação em tempo real, aprovação. Sinais do **RAD**: entrega rápida usando JAD, CASE e prototipação. Sinais da **etnografia**: imersão, cultura, antropologia. Sinais de **card sorting**: agrupar cartões.

---

## I6 — Detalhes das técnicas de elicitação
**Subtópico coberto:** 2.1, descrição de brainstorming, JAD, laddering, repertory grids e análise social (apostila p. 24–27; slides p. 40)
**Por que é provável:** a apostila descreve em detalhe as fases do brainstorming e os 7 aspectos da JAD. É o conteúdo mais denso da seção e permite trocar a descrição de uma técnica pela de outra.
**Prioridade:** Alta
**Tipo ENADE:** Afirmativa negativa (INCORRETA)

**Enunciado:**
Uma consultoria de software está treinando analistas juniores em técnicas de elicitação de requisitos. Ao final do treinamento, os analistas devem saber reconhecer o funcionamento de cada técnica para escolher a mais adequada ao tempo disponível, aos recursos, à complexidade do projeto e às informações que precisam ser obtidas. Considerando as técnicas de elicitação de requisitos, assinale a alternativa **INCORRETA**.

**Alternativas:**
- **A)** No brainstorming, durante a fase de geração de ideias, não há julgamento das ideias e a ênfase está na quantidade, não na qualidade. A relevância, a viabilidade e o valor das ideias são discutidos depois, na fase de discussão e seleção.
- **B)** A JAD reúne participantes-chave em sessões intensivas, conduzidas por um facilitador, com agenda definida e documentação em tempo real. Ao final, os requisitos são revisados e aprovados pelos stakeholders presentes.
- **C)** O laddering usa perguntas abertas, como "Por que você acha isso importante?", para explorar as relações hierárquicas entre valores, crenças e objetivos dos usuários, representadas em forma de escada.
- **D)** O repertory grids é uma técnica contextual de origem antropológica em que o pesquisador fica imerso por longos períodos no ambiente do usuário, faz anotações detalhadas e documenta suas experiências.
- **E)** A análise social estuda as interações e a comunicação entre os stakeholders, incluindo e-mails e reuniões, para entender como a informação flui e como as decisões são tomadas.

**Gabarito: D**

**Por que cada alternativa está certa ou errada:**
- **A) ❌ (afirmação correta)** — Descreve as fases do brainstorming da apostila: preparação, geração sem julgamento, duração limitada, ideias visíveis, discussão e seleção, documentação (p. 24–25).
- **B) ❌ (afirmação correta)** — Reproduz os aspectos da JAD (p. 25–26).
- **C) ❌ (afirmação correta)** — É a definição de laddering (p. 26).
- **D) ✅ (afirmação INCORRETA)** — A descrição é da **etnografia**, que é **contextual**. O **repertory grids** é uma técnica **cognitiva** em que os usuários **comparam e contrastam elementos** para revelar as dimensões que consideram relevantes (p. 27).
- **E) ❌ (afirmação correta)** — É a definição de análise social, também técnica contextual (p. 27).

**Base no material:** p. 24–27 (descrição de cada técnica); slides p. 40 ("Brainstorming: geração livre e sem julgamentos..."; "JAD: imersão intensiva conduzida por um facilitador...").
**Conceito-chave para a prova:** técnicas **cognitivas** investigam o **pensamento** do usuário (protocolo, laddering, card sorting, repertory grids). Técnicas **contextuais** investigam o **ambiente** (etnografia, análise social). A prototipação é indicada para **alto grau de incerteza** e feedback rápido (p. 26). Slide 38: "A melhor elicitação é aquela que consegue identificar o maior número possível de requisitos".

---

## I7 — UML: visão geral e tipos de diagramas
**Subtópico coberto:** 2.2, UML (apostila p. 29–33; slides p. 56–57)
**Por que é provável:** a apostila traz a classificação "14 tipos de diagramas, estruturais × comportamentais", com a lista completa, e os modelos funcional/objeto/dinâmico. Os slides acrescentam a norma ISO/IEC 19505. Classificar diagramas é questão clássica.
**Prioridade:** Alta
**Tipo ENADE:** Afirmativas múltiplas (I–IV)

**Enunciado:**
Uma empresa que desenvolve um sistema de gestão escolar decidiu padronizar a documentação de seus projetos com a UML, para reduzir o tempo gasto explicando o sistema repetidamente a novos desenvolvedores e às partes interessadas. Antes de definir quais diagramas seriam obrigatórios, a arquiteta de software listou algumas premissas. Avalie as afirmações a seguir.

I. A UML é uma linguagem de modelagem padronizada, reconhecida como padrão internacional (ISO/IEC 19505), que permite visualizar, especificar, construir e documentar sistemas de software. Seus padrões identificam 14 tipos de diagramas, divididos em estruturais e comportamentais.

II. Os diagramas de classes, de componentes, de implantação, de objetos e de pacotes são estruturais. Os diagramas de atividades, de sequência, de estados e de casos de uso são comportamentais.

III. O diagrama de casos de uso é estrutural, pois representa o limite do sistema e os atores que estão fora dele.

IV. O diagrama de sequência representa a estrutura estática do sistema, com classes, atributos e operações, e por isso é considerado a base principal de qualquer solução orientada a objetos.

É correto o que se afirma em:

**Julgamento das afirmativas:**
- **I — Verdadeira.** Slides p. 56 (ISO/IEC 19505; visualizar, especificar, construir e documentar) e apostila p. 30 (14 tipos em 2 grupos).
- **II — Verdadeira.** São estruturais: classes, componentes, estrutura composta, implantação, objetos, pacotes e perfil. São comportamentais: atividades, comunicação, visão geral de interação, sequência, estados, tempo e caso de uso (p. 30–32).
- **III — Falsa.** O caso de uso é **comportamental**, porque modela como os usuários interagem com o sistema, e corresponde ao **modelo funcional** (p. 32). Desenhar o limite do sistema não o torna estrutural.
- **IV — Falsa.** A descrição é do **diagrama de classes**, "o diagrama UML mais comumente usado e a base principal de qualquer solução orientada a objetos" (p. 30). O diagrama de sequência é comportamental (de interação) e mostra **a ordem** em que os objetos interagem.

**Alternativas:**
- **A)** I, apenas.
- **B)** I e II, apenas.
- **C)** II e III, apenas.
- **D)** I, II e IV, apenas.
- **E)** I, III e IV, apenas.

**Gabarito: B**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Omite a II, que também é verdadeira.
- **B) ✅** — I e II são verdadeiras. III e IV são falsas.
- **C) ❌** — Inclui a III (caso de uso não é estrutural) e omite a I.
- **D) ❌** — Inclui a IV, que troca sequência por classes.
- **E) ❌** — Inclui III e IV e omite a II.

**Base no material:** apostila p. 30–32 (lista dos 14 diagramas); p. 32 ("Funcional: diagramas de caso de uso... Objeto: diagramas de classes... Dinâmico: diagramas de interação, de máquina de estados e de atividades"); slides p. 56–57.
**Conceito-chave para a prova:** **estrutural = o que o sistema É** (classes, objetos, componentes, implantação, pacotes, estrutura composta, perfil). **Comportamental = o que o sistema FAZ ao longo do tempo** (casos de uso, atividades, estados, sequência, comunicação, tempo, visão geral de interação). Os diagramas de interação (sequência, comunicação, tempo, visão geral) são um subgrupo dos comportamentais. Os 4 pilares OO aparecem resumidos na p. 33 (ver I16).

---
