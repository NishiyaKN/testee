# Arquitetura de Computadores — Questões INFERIDAS (prováveis questões do banco do squad que não temos)

> ⚠️ **Atenção:** estas questões NÃO constam nos materiais. Foram elaboradas para cobrir os subtópicos do material do
> Squad 5 que não têm questão conhecida, imitando o estilo das questões do squad. Servem para estudo dirigido.
> As questões reais conhecidas estão em `../questoes_por_topico/05_Arquitetura_de_Computadores.md`.

**Base usada:**
- `Revisão Arquitetura de Computadores-1.pdf` (22 p.): sumário na p. 2 e "Mapa rápido dos 16 tópicos" na p. 3. Cada tópico (p. 4–21) traz "Explicação detalhada", "Exemplo simples", tabela "Comparação / resumo visual" e o box **"O que lembrar na prova"**. A p. 3 diz que *"muitas questões de Arquitetura de Computadores testam exatamente essas confusões"*. Referências na p. 22 (MIT 6.004, SNIA Dictionary, Seagate, Kingston, IBM etc.).
- `Apresentação Arquitetura de Computadores.pdf` (41 p.): 22 seções numeradas (p. 2–33). Todas as páginas só com imagem foram renderizadas e lidas: p. 3 (figura do modelo de von Neumann), p. 8 (pirâmide da hierarquia), p. 14 (pipeline de 5 estágios S1–S5 com diagrama de tempo), p. 18 (prato do HDD com trilhas, setores, cabeçote e braço), p. 21 (RAID 0/RAID 1), p. 23 (RAID 2), p. 24 (RAID 3), p. 26 (RAID 4), p. 27 (RAID 5), p. 29 (RAID 1+0). Questões conhecidas Q1–Q3 nas p. 35–40.
- **Estilo identificado do squad (Q1–Q3):** **5 alternativas (A)–(E)**. O enunciado traz um parágrafo de contexto técnico, às vezes com cenário prático (ex.: "vídeo 4K do disco + teclado"), seguido de "Avalie as afirmativas a seguir" com 4 afirmativas I–IV, ou "avalie as asserções a seguir" com I PORQUE II. O comando é "**É correto o que se afirma em:**" ou "**A respeito dessas asserções, assinale a opção correta:**". Termos em inglês aparecem em itálico (*pipelining*, *throughput*, *forwarding*, *polling*). Cada questão tem um box "GABARITO COMENTADO — ALTERNATIVA CORRETA: (X)". Os tipos usados são **afirmativas múltiplas** (2) e **asserção-razão** (1), e as afirmativas falsas exploram exatamente as "confusões" que a apostila aponta: forwarding × controle, latência × vazão, IR × flags. Por isso a maioria das inferidas segue esses dois tipos, com algumas de resposta única (cálculo), associação e afirmativa negativa para variar.

## Mapa de cobertura
| # | Subtópico (material) | Páginas | Questão conhecida | Questão inferida | Prioridade |
|---|---|---|---|---|---|
| 1 | Arquitetura de von Neumann e arquitetura dos computadores (arquitetura × organização, gargalo, Harvard, Harvard modificada) | Revisão p. 4–5; slides p. 2–3 (figura p. 3) | — | I1, I2 | Alta |
| 2 | Tecnologias de barramento (dados/endereços/controle, PCIe/USB/SATA, chipset, gargalo, Plug and Play) | Revisão p. 6; slides p. 4–6 | — | I3, I4 | Alta |
| 3 | Tecnologias de memória e hierarquia de memória (SRAM/DRAM/flash, cache, localidade, hit/miss, memória virtual) | Revisão p. 7–8; slides p. 7–8 | — | I5, I6 | Alta |
| 4 | Principais registradores do processador | Revisão p. 9; slides p. 9 | **Q2** | — (variação provável: trocar a função de um registrador, ex. "PC guarda a instrução", "MAR guarda o dado", "SP aponta a próxima instrução") | — |
| 5 | Interfaces entre processador, memória e E/S | Revisão p. 10; slides p. 10–11 | **Q3** (polling, interrupção e DMA, slide 11) | I7 (só a parte que a Q3 não cobra: E/S mapeada × isolada, controladores × drivers, slide 10) | Baixa |
| 6 | Ciclo de máquina e execução de instruções | Revisão p. 11; slides p. 12 | Q2 só **parcialmente** (fetch PC→MAR→MDR e desvio no PC) | I8 (ciclo de instrução × ciclo de clock, etapas, opcode) | Alta |
| 7 | Pipeline de instruções | Revisão p. 12; slides p. 13–15 (figura p. 14) | **Q1** | — (variação provável: cálculo de ciclos k + n − 1, ex. 5 estágios e 100 instruções = 104 ciclos contra 500, *speedup* ≈ 4,8; ou associação hazard ↔ técnica) | — |
| 8 | Arquiteturas CISC e RISC | Revisão p. 13; slides p. 16 | Q1 só **parcialmente** (afirmativas I e III: load/store e µops) | I9 (mitos: "1 instrução = 1 ciclo", "RISC sempre mais rápido", microcódigo) | Média |
| 9 | Discos magnéticos: conceitos básicos | Revisão p. 14; slides p. 17–18 (figura p. 18) | — | I10 | Alta |
| 10 | Discos magnéticos: parâmetros de desempenho | Revisão p. 15; slides p. 19 | — | I11 (cálculo), I12 | Alta |
| 11 | RAID níveis 0, 1, 2 e 3 | Revisão p. 16; slides p. 20–24 (figuras p. 21, 23, 24) | — | I13, I14 | Alta |
| 12 | RAID níveis 4, 5 e 10 | Revisão p. 17; slides p. 25–29 (figuras p. 26, 27, 29) | — | I15 (capacidade), I16 (figura RAID 10), I17 (paridade) | Alta |
| 13 | SSD — Solid State Drive | Revisão p. 18; slides p. 30 | — | I18, I19 | Alta |
| 14 | DAS — Direct Attached Storage | Revisão p. 19; slides p. 31 | — | I20 (+ I23) | Alta |
| 15 | NAS — Network Attached Storage | Revisão p. 20; slides p. 32 | — | I21 (+ I23) | Alta |
| 16 | SAN — Storage Area Network | Revisão p. 21; slides p. 33 | — | I22 (+ I23, associação DAS × NAS × SAN) | Alta |

**Resumo:** 16 subtópicos (os 16 tópicos da apostila). 3 já estão cobertos por questões conhecidas: tópico 4 (Q2), tópico 5 (Q3) e tópico 7 (Q1). Os tópicos 6 e 8 aparecem só de passagem em afirmativas de Q2 e Q1, então foram tratados como sem questão própria. Ficam **13 subtópicos sem questão** (1, 2, 3, 6, 8, 9–16). Foram inferidas **23 questões**: 22 para esses 13 subtópicos e 1 (I7, prioridade baixa) para a parte do tópico 5 que a Q3 não cobra. Gabaritos: A = 4 (I2, I10, I16, I20) · B = 5 (I1, I8, I12, I15, I21) · C = 5 (I5, I7, I11, I19, I23) · D = 5 (I3, I9, I14, I17, I22) · E = 4 (I4, I6, I13, I18).

