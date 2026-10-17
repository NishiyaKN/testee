# Engenharia de Software — Questões e Gabarito Comentado

**Squad responsável:** Squad 8
**Materiais analisados:**
| Arquivo | Páginas | Tipo | Questões encontradas (páginas) |
|---|---|---|---|
| `ENGENHARIA DE SOFTWARE.pdf` | 106 | Slides (Canva) | Q1 (p. 19–20), Q2 (p. 35–36), Q3 (p. 53–54), Q4 (p. 103–104); exercício discursivo Q5 (p. 61) |
| `APOSTILA DE ESTUDO PARA O ENADE SOBRE ENGENHARIA DE SOFTWARE.pdf` | 106 | Apostila (material explicativo, 7 módulos) | Nenhuma questão. Só teoria. As páginas com pouco texto (42, 89, 90, 95, 96) foram renderizadas: são imagens (fases do RUP e tabelas de símbolos UML de sequência e de componentes), sem questões |
| `Estrutura de Questões sob o padrão do ENADE.pdf` (documento do professor) | 31 | Guia do professor | Questão-exemplo QP (p. 10), Padrão Observer/GoF |

**Resumo:** 6 itens no total. São 4 questões objetivas no padrão ENADE nos slides (Q1–Q4), 1 exercício discursivo nos slides (Q5) e 1 questão-exemplo do professor (QP). **Todos os 6 têm gabarito ou resposta no próprio material.** Os slides trazem "Gabarito" + "Justificativa" no slide seguinte a cada questão, e a resposta do exercício Q5 é o diagrama desenhado no próprio slide. Nenhum item ficou sem gabarito. A apostila não tem nenhuma questão nem exercício: só traz títulos retóricos ("Quais são as 5 etapas...?", "Onde o modelo cascata é mais empregado?"), que não foram contados como questões.

> Legenda: ✅ correta · ❌ incorreta · ⚠️ ponto de atenção (gabarito do material duvidoso, ambiguidade, versão divergente)

