# Sistemas Operacionais — Questões e Gabarito Comentado

**Squad responsável:** Squad 6 (Jorge Orselli Mutran, Kaick Kenithi Nishiya, Lucas Koiti Zotovici Kobayashi, Lucas Secanho do Prado, Matheus Pestilli Rodrigues João)

**Materiais analisados:**
| Arquivo | Páginas | Tipo | Questões encontradas (páginas) |
|---|---|---|---|
| `SISTEMAS_OPERACIONAIS - GABARITO.pdf` | 22 | Gabarito comentado das "12 questões objetivas — Tema 6". Traz tipo, letra correta, texto literal de todas as alternativas e a justificativa de cada uma, mas **não traz o enunciado** | Q1–Q12 (gabarito resumido na p. 2; questões nas p. 3–21) |
| `Slides.pdf` | 53 | Slides "Revisão para o ENADE 2026 – Sistemas Operacionais – Squad 6" | 5 questões completas, numeradas 1–5 nos slides = Q2, Q5, Q7, Q8 e Q12 do caderno (p. 11–12, 26–27, 33–35, 42–44, 51–52) + 1 exercício sugerido (E1, p. 35) |
| `SISTEMAS_OPERACIONAIS - MATERIAL_EXPLICATIVO.pdf` | 57 | Apostila (material explicativo dos 9 tópicos) | Nenhuma questão. Só remete ao "caderno de questões" (p. 15, 28, 34, 43, 50) e comenta Q1 (p. 5), Q2 (p. 10), Q3 (p. 51), Q4 (p. 16), Q5 (p. 25), Q6 (p. 21), Q7 (p. 32), Q9 (p. 41), Q10 (p. 46) e Q12 (p. 48) |

**Resumo:** 12 questões objetivas no padrão ENADE (Q1–Q12, na numeração do caderno/gabarito) e 1 exercício sugerido nos slides (E1). As 12 questões têm gabarito no próprio material; o E1 não tem e foi resolvido aqui. Todos os gabaritos foram conferidos (cálculos refeitos com simulação em Python) e **todos estão corretos**.

> ⚠️ **Material incompleto: falta o caderno de questões.** A apostila manda "consultar o caderno de questões" (questões 1 a 12), mas esse arquivo **não está entre os PDFs**. O GABARITO.pdf só traz alternativas e justificativas. Por isso:
> - **5 questões têm enunciado completo**, tirado dos slides: Q2, Q5, Q7, Q8 e Q12.
> - **7 questões têm alternativas literais, mas o enunciado foi reconstruído** a partir das justificativas e das figuras do gabarito: Q1, Q3, Q4, Q6, Q9, Q10 e Q11. Na Q9 e na Q11, as afirmativas I–IV também foram reconstruídas: o conteúdo de cada uma sai do comentário com segurança, a redação literal não. Essas partes vêm marcadas com *[Reconstruído]*.
>
> **Correspondência de numeração:** Slides Q1 = caderno Q2 · Slides Q2 = Q5 · Slides Q3 = Q7 · Slides Q4 = Q8 · Slides Q5 = Q12.
> **A letra correta muda entre as versões em duas questões:** Q2 (D no gabarito, A nos slides) e Q7 (C no gabarito, B nos slides). Na Q8 os distratores B, C e D são outros. Memorize o **conteúdo** da resposta, não a letra.

**Gabarito rápido**
| Questão | Tipo | Gabarito (GABARITO.pdf) | Gabarito (Slides) | Conteúdo da resposta correta |
|---|---|---|---|---|
| Q1 | Lacunas | C | — | máquina estendida / gerenciador de recursos / montador / interpretador |
| Q2 | V/F (alternativas constantes) | D | A (Questão 1) | V – F – V – F |
| Q3 | Ordenação | B | — | 2 – 4 – 1 – 5 – 3 (POST → dispositivo → gerenciador de boot → kernel → init) |
| Q4 | Afirmativa incompleta | A | — | PCB (Bloco de Controle de Processo) |
| Q5 | Asserção-razão | D | D (Questão 2) | I falsa, II verdadeira |
| Q6 | Interpretação (cálculo) | B | — | SRTF, espera média 3,0 ms |
| Q7 | Resposta única | C | B (Questão 3) | área de 300 KB; fragmentação externa |
| Q8 | Resposta única (cálculo) | A | A (Questão 4) | 9, 8 e 6 faltas; Ótimo = referência teórica, LRU = melhor aproximação |
| Q9 | Afirmativas múltiplas | C | — | I, III e IV |
| Q10 | Associação | D | — | 2 – 1 – 3 (encadeada, contígua, indexada) |
| Q11 | Afirmativas múltiplas | B | — | I, II e IV |
| Q12 | Afirmativa negativa | E | E (Questão 5) | a afirmação errada é a do polling |

> Legenda: ✅ correta · ❌ incorreta · ⚠️ ponto de atenção (gabarito do material duvidoso, ambiguidade, versão divergente)

