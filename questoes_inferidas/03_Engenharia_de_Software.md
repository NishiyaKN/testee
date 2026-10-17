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

## I8 — ISO/IEC 25010:2023: classificação de requisitos
**Subtópico coberto:** ISO/IEC 25010:2023, as nove características de qualidade de produto (slides p. 41, 43–52)
**Por que é provável:** os slides gastam **10 páginas** com a norma, uma por característica, com a lista de subcaracterísticas. Nenhuma questão conhecida cobra isso; a Q3 só a cita como referência.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única ("respectivamente")

**Enunciado:**
A equipe de qualidade de um banco digital está classificando os requisitos não funcionais do novo aplicativo segundo o modelo de qualidade de produto da ISO/IEC 25010:2023. Foram analisados os seguintes requisitos:

I. "Toda transação deve gerar um registro que impeça o cliente de negar, posteriormente, que a realizou."
II. "O aplicativo deve continuar operando, sem interrupção perceptível, quando um dos servidores do cluster falhar."
III. "O sistema deve trocar e utilizar informações com os sistemas do Banco Central por meio de uma API padronizada."
IV. "Na migração para outro provedor de nuvem, o sistema deve ser instalado de forma eficiente, e seus componentes devem poder ser substituídos com o mínimo de interrupção."

De acordo com a ISO/IEC 25010:2023, os requisitos I, II, III e IV pertencem, respectivamente, às características:

**Alternativas:**
- **A)** Confiabilidade; Segurança (Security); Flexibilidade; Compatibilidade.
- **B)** Segurança (Security); Eficiência de desempenho; Compatibilidade; Portabilidade.
- **C)** Segurança (Security); Confiabilidade; Compatibilidade; Flexibilidade.
- **D)** Safety; Confiabilidade; Adequação funcional; Manutenibilidade.
- **E)** Segurança (Security); Confiabilidade; Capacidade de interação; Flexibilidade.

**Gabarito: C**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Troca os dois primeiros: impedir a negação de uma transação é **não repúdio** (Security), e operar apesar da falha de um servidor é **tolerância a falhas** (Confiabilidade). Também troca III e IV.
- **B) ❌** — Continuar operando durante uma falha não é desempenho, e **Portabilidade não existe mais** na versão 2023: foi substituída por **Flexibilidade**.
- **C) ✅** — I: **não repúdio**, subcaracterística de **Security** (slide p. 49). II: **tolerância a falhas**, de **Confiabilidade** (p. 48). III: **interoperabilidade**, de **Compatibilidade** (p. 46). IV: **facilidade de instalação** e **substituibilidade**, de **Flexibilidade** (p. 51).
- **D) ❌** — **Safety** é proteção contra danos não intencionais a pessoas, propriedades e meio ambiente, não contra a negação de transações. Troca de dados entre sistemas não é adequação funcional.
- **E) ❌** — Interoperabilidade é de **Compatibilidade**. **Capacidade de interação** (que substituiu a usabilidade) trata da interação do usuário com o software.

**Base no material:** slides p. 44–52. Subcaracterísticas: Compatibilidade (coexistência, interoperabilidade), Confiabilidade (impecabilidade, disponibilidade, tolerância a falhas, recuperabilidade), Security (confidencialidade, integridade, não repúdio, responsabilização, autenticidade, resistência), Flexibilidade (adaptabilidade, facilidade de instalação, substituibilidade, escalabilidade).
**Conceito-chave para a prova:** as 9 características da 25010:2023 são: **Adequação funcional, Eficiência de desempenho, Compatibilidade, Capacidade de interação, Confiabilidade, Security, Manutenibilidade, Flexibilidade e Safety**. As mudanças de 2023 foram: usabilidade virou **capacidade de interação**, portabilidade virou **flexibilidade** e **safety** é nova.

---

## I9 — ISO/IEC 25010:2023: Safety × Security
**Subtópico coberto:** ISO/IEC 25010:2023, característica Safety, nova na versão 2023 (slides p. 49 e 52)
**Por que é provável:** os slides destacam a Safety como "uma das adições mais significativas" e a distinguem da Security. Em português as duas se traduzem como "segurança", o que é uma pegadinha natural para asserção-razão.
**Prioridade:** Alta
**Tipo ENADE:** Asserção-razão

**Enunciado:**
Uma empresa de equipamentos médicos está especificando o software embarcado de uma bomba de infusão hospitalar. Um dos requisitos diz: "ao detectar falha no sensor de fluxo, o equipamento deve interromper imediatamente a infusão, entrar em um estado operacional seguro e emitir alerta sonoro à equipe de enfermagem". A equipe precisa enquadrar esse requisito no modelo de qualidade da ISO/IEC 25010:2023.

Analise as asserções a seguir e a relação proposta entre elas:

I. O requisito descrito pertence à característica Safety da ISO/IEC 25010:2023, pois envolve comportamento à prova de falhas e aviso de perigo para evitar riscos inaceitáveis ao paciente.

**PORQUE**

II. Safety é o novo nome que a ISO/IEC 25010:2023 deu à antiga característica Security, que passou a reunir as subcaracterísticas de confidencialidade, integridade, não repúdio e autenticidade.

**Julgamento:**
- **Asserção I — Verdadeira.** Safety mede o grau em que o software evita riscos inaceitáveis a pessoas, organizações, propriedades ou ao meio ambiente. Tem como subcaracterísticas restrição operacional, identificação de riscos, **comportamento à prova de falhas** ("transição para estados operacionais seguros durante falhas"), **aviso de perigo** e integração segura (slide p. 52).
- **Asserção II — Falsa.** A Safety **não substitui** a Security. É uma característica **nova**, e a Security continua existindo como característica própria, com confidencialidade, integridade, não repúdio, responsabilização, autenticidade e resistência (slide p. 49). As substituições da versão 2023 foram outras: usabilidade virou capacidade de interação e portabilidade virou flexibilidade.

**Alternativas:**
- **A)** As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
- **B)** As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
- **C)** A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
- **D)** A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
- **E)** As asserções I e II são proposições falsas.

**Gabarito: C**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — A II é falsa, então não pode justificar a I.
- **B) ❌** — A II é falsa.
- **C) ✅** — A I é verdadeira (requisito de Safety) e a II é falsa (Safety ≠ Security renomeada).
- **D) ❌** — A I é verdadeira. Quem enquadrasse o requisito em "Confiabilidade/tolerância a falhas" esqueceria que, aqui, o sistema **para** e vai para estado seguro para proteger uma pessoa, em vez de continuar operando.
- **E) ❌** — A I é verdadeira.

**Base no material:** slide p. 52 ("Uma das adições mais significativas na ISO/IEC 25010:2023 é a Safety... proteção contra danos não intencionais"); slide p. 49 (Security e suas subcaracterísticas); slides p. 47 e p. 51 (substituições de usabilidade e portabilidade).
**Conceito-chave para a prova:** **Security** = proteger **informação** contra acesso, modificação ou divulgação **não autorizados** (ataques). **Safety** = evitar **danos não intencionais** a **pessoas, propriedades e meio ambiente**. **Confiabilidade/tolerância a falhas** = **continuar funcionando** apesar da falha. **Comportamento à prova de falhas (Safety)** = **ir para um estado seguro** quando a falha ocorre.

---

## I10 — Modelos de processo e fluxo paralelo
**Subtópico coberto:** 3.1 Fluxos de software (fluxo paralelo) e 3.2 Modelos de processo (Incremental, Espiral, Reuso). A apostila trata deles nas p. 34–39 e os slides nas p. 23 e 29–33. A Q2 só cobriu evolucionário, Prototipação e Cascata.
**Por que é provável:** os slides dedicam um slide a cada modelo, e a Q2 deixou de fora incremental, espiral, reuso e paralelo. Os slides destacam que o incremental "combina elementos do fluxo de processos lineares e paralelos", o que dá um distrator natural.
**Prioridade:** Média
**Tipo ENADE:** Associação

**Enunciado:**
Uma empresa de tecnologia conduz quatro projetos simultâneos, cada um com uma abordagem de processo diferente:

I. Uma plataforma de e-commerce é entregue em partes: primeiro o catálogo, depois o carrinho e, por fim, o pagamento. Cada parte é planejada, projetada, codificada, testada e liberada individualmente, aplicando sequências lineares escalonadas ao longo do tempo.

II. Um sistema de controle de tráfego aéreo, de grande porte e alto risco, é desenvolvido em ciclos que se ampliam progressivamente. Cada ciclo começa com planejamento e identificação de riscos, seguido de desenvolvimento, testes e coleta de feedback.

III. Um portal interno é construído a partir de módulos de autenticação, bibliotecas de relatórios e componentes de pagamento já existentes, em vez de desenvolver tudo do zero.

IV. Em um aplicativo de delivery, enquanto uma equipe codifica o módulo de pedidos, outra testa o módulo de cadastro e uma terceira projeta novas funcionalidades, ao mesmo tempo.

Associe cada projeto à abordagem correspondente:

1. Modelo Espiral
2. Engenharia de software orientada a reuso
3. Fluxo paralelo
4. Desenvolvimento incremental

Assinale a alternativa que apresenta a associação correta.

**Alternativas:**
- **A)** I-3, II-1, III-2, IV-4.
- **B)** I-4, II-2, III-1, IV-3.
- **C)** I-1, II-4, III-2, IV-3.
- **D)** I-4, II-1, III-3, IV-2.
- **E)** I-4, II-1, III-2, IV-3.

**Gabarito: E**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Inverte I e IV. Entregar por partes testadas e liberadas individualmente é **incremental**. Várias equipes fazendo atividades diferentes ao mesmo tempo é **paralelo**. O incremental "combina" linear e paralelo, mas o que o define são os **incrementos entregáveis**.
- **B) ❌** — Troca Espiral e Reuso: "identificação de riscos a cada ciclo" é a marca do Espiral.
- **C) ❌** — Associa o e-commerce por partes ao Espiral e o tráfego aéreo ao incremental. O alto risco e os ciclos que se ampliam indicam o contrário.
- **D) ❌** — Troca reuso e paralelo.
- **E) ✅** — I-4: incrementos planejados, codificados e testados individualmente, com "sequências lineares de forma escalonada" (slides p. 29). II-1: Espiral, ciclos "que vão se ampliando", cada um começando por planejamento e **identificação de riscos** (apostila p. 38; slides p. 32). III-2: reuso de componentes, módulos e bibliotecas existentes (p. 39; slides p. 33). IV-3: fluxo paralelo, várias atividades realizadas ao mesmo tempo por equipes distintas (p. 35; slides p. 23).

**Base no material:** apostila p. 34–39; slides p. 22–33.
**Conceito-chave para a prova:** **Linear** = sequência fixa, sem retorno. **Iterativo** = repete e volta a etapas. **Evolucionário** = ciclos com feedback (inclui Prototipação e Espiral). **Paralelo** = atividades simultâneas. **Incremental** = entregas em partes (linear + paralelo escalonado). **Espiral** = ciclos com **análise de riscos**. **Reuso** = componentes prontos. **Cascata** = requisitos estáveis e bem compreendidos.

---

## I11 — Fases do RUP
**Subtópico coberto:** 3.3, RUP (Rational Unified Process) (apostila p. 40–42; slides p. 34)
**Por que é provável:** o RUP está nos slides e na apostila, com objetivo, atividades e saída de cada fase, mais o gráfico "Fases do RUP" (p. 42). O arquivo de questões conhecidas o lista entre os temas sem questão.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única ("respectivamente")

**Enunciado:**
Uma empresa de logística adotou o RUP (Rational Unified Process), um processo iterativo e incremental desenvolvido pela Rational Software, para construir um sistema de rastreamento de cargas. Ao revisar o cronograma, o gerente identificou as seguintes atividades, cada uma típica de uma fase diferente do RUP:

- Treinamento dos usuários, implantação no ambiente de produção e coleta de feedback.
- Desenvolvimento de uma arquitetura inicial e de um protótipo, com detalhamento dos requisitos funcionais e não funcionais para reduzir os riscos identificados.
- Identificação dos stakeholders, análise de viabilidade e produção do documento de visão.
- Codificação e testes das funcionalidades, integração de componentes e testes contínuos.

As atividades listadas pertencem, respectivamente, às fases:

**Alternativas:**
- **A)** Transição; Elaboração; Iniciação; Construção.
- **B)** Transição; Construção; Iniciação; Elaboração.
- **C)** Construção; Elaboração; Iniciação; Transição.
- **D)** Transição; Iniciação; Elaboração; Construção.
- **E)** Implantação; Análise e Design; Iniciação; Implementação.