## Índice
1. [Q1 — Papéis no Scrum](#q1--papéis-no-scrum)
2. [Q2 — Modelo evolucionário e prototipação](#q2--modelo-evolucionário-e-prototipação)
3. [Q3 — Requisitos não funcionais e arquitetura](#q3--requisitos-não-funcionais-e-arquitetura)
4. [Q4 — Diagrama de casos de uso: include, extend, generalização e atores](#q4--diagrama-de-casos-de-uso-include-extend-generalização-e-atores)
5. [Q5 — Exercício: caso de uso do caixa eletrônico](#q5--exercício-caso-de-uso-do-caixa-eletrônico)
6. [Questão-exemplo do professor (documento Estrutura de Questões ENADE)](#questão-exemplo-do-professor-documento-estrutura-de-questões-enade)
   - [QP — Padrão de projeto GoF Observer](#qp--padrão-de-projeto-gof-observer)
7. [Observações gerais sobre o material](#observações-gerais-sobre-o-material)

---

## Q1 — Papéis no Scrum
**Fonte:** `ENGENHARIA DE SOFTWARE.pdf`, p. 19 (enunciado) e p. 20 (gabarito/justificativa). A questão está só nos slides. A teoria correspondente está na tabela "Atores" (slides p. 16) e na apostila p. 46 (4.3 Scrum e seus papéis).
**Tipo ENADE:** Resposta única (situação-problema + "assinale a alternativa que identifica corretamente ..., respectivamente")

**Enunciado:**
Uma equipe de desenvolvimento de software adotou o Scrum para gerenciar a construção de um aplicativo financeiro. A metodologia ágil otimiza o gerenciamento de projetos ao dividir demandas complexas em ciclos curtos chamados sprints. Durante a execução do projeto, observou-se que o João era o responsável exclusivo por definir a visão do produto, entender as necessidades dos usuários, gerenciar e priorizar dinamicamente a lista de tarefas do projeto (Product Backlog). Por outro lado, a Maria focava em facilitar os processos ágeis, orientar a equipe, atuar como uma líder servidora e remover ativamente os impedimentos que travavam o progresso do time técnico. A partir das responsabilidades descritas, assinale a alternativa que identifica corretamente os papéis desempenhados por João e Maria, respectivamente, dentro do framework Scrum.

**Alternativas:**
- **A)** João é o Scrum Master (SM); Maria é o Product Owner (PO).
- **B)** João é o Líder Técnico de Desenvolvedores; Maria é a Gerente de Projetos (PMBOK).
- **C)** João é o Product Owner (PO); Maria é a Scrum Master (SM).
- **D)** João é o Gerente de Portfólio; Maria é a Desenvolvedora sênior.
- **E)** João e Maria compartilham o papel de Product Owner (PO).

**Gabarito: C** — _(origem: gabarito do próprio material, p. 20)_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Inverte os papéis. Quem define a visão do produto e prioriza o Product Backlog é o PO, não o SM. "Líder servidor" e "remover impedimentos" são atribuições do SM, não do PO. O distrator explora a troca da ordem ("respectivamente").
- **B) ❌** — O Scrum só tem três responsabilidades: PO, Scrum Master e Desenvolvedores. "Líder Técnico" e "Gerente de Projetos" não existem no Scrum. A apostila (p. 46) diz que o Scrum funciona "sem a necessidade de um 'gerente de projeto' tradicional". Além disso, o PMBOK não define papéis do Scrum: é um guia de boas práticas e "não é uma metodologia" (slides p. 17).
- **C) ✅** — Conforme a justificativa do material (p. 20), o **PO** define a visão do produto, maximiza o valor entregue e gerencia/prioriza o Product Backlog, que é exatamente o perfil de João. O **Scrum Master** atua como líder servidor, facilita os processos, orienta a equipe sobre práticas ágeis e remove impedimentos, que é o papel de Maria. Os Desenvolvedores constroem o incremento do produto.
- **D) ❌** — "Gerente de Portfólio" não é papel do Scrum. "Desenvolvedora sênior" contradiz o enunciado, porque Maria não constrói o incremento: ela facilita e remove impedimentos.
- **E) ❌** — O PO é uma única pessoa responsável pelo backlog (não um comitê), e as atividades de Maria (facilitar, líder servidora, remover impedimentos) são de SM, não de PO.

**Conceito-chave para a prova:** PO = **"o quê" e "por quê"**: visão do produto, valor, Product Backlog, priorização, aceitar ou rejeitar entregas. SM = **líder servidor**: facilita cerimônias, remove impedimentos, protege o time, ensina Scrum. Desenvolvedores = **"como"**: auto-organizados, estimam, constroem e testam o incremento. Se a versão da prova trocar as descrições entre João e Maria, a resposta passa a ser a inversa (alternativa tipo A).

---

## Q2 — Modelo evolucionário e prototipação
**Fonte:** `ENGENHARIA DE SOFTWARE.pdf`, p. 35 (enunciado) e p. 36 (gabarito/justificativa). A questão está só nos slides. Teoria: slides p. 22–32 (fluxos linear/iterativo/evolucionário/paralelo, Cascata, Prototipação, Espiral) e apostila p. 34–38.
**Tipo ENADE:** Afirmativas múltiplas (I, II, III → "É correto o que se afirma em")

**Enunciado:**
Uma startup de tecnologia da área de saúde está desenvolvendo um novo sistema de prontuário eletrônico. Os desenvolvedores adotaram um ciclo de trabalho em que o software é desenvolvido em ciclos contínuos de planejamento, criação, testes e refinamento. Devido à criticidade das informações e à dificuldade inicial dos médicos em expressarem exatamente o que precisavam, a equipe técnica decidiu criar versões preliminares e simples da interface. Essas versões foram disponibilizadas aos médicos para que pudessem validar o funcionamento na prática, permitindo à equipe entender melhor as necessidades reais antes de iniciar a codificação definitiva e complexa do back-end. Com base nos modelos e fluxos de processos de software, avalie as afirmações a seguir sobre a estratégia adotada pela startup:

I. A equipe está utilizando um modelo de fluxo evolucionário, que permite que o produto se adapte às necessidades do público ao longo do tempo com base em feedback constante.

II. A criação de versões preliminares e simples para validação do funcionamento caracteriza a técnica de Prototipação, que ajuda a entender melhor os requisitos antes do desenvolvimento definitivo.

III. O processo descrito exemplifica o modelo Cascata, pois a fase de levantamento de requisitos com os médicos está sendo finalizada completamente antes do início do projeto e da implementação.

É correto o que se afirma em:

**Julgamento das afirmativas:**
- **I — Verdadeira.** "Ciclos contínuos de planejamento, criação, testes e refinamento" com feedback dos usuários é a definição de fluxo/modelo **evolucionário** dada nos slides (p. 23 e p. 30: "Modelos evolucionários são iterativos").
- **II — Verdadeira.** Criar "versões preliminares e simples para validar o funcionamento com os usuários, permitindo entender melhor os requisitos e aplicar ajustes antes do desenvolvimento definitivo" é a definição literal de **Prototipação** nos slides (p. 31). A prototipação é um dos dois modelos evolucionários, junto com o Espiral.
- **III — Falsa.** O Cascata é linear, rígido e sequencial, sem retorno a etapas concluídas (slides p. 24–27). O cenário é iterativo, com validação contínua por protótipos. A frase "antes de iniciar a codificação definitiva" é a isca: entender requisitos com protótipos antes de codificar não significa fechar completamente uma fase de requisitos, como exige o Cascata.

**Alternativas:**
- **A)** I, apenas.
- **B)** I e II, apenas.
- **C)** II, apenas.
- **D)** II e III, apenas.
- **E)** I, II e III.

**Gabarito: B** — _(origem: gabarito do próprio material, p. 36)_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Omite a II, que também é verdadeira (é a definição de Prototipação).
- **B) ✅** — I e II são verdadeiras e III é falsa. Justificativa do material: o evolucionário foca em ciclos contínuos de aprimoramento com feedback; a Prototipação cria versões preliminares para entender requisitos antes do desenvolvimento definitivo; o Cascata é rígido, sequencial e não permite retorno, o oposto do cenário.
- **C) ❌** — Omite a I. O cenário descreve justamente ciclos contínuos com feedback (evolucionário).
- **D) ❌** — Inclui a III, que é falsa (cenário iterativo ≠ Cascata).
- **E) ❌** — Inclui a III, que é falsa.

**⚠️ Atenção:** a afirmativa II chama a Prototipação de "técnica". Os slides (p. 30–31) a apresentam como **modelo** evolucionário, e a apostila a trata também como **técnica de elicitação** (p. 26/28) e **técnica de validação** de requisitos (p. 11 e p. 21). As três leituras são aceitas no material e o gabarito não muda. Não caia em uma versão que diga "Prototipação não é técnica, é modelo" como motivo para considerar II falsa.

**Conceito-chave para a prova:** Evolucionário = ciclos + feedback (subtipos: **Prototipação** = versões simples para descobrir/validar requisitos; **Espiral** = ciclos com **análise de riscos**). Cascata = linear, sem retorno, requisitos estáveis, documentação extensa, cliente só no início e no fim. Se a versão alterada trocar "versões preliminares" por "análise de riscos a cada ciclo", a afirmativa passaria a descrever o **Espiral**.

---

## Q3 — Requisitos não funcionais e arquitetura
**Fonte:** `ENGENHARIA DE SOFTWARE.pdf`, p. 53 (enunciado) e p. 54 (gabarito/justificativa). A questão está só nos slides. Teoria: slides p. 41–52 (RF × RNF, ISO/IEC 25010:2023) e apostila p. 4–7 ("De requisito vago a requisito testável"; RNFs "resolvidos no nível da arquitetura").
**Tipo ENADE:** Asserção-razão