## Índice
1. [Q1 — Visões do SO e softwares tradutores](#q1--visões-do-so-e-softwares-tradutores)
2. [Q2 — Modo kernel, interrupção, exceção e syscall](#q2--modo-kernel-interrupção-exceção-e-syscall)
3. [Q3 — Sequência de boot](#q3--sequência-de-boot)
4. [Q4 — PCB e troca de contexto](#q4--pcb-e-troca-de-contexto)
5. [Q5 — Exclusão mútua e deadlock](#q5--exclusão-mútua-e-deadlock)
6. [Q6 — Escalonamento SRTF e SLA de espera](#q6--escalonamento-srtf-e-sla-de-espera)
7. [Q7 — Best-fit e fragmentação externa](#q7--best-fit-e-fragmentação-externa)
8. [Q8 — Substituição de páginas FIFO, LRU e Ótimo](#q8--substituição-de-páginas-fifo-lru-e-ótimo)
9. [Q9 — Thrashing, working set, TLB e alocação de quadros](#q9--thrashing-working-set-tlb-e-alocação-de-quadros)
10. [Q10 — Métodos de alocação em disco](#q10--métodos-de-alocação-em-disco)
11. [Q11 — Projeto de armazenamento com journaling](#q11--projeto-de-armazenamento-com-journaling)
12. [Q12 — Técnicas de E/S, spooling, cache e permissões](#q12--técnicas-de-es-spooling-cache-e-permissões)
13. [E1 — Exercício sugerido de first-fit, best-fit e worst-fit](#e1--exercício-sugerido-de-first-fit-best-fit-e-worst-fit)
14. [Apêndice — ENADEs anteriores citados e exemplos numéricos do material](#apêndice--enades-anteriores-citados-e-exemplos-numéricos-do-material)

---

## Q1 — Visões do SO e softwares tradutores
**Fonte:** `SISTEMAS_OPERACIONAIS - GABARITO.pdf`, p. 3 (citada em `MATERIAL_EXPLICATIVO.pdf`, p. 5: "a questão 1 do caderno as cobra em formato de lacunas"). Não aparece nos slides.
**Tipo ENADE:** Lacunas (CAT 1) · Tópico 1 — Visão geral dos SO, máquina de níveis e softwares tradutores

**Enunciado:**
*[Reconstruído — o enunciado original está no caderno de questões, que não foi fornecido. Pelas justificativas do gabarito, o texto tem quatro lacunas, nesta ordem:]*

O sistema operacional pode ser analisado sob duas perspectivas. Como **__(1)__**, ele esconde a complexidade do hardware por trás de abstrações e de uma interface mais simples. Como **__(2)__**, ele arbitra o uso compartilhado de CPU, memória e dispositivos entre programas concorrentes. Na máquina de níveis, os softwares tradutores também se distinguem: o **__(3)__** traduz linguagem simbólica de montagem (mnemônicos) em linguagem de máquina, e o **__(4)__** traduz e executa o código-fonte comando a comando, sem produzir um módulo objeto completo antes da execução.

Assinale a alternativa que preenche corretamente as lacunas.

**Alternativas:** (texto literal do gabarito)
- **A)** gerenciador de recursos / máquina estendida / compilador / montador
- **B)** máquina estendida / gerenciador de recursos / compilador / ligador
- **C)** máquina estendida / gerenciador de recursos / montador / interpretador
- **D)** gerenciador de recursos / máquina estendida / montador / compilador

**Gabarito: C** — _(origem: gabarito do próprio material, p. 2 e p. 3)_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Inverte as duas visões do SO: quem esconde o hardware atrás de abstrações é a máquina estendida, não o gerenciador de recursos. Também troca os tradutores: o compilador traduz linguagem de alto nível, não linguagem de montagem (3ª lacuna), e o montador não executa código-fonte comando a comando (4ª lacuna). Pega quem decorou os termos sem associá-los às definições.
- **B) ❌** — Acerta as duas primeiras lacunas e erra as duas últimas. Quem traduz linguagem de montagem é o montador, não o compilador. O ligador (linker) não traduz nada: só resolve referências entre módulos objeto e bibliotecas e gera o executável.
- **C) ✅** — Máquina estendida (ou máquina virtual, no sentido antigo) = esconder o hardware atrás de uma interface simples; gerenciador de recursos = arbitrar CPU, memória e dispositivos. O montador (assembler) converte mnemônicos em código de máquina, quase uma instrução para uma. O interpretador traduz e executa comando a comando, sem gerar módulo objeto.
- **D) ❌** — Inverte as visões do SO e troca interpretador por compilador na 4ª lacuna. O compilador traduz o programa inteiro para um módulo objeto ANTES da execução. Erro comum: tratar compilador e interpretador como sinônimos porque os dois partem de código de alto nível.

**⚠️ Atenção:** enunciado reconstruído; a ordem e a redação das lacunas na prova podem ser outras. O gabarito fala em "duas funções do SO", mas a apostila (p. 3) insiste que são **duas visões** do mesmo sistema (Tanenbaum), não duas tarefas separadas. Uma versão alterada pode cobrar exatamente isso.

**Conceito-chave para a prova:** máquina estendida = de cima para baixo (abstrações para quem programa); gerenciador de recursos = de baixo para cima (multiplexação no tempo e no espaço). Montador: assembly → máquina. Compilador: alto nível → módulo objeto antes da execução. Interpretador: traduz e executa comando a comando. Ligador: junta módulos (não traduz). Carregador: põe o executável na memória.

---

## Q2 — Modo kernel, interrupção, exceção e syscall
**Fonte:** `Slides.pdf`, p. 11 (enunciado, "QUESTÃO 1 · ENADE") e p. 12 (gabarito); `SISTEMAS_OPERACIONAIS - GABARITO.pdf`, p. 4 (questão 2). Comentada em `MATERIAL_EXPLICATIVO.pdf`, p. 10.
**Tipo ENADE:** Alternativas constantes — V/F (CAT 2) · Tópico 2 — Modos de acesso, interrupções, exceções e chamadas de sistema

**Enunciado:** (literal, slides p. 11)

SITUAÇÃO-PROBLEMA
Uma aplicação de terceiros tentou escrever diretamente no registrador de controle da controladora de disco e foi encerrada pelo sistema operacional com erro de violação de acesso. A equipe revisita então os mecanismos de proteção por modo de acesso.

COMANDO
Analise as afirmações a seguir sobre modo de acesso e transferência de controle ao núcleo, identificando-as como Verdadeiras (V) ou Falsas (F).

( ) A instrução que desabilita interrupções é privilegiada; se um processo em modo usuário tentar executá-la, o hardware gera uma exceção e passa o controle ao núcleo.
( ) A interrupção é um evento síncrono, provocado pela instrução em execução, como uma divisão por zero ou um acesso a endereço inválido.
( ) A chamada de sistema é o mecanismo pelo qual um processo pede um serviço ao núcleo, trocando de modo usuário para modo kernel por meio de um trap.
( ) A API é sinônimo de chamada de sistema, pois toda função de biblioteca corresponde a uma única syscall executada em modo kernel.

Assinale a alternativa com a sequência correta.

**Julgamento das afirmações:**
- **1ª — Verdadeira.** Desabilitar interrupções é instrução privilegiada; em modo usuário o hardware não a executa, gera uma exceção e passa o controle ao núcleo. É o mesmo mecanismo que encerrou a aplicação do incidente.
- **2ª — Falsa.** O texto descreve uma **exceção** (síncrona, causada pela instrução em curso: divisão por zero, endereço inválido). A interrupção é **assíncrona** e vem de um dispositivo externo (disco terminou, temporizador expirou, tecla).
- **3ª — Verdadeira.** É a definição de chamada de sistema: um pedido síncrono e voluntário de serviço ao núcleo, feito por uma instrução de trap que troca para modo kernel.
- **4ª — Falsa.** A API (libc, Win32) roda em modo usuário. Há funções que não geram syscall nenhuma (strlen, sqrt) e outras que geram várias (fopen → open + fstat; printf com buffer pode gerar zero ou vários write).

**Alternativas — versão do caderno (GABARITO.pdf, p. 4):**
- **A)** V – V – F – F
- **B)** F – V – V – V
- **C)** V – F – F – V
- **D)** V – F – V – F

**Alternativas — versão dos slides (p. 11):**
- **A)** V – F – V – F
- **B)** V – V – F – F
- **C)** F – V – V – V
- **D)** V – F – F – V

**Gabarito: D na versão do caderno = A na versão dos slides** (sequência **V – F – V – F**) — _(origem: GABARITO.pdf p. 2 e 4 ("GABARITO: D"); Slides p. 12 ("GABARITO: A"))_

**Por que cada alternativa está certa ou errada** (letras do caderno; entre parênteses, a letra nos slides):
- **A) V–V–F–F ❌** (slides B) — Aceita a 2ª, trocando exceção por interrupção (o erro de terminologia mais comum do tópico), e rejeita a 3ª, que define corretamente a syscall. Pega quem usa "interrupção" para qualquer desvio de fluxo.
- **B) F–V–V–V ❌** (slides C) — Nega a 1ª, que está certa e explica o próprio incidente; aceita a 2ª (troca exceção por interrupção) e a 4ª (confunde API com syscall). Só acerta a 3ª.
- **C) V–F–F–V ❌** (slides D) — Acerta as duas primeiras e inverte as duas últimas: nega a definição correta de syscall e aceita a equivalência API = system call.
- **D) V–F–V–F ✅** (slides A) — É o julgamento acima.

**Diferenças entre versões:**
- **Ordem das alternativas:** a sequência correta é a última (D) no caderno e a primeira (A) nos slides; as outras três mantêm a ordem relativa (V–V–F–F, F–V–V–V, V–F–F–V). A letra do gabarito muda: **D (caderno) × A (slides)**.
- Numeração: questão 2 no caderno, "QUESTÃO 1" nos slides.
- As justificativas do slide são versões resumidas das do gabarito (p. ex., a do F–V–V–V nos slides não diz "acerta apenas a terceira").

**⚠️ Atenção:** só a letra do gabarito diverge; o conteúdo é o mesmo. Na prova, confira a sequência V–F–V–F e não a letra.

**Conceito-chave para a prova:** interrupção = assíncrona, externa (dispositivo/temporizador); exceção/trap = síncrona, involuntária, causada pela instrução (divisão por zero, endereço inválido, instrução privilegiada, falta de página); syscall = síncrona e voluntária, via instrução de trap. API ≠ syscall. Instrução privilegiada em modo usuário → exceção → o núcleo normalmente encerra o processo.

---

## Q3 — Sequência de boot
**Fonte:** `SISTEMAS_OPERACIONAIS - GABARITO.pdf`, p. 5–6 (com figura da sequência correta). Base teórica: `MATERIAL_EXPLICATIVO.pdf`, Apêndice, p. 51–52 ("é exatamente isso que a questão de ordenação cobra"). Não aparece nos slides; o boot ficou fora da apresentação, segundo a apostila (p. 51).
**Tipo ENADE:** Ordenação (CAT 3) · Tópico 3 — Arquiteturas de núcleo, boot, carregadores de kernel e virtualização

**Enunciado:**
*[Reconstruído — o enunciado original não está nos PDFs. Dados tirados da figura e das justificativas do gabarito:]*

Uma analista investiga um servidor que não inicializa. A mensagem na tela mostra que o POST foi concluído, mas o firmware não encontrou um dispositivo inicializável (algo como "nenhum dispositivo inicializável encontrado"). Para localizar a falha, ela precisa ordenar as etapas da inicialização, apresentadas fora de ordem:

1. O **gerenciador de boot** carrega o kernel na memória (ex.: GRUB · Windows Boot Manager).
2. O **firmware** executa o POST e inventaria o hardware (ex.: BIOS · UEFI).
3. O **primeiro processo** de modo usuário sobe os serviços do sistema (ex.: init / systemd, PID 1).
4. O firmware seleciona o **dispositivo de boot**, localiza a unidade e lê o carregador (ex.: MBR · partição EFI).
5. O **kernel** se inicializa, monta a raiz e carrega os drivers (ex.: vmlinuz · ntoskrnl.exe).