## Índice
1. [I1 — Arquitetura × organização e gargalo de von Neumann](#i1--arquitetura--organização-e-gargalo-de-von-neumann)
2. [I2 — Figura do modelo de von Neumann (asserção-razão)](#i2--figura-do-modelo-de-von-neumann-asserção-razão)
3. [I3 — Barramentos de dados, endereços e controle; PCIe, SATA e USB](#i3--barramentos-de-dados-endereços-e-controle-pcie-sata-e-usb)
4. [I4 — Plug and Play e drivers](#i4--plug-and-play-e-drivers)
5. [I5 — Hierarquia e tecnologias de memória](#i5--hierarquia-e-tecnologias-de-memória)
6. [I6 — Cache: localidade, hit/miss e tempo médio de acesso](#i6--cache-localidade-hitmiss-e-tempo-médio-de-acesso)
7. [I7 — E/S mapeada em memória × E/S isolada; controlador × driver](#i7--es-mapeada-em-memória--es-isolada-controlador--driver)
8. [I8 — Ciclo de instrução × ciclo de clock](#i8--ciclo-de-instrução--ciclo-de-clock)
9. [I9 — CISC × RISC: o que NÃO é verdade](#i9--cisc--risc-o-que-não-é-verdade)
10. [I10 — HDD: trilha, setor, cilindro, LBA e seek (associação)](#i10--hdd-trilha-setor-cilindro-lba-e-seek-associação)
11. [I11 — HDD: cálculo do tempo de acesso aleatório e IOPS](#i11--hdd-cálculo-do-tempo-de-acesso-aleatório-e-iops)
12. [I12 — HDD: throughput × IOPS, sequencial × aleatório](#i12--hdd-throughput--iops-sequencial--aleatório)
13. [I13 — RAID 0, 1, 2 e 3](#i13--raid-0-1-2-e-3)
14. [I14 — RAID 1 não substitui backup](#i14--raid-1-não-substitui-backup)
15. [I15 — Escolha do nível RAID e capacidade útil](#i15--escolha-do-nível-raid-e-capacidade-útil)
16. [I16 — RAID 10: falhas toleradas (figura)](#i16--raid-10-falhas-toleradas-figura)
17. [I17 — RAID 5: reconstrução por paridade](#i17--raid-5-reconstrução-por-paridade)
18. [I18 — SSD: páginas, blocos, TRIM e wear leveling](#i18--ssd-páginas-blocos-trim-e-wear-leveling)
19. [I19 — SSD: M.2 × NVMe × SATA](#i19--ssd-m2--nvme--sata)
20. [I20 — DAS externo compartilhado por servidor](#i20--das-externo-compartilhado-por-servidor)
21. [I21 — NAS em pequeno escritório](#i21--nas-em-pequeno-escritório)
22. [I22 — SAN com iSCSI](#i22--san-com-iscsi)
23. [I23 — DAS × NAS × SAN (associação)](#i23--das--nas--san-associação)

---

## I1 — Arquitetura × organização e gargalo de von Neumann
**Subtópico coberto:** Tópico 1, Arquitetura de von Neumann e arquitetura dos computadores (Revisão p. 4–5; slides p. 2–3)
**Por que é provável:** é o primeiro tópico da apostila e dos slides, e o box "O que lembrar na prova" (p. 5) traz quatro frases que viram afirmativas V/F quase diretas: arquitetura = ISA; organização = implementação; gargalo = caminho compartilhado; "não confunda CPU com computador inteiro".
**Prioridade:** Alta
**Tipo ENADE:** Afirmativas múltiplas

**Enunciado:**
Uma empresa de software vai renovar suas estações de trabalho e compara dois processadores compatíveis com o conjunto de instruções x86-64. O processador X opera a 3,0 GHz e tem 8 MB de cache. O processador Y opera a 4,2 GHz, tem 32 MB de cache e trabalha com memória DDR5. Os mesmos executáveis rodam nos dois modelos sem recompilação, mas com tempos de execução diferentes. Considerando os conceitos de arquitetura e organização de computadores e o modelo de von Neumann, avalie as afirmativas a seguir:

I. Como os dois processadores executam os mesmos programas sem recompilação, eles compartilham a mesma arquitetura, isto é, o conjunto de instruções, os registradores visíveis ao programador e as formas de endereçamento, ainda que difiram na organização.

II. A frequência de *clock*, o tamanho da cache e a tecnologia da memória principal são aspectos de organização, pois descrevem como as características visíveis ao programador são implementadas física e eletronicamente.

III. O gargalo de von Neumann decorre principalmente da lentidão da ULA ao executar operações aritméticas e lógicas, razão pela qual ele é eliminado quando se adota uma ULA de maior frequência.

IV. No modelo de von Neumann, a CPU, formada por unidade de controle, ULA e registradores, corresponde ao computador inteiro, e a memória e os dispositivos de E/S são elementos externos ao sistema computacional.

É correto o que se afirma em:

**Alternativas:**
- **A)** I e III, apenas.
- **B)** I e II, apenas.
- **C)** II e IV, apenas.
- **D)** I, II e III, apenas.
- **E)** I, II, III e IV.

**Gabarito: B**

**Julgamento das afirmativas:**
- **I — Verdadeira.** Arquitetura é o que a ISA expõe a quem programa (instruções, registradores, endereçamento). Se o mesmo binário roda nos dois, a arquitetura é a mesma.
- **II — Verdadeira.** Clock, tamanho da cache e tipo de DRAM não mudam o que o programador vê, só como (e com que velocidade) aquilo é implementado. Isso é organização.
- **III — Falsa.** O gargalo de von Neumann está no **caminho compartilhado entre CPU e memória** para instruções e dados. Uma ULA mais rápida não resolve o problema e até aumenta a distância entre a velocidade da CPU e a do caminho até a memória.
- **IV — Falsa.** A apostila alerta: "Não confunda CPU com computador inteiro: memória e E/S também fazem parte do sistema".

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Inclui a III (gargalo atribuído à ULA) e deixa de fora a II, que é verdadeira.
- **B) ✅** — I e II são exatamente as verdadeiras.
- **C) ❌** — A IV é falsa (CPU ≠ computador inteiro), e a I, verdadeira, ficou de fora.
- **D) ❌** — Inclui a III, que é falsa.
- **E) ❌** — III e IV são falsas.

**Base no material:** Revisão p. 4 ("A arquitetura está ligada às características que são visíveis para quem cria programas… A organização explica como essas características são implementadas fisicamente e eletronicamente"; "gargalo de von Neumann: a CPU pode ser muito rápida, mas o caminho entre processador e memória pode limitar…") e p. 5 (box "O que lembrar na prova"); slides p. 2.
**Conceito-chave para a prova:** arquitetura = **o quê** (ISA visível); organização = **como** (implementação). O gargalo de von Neumann vem do **caminho compartilhado** CPU↔memória, e não da ULA. CPU + memória + E/S formam o sistema.

---

## I2 — Figura do modelo de von Neumann (asserção-razão)
**Subtópico coberto:** Tópico 1, von Neumann × Harvard (Revisão p. 4; slides p. 3, figura)
**Por que é provável:** o slide 3 é uma figura dedicada só ao modelo de von Neumann (memória única "Instruções e Dados" e três barramentos), e o squad usou asserção-razão com cenário prático na Q3. O gargalo de von Neumann aparece na explicação e no "O que lembrar na prova".
**Prioridade:** Média
**Tipo ENADE:** Asserção-razão

**Enunciado:**
A figura a seguir representa o modelo clássico de von Neumann.

[Figura (slides p. 3): à esquerda, o bloco **Memória**, contendo "Instruções e Dados". À direita, o bloco **Processador**, com "Unidade de Controle", "Registradores" e "ULA". Entre eles há três barramentos: **Barramento de Endereço** (seta do processador para a memória), **Barramento de Instruções e dados** (seta bidirecional) e **Barramento de Controle** (seta do processador para a memória).]

Considere um programa que, a cada iteração de um laço, busca uma instrução na memória e, em seguida, lê um operando que também está armazenado na memória. A respeito desse cenário, avalie as asserções a seguir:

I. No modelo representado, a busca da próxima instrução e a leitura do operando disputam o mesmo caminho de comunicação com a memória, de modo que, por mais rápida que seja a CPU, a transferência entre processador e memória pode limitar o desempenho.

PORQUE

II. No modelo de von Neumann, instruções e dados ficam armazenados na mesma memória e, no modelo clássico, compartilham o caminho de comunicação com o processador, limitação conhecida como gargalo de von Neumann.

A respeito dessas asserções, assinale a opção correta:

**Alternativas:**
- **A)** As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
- **B)** As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
- **C)** A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
- **D)** A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
- **E)** As asserções I e II são proposições falsas.

**Gabarito: A**

**Julgamento:**
- **Asserção I — Verdadeira.** Na figura há um único "Barramento de Instruções e dados". A instrução e o operando passam pelo mesmo caminho, um de cada vez.
- **Asserção II — Verdadeira.** É a definição do modelo e do gargalo de von Neumann dada na apostila.
- **Relação — A II justifica a I.** A disputa descrita na I acontece *porque* instruções e dados compartilham memória e caminho.

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — As duas são verdadeiras e a II é a causa da situação descrita na I.
- **B) ❌** — Armadilha "verdadeiras, mas sem relação". Aqui a II é exatamente o motivo da I.
- **C) ❌** — A II não é falsa: descreve corretamente o princípio do programa armazenado no modelo de von Neumann.
- **D) ❌** — A I não é falsa. Ela só seria falsa numa arquitetura **Harvard**, em que instruções e dados usam memórias e caminhos separados.
- **E) ❌** — As duas asserções estão corretas.

**Base no material:** Revisão p. 4 ("Na arquitetura de von Neumann, instruções e dados utilizam a mesma memória e, no modelo clássico, compartilham o caminho de comunicação. Isso cria uma limitação conhecida como gargalo de von Neumann"; Harvard: "a memória e os caminhos para instruções e dados são separados"); slides p. 3 (figura).
**Conceito-chave para a prova:** von Neumann = **mesma memória e mesmo caminho** → gargalo. Harvard = memórias e caminhos **separados**. Harvard modificada = memória principal unificada com **caches separadas** de instruções e dados (comum nos processadores modernos). Numa versão alterada, uma II do tipo "o gargalo se deve à lentidão da ULA" seria falsa (resposta C).

---

## I3 — Barramentos de dados, endereços e controle; PCIe, SATA e USB
**Subtópico coberto:** Tópico 2, Tecnologias de barramento (Revisão p. 6; slides p. 4–6)
**Por que é provável:** o squad dedica três slides (p. 4, 5 e 6) ao tema, e o "O que lembrar na prova" insiste em "PCIe não é o mesmo que SATA" e na origem dos gargalos (banda, latência, disputa).
**Prioridade:** Alta
**Tipo ENADE:** Afirmativas múltiplas

**Enunciado:**
Um técnico monta uma estação de trabalho para edição de vídeo com uma placa de vídeo em um *slot* PCI Express x16, um SSD de 2,5" ligado por SATA, e teclado e mouse conectados por USB. Ao explicar o funcionamento do equipamento a um estagiário, ele descreve como a CPU lê um dado da memória principal e como os dispositivos se comunicam com a placa-mãe. Considerando as tecnologias de barramento e interconexão, avalie as afirmativas a seguir:

I. Em uma leitura da memória, o barramento de endereços identifica onde a operação deve ocorrer, os sinais de controle indicam o tipo e o momento da operação (leitura) e o barramento de dados transporta o valor lido.

II. O PCI Express usado pela placa de vídeo é um barramento paralelo compartilhado, no qual todos os dispositivos da placa-mãe disputam as mesmas linhas de dados, característica que o torna adequado a componentes de alto desempenho.

III. SATA e PCI Express são denominações diferentes para a mesma interface. Por isso, um SSD ligado por SATA atinge necessariamente o mesmo desempenho de um SSD ligado por PCIe.

IV. Um gargalo pode surgir em qualquer enlace do caminho percorrido pela informação, por pouca largura de banda, muita latência ou grande disputa. Por isso, não basta analisar um único componente.

É correto o que se afirma em:

**Alternativas:**
- **A)** I e II, apenas.
- **B)** II e III, apenas.
- **C)** III e IV, apenas.
- **D)** I e IV, apenas.
- **E)** I, II e IV, apenas.