**Gabarito: A**

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — Treinamento, implantação e feedback = **Transição**. Arquitetura inicial, protótipo e redução de riscos = **Elaboração**. Stakeholders, viabilidade e documento de visão = **Iniciação (Inception/Incepção)**. Codificação, integração e testes contínuos = **Construção** (apostila p. 40–41).
- **B) ❌** — Troca Elaboração e Construção. A arquitetura sólida é **saída** da Elaboração, e a Construção desenvolve **sobre** ela.
- **C) ❌** — Implantação em produção e treinamento não são Construção, cuja saída é o produto "quase final".
- **D) ❌** — O documento de visão é saída da **Iniciação**, e a arquitetura inicial é da **Elaboração**. A alternativa inverte as duas.
- **E) ❌** — Usa nomes de **disciplinas** do RUP (Modelagem de Negócio, Requisitos, Análise e Design, Implementação, Teste, Implantação, do gráfico da p. 42) no lugar das **fases**. As fases são só 4: Iniciação, Elaboração, Construção e Transição.

**Base no material:** apostila p. 40–41 (objetivo, atividades e saída de cada fase); p. 42 (gráfico com as fases I1, E1–E2, C1–C4, T1–T2 × disciplinas); slides p. 34 ("Incepção... Elaboração: define-se uma solução... do ponto de vista de arquitetura... Construção: projeto, programação e testes. Transição: libera o sistema para seu ambiente operacional").
**Conceito-chave para a prova:** **I-E-C-T**. Saídas: **Iniciação** → documento de visão. **Elaboração** → arquitetura sólida e plano detalhado. **Construção** → produto quase final. **Transição** → produto entregue e plano de suporte. As **fases** (tempo) não se confundem com as **disciplinas** (trabalho, que se repete em todas as fases com intensidades diferentes). O RUP é **iterativo e incremental**.

---

## I12 — Ágil × tradicional
**Subtópico coberto:** 4.1, Metodologia Ágil e comparação Ágil × Tradicional (apostila p. 43–44; slides p. 5–6)
**Por que é provável:** a apostila e os slides trazem tabelas comparativas (estrutura, planejamento, execução, mudanças, feedback, entrega de valor). Tabela comparativa costuma virar afirmativas.
**Prioridade:** Média
**Tipo ENADE:** Afirmativas múltiplas (I–IV)

**Enunciado:**
Uma seguradora que sempre desenvolveu seus sistemas no modelo tradicional (Cascata) decidiu migrar para a metodologia Ágil, após sucessivos atrasos e entregas que já não atendiam ao negócio quando ficavam prontas. Em um workshop de transição, o coach ágil apresentou as diferenças entre os dois fluxos de trabalho. Avalie as afirmações a seguir.

I. No fluxo ágil, o escopo é reavaliado a cada ciclo e o cliente recebe partes funcionais (incrementos) com frequência. No tradicional, o cliente só vê o produto funcionando no final do cronograma.

II. No fluxo tradicional, as mudanças são rígidas e exigem processos formais lentos, e a execução de cada etapa depende da conclusão da etapa anterior.

III. A metodologia ágil divide demandas complexas em etapas menores e gerenciáveis chamadas sprints, e o feedback coletado ao final de cada iteração direciona as próximas fases.

IV. Por ser flexível, o fluxo ágil dispensa o Product Backlog, já que a priorização das tarefas é feita apenas na entrega final do projeto.

É correto o que se afirma em:

**Julgamento das afirmativas:**
- **I — Verdadeira.** Linhas "Flexibilidade" e "Entrega de valor" da tabela da apostila (p. 44).
- **II — Verdadeira.** Linhas "Mudanças" e "Execução" da tabela dos slides (p. 6).
- **III — Verdadeira.** Definição dos slides (p. 5).
- **IV — Falsa.** O Product Backlog é "uma parte fundamental do fluxo de trabalho Ágil", e no **início de cada sprint** a equipe revisa o backlog e prioriza as tarefas mais importantes (p. 43).

**Alternativas:**
- **A)** I e II, apenas.
- **B)** I e IV, apenas.
- **C)** III e IV, apenas.
- **D)** I, II e III, apenas.
- **E)** I, II, III e IV.

**Gabarito: D**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Omite a III, que é a própria definição de Ágil dos slides.
- **B) ❌** — Inclui a IV (falsa) e omite II e III.
- **C) ❌** — Inclui a IV e omite I e II.
- **D) ✅** — I, II e III são verdadeiras. A IV é falsa.
- **E) ❌** — A IV é falsa.

**Base no material:** slides p. 5–6; apostila p. 43 (vantagens: flexibilidade, colaboração, valor ao cliente, priorização pelo product backlog) e p. 44 (tabela Ágil × Tradicional).
**Conceito-chave para a prova:** no tradicional, planejamento totalmente definido antes, mudanças rígidas e feedback **só no fim**. No ágil, planejamento atualizado continuamente, mudanças integradas a cada ciclo, feedback **após cada sprint** e incrementos frequentes. Foco do ágil: colaboração constante, software em funcionamento e resposta rápida à mudança.

---

## I13 — Frameworks ágeis
**Subtópico coberto:** 4.2, Frameworks e práticas ágeis (apostila p. 44–45; slides p. 7–15)
**Por que é provável:** os slides dedicam **9 páginas**, uma por framework (Kanban, Lean, Scrum, Scrumban, XP, TDD, FDD, ASD, SAFe). A Q1 cobre só os papéis do Scrum.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única ("respectivamente")

**Enunciado:**
Uma consultoria de transformação digital atende cinco clientes, e cada um adotou uma abordagem diferente do universo Ágil:

I. A equipe de suporte e manutenção de uma operadora mantém os papéis e as cerimônias do Scrum, mas abandonou os sprints de duração fixa em favor do fluxo contínuo com limites de trabalho em progresso (WIP).

II. Um banco com centenas de desenvolvedores precisa alinhar a estratégia de negócios da alta gestão com a execução técnica de múltiplos times simultâneos, combinando práticas de Scrum, Kanban, Lean e XP.

III. Uma startup trata o desenvolvimento como complexo e imprevisível e substituiu o ciclo "Planejar-Construir-Testar" pelo ciclo "Especular-Colaborar-Aprender".

IV. Uma software house começa cada projeto pela modelagem do domínio do negócio, cria uma lista de funcionalidades e, então, planeja e constrói iterativamente cada uma delas.

V. Uma montadora aplica ao software os princípios originados no sistema de produção da Toyota: elimina tudo o que não gera valor ao cliente e adia decisões irreversíveis até o último momento seguro.

As abordagens adotadas pelos clientes I, II, III, IV e V são, respectivamente:

**Alternativas:**
- **A)** Kanban; SAFe; ASD; FDD; Lean.
- **B)** Scrumban; SAFe; ASD; FDD; Lean.
- **C)** Scrumban; Scrum; XP; FDD; Lean.
- **D)** Scrumban; SAFe; FDD; ASD; Lean.
- **E)** Kanban; SAFe; ASD; TDD; XP.

**Gabarito: B**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — O Kanban puro não usa os papéis e as cerimônias do Scrum. O híbrido que os mantém e troca os sprints por fluxo contínuo com limite de WIP é o **Scrumban**, "muito usado por equipes de suporte ou manutenção" (slides p. 10).
- **B) ✅** — I: Scrumban. II: **SAFe**, que escala o Ágil em grandes corporações (p. 15). III: **ASD**, com o ciclo Speculate-Collaborate-Learn (p. 14). IV: **FDD**, orientado por modelos e por features (p. 13). V: **Lean**, nascido na Toyota, com eliminação de desperdícios e decisões adiadas (p. 8).
- **C) ❌** — O Scrum não resolve o alinhamento de centenas de devs em múltiplos times, e o XP não usa o ciclo Especular-Colaborar-Aprender.
- **D) ❌** — Inverte ASD e FDD.
- **E) ❌** — TDD não é framework de gestão, é prática técnica de testar antes. O XP foca em excelência técnica (pair programming, refatoração), não na eliminação de desperdícios.

**Base no material:** slides p. 7–15; apostila p. 44–45.
**Conceito-chave para a prova:** Kanban = quadro + **limite de WIP**. Lean = **eliminar desperdício** (Toyota). Scrum = sprints de duração fixa + 3 papéis + 4 ritos. Scrumban = Scrum + fluxo contínuo (suporte/manutenção). XP = **excelência técnica** (pair programming, integração contínua, refatoração). TDD = **Red-Green-Refactor**. FDD = **features + modelagem do domínio**. ASD = **Especular-Colaborar-Aprender**. SAFe = **escala corporativa**. A duração da sprint diverge no material: os slides (p. 9) dizem 1 a 4 semanas e a apostila (p. 44) diz 2 a 4 semanas.

---

## I14 — TDD e XP
**Subtópico coberto:** 4.2, práticas técnicas ágeis: TDD (Red-Green-Refactor) e XP (apostila p. 45; slides p. 11–12)
**Por que é provável:** o material insiste que o TDD "não é um framework de gestão, mas uma prática técnica" e dá a ordem exata do ciclo. Isso permite uma asserção falsa sobre a ordem (código antes do teste) com uma razão verdadeira.
**Prioridade:** Alta
**Tipo ENADE:** Asserção-razão

**Enunciado:**
Uma equipe de desenvolvimento de um sistema de folha de pagamento vinha sofrendo com regressões frequentes. O líder técnico decidiu adotar práticas ágeis focadas em qualidade de código e propôs o Desenvolvimento Orientado a Testes (TDD).

Analise as asserções a seguir e a relação proposta entre elas:

I. No TDD, o programador primeiro escreve o código da funcionalidade e, em seguida, os testes automatizados que comprovam que ela funciona, seguindo o ciclo Green-Red-Refactor.

**PORQUE**

II. O TDD não é um framework de gestão, mas uma prática técnica de engenharia, alinhada a metodologias focadas em qualidade de código, como o Extreme Programming (XP), que enfatiza testes contínuos, programação em par e refatoração constante.

**Julgamento:**
- **Asserção I — Falsa.** No TDD o teste vem **antes** do código: "O programador escreve o teste automatizado antes de escrever o código da funcionalidade. O ciclo é: escrever um teste que falha (**Red**), escrever o código mínimo para o teste passar (**Green**) e melhorar o código (**Refactor**)" (slides p. 12). A ordem certa é **Red → Green → Refactor**.
- **Asserção II — Verdadeira.** O material diz literalmente que o TDD "não é um framework de gestão, mas uma prática técnica" (p. 12), e o XP é "muito focado na qualidade técnica e na engenharia de código, enfatizando práticas como testes contínuos, programação em pares e refatoração constante" (apostila p. 45).

**Alternativas:**
- **A)** As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
- **B)** As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
- **C)** A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
- **D)** A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
- **E)** As asserções I e II são proposições falsas.

**Gabarito: D**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — A I é falsa: inverte a ordem teste → código e a ordem do ciclo.
- **B) ❌** — A I é falsa.
- **C) ❌** — Inverte o julgamento: a I é que é falsa, e a II é verdadeira.
- **D) ✅** — I falsa (código antes do teste e ciclo invertido). II verdadeira.
- **E) ❌** — A II é verdadeira.

**Base no material:** slides p. 11 (XP) e p. 12 (TDD); apostila p. 45.
**Conceito-chave para a prova:** **Red** (teste que falha) → **Green** (código **mínimo** para passar) → **Refactor** (melhorar sem quebrar). TDD = prática técnica, não gestão. XP = pair programming, integração contínua, refatoração constante e entregas muito frequentes.

---

## I15 — PMBOK: princípios da 8ª edição
**Subtópico coberto:** 4.4, PMBOK (apostila p. 47–48; slides p. 17–18)
**Por que é provável:** está nos slides ("PMBOK: O que é e suas fases") e na apostila, com tabela dos 6 princípios. A Q1 só usa o PMBOK como distrator.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única ("respectivamente")

**Enunciado:**
O PMBOK (Project Management Body of Knowledge) é um guia que descreve práticas, diretrizes e terminologias padronizadas de gestão de projetos. Não é uma metodologia, mas uma estrutura que organiza conhecimentos e pode ser adaptada à realidade de cada organização. Ao conduzir a implantação de um ERP em uma rede varejista, a gerente de projetos Ana tomou as seguintes atitudes:

- Analisou como as decisões do projeto afetariam toda a organização, e não apenas a área de TI, adotando o pensamento sistêmico.
- Passou a medir o sucesso do projeto pelos resultados que importam aos stakeholders, e não apenas pela quantidade de tarefas concluídas.
- Incluiu no planejamento os impactos ambientais, econômicos e sociais, como o consumo de energia dos servidores e o descarte dos equipamentos antigos.
- Estimulou a colaboração, a confiança e a segurança psicológica na equipe, para que todos se sentissem à vontade para apontar problemas.

Segundo os princípios do Guia PMBOK (8ª edição), as atitudes de Ana correspondem, respectivamente, aos princípios:

**Alternativas:**
- **A)** Seja um líder responsável; Foque no valor; Adote uma visão holística; Construir uma cultura de empoderamento.
- **B)** Adote uma visão holística; Qualidade de incorporação; Integrar a sustentabilidade; Seja um líder responsável.
- **C)** Foque no valor; Adote uma visão holística; Construir uma cultura de empoderamento; Integrar a sustentabilidade.
- **D)** Adote uma visão holística; Foque no valor; Construir uma cultura de empoderamento; Integrar a sustentabilidade.
- **E)** Adote uma visão holística; Foque no valor; Integrar a sustentabilidade; Construir uma cultura de empoderamento.