Assinale a alternativa que apresenta a ordem correta das etapas.

**Alternativas:** (texto literal do gabarito)
- **A)** 4 – 2 – 1 – 3 – 5
- **B)** 2 – 4 – 1 – 5 – 3
- **C)** 2 – 1 – 4 – 5 – 3
- **D)** 2 – 4 – 5 – 1 – 3

**Gabarito: B** — _(origem: gabarito do próprio material, p. 2 e p. 5)_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Põe a busca pelo dispositivo (4) antes do POST (2): o firmware precisa primeiro testar e inventariar o hardware para saber que unidades existem. Também inverte as duas últimas, pondo o primeiro processo (3) antes da montagem da raiz (5), o que é impossível, porque o init é um executável que mora no sistema de arquivos raiz.
- **B) ✅** — (2) POST do firmware → (4) seleção do dispositivo e leitura do carregador → (1) gerenciador de boot carrega o kernel → (5) kernel se inicializa e monta a raiz → (3) primeiro processo sobe os serviços. A mensagem mostra que a etapa 2 terminou e a falha está na etapa 4: o problema é o dispositivo de boot ou a configuração do firmware, não o kernel.
- **C) ❌** — Põe o gerenciador de boot (1) antes da leitura do dispositivo (4). O gerenciador não roda desde o início: ele é justamente o código que o firmware lê do dispositivo na etapa 4.
- **D) ❌** — Inverte 1 e 5: o kernel se inicializaria antes de ter sido carregado na memória. É o distrator mais sutil, porque acerta o começo e o fim; atrai quem trata "carregador de boot" e "carga do kernel" como um passo só.

**⚠️ Atenção:** enunciado reconstruído; os números atribuídos a cada etapa podem mudar na prova. Guarde a **ordem das funções**, não os números.

**Conceito-chave para a prova:** firmware (BIOS/UEFI) + POST → dispositivo de boot (MBR / partição EFI em GPT) → gerenciador de boot (GRUB) carrega kernel + initramfs → kernel inicializa e monta a raiz (switch_root) → PID 1 (init/systemd) sobe os serviços. "Nenhum dispositivo inicializável" = falha entre o POST e o carregador. O modo kernel só existe a partir da etapa do kernel.

---

## Q4 — PCB e troca de contexto
**Fonte:** `SISTEMAS_OPERACIONAIS - GABARITO.pdf`, p. 7. Citada em `MATERIAL_EXPLICATIVO.pdf`, p. 16 ("a questão sobre o núcleo didático cujos processos 'reiniciam do começo' descreve justamente um sistema que não salva esse contexto"). Não aparece nos slides.
**Tipo ENADE:** Afirmativa incompleta (CAT 1) · Tópico 4 — Processos e threads: PCB, contextos, estados e transições

**Enunciado:**
*[Reconstruído — o enunciado original não está nos PDFs. Pela apostila e pelo gabarito:]*

Em um núcleo didático (simplificado), os processos, ao voltarem a ser escalonados depois de perderem a CPU, **reiniciam do começo** em vez de retomar o ponto em que pararam. Falta a esse núcleo uma estrutura mantida por processo que guarde o contexto de hardware (registradores, PC, ponteiro de pilha, PSW), o contexto de software e o espaço de endereçamento. A peça que falta no núcleo descrito é o(a)...

**Alternativas:** (texto literal do gabarito)
- **A)** Bloco de Controle de Processo (PCB), salvo e restaurado pelo dispatcher a cada troca de contexto.
- **B)** tabela de páginas do processo, mantida pela MMU para traduzir seus endereços lógicos durante a execução.
- **C)** pilha de execução do processo, na qual são alocados os registros de ativação das funções chamadas.
- **D)** vetor de interrupções, consultado pelo processador para localizar a rotina de tratamento do evento ocorrido.

**Gabarito: A** — _(origem: gabarito do próprio material, p. 2 e p. 7)_

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — O PCB (task_struct no Linux, EPROCESS no Windows) representa o processo dentro do núcleo. Guarda o contexto de hardware (registradores, PC, SP, PSW), o contexto de software (PID, prioridade, quotas, limites, estado) e o espaço de endereçamento. É o que o dispatcher salva ao tirar o processo da CPU e restaura ao devolvê-la; sem ele, o processo não tem como retomar do ponto em que parou.
- **B) ❌** — A tabela de páginas também é por processo e também é trocada na troca de contexto, o que a torna plausível. Mas guarda o mapeamento página → quadro, não os registradores: restaurá-la sozinha devolveria a memória, não o ponto de execução (PC).
- **C) ❌** — A pilha guarda endereços de retorno e variáveis locais, o que lembra "retomar de onde parou". Mas isso vale entre chamadas de função dentro do mesmo fluxo; ela não preserva o estado completo do processador entre processos, nem é gerenciada pelo dispatcher.
- **D) ❌** — O vetor de interrupções é consultado no instante da interrupção, daí a associação. Mas é uma estrutura **global** do sistema, não por processo: contém endereços de rotinas de tratamento, não o estado de quem foi interrompido.

**⚠️ Atenção:** enunciado reconstruído; as alternativas são literais.

**Conceito-chave para a prova:** PCB = contexto de hardware + contexto de software + espaço de endereçamento (Machado & Maia). A troca de contexto salva o contexto de hardware no PCB do processo que sai e restaura o do que entra; é puro overhead. Não existe a transição ESPERA → EXECUÇÃO (sempre se passa por PRONTO).

---

## Q5 — Exclusão mútua e deadlock
**Fonte:** `Slides.pdf`, p. 26 (enunciado, "QUESTÃO 2 · ENADE") e p. 27 (gabarito); `SISTEMAS_OPERACIONAIS - GABARITO.pdf`, p. 8–9 (questão 5, com figura do grafo de alocação). Comentada em `MATERIAL_EXPLICATIVO.pdf`, p. 25–26.
**Tipo ENADE:** Asserção-razão (CAT 3) · Tópico 4 — Concorrência, exclusão mútua, semáforos e deadlock

**Enunciado:** (literal, slides p. 26)

SITUAÇÃO-PROBLEMA
Um sistema de reservas protege a agenda de salas com o mutex A e o cadastro de participantes com o mutex B. A rotina de criação adquire A e, ainda de posse dele, pede B; a de cancelamento adquire B e pede A. Todas as regiões críticas estão corretamente delimitadas. Em produção, sob carga, as duas rotinas travam indefinidamente.

COMANDO
Avalie as asserções a seguir e a relação proposta entre elas.

I. O uso correto de semáforos binários (mutexes) em torno de todas as regiões críticas do sistema descrito é suficiente para garantir que ele não entre em deadlock,

PORQUE

II. a exclusão mútua assegurada pelos semáforos impede que dois fluxos acessem simultaneamente a mesma estrutura compartilhada, eliminando as condições de corrida.

A respeito dessas asserções, assinale a opção correta.

[Figura do gabarito, p. 8: grafo de alocação de recursos. T1 detém R1 (mutex A) e espera R2 (mutex B); T2 detém R2 (mutex B) e espera R1 (mutex A). Ciclo fechado T1 → R2 → T2 → R1 → T1 = deadlock. Ao lado, as 4 condições de Coffman: 1) exclusão mútua, 2) posse e espera, 3) não preempção, 4) espera circular.]

**Julgamento:**
- **Asserção I — Falsa.** Exclusão mútua não previne impasse; ela é a **primeira** das quatro condições de Coffman. No cenário as outras três também valem: posse e espera (cada rotina segura um mutex e pede o outro), não preempção e espera circular (A e B adquiridos em ordens opostas). O sistema trava justamente porque os mutexes funcionam.
- **Asserção II — Verdadeira.** Descreve corretamente o papel da exclusão mútua: impedir acesso simultâneo à estrutura compartilhada e, assim, eliminar condições de corrida.
- **Relação:** como I é falsa, não há justificativa a avaliar. Além disso, II trata de outro problema (condição de corrida, não deadlock).

**Alternativas:** (iguais nas duas versões)
- **A)** As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
- **B)** As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
- **C)** A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
- **D)** A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
- **E)** As asserções I e II são proposições falsas.

