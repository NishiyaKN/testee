# Arquitetura de Computadores — Questões e Gabarito Comentado

**Squad responsável:** Squad 5
**Materiais analisados:**
| Arquivo | Páginas | Tipo | Questões encontradas (páginas) |
|---|---|---|---|
| `Apresentação Arquitetura de Computadores.pdf` | 41 | Slides | Q1–Q3 (p. 34–40: p. 34 = divisória "Questões"; enunciados nas p. 35, 37 e 39; gabaritos comentados nas p. 36, 38 e 40). Todas essas páginas são só imagem e foram lidas renderizadas. |
| `Revisão Arquitetura de Computadores-1.pdf` | 22 | Apostila de revisão (material explicativo) | Nenhuma questão. Tem 16 tópicos com "Explicação detalhada", "Exemplo simples", tabela-resumo e "O que lembrar na prova", além de referências (p. 22). Serve de apoio teórico para as 3 questões. |

**Resumo:** 3 questões encontradas, todas nos slides e todas no padrão ENADE: 2 de afirmativas múltiplas e 1 de asserção-razão. As 3 têm gabarito comentado no próprio material, e nas 3 o gabarito confere com a conferência independente (Q1 = A, Q2 = C, Q3 = A). Nenhuma questão aparece em mais de um arquivo, então não há versões divergentes entre os materiais.

> Legenda: ✅ correta · ❌ incorreta · ⚠️ ponto de atenção (gabarito do material duvidoso, ambiguidade, versão divergente)

## Índice
1. [Q1 — Pipeline, hazards e ISA](#q1--pipeline-hazards-e-isa)
2. [Q2 — Registradores no ciclo de busca e desvio](#q2--registradores-no-ciclo-de-busca-e-desvio)
3. [Q3 — DMA, interrupção e polling](#q3--dma-interrupção-e-polling)
4. [Apêndice — Pontos da apostila úteis para versões alteradas](#apêndice--pontos-da-apostila-úteis-para-versões-alteradas)

---

## Q1 — Pipeline, hazards e ISA
**Fonte:** `Apresentação Arquitetura de Computadores.pdf`, p. 35 (enunciado) e p. 36 (gabarito comentado). Teoria correspondente em `Revisão Arquitetura de Computadores-1.pdf`, p. 12 (Pipeline) e p. 13 (CISC e RISC), e nos slides p. 13–16.
**Tipo ENADE:** Afirmativas múltiplas

**Enunciado:**
Na análise de desempenho de processadores, o paralelismo em nível de instrução (ILP) via *pipelining* busca otimizar a vazão (*throughput*) de execução. No entanto, a presença de *hazards* (conflitos) exige mecanismos de tratamento específicos pela microarquitetura. Avalie as afirmativas a seguir sobre a relação entre a arquitetura do conjunto de instruções (ISA) e o comportamento do *pipeline*:

I. O modelo *load/store*, característico de arquiteturas predominantemente RISC, simplifica o projeto dos estágios do *pipeline*, pois restringe as operações aritméticas e lógicas aos registradores internos, isolando os acessos à memória em instruções específicas.

II. O uso da técnica de *forwarding* (ou encaminhamento) é uma solução voltada para solucionar *hazards* de controle causados por desvios condicionais imprevistos, evitando o descarte do trabalho especulativo.

III. Arquiteturas CISC com instruções de múltiplos ciclos e formatos variáveis enfrentam maior complexidade no projeto de *pipelines*, motivo pelo qual muitos processadores CISC modernos traduzem instruções complexas em operações internas mais simples e regulares (micro-operações).

IV. O ganho de desempenho obtido pelo uso de um *pipeline* de 5 estágios reflete-se primariamente na redução drástica da latência individual de cada instrução isolada.

É correto o que se afirma em:

**Alternativas:**
- **A)** I e III, apenas.
- **B)** I e II, apenas.
- **C)** II e IV, apenas.
- **D)** I, III e IV, apenas.
- **E)** I, II, III e IV.

**Gabarito: A** — _(origem: gabarito do próprio material, p. 36; conferido aqui e confirmado)_