**Gabarito: E**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — "Seja um líder responsável" trata de decisões éticas e boa governança, não de pensamento sistêmico. A visão holística não corresponde à atitude de sustentabilidade.
- **B) ❌** — "Qualidade de incorporação" é integrar a qualidade aos processos e entregas, não medir resultados para os stakeholders. A segurança psicológica é da cultura de empoderamento, não do líder responsável.
- **C) ❌** — Inverte as duas primeiras e também as duas últimas.
- **D) ❌** — Inverte sustentabilidade e empoderamento. É a **pegadinha do próprio slide** (p. 18): por erro, o rótulo "Construir uma cultura de empoderamento" aparece duplicado ao lado da descrição de sustentabilidade.
- **E) ✅** — Visão holística = pensamento sistêmico. Foco no valor = resultados para os stakeholders. Integrar a sustentabilidade = considerações ambientais, econômicas e sociais. Cultura de empoderamento = colaboração, confiança e segurança psicológica (apostila p. 47–48).

**Base no material:** apostila p. 47–48 (tabela correta dos 6 princípios); slides p. 17 (definição: "não é uma metodologia") e p. 18 (tabela com o rótulo duplicado).
**Conceito-chave para a prova:** os 6 princípios do PMBOK 8 são: **visão holística, foco no valor, qualidade incorporada ("de incorporação"), líder responsável, sustentabilidade e cultura de empoderamento**. O PMBOK é um **guia de boas práticas, adaptável a qualquer metodologia**, e não uma metodologia. A apostila diz que ele é "a base de metodologias mais fundamentadas, como o Adaptive Project Framework (APF)".
**⚠️ Atenção:** se a prova copiar a tabela dos slides com o erro, siga a **descrição**: "ambiental, econômica e social" é **sustentabilidade**.

---

## I16 — Pilares da POO
**Subtópico coberto:** 5.1, POO: abstração, encapsulamento, herança e polimorfismo, e POO × programação estruturada (apostila p. 49–54)
**Por que é provável:** a seção tem 6 páginas com exemplos fixos (getters/setters, televisão, Eletrodoméstico.Ligar(), herança múltipla em C++) e uma comparação de desempenho com a programação estruturada que contraria o senso comum. É material bom para afirmativas com pegadinha.
**Prioridade:** Média
**Tipo ENADE:** Afirmativas múltiplas (I–IV)

**Enunciado:**
Uma empresa que mantém um sistema legado em linguagem C decidiu reescrever seu módulo de cadastro de eletrodomésticos em uma linguagem orientada a objetos. Para isso, a equipe modelou a classe genérica `Eletrodomestico`, com o método `Ligar()`, e as classes filhas `Televisao` e `Geladeira`. Os atributos de cada classe foram declarados como privados. Sobre os pilares da Programação Orientada a Objetos e sua comparação com a programação estruturada, avalie as afirmações a seguir.

I. Ao declarar os atributos como privados e permitir o acesso apenas por métodos getters e setters, a equipe aplica o encapsulamento, que esconde as propriedades do objeto e cria uma espécie de "caixa preta".

II. Ao reescrever o método `Ligar()` em `Televisao` e em `Geladeira`, que não são ligadas da mesma forma, a equipe aplica o polimorfismo, que consiste na alteração do funcionamento interno de um método herdado da classe pai.

III. A herança múltipla, presente em C++, foi amplamente adotada pelas linguagens mais modernas, como C# e Java, porque elimina os problemas da herança simples.

IV. A programação orientada a objetos tem execução mais rápida que a estruturada, já que as classes eliminam os desvios do fluxo de execução, e por isso é a mais indicada para sistemas embarcados com hardware limitado.

É correto o que se afirma em:

**Julgamento das afirmativas:**
- **I — Verdadeira.** A maior parte das linguagens OO implementa o encapsulamento com "propriedades privadas, ligadas a métodos especiais chamados getters e setters" (p. 51).
- **II — Verdadeira.** É o exemplo literal da apostila (p. 52–53): o polimorfismo é "a alteração do funcionamento interno de um método herdado de um objeto pai".
- **III — Falsa.** A apostila diz o contrário: "Devido a problemas, essa prática [herança múltipla] não foi difundida em linguagens mais modernas, que utilizam outras artimanhas para criar uma espécie de herança múltipla" (p. 52).
- **IV — Falsa.** Segundo a apostila, a programação **estruturada**, quando bem feita, tem desempenho **superior**, por ser sequencial e com menos desvios. A **POO** é mais lenta, "o grande motivo por trás da preferência pela linguagem C em hardware limitado, como sistemas embarcados" (p. 50 e 54).

**Alternativas:**
- **A)** I e II, apenas.
- **B)** I e III, apenas.
- **C)** II e IV, apenas.
- **D)** I, II e IV, apenas.
- **E)** II, III e IV, apenas.

**Gabarito: A**

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — Só I e II são verdadeiras.
- **B) ❌** — Inclui a III. A herança múltipla **não** se difundiu.
- **C) ❌** — Inclui a IV, que inverte o argumento de desempenho, e omite a I.
- **D) ❌** — Inclui a IV.
- **E) ❌** — Inclui III e IV, ambas falsas.

**Base no material:** p. 49–54. Abstração: identidade, propriedades e métodos, como no exemplo "Cachorro". Encapsulamento: caixa preta, getters/setters, botão da TV. Herança: direta × indireta, herança múltipla em C++, classe `object` em C#. Polimorfismo: `virtual`/`override` em C# e `@Override` em Java. Vantagens: reúso, leitura, manutenção e bibliotecas. Desvantagem: execução mais lenta.
**Conceito-chave para a prova:** **Abstração** = identidade + propriedades + métodos. **Encapsulamento** = esconder dados (privado + getters/setters). **Herança** = reúso, que pode ser direta (pai) ou indireta (avô). **Polimorfismo** = reescrever (sobrescrever) um método herdado. Segundo a apostila, a estruturada é **mais rápida** e a POO tem **mais reúso e manutenção**.

---

## I17 — SOLID: identificação dos princípios
**Subtópico coberto:** 5.2, SOLID (apostila p. 55–57)
**Por que é provável:** cada um dos 5 princípios tem "Definição / O Problema / Exemplo Prático / A Solução", em formato de estudo de caso. O arquivo de questões conhecidas aponta o SOLID como primeiro tema sem questão, e o tema é clássico no ENADE.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única ("respectivamente")

**Enunciado:**
Durante uma revisão de código de um sistema de e-commerce, o arquiteto de software encontrou quatro problemas de design:

I. A classe `GerenciadorDePedidos` calcula o total do pedido, aplica descontos, gera o recibo em PDF e salva os dados no banco. Qualquer mudança na regra de desconto tem quebrado a geração do recibo.

II. A classe `Pinguim` herda de `Ave`, mas seu método `voar()` lança `NotImplementedException`. Quando o sistema percorre uma lista de aves e manda todas voarem, a aplicação quebra ao chegar no pinguim.

III. A interface `IMaquinaTrabalho` exige os métodos `imprimir()`, `escanear()` e `enviarFax()`, o que obriga a classe `ImpressoraBasica` a deixar dois deles vazios.

IV. A classe `ProcessadorDePagamento` tem um grande bloco `switch/case` por tipo de pagamento, e a inclusão do Pix vai obrigar a alterar essa classe, já testada e em produção.

Os problemas I, II, III e IV representam, respectivamente, violações dos princípios:

**Alternativas:**
- **A)** Responsabilidade Única (SRP); Segregação de Interfaces (ISP); Substituição de Liskov (LSP); Inversão de Dependência (DIP).
- **B)** Aberto/Fechado (OCP); Substituição de Liskov (LSP); Segregação de Interfaces (ISP); Responsabilidade Única (SRP).
- **C)** Responsabilidade Única (SRP); Substituição de Liskov (LSP); Segregação de Interfaces (ISP); Aberto/Fechado (OCP).
- **D)** Responsabilidade Única (SRP); Inversão de Dependência (DIP); Segregação de Interfaces (ISP); Aberto/Fechado (OCP).
- **E)** Segregação de Interfaces (ISP); Substituição de Liskov (LSP); Responsabilidade Única (SRP); Aberto/Fechado (OCP).

**Gabarito: C**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Troca LSP e ISP. O switch/case que precisa ser modificado viola o **OCP**, não o DIP.
- **B) ❌** — Inverte SRP e OCP. A "Classe Deus" com múltiplas funções (I) viola o **SRP**, e o switch/case (IV) viola o **OCP**.
- **C) ✅** — I: **SRP**, porque a classe tem mais de um motivo para mudar ("God Class"). II: **LSP**, porque a subclasse não pode substituir a superclasse sem quebrar o programa. III: **ISP**, interface "gorda" que obriga a implementar métodos não usados. IV: **OCP**, porque a classe deveria estar aberta para extensão (nova classe `PagamentoPix`) e fechada para modificação (p. 55–56).
- **D) ❌** — O pinguim não é problema de dependência de módulos de baixo nível. É herança mal utilizada (LSP).
- **E) ❌** — Troca ISP e SRP entre I e III.

**Base no material:** p. 55–56. Soluções da apostila: dividir em `CalculadoraDePedidos`, `GeradorDeReciboPdf` e `PedidoRepository` (SRP); criar `AveQueVoa` e `AveQueNada` (LSP); separar `IImpressora`, `IEscaner` e `IFax` (ISP); criar a interface `MetodoDePagamento` com `processar()` e uma classe por meio de pagamento (OCP, via polimorfismo).
**Conceito-chave para a prova:** **S** = um motivo para mudar. **O** = estender sem modificar. **L** = a subclasse substitui a base sem surpresas. **I** = várias interfaces pequenas em vez de uma "gorda". **D** = depender de abstrações, não de implementações concretas. Os princípios foram formulados por Robert C. Martin (Uncle Bob). Custo: mais arquivos e pastas. Ganho: manutenção, escalabilidade e refatoração segura.

---

## I18 — SOLID: inversão de dependência em código
**Subtópico coberto:** 5.2, SOLID, princípio D (DIP) e injeção de dependência (apostila p. 57)
**Por que é provável:** a apostila descreve um caso concreto e codificável (`new MySQLConnection()` dentro de `ServicoDeUsuario`, migração para PostgreSQL, `IUsuarioRepository` injetada via construtor). Questões ENADE costumam trazer o trecho de código como dado de suporte.
**Prioridade:** Alta
**Tipo ENADE:** Afirmativas múltiplas (I–IV), com código

**Enunciado:**
Uma empresa de SaaS pretende migrar o banco de dados de sua plataforma de MySQL para PostgreSQL. Ao analisar o código, a equipe encontrou a classe a seguir, responsável pelas regras de negócio do cadastro de usuários:

```java
public class ServicoDeUsuario {

    public void cadastrar(Usuario usuario) {
        // ... validações e regras de negócio do cadastro ...
        MySQLConnection conexao = new MySQLConnection("localhost", 3306);
        conexao.executar("INSERT INTO usuarios (nome, email) VALUES (?, ?)",
                         usuario.getNome(), usuario.getEmail());
    }
}
```

Com base nos princípios SOLID, avalie as afirmações a seguir.

I. O código viola o Princípio da Inversão de Dependência (DIP), pois um módulo de alto nível, que contém regras de negócio, instancia diretamente um detalhe de infraestrutura de baixo nível, em vez de depender de uma abstração.

II. Uma refatoração adequada é fazer `ServicoDeUsuario` depender de uma interface `IUsuarioRepository` e receber a implementação concreta (por exemplo, `MySQLUsuarioRepository`) pelo construtor, por meio de injeção de dependência.

III. Mesmo após a refatoração descrita em II, a migração para PostgreSQL ainda exigiria reescrever `ServicoDeUsuario`, pois o serviço precisa saber qual banco de dados está sendo utilizado.

IV. Além de facilitar a troca de tecnologia, a refatoração descrita em II permite testar `ServicoDeUsuario` isoladamente, injetando uma implementação simulada de `IUsuarioRepository` no lugar do banco real.

É correto o que se afirma em:

**Julgamento das afirmativas:**
- **I — Verdadeira.** É o "Problema" descrito na apostila: alto acoplamento, em que a regra de negócio instancia ferramentas de infraestrutura e fica "dependente de uma tecnologia específica" (p. 57).
- **II — Verdadeira.** É a "Solução" da apostila: injeção de dependência, com a implementação concreta passada via construtor.
- **III — Falsa.** Depois da refatoração, "o serviço passa a desconhecer qual banco está sendo usado, focando apenas nas regras de negócio". Basta criar `PostgreSQLUsuarioRepository` e injetá-la. `ServicoDeUsuario` não muda, e a mudança também atende ao OCP.
- **IV — Verdadeira.** A apostila diz que a classe acoplada fica "quase impossível de testar isoladamente". Com a abstração, é possível injetar um mock ou stub, técnica citada também na p. 58 para testar camadas isoladamente.