**Gabarito: D**

**Julgamento das afirmativas:**
- **I — Verdadeira.** São os três papéis clássicos: **dados** = valores; **endereços** = onde; **controle** = tipo e momento.
- **II — Falsa.** O PCIe usa **enlaces seriais ponto a ponto**, e não um barramento paralelo compartilhado. É justamente essa característica que o torna adequado ao alto desempenho.
- **III — Falsa.** "PCIe não é o mesmo que SATA": o PCIe é uma interconexão de alta velocidade usada por vários componentes, e o SATA é uma interface de armazenamento, com finalidade e características diferentes.
- **IV — Verdadeira.** É praticamente o texto da apostila: é preciso observar o caminho completo.

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Inclui a II, que transforma o PCIe em barramento paralelo compartilhado.
- **B) ❌** — As duas afirmativas listadas são falsas.
- **C) ❌** — Inclui a III (SATA = PCIe) e deixa de fora a I.
- **D) ✅** — I e IV são exatamente as verdadeiras.
- **E) ❌** — Inclui a II, que é falsa.

**Base no material:** Revisão p. 6 ("O barramento de dados transporta os dados… O de endereços identifica onde… Os sinais de controle indicam o tipo e o momento"; "O PCI Express… utiliza enlaces seriais ponto a ponto"; "SATA é uma interface de armazenamento"; "não basta olhar para um único componente: é preciso observar o caminho completo"); slides p. 4, 5 e 6 ("Gargalo: pode surgir por baixa largura de banda, alta latência ou disputa por um mesmo enlace").
**Conceito-chave para a prova:** dados = **o quê**, endereços = **onde**, controle = **tipo/quando**. **PCIe = serial ponto a ponto**, alto desempenho. **SATA = armazenamento**. **USB = periféricos**. Um gargalo pode estar em **banda, latência ou disputa** em qualquer ponto do caminho.