Texto do gabarito comentado (p. 36), transcrito: *"Item I (Correto): O modelo load/store garante que a ULA opere apenas sobre registradores, padronizando a latência dos estágios. Item III (Correto): CPUs CISC modernas (ex: x86) traduzem instruções complexas em micro-operações (µops) regulares para manter o fluxo contínuo do pipeline. Análise dos Incorretos: O item II é falso porque forwarding resolve hazards de dados (não de controle/desvio). O item IV é falso porque o pipeline aumenta o throughput (vazão), mas não reduz a latência individual da instrução."*

**Julgamento das afirmativas:**
- **I — Verdadeira.** No modelo load/store (RISC: Arm, RISC-V), só as instruções LOAD e STORE acessam a memória. As instruções aritméticas e lógicas trabalham sobre registradores. Com isso cada instrução passa pelos estágios de forma regular (formato fixo, no máximo um acesso à memória, no estágio MEM), o que simplifica o pipeline.
- **II — Falsa.** *Forwarding/bypassing* trata **hazards de dados**: ele leva o resultado de uma instrução, ainda no pipeline, direto para a entrada da ULA da instrução seguinte que depende dele, sem esperar a escrita no banco de registradores. *Hazards de controle* (desvios) são tratados com **previsão de desvio**, inserção de bolhas/stalls ou desvio atrasado. "Evitar o descarte do trabalho especulativo" também não é papel do forwarding: quando a previsão de desvio erra, o trabalho especulativo é descartado (flush). A apostila (p. 12) diz: "Forwarding ajuda com dependências de dados" e "Previsão errada de desvio pode causar descarte de trabalho especulativo".
- **III — Verdadeira.** Instruções CISC (x86) têm tamanho e formato variáveis, vários modos de endereçamento e operandos em memória, o que dificulta o pipeline. Os processadores x86 modernos decodificam essas instruções em micro-operações (µops) simples e regulares, que alimentam um núcleo interno de estilo RISC.
- **IV — Falsa.** O pipeline aumenta a **vazão** (instruções concluídas por unidade de tempo), mas **não** reduz a latência de uma instrução isolada. Essa latência continua sendo a soma dos estágios e pode até crescer um pouco, por causa dos registradores entre estágios e do balanceamento pelo estágio mais lento. Exemplo: com 5 estágios de 1 ns, cada instrução ainda leva 5 ns do início ao fim, mas, com o pipeline cheio, sai 1 instrução por ns. Para n instruções o tempo cai de 5n para (5 + n − 1) ciclos. É o que mostra o diagrama do slide 14: a instrução 1 termina no tempo 5 e, a partir daí, uma instrução termina por ciclo.

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — Reúne exatamente as afirmativas verdadeiras, I e III.
- **B) ❌** — Inclui II, que confunde *hazard* de dados com *hazard* de controle, e omite a III, que é verdadeira.
- **C) ❌** — As duas afirmativas listadas são falsas: II (forwarding ≠ solução para desvios) e IV (pipeline ≠ redução de latência).
- **D) ❌** — Inclui a IV. É a pegadinha clássica "pipeline reduz a latência de cada instrução", quando o ganho é de vazão.
- **E) ❌** — II e IV são falsas.

**Conceito-chave para a prova:** Pipeline aumenta a **vazão (throughput)**, não reduz a latência individual. **Forwarding → hazard de dados**; **previsão de desvio/flush → hazard de controle**; **hazard estrutural → disputa por recurso** (resolvida com duplicação de recursos ou stall). Load/store (RISC) facilita o pipeline, e CISC moderno traduz para µops. Se a versão da prova trocar "latência" por "vazão" na IV, ela fica verdadeira (resposta passaria a "I, III e IV"). Se trocar "controle" por "dados" na II, a II fica verdadeira até "evitando o descarte do trabalho especulativo" (atenção a esse trecho final, que continua ligado a desvio).

---

## Q2 — Registradores no ciclo de busca e desvio
**Fonte:** `Apresentação Arquitetura de Computadores.pdf`, p. 37 (enunciado) e p. 38 (gabarito comentado). Teoria correspondente em `Revisão Arquitetura de Computadores-1.pdf`, p. 9 (Principais registradores) e p. 11 (Ciclo de máquina), e nos slides p. 9 e 12.
**Tipo ENADE:** Afirmativas múltiplas

**Enunciado:**
Durante o ciclo de busca (*fetch*) e execução de uma instrução de desvio condicional em linguagem de máquina (ex: `JZ target` — desvia para target se a flag *Zero* estiver ativa), a CPU coordena o fluxo entre seus registradores internos. Avalie as afirmativas a seguir:

I. Na etapa de busca, a CPU copia o valor do *Program Counter* (PC) para o *Memory Address Register* (MAR) a fim de indicar ao barramento de endereços a posição de memória a ser lida.

II. O resultado da instrução em processamento permanece retido dentro do *Instruction Register* (IR), registrador encarregado de armazenar também as *flags* de estado como *Zero*, *Overflow* e *Carry*.

III. O *Memory Data Register* (MDR) armazena temporariamente a instrução ou dado lido da memória antes de seu encaminhamento interno para os registradores da CPU.

IV. Se a condição do desvio for satisfeita, o endereço de destino (target) é carregado no *Program Counter* (PC), alterando a sequência normal de execução.

É correto o que se afirma em:

**Alternativas:**
- **A)** I e II, apenas.
- **B)** III e IV, apenas.
- **C)** I, III e IV, apenas.
- **D)** II, III e IV, apenas.
- **E)** I, II, III e IV.

**Gabarito: C** — _(origem: gabarito do próprio material, p. 38; conferido aqui e confirmado)_

Texto do gabarito comentado (p. 38), transcrito: *"Itens I, III e IV (Corretos): O PC indica o endereço ao MAR no fetch; o MDR guarda o conteúdo trafegado no barramento; e a atualização do PC com o endereço target efetiva o desvio de fluxo. Item II (Incorreto): O IR armazena apenas o código da instrução atual. As flags de estado (Zero, Overflow) ficam no Registrador de Estado/Flags (EFLAGS ou PSW)."*

**Julgamento das afirmativas:**
- **I — Verdadeira.** A micro-sequência clássica do *fetch* é `MAR ← PC`, depois `MDR ← Mem[MAR]` (o endereço vai para o barramento de endereços e a leitura é sinalizada no barramento de controle), depois `IR ← MDR` e `PC ← PC + 1` (ou + tamanho da instrução).
- **II — Falsa.** O IR guarda a **instrução** atual (opcode e campos) para ser decodificada. Ele não guarda o resultado nem as flags. O resultado vai para o registrador de destino ou para a memória. As flags (Zero, Sinal, Overflow, Carry) ficam no **registrador de estado/flags** (PSW, FLAGS/EFLAGS no x86, CPSR no Arm). A instrução `JZ` consulta justamente a flag Zero desse registrador, que foi ajustada por uma instrução anterior (ex.: `CMP`/`SUB`).
- **III — Verdadeira.** O MDR (ou MBR) é o "buffer" entre a CPU e o barramento de dados: recebe o conteúdo lido da memória (instrução ou dado) antes de ele ir para o IR ou para outro registrador, e guarda o conteúdo a ser escrito. Na apostila: "MAR é associado ao endereço; MDR ao conteúdo".
- **IV — Verdadeira.** Desvio = alteração do PC. Se a flag Zero estiver ativa, `PC ← target`. Se não estiver, o PC mantém o valor já incrementado no fetch e a execução segue em sequência.

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Inclui a II (falsa) e deixa de fora III e IV, que são verdadeiras.
- **B) ❌** — Omite a I, que é verdadeira (PC → MAR no fetch).
- **C) ✅** — I, III e IV são exatamente as verdadeiras.
- **D) ❌** — Inclui a II (falsa) e omite a I (verdadeira).
- **E) ❌** — A II é falsa: o IR não armazena resultado nem flags.

**Conceito-chave para a prova:** **PC** = endereço da próxima instrução (não guarda a instrução). **IR** = instrução em execução. **MAR** = endereço do acesso à memória. **MDR/MBR** = conteúdo transferido. **SP** = topo da pilha. **Flags/PSW** = estado (zero, sinal, overflow, carry). Um desvio é efetivado carregando o endereço-alvo no PC. A pegadinha mais provável numa versão alterada é trocar qual registrador guarda o quê (ex.: "PC guarda a instrução", "MAR guarda o dado", "IR guarda as flags").

---

## Q3 — DMA, interrupção e polling
**Fonte:** `Apresentação Arquitetura de Computadores.pdf`, p. 39 (enunciado) e p. 40 (gabarito comentado). Teoria correspondente em `Revisão Arquitetura de Computadores-1.pdf`, p. 10 (Interfaces entre processador, memória e E/S), e nos slides p. 10–11.
**Tipo ENADE:** Asserção-razão