**Alternativas:**
- **A)** I, apenas.
- **B)** I e III, apenas.
- **C)** II e III, apenas.
- **D)** II, III e IV, apenas.
- **E)** I, II e IV, apenas.

**Gabarito: E**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Omite II e IV, também verdadeiras.
- **B) ❌** — Inclui a III, que nega o objetivo da refatoração.
- **C) ❌** — Inclui a III e omite I e IV.
- **D) ❌** — Inclui a III e omite a I.
- **E) ✅** — I, II e IV são verdadeiras. A III é falsa.

**Base no material:** apostila p. 57: "Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações... detalhes devem depender de abstrações"; "Se a empresa migrar para PostgreSQL, a classe ServicoDeUsuario inteira precisará ser reescrita"; "A implementação concreta (como MySQLUsuarioRepository) é injetada (passada via construtor...)".
**Conceito-chave para a prova:** `new ClasseConcreta()` de infraestrutura dentro de uma regra de negócio é sinal de **violação do DIP**. A correção é **interface + injeção de dependência** (pelo construtor). O DIP **não** é a mesma coisa que injeção de dependência: o DIP é o princípio, e a injeção é a técnica que o implementa.

---

## I19 — Arquitetura em camadas
**Subtópico coberto:** 5.3, Arquitetura em camadas (apostila p. 57–59)
**Por que é provável:** a seção lista as 4 camadas lógicas, 4 configurações físicas e vantagens × desvantagens. Esse formato dá afirmativas verdadeiras e falsas com facilidade.
**Prioridade:** Média
**Tipo ENADE:** Afirmativas múltiplas (I–IV)

**Enunciado:**
Uma cooperativa de crédito está reestruturando o sistema de concessão de empréstimos, que hoje é um único bloco de código. A equipe propôs organizá-lo em quatro camadas lógicas: Apresentação (UI/Web/API), Aplicação/Serviço, Domínio/Negócio e Infraestrutura/Acesso a dados. Sobre essa arquitetura, avalie as afirmações a seguir.

I. A regra "cooperados com mais de cinco anos de associação têm taxa de juros reduzida" deve ficar na camada de Domínio/Negócio, e a comunicação com o banco de dados PostgreSQL deve ficar na camada de Infraestrutura/Acesso a dados.

II. Manter todas as camadas lógicas em um único processo (monolito) facilita implantar, testar e depurar, mas é pouco escalável e pode resultar em um sistema difícil de manter.

III. A arquitetura em camadas melhora a testabilidade, pois os componentes de uma camada podem ser testados isoladamente com mocks e stubs das outras camadas.

IV. Por isolar responsabilidades, a arquitetura em camadas elimina o overhead de chamadas entre camadas e facilita as mudanças transversais, como auditoria e rastreamento, que passam a afetar uma única camada.

É correto o que se afirma em:

**Julgamento das afirmativas:**
- **I — Verdadeira.** O Domínio contém "regras de negócio puras, entidades, serviços de domínio". A Infraestrutura cuida da "comunicação com banco de dados, serviços externos, armazenamento" (p. 57–58).
- **II — Verdadeira.** Configuração física 1 da apostila: "simples de implantar, testar e depurar, mas é pouco escalável. Pode virar um monólito difícil de manter" (p. 58).
- **III — Verdadeira.** Vantagem citada na p. 58.
- **IV — Falsa.** As duas partes estão nas **desvantagens** da apostila: "pode haver overhead de chamadas entre camadas" e "dificuldades em mudanças transversais (ex.: rastreamento, auditoria)", porque essas alterações atravessam várias camadas (p. 59).

**Alternativas:**
- **A)** I e IV, apenas.
- **B)** I, II e III, apenas.
- **C)** I, II e IV, apenas.
- **D)** II, III e IV, apenas.
- **E)** I, II, III e IV.

**Gabarito: B**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Inclui a IV e omite II e III.
- **B) ✅** — I, II e III são verdadeiras. A IV inverte duas desvantagens.
- **C) ❌** — Inclui a IV.
- **D) ❌** — Inclui a IV e omite a I.
- **E) ❌** — A IV é falsa.

**Base no material:** p. 57–59. Camadas lógicas. Configurações físicas: monolito, múltiplos processos, microsserviços e camadas combinadas (serverless/JAMstack). Vantagens: separação de responsabilidades, reúso, testabilidade, manutenção e escalabilidade organizacional. Desvantagens: overhead, rigidez, mudanças transversais e exigência de planejamento.
**Conceito-chave para a prova:** a camada de **Aplicação/Serviço orquestra** a lógica entre apresentação e domínio, e o **Domínio** guarda as **regras puras**. Camadas **lógicas** não são camadas **físicas**: as mesmas camadas podem rodar num monolito ou em serviços distribuídos. Desvantagens que caem: **overhead** entre camadas e dificuldade com **mudanças transversais**.

---

## I20 — Cliente-servidor e microsserviços
**Subtópico coberto:** 5.4, Cliente-servidor e microsserviços (apostila p. 59–61; numerada "5.3" por erro no corpo da apostila)
**Por que é provável:** a apostila traz o exemplo da Black Friday, do serviço de Recomendações que trava, do banco de dados por serviço ("regra de ouro") e do API Gateway. É um cenário pronto para questão.
**Prioridade:** Média
**Tipo ENADE:** Resposta única

**Enunciado:**
Um e-commerce migrou seu servidor monolítico, um único bloco de código com login, catálogo, carrinho, pagamento e recomendações ligados a um único banco de dados, para uma arquitetura de microsserviços. Agora, cada serviço tem seu próprio banco de dados, e o aplicativo do cliente envia todas as requisições a um API Gateway. Durante a Black Friday, o tráfego nos serviços de Carrinho e Pagamento aumentou dez vezes e, no pico, o serviço de Recomendações travou. Considerando as características da arquitetura de microsserviços, assinale a alternativa correta.

**Alternativas:**
- **A)** É possível escalar apenas os serviços de Carrinho e Pagamento, e o cliente ainda consegue finalizar a compra, pois a falha do serviço de Recomendações não afeta o serviço de Checkout.
- **B)** Toda a aplicação precisa ser escalada em conjunto, pois, na arquitetura de microsserviços, todos os serviços compartilham um único banco de dados central.
- **C)** Como os microsserviços substituem o modelo cliente-servidor, o aplicativo do usuário deixa de atuar como cliente e passa a processar as regras de negócio localmente.
- **D)** A falha do serviço de Recomendações deixa todos os clientes inoperantes, já que cada requisição precisa passar por todos os microsserviços antes de retornar.
- **E)** A tolerância a falhas só é obtida se todos os serviços forem escritos na mesma linguagem e usarem o mesmo SGBD, garantindo padronização tecnológica.

**Gabarito: A**

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — É a **escalabilidade isolada** ("você não precisa escalar o sistema inteiro, apenas multiplica os servidores do serviço de 'Pagamento' e 'Carrinho'") e a **tolerância a falhas** ("Se o microsserviço de 'Recomendações' travar, o usuário ainda consegue finalizar a compra") descritas na p. 61.
- **B) ❌** — Contradiz a "regra de ouro": cada microsserviço tem **banco de dados independente**.
- **C) ❌** — "Os microsserviços não substituem a ideia de cliente-servidor; eles revolucionam a forma como o Servidor é construído" (p. 60). O celular continua sendo o cliente.
- **D) ❌** — Esse comportamento ("sistema fora do ar") é do servidor **monolítico**. No modelo novo, o API Gateway roteia cada pedido só para o microsserviço específico.
- **E) ❌** — Microsserviços permitem **independência tecnológica** (Pagamento em Java com Oracle, Recomendações em Python com MongoDB, p. 61).

**Base no material:** p. 59–61 (cliente, servidor, monolito, microsserviços, vantagens, "ponto-chave da evolução": API Gateway como maestro).
**Conceito-chave para a prova:** cliente-servidor define **quem pede e quem responde**. Microsserviços definem **como o servidor é construído por dentro**, e todo sistema de microsserviços continua sendo cliente-servidor. Vantagens: **escalabilidade isolada, tolerância a falhas e independência tecnológica**. Regra de ouro: **um banco por serviço**. O ponto de entrada é o **API Gateway**. Custo, segundo a p. 58: orquestração, observabilidade e versionamento mais complexos.

---

## I21 — Padrões GoF: famílias e exemplos
**Subtópico coberto:** 5.5, Design Patterns e GoF (apostila p. 62–63). A QP do professor cobre só o Observer.
**Por que é provável:** a apostila traz as 3 famílias e os 23 padrões, os 4 elementos obrigatórios e três exemplos práticos (Factory Method, Adapter, Strategy) que a QP não usa. O exemplo de frete por Correios ou Transportadora é um cenário pronto.
**Prioridade:** Média
**Tipo ENADE:** Resposta única ("respectivamente")

**Enunciado:**
A equipe de um marketplace precisa resolver três problemas de projeto orientado a objetos:

1. O cálculo do frete deve alternar, em tempo de execução, entre as regras dos Correios e de uma transportadora, cada uma encapsulada como um algoritmo intercambiável.
2. É preciso integrar uma API externa e legada de antifraude, cuja interface é incompatível com a esperada pela aplicação, sem refatorações drásticas.
3. A criação dos objetos de pagamento (Cartão ou Pix) deve ser delegada a subclasses ou fábricas concretas, para que o código cliente não fique acoplado às implementações e não precise de múltiplos blocos if/switch.

Considerando o catálogo de 23 padrões da Gang of Four (GoF), os padrões indicados para os problemas 1, 2 e 3 e as famílias a que pertencem são, respectivamente:

**Alternativas:**
- **A)** Strategy (criacional); Facade (estrutural); Singleton (criacional).
- **B)** Observer (comportamental); Adapter (estrutural); Abstract Factory (estrutural).
- **C)** Template Method (estrutural); Proxy (comportamental); Factory Method (criacional).
- **D)** Strategy (comportamental); Adapter (estrutural); Factory Method (criacional).
- **E)** Strategy (comportamental); Bridge (criacional); Builder (comportamental).

**Gabarito: D**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — O Strategy é **comportamental**, não criacional. O Facade simplifica o acesso a um subsistema e não converte uma interface incompatível. O Singleton garante instância única e não resolve a escolha da classe a instanciar.
- **B) ❌** — O Observer notifica dependentes de uma mudança de estado e não troca algoritmos. O Abstract Factory é **criacional**, não estrutural.
- **C) ❌** — Erra as famílias: o Template Method é comportamental e o Proxy é estrutural. Também erra os padrões dos problemas 1 e 2.
- **D) ✅** — **Strategy** (comportamental) encapsula uma família de algoritmos intercambiáveis, como o frete. **Adapter** (estrutural) converte a interface de uma API externa ou legada. **Factory Method** (criacional) encapsula a criação de objetos em subclasses ou fábricas e evita if/switch (p. 63).
- **E) ❌** — O Bridge é **estrutural** e não é a solução clássica para integrar interface incompatível. O Builder é **criacional**.

**Base no material:** p. 62–63. Origem: Christopher Alexander (1977), Beck e Cunningham (1987), GoF (1994). Elementos: nome, problema, solução e consequências. Famílias: criacionais (Abstract Factory, Builder, Factory Method, Prototype, Singleton), estruturais (Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy) e comportamentais (Chain of Responsibility, Command, Interpreter, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, Visitor).
**Conceito-chave para a prova:** a família se descobre pelo **verbo**. **Criar** objetos = criacional (5). **Compor e estruturar** classes e objetos = estrutural (7). **Distribuir responsabilidades e comunicação** = comportamental (11). Um padrão de projeto "não representa código pronto ou bibliotecas", e sim um **modelo genérico** de solução. Observer, Composite, Interpreter, Mediator e Proxy também funcionam como **táticas arquiteturais** (p. 63).

---

## I22 — ADR e trade-offs
**Subtópico coberto:** 5.6, Architecture Decision Records (ADR) e análise de trade-offs (apostila p. 64–65)
**Por que é provável:** a seção traz regras pontuais e cobráveis: append-only, superseding, estrutura título/data/status/contexto/decisão/consequências, Y-Statement e a "Primeira Lei da Arquitetura".
**Prioridade:** Média
**Tipo ENADE:** Afirmativas múltiplas (I–IV)

**Enunciado:**
Uma equipe de arquitetura decidiu adotar um cache distribuído para reduzir a latência do catálogo de produtos e registrou a decisão no documento "ADR-007 — Adoção de cache distribuído", armazenado no diretório `doc/adr` do repositório. Seis meses depois, uma mudança no volume de acessos exigiu rever essa decisão. Sobre Architecture Decision Records (ADR) e análise de trade-offs, avalie as afirmações a seguir.