**Gabarito: D** — _(origem: GABARITO.pdf p. 2 e 9; Slides p. 27)_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Exigiria I verdadeira, o que o próprio cenário desmente (mutexes corretos e mesmo assim trava). É o distrator mais atraente, porque II é verdadeira e parece "explicar" I: a armadilha clássica da asserção-razão.
- **B) ❌** — Também supõe I verdadeira. Pega quem percebeu que exclusão mútua e deadlock são fenômenos distintos, mas não concluiu que I é falsa.
- **C) ❌** — Inverte os valores lógicos: II é a definição correta de exclusão mútua; negá-la é desconhecer a função do semáforo.
- **D) ✅** — I é falsa (exclusão mútua é condição do deadlock, não proteção contra ele); II é verdadeira. A prevenção correta seria impor uma **ordem global de aquisição** (todos pegam A antes de B), quebrando a espera circular.
- **E) ❌** — Nega também II, que está correta. Pega quem, depois de achar o erro de I, passa a desconfiar do próprio semáforo.

**Diferenças entre versões:** enunciado e alternativas iguais; gabarito D nas duas. Os slides chamam de "QUESTÃO 2", o caderno de "questão 5". A figura do gabarito usa os rótulos "detém/espera" e a dos slides (p. 20) "alocado a/requisita". Justificativas dos slides resumidas.

**Conceito-chave para a prova:** condições de Coffman (todas precisam valer juntas): exclusão mútua, posse e espera, não preempção, espera circular. Condição de corrida ≠ deadlock: o semáforo resolve a primeira e, mal usado, causa o segundo. Remédio típico (ENADE 2017): ordem global de aquisição dos locks.

---

## Q6 — Escalonamento SRTF e SLA de espera
**Fonte:** `SISTEMAS_OPERACIONAIS - GABARITO.pdf`, p. 10–11 (com figura de Gantt das quatro políticas). Citada em `MATERIAL_EXPLICATIVO.pdf`, p. 21 ("É o SRTF que gera o diagrama de Gantt da questão 6 do caderno"). Não aparece nos slides.
**Tipo ENADE:** Interpretação (CAT 1), com cálculo · Tópico 5 — Compartilhamento do processador e algoritmos de escalonamento

**Enunciado:**
*[Reconstruído — o enunciado original não está nos PDFs. Os dados abaixo saem com segurança dos cálculos do gabarito, que conferem com a figura:]*

Um serviço tem um requisito (SLA) de **tempo médio de espera ≤ 3,5 ms**. A política atual é **FCFS** (o traço observado é o do FCFS) e não cumpre o requisito. As durações das tarefas são conhecidas. Carga:

| Processo | Chegada (ms) | Duração / burst (ms) |
|---|---|---|
| P1 | 0 | 7 |
| P2 | 2 | 4 |
| P3 | 4 | 1 |
| P4 | 5 | 4 |

(No Round-Robin, o processo que chega entra na fila antes do processo preemptado.)

Comando (reconstruído): qual política de escalonamento atende ao SLA, e com qual tempo médio de espera?

**Alternativas:** (texto literal do gabarito)
- **A)** SJF não preemptivo (Shortest Job First), com tempo médio de espera de 3,0 ms.
- **B)** SRTF (menor tempo restante primeiro), com tempo médio de espera de 3,0 ms.
- **C)** Round-Robin com quantum de 2 ms, com tempo médio de espera de 1,5 ms.
- **D)** Manter o FCFS (4,75 ms), pois políticas preemptivas levariam tarefas longas à inanição.

**Gabarito: B** — _(origem: gabarito do próprio material, p. 2 e p. 10)_

**Cálculos refeitos** (espera = conclusão − chegada − duração):

| Política | Gantt | Esperas P1, P2, P3, P4 | Média | SLA ≤ 3,5? |
|---|---|---|---|---|
| FCFS | P1[0–7] P2[7–11] P3[11–12] P4[12–16] | 0, 5, 7, 7 | 19/4 = **4,75 ms** | não |
| SJF não preemptivo | P1[0–7] P3[7–8] P2[8–12] P4[12–16] | 0, 6, 3, 7 | 16/4 = **4,0 ms** | não |
| SRTF | P1[0–2] P2[2–4] P3[4–5] P2[5–7] P4[7–11] P1[11–16] | 9, 1, 0, 2 | 12/4 = **3,0 ms** | **sim** |
| RR q = 2 (chegada antes do preemptado) | P1[0–2] P2[2–4] P1[4–6] P3[6–7] P2[7–9] P4[9–11] P1[11–13] P4[13–15] P1[15–16] | 9, 3, 2, 6 | 20/4 = **5,0 ms** | não |
| RR q = 2 (preemptado antes da chegada) | P1[0–4] P2[4–6] P1[6–8] P3[8–9] P4[9–11] P2[11–13] P1[13–14] P4[14–16] | 7, 7, 4, 7 | 25/4 = **6,25 ms** | não |

Tempo de **resposta** no RR (convenção do enunciado): 0, 0, 2, 4 → média **1,5 ms**.

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — No SJF **não preemptivo**, P1 começa em t = 0 e vai até t = 7 sem ser interrompido; a média é **4,0 ms** (o empate P2/P4 em t = 8 não altera a média). Os 3,0 ms só aparecem se P2 e P3 interromperem P1, ou seja, simulando SRTF sem perceber. Pega a confusão entre as versões preemptiva e não preemptiva do SJF.
- **B) ✅** — Em t = 2, P2 (4 ms) preempta P1 (5 ms restantes); em t = 4, P3 (1 ms) preempta P2 (2 restantes); em t = 5, P4 (4) não preempta P2 (2 restantes); em t = 7, P4 (4) vence P1 (5). Esperas 9, 1, 0, 2 → (9 + 1 + 0 + 2)/4 = 3,0 ms ≤ 3,5 ms. O SRTF minimiza a espera média quando as durações são conhecidas (premissa do enunciado).
- **C) ❌** — A espera média real do RR q = 2 é **5,0 ms** (6,25 ms na convenção inversa da fila): viola o SLA. Os **1,5 ms** são a média do tempo de **resposta** (até a 1ª execução: 0, 0, 2, 4). Pega quem confunde resposta com espera, justamente o critério em que o RR se destaca.
- **D) ❌** — O FCFS dá de fato 4,75 ms (esperas 0, 5, 7, 7), acima do limite: mantê-lo descumpre o SLA. A preocupação com inanição é legítima no SRTF com chegada contínua de tarefas curtas, mas se trata com envelhecimento (aging); nesta carga P1 termina em t = 16, sem inanição.

**⚠️ Atenção:** enunciado reconstruído. No RR, a média depende da convenção da fila quando chegada e preempção coincidem (5,0 ou 6,25 ms); as duas violam o SLA, então a resposta não muda. Numa versão alterada (outros bursts ou chegadas), **refaça o Gantt reavaliando a fila a cada chegada**: o erro mais comum, segundo a apostila (p. 28), é aplicar a política uma vez só, o que transforma SRTF em SJF não preemptivo.

**Conceito-chave para a prova:** turnaround = conclusão − chegada; espera = turnaround − duração; resposta = 1ª execução − chegada. SRTF (preemptivo) minimiza a espera média; SJF não preemptivo só é ótimo com chegadas simultâneas; RR otimiza o tempo de resposta, não a espera; FCFS sofre efeito comboio.

---

## Q7 — Best-fit e fragmentação externa
**Fonte:** `Slides.pdf`, p. 33 (enunciado, "QUESTÃO 3 · ENADE"), p. 34 (gabarito) e p. 35 (resolução passo a passo); `SISTEMAS_OPERACIONAIS - GABARITO.pdf`, p. 12–13 (questão 7, com figura). Citada em `MATERIAL_EXPLICATIVO.pdf`, p. 32.
**Tipo ENADE:** Resposta única (CAT 1) · Tópico 6 — Memória principal: alocação contígua, particionamento e fragmentação

**Enunciado:** (literal, slides p. 33)

SITUAÇÃO-PROBLEMA
Um sistema embarcado usa partições variáveis com alocação contígua. O mapa de áreas livres apresenta, em ordem crescente de endereço, blocos de 100 KB, 500 KB, 200 KB, 300 KB e 600 KB. Chega a requisição de um processo que precisa de 212 KB contíguos.

COMANDO
Considerando o funcionamento das estratégias de alocação e os tipos de fragmentação, assinale a alternativa que indica corretamente a área escolhida pela estratégia best-fit e o tipo de fragmentação característico desse esquema de gerenciamento.