**Enunciado:**
Um sistema de vídeo lê constantemente grandes blocos de dados (vídeo 4K) do disco para a memória RAM, enquanto simultaneamente recebe comandos curtos e imprevisíveis de um teclado. Considerando o uso adequado dos mecanismos de E/S, avalie as asserções a seguir:

I. A transferência dos blocos de dados do disco para a RAM deve ser realizada por um controlador de DMA (*Direct Memory Access*), enquanto as entradas do teclado devem utilizar o mecanismo de interrupção.

PORQUE

II. O DMA permite a transferência massiva de dados diretamente entre o periférico e a memória sem a intervenção da CPU instrução por instrução, enquanto as interrupções tratam eventos imprevisíveis de baixa frequência evitando o desperdício de ciclos em *polling* (espera ocupada).

A respeito dessas asserções, assinale a opção correta:

**Alternativas:**
- **A)** As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
- **B)** As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
- **C)** A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
- **D)** A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
- **E)** As asserções I e II são proposições falsas.

**Gabarito: A** — _(origem: gabarito do próprio material, p. 40; conferido aqui e confirmado)_

Texto do gabarito comentado (p. 40), transcrito: *"Justificativa: Ambas são verdadeiras e a II justifica a I. O DMA é desenhado para transferências contínuas de alto volume sem ocupar a ULA. A interrupção é ideal para eventos lentos/assíncronos (teclado), pois não gasta ciclos da CPU verificando o estado do periférico repetidamente como no polling."*

**Julgamento:**
- **Asserção I — Verdadeira.** Fluxo grande e contínuo (blocos de vídeo do disco para a RAM) é o caso típico de DMA: o controlador copia os blocos sem que a CPU copie palavra por palavra. Eventos curtos, raros e assíncronos (teclas) são o caso típico de interrupção: o dispositivo avisa quando há dado e a CPU executa a rotina de atendimento.
- **Asserção II — Verdadeira.** Descreve corretamente os dois mecanismos. No DMA a CPU só configura a transferência (endereço, tamanho, direção) e é avisada no fim, normalmente por uma interrupção. A interrupção evita a espera ocupada (*busy waiting*) do polling, em que a CPU consulta o dispositivo repetidamente e gasta ciclos à toa.
- **Relação — A II justifica a I.** A II dá exatamente o motivo da escolha feita na I: DMA porque o volume é alto e não convém a CPU copiar cada unidade; interrupção porque os eventos são imprevisíveis e de baixa frequência, e o polling desperdiçaria ciclos.

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — As duas são verdadeiras e a II explica diretamente a I.
- **B) ❌** — As duas são verdadeiras, mas a II **é** justificativa da I, porque trata dos mesmos dois mecanismos e do critério de escolha de cada um. Esta é a armadilha "verdadeiras, mas sem relação".
- **C) ❌** — A II não é falsa. "Sem a intervenção da CPU instrução por instrução" está correto, pois o DMA dispensa a cópia unidade por unidade feita pela CPU.
- **D) ❌** — A I não é falsa: DMA para volume e interrupção para teclado é a combinação adequada.
- **E) ❌** — As duas asserções estão corretas.

**⚠️ Atenção:** O gabarito (A) está correto. Há só uma imprecisão no texto do gabarito comentado: "sem ocupar a ULA". O certo seria "sem ocupar a CPU com a cópia de cada unidade de dado". A apostila (p. 10) é mais precisa: "DMA reduz a participação da CPU, mas não elimina custos de banda e coordenação". A CPU configura a operação e acompanha a conclusão, e o controlador de DMA disputa o barramento com a CPU (roubo de ciclo). Numa versão alterada, uma afirmação como "o DMA elimina totalmente a participação da CPU" ou "o DMA não consome largura de banda do barramento" deve ser julgada **falsa**. O trecho "instrução por instrução" da asserção II é o que a torna verdadeira.

**Conceito-chave para a prova:** **Polling** = a CPU pergunta repetidamente (simples, mas gasta CPU, é espera ocupada). **Interrupção** = o dispositivo avisa (bom para eventos assíncronos e pouco frequentes, como teclado e mouse). **DMA** = o controlador transfere blocos entre dispositivo e memória (bom para grande volume, como disco, rede e vídeo), com a CPU só configurando e recebendo o aviso de término. Se a versão trocar os papéis (ex.: "teclado por DMA e disco por polling"), a I fica falsa.