I. Uma ADR típica tem título numerado sequencialmente, data e status (proposto, aceito, rejeitado ou substituído), contexto, decisão com as alternativas consideradas e descartadas, e consequências ou trade-offs, incluindo os débitos técnicos conscientemente aceitos.

II. Como a decisão mudou, a equipe deve editar o próprio ADR-007 para refletir a nova escolha, mantendo um único registro sempre atualizado e evitando duplicidade de documentos.

III. Pela Primeira Lei da Arquitetura de Software, não existem soluções perfeitas, apenas trade-offs. Por exemplo, adicionar camadas de abstração eleva a modificabilidade e a modularidade, mas introduz overhead de comunicação e aumenta a latência.

IV. O formato Y-Statement padroniza a escrita sintética da decisão: "No contexto de [sistema], enfrentando [problema], decidimos por [decisão] (e não [alternativas descartadas]) para alcançar [resultado], aceitando que [trade-offs]".

É correto o que se afirma em:

**Julgamento das afirmativas:**
- **I — Verdadeira.** É a "Estrutura Básica de uma ADR" (p. 64).
- **II — Falsa.** O repositório de ADRs é **append-only**, um histórico imutável. "Registros aceitos não devem ser editados posteriormente". A equipe deve criar um **novo** ADR que **substitui (supersedes)** o ADR-007, com link entre os dois, preservando a rastreabilidade histórica (p. 64).
- **III — Verdadeira.** É o trade-off "Desempenho vs. Modificabilidade" da p. 65.
- **IV — Verdadeira.** É o modelo Y-Statement da p. 65.

**Alternativas:**
- **A)** I e II, apenas.
- **B)** II e III, apenas.
- **C)** I, III e IV, apenas.
- **D)** II, III e IV, apenas.
- **E)** I, II, III e IV.

**Gabarito: C**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Inclui a II (falsa) e omite III e IV.
- **B) ❌** — Inclui a II e omite I e IV.
- **C) ✅** — I, III e IV são verdadeiras. A II viola o princípio append-only.
- **D) ❌** — Inclui a II e omite a I.
- **E) ❌** — A II é falsa.

**Base no material:** p. 64–65. ADR proposto por Michael Nygard (2011). Modelo Debt-Aware. Princípio append-only. Superseding. Y-Statement e Decision Story. Trade-offs: desempenho × modificabilidade, desempenho × disponibilidade (replicação) e o Proxy como resolvedor de conflito (carregamento sob demanda).
**Conceito-chave para a prova:** **ADR não se edita, se substitui** (novo ADR com status "Substituído" no antigo e link entre os dois). "Não existem soluções perfeitas em arquitetura, apenas **trade-offs**". Ganhar modificabilidade custa desempenho, e ganhar disponibilidade (replicação) custa recursos.

---

## I23 — Verificação × validação
**Subtópico coberto:** 6.1, Verificação e Validação (apostila p. 66–68)
**Por que é provável:** a seção abre o Módulo 6 com as "duas perguntas clássicas", o modelo V, uma tabela "Comparativo Direto" e o exemplo da casa (passou na verificação, falhou na validação). Esse exemplo pode ser transposto para software em uma asserção-razão.
**Prioridade:** Alta
**Tipo ENADE:** Asserção-razão

**Enunciado:**
Uma rede de supermercados contratou o desenvolvimento de um sistema de controle de ponto eletrônico. Ao longo da construção, a equipe técnica fez revisões de código, inspeções de documentos, análise estática e testes unitários e de integração, e confirmou que o sistema seguia exatamente o documento de requisitos e os diagramas UML aprovados. No teste de aceitação em homologação, porém, os gerentes das lojas perceberam que o sistema não tratava a escala de trabalho 12×36 usada pelos vigilantes e que, por isso, não resolvia o problema real de apuração das horas.

Analise as asserções a seguir e a relação proposta entre elas:

I. O sistema foi aprovado na verificação, mas reprovado na validação.

**PORQUE**

II. A verificação responde à pergunta "estamos construindo o produto corretamente?" e confere a conformidade com as especificações por meio de revisões, análises estáticas e testes unitários e de integração. A validação responde à pergunta "estamos construindo o produto certo?" e confere se o produto resolve o problema real do cliente, por exemplo por meio de testes de aceitação do usuário.

**Julgamento:**
- **Asserção I — Verdadeira.** O produto seguiu as especificações (verificação) mas não atende à necessidade real (validação). É a mesma situação da casa construída "exatamente como estava na planta", com portas estreitas demais para a geladeira (p. 67–68).
- **Asserção II — Verdadeira.** São as definições, os "como é feita" e as perguntas-chave da apostila (p. 66–67).
- **Relação — II justifica I.** A I só pode ser afirmada porque as atividades executadas (revisões, análise estática, testes unitários e de integração) são de **verificação**, e a falha apareceu no **teste de aceitação**, que é atividade de **validação**.

**Alternativas:**
- **A)** As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
- **B)** As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
- **C)** A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
- **D)** A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
- **E)** As asserções I e II são proposições falsas.

**Gabarito: A**

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — As duas asserções são verdadeiras, e a II explica por que o caso é "verificação ok, validação falhou".
- **B) ❌** — Há nexo causal direto: a II classifica as atividades que aparecem no cenário.
- **C) ❌** — A II reproduz as definições do material.
- **D) ❌** — A I é verdadeira. Quem inverte os conceitos ("verificação = produto certo") cai aqui.
- **E) ❌** — As duas são verdadeiras.

**Base no material:** p. 66 (verificação: interna, técnica, foco no processo, sem participação do cliente); p. 67 (validação: externa, voltada ao negócio, UAT, testes beta, testes de sistema; tabela "Comparativo Direto"); p. 67–68 (exemplo da casa e da NR-10); figura do modelo V na p. 66.
**Conceito-chave para a prova:** **Verificação = produto CORRETAMENTE = conforme a especificação.** É feita por desenvolvedores e QA, com revisões, inspeções, análise estática, testes unitários e de integração. **Validação = produto CERTO = conforme a necessidade real.** É feita por usuários e PO, com UAT, beta e testes de sistema. O teste de **sistema** fica na transição entre os dois (p. 69–70).

---

## I24 — Níveis de teste
**Subtópico coberto:** 6.2, Testes unitários, de integração, de sistema e de aceitação (apostila p. 68–70)
**Por que é provável:** cada nível tem foco, executor, ambiente e um **exemplo concreto** (`calcularDesconto`, API + PostgreSQL + RabbitMQ, fluxo PIX, gerente da loja), além do "Comparativo Rápido". Exemplos assim viram itens de associação.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única ("respectivamente")

**Enunciado:**
A equipe de qualidade de uma loja virtual montou o plano de testes da nova versão da plataforma, com quatro atividades:

1. Um desenvolvedor verifica se a função `calcularDesconto(valor, taxa)` retorna 90 quando recebe 100 e 0.10, usando mocks para simular o banco de dados.
2. Desenvolvedores e engenheiros de QA verificam se a API de pedidos grava os dados da compra no PostgreSQL e publica uma mensagem na fila do RabbitMQ.
3. A equipe de QA, em ambiente de homologação idêntico ao de produção, faz login, adiciona um produto ao carrinho, paga via PIX e confere se o pedido muda para "pago" e se o e-mail de confirmação é disparado.
4. O gerente da loja usa a plataforma em homologação e confirma que os relatórios atendem às regras do setor contábil, aprovando formalmente a liberação para produção.

As atividades 1, 2, 3 e 4 correspondem, respectivamente, aos testes:

**Alternativas:**
- **A)** unitário; de sistema; de integração; de aceitação.
- **B)** de integração; unitário; de aceitação; de sistema.
- **C)** unitário; de integração; de aceitação; de sistema.
- **D)** unitário; de integração; de sistema; de regressão.
- **E)** unitário; de integração; de sistema; de aceitação.

**Gabarito: E**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Troca integração e sistema. A comunicação entre dois módulos (API ↔ banco ↔ fila) é **integração**. O fluxo completo, de ponta a ponta, é **sistema**.
- **B) ❌** — A menor unidade isolada, com mocks, é o teste **unitário**, não o de integração.
- **C) ❌** — Troca sistema e aceitação. Quem executa o teste de sistema é a **equipe de QA**. O teste de aceitação é feito pelo **cliente/usuário/PO** e busca a **aprovação formal**.
- **D) ❌** — Regressão é a reexecução de testes de funcionalidades antigas a cada deploy (p. 75), não um dos 4 níveis. A atividade 4 é aceitação (UAT).
- **E) ✅** — São os exemplos da apostila para cada nível, na ordem da pirâmide: unitário → integração → sistema → aceitação (p. 68–69).

**Base no material:** p. 68–70. "Comparativo Rápido": unitário (verificação, devs), integração (verificação, devs/QA), sistema (verificação + validação, QA), aceitação (validação, cliente/usuário/PO).
**Conceito-chave para a prova:** **Unitário** = função ou classe isolada, com mocks/stubs. **Integração** = interfaces e contratos entre módulos, com dependências reais ou contêineres. **Sistema** = ponta a ponta em staging, incluindo RFs e RNFs. **Aceitação (UAT)** = cliente aprova; inclui testes alfa e beta. Os níveis vão do mais técnico ao mais de negócio.

---

## I25 — Particionamento por equivalência e valor-limite
**Subtópico coberto:** 6.3, técnicas de caixa-preta: particionamento por equivalência e análise do valor-limite (apostila p. 72)
**Por que é provável:** é o único ponto do Módulo 6 com exemplo numérico ("idades de 18 a 60 anos → 17, 18, 19 e 59, 60, 61"). Exemplo numérico costuma virar questão de cálculo com números trocados.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única (cálculo/aplicação)

**Enunciado:**
O cadastro de um aplicativo bancário só aceita senhas com **8 a 16 caracteres** (inclusive). O analista de testes precisa projetar casos de teste de caixa-preta para esse campo e vai aplicar duas técnicas: o particionamento por equivalência, testando apenas um representante de cada classe de entrada (válidas e inválidas), e a análise do valor-limite, testando os pontos críticos de cada borda (o próprio limite, o valor imediatamente abaixo e o imediatamente acima), como faz a apostila do squad.

O número mínimo de casos de teste exigido pelo particionamento por equivalência e o conjunto de comprimentos de senha a testar pela análise do valor-limite são, respectivamente:

**Alternativas:**
- **A)** 2 casos; {8, 16}.
- **B)** 3 casos; {7, 8, 9, 15, 16, 17}.
- **C)** 3 casos; {8, 12, 16}.
- **D)** 1 caso; {7, 8, 16, 17}.
- **E)** 2 casos; {7, 8, 9, 15, 16, 17}.

**Gabarito: B**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Esquece uma das classes inválidas e testa só os limites, sem os vizinhos.
- **B) ✅** — **Particionamento:** há 3 classes, comprimento < 8 (inválida), 8 a 16 (válida) e > 16 (inválida), e um representante por classe dá **3 casos**. **Valor-limite**, como no exemplo da apostila (18 a 60 → 17, 18, 19, 59, 60, 61): borda inferior **7, 8, 9** e borda superior **15, 16, 17** (conferido em Python: `sorted({lo-1, lo, lo+1, hi-1, hi, hi+1})` = [7, 8, 9, 15, 16, 17]).
- **C) ❌** — {8, 12, 16} são só valores válidos (um representante da classe válida e os dois limites). Não testam nenhuma borda inválida.
- **D) ❌** — Um único caso não cobre as classes inválidas. O conjunto de 4 valores omite os vizinhos internos 9 e 15, que o padrão da apostila inclui.
- **E) ❌** — O conjunto de valores-limite está certo, mas o particionamento exige 3 classes, e não 2.

**Base no material:** p. 72: "Particionamento por Equivalência: divide o conjunto de dados de entrada em classes válidas e inválidas. Testa-se apenas um representante de cada classe"; "Análise do Valor Limite... Se um sistema aceita idades de 18 a 60 anos, os testes avaliam exatamente os pontos críticos: 17, 18, 19 e 59, 60, 61".
**Conceito-chave para a prova:** um intervalo [a, b] gera **3 classes** (abaixo, dentro, acima). O valor-limite no padrão do material testa **a−1, a, a+1, b−1, b, b+1**. Outras técnicas de caixa-preta: **tabelas de decisão** e **transição de estados**.
**⚠️ Atenção:** parte da literatura usa o valor-limite "de 2 pontos" (a−1, a, b, b+1 = {7, 8, 16, 17}). Se a prova trouxer só essa opção junto com um número de casos coerente, ela pode ser a esperada. Pelo material do squad, vale o padrão de 3 pontos.

---