[Figura (gabarito p. 12 / slides p. 35): áreas livres, em ordem de endereço, separadas por blocos ocupados: 100 KB | 500 KB | 200 KB | 300 KB | 600 KB. Pedido de 212 KB. first-fit → 500 KB (resto 288 KB); best-fit → 300 KB (resto 88 KB); worst-fit → 600 KB (resto 388 KB).]

**Alternativas — versão dos slides (p. 33):**
- **A)** A área de 500 KB; a fragmentação característica é a interna, pois sobra espaço não utilizado dentro da partição alocada ao processo.
- **B)** A área de 300 KB; a fragmentação característica é a externa, pois restam lacunas livres pequenas e dispersas, incapazes de atender a novos pedidos.
- **C)** A área de 300 KB; a fragmentação característica é a interna, pois a partição tem tamanho predefinido e sempre maior que o do processo.
- **D)** A área de 600 KB; a fragmentação característica é a externa, pois a maior lacuna disponível é subdividida a cada nova alocação realizada.

**Alternativas — versão do caderno (GABARITO.pdf, p. 12–13):**
- **A)** A área de 500 KB; a fragmentação característica é a interna, pois sobra espaço não utilizado dentro da partição alocada ao processo.
- **B)** A área de 300 KB; a fragmentação característica é a interna, pois a partição tem tamanho predefinido, superior ao exigido pelo processo.
- **C)** A área de 300 KB; a fragmentação característica é a externa, pois restam lacunas livres pequenas e dispersas, incapazes de atender a novos pedidos.
- **D)** A área de 600 KB; a fragmentação característica é a externa, pois a maior lacuna disponível é subdividida a cada nova alocação realizada.

**Gabarito: C na versão do caderno = B na versão dos slides** (300 KB + fragmentação **externa**) — _(origem: GABARITO.pdf p. 2 e 13 ("GABARITO: C"); Slides p. 34 ("GABARITO: B"))_

**Por que cada alternativa está certa ou errada** (descrição pelo conteúdo, que vale para as duas versões):
- **500 KB / interna ❌** (A nas duas) — 500 KB é a resposta do **first-fit** (a primeira que cabe). E fragmentação interna é característica de partições **fixas**.
- **300 KB / interna ❌** (C nos slides, B no caderno) — Acerta a área do best-fit e erra o tipo de fragmentação. Em partições variáveis, a partição nasce com o tamanho exato do processo; não existe "tamanho predefinido maior", e o desperdício fica FORA das partições. É o distrator mais próximo do gabarito.
- **300 KB / externa ✅** (B nos slides, C no caderno) — O best-fit varre todas as áreas e escolhe a MENOR que comporta o pedido: entre 500, 300 e 600 KB (as que cabem 212 KB), a menor é 300 KB, com resto de 88 KB. Em alocação contígua com partições variáveis, o desperdício são lacunas livres pequenas e dispersas = fragmentação **externa**.
- **600 KB / externa ❌** (D nas duas) — 600 KB é a resposta do **worst-fit** (a maior de todas). O tipo de fragmentação está certo, o que aumenta a plausibilidade, mas a estratégia não é a pedida.

**Diferenças entre versões:**
- **B e C trocam de lugar**, e a letra do gabarito muda: **B (slides) × C (caderno)**.
- Redação da alternativa "300 KB / interna": slides "pois a partição tem tamanho predefinido **e sempre maior que o do processo**"; caderno "pois a partição tem tamanho predefinido, **superior ao exigido pelo processo**".
- Slides chamam de "QUESTÃO 3", o caderno de "questão 7". O slide p. 35 mostra os restos (288/88/388 KB) e sugere treinar o mesmo mapa com pedidos de 417, 112 e 426 KB (ver E1).

**⚠️ Atenção:** a letra correta depende da versão; memorize "300 KB + externa".

**Conceito-chave para a prova:** first-fit = primeira que cabe (mais rápida); best-fit = menor que cabe (menor resto, mas espalha lacunas minúsculas); worst-fit = maior de todas. Fragmentação interna = DENTRO da área alocada (partições fixas, última página na paginação); externa = FORA, em lacunas dispersas (partições variáveis, segmentação). Compactação resolve a externa, mas exige relocação dinâmica.

---

## Q8 — Substituição de páginas FIFO, LRU e Ótimo
**Fonte:** `Slides.pdf`, p. 42 (enunciado, "QUESTÃO 4 · ENADE"), p. 43 (gabarito) e p. 44 (simulação quadro a quadro); `SISTEMAS_OPERACIONAIS - GABARITO.pdf`, p. 14–15 (questão 8, com figura FIFO/LRU).
**Tipo ENADE:** Resposta única com cálculo aplicado (CAT 1) · Tópico 7 — Memória virtual: políticas de substituição de páginas

**Enunciado:** (literal, slides p. 42)

SITUAÇÃO-PROBLEMA
A arquiteta de um sistema operacional para dispositivos de borda precisa escolher a política de substituição de páginas. Para fundamentar a decisão, simula três algoritmos sobre a mesma carga, com três quadros e memória inicialmente vazia.

DADOS DE SUPORTE
Cadeia de referências a páginas utilizada na simulação:
7 · 0 · 1 · 2 · 0 · 3 · 0 · 4 · 2 · 3
Número de quadros disponíveis: 3. Memória inicialmente vazia (todas as faltas iniciais devem ser contabilizadas).

COMANDO
Ao simular os algoritmos FIFO, LRU e Ótimo sobre a cadeia de referências apresentada, qual é o número de faltas de página produzido por cada um deles, respectivamente, e qual conclusão de projeto se sustenta a partir do resultado?

**Alternativas — versão dos slides (p. 42):**
- **A)** 9, 8 e 6 faltas; o algoritmo Ótimo serve apenas como referência teórica de desempenho, e o LRU é a política implementável mais próxima dele.
- **B)** 9, 9 e 6 faltas; FIFO e LRU produzem o mesmo resultado nesta cadeia, e a escolha entre eles deve recair sobre o de menor custo de implementação.
- **C)** 9, 8 e 7 faltas; o Ótimo não elimina as faltas de partida a frio e, por isso, fica apenas uma falta abaixo do LRU nesta simulação.
- **D)** 10, 8 e 6 faltas; o FIFO penaliza as páginas mais antigas mesmo quando reutilizadas, gerando uma falta a mais que o LRU nas referências repetidas.

**Alternativas — versão do caderno (GABARITO.pdf, p. 14–15):**
- **A)** 9, 8 e 6 faltas; o algoritmo Ótimo serve apenas como referência teórica de desempenho, e o LRU é a política implementável mais próxima dele.
- **B)** 9, 9 e 8 faltas; FIFO e LRU têm desempenho equivalente nessa carga, de modo que a escolha entre eles deve considerar apenas o custo de implementação.
- **C)** 6, 5 e 3 faltas; como as primeiras cargas ocorrem em memória vazia, elas não configuram falta de página e não entram na contagem.
- **D)** 15, 13 e 9 faltas; toda referência a uma página que provoque substituição gera duas faltas, uma na retirada e outra na carga da nova página.

**Gabarito: A** (nas duas versões) — _(origem: GABARITO.pdf p. 2 e 14; Slides p. 43)_

**Simulação quadro a quadro** (conferida em Python; igual às figuras do gabarito p. 14 e do slide p. 44; F = falta, · = acerto):

| Ref. | 7 | 0 | 1 | 2 | 0 | 3 | 0 | 4 | 2 | 3 | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FIFO quadros | 7 | 7,0 | 7,0,1 | 2,0,1 | 2,0,1 | 2,3,1 | 2,3,0 | 4,3,0 | 4,2,0 | 4,2,3 | |
| FIFO | F | F | F | F | · | F | F | F | F | F | **9** |
| LRU quadros | 7 | 7,0 | 7,0,1 | 2,0,1 | 2,0,1 | 2,0,3 | 2,0,3 | 4,0,3 | 4,0,2 | 4,3,2 | |
| LRU | F | F | F | F | · | F | · | F | F | F | **8** |
| Ótimo quadros | 7 | 7,0 | 7,0,1 | 2,0,1 | 2,0,1 | 2,0,3 | 2,0,3 | 2,4,3 | 2,4,3 | 2,4,3 | |
| Ótimo | F | F | F | F | · | F | · | F | · | · | **6** |

Vítimas decisivas: na 6ª referência (página 3), o FIFO tira a 0 (a mais antiga), o LRU tira a 1 (a menos recentemente usada) e o Ótimo tira a 1 (nunca mais usada). Na 8ª referência (página 4), o Ótimo tira a 0 (nunca mais usada) e ganha os acertos em 2 e 3.