**Enunciado:**
Na Engenharia de Requisitos, a distinção clara entre Requisitos Funcionais (RF) e Requisitos Não Funcionais (RNF) é determinante para a sustentabilidade arquitetural. Em muitos projetos ágeis, observa-se a tendência de expressar apenas necessidades funcionais na forma de User Stories (Ex.: "Eu como cliente quero visualizar meu extrato"), negligenciando restrições de desempenho, disponibilidade e escalabilidade.

Analise as asserções a seguir e a relação proposta entre elas:

I. Requisitos Não Funcionais (RNFs) devem ser quantificáveis e testáveis por meio de métricas objetivas (como tempo máximo de resposta em milissegundos ou taxa de disponibilidade em porcentagem), evitando-se formulações ambíguas como "o sistema deve ser rápido e amigável".

**PORQUE**

II. RNFs orientam diretamente a definição da arquitetura de software e dos atributos de qualidade do sistema, impactando decisões estruturais que raramente podem ser corrigidas apenas com alterações pontuais na camada de código de uma única funcionalidade.

_(O slide não traz frase de comando após as asserções; as alternativas vêm logo em seguida.)_

**Julgamento:**
- **Asserção I — Verdadeira.** RNFs devem ter critérios mensuráveis (slides p. 42: "Devem ser especificados quantitativamente para permitir testes e validações precisas"; apostila p. 7: "Vago: 'o sistema deve ser rápido'" × "Testável: '95% das requisições devem responder em menos de 300 milissegundos, com 5 mil usuários simultâneos'").
- **Asserção II — Verdadeira.** RNFs são transversais e afetam todas as funcionalidades, por isso "precisem ser resolvidos no nível da arquitetura do software e não na programação" (apostila p. 7). Exemplos: disponibilidade 24×7 exige alta disponibilidade, fall-back e infraestrutura.
- **Relação — segundo o material, II justifica I.** Como as decisões guiadas pelos RNFs são estruturais e caras de reverter, elas precisam ser especificadas com precisão e verificadas objetivamente desde cedo. Por isso os RNFs devem ser quantificáveis.

**Alternativas:**
- **A)** As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
- **B)** As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
- **C)** A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
- **D)** A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
- **E)** As asserções I e II são proposições falsas.

**Gabarito: A** — _(origem: gabarito do próprio material, p. 54)_

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — Justificativa do material (p. 54): a asserção I é verdadeira porque os RNFs especificam atributos de qualidade e restrições técnicas que exigem validação objetiva por testes, o que torna indispensáveis critérios quantificáveis (tempos-limite, percentuais de disponibilidade) em vez de descrições vagas. A II é verdadeira porque os RNFs são os principais direcionadores da arquitetura (infraestrutura, bancos de dados, cache, padrões de comunicação), decisões de alto impacto que não se corrigem com ajustes isolados no código. A II justifica a I porque "a obrigatoriedade de medir e quantificar os RNFs com precisão existe justamente devido ao peso que essas definições exercem sobre as fundações arquiteturais", prevenindo falhas estruturais de difícil reparação.
- **B) ❌** — É o distrator mais forte. Segundo o material, existe relação causal: a quantificação é exigida por causa do impacto arquitetural dos RNFs (ver ⚠️).
- **C) ❌** — A II é verdadeira: RNFs são transversais e tratados na arquitetura (apostila p. 7; trade-offs de atributos de qualidade na apostila p. 65).
- **D) ❌** — A I é verdadeira: RNF vago não é testável e não serve como critério de aceite.
- **E) ❌** — As duas asserções são verdadeiras.