## I26 — Caixa-branca, caixa-preta e caixa-cinza
**Subtópico coberto:** 6.3, Caixa-preta e caixa-branca, e o elo intermediário caixa-cinza (apostila p. 70–73)
**Por que é provável:** a seção tem 4 páginas, uma tabela comparativa de 3 colunas e um "Exemplo Prático Integrado" (tela de login com bloqueio após 3 tentativas) que mostra as três abordagens no mesmo cenário.
**Prioridade:** Alta
**Tipo ENADE:** Afirmativas múltiplas (I–IV)

**Enunciado:**
Um sistema de internet banking bloqueia o usuário após três tentativas incorretas de senha. Três profissionais testaram esse recurso: o desenvolvedor inspecionou a função `autenticar()`; um testador enviou requisições pelo Postman ao endpoint `/api/login`; e uma analista de QA usou o navegador como um usuário comum. Sobre as abordagens de teste empregadas, avalie as afirmações a seguir.

I. Ao inspecionar `autenticar()`, verificar se a biblioteca de hash BCrypt é invocada corretamente e se o contador de tentativas incrementa até disparar o bloqueio, o desenvolvedor faz um teste de caixa-branca. A essa abordagem pertencem técnicas como cobertura de decisões e análise de complexidade ciclomática.

II. Ao conferir os códigos HTTP 401 e 429 retornados pelo endpoint e consultar o banco de dados para checar se a flag `is_locked` mudou para `true`, sem alterar o código-fonte, o testador faz um teste de caixa-cinza.

III. Tabelas de decisão e transição de estados (por exemplo, "Ativo → Bloqueado → Desbloqueado") são técnicas de caixa-branca, pois dependem da leitura do código-fonte para identificar os caminhos de execução.

IV. Uma desvantagem da caixa-preta é não conseguir testar caminhos ocultos ou não documentados no código. Uma desvantagem da caixa-branca é não garantir que o software atenda às expectativas do cliente, já que pode testar um código perfeito que executa uma regra de negócio errada.

É correto o que se afirma em:

**Julgamento das afirmativas:**
- **I — Verdadeira.** É o exemplo de caixa-branca da apostila (p. 73). Cobertura de comandos, de decisões e de caminhos e complexidade ciclomática são técnicas de caixa-branca (p. 71).
- **II — Verdadeira.** O testador tem conhecimento **parcial** (APIs, schemas de banco, logs) e não altera o código: é caixa-cinza (p. 72–73).
- **III — Falsa.** Tabelas de decisão e transição de estados são técnicas de **caixa-preta**, baseadas em especificação, junto com particionamento e valor-limite (p. 72). Não exigem acesso ao código.
- **IV — Verdadeira.** São as desvantagens listadas para cada abordagem (p. 71–72).

**Alternativas:**
- **A)** I e II, apenas.
- **B)** I e III, apenas.
- **C)** III e IV, apenas.
- **D)** I, II e IV, apenas.
- **E)** I, II, III e IV.

**Gabarito: D**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Omite a IV, que também é verdadeira.
- **B) ❌** — Inclui a III (falsa) e omite II e IV.
- **C) ❌** — Inclui a III e omite I e II.
- **D) ✅** — I, II e IV são verdadeiras. A III troca a família das técnicas.
- **E) ❌** — A III é falsa.

**Base no material:** p. 70–73. Tabela "Comparativo Direto": visibilidade do código total, nenhuma ou parcial; base para os testes no código, nos requisitos/casos de uso ou nos schemas/APIs; nível do modelo V no teste unitário, nos testes de aceitação/sistema ou nos testes de integração/API. O exemplo da tela de login está na p. 73.
**Conceito-chave para a prova:** **Branca** (glass-box, estrutural) = vê o código; é feita por devs e SDETs; usa cobertura e complexidade ciclomática; nível unitário. **Preta** (funcional) = só entradas e saídas; é feita por QA, negócio e usuários; usa particionamento, valor-limite, tabela de decisão e transição de estados; níveis de sistema e aceitação. **Cinza** = conhecimento parcial; usada em testes de API, integração e pentest.

---

## I27 — Casos de teste e testes automatizados
**Subtópico coberto:** 6.4 Casos de teste e 6.5 Testes automatizados, agrupados por serem curtos e relacionados (apostila p. 74–76)
**Por que é provável:** a 6.4 traz uma tabela de campos com exemplo (CT-AUT-001), e a 6.5 traz a lista "Excelente para automação × Melhor manter manual", com critério de ROI. São duas listas fáceis de transformar em afirmativas com troca.
**Prioridade:** Média
**Tipo ENADE:** Afirmativas múltiplas (I–IV)

**Enunciado:**
Uma varejista online passou a fazer deploys diários com integração e entrega contínuas (CI/CD) e reestruturou seu processo de testes. A coordenadora de QA documentou o caso de teste "CT-AUT-001 — Validar bloqueio de login com senha incorreta" e definiu quais testes seriam automatizados. Avalie as afirmações a seguir.

I. Para ser eficaz, um caso de teste deve ser claro, reproduzível, independente de outros testes e rastreável a um requisito, e deve conter campos como ID, título, pré-condições, massa de dados, passos de execução, resultado esperado e pós-condições.

II. No CT-AUT-001, "usuário cadastrado e ativo no sistema" é a pós-condição, e "nenhuma alteração no estado do perfil do usuário" é a pré-condição.

III. Testes de regressão, testes de fumaça (smoke tests), testes de carga e desempenho e testes orientados a dados são bons candidatos à automação, pois se repetem a cada deploy ou são impossíveis de executar manualmente.

IV. Testes exploratórios e testes de usabilidade devem ser os primeiros a ser automatizados, pois o retorno sobre o investimento é maior em funcionalidades instáveis, cujo layout e regras mudam constantemente.

É correto o que se afirma em:

**Julgamento das afirmativas:**
- **I — Verdadeira.** Definição e "Estrutura Fundamental de um Caso de Teste" (p. 74).
- **II — Falsa.** Inverte os campos. "Usuário cadastrado e ativo" é a **pré-condição**, o estado **antes** da execução. "Nenhuma alteração no estado do perfil" é a **pós-condição**, o estado **depois** (p. 74–75).
- **III — Verdadeira.** É a lista "Excelente para Automação" (p. 75).
- **IV — Falsa.** Exploratórios, usabilidade/UX e funcionalidades instáveis estão em "**Melhor Manter Manual**". Para funcionalidades instáveis, "o custo de manutenção do código de teste será maior que a execução manual" (p. 75–76).

**Alternativas:**
- **A)** I e II, apenas.
- **B)** II e IV, apenas.
- **C)** I e III, apenas.
- **D)** I, III e IV, apenas.
- **E)** II, III e IV, apenas.

**Gabarito: C**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Inclui a II, que troca pré e pós-condição.
- **B) ❌** — Inclui as duas falsas.
- **C) ✅** — Só I e III são verdadeiras.
- **D) ❌** — Inclui a IV.
- **E) ❌** — Inclui II e IV e omite a I.

**Base no material:** p. 74–75 (tabela de campos com exemplos: CT-AUT-001; joao@email.com / SenhaErrada123; alerta "Usuário ou senha inválidos"); p. 75–76 (quando automatizar; ferramentas: Postman, RestAssured, Supertest; Cypress, Playwright, Selenium; Appium; JMeter, k6, Locust).
**Conceito-chave para a prova:** a decisão de automatizar depende do **ROI**. **Automatize** o que se **repete** (regressão, smoke, data-driven) ou o que é **impossível manualmente** (carga). **Mantenha manual** o que exige **julgamento humano** (exploratório, usabilidade) ou o que **muda o tempo todo**. Pré-condição = estado **antes**. Pós-condição = estado **depois**.

---

## I28 — Severidade × prioridade de defeitos
**Subtópico coberto:** 6.6, Defeitos e rastreamento: severidade × prioridade (apostila p. 77)
**Por que é provável:** a apostila dá um exemplo de "prioridade alta / severidade baixa" (logotipo errado), um caso clássico de pegadinha, e o arquivo de questões conhecidas lista o tema como de risco.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única

**Enunciado:**
Na véspera do lançamento de uma grande campanha publicitária, a equipe de QA de uma rede de farmácias registrou dois defeitos no sistema:

- **D1:** o logotipo da empresa aparece com o nome digitado errado na página principal de login. O sistema funciona normalmente.
- **D2:** ao salvar um registro no módulo de auditoria anual, que só é usado uma vez por ano e cuja próxima utilização está prevista para daqui a dez meses, um erro de banco de dados derruba completamente o sistema (crash).

Considerando que a severidade mede o impacto técnico da falha e a prioridade mede a urgência de negócio para a correção, assinale a alternativa que classifica corretamente os defeitos D1 e D2.

**Alternativas:**
- **A)** D1: severidade alta e prioridade alta; D2: severidade baixa e prioridade baixa.
- **B)** D1: severidade baixa e prioridade baixa; D2: severidade alta e prioridade alta.
- **C)** D1: severidade alta e prioridade baixa; D2: severidade baixa e prioridade alta.
- **D)** D1 e D2: severidade e prioridade altas, pois todo defeito visível ao usuário deve ser corrigido imediatamente.
- **E)** D1: severidade baixa e prioridade alta; D2: severidade alta e prioridade baixa.

**Gabarito: E**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — O logotipo errado "não quebra o sistema", logo sua severidade é baixa. Um crash completo nunca tem severidade baixa.
- **B) ❌** — Ignora que a prioridade é urgência de negócio. A marca errada às vésperas da campanha "precisa ser corrigida imediatamente".
- **C) ❌** — Inverte os dois eixos nos dois defeitos.
- **D) ❌** — Mistura os conceitos e trata severidade e prioridade como se fossem a mesma coisa. A classificação existe justamente para evitar conflitos entre QA, desenvolvimento e negócio.
- **E) ✅** — D1 é o exemplo da apostila: "não quebra o sistema (baixa severidade), mas prejudica a marca e precisa ser corrigido imediatamente (alta prioridade)". D2 tem o exemplo de severidade alta da apostila (erro de banco que faz o sistema cair ao salvar um registro), mas sem urgência de negócio: o módulo só será usado daqui a dez meses.

**Base no material:** p. 77: "Severidade (Impacto Técnico): Mede o grau de dano que a falha causa..."; "Prioridade (Urgência de Negócio): Mede a rapidez com que a falha deve ser corrigida com base nas necessidades comerciais ou operacionais"; os dois exemplos do texto.
**Conceito-chave para a prova:** **severidade = quanto quebra** (técnico). **Prioridade = quão rápido corrigir** (negócio). Os eixos são **independentes**, e os casos cruzados (alta/baixa e baixa/alta) são os que caem.
**⚠️ Atenção:** o caso "severidade alta / prioridade baixa" (D2) não está escrito na apostila. Foi montado aplicando as definições do material. A prioridade é uma decisão de negócio, e o enunciado deixa explícita a falta de urgência para não haver ambiguidade.

---

## I29 — Ciclo de vida do defeito
**Subtópico coberto:** 6.6, Defeitos e rastreamento: ciclo de vida do defeito (apostila p. 76–77)
**Por que é provável:** a apostila numera os 6 estados (Novo → Atribuído → Em Correção → Resolvido → Re-teste → Fechado) e cita a alternativa "Reaberto". Sequência numerada costuma virar questão de ordenação.
**Prioridade:** Alta
**Tipo ENADE:** Ordenação

**Enunciado:**
Em uma fintech, a analista de QA Juliana encontrou uma falha no cálculo de juros do simulador de empréstimos e a registrou no Jira. Os eventos ocorridos a partir daí estão listados abaixo, fora de ordem:

I. Juliana executa novamente o caso de teste que havia gerado a falha original.
II. O líder de desenvolvimento analisa a falha e a atribui ao desenvolvedor Pedro.
III. O teste falha e Juliana registra o defeito no sistema de rastreamento.
IV. A correção funciona e o bug é oficialmente encerrado.
V. Pedro investiga o código-fonte e escreve a correção.
VI. A correção é enviada para o ambiente de homologação (staging).

Assinale a alternativa que apresenta a ordem correta dos eventos, conforme o ciclo de vida do defeito.

**Alternativas:**
- **A)** III – II – V – VI – I – IV
- **B)** III – V – II – VI – I – IV
- **C)** III – II – V – I – VI – IV
- **D)** II – III – V – VI – I – IV
- **E)** III – II – VI – V – I – IV

**Gabarito: A**

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — **Novo** (III) → **Atribuído** (II) → **Em Correção** (V) → **Resolvido/Corrigido** (VI) → **Re-teste** (I) → **Fechado** (IV) (p. 76–77).
- **B) ❌** — O desenvolvedor só corrige depois que o defeito lhe é **atribuído**.
- **C) ❌** — Faz o re-teste antes de a correção chegar ao ambiente de testes.
- **D) ❌** — O líder não pode atribuir um defeito que ainda não foi registrado.
- **E) ❌** — Envia a correção ao staging antes de ela ser escrita.