**Por que cada alternativa está certa ou errada:**
- **A) ✅** (nas duas versões) — 9 (FIFO: só o 0 da 5ª posição é acerto), 8 (LRU: acertos nos 0 da 5ª e da 7ª) e 6 (Ótimo: acertos em 0, 0, 2 e 3). A conclusão também está certa: o Ótimo exige conhecer o futuro, então é limite inferior teórico; o LRU o aproxima usando o passado recente.
- **B, slides (9, 9 e 6) ❌** — Trata o LRU como FIFO. Na 6ª referência o LRU expulsa a 1, não a 0, e por isso acerta na 7ª. Quem "empata" os dois não simulou.
- **B, caderno (9, 9 e 8) ❌** — O LRU dá 8 (não 9) e o Ótimo dá 6 (não 8). A conclusão também falha: além de não haver empate, o FIFO sofre a anomalia de Belady e o LRU (algoritmo de pilha) não, então o custo de implementação não é o único critério.
- **C, slides (9, 8 e 7) ❌** — Ótimo mal simulado: expulsar a 2 (em vez da 1, que nunca mais aparece) na 6ª referência gera uma falta extra na 9ª. O Ótimo nunca perde para o LRU. A primeira parte da frase ("não elimina as faltas de partida a frio") é verdadeira, mas o número está errado.
- **C, caderno (6, 5 e 3) ❌** — Não conta as 3 faltas compulsórias (memória vazia), que são faltas legítimas e que o enunciado manda contar: 9 − 3, 8 − 3, 6 − 3.
- **D, slides (10, 8 e 6) ❌** — Conta a 5ª referência (página 0, já residente) como falta do FIFO. Acerto não gera substituição: é erro de contagem.
- **D, caderno (15, 13 e 9) ❌** — Conta duas faltas por substituição. Uma substituição é **um** evento de falta (retira a vítima e carrega a nova no mesmo tratamento): 3 + 2×6 = 15, 3 + 2×5 = 13, 3 + 2×3 = 9.

**Diferenças entre versões:**
- **A** (correta) é idêntica nas duas.
- **B:** slides "9, 9 e **6**; FIFO e LRU produzem o mesmo resultado nesta cadeia, e a escolha entre eles deve recair sobre o de menor custo de implementação" × caderno "9, 9 e **8**; FIFO e LRU têm desempenho equivalente nessa carga, de modo que a escolha entre eles deve considerar apenas o custo de implementação".
- **C:** slides "9, 8 e 7" (Ótimo mal simulado) × caderno "6, 5 e 3" (sem as faltas compulsórias).
- **D:** slides "10, 8 e 6" (acerto contado como falta) × caderno "15, 13 e 9" (duas faltas por substituição).
- Slides chamam de "QUESTÃO 4", o caderno de "questão 8". O slide p. 44 traz a tabela do Ótimo; a figura do gabarito só traz FIFO e LRU e dá o total do Ótimo (6).

**⚠️ Atenção:** a resposta é A nas duas versões, mas os distratores mudam; a prova pode trazer qualquer combinação deles. Se a cadeia ou o número de quadros mudar, simule de novo (empate de vítima no Ótimo não altera o total).

**Conceito-chave para a prova:** faltas compulsórias contam; substituição = 1 falta; FIFO tira a mais antiga e sofre anomalia de Belady (1-2-3-4-1-2-5-1-2-3-4-5: 9 faltas com 3 quadros, 10 com 4 — conferido); LRU tira a menos recentemente usada, é de pilha (sem Belady) e precisa de apoio de hardware; Ótimo tira a usada mais tarde ou nunca, não é implementável e serve de referência.

---

## Q9 — Thrashing, working set, TLB e alocação de quadros
**Fonte:** `SISTEMAS_OPERACIONAIS - GABARITO.pdf`, p. 16–17 (com figura da curva de Denning). Citada em `MATERIAL_EXPLICATIVO.pdf`, p. 41 ("a armadilha que a questão 9 do caderno explora"). Não aparece nos slides.
**Tipo ENADE:** Afirmativas múltiplas (CAT 2) · Tópico 7 — Working set, TLB, thrashing e políticas de alocação de quadros

**Enunciado:**
*[Reconstruído — o enunciado e as afirmativas originais não estão nos PDFs. Pelas justificativas do gabarito:]*

Um servidor apresenta **utilização de CPU baixa, disco saturado e taxa de faltas de página elevada**. A equipe avalia as afirmativas a seguir.

I. O quadro caracteriza **thrashing**: a soma dos working sets dos processos residentes excede o número de quadros disponíveis, e os processos passam mais tempo esperando páginas do que executando.
II. Como a CPU está ociosa, a medida corretiva adequada é **aumentar o grau de multiprogramação**, admitindo mais processos para ocupar o processador.
III. A **TLB** é uma cache associativa das traduções página → quadro; num acerto, o quadro é obtido sem o acesso extra à tabela de páginas na memória.
IV. Na alocação **global**, um processo pode tomar quadros de outros processos (o que adapta melhor o sistema, mas faz o desempenho de cada um depender do comportamento dos demais e reduz a previsibilidade); na alocação **local**, o processo só substitui páginas próprias.

É correto o que se afirma em

[Figura do gabarito, p. 16: utilização da CPU × grau de multiprogramação. A curva sobe ("cada processo ainda tem quadros suficientes") até o "ponto de virada" e depois despenca (THRASHING: "o working set não cabe — mais paginação que trabalho útil").]

**Julgamento das afirmativas:**
- **I — Verdadeira.** CPU baixa + disco saturado + faltas em alta é o retrato do thrashing; o critério é o working set não caber nos quadros.
- **II — Falsa.** É a medida que **agrava** o problema: mais processos significa menos quadros por processo, mais faltas e mais colapso (o ciclo vicioso do escalonador de longo prazo que, vendo a CPU ociosa, admite mais processos). O certo é **reduzir** o grau de multiprogramação, suspendendo processos.
- **III — Verdadeira.** Definição correta de TLB e do efeito do acerto.
- **IV — Verdadeira.** Distingue corretamente alocação global e local, inclusive o efeito colateral da global sobre a previsibilidade.

**Alternativas:** (texto literal do gabarito)
- **A)** I e II.
- **B)** II e III.
- **C)** I, III e IV.
- **D)** I, II e IV.

**Gabarito: C** — _(origem: gabarito do próprio material, p. 2 e p. 16)_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Aceita II, justamente a intervenção que aprofunda o colapso.
- **B) ❌** — Aceita II e rejeita I (o diagnóstico correto) e IV. Pega quem sabe TLB mas não liga os três indicadores ao thrashing.
- **C) ✅** — I, III e IV corretas; II é a única falsa.
- **D) ❌** — Acerta I e IV, mas inclui II. É o distrator mais próximo: atrai quem identificou o fenômeno e raciocinou só em "manter a CPU ocupada".

**⚠️ Atenção:** enunciado e afirmativas reconstruídos; o conteúdo de cada afirmativa sai das justificativas do gabarito, a redação literal não. Pode haver detalhes (números de CPU, disco ou faltas) que não aparecem aqui.

**Conceito-chave para a prova:** thrashing = CPU baixa + disco saturado + faltas altas → **reduzir** a multiprogramação (suspender processos); prevenção por modelo de working set ou PFF (frequência de faltas). TLB: TEA = h·(ε + t) + (1 − h)·(ε + 2t). Alocação local isola o processo; a global adapta melhor, mas contamina.

---

## Q10 — Métodos de alocação em disco
**Fonte:** `SISTEMAS_OPERACIONAIS - GABARITO.pdf`, p. 18 (com figura). Ver `MATERIAL_EXPLICATIVO.pdf`, p. 45–46 (palavras-chave para "questão de associação"). Não aparece nos slides como questão (só a figura no slide p. 47).
**Tipo ENADE:** Associação de colunas (CAT 2) · Tópico 8 — Sistemas de arquivos: métodos de alocação em disco

**Enunciado:**
*[Reconstruído — o enunciado original não está nos PDFs. Estrutura deduzida das justificativas:]*

Relacione os métodos de alocação de arquivos em disco às respectivas características.

Coluna 1 — Métodos:
1. Alocação contígua
2. Alocação encadeada
3. Alocação indexada