---

## Apêndice — Pontos da apostila úteis para versões alteradas
Este apêndice não contém questões, porque a apostila `Revisão Arquitetura de Computadores-1.pdf` não tem nenhuma. São as frases da seção "O que lembrar na prova" e trechos da explicação que mais servem como pegadinha em versões alteradas das questões acima ou em afirmativas sobre o restante do conteúdo:

- **Arquitetura × organização (p. 4–5):** arquitetura é o que a ISA expõe ao programador (instruções, registradores, endereçamento); organização é a implementação física. O gargalo de von Neumann vem do caminho compartilhado entre CPU e memória para instruções e dados. Harvard separa memórias e caminhos. Harvard modificada tem memória principal unificada com caches de instrução e de dados separadas.
- **Barramentos (p. 6):** o de dados leva os valores, o de endereços diz onde, o de controle diz tipo e momento (leitura/escrita). PCIe usa enlaces seriais ponto a ponto, diferente de SATA, que é interface de armazenamento. USB é para periféricos. Plug and Play facilita a configuração, mas **não garante compatibilidade**.
- **Memória (p. 7–8):** quanto mais perto da CPU, menor, mais rápida e mais cara por bit. **SRAM**: volátil, sem refresh, usada em cache. **DRAM**: volátil, com refresh, usada na memória principal. ROM e flash não são voláteis. A cache explora localidade **temporal** e **espacial** (hit/miss). Memória virtual **não** torna o disco equivalente à RAM.
- **Ciclo de instrução (p. 11):** buscar, decodificar, obter operandos, executar, registrar o resultado. Ciclo de instrução ≠ ciclo de clock: uma instrução pode levar vários ciclos de clock. O opcode identifica a operação.
- **CISC × RISC (p. 13):** são tendências de ISA, não uma divisão absoluta. Microcódigo **não** é exclusivo de CISC. **Não** é verdade que RISC significa "uma instrução = um ciclo" nem que RISC é sempre mais rápido.
- **HDD (p. 14–15):** trilha = círculo concêntrico; setor = parte da trilha; cilindro = trilhas de mesmo raio em superfícies diferentes. LBA dá a visão lógica dos blocos. Tempo de acesso = seek (mover a cabeça) + latência rotacional (esperar o setor) + transferência; o tempo de resposta pode incluir fila e controlador. **Throughput (MB/s) ≠ IOPS (operações/s)**. Acesso aleatório sofre mais com a mecânica. Interface rápida não garante taxa sustentada igual à nominal.
- **RAID (p. 16–17):** RAID 0 = striping **sem** redundância. RAID 1 = espelhamento. RAID 2 = bits + Hamming. RAID 3 = bytes + paridade dedicada. RAID 4 = blocos + paridade **dedicada**, com gargalo nas escritas. RAID 5 = paridade **distribuída**, tolera 1 falha. RAID 10 = espelhamento e depois striping, com no mínimo 4 discos e metade da capacidade útil; suporta várias falhas desde que nenhum espelho perca todas as cópias. **RAID 10 ≠ RAID 0+1.** RAID **não substitui backup**. Tolerar falha não significa manter o mesmo desempenho (há reconstrução).
- **SSD (p. 18):** flash NAND, sem partes móveis. Grava em **páginas** e apaga em **blocos**. Garbage collection, wear leveling. **TRIM não é apagamento seguro imediato.** **M.2 é formato físico** e não garante NVMe. NVMe é o protocolo sobre PCIe.
- **DAS/NAS/SAN (p. 19–21):** **DAS** = ligação direta; pode ser externo (USB/SAS) e o hospedeiro administra. Um servidor que compartilha um DAS não o transforma em NAS. **NAS** = rede + **arquivos** (SMB/NFS); o NAS administra sistema de arquivos e permissões. **SAN** = rede dedicada + **blocos** (Fibre Channel, iSCSI); **não** exige fibra óptica e o servidor administra o volume. Acesso aos mesmos blocos **não** é compartilhamento seguro de arquivos (precisa de cluster ou sistema de arquivos compatível).