**⚠️ Atenção:** a relação de justificativa é o ponto discutível da questão. A razão **mais direta** para um RNF ser quantificável é a **verificabilidade/testabilidade** (sem métrica não há critério de aceite). A II dá uma razão **indireta**: o alto custo de errar decisões arquiteturais. Um corretor rigoroso poderia defender **B** (ambas verdadeiras, sem relação de causa). Mesmo assim, o material adota **A** e a argumentação é coerente ("é preciso quantificar porque a decisão é estrutural e cara de corrigir"). Na prova, mantenha **A** se o texto for igual a este. Se a versão alterada trocar a II por algo sem nexo causal com a I (ex.: "RNFs são escritos como User Stories" ou "RNFs descrevem o que o sistema faz"), a resposta muda para B ou para D/C, conforme a veracidade.

**Conceito-chave para a prova:** RF = "o que o sistema faz". RNF = "como o sistema se comporta" (atributos de qualidade: desempenho, disponibilidade, segurança, escalabilidade...). RNFs devem ser **mensuráveis/testáveis** e são **transversais e arquiteturais**. Na ISO/IEC 25010:2023 são 9 características: adequação funcional, eficiência de desempenho, compatibilidade, **capacidade de interação** (substitui usabilidade), confiabilidade, segurança (security), manutenibilidade, **flexibilidade** (substitui portabilidade) e **safety** (nova).

---

## Q4 — Diagrama de casos de uso: include, extend, generalização e atores
**Fonte:** `ENGENHARIA DE SOFTWARE.pdf`, p. 103 (enunciado) e p. 104 (gabarito/justificativa). A questão está só nos slides. Teoria: slides p. 58–61 e apostila p. 78–80 (diagrama de casos de uso; a apostila, p. 80, diz que "Ator pode ser uma pessoa, organização ou sistema externo").
**Tipo ENADE:** Afirmativas múltiplas (I a IV → "É correto o que se afirma em")

**Enunciado:**
Durante o levantamento de requisitos de um complexo sistema de e-commerce, o Analista de Requisitos modelou os seguintes cenários no Diagrama de Casos de Uso:
- Ao realizar a ação "Finalizar Compra", o sistema invariavelmente executa a ação "Calcular Frete".
- Durante a ação "Finalizar Compra", o sistema pode, opcionalmente, executar a ação "Aplicar Cupom de Desconto", dependendo de uma condição específica inserida pelo usuário.
- O sistema possui dois perfis: "Cliente Ouro" e "Cliente Prata", ambos derivam de um perfil genérico chamado "Cliente".

Considerando as diretrizes da UML, analise as proposições sobre a modelagem desse cenário:

I. O relacionamento entre "Finalizar Compra" e "Calcular Frete" deve ser modelado com o estereótipo `<<include>>` (inclusão), pois indica um comportamento obrigatório e incorporado pelo caso de uso base.

II. O relacionamento entre "Finalizar Compra" e "Aplicar Cupom de Desconto" deve ser modelado com o estereótipo `<<extend>>` (extensão), pois o caso de uso estendido é acionado apenas se os pontos de extensão (extension points) e suas condições forem satisfeitos.

III. Os perfis "Cliente Ouro" e "Cliente Prata" devem estar ligados ao ator genérico "Cliente" através de um relacionamento de associação bidirecional, indicando troca de dados entre os atores.

IV. Atores em diagramas de casos de uso representam estritamente seres humanos; caso o sistema precise validar o pagamento com um "Gateway do Banco" externo, esse gateway deve ser modelado como uma classe interna e não como um ator.

É correto o que se afirma em:

**Julgamento das afirmativas:**
- **I — Verdadeira.** "Invariavelmente executa" significa comportamento obrigatório e reutilizável: `<<include>>`. A seta tracejada sai do caso base ("Finalizar Compra") e aponta para o incluído ("Calcular Frete").
- **II — Verdadeira.** "Opcionalmente, dependendo de uma condição" significa `<<extend>>`. O comportamento extensor só é inserido quando a condição associada ao ponto de extensão do caso base é satisfeita. A seta tracejada sai do extensor ("Aplicar Cupom") e aponta para o caso base ("Finalizar Compra").
- **III — Falsa.** "Derivam de um perfil genérico" significa **generalização/herança** entre atores (linha sólida com triângulo vazado apontando para "Cliente"), e não associação. Atores não se associam entre si para "trocar dados" no diagrama de casos de uso.
- **IV — Falsa.** Ator é qualquer entidade **externa** que interage com o sistema: pessoa, organização, hardware ou outro sistema/API. O "Gateway do Banco" externo deve ser um **ator** (frequentemente desenhado com o estereótipo `<<system>>`/`<<actor>>`). O próprio exemplo de caixa eletrônico dos slides (p. 61) usa "Banco" como ator.