**Base no material:** p. 76–77 (ciclo de 6 estados; "Alternativa: Reaberto (Reopened) caso o defeito persistir durante o re-teste"; anatomia do bug report: título claro, passos para reproduzir, resultado obtido × esperado, ambiente, evidências; ferramentas Jira, Azure DevOps, Bugzilla, Redmine, Trello).
**Conceito-chave para a prova:** **N-A-C-R-R-F** (Novo, Atribuído, em Correção, Resolvido, Re-teste, Fechado). Se o re-teste falhar, o status vira **Reaberto** e o defeito volta ao fluxo. "Resolvido" significa que a correção foi **enviada** ao staging; "Fechado" significa que o QA **confirmou** a correção.

---

## I30 — Diagrama de classes: visibilidade e escopo
**Subtópico coberto:** 7.2, Diagrama de classes: modificadores de acesso e escopos de membros (apostila p. 83–84; slides p. 65)
**Por que é provável:** os slides e a apostila listam os 6 símbolos (+, −, #, ~, /, sublinhado) e explicam classificador × instância. É conteúdo de memorização típico de questão de lacunas aplicada a um diagrama.
**Prioridade:** Alta
**Tipo ENADE:** Lacunas (aplicada a um diagrama)

**Enunciado:**
Um analista modelou a classe a seguir no diagrama de classes de um sistema bancário:

| **ContaBancaria** |
|---|
| − saldo: double |
| # agencia: String |
| ~ codigoInterno: int |
| / saldoDisponivel: double |
| + <u>taxaJuros</u>: double _(nome sublinhado no diagrama)_ |
| + depositar(valor: double): void |

[Figura: retângulo de classe UML com três compartimentos. No superior, o nome "ContaBancaria" em negrito e centralizado. No central, os cinco atributos acima. No inferior, a operação `depositar`.]

Considerando a notação UML de visibilidade e de escopo de membros, complete as lacunas:

"No diagrama, o atributo `saldo` tem visibilidade ______; `agencia` tem visibilidade ______; `codigoInterno` tem visibilidade ______; `saldoDisponivel` é um atributo ______; e `taxaJuros`, por estar sublinhado, é um membro ______, cujo valor é o mesmo em todas as instâncias."

**Alternativas:**
- **A)** privada; de pacote; protegida; derivado; estático.
- **B)** protegida; privada; de pacote; estático; derivado.
- **C)** pública; protegida; de pacote; derivado; abstrato.
- **D)** privada; protegida; de pacote; derivado; estático.
- **E)** privada; protegida; derivado; de pacote; de instância.

**Gabarito: D**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Troca `#` (protegido) e `~` (pacote).
- **B) ❌** — O `−` é **privado**, não protegido. O `/` indica **derivado** e o sublinhado indica **estático**, e a alternativa inverte os dois.
- **C) ❌** — O `−` não é público (público é `+`). O sublinhado indica estático, não abstrato.
- **D) ✅** — `+` público, `−` privado, `#` protegido, `~` pacote, `/` derivado, sublinhado = estático, ou seja, escopo de **classificador**: "os valores dos atributos permanecem os mesmos em todas as instâncias" (p. 84; slides p. 65).
- **E) ❌** — Troca `/` e `~`. Membro sublinhado é de **classificador**, não de **instância**: texto sem formatação indica instância.

**Base no material:** apostila p. 84 e slides p. 65 ("Público (+), Privado (-), Protegido (#), Pacote (~), Derivado (/), Estático (sublinhado)"; "Para indicar um classificador, basta sublinhar seu nome"). Seções da classe na p. 83: o nome é obrigatório, começa com maiúscula, vai em negrito e centralizado.
**Conceito-chave para a prova:** **+ público · − privado · # protegido · ~ pacote · / derivado · sublinhado estático.** Só o compartimento do **nome** é obrigatório. Os atributos e as operações são opcionais (p. 82–83).

---

## I31 — Diagrama de classes: herança e multiplicidade
**Subtópico coberto:** 7.2, Diagrama de classes: interações (herança/generalização, associação bidirecional e unidirecional, multiplicidade) (apostila p. 84–85; slides p. 66–68)
**Por que é provável:** os slides trazem 3 páginas com os exemplos Veículo/Carro, Car/RoadTrip (multiplicidades 0..1 e 0..*) e radar de velocidade (associação unidirecional). Asserção-razão com duas verdades sem nexo é um formato que o squad ainda não usou.
**Prioridade:** Alta
**Tipo ENADE:** Asserção-razão

**Enunciado:**
Uma locadora de veículos está modelando seu sistema com diagramas de classes UML. A classe `Veiculo` tem os atributos velocidade, número de passageiros e combustível e os métodos `go()`, `stop()` e `changeDirection()`. A classe `Carro` acrescenta tipo de modelo, número de portas e fabricante, além de métodos próprios. A classe `Carro` também se associa à classe `Viagem`: na extremidade de `Viagem`, a multiplicidade é 0..*, já que um carro pode fazer várias viagens.

Analise as asserções a seguir e a relação proposta entre elas:

I. A relação entre `Carro` e `Veiculo` deve ser representada por uma linha sólida com seta fechada e vazia apontando para `Veiculo`, e `Carro` herda todos os atributos e métodos de `Veiculo`, além de ter os seus próprios.

**PORQUE**

II. Em um diagrama de classes, a multiplicidade 0..* na extremidade de uma associação indica que uma instância pode estar ligada a nenhuma ou a várias instâncias da outra classe.

**Julgamento:**
- **Asserção I — Verdadeira.** A herança (generalização) "é mostrada em um diagrama de classes usando uma linha sólida com uma seta fechada e vazia" apontando para a superclasse, e "Carro" herda os atributos e métodos de "Veículo" além dos seus (slides p. 66; apostila p. 84–85).
- **Asserção II — Verdadeira.** No exemplo dos slides, "um carro poderia fazer várias viagens: o valor da multiplicidade é definido como 0..*" (p. 67).
- **Relação — a II não justifica a I.** A notação e a semântica da **herança** não decorrem da **multiplicidade** de uma **associação**. São relacionamentos diferentes, e a generalização nem tem multiplicidade.

**Alternativas:**
- **A)** As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
- **B)** As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
- **C)** A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
- **D)** A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
- **E)** As asserções I e II são proposições falsas.

**Gabarito: B**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — É a armadilha clássica: as duas são verdadeiras, mas tratam de relacionamentos distintos.
- **B) ✅** — As duas são verdadeiras e não há relação de causa entre elas.
- **C) ❌** — A II é verdadeira.
- **D) ❌** — A I é verdadeira. Quem confunde a seta de herança com a seta aberta da associação unidirecional pode marcar aqui.
- **E) ❌** — As duas são verdadeiras.

**Base no material:** slides p. 66 (herança), p. 67 (associação bidirecional: "linha reta entre duas classes"; multiplicidades 0..1 e 0..*) e p. 68 (associação unidirecional: "ponta de seta aberta da classe que conhece para a classe conhecida"; exemplo do radar).
**Conceito-chave para a prova:** **herança** = linha sólida + triângulo **vazado** apontando para o **pai**. **Associação bidirecional** = linha simples, e as duas classes se conhecem. **Associação unidirecional** = linha com **seta aberta** apontando da classe que conhece para a classe conhecida. Multiplicidades: **0..1** (nenhum ou um) e **0..*** (nenhum ou muitos).

---

## I32 — Diagrama de sequência: fragmentos alt, opt e loop
**Subtópico coberto:** 7.3, Diagrama de sequência: alternativas, opções e ciclos (slides p. 77)
**Por que é provável:** os slides trazem uma figura com os três fragmentos combinados em um cenário de compra (pagamento confirmado/recusado, cupom de desconto, verificação de cada item do carrinho). É o mesmo domínio da Q4 (e-commerce, cupom), o que favorece uma questão "respectivamente".
**Prioridade:** Alta
**Tipo ENADE:** Resposta única ("respectivamente")

**Enunciado:**
Ao modelar o diagrama de sequência do processo de checkout de uma loja virtual, a analista precisou representar três trechos da interação:

1. Para cada item do carrinho, o sistema consulta o serviço de estoque para verificar a disponibilidade.
2. Se o pagamento for confirmado, o sistema exibe a confirmação do pedido. Caso contrário, exibe uma mensagem de falha no pagamento. Apenas um desses fluxos é executado.
3. Somente se o cliente informar um código de cupom, o sistema aplica o desconto e atualiza o total.

Os quadros (fragmentos combinados) da UML adequados para representar os trechos 1, 2 e 3 são, respectivamente:

**Alternativas:**
- **A)** loop; opt; alt.
- **B)** alt; alt; opt.
- **C)** loop; alt; opt.
- **D)** opt; alt; loop.
- **E)** loop; par; opt.

**Gabarito: C**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Inverte opt e alt. Dois caminhos mutuamente exclusivos são **alt**. Um único caminho condicional é **opt**.
- **B) ❌** — A repetição "para cada item" é **loop**, e não alternativa.
- **C) ✅** — **loop**: "sequência de mensagens que se repetem até que uma condição seja atendida", aqui `[para cada item do carrinho]`. **alt**: "possíveis fluxos de interação, onde apenas um é executado se uma condição for atendida", aqui `[pagamento confirmado]` / `[pagamento recusado]`. **opt**: "um único caminho que é executado somente se sua condição for verdadeira", aqui `[cliente informa cupom]` (slides p. 77).
- **D) ❌** — Inverte loop e opt.
- **E) ❌** — **par** representa fluxos executados em **paralelo**, não escolha condicional entre dois fluxos.

**Base no material:** slides p. 77. A figura mostra "Alternative" ([Payment confirmed]/[Payment declined]), "Option" ([Customer enters discount code]) e "Loop" ([For each item in cart]). "Os três elementos incluem texto entre colchetes para fornecer contexto adicional, como a condição necessária."
**Conceito-chave para a prova:** **alt** = if/else (vários caminhos, só um executa). **opt** = if sem else (um caminho, executa ou não). **loop** = repetição. A condição de guarda vai **entre colchetes**.

---

## I33 — Diagrama de sequência: símbolos e DSS
**Subtópico coberto:** 7.3, Diagrama de sequência: linhas de vida, ativação, mensagens e Diagrama de Sequência do Sistema (DSS) (apostila p. 87–92; slides p. 70–76)
**Por que é provável:** os slides dedicam 4 páginas aos símbolos (linha de vida, ator, caixa de ativação, mensagem de retorno, auto-mensagem, criação e destruição), e a apostila explica o DSS como "caixa-preta". O DSS é um bom alvo para afirmativa falsa.
**Prioridade:** Alta
**Tipo ENADE:** Afirmativas múltiplas (I–IV)

**Enunciado:**
Um hospital está documentando o processo de agendamento de exames do seu sistema de gestão hospitalar com diagramas de sequência UML, que mostram como e em que ordem um grupo de objetos trabalha em conjunto. Sobre os elementos desse diagrama, avalie as afirmações a seguir.

I. A caixa de ativação, um retângulo fino sobre a linha de vida, indica que o objeto está envolvido na operação iniciada por uma mensagem. Quanto mais tempo a tarefa leva, maior é o retângulo.

II. A mensagem de retorno é representada por uma seta tracejada e é enviada quando o receptor termina de processar uma mensagem e devolve o controle ao chamador. A auto-mensagem, uma seta em forma de U, representa uma operação interna do próprio objeto.

III. A mensagem de destruição remove um objeto existente e é marcada com um X na linha de vida destruída. A mensagem de criação adiciona um novo objeto ao diagrama.

IV. No Diagrama de Sequência do Sistema (DSS), o sistema é detalhado em todos os seus objetos internos, e os atores externos não aparecem, pois o foco é a colaboração entre as classes.

É correto o que se afirma em:

**Julgamento das afirmativas:**
- **I — Verdadeira.** Slides p. 74 e tabela de símbolos da apostila (p. 89).
- **II — Verdadeira.** Slides p. 75.
- **III — Verdadeira.** Slides p. 76.
- **IV — Falsa.** É o oposto. O DSS "normalmente trata o sistema como uma '**caixa-preta**' e se concentra no fluxo de eventos **do ator externo** ao sistema de um caso de uso específico" (apostila p. 87; também p. 91). Quem modela a colaboração de vários objetos internos é o diagrama de sequência **padrão**.

**Alternativas:**
- **A)** I e II, apenas.
- **B)** I e IV, apenas.
- **C)** II e III, apenas.
- **D)** II, III e IV, apenas.
- **E)** I, II e III, apenas.

**Gabarito: E**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Omite a III, que também é verdadeira.
- **B) ❌** — Inclui a IV, que inverte o conceito de DSS.
- **C) ❌** — Omite a I.
- **D) ❌** — Inclui a IV e omite a I.
- **E) ✅** — I, II e III são verdadeiras. A IV é falsa.