---

## I4 — Plug and Play e drivers
**Subtópico coberto:** Tópico 2, Tecnologias de barramento: Plug and Play e chipset (Revisão p. 6; slides p. 6)
**Por que é provável:** o slide 6 tem um destaque "**Importante:** Plug and Play facilita a configuração, mas não garante compatibilidade entre todos os componentes", repetido no "O que lembrar na prova". É uma "confusão" típica para asserção-razão.
**Prioridade:** Média
**Tipo ENADE:** Asserção-razão

**Enunciado:**
Um usuário conecta à porta USB de seu computador uma placa de captura de vídeo antiga. O sistema operacional detecta o dispositivo e exibe o nome do fabricante no gerenciador de dispositivos, mas não existe *driver* para a versão atual do sistema, e a placa não funciona. Em outro computador, com uma versão anterior do sistema operacional e o *driver* correspondente instalado, a mesma placa funciona normalmente. Considerando o mecanismo Plug and Play, avalie as asserções a seguir:

I. Como o computador e a placa suportam Plug and Play, a falha só pode ser explicada por defeito físico da placa, pois o Plug and Play garante a compatibilidade entre hardware, sistema operacional e *drivers*.

PORQUE

II. No Plug and Play, a identificação, a configuração e a alocação de recursos do dispositivo são realizadas inteiramente pelo hardware, sem a participação do sistema operacional nem de *drivers*.

A respeito dessas asserções, assinale a opção correta:

**Alternativas:**
- **A)** As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
- **B)** As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
- **C)** A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
- **D)** A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
- **E)** As asserções I e II são proposições falsas.

**Gabarito: E**

**Julgamento:**
- **Asserção I — Falsa.** O próprio cenário mostra que a placa funciona em outro computador com o *driver* adequado, então não há defeito físico. O Plug and Play "facilita a instalação, mas não elimina incompatibilidades de hardware, software ou drivers".
- **Asserção II — Falsa.** A apostila diz que o Plug and Play "automatiza **parte** da identificação, configuração e alocação de recursos" e que "o sistema operacional e os drivers participam desse processo". O slide 6 diz que ele "ajuda o sistema operacional e os drivers a identificar e configurar dispositivos".

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — As duas asserções contrariam o material.
- **B) ❌** — Pressupõe as duas verdadeiras.
- **C) ❌** — A I é falsa: Plug and Play não garante compatibilidade.
- **D) ❌** — A II também é falsa: SO e *drivers* participam do processo.
- **E) ✅** — As duas são falsas.

**Base no material:** Revisão p. 6 (parágrafo sobre Plug and Play e "O que lembrar na prova": "Plug and Play facilita configuração; não significa compatibilidade garantida"); slides p. 6 (quadro "Plug and Play" e box "Importante"). Na mesma página aparece o chipset: "Historicamente, funções eram divididas entre northbridge e southbridge, mas os computadores modernos passaram a integrar diversas dessas funções na própria CPU".
**Conceito-chave para a prova:** Plug and Play = **automatiza parte** da identificação/configuração **com SO e drivers**, e **não garante compatibilidade**. Se uma versão alterada trouxer a II correta ("…com participação do SO e dos drivers"), a resposta passa a ser **D**.

---

## I5 — Hierarquia e tecnologias de memória
**Subtópico coberto:** Tópico 3, Tecnologias de memória e hierarquia de memória (Revisão p. 7–8; slides p. 7–8)
**Por que é provável:** o tópico tem tabela-resumo, a pirâmide do slide 8 e quatro frases no "O que lembrar na prova" (SRAM em cache, DRAM na principal, localidade, memória virtual ≠ RAM), material típico de afirmativas V/F.
**Prioridade:** Alta
**Tipo ENADE:** Afirmativas múltiplas

**Enunciado:**
Uma equipe projeta um equipamento embarcado de monitoramento industrial e precisa definir as tecnologias de memória de cada nível: a cache do processador, a memória principal e a memória que guardará o *firmware*, que deve ser preservado mesmo com o equipamento desligado. Considerando a hierarquia de memória e as tecnologias disponíveis, avalie as afirmativas a seguir:

I. A SRAM, volátil e sem necessidade de *refresh* periódico, é adequada à cache. A DRAM, também volátil, mas que precisa de *refresh* para manter os dados, é a escolha usual para a memória principal.

II. Na hierarquia de memória, quanto mais próximo da CPU está o nível, maior tende a ser sua capacidade e menor o seu custo por bit, o que explica por que os registradores são o nível de maior capacidade do sistema.

III. A memória flash preserva os dados sem energia e pode ser reprogramada. Por isso é adequada ao armazenamento do *firmware*, e também é utilizada em SSDs.

IV. Caso a memória principal seja insuficiente, a memória virtual poderá manter páginas no armazenamento, o que torna o acesso a esse armazenamento tão rápido quanto o acesso à RAM.

É correto o que se afirma em:

**Alternativas:**
- **A)** I e II, apenas.
- **B)** II e IV, apenas.
- **C)** I e III, apenas.
- **D)** I, III e IV, apenas.
- **E)** I, II, III e IV.

**Gabarito: C**

**Julgamento das afirmativas:**
- **I — Verdadeira.** É o primeiro item do "O que lembrar na prova": "SRAM é comum em cache; DRAM é comum na memória principal". O *refresh* é a diferença técnica entre as duas.
- **II — Falsa.** É o contrário: quanto mais perto da CPU, **menor, mais rápida e mais cara por bit**. Registradores são o nível mais rápido e o de **menor** capacidade (topo da pirâmide do slide 8).
- **III — Verdadeira.** "ROM e flash conseguem preservar dados sem energia. A flash pode ser reprogramada e é utilizada, por exemplo, em firmware e em SSDs."
- **IV — Falsa.** "Memória virtual não torna armazenamento equivalente à RAM": ela amplia a flexibilidade, mas o disco continua muito mais lento.

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Inclui a II, que inverte a relação de tamanho e custo.
- **B) ❌** — As duas afirmativas listadas são falsas.
- **C) ✅** — I e III são exatamente as verdadeiras.
- **D) ❌** — Inclui a IV, pegadinha clássica da memória virtual.
- **E) ❌** — II e IV são falsas.