**Alternativas:**
- **A)** I e II, apenas.
- **B)** II e III, apenas.
- **C)** I, II e IV, apenas.
- **D)** I, III e IV, apenas.
- **E)** I, II, III e IV.

**Gabarito: A** — _(origem: gabarito do próprio material, p. 104)_

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — Justificativa do material (p. 104): I correta, porque `<<include>>` "dita obrigatoriedade e reuso" ("Finalizar Compra" sempre invocará "Calcular Frete"); II correta, porque `<<extend>>` "é acionado de forma condicional/opcional", e a aplicação de cupom depende de pontos de extensão; III incorreta, porque a derivação entre atores usa generalização/herança (seta vazada), e não associação bidirecional; IV incorreta, porque na UML atores não são apenas humanos: sistemas externos, hardwares, serviços e APIs de terceiros "DEVEM ser modelados como atores se eles interagirem com as fronteiras do sistema".
- **B) ❌** — Inclui a III (falsa: é generalização) e omite a I (verdadeira).
- **C) ❌** — Inclui a IV (falsa: sistema externo é ator).
- **D) ❌** — Omite a II (verdadeira) e inclui III e IV (ambas falsas).
- **E) ❌** — III e IV são falsas.

**⚠️ Atenção:**
1. **Terminologia da afirmativa II:** pela nomenclatura estrita da UML, o caso de uso **estendido** é o caso **base** ("Finalizar Compra"). O que é acionado condicionalmente é o caso **extensor** ("Aplicar Cupom de Desconto"). A afirmativa II chama o extensor de "estendido". A imprecisão não muda o gabarito (a ideia de `<<extend>>` = opcional/condicional está certa), mas uma versão alterada pode explorar essa diferença.
2. **Material ambíguo sobre atores:** os slides (p. 60) e a apostila (p. 79) dizem que atores são "bonecos palito, representando as pessoas que realmente implementam os casos de uso". Lida isoladamente, essa frase parece apoiar a IV. A apostila (p. 80) corrige: ator pode ser "pessoa, organização ou sistema externo". Vale o gabarito: **IV é falsa**.
3. `<<include>>`/`<<extend>>` não são explicados nas seções teóricas da apostila nem dos slides. O conteúdo só aparece na própria questão e na justificativa (p. 104).

**Conceito-chave para a prova:** `<<include>>` = **sempre** executa (obrigatório, reuso; seta base → incluído). `<<extend>>` = **às vezes**, sob condição/ponto de extensão (seta extensor → base). Generalização (triângulo vazado) = herança entre atores ou entre casos de uso. Ator = papel **externo** (humano **ou** sistema/hardware/organização).

---

## Q5 — Exercício: caso de uso do caixa eletrônico
**Fonte:** `ENGENHARIA DE SOFTWARE.pdf`, p. 61 (slide "Exemplo: Caixa eletrônico"; o enunciado e o diagrama-resposta estão no mesmo slide). Não aparece na apostila.
**Tipo ENADE:** Exercício discursivo/aberto (modelagem UML)

**Enunciado:**
Nesta modelagem em caso de uso um Cliente de Banco faz o acesso a uma caixa eletrônico e pode fazer as seguintes operações financeiras: checar saldo, depositar, sacar e transferir. Além do Cliente e Banco, um outro ator é o Técnico que pode fazer manutenção ou reparo neste sistema. Elabore o caso de uso.