**Base no material:** apostila p. 87–92 (definição: também chamado de diagrama de eventos ou cenário de eventos; DSS; benefícios; usos: cenário de uso, lógica do método, lógica de serviço; símbolos); slides p. 70–76.
**Conceito-chave para a prova:** **linha de vida** = linha tracejada vertical (passagem do tempo). **Ativação** = retângulo fino (o objeto está trabalhando). **Retorno** = seta **tracejada**. **Auto-mensagem** = seta em **U**. **Destruição** = **X**. O diagrama de sequência é um **diagrama de interação**, portanto comportamental. O **DSS** trata o sistema como **caixa-preta** e mostra os eventos ator → sistema de **um caso de uso**.

---

## I34 — Diagrama de atividades
**Subtópico coberto:** Diagrama de atividades, presente só nos slides; a apostila apenas o cita na seção 2.2 (slides p. 79–87; apostila p. 31)
**Por que é provável:** os slides dedicam **9 páginas** a esse diagrama, com símbolos de início, ação, decisão, garfo, junção, final de fluxo, término etc. e um exemplo bancário de saque/depósito. Nenhuma questão conhecida cobra o tema.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única ("respectivamente")

**Enunciado:**
Uma analista está modelando, com um diagrama de atividades UML, o processo de saque em um caixa eletrônico. Depois que o cartão é validado, o processo segue estes passos:

1. O fluxo único se divide em duas atividades executadas simultaneamente: "Registrar log de acesso" e "Consultar saldo".
2. As duas atividades simultâneas se combinam e voltam a formar um único fluxo.
3. O processo segue por caminhos diferentes conforme a condição "[saldo suficiente]" ou "[saldo insuficiente]".
4. Por fim, marca-se o estado final da atividade, que representa a conclusão de **todos** os fluxos do processo.

Os símbolos do diagrama de atividades usados nos passos 1, 2, 3 e 4 são, respectivamente:

**Alternativas:**
- **A)** garfo (fork); junção (barra de sincronização); decisão (losango); término (nó final).
- **B)** junção (barra de sincronização); garfo (fork); decisão (losango); final de fluxo.
- **C)** garfo (fork); junção (barra de sincronização); decisão (losango); final de fluxo.
- **D)** decisão (losango); junção (barra de sincronização); garfo (fork); término (nó final).
- **E)** garfo (fork); decisão (losango); junção (barra de sincronização); término (nó final).

**Gabarito: A**

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — **Garfo**: "divide um único fluxo de atividade em duas atividades simultâneas". **Junção/barra de sincronização**: "combina duas atividades simultâneas e as reintroduz em um fluxo onde apenas uma atividade ocorre por vez". **Decisão**: losango com pelo menos dois caminhos e texto de condição. **Término**: "marca o estado final de uma atividade e representa a conclusão de todos os fluxos" (slides p. 83 e 86).
- **B) ❌** — Inverte garfo e junção, e usa final de fluxo no lugar de término.
- **C) ❌** — Os três primeiros estão certos, mas o **final de fluxo** encerra só **um** fluxo específico e "não deve representar o fim de todos os fluxos em uma atividade. Nesse caso, use o símbolo de término" (slides p. 85).
- **D) ❌** — A divisão em atividades simultâneas não é uma decisão, porque na decisão só **um** caminho é seguido.
- **E) ❌** — Troca a ordem de decisão e junção.

**Base no material:** slides p. 79 (diagrama de comportamento, junto com casos de uso e máquina de estados), p. 81 (nó inicial = círculo preto; nó final = círculo preto contornado; nó de decisão = losango com uma entrada e duas ou mais saídas), p. 82–86 (símbolos) e p. 87 (exemplo bancário de saque/depósito).
**Conceito-chave para a prova:** **garfo = 1 → N simultâneos. Junção = N simultâneos → 1. Decisão = escolhe 1 de N caminhos, com condição entre colchetes. Final de fluxo = encerra um ramo. Término/nó final = encerra a atividade inteira.** Nó inicial = círculo preto. Nó final = círculo preto contornado.

---

## I35 — Diagrama de componentes
**Subtópico coberto:** 7.4, Diagrama de componentes (apostila p. 93–98; slides p. 88–96)
**Por que é provável:** os slides detalham símbolos de componente, nó, interface, porta, pacote, nota e dependência, e reservam uma página só para interface fornecida × necessária ("pirulito" × "soquete"). O exemplo do sistema de bibliotecas (slides p. 96) dá um cenário pronto.
**Prioridade:** Média
**Tipo ENADE:** Resposta única

**Enunciado:**
No diagrama de componentes UML de um sistema de gerenciamento de bibliotecas, o componente `Catálogo` disponibiliza o serviço `IConsultaLivros`, e o componente `Empréstimo` precisa desse serviço para verificar se um livro está disponível antes de registrar o empréstimo. A ligação entre os dois foi desenhada com a notação "bola-e-soquete".

A notação de `IConsultaLivros` junto ao componente `Catálogo` e junto ao componente `Empréstimo` corresponde, respectivamente, a:

**Alternativas:**
- **A)** interface necessária (linha com círculo) junto a `Catálogo` e interface fornecida (linha com semicírculo) junto a `Empréstimo`.
- **B)** porta (pequeno quadrado) junto a `Catálogo` e dependência (linha sólida com triângulo vazado) junto a `Empréstimo`.
- **C)** interface fornecida (linha com semicírculo) junto a `Catálogo` e interface necessária (linha com círculo) junto a `Empréstimo`.
- **D)** interface fornecida (linha com círculo, o "pirulito") junto a `Catálogo` e interface necessária (linha com semicírculo, o "soquete") junto a `Empréstimo`.
- **E)** nó (caixa tridimensional) junto a `Catálogo` e artefato (retângulo com «artifact») junto a `Empréstimo`.

**Gabarito: D**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Inverte os papéis: quem **disponibiliza** o serviço (`Catálogo`) tem a interface **fornecida**.
- **B) ❌** — A porta é um ponto de interação separado entre o componente e o ambiente, não a interface fornecida em si. A dependência é representada por linha **tracejada**, não por linha sólida com triângulo, que é a notação de herança.
- **C) ❌** — Inverte os símbolos: o **círculo** é a fornecida e o **semicírculo** é a necessária.
- **D) ✅** — "Interface fornecida: uma linha reta a partir da caixa de componentes e com um círculo anexado... a interface na qual um componente produz informações usadas pela interface necessária de outro componente". "Interface necessária: uma linha reta... com um semicírculo anexado... a interface na qual um componente requer informações para executar a função correta" (slides p. 95; figura renderizada).
- **E) ❌** — Nó e artefato pertencem ao **diagrama de implementação**, e o nó é de nível superior aos componentes.

**Base no material:** slides p. 88 (componente = módulo de classes que representa sistemas ou subsistemas independentes; desenvolvimento baseado em componentes, CBD), p. 91–93 (componente, nó, interface "pirulito, soquete e bola-e-soquete", porta = pequeno quadrado, pacote, nota, dependência = linha tracejada), p. 94–95 (interfaces) e p. 96 (sistema de bibliotecas); apostila p. 93–98.
**Conceito-chave para a prova:** **pirulito (○) = fornece. Soquete (◡) = requer.** Os dois juntos formam a "bola-e-soquete". **Porta** = quadradinho. **Dependência** = linha tracejada com seta. Componentes e pacotes ligam-se por conectores de **montagem** e de **delegação**. O nome do componente leva o estereótipo «component» e/ou o ícone, para não ser confundido com uma classe.

---

## I36 — Diagrama de implementação
**Subtópico coberto:** 7.5, Diagrama de implementação, também chamado de implantação (apostila p. 98–103; slides p. 97–102)
**Por que é provável:** o material define nó de dispositivo × nó de ambiente de execução (EEN: SO, JVM), artefato e percurso de comunicação, e traz o exemplo servidor web + servidor de banco + dispositivo do usuário. Também frisa que o diagrama é **estrutural** e o único que descreve hardware.
**Prioridade:** Média
**Tipo ENADE:** Afirmativas múltiplas (I–IV)

**Enunciado:**
Uma loja virtual documentou a arquitetura física do seu sistema com um diagrama de implementação UML. O diagrama mostra o computador do usuário com o navegador; um servidor web com o sistema operacional Ubuntu e uma JVM, na qual está implantado o arquivo `loja.war`; e um servidor de banco de dados. As caixas que representam os equipamentos estão ligadas por linhas retas. Sobre esse diagrama, avalie as afirmações a seguir.

I. O computador do usuário e os dois servidores são nós de dispositivo. O Ubuntu e a JVM são nós de ambiente de execução (EEN), sistemas de computação que residem dentro de um nó de dispositivo.

II. O arquivo `loja.war`, informação gerada pelo software e implantada na JVM, é um artefato, representado por um retângulo com o estereótipo «artifact» e o nome do arquivo.

III. Por representar o hardware e a distribuição física do software, o diagrama de implementação pertence à família dos diagramas comportamentais da UML.

IV. Esse diagrama permite mostrar quais elementos de software são empregados por quais elementos de hardware e oferece uma visão da topologia do sistema, com os nós ligados por percursos de comunicação.

É correto o que se afirma em:

**Julgamento das afirmativas:**
- **I — Verdadeira.** Nós de dispositivo são recursos de computação com capacidade de processamento, como PCs, laptops e celulares. O EEN "é qualquer sistema de computação que resida dentro de um nó de dispositivo. Pode ser um sistema operacional, um JVM ou outro recipiente web" (slides p. 100; apostila p. 101).
- **II — Verdadeira.** "A informação gerada pelo software é chamada de artefato". O artefato é um retângulo com o nome e a palavra "artefato" (artifact) entre aspas angulares (apostila p. 98 e 100).
- **III — Falsa.** O diagrama de implementação "faz parte da família de diagramação **estrutural**" (p. 98; slides p. 97). Ele é estático e descreve onde cada coisa roda, não comportamento ao longo do tempo.
- **IV — Verdadeira.** Aplicações do diagrama (slides p. 98) e percurso de comunicação como "uma linha reta que representa a comunicação entre dois nódulos de aparelho" (slides p. 101).

**Alternativas:**
- **A)** I e III, apenas.
- **B)** I, II e IV, apenas.
- **C)** II e III, apenas.
- **D)** II, III e IV, apenas.
- **E)** I, II, III e IV.

**Gabarito: B**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Inclui a III (falsa) e omite II e IV.
- **B) ✅** — I, II e IV são verdadeiras. A III troca estrutural por comportamental.
- **C) ❌** — Inclui a III e omite I e IV.
- **D) ❌** — Inclui a III e omite a I.
- **E) ❌** — A III é falsa.

**Base no material:** apostila p. 98–103 (definição, aplicações, diretrizes, elementos: artefato, associação, componente, dependência, interface, nó, nó como contêiner, estereótipo; base de dados; exemplo da p. 103); slides p. 97–102.
**Conceito-chave para a prova:** **nó** = caixa **3D**. **Nó de dispositivo** = hardware (PC, servidor, celular). **EEN** = ambiente dentro do dispositivo (SO, JVM, contêiner web). **Artefato** = arquivo gerado ou implantado (.war, .jar, executável). **Percurso de comunicação** = linha entre nós. É diagrama **estrutural**, "único no universo UML" por descrever hardware. A apostila usa "implantação" (p. 30) e "implementação" (p. 98) como sinônimos para o mesmo diagrama (deployment).

---

## Observações finais
- **Por que tantas questões:** o material do Squad 8 é muito extenso (2 PDFs de 106 p. cada, 32 subseções), e as 4 questões objetivas conhecidas cobrem só os 4 blocos dos slides (Ágil, Fluxos, Requisitos, UML/casos de uso). Os Módulos 5 (POO/arquitetura/design) e 6 (V&V e testes) da apostila não têm nenhuma questão conhecida. Se o banco do squad seguir a premissa "1 questão por subtópico", é ali que estão as questões que faltam.
- **Prioridade de estudo sugerida:** (1) temas dos slides sem questão: ISO 25010 (I8, I9), frameworks ágeis (I13, I14), PMBOK (I15), RUP (I11), elicitação (I5, I6), diagramas de classes, sequência, atividades, componentes e implementação (I30–I36); (2) temas clássicos de ENADE na apostila: SOLID (I17, I18), V&V (I23), níveis e técnicas de teste (I24–I26), defeitos (I28, I29); (3) os demais.
- **Inconsistências do material que podem aparecer na prova:** a tabela do PMBOK nos slides (p. 18) duplica o rótulo "Construir uma cultura de empoderamento" (explorado em I15). A duração da sprint é de 1 a 4 semanas nos slides e de 2 a 4 semanas na apostila. A apostila numera duas seções como "5.3" (camadas e cliente-servidor). A apostila chama o mesmo diagrama de "implantação" e de "implementação". Os slides e a apostila dizem que atores são "pessoas" (p. 60/79), mas a apostila (p. 80) corrige para "pessoa, organização ou sistema externo".
- **Limitação:** as questões inferidas usam só conteúdo do material do squad. Onde foi preciso complementar com conhecimento-padrão (fragmento `par` em I32, caso "severidade alta / prioridade baixa" em I28, valor-limite de 2 pontos em I25), isso está indicado na própria questão.