Coluna 2 — Características (na ordem do enunciado):
( ) Cada bloco guarda um ponteiro para o bloco seguinte; não há fragmentação externa, mas o acesso direto é ruim (é preciso percorrer a cadeia).
( ) Os blocos do arquivo são sequenciais no disco; ótimo desempenho na leitura sequencial, acesso direto por cálculo (bloco = início + i), mas sujeita a fragmentação externa.
( ) Um bloco de índice reúne os ponteiros para todos os blocos do arquivo; acesso direto eficiente, ao custo do espaço do índice.

Assinale a sequência correta.

[Figura do gabarito, p. 18: o mesmo arquivo de 4 blocos num disco de 20 blocos (0–19). Contígua: blocos 6, 7, 8, 9 — "diretório: início = 6, tamanho = 4 · acesso direto: bloco = 6 + i · sofre fragmentação externa". Encadeada: blocos 2 → 8 → 15 → 18 — "diretório: início = 2, fim = 18 · acesso direto exige percorrer a cadeia". Indexada: bloco de índice 5 → {2, 8, 15, 18} — "acesso direto eficiente · custa espaço para o índice".]

**Alternativas:** (texto literal do gabarito)
- **A)** 1 – 2 – 3
- **B)** 3 – 1 – 2
- **C)** 2 – 3 – 1
- **D)** 2 – 1 – 3

**Gabarito: D** — _(origem: gabarito do próprio material, p. 2 e p. 18)_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Troca as duas primeiras: atribui à contígua o encadeamento por ponteiros, o que contradiz a contiguidade (o próximo bloco sai por cálculo, não precisa ser armazenado).
- **B) ❌** — Associa a 1ª característica à indexada e a 3ª à encadeada. É plausível porque as duas usam ponteiros; a diferença é onde eles ficam: espalhados nos blocos (encadeada) ou centralizados num bloco de índice (indexada).
- **C) ❌** — Acerta a 1ª e inverte as duas últimas: dá à contígua o bloco de índice e à indexada a contiguidade física. Pega quem não distingue "endereço calculado" de "endereço tabelado".
- **D) ✅** — 1ª (ponteiro em cada bloco) = **encadeada (2)**; 2ª (blocos sequenciais, cálculo, fragmentação externa) = **contígua (1)**; 3ª (bloco de índice) = **indexada (3)**.

**⚠️ Atenção:** enunciado reconstruído; na prova a ordem das características (e, portanto, a sequência correta) pode mudar. Associe pelas palavras-chave.

**Conceito-chave para a prova:** "ponteiro em cada bloco" = encadeada (FAT = encadeada com tabela à parte); "blocos sequenciais / cálculo / fragmentação externa" = contígua; "bloco de índice / tabela de ponteiros" = indexada (inode com ponteiros diretos e indiretos; ext4 usa extents). Acesso sequencial e crescimento → encadeada; acesso aleatório → indexada; arquivos que não mudam → contígua.

---

## Q11 — Projeto de armazenamento com journaling
**Fonte:** `SISTEMAS_OPERACIONAIS - GABARITO.pdf`, p. 19. Base teórica em `MATERIAL_EXPLICATIVO.pdf`, p. 46–47 e slide p. 48. Não aparece nos slides como questão.
**Tipo ENADE:** Afirmativas múltiplas (CAT 2), propostas de projeto · Tópico 8 — Projeto de solução de armazenamento, journaling e espaços livres

**Enunciado:**
*[Reconstruído — o enunciado e as propostas originais não estão nos PDFs. Pelas justificativas do gabarito:]*

Uma equipe projeta o armazenamento de **exames de 2 GB a 40 GB**, lidos por regiões arbitrárias (**acesso aleatório**), com requisito de **integridade dos dados e metadados após falha** (queda de energia). São avaliadas as propostas:

I. Usar um sistema de arquivos com **journaling** (como ext4 ou XFS), que registra as operações num diário antes de aplicá-las; após uma falha, basta reaplicar ou descartar as transações incompletas, sem varrer o volume inteiro, o que encurta a recuperação.
II. Adotar **alocação indexada**, adequada ao padrão de acesso aleatório descrito.
III. Adotar **FAT32**, cuja tabela de alocação centralizada ofereceria garantias de integridade equivalentes às de um diário de transações (journaling).
IV. Gerenciar os espaços livres com **mapa de bits**, que permite varrer sequências de bits livres e achar regiões contíguas com facilidade, vantagem que a lista encadeada de blocos livres não oferece.

Devem compor a solução as propostas

**Julgamento das propostas:**
- **I — Correta.** Descreve bem o journaling e o ganho de tempo na recuperação, atendendo ao requisito de integridade.
- **II — Correta.** O acesso aleatório exige localizar qualquer bloco diretamente: alocação indexada (inodes/extents).
- **III — Incorreta.** Dois erros graves: o FAT32 **não tem journaling**, e seu limite de **4 GB por arquivo** inviabiliza exames de 2 a 40 GB.
- **IV — Correta.** Mapa de bits = um bit por bloco, fácil achar sequências contíguas livres.

**Alternativas:** (texto literal do gabarito)
- **A)** I e III.
- **B)** I, II e IV.
- **C)** II e III.
- **D)** I, III e IV.

**Gabarito: B** — _(origem: gabarito do próprio material, p. 2 e p. 19)_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Aceita III (FAT32 sem journaling e limitado a 4 GB) e descarta II e IV, que são corretas.
- **B) ✅** — I, II e IV atendem a integridade, acesso aleatório e gestão de espaço livre; III é a única que não deve entrar.
- **C) ❌** — Inclui III e rejeita I, a solução direta para a integridade. Pega quem pensa só no padrão de acesso e esquece a consistência dos metadados após falha.
- **D) ❌** — O distrator mais atraente: junta duas corretas (I e IV) com a incorreta (III) e exclui II. Atrai quem associa a "tabela de alocação" do FAT a uma "estrutura centralizada de índice" com as mesmas garantias de um diário.

**⚠️ Atenção:** enunciado e propostas reconstruídos; a redação literal pode ser outra. Em versões alteradas, procure as palavras-chave: "queda de energia / integridade" → journaling; "arquivos > 4 GB" → FAT32 eliminado; "acesso aleatório" → indexada; "achar blocos contíguos livres" → mapa de bits.

**Conceito-chave para a prova:** journaling grava a operação no diário ANTES de aplicá-la; recuperação lê só o diário (redo/descartar). ext4 (modos data=ordered padrão, data=journal, data=writeback) e XFS (arquivos muito grandes) têm journaling; NTFS também (com ACL); FAT32 não tem journaling nem permissões e limita arquivos a 4 GB.

---

## Q12 — Técnicas de E/S, spooling, cache e permissões
**Fonte:** `Slides.pdf`, p. 51 (enunciado, "QUESTÃO 5 · ENADE") e p. 52 (gabarito); `SISTEMAS_OPERACIONAIS - GABARITO.pdf`, p. 20–21 (questão 12, com figura). Citada em `MATERIAL_EXPLICATIVO.pdf`, p. 48 ("a de afirmativa negativa do caderno").
**Tipo ENADE:** Afirmativa negativa — assinale a INCORRETA (CAT 1) · Tópico 9 — Gerência de E/S, DMA, spooling, cache e proteção de recursos

**Enunciado:** (literal, slides p. 51)

SITUAÇÃO-PROBLEMA
Ao revisar a configuração de um servidor que acumula as funções de arquivo e de impressão, um administrador redige as premissas que orientaram suas decisões sobre o subsistema de entrada e saída. A equipe de arquitetura precisa identificar premissas equivocadas antes de aprovar o documento.

COMANDO
Considerando o funcionamento do subsistema de entrada e saída e os mecanismos de proteção de recursos, assinale a alternativa que apresenta uma afirmação INCORRETA.

**Alternativas:** (iguais nas duas versões)
- **A)** Na E/S por acesso direto à memória (DMA), o controlador transfere blocos inteiros entre o dispositivo e a memória principal e interrompe o processador apenas ao final da transferência, reduzindo a sobrecarga da CPU em relação à E/S por interrupção.
- **B)** O spooling desacopla a aplicação do dispositivo ao gravar a saída em uma área intermediária em disco, permitindo que vários processos submetam trabalhos simultaneamente enquanto um processo servidor os envia à impressora, um de cada vez.
- **C)** O buffer cache mantém em memória principal blocos de disco recentemente acessados e aproveita o princípio da localidade de referência para reduzir o número de acessos físicos ao dispositivo.
- **D)** Em sistemas Linux, as permissões de leitura, escrita e execução aplicadas ao proprietário, ao grupo e aos demais usuários são verificadas pelo núcleo, e o bit de execução em um diretório controla a possibilidade de atravessá-lo para alcançar seu conteúdo.
- **E)** Na E/S programada por polling, o processador delega ao controlador o controle completo da transferência e permanece livre para executar outros processos, sendo por isso a técnica mais eficiente para dispositivos de alta taxa de transferência.