**Resposta esperada:** _(diagrama apresentado no próprio slide p. 61)_

[Figura: diagrama de casos de uso UML. Uma caixa de limite do sistema com o título **"Sistema de Caixa Eletrônico"** contém 6 casos de uso (elipses): **Checar Saldo**, **Depositar**, **Sacar**, **Transferir**, **Manutenção** e **Reparo**. Fora da caixa há 3 atores (bonecos palito): **Cliente** (à esquerda, em cima), **Técnico** (à esquerda, embaixo) e **Banco** (à direita). Associações (linhas simples, sem setas):
- Cliente — Checar Saldo, Depositar, Sacar, Transferir;
- Técnico — Manutenção, Reparo;
- Banco — Checar Saldo, Depositar, Sacar, Transferir, Manutenção, Reparo (ligado aos 6 casos de uso).
Não há relacionamentos `<<include>>`/`<<extend>>` nem generalizações no diagrama.]

Pontos que a resposta deve mostrar:
- **Limite do sistema** (caixa) com os casos de uso dentro e os atores fora.
- **Ator primário humano** (Cliente) ligado às 4 operações financeiras.
- **Ator de manutenção** (Técnico) ligado a Manutenção e Reparo.
- **Banco como ator**, porque é um sistema externo que participa de todas as operações. Isso confirma que ator não precisa ser humano (ver Q4, afirmativa IV).

_Complemento (não consta no slide):_ numa modelagem mais detalhada seria comum um caso "Autenticar Cliente" ligado por `<<include>>` às operações financeiras (obrigatório), e um caso opcional como "Imprimir Comprovante" ligado por `<<extend>>` a "Sacar". Isso é útil se a prova trouxer uma variação deste exercício combinada com a Q4.

**Conceito-chave para a prova:** elementos do diagrama de casos de uso: ator (externo), caso de uso (elipse), associação (linha ator–caso), limite do sistema (caixa) e pacote. Atores podem ser pessoas **ou sistemas** (aqui, o Banco).

---

## Questão-exemplo do professor (documento Estrutura de Questões ENADE)

### QP — Padrão de projeto GoF Observer
**Fonte:** `Estrutura de Questões sob o padrão do ENADE.pdf`, p. 10 ("4 – Alternativas de respostas · Exemplos de Distratores · Exemplo 2: Engenharia de Software (Padrões de Projeto / Design Patterns)"). Conteúdo de apoio na apostila do Squad 8, p. 62–63 (5.5 Design Patterns e a GoF: o Observer, o Mediator e o Singleton aparecem na lista dos 23 padrões; nenhum deles é explicado em detalhe).
**Tipo ENADE:** Resposta única (4 alternativas, A–D)

**Enunciado:**
_Situação-Problema:_
Uma equipe de desenvolvimento está projetando o módulo de notificações de um sistema de entregas. O requisito define que sempre que o status de um pedido for alterado (ex: "Pedido Enviado", "Saiu para Entrega"), múltiplos módulos independentes (o aplicativo do cliente, o painel do administrador e o sistema de SMS) devem ser notificados automaticamente e atualizar suas respectivas interfaces de forma desacoplada.

_Comando:_
Para atender a esse requisito de arquitetura garantindo o baixo acoplamento, qual padrão de projeto do catálogo GoF (Gang of Four) deve ser aplicado?

**Alternativas:**
- **A)** Observer.
- **B)** Publish-Subscribe.
- **C)** Singleton.
- **D)** Mediator.

**Gabarito: A** — _(origem: gabarito do próprio documento do professor, p. 10, "Gabarito Correto")_