**Base no material:** Revisão p. 7 (explicação, tabela-resumo e "O que lembrar") e p. 8 ("Memória virtual não torna armazenamento equivalente à RAM"); slides p. 7 e p. 8 (pirâmide: registradores → cache → memória primária → memória secundária, com "mais velocidade" para cima e "mais armazenamento" para baixo).
**Conceito-chave para a prova:** **perto da CPU = pequeno, rápido, caro por bit**. **SRAM** (sem *refresh*) → cache. **DRAM** (com *refresh*) → principal. **ROM/flash** → não voláteis. Memória virtual **≠** disco com velocidade de RAM.

---

## I6 — Cache: localidade, hit/miss e tempo médio de acesso
**Subtópico coberto:** Tópico 3, cache, localidade temporal/espacial e hit/miss (Revisão p. 7)
**Por que é provável:** dois dos quatro itens do "O que lembrar na prova" do tópico 3 são sobre a cache ("explora localidade temporal e espacial"; "hit… miss exige buscar em nível seguinte"). O squad gosta de situação-problema técnica (Q1, Q2), e um laço sobre vetor é o exemplo padrão.
**Prioridade:** Média
**Tipo ENADE:** Afirmativas múltiplas (com cálculo)

**Enunciado:**
Um programador analisa o desempenho do trecho de código a seguir, em que `v` é um vetor de inteiros armazenado de forma contígua na memória.

```c
int soma = 0;
for (int i = 0; i < 1000; i++) {
    soma = soma + v[i];
}
```

Medições no processador indicaram: tempo de acerto na cache (*hit time*) = 2 ns; penalidade de falha (*miss penalty*, tempo adicional para buscar o dado no nível seguinte) = 60 ns; taxa de acerto = 95%. Considere: **tempo médio de acesso = tempo de acerto + taxa de falha × penalidade de falha**.

Com base nessa situação, avalie as afirmativas a seguir:

I. O acesso sequencial a `v[0]`, `v[1]`, `v[2]`, … explora a localidade espacial, pois, quando um bloco é trazido para a cache, as posições vizinhas também passam a estar disponíveis no nível mais rápido.

II. A reutilização da variável `soma`, do contador `i` e das próprias instruções do laço, a cada iteração, explora a localidade temporal.

III. Com os dados informados, o tempo médio de acesso é de 5 ns.

IV. Como a taxa de acerto já é alta, uma queda de 95% para 90% praticamente não altera o tempo médio de acesso, que permanece próximo de 5 ns.

É correto o que se afirma em:

**Alternativas:**
- **A)** I e II, apenas.
- **B)** III e IV, apenas.
- **C)** I, II e IV, apenas.
- **D)** II, III e IV, apenas.
- **E)** I, II e III, apenas.

**Gabarito: E**

**Julgamento das afirmativas:**
- **I — Verdadeira.** Localidade **espacial**: posições próximas tendem a ser acessadas juntas. Um vetor contíguo percorrido em sequência é o exemplo típico.
- **II — Verdadeira.** Localidade **temporal**: o que foi usado recentemente tende a ser usado de novo, como `soma`, `i` e as instruções do laço, reutilizadas mil vezes.
- **III — Verdadeira.** 2 + (1 − 0,95) × 60 = 2 + 0,05 × 60 = 2 + 3 = **5 ns** (conferido em python). Sem cache, cada acesso levaria cerca de 60 ns, 12 vezes mais.
- **IV — Falsa.** Com 90%: 2 + 0,10 × 60 = **8 ns**, aumento de 60%. Pequenas quedas na taxa de acerto pesam muito, porque cada *miss* custa 30 vezes o tempo de um *hit*.

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Deixa de fora a III, que está correta.
- **B) ❌** — Inclui a IV (falsa) e deixa de fora I e II.
- **C) ❌** — Inclui a IV: o tempo sobe para 8 ns.
- **D) ❌** — Inclui a IV e deixa de fora a I.
- **E) ✅** — I, II e III são as verdadeiras.

**Base no material:** Revisão p. 7 ("Ela aproveita a localidade temporal, quando um dado usado recentemente tende a ser usado novamente, e a localidade espacial, quando posições próximas tendem a ser acessadas juntas. Quando o dado está na cache ocorre um cache hit… Quando não está, ocorre um cache miss e o sistema precisa buscar a informação em outro nível"). A fórmula do tempo médio é conhecimento padrão (referência MIT 6.004 "Caches and the Memory Hierarchy", p. 22) e foi dada no enunciado para evitar ambiguidade.
**Conceito-chave para a prova:** vetor percorrido em sequência = **espacial**; variável e laço reutilizados = **temporal**. Tempo médio = *hit* + (1 − taxa de acerto) × penalidade. ⚠️ Se a questão usar a outra fórmula comum, h × t_cache + (1 − h) × t_mem, o resultado muda (0,95 × 2 + 0,05 × 60 = 4,9 ns). Confira qual fórmula o enunciado define.

---

## I7 — E/S mapeada em memória × E/S isolada; controlador × driver
**Subtópico coberto:** Tópico 5, Interfaces entre processador, memória e E/S, **somente a parte não cobrada pela Q3** (Revisão p. 10; slides p. 10)
**Por que é provável:** os slides separam o tópico em duas seções, "7. Interfaces entre CPU, memória e E/S" (p. 10: controladores, drivers, E/S mapeada, E/S isolada) e "8. Polling, interrupção e DMA" (p. 11). A Q3 cobre só a seção 8. O "O que lembrar" ainda traz "Driver é software usado para controlar o dispositivo".
**Prioridade:** Baixa (o tópico 5 já tem a Q3)
**Tipo ENADE:** Afirmativas múltiplas

**Enunciado:**
Uma empresa desenvolve uma placa de aquisição de dados e o respectivo *driver* para duas plataformas. Na plataforma baseada em Arm, os registradores de controle e de status da placa ocupam a faixa de endereços `0x4000_0000` a `0x4000_00FF` do espaço de endereçamento do processador. Na plataforma x86, a mesma placa é acessada por portas de E/S, com as instruções `IN` e `OUT`. Considerando as interfaces entre processador, memória e dispositivos de E/S, avalie as afirmativas a seguir:

I. Na plataforma Arm, a placa utiliza E/S mapeada em memória: seus registradores ocupam endereços do mesmo espaço de endereços da memória e podem ser acessados por instruções normais de leitura e escrita.

II. Na plataforma x86, o acesso por portas com as instruções `IN` e `OUT` caracteriza E/S isolada, em que existe um espaço de E/S separado e instruções específicas para acessar os dispositivos.

III. O *driver* é o circuito da placa responsável por adaptar sinais elétricos, protocolos e velocidades entre o periférico e o barramento, o que dispensa software específico no sistema operacional.

IV. Na E/S mapeada em memória, a CPU só consegue ler os registradores de status da placa por meio de um controlador de DMA, já que instruções comuns de leitura e escrita acessam apenas a RAM.

É correto o que se afirma em:

**Alternativas:**
- **A)** I, apenas.
- **B)** III e IV, apenas.
- **C)** I e II, apenas.
- **D)** I, II e III, apenas.
- **E)** II, III e IV, apenas.

**Gabarito: C**

**Julgamento das afirmativas:**
- **I — Verdadeira.** É a definição de E/S mapeada em memória: "os registradores do dispositivo ocupam endereços dentro do mesmo espaço de endereços da memória. Dessa forma, instruções normais de leitura e escrita podem acessar esses registradores".
- **II — Verdadeira.** "Na E/S isolada, existe um espaço de E/S separado e, dependendo da arquitetura, instruções específicas para acessar os dispositivos." `IN`/`OUT` do x86 são o exemplo clássico.
- **III — Falsa.** Confunde **controlador** (hardware que "faz a ponte… adaptando sinais, protocolos e velocidades") com **driver** ("software usado pelo sistema operacional para controlar dispositivos").
- **IV — Falsa.** Na E/S mapeada, o acesso aos registradores do dispositivo é feito justamente com instruções comuns de leitura e escrita. O DMA serve para transferir blocos de dados entre dispositivo e memória, e não é o único meio de ler registradores.

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Omite a II, que também está correta.
- **B) ❌** — As duas afirmativas listadas são falsas.
- **C) ✅** — I e II são as verdadeiras.
- **D) ❌** — Inclui a III (driver tratado como hardware).
- **E) ❌** — Inclui III e IV, falsas, e omite a I.

**Base no material:** Revisão p. 10 (dois primeiros parágrafos e "O que lembrar": "Driver é software usado para controlar o dispositivo"); slides p. 10 (quadros "Controladores", "Drivers", "E/S mapeada em memória", "E/S isolada").
**Conceito-chave para a prova:** **mapeada** = mesmo espaço de endereços, instruções normais de load/store. **Isolada** = espaço separado, instruções específicas (ex.: `IN`/`OUT`). **Controlador = hardware** e **driver = software**.

---

## I8 — Ciclo de instrução × ciclo de clock
**Subtópico coberto:** Tópico 6, Ciclo de máquina e execução de instruções (Revisão p. 11; slides p. 12)
**Por que é provável:** o slide 12 tem um box "**Atenção: ciclo de instrução ≠ ciclo de clock**", repetido na apostila ("É essencial separar…") e no "O que lembrar na prova". A Q2 só cobre a etapa de busca, sem as etapas seguintes nem a relação com o clock.
**Prioridade:** Alta
**Tipo ENADE:** Afirmativas múltiplas (com cálculo)

**Enunciado:**
Um processador didático opera com *clock* de 2 GHz. Nele, a instrução `ADD R1, R2, [X]`, que soma o conteúdo de R2 ao valor armazenado no endereço de memória X e grava o resultado em R1, consome 6 ciclos de *clock*. Já a instrução `ADD R1, R2, R3`, com todos os operandos em registradores, consome 4 ciclos de *clock*. Considerando o ciclo de máquina e a execução de instruções, avalie as afirmativas a seguir:

I. Na execução de `ADD R1, R2, [X]`, a CPU busca a instrução no endereço indicado pelo PC, decodifica o *opcode* e os demais campos, obtém os operandos (inclusive o valor lido do endereço X), executa a soma na ULA e registra o resultado em R1.

II. Como cada ciclo de instrução corresponde a exatamente um ciclo de *clock*, as duas instruções são concluídas em 0,5 ns cada.

III. A instrução `ADD R1, R2, [X]` leva 3 ns para ser concluída, e a instrução `ADD R1, R2, R3` leva 2 ns.

IV. Caso ocorra uma interrupção durante a execução do programa, o fluxo normal pode ser desviado para uma rotina de atendimento, assim como uma instrução de desvio altera o valor do PC.

É correto o que se afirma em:

**Alternativas:**
- **A)** I e II, apenas.
- **B)** I, III e IV, apenas.
- **C)** II e III, apenas.
- **D)** II, III e IV, apenas.
- **E)** I, II, III e IV.

**Gabarito: B**

**Julgamento das afirmativas:**
- **I — Verdadeira.** São as cinco etapas do slide 12, na ordem: buscar (PC) → decodificar (opcode e campos) → obter operandos (registradores ou memória) → executar → registrar resultado.
- **II — Falsa.** "Ciclo de instrução ≠ ciclo de clock. Uma instrução pode ocupar vários ciclos de clock." Aqui uma instrução leva 6 ciclos e a outra, 4.
- **III — Verdadeira.** Período do clock = 1 / 2 GHz = 0,5 ns. 6 × 0,5 = **3 ns** e 4 × 0,5 = **2 ns** (conferido em python). A versão com operando em memória demora mais porque precisa de um acesso extra à memória para obter o operando.
- **IV — Verdadeira.** "Interrupções e desvios alteram o fluxo normal." Após a execução, "o PC é atualizado para continuar o programa ou seguir para o destino de um desvio".

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Inclui a II, que iguala ciclo de instrução a ciclo de clock.
- **B) ✅** — I, III e IV são as verdadeiras.
- **C) ❌** — Inclui a II e omite I e IV.
- **D) ❌** — Inclui a II e omite a I.
- **E) ❌** — A II é falsa.

**Base no material:** Revisão p. 11 (explicação, tabela das cinco etapas e "O que lembrar na prova": "Opcode identifica a operação. PC participa da busca da próxima instrução. Uma instrução pode usar vários ciclos de clock. Interrupções e desvios alteram o fluxo normal"); slides p. 12 (etapas 1–5 e box "Atenção").
**Conceito-chave para a prova:** tempo da instrução = nº de ciclos × período (período = 1/f; 2 GHz → 0,5 ns). Etapas: **buscar → decodificar → obter operandos → executar → registrar**. O **opcode** identifica a operação. Uma versão de "ordenação" pode trocar "decodificar" e "obter operandos" de lugar: a ordem correta é decodificar **antes**.

---

## I9 — CISC × RISC: o que NÃO é verdade
**Subtópico coberto:** Tópico 8, Arquiteturas CISC e RISC (Revisão p. 13; slides p. 16)
**Por que é provável:** a apostila dedica um parágrafo inteiro a desfazer mitos ("É importante não decorar a ideia errada de que RISC significa 'uma instrução = um ciclo' ou que RISC sempre é mais rápido"), e o "O que lembrar" repete esses pontos. A Q1 só usa load/store e µops, como apoio à discussão de pipeline.
**Prioridade:** Média
**Tipo ENADE:** Afirmativa negativa (INCORRETA)

**Enunciado:**
Ao escolher a plataforma de um novo servidor de aplicações, uma equipe compara processadores x86 com processadores baseados em Arm e em RISC-V. Durante a reunião técnica, foram feitas várias afirmações sobre as abordagens CISC e RISC de projeto do conjunto de instruções.

Assinale a alternativa **INCORRETA**.