[Figura do gabarito, p. 20: três caixas. E/S PROGRAMADA (polling) — "a CPU fica 100% presa durante toda a transferência": a CPU escreve o comando e fica em espera ocupada, testando o registrador de status em laço, e transfere byte a byte, ela mesma. E/S POR INTERRUPÇÃO — "libera a CPU entre os eventos, mas uma interrupção por byte": a CPU dispara a operação e vai executar outro processo; o controlador interrompe a cada byte/palavra pronta; a CPU move o dado do controlador para a memória. E/S POR DMA — "menor sobrecarga — indispensável em disco e rede": a CPU programa o controlador de DMA (endereço, contagem); o DMA transfere o bloco INTEIRO direto para a memória; só ao final gera UMA interrupção.]

**Gabarito: E** (nas duas versões) — _(origem: GABARITO.pdf p. 2 e 21; Slides p. 52)_

**Por que cada alternativa está certa ou errada** (o comando pede a INCORRETA):
- **A) ❌ (afirmação correta, não é a resposta)** — Definição exata do DMA: uma interrupção por bloco, em vez de uma por byte/palavra.
- **B) ❌ (afirmação correta)** — Descreve fielmente o spooling: fila em disco que torna um dispositivo dedicado (impressora) utilizável de forma concorrente; um daemon envia um trabalho por vez.
- **C) ❌ (afirmação correta)** — Buffer cache de disco, fundamentado na localidade de referência.
- **D) ❌ (afirmação correta)** — O núcleo verifica as permissões rwx (dono/grupo/outros); em diretório, x = atravessar e r = listar.
- **E) ✅ (é a afirmação INCORRETA → gabarito)** — O polling faz o oposto: a CPU fica em **espera ocupada**, testando o registrador de status em laço e movendo os dados ela mesma, byte a byte. É a técnica de MAIOR sobrecarga de CPU e a menos indicada para dispositivos rápidos. O texto descreve, na verdade, o DMA.

**Diferenças entre versões:** enunciado e alternativas iguais; gabarito E nas duas. Slides "QUESTÃO 5", caderno "questão 12". As justificativas do gabarito trazem "CORRETA (e por isso não é a resposta)" para A–D; as dos slides são resumidas.

**Conceito-chave para a prova:** polling = CPU presa 100% (espera ocupada); por interrupção = CPU livre entre eventos, uma interrupção por byte/palavra; DMA = bloco inteiro e UMA interrupção no fim (menor sobrecarga). Buffering = cópia em trânsito; caching = cópia extra para reuso; spooling = fila em disco para dispositivo dedicado. chmod 754 = rwxr-xr--.

---

## E1 — Exercício sugerido de first-fit, best-fit e worst-fit
**Fonte:** `Slides.pdf`, p. 35 (nota de rodapé da resolução da Questão 3: "o mesmo mapa é o exercício clássico de Silberschatz (100, 500, 200, 300, 600 KB) — treinem também com pedidos de 417, 112 e 426 KB").
**Tipo ENADE:** Exercício aberto (sem alternativas), cálculo

**Enunciado:** Com o mesmo mapa de áreas livres da Q7 (100 KB, 500 KB, 200 KB, 300 KB e 600 KB, em ordem de endereço), aplique first-fit, best-fit e worst-fit também aos pedidos de 417 KB, 112 KB e 426 KB.

**Resposta esperada:** _(não consta no material; resolvido aqui e conferido em Python)_

*Leitura clássica de Silberschatz: pedidos em sequência 212 → 417 → 112 → 426 KB, cada um consumindo a lacuna escolhida.*

| Pedido | First-fit | Best-fit | Worst-fit |
|---|---|---|---|
| 212 KB | 500 → resto 288 | 300 → resto 88 | 600 → resto 388 |
| 417 KB | 600 → resto 183 | 500 → resto 83 | 500 → resto 83 |
| 112 KB | 288 → resto 176 | 200 → resto 88 | 388 → resto 276 |
| 426 KB | **não é atendido** (lacunas 100, 176, 200, 300, 183) | 600 → resto 174 | **não é atendido** (lacunas 100, 83, 200, 300, 276) |

Conclusão: nesse exemplo, só o **best-fit** atende os quatro pedidos.

*Leitura alternativa (cada pedido isolado, sobre o mapa original):* 417 KB → first 500, best 500, worst 600; 112 KB → first 500, best 200, worst 600; 426 KB → first 500, best 500, worst 600.

**Conceito-chave para a prova:** aplique a estratégia a cada pedido sobre o mapa **atualizado**; nenhuma das três elimina a fragmentação externa, só a administra.

---

## Apêndice — ENADEs anteriores citados e exemplos numéricos do material

*(Isto não são questões do squad. O material só cita esses ENADEs, sem reproduzir os enunciados; os números abaixo são exemplos resolvidos na apostila e nos slides, todos conferidos.)*

**ENADEs anteriores citados (sem enunciado no material):**
- **ENADE 2017:** FIFO × LRU em asserção-razão / anomalia de Belady (cadeia 1-2-3-4-1-2-5-1-2-3-4-5: FIFO 9 faltas com 3 quadros, 10 com 4, conferido) e deadlock com dois mutexes em ordens opostas (resposta: ordem global de aquisição).
- **ENADE 2021:** algoritmo × ambiente (resposta "escalonamento por prioridades → sistemas interativos"; distratores "FILO para tempo real", "RMS para lote", "SJF para interativo", "RR para tempo real") e asserção-razão sobre desabilitar interrupções (só o kernel pode, e só funciona em monoprocessador).
- **ENADE 2005 e 2014:** produtor–consumidor com semáforos (mutex = 1, vazio = N, cheio = 0; inverter down(mutex) e down(vazio) causa deadlock).
- **ENADE 2008, 2011 e 2014:** threads (compartilham código, dados e arquivos; PC, registradores e pilha próprios; multithread num núcleo é concorrência, não paralelismo).
- **ENADE 2008 (discursiva):** inversão de prioridade em tempo real, resolvida por herança de prioridade. **ENADE 2005:** SJF não é o escalonador típico de tempo real; espaço virtual pode ser maior que a memória física. **ENADE 2014:** tradução de endereço com quadros de 1 KB e bit de validade.

**Exemplos numéricos do material (conferidos):**
- Escalonamento (Silberschatz; P1 = 24, P2 = 3, P3 = 3 ms, todos em t = 0): FCFS espera média 17 ms / turnaround 27 ms; SJF 3 / 13 ms; RR q = 4: 5,67 ≈ 5,7 / 15,67 ≈ 15,7 ms.
- TLB: 90 % de acerto, TLB 10 ns, memória 100 ns → 0,9·110 + 0,1·210 = **120 ns** (200 ns sem TLB); 98 % e 100 ns (TLB desprezível) → ≈ 102 ns.
- Base/limite: lógico 1250 < limite 4000 → físico 14000 + 1250 = **15250**; lógico 4500 ≥ 4000 → trap.
- Paginação: endereço de 32 bits e página de 4 KB → 12 bits de deslocamento e 20 de página (2²⁰ entradas); físico = f × 4096 + d (exemplo da figura: p = 3 → f = 7, d = 512 → 7×4096 + 512 = 29.184, cálculo nosso; o material não dá o valor final).
- Fragmentação (figura 12): partições fixas de 100 KB com processos de 60, 30 e 80 KB → 40 + 70 + 20 = 130 KB de fragmentação interna; partições variáveis com lacunas de 40, 30 e 50 KB → 120 KB livres, mas um processo de 100 KB não cabe (externa).
- Falta de página: RAM 100 ns, falta 8 ms; taxa de 1/1000 → ≈ 8,1 µs por acesso (≈ 81×; o material arredonda para "multiplica por 80").
- Escalonamento de disco (fila 98, 183, 37, 122, 14, 124, 65, 67; cabeça em 53): FCFS 640 cilindros; SSTF 236; SCAN indo para o 0: 236.
- Mapa de bits: 1 TB com blocos de 4 KB → 2²⁸ bits = 32 MB. Índice: bloco de 4 KB com ponteiros de 4 B → 1024 ponteiros → arquivo de até 4 MB.