**Por que cada alternativa está certa ou errada:** _(análise dos distratores feita pelo professor, resumida e complementada)_
- **A) ✅** — O Observer "define uma dependência um-para-muitos entre objetos, de modo que quando um objeto muda de estado, todos os seus dependentes são notificados e atualizados automaticamente". No cenário, o Pedido é o *Subject* e o app do cliente, o painel do administrador e o SMS são os *Observers*. O Subject só conhece a interface dos observadores, o que garante baixo acoplamento.
- **B) ❌** — Segundo o professor, é um distrator "extremamente plausível porque resolve o mesmo problema arquitetural", mas o comando pede um padrão **do catálogo GoF**. O Pub-Sub é um padrão de arquitetura de sistemas distribuídos (com um *Event Broker* intermediário) e não é um dos 23 padrões originais do GoF.
- **C) ❌** — Atrai por associação de palavras ("um" status central disparando para muitos). O Singleton é **criacional** e garante uma **única instância** de uma classe. Ele não trata da notificação entre objetos.
- **D) ❌** — Forte distrator **comportamental**. O Mediator também reduz o acoplamento entre vários objetos, mas encapsula e centraliza a interação **bidirecional** entre eles (colegas falam com o mediador, que coordena o fluxo). O cenário descreve notificação **unidirecional**: um emissor para muitos receptores.

**⚠️ Atenção:** no próprio livro do GoF (*Design Patterns*, 1994), o Observer aparece com os nomes alternativos ("Also Known As") **Dependents** e **Publish-Subscribe**. Portanto "Publish-Subscribe" não é totalmente "alheio ao GoF": é um apelido do Observer no catálogo. A literatura moderna distingue os dois: no Pub-Sub, publicadores e assinantes não se conhecem e há um broker ou canal de eventos no meio. A resposta esperada continua sendo **A (Observer)**, que é o **nome canônico** do padrão no catálogo. Se uma versão alterada não trouxer "Observer" entre as alternativas e trouxer "Publish-Subscribe", este passa a ser a melhor resposta.

**Conceito-chave para a prova:** GoF = 23 padrões em 3 famílias. **Criacionais:** Abstract Factory, Builder, Factory Method, Prototype, Singleton. **Estruturais:** Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy. **Comportamentais:** Chain of Responsibility, Command, Interpreter, Iterator, Mediator, Memento, **Observer**, State, Strategy, Template Method, Visitor (apostila p. 63). "Um muda, muitos são avisados automaticamente" = **Observer**. "Centralizar a conversa entre muitos objetos" = **Mediator**. "Trocar algoritmo em tempo de execução" = **Strategy**. "Adaptar interface legada" = **Adapter**.

---

## Observações gerais sobre o material
- **Onde estão as questões:** as 4 questões objetivas e o exercício estão **somente nos slides**. A apostila (106 p.) é só teoria, sem questões. Por isso não houve versões divergentes da mesma questão entre os arquivos.
- **Erro na tabela do PMBOK (slides p. 18):** a linha "Construir uma cultura de empoderamento" aparece **duplicada**. A primeira ocorrência traz a descrição de **"Integrar a Sustentabilidade"** ("Enfatiza as considerações ambientais, econômicas e sociais..."). A apostila (p. 47–48) traz a versão correta dos seis princípios do PMBOK 8ª ed.: visão holística, foco no valor, qualidade incorporada, líder responsável, integrar a sustentabilidade, cultura de empoderamento.
- **Duração da Sprint divergente:** os slides (p. 9) dizem "geralmente de 1 a 4 semanas" e a apostila (p. 44) diz "geralmente de 2 a 4 semanas". Pelo Scrum Guide, a Sprint tem duração fixa de **até um mês**.
- **Grafia:** a apostila (p. 34) escreve fluxo "Interativo" e os slides (p. 22) escrevem "Iterativo". O termo correto é **iterativo** (de iteração/repetição de ciclos).
- **Temas da apostila sem nenhuma questão:** SOLID, arquitetura em camadas, cliente-servidor/microsserviços, ADR/trade-offs, verificação × validação, níveis de teste, caixa-branca/preta/cinza, valor-limite, ciclo de vida do defeito, severidade × prioridade, RUP e técnicas de elicitação (JAD, RAD, etnografia, laddering etc.). Se a prova cobrir Engenharia de Software além das questões acima, esses são os temas de risco.