**Alternativas:**
- **A)** CISC e RISC são tendências de projeto do conjunto de instruções (ISA), e não uma divisão absoluta. Processadores modernos de ambas as famílias utilizam pipeline e outras técnicas avançadas.
- **B)** No modelo *load/store*, associado a RISC, instruções específicas transferem dados entre memória e registradores, e as operações aritméticas trabalham principalmente com registradores.
- **C)** O x86, tradicionalmente associado a CISC, apresenta instruções mais complexas, com formatos e modos de endereçamento mais variados, e algumas instruções podem acessar operandos na memória.
- **D)** Por definição, um processador RISC executa cada instrução em exatamente um ciclo de *clock*, o que garante que ele seja sempre mais rápido que um CISC executando o mesmo programa, qualquer que seja o compilador.
- **E)** O microcódigo é historicamente associado a CISC, mas não é exclusivo dessa abordagem, e o desempenho final depende também da implementação, do compilador, do programa e do sistema de memória.

**Gabarito: D**

**Por que cada alternativa está certa ou errada:**
- **A) ❌ (afirmação correta)** — "CISC e RISC são tendências de projeto do conjunto de instruções (ISA). Elas não devem ser tratadas como uma divisão absoluta…"; "Processadores modernos de diferentes famílias utilizam pipeline e técnicas avançadas."
- **B) ❌ (afirmação correta)** — É a descrição de load/store da apostila e do slide 16 ("Modelo load/store", "Forte uso de registradores").
- **C) ❌ (afirmação correta)** — Slide 16: "Instruções mais complexas; mais variedade de formatos e modos de endereçamento; algumas instruções podem acessar operandos na memória. Exemplo tradicional: x86."
- **D) ✅ (afirmação INCORRETA)** — Junta os dois mitos que a apostila manda não decorar: "RISC = uma instrução por ciclo" e "RISC sempre é mais rápido". O desempenho "depende também da implementação, do compilador, do programa e do sistema de memória".
- **E) ❌ (afirmação correta)** — "Microcódigo… é historicamente associado a CISC, mas não é exclusivo dessa abordagem", e a parte sobre desempenho repete a apostila.

**Base no material:** Revisão p. 13 (explicação, tabela e "O que lembrar na prova": "CISC e RISC são tendências de ISA. Load/store é uma característica importante na descrição de RISC. Microcódigo não é exclusividade de CISC. Não associe RISC automaticamente a maior desempenho"); slides p. 16.
**Conceito-chave para a prova:** CISC/RISC = **tendências**. RISC → **load/store**, regularidade, registradores (Arm, RISC-V). CISC → instruções complexas, formatos variados, operandos em memória (x86). **Microcódigo não é exclusivo de CISC.** RISC **não** é "1 ciclo por instrução" nem "sempre mais rápido".

---

## I10 — HDD: trilha, setor, cilindro, LBA e seek (associação)
**Subtópico coberto:** Tópico 9, Discos magnéticos: conceitos básicos (Revisão p. 14; slides p. 17–18)
**Por que é provável:** o tópico tem uma tabela-resumo de três termos geométricos (trilha, setor, cilindro), e o slide 18 é uma figura do prato com trilhas, setores, cabeçote e braço. Isso é material típico de associação. O "O que lembrar" acrescenta seek e LBA.
**Prioridade:** Alta
**Tipo ENADE:** Associação

**Enunciado:**
Um técnico explica a estrutura interna de um HDD com o auxílio da figura a seguir.

[Figura (slides p. 18): um prato (disco) girando no sentido rotacional indicado por uma seta. Na superfície há trilhas concêntricas, divididas em setores. Um cabeçote de leitura/gravação fica na ponta de um braço de posicionamento do cabeçote.]

Relacione os conceitos da coluna I às descrições da coluna II.

| Coluna I | Coluna II |
|---|---|
| 1. Trilha | ( ) Numeração lógica de blocos apresentada ao sistema operacional, que separa a visão lógica da geometria física do disco. |
| 2. Setor | ( ) Círculo concêntrico gravado na superfície de um prato. |
| 3. Cilindro | ( ) Deslocamento da cabeça de leitura/gravação, movida pelo atuador, até a trilha desejada. |
| 4. LBA | ( ) Subdivisão de uma trilha, utilizada para armazenar os dados. |
| 5. *Seek* | ( ) Conjunto de trilhas que ocupam a mesma posição radial em superfícies diferentes. |

A sequência correta dos números, de cima para baixo, é:

**Alternativas:**
- **A)** 4 – 1 – 5 – 2 – 3.
- **B)** 4 – 2 – 5 – 1 – 3.
- **C)** 3 – 1 – 5 – 2 – 4.
- **D)** 4 – 1 – 3 – 2 – 5.
- **E)** 5 – 2 – 4 – 1 – 3.

**Gabarito: A**

**Associação correta:** numeração lógica de blocos = **4 (LBA)**; círculo concêntrico = **1 (trilha)**; deslocamento da cabeça = **5 (seek)**; subdivisão da trilha = **2 (setor)**; trilhas de mesmo raio em superfícies diferentes = **3 (cilindro)**.

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — 4 – 1 – 5 – 2 – 3, todas as associações corretas.
- **B) ❌** — Troca trilha e setor, a confusão mais comum: o setor é **parte** da trilha.
- **C) ❌** — Troca cilindro e LBA. Cilindro é conceito geométrico; LBA é endereçamento lógico.
- **D) ❌** — Troca cilindro e seek. Seek é movimento/tempo, e não uma estrutura.
- **E) ❌** — Erra quase todas: põe seek no lugar de LBA, setor no lugar de trilha e vice-versa, e LBA no lugar de seek.

**Base no material:** Revisão p. 14 ("trilhas são círculos concêntricos… Setores são subdivisões das trilhas. Cilindros reúnem trilhas que ocupam a mesma posição radial em superfícies diferentes"; "o disco costuma apresentar blocos numerados por endereçamento lógico, o LBA"; "O que lembrar": "Seek está ligado ao posicionamento da cabeça. LBA fornece uma visão lógica dos blocos"); slides p. 17 (pratos, cabeças, atuador) e p. 18 (figura).
**Conceito-chave para a prova:** trilha = círculo; setor = pedaço da trilha; cilindro = trilhas de mesmo raio em superfícies diferentes; **LBA = visão lógica** (o SO enxerga blocos numerados, e não a geometria); seek = mover a cabeça. HDD é **não volátil** e **mecânico**.

---

## I11 — HDD: cálculo do tempo de acesso aleatório e IOPS
**Subtópico coberto:** Tópico 10, Discos magnéticos: parâmetros de desempenho (Revisão p. 15; slides p. 19)
**Por que é provável:** o tópico define seek, latência rotacional, transferência, tempo de resposta, throughput e IOPS, e o slide 19 tem os quatro quadros. É o subtópico mais "calculável" de todo o material, e o squad gosta de situação-problema prática.
**Prioridade:** Média
**Tipo ENADE:** Resposta única (cálculo)

**Enunciado:**
Um administrador avalia se um HDD de 7.200 RPM atende a um banco de dados que realiza leituras **aleatórias** de 4 KB. O fabricante informa tempo médio de busca (*seek*) de 5,8 ms e taxa de transferência sustentada de 120 MB/s.

Considere: latência rotacional média = tempo de meia rotação; 1 KB = 1.000 bytes; 1 MB = 1.000.000 bytes. Desconsidere o tempo de fila e de processamento no controlador.

O tempo médio de cada leitura aleatória e a quantidade aproximada de operações de E/S por segundo (IOPS) que esse disco consegue atender são, respectivamente:

**Alternativas:**
- **A)** 5,83 ms e cerca de 171 IOPS.
- **B)** 14,17 ms e cerca de 71 IOPS.
- **C)** 10,0 ms e cerca de 100 IOPS.
- **D)** 4,2 ms e cerca de 238 IOPS.
- **E)** 0,033 ms e cerca de 30.000 IOPS.

**Gabarito: C**

**Resolução (conferida em python):**
- Uma rotação: 60 s / 7.200 = 8,333 ms → latência rotacional média = 8,333 / 2 = **4,167 ms**.
- Transferência: 4.000 B / 120.000.000 B/s = **0,033 ms**.
- Tempo de acesso = seek + latência rotacional + transferência = 5,8 + 4,167 + 0,033 = **10,0 ms**.
- IOPS ≈ 1 / 0,010 s = **100 IOPS**. A vazão efetiva nesse padrão é 100 × 4 KB = **0,4 MB/s**, cerca de 300 vezes menor que os 120 MB/s do acesso sequencial.

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — 5,8 + 0,033 = 5,83 ms: esquece a **latência rotacional**.
- **B) ❌** — 5,8 + 8,333 + 0,033 = 14,17 ms: usa a rotação **inteira** em vez da média de meia rotação.
- **C) ✅** — Soma correta dos três componentes: 10 ms → 100 IOPS.
- **D) ❌** — 4,167 + 0,033 = 4,2 ms: esquece o **seek**.
- **E) ❌** — Considera só a transferência (120 MB/s ÷ 4 KB = 30.000), como se o acesso fosse sequencial e não houvesse custo mecânico. É o erro de achar que a "interface rápida garante a taxa nominal".

**Base no material:** Revisão p. 15 ("Seek time é o tempo associado ao deslocamento da cabeça… Latência rotacional é a espera para que o setor desejado fique sob a cabeça. Tempo de transferência é o período de envio…"; "IOPS representa quantas operações de entrada e saída são realizadas por segundo"; "Em acessos aleatórios, a cabeça precisa mudar de posição com mais frequência"); slides p. 19. A latência média igual a meia rotação é conhecimento padrão (referência Seagate, "How to Model Hard Drive Performance", p. 22).
**Conceito-chave para a prova:** **tempo de acesso = seek + latência rotacional (½ volta) + transferência** (o tempo de resposta pode somar fila e controlador). IOPS ≈ 1 / tempo de acesso. Em acesso aleatório o HDD é limitado pela **mecânica**, e não pela interface.

---

## I12 — HDD: throughput × IOPS, sequencial × aleatório
**Subtópico coberto:** Tópico 10, Discos magnéticos: parâmetros de desempenho (Revisão p. 15)
**Por que é provável:** os três itens do "O que lembrar na prova" do tópico 10 ("Throughput e IOPS medem coisas diferentes"; "Acesso aleatório sofre mais"; "Interface rápida não garante taxa sustentada") e o "Exemplo simples" (arquivo grande contínuo × milhares de arquivos pequenos) formam um cenário pronto para asserção-razão.
**Prioridade:** Alta
**Tipo ENADE:** Asserção-razão

**Enunciado:**
Um analista mede o desempenho de um HDD SATA III (interface de 6 Gb/s) de 7.200 RPM em duas cargas de trabalho:

| Carga | Descrição | Resultado medido |
|---|---|---|
| 1 | Cópia contínua de um único arquivo de 20 GB | ≈ 180 MB/s |
| 2 | Leitura de 100.000 arquivos de 4 KB espalhados pelo disco | ≈ 120 IOPS (≈ 0,5 MB/s) |

Com base nesses resultados, avalie as asserções a seguir:

I. Na carga 2, o desempenho do HDD deve ser avaliado principalmente em IOPS, e a vazão muito inferior à da carga 1 é um comportamento esperado para esse tipo de dispositivo, e não necessariamente um defeito.

PORQUE

II. A velocidade nominal da interface SATA III, de 6 Gb/s (cerca de 600 MB/s), é superior à taxa sustentada que o HDD consegue entregar mesmo na carga 1.

A respeito dessas asserções, assinale a opção correta:

**Alternativas:**
- **A)** As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
- **B)** As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
- **C)** A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
- **D)** A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
- **E)** As asserções I e II são proposições falsas.

**Gabarito: B**

**Julgamento:**
- **Asserção I — Verdadeira.** A carga 2 tem muitas operações pequenas, e para ela a métrica relevante é IOPS. A queda de vazão é esperada: "Acesso aleatório sofre mais com a mecânica do HDD". Conferência: 120 IOPS × 4 KB = 0,48 MB/s ≈ 0,5 MB/s.
- **Asserção II — Verdadeira.** 6 Gb/s com codificação 8b/10b dá cerca de 600 MB/s, bem acima dos 180 MB/s que o disco sustenta ("Interface rápida não garante taxa sustentada igual à nominal").
- **Relação — A II não justifica a I.** A II explica por que a carga 1 não chega a 600 MB/s, mas não explica a queda na carga 2. O motivo da queda é mecânico: em cada acesso aleatório a cabeça precisa ser reposicionada (*seek*) e esperar o setor (latência rotacional). Essa seria a justificativa correta.

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Armadilha principal: as duas são verdadeiras, mas a justificativa da I é o custo mecânico do acesso aleatório, e não a velocidade da interface.
- **B) ✅** — As duas são verdadeiras e não há relação de causa entre elas.
- **C) ❌** — A II é verdadeira: a interface é mais rápida que o disco.
- **D) ❌** — A I é verdadeira: IOPS é a métrica adequada e a queda é esperada.
- **E) ❌** — As duas asserções são verdadeiras.

**Base no material:** Revisão p. 15 ("Vazão (throughput) representa o volume de dados transferido por unidade de tempo. IOPS representa quantas operações… por segundo"; "Em acessos aleatórios, a cabeça precisa mudar de posição com mais frequência, aumentando os custos mecânicos"; "A velocidade nominal da interface não é uma garantia da taxa sustentada"; "Exemplo simples"); slides p. 19.
**Conceito-chave para a prova:** **throughput = MB/s** (importa no sequencial); **IOPS = operações/s** (importa em muitos acessos pequenos). HDD aleatório é lento por causa de **seek + latência rotacional**. Se a II de uma versão alterada disser "em acessos aleatórios a cabeça precisa ser reposicionada com mais frequência…", a resposta passa a ser **A**.
