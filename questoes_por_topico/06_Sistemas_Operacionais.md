# Sistemas Operacionais — Questões e Gabarito Comentado

**Squad responsável:** Squad 6 (Jorge Orselli Mutran, Kaick Kenithi Nishiya, Lucas Koiti Zotovici Kobayashi, Lucas Secanho do Prado, Matheus Pestilli Rodrigues João)

**Materiais analisados:**
| Arquivo | Páginas | Tipo | Questões encontradas (páginas) |
|---|---|---|---|
| `SISTEMAS_OPERACIONAIS - QUESTOES.docx` | 14 (rodapé "Página X de 14"; conferido na conversão para PDF) | **Caderno de questões** ("Questões objetivas no padrão ENADE — Tema 6"): apresentação, "Quadro de cobertura da Matriz de Referência" (p. 2) e os enunciados completos das 12 questões, uma por página. Não traz gabarito ("encontra-se em documento separado"). Tem 1 figura (Gantt da Q6) | Q1–Q12 (Q1 = p. 3, Q2 = p. 4, …, Q12 = p. 14) |
| `SISTEMAS_OPERACIONAIS - GABARITO.pdf` | 22 | Gabarito comentado das "12 questões objetivas — Tema 6". Traz tipo, domínio cognitivo, letra correta, o texto de todas as alternativas e a justificativa de cada uma, mas não o enunciado. **As alternativas são idênticas, palavra por palavra, às do caderno**, e as 12 letras valem para o caderno | Q1–Q12 (gabarito resumido na p. 2; questões nas p. 3–21) |
| `Slides.pdf` | 53 | Slides "Revisão para o ENADE 2026 – Sistemas Operacionais – Squad 6" | 5 questões, numeradas 1–5 nos slides = Q2, Q5, Q7, Q8 e Q12 do caderno, com enunciado **resumido** (p. 11–12, 26–27, 33–35, 42–44, 51–52) + 1 exercício sugerido (E1, p. 35) |
| `SISTEMAS_OPERACIONAIS - MATERIAL_EXPLICATIVO.pdf` | 57 | Apostila (material explicativo dos 9 tópicos) | Nenhuma questão. Remete ao caderno (p. 15, 28, 34, 43, 50) e comenta Q1 (p. 5), Q2 (p. 10), Q3 (p. 51), Q4 (p. 16), Q5 (p. 25), Q6 (p. 21), Q7 (p. 32), Q9 (p. 41), Q10 (p. 46) e Q12 (p. 48) |

**Resumo:** 12 questões objetivas no padrão ENADE (Q1–Q12, numeração do caderno) e 1 exercício sugerido nos slides (E1). As 12 questões têm enunciado completo no caderno e gabarito no GABARITO.pdf; o E1 não tem gabarito e foi resolvido aqui. Todos os gabaritos foram conferidos (cálculos refeitos com simulação em Python) e **todos estão corretos**. Caderno × gabarito: alternativas, ordem, tipos e tópicos idênticos; nenhuma letra muda. Caderno × slides: os slides trazem versões resumidas de 5 enunciados e mudam a letra correta em Q2 e Q7, além dos distratores da Q8 (ver "Diferenças entre versões" em cada questão).

> **Correspondência de numeração:** Slides Q1 = caderno Q2 · Slides Q2 = Q5 · Slides Q3 = Q7 · Slides Q4 = Q8 · Slides Q5 = Q12.
> **Letras que mudam entre caderno e slides:** Q2 (**D no caderno** e no gabarito, A nos slides) e Q7 (**C no caderno** e no gabarito, B nos slides). Na Q8 a letra é A nas duas versões, mas os distratores B, C e D dos slides são outros. Memorize o **conteúdo** da resposta, não a letra.
> **Quadro de cobertura do caderno (p. 2):** 9 tópicos da matriz (T1–T9) → 12 questões; 10 tipos de questão diferentes (Q9 e Q11 repetem "afirmativas múltiplas"). O quadro só dá o primeiro domínio cognitivo de cada questão (ex.: "Conhecimento"); o gabarito dá os dois (ex.: "Conhecimento (Lembrar) e Compreensão (Entender)").

**Gabarito rápido**
| Questão | Tipo (caderno) | Domínio (quadro) | Gabarito (caderno = GABARITO.pdf) | Gabarito (Slides) | Conteúdo da resposta correta |
|---|---|---|---|---|---|
| Q1 | Lacunas (CAT 1) | Conhecimento | C | — | máquina estendida / gerenciador de recursos / montador / interpretador |
| Q2 | Alternativas constantes — V/F (CAT 2) | Análise | D | A (Questão 1) | V – F – V – F |
| Q3 | Ordenação (CAT 3) | Aplicação | B | — | 2 – 4 – 1 – 5 – 3 (POST → dispositivo → gerenciador de boot → kernel → PID 1) |
| Q4 | Afirmativa incompleta (CAT 1) | Conhecimento | A | — | PCB (Bloco de Controle de Processo) |
| Q5 | Asserção-razão (CAT 3) | Análise | D | D (Questão 2) | I falsa, II verdadeira |
| Q6 | Interpretação (CAT 1) | Aplicação | B | — | SRTF, espera média 3,0 ms |
| Q7 | Resposta única (CAT 1) | Conhecimento | C | B (Questão 3) | área de 300 KB; fragmentação externa |
| Q8 | Resposta única com cálculo aplicado (CAT 1) | Aplicação | A | A (Questão 4) | 9, 8 e 6 faltas; Ótimo = referência teórica, LRU = melhor aproximação |
| Q9 | Afirmativas múltiplas (CAT 2) | Análise | C | — | I, III e IV |
| Q10 | Associação de colunas (CAT 2) | Conhecimento | D | — | 2 – 1 – 3 (encadeada, contígua, indexada) |
| Q11 | Afirmativas múltiplas (CAT 2) | Aplicação | B | — | I, II e IV |
| Q12 | Afirmativa negativa (CAT 1) | Compreensão | E | E (Questão 5) | a afirmação errada é a do polling |

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
**Fonte:** `SISTEMAS_OPERACIONAIS - QUESTOES.docx`, p. 3 (QUESTÃO 1); gabarito em `SISTEMAS_OPERACIONAIS - GABARITO.pdf`, p. 3. Citada em `MATERIAL_EXPLICATIVO.pdf`, p. 5 ("a questão 1 do caderno as cobra em formato de lacunas"). Não aparece nos slides.
**Tipo ENADE:** Lacunas (CAT 1) · Tópico 1 — Visão geral dos SO, máquina de níveis e softwares tradutores · Domínio: Conhecimento

**Enunciado:** (literal, caderno p. 3; a numeração das lacunas entre parênteses foi acrescentada aqui)

Uma fabricante de equipamentos médicos está integrando novos analistas ao time de software embarcado. No treinamento inicial, o arquiteto do produto apresenta o computador como uma máquina de níveis: cada camada oferece uma interface mais conveniente que a camada imediatamente inferior, e o sistema operacional ocupa a posição central dessa organização, cumprindo dois papéis complementares. Em seguida, ele explica como o código escrito pela equipe chega a ser executado pelo processador, passando pelos programas utilitários de tradução.

**Considerando a organização do computador em máquina de níveis e as categorias de softwares tradutores, assinale a alternativa que preenche corretamente as lacunas do texto a seguir.**

Ao ocultar do programador os detalhes do hardware e oferecer abstrações como arquivos, processos e chamadas de sistema, o sistema operacional atua como `__________` (1). Ao arbitrar o uso da CPU, da memória e dos dispositivos entre múltiplos programas e usuários concorrentes, ele atua como `__________` (2). Entre os programas utilitários, aquele que traduz um programa escrito em linguagem simbólica de montagem para a linguagem de máquina é o `__________` (3), enquanto aquele que traduz e executa o código-fonte comando a comando, sem gerar previamente um módulo objeto completo, é o `__________` (4).

**Alternativas:**
- **A)** gerenciador de recursos / máquina estendida / compilador / montador
- **B)** máquina estendida / gerenciador de recursos / compilador / ligador
- **C)** máquina estendida / gerenciador de recursos / montador / interpretador
- **D)** gerenciador de recursos / máquina estendida / montador / compilador

**Gabarito: C** — _(origem: GABARITO.pdf, p. 2 e p. 3)_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Inverte os dois papéis do SO: quem esconde o hardware atrás de abstrações (lacuna 1) é a máquina estendida, não o gerenciador de recursos. Também troca os tradutores: o compilador traduz linguagem de alto nível, não linguagem de montagem (lacuna 3), e o montador não executa código-fonte comando a comando (lacuna 4). Pega quem decorou os termos sem associá-los às definições.
- **B) ❌** — Acerta as duas primeiras lacunas e erra as duas últimas. Quem traduz linguagem de montagem é o montador, não o compilador. O ligador (linker) não traduz nada: só resolve referências entre módulos objeto e bibliotecas e gera o executável.
- **C) ✅** — Máquina estendida (ou máquina virtual, no sentido antigo) = ocultar o hardware e oferecer abstrações (arquivos, processos, chamadas de sistema); gerenciador de recursos = arbitrar CPU, memória e dispositivos entre programas e usuários concorrentes. O montador (assembler) converte mnemônicos em código de máquina, quase uma instrução para uma. O interpretador traduz e executa comando a comando, sem gerar módulo objeto.
- **D) ❌** — Inverte os papéis do SO e troca interpretador por compilador na lacuna 4. O compilador traduz o programa inteiro para um módulo objeto ANTES da execução, justamente o que a lacuna 4 nega ("sem gerar previamente um módulo objeto completo"). Erro comum: tratar compilador e interpretador como sinônimos porque os dois partem de código de alto nível.

**Diferenças entre versões:** caderno × gabarito: alternativas idênticas, mesma letra (C). Vocabulário: o caderno fala em "dois **papéis** complementares" e "atua como"; o gabarito, em "duas **funções** do SO" (justificativas de A e D); a apostila (p. 3) e o slide p. 4 dizem "duas **visões** do mesmo SO".

**⚠️ Atenção:** a apostila (p. 3) insiste que são **duas visões** do mesmo sistema (Tanenbaum), não duas tarefas independentes, e diz que "uma questão bem construída tentaria justamente derrubar a leitura de que se trata de duas tarefas independentes". Uma versão alterada pode cobrar exatamente isso. A ordem das lacunas também pode mudar: associe "ocultar/abstrair" → máquina estendida e "arbitrar/compartilhar" → gerenciador de recursos.

**Conceito-chave para a prova:** máquina estendida = de cima para baixo (abstrações para quem programa); gerenciador de recursos = de baixo para cima (multiplexação no tempo e no espaço). Montador: assembly → máquina. Compilador: alto nível → módulo objeto antes da execução. Interpretador: traduz e executa comando a comando. Ligador: junta módulos (não traduz). Carregador: põe o executável na memória.

---

## Q2 — Modo kernel, interrupção, exceção e syscall
**Fonte:** `SISTEMAS_OPERACIONAIS - QUESTOES.docx`, p. 4 (QUESTÃO 2); gabarito em `SISTEMAS_OPERACIONAIS - GABARITO.pdf`, p. 4. Também em `Slides.pdf`, p. 11 (enunciado resumido, "QUESTÃO 1 · ENADE") e p. 12 (gabarito). Comentada em `MATERIAL_EXPLICATIVO.pdf`, p. 10.
**Tipo ENADE:** Alternativas constantes — V/F (CAT 2) · Tópico 2 — Modos de acesso, interrupções, exceções e chamadas de sistema · Domínio: Análise

**Enunciado:** (literal, caderno p. 4)

Durante a análise de um incidente, uma equipe de sustentação constatou que uma aplicação de terceiros tentou escrever diretamente no registrador de controle da controladora de disco e foi encerrada pelo sistema operacional com erro de violação de acesso. Ao investigar, a equipe revisitou os mecanismos de proteção por modo de acesso e as três formas pelas quais o controle é transferido ao núcleo.

**Analise as afirmações a seguir sobre modo usuário, modo kernel e transferência de controle ao núcleo, identificando-as como Verdadeiras (V) ou Falsas (F).**

( ) A instrução que desabilita as interrupções do processador é privilegiada; se um processo em modo usuário tentar executá-la, o próprio hardware gera uma exceção e transfere o controle ao núcleo.

( ) A interrupção é um evento síncrono, provocado pela instrução que está sendo executada, como uma divisão por zero ou o acesso a um endereço inválido.

( ) A chamada de sistema é o mecanismo pelo qual um processo solicita um serviço ao núcleo, e sua execução provoca a troca controlada de modo usuário para modo kernel por meio de uma instrução de trap.

( ) A API é sinônimo de chamada de sistema, pois toda função de biblioteca corresponde obrigatoriamente a uma única chamada de sistema executada em modo kernel.

**Assinale a alternativa que apresenta a sequência correta.**

**Julgamento das afirmações:**
- **1ª — Verdadeira.** Desabilitar interrupções é instrução privilegiada; em modo usuário o hardware não a executa, gera uma exceção e passa o controle ao núcleo. É o mesmo mecanismo que encerrou a aplicação do incidente.
- **2ª — Falsa.** O texto descreve uma **exceção** (síncrona, causada pela instrução em curso: divisão por zero, endereço inválido). A interrupção é **assíncrona** e vem de um dispositivo externo (disco terminou, temporizador expirou, tecla).
- **3ª — Verdadeira.** É a definição de chamada de sistema: um pedido síncrono e voluntário de serviço ao núcleo, feito por uma instrução de trap que troca para modo kernel.
- **4ª — Falsa.** A API (libc, Win32) roda em modo usuário. Há funções que não geram syscall nenhuma (strlen, sqrt) e outras que geram várias (fopen → open + fstat; printf com buffer pode gerar zero ou vários write). O "obrigatoriamente" e o "uma única" denunciam o erro.

**Alternativas** (caderno = GABARITO.pdf, p. 4):
- **A)** V – V – F – F
- **B)** F – V – V – V
- **C)** V – F – F – V
- **D)** V – F – V – F

**Gabarito: D** (no caderno e no gabarito) **= A na versão dos slides** (sequência **V – F – V – F**) — _(origem: GABARITO.pdf p. 2 e 4 ("GABARITO: D"); Slides p. 12 ("GABARITO: A"))_

**Por que cada alternativa está certa ou errada** (letras do caderno; entre parênteses, a letra nos slides):
- **A) V–V–F–F ❌** (slides B) — Aceita a 2ª, trocando exceção por interrupção (o erro de terminologia mais comum do tópico), e rejeita a 3ª, que define corretamente a syscall. Pega quem usa "interrupção" para qualquer desvio de fluxo.
- **B) F–V–V–V ❌** (slides C) — Nega a 1ª, que está certa e explica o próprio incidente; aceita a 2ª (troca exceção por interrupção) e a 4ª (confunde API com syscall). Só acerta a 3ª.
- **C) V–F–F–V ❌** (slides D) — Acerta as duas primeiras e inverte as duas últimas: nega a definição correta de syscall e aceita a equivalência API = system call.
- **D) V–F–V–F ✅** (slides A) — É o julgamento acima.

**Diferenças entre versões:**
- **Caderno × gabarito:** alternativas idênticas e na mesma ordem; letra D nos dois.
- **Ordem das alternativas nos slides (p. 11):** A) V – F – V – F · B) V – V – F – F · C) F – V – V – V · D) V – F – F – V. A sequência correta passa da última (D) para a primeira (A); as outras três mantêm a ordem relativa. **Letra: D (caderno/gabarito) × A (slides).**
- **Enunciado dos slides (resumido):** "SITUAÇÃO-PROBLEMA — Uma aplicação de terceiros tentou escrever diretamente no registrador de controle da controladora de disco e foi encerrada pelo sistema operacional com erro de violação de acesso. A equipe revisita então os mecanismos de proteção por modo de acesso." (some "Durante a análise de um incidente, uma equipe de sustentação constatou que…" e "e as três formas pelas quais o controle é transferido ao núcleo").
- **Comando:** caderno "sobre **modo usuário, modo kernel** e transferência de controle ao núcleo" × slides "sobre **modo de acesso** e transferência de controle ao núcleo".
- **Afirmações (caderno × slides):** 1ª "desabilita **as** interrupções **do processador**… o **próprio** hardware gera uma exceção e **transfere** o controle" × "desabilita interrupções… o hardware gera uma exceção e **passa** o controle"; 2ª "provocado pela instrução **que está sendo executada**… ou **o** acesso a **um** endereço inválido" × "pela instrução **em execução**… ou **um** acesso a endereço inválido"; 3ª "um processo **solicita** um serviço ao núcleo, **e sua execução provoca a troca controlada** de modo usuário para modo kernel por meio de **uma instrução de trap**" × "um processo **pede** um serviço ao núcleo, **trocando** de modo usuário para modo kernel por meio de **um trap**"; 4ª "corresponde **obrigatoriamente** a uma única **chamada de sistema**" × "corresponde a uma única **syscall**".
- **Fecho:** caderno "Assinale a alternativa **que apresenta** a sequência correta" × slides "Assinale a alternativa **com** a sequência correta".
- Numeração: questão 2 no caderno, "QUESTÃO 1" nos slides. As justificativas do slide são resumos das do gabarito.

**⚠️ Atenção:** só a letra do gabarito diverge entre caderno e slides; o conteúdo é o mesmo. No caderno (versão oficial, coerente com o GABARITO.pdf) a resposta é **D**. Na prova, confira a sequência V–F–V–F e não a letra.

**Conceito-chave para a prova:** interrupção = assíncrona, externa (dispositivo/temporizador); exceção/trap = síncrona, involuntária, causada pela instrução (divisão por zero, endereço inválido, instrução privilegiada, falta de página); syscall = síncrona e voluntária, via instrução de trap. API ≠ syscall. Instrução privilegiada em modo usuário → exceção → o núcleo normalmente encerra o processo.

---

## Q3 — Sequência de boot
**Fonte:** `SISTEMAS_OPERACIONAIS - QUESTOES.docx`, p. 5 (QUESTÃO 3); gabarito em `SISTEMAS_OPERACIONAIS - GABARITO.pdf`, p. 5–6 (com figura da sequência correta). Base teórica: `MATERIAL_EXPLICATIVO.pdf`, Apêndice, p. 51–52 ("é exatamente isso que a questão de ordenação cobra"). Não aparece nos slides (o boot ficou fora da apresentação, segundo a apostila, p. 51).
**Tipo ENADE:** Ordenação (CAT 3) · Tópico 3 — Arquiteturas de núcleo, boot, carregadores de kernel e virtualização · Domínio: Aplicação

**Enunciado:** (literal, caderno p. 5)

Um servidor de uma clínica deixou de inicializar após uma atualização malsucedida. Na tela, o equipamento exibe a mensagem de teste de memória e, logo em seguida, a informação de que nenhum dispositivo inicializável foi encontrado. Para isolar o ponto exato da falha, a analista responsável precisa percorrer mentalmente toda a sequência de inicialização, do acionamento do botão de energia até a disponibilização dos serviços do sistema.

> Etapas da inicialização, apresentadas fora de ordem:
>
> 1. O gerenciador de boot apresenta as opções disponíveis, carrega a imagem do kernel para a memória principal e transfere o controle a ele.
> 2. O firmware residente na placa-mãe executa o autoteste de inicialização (POST), testando e inventariando os dispositivos de hardware essenciais.
> 3. O kernel cria o primeiro processo em modo usuário, de identificador 1, que ativa os serviços e conduz o sistema ao seu estado operacional padrão.
> 4. O firmware localiza o dispositivo de inicialização segundo a ordem configurada e lê o código do carregador nele gravado.
> 5. O kernel inicializa suas estruturas internas, monta o sistema de arquivos raiz e carrega os drivers necessários.

**Considerando o processo de inicialização de um computador de uso geral, ordene as etapas acima na sequência lógica em que devem ocorrer.**

**Alternativas:**
- **A)** 4 – 2 – 1 – 3 – 5
- **B)** 2 – 4 – 1 – 5 – 3
- **C)** 2 – 1 – 4 – 5 – 3
- **D)** 2 – 4 – 5 – 1 – 3

[Figura do gabarito, p. 5 (não está no caderno): cinco cartões da esquerda para a direita, com os números das etapas do enunciado nos círculos — (2) FIRMWARE, "executa o POST e inventaria o hardware", exemplos BIOS · UEFI → (4) DISPOSITIVO DE BOOT, "localiza a unidade e lê o carregador", MBR · partição EFI → (1) GERENCIADOR DE BOOT, "carrega o kernel na memória", GRUB · Boot Manager → (5) KERNEL, "inicializa, monta a raiz e os drivers", vmlinuz · ntoskrnl.exe → (3) PRIMEIRO PROCESSO, "sobe os serviços do sistema", init / systemd (PID 1). Barra "firmware" sob os dois primeiros; "software do sistema operacional" sob os três últimos. "ordem de execução: da esquerda para a direita → 2 - 4 - 1 - 5 - 3".]

**Gabarito: B** — _(origem: GABARITO.pdf, p. 2 e p. 5)_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Põe a busca pelo dispositivo (4) antes do POST (2): o firmware precisa primeiro testar e inventariar o hardware para saber que unidades existem. Também inverte as duas últimas, pondo o primeiro processo (3) antes da montagem da raiz (5), o que é impossível, porque o processo de PID 1 é um executável que mora no sistema de arquivos raiz.
- **B) ✅** — (2) POST do firmware → (4) seleção do dispositivo e leitura do carregador → (1) gerenciador de boot carrega o kernel → (5) kernel se inicializa e monta a raiz → (3) primeiro processo sobe os serviços. A tela mostra que a etapa 2 terminou (mensagem de teste de memória) e que a falha está na etapa 4 ("nenhum dispositivo inicializável"): o problema é o dispositivo de boot ou a configuração do firmware, não o kernel.
- **C) ❌** — Põe o gerenciador de boot (1) antes da leitura do dispositivo (4). O gerenciador não roda desde o início: ele é justamente o código que o firmware lê do dispositivo na etapa 4.
- **D) ❌** — Inverte 1 e 5: o kernel se inicializaria antes de ter sido carregado na memória. É o distrator mais sutil, porque acerta o começo e o fim; atrai quem trata "carregador de boot" e "carga do kernel" como um passo só.

**Diferenças entre versões:**
- **Caderno × gabarito:** alternativas idênticas, letra B nos dois. Os exemplos de implementação (BIOS/UEFI, MBR/partição EFI, GRUB/Windows Boot Manager, vmlinuz/ntoskrnl.exe, init/systemd) só aparecem na figura do gabarito; o caderno descreve as etapas pela função.
- **Numeração das etapas:** o caderno embaralha os números (1 = gerenciador de boot, 2 = POST, 3 = PID 1, 4 = dispositivo, 5 = kernel). A Figura 4 da apostila (p. 52) numera as mesmas etapas em ordem temporal (1 firmware, 2 dispositivo de boot, 3 gerenciador de boot, 4 kernel, 5 primeiro processo). Uma versão alterada pode embaralhar de outro jeito.

**⚠️ Atenção:** guarde a **ordem das funções**, não os números. Detalhe do material: o "Como ler a figura" da apostila (p. 52) diz que "o modo kernel só começa a valer a partir do passo 3", mas na própria Figura 4 o passo 3 é o gerenciador de boot e o kernel é o passo 4. O certo é: o modo kernel passa a valer quando há um núcleo em execução (etapa do kernel).

**Conceito-chave para a prova:** firmware (BIOS/UEFI) + POST → dispositivo de boot (MBR / partição EFI em GPT) → gerenciador de boot (GRUB) carrega kernel + initramfs → kernel inicializa e monta a raiz (switch_root) → PID 1 (init/systemd) sobe os serviços. "Nenhum dispositivo inicializável" = falha entre o POST e o carregador.

---

## Q4 — PCB e troca de contexto
**Fonte:** `SISTEMAS_OPERACIONAIS - QUESTOES.docx`, p. 6 (QUESTÃO 4); gabarito em `SISTEMAS_OPERACIONAIS - GABARITO.pdf`, p. 7. Citada em `MATERIAL_EXPLICATIVO.pdf`, p. 16 ("a questão sobre o núcleo didático cujos processos 'reiniciam do começo' descreve justamente um sistema que não salva esse contexto"). Não aparece nos slides.
**Tipo ENADE:** Afirmativa incompleta (CAT 1) · Tópico 4 — Processos e threads: PCB, contextos, estados e transições · Domínio: Conhecimento

**Enunciado:** (literal, caderno p. 6)

Uma equipe está implementando um núcleo didático multitarefa para uma disciplina de laboratório. O escalonador já funciona, mas os processos, ao retomarem a execução após terem sido preemptados, reiniciam do começo em vez de continuar do ponto em que pararam. A equipe conclui que falta salvar e restaurar corretamente a estrutura de dados que preserva a situação do processador no instante da preempção.

**A estrutura de dados mantida pelo sistema operacional que armazena o contexto de hardware de um processo — em especial o conteúdo dos registradores, do contador de programa e do ponteiro de pilha no instante em que ele perde o processador, permitindo que sua execução seja retomada exatamente do ponto de interrupção — é denominada**

**Alternativas:**
- **A)** Bloco de Controle de Processo (PCB), salvo e restaurado pelo dispatcher a cada troca de contexto.
- **B)** tabela de páginas do processo, mantida pela MMU para traduzir seus endereços lógicos durante a execução.
- **C)** pilha de execução do processo, na qual são alocados os registros de ativação das funções chamadas.
- **D)** vetor de interrupções, consultado pelo processador para localizar a rotina de tratamento do evento ocorrido.

**Gabarito: A** — _(origem: GABARITO.pdf, p. 2 e p. 7)_

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — O PCB (task_struct no Linux, EPROCESS no Windows) representa o processo dentro do núcleo. Guarda o contexto de hardware (registradores, PC, SP, PSW), o contexto de software (PID, prioridade, quotas, limites, estado) e o espaço de endereçamento. É o que o dispatcher salva ao tirar o processo da CPU e restaura ao devolvê-la; sem ele, o processo não tem como retomar do ponto em que parou.
- **B) ❌** — A tabela de páginas também é por processo e também é trocada na troca de contexto, o que a torna plausível. Mas guarda o mapeamento página → quadro, não os registradores: restaurá-la sozinha devolveria a memória, não o ponto de execução (PC).
- **C) ❌** — A pilha guarda endereços de retorno e variáveis locais, o que lembra "retomar de onde parou". Mas isso vale entre chamadas de função dentro do mesmo fluxo; ela não preserva o estado completo do processador entre processos, nem é gerenciada pelo dispatcher.
- **D) ❌** — O vetor de interrupções é consultado no instante da interrupção, daí a associação. Mas é uma estrutura **global** do sistema, não por processo: contém endereços de rotinas de tratamento, não o estado de quem foi interrompido.

**Diferenças entre versões:** caderno × gabarito: alternativas idênticas, letra A nos dois. Única outra fonte: a apostila p. 16, que resume o cenário ("processos que 'reiniciam do começo'").

**⚠️ Atenção:** o gabarito está certo. Nuance de redação: a alternativa A diz que o PCB é "salvo e restaurado"; a rigor, o dispatcher salva o contexto de hardware **no** PCB e o restaura **a partir** dele (apostila p. 17; slide p. 14). Não muda a resposta.

**Conceito-chave para a prova:** PCB = contexto de hardware + contexto de software + espaço de endereçamento (Machado & Maia). A troca de contexto salva o contexto de hardware no PCB do processo que sai e restaura o do que entra; é puro overhead. Não existe a transição ESPERA → EXECUÇÃO (sempre se passa por PRONTO).

---

## Q5 — Exclusão mútua e deadlock
**Fonte:** `SISTEMAS_OPERACIONAIS - QUESTOES.docx`, p. 7 (QUESTÃO 5); gabarito em `SISTEMAS_OPERACIONAIS - GABARITO.pdf`, p. 8–9 (com figura do grafo de alocação). Também em `Slides.pdf`, p. 26 (enunciado resumido, "QUESTÃO 2 · ENADE") e p. 27 (gabarito). Comentada em `MATERIAL_EXPLICATIVO.pdf`, p. 25–26.
**Tipo ENADE:** Asserção-razão (CAT 3) · Tópico 4 — Concorrência, exclusão mútua, semáforos e deadlock · Domínio: Análise

**Enunciado:** (literal, caderno p. 7)

Um sistema de reservas mantém duas estruturas compartilhadas — a agenda de salas (protegida pelo mutex A) e o cadastro de participantes (protegido pelo mutex B). A rotina de criação de reunião adquire A e, ainda de posse dele, solicita B. A rotina de cancelamento adquire B e, ainda de posse dele, solicita A. Todas as regiões críticas estão corretamente delimitadas por operações de aquisição e liberação. Em produção, sob carga, o sistema trava de forma intermitente: as duas rotinas ficam bloqueadas indefinidamente e nenhuma delas prossegue.

**Considerando os mecanismos de sincronização e as condições necessárias à ocorrência de impasses, avalie as asserções a seguir e a relação proposta entre elas.**

I. O uso correto de semáforos binários (mutexes) em torno de todas as regiões críticas do sistema descrito é suficiente para garantir que ele não entre em deadlock,

**PORQUE**

II. a exclusão mútua assegurada pelos semáforos impede que dois fluxos de execução acessem simultaneamente a mesma estrutura compartilhada, eliminando as condições de corrida.

**A respeito dessas asserções, assinale a opção correta.**

[Figura do gabarito, p. 8 (não está no caderno): grafo de alocação de recursos. T1 detém R1 (mutex A) e espera R2 (mutex B); T2 detém R2 (mutex B) e espera R1 (mutex A). Ciclo fechado T1 → R2 → T2 → R1 → T1 = deadlock. Ao lado, as 4 condições de Coffman: 1) exclusão mútua, 2) posse e espera, 3) não preempção, 4) espera circular.]

**Julgamento:**
- **Asserção I — Falsa.** Exclusão mútua não previne impasse; ela é a **primeira** das quatro condições de Coffman. No cenário as outras três também valem: posse e espera (cada rotina segura um mutex e pede o outro), não preempção e espera circular (A e B adquiridos em ordens opostas). O sistema trava justamente porque os mutexes funcionam.
- **Asserção II — Verdadeira.** Descreve corretamente o papel da exclusão mútua: impedir acesso simultâneo à estrutura compartilhada e, assim, eliminar condições de corrida.
- **Relação:** como I é falsa, não há justificativa a avaliar. Além disso, II trata de outro problema (condição de corrida, não deadlock).

**Alternativas:** (iguais no caderno, no gabarito e nos slides)
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

**Diferenças entre versões:**
- **Caderno × gabarito × slides:** alternativas e asserção I idênticas; gabarito D nas três fontes. Numeração: questão 5 no caderno, "QUESTÃO 2" nos slides.
- **Situação-problema dos slides (resumida):** "Um sistema de reservas protege a agenda de salas com o mutex A e o cadastro de participantes com o mutex B. A rotina de criação adquire A e, ainda de posse dele, pede B; a de cancelamento adquire B e pede A. Todas as regiões críticas estão corretamente delimitadas. Em produção, sob carga, as duas rotinas travam indefinidamente." O caderno acrescenta "mantém duas estruturas compartilhadas", "criação **de reunião**", "solicita" (× "pede"), "delimitadas **por operações de aquisição e liberação**" e "o sistema trava **de forma intermitente**: … e nenhuma delas prossegue".
- **Comando:** o caderno começa com "**Considerando os mecanismos de sincronização e as condições necessárias à ocorrência de impasses,** avalie…"; os slides só "Avalie as asserções a seguir e a relação proposta entre elas."
- **Asserção II:** caderno "dois fluxos **de execução**" × slides "dois fluxos".
- A figura do gabarito usa os rótulos "detém/espera" e a dos slides (p. 20) "alocado a/requisita". Justificativas dos slides resumidas.

**Conceito-chave para a prova:** condições de Coffman (todas precisam valer juntas): exclusão mútua, posse e espera, não preempção, espera circular. Condição de corrida ≠ deadlock: o semáforo resolve a primeira e, mal usado, causa o segundo. Remédio típico (ENADE 2017): ordem global de aquisição dos locks.

---

## Q6 — Escalonamento SRTF e SLA de espera
**Fonte:** `SISTEMAS_OPERACIONAIS - QUESTOES.docx`, p. 8 (QUESTÃO 6, com figura do Gantt observado); gabarito em `SISTEMAS_OPERACIONAIS - GABARITO.pdf`, p. 10–11 (com figura de Gantt das quatro políticas). Citada em `MATERIAL_EXPLICATIVO.pdf`, p. 21. Não aparece nos slides.
**Tipo ENADE:** Interpretação (CAT 1), com cálculo · Tópico 5 — Compartilhamento do processador e algoritmos de escalonamento · Domínio: Aplicação

**Enunciado:** (literal, caderno p. 8)

A equipe de engenharia de desempenho de uma plataforma de atendimento coletou o traço de execução de quatro tarefas em um núcleo de processamento, sob a política de escalonamento atualmente configurada. O acordo de nível de serviço (SLA) da plataforma estabelece que o tempo médio de espera das tarefas na fila de prontos não pode ultrapassar 3,5 ms, e a equipe precisa propor a política que passará a ser adotada.

> Tabela de processos e diagrama de Gantt observado com a política atual (ver figura):
>
> P1 — chegada 0 ms, duração 7 ms
> P2 — chegada 2 ms, duração 4 ms
> P3 — chegada 4 ms, duração 1 ms
> P4 — chegada 5 ms, duração 4 ms
>
> Execução observada: P1 [0–7] · P2 [7–11] · P3 [11–12] · P4 [12–16]
>
> Requisito do SLA: tempo médio de espera ≤ 3,5 ms. As durações das tarefas são conhecidas previamente pelo escalonador.

[Figura do caderno — título "Diagrama de Gantt observado com a política atual". À esquerda, tabela Processo | Chegada | Duração: P1 | 0 ms | 7 ms; P2 | 2 ms | 4 ms; P3 | 4 ms | 1 ms; P4 | 5 ms | 4 ms. À direita, Gantt com eixo "tempo (ms)" marcado em 0, 7, 11, 12, 16: P1 de 0 a 7, P2 de 7 a 11, P3 de 11 a 12, P4 de 12 a 16. Rodapé: "Cada barra indica qual processo ocupou o processador em cada intervalo." Legenda: "Figura — Traço de execução observado com a política atual. Elaboração dos autores."]

**Com base na interpretação do diagrama de Gantt e da tabela de processos, assinale a alternativa que propõe a política de escalonamento capaz de atender ao SLA, acompanhada do tempo médio de espera que ela produz para essa carga.**

**Alternativas:**
- **A)** SJF não preemptivo (Shortest Job First), com tempo médio de espera de 3,0 ms.
- **B)** SRTF (menor tempo restante primeiro), com tempo médio de espera de 3,0 ms.
- **C)** Round-Robin com quantum de 2 ms, com tempo médio de espera de 1,5 ms.
- **D)** Manter o FCFS (4,75 ms), pois políticas preemptivas levariam tarefas longas à inanição.

**Gabarito: B** — _(origem: GABARITO.pdf, p. 2 e p. 10)_

**Interpretação do traço:** o enunciado não nomeia a política atual, mas o Gantt mostra os processos atendidos na ordem de chegada e sem preempção = **FCFS** (a alternativa D e a figura do gabarito, "FCFS (política atual)", confirmam).

**Cálculos refeitos** (espera = conclusão − chegada − duração; conferido em Python):

| Política | Gantt | Esperas P1, P2, P3, P4 | Média | SLA ≤ 3,5? |
|---|---|---|---|---|
| FCFS (traço observado) | P1[0–7] P2[7–11] P3[11–12] P4[12–16] | 0, 5, 7, 7 | 19/4 = **4,75 ms** | não |
| SJF não preemptivo | P1[0–7] P3[7–8] P2[8–12] P4[12–16] | 0, 6, 3, 7 | 16/4 = **4,0 ms** | não |
| SRTF | P1[0–2] P2[2–4] P3[4–5] P2[5–7] P4[7–11] P1[11–16] | 9, 1, 0, 2 | 12/4 = **3,0 ms** | **sim** |
| RR q = 2 (chegada antes do preemptado — convenção do gabarito) | P1[0–2] P2[2–4] P1[4–6] P3[6–7] P2[7–9] P4[9–11] P1[11–13] P4[13–15] P1[15–16] | 9, 3, 2, 6 | 20/4 = **5,0 ms** | não |
| RR q = 2 (preemptado antes da chegada simultânea) | P1[0–4] P2[4–6] P1[6–8] P3[8–9] P4[9–11] P2[11–13] P1[13–14] P4[14–16] | 7, 7, 4, 7 | 25/4 = **6,25 ms** | não |

Tempo de **resposta** no RR (convenção do gabarito): 0, 0, 2, 4 → média **1,5 ms**.

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — No SJF **não preemptivo**, P1 começa em t = 0 e vai até t = 7 sem ser interrompido; a média é **4,0 ms** (o empate P2/P4 em t = 8 não altera a média). Os 3,0 ms só aparecem se P2 e P3 interromperem P1, ou seja, simulando SRTF sem perceber. Pega a confusão entre as versões preemptiva e não preemptiva do SJF.
- **B) ✅** — Em t = 2, P2 (4 ms) preempta P1 (5 ms restantes); em t = 4, P3 (1 ms) preempta P2 (2 restantes); em t = 5, P4 (4) não preempta P2 (2 restantes); em t = 7, P4 (4) vence P1 (5). Esperas 9, 1, 0, 2 → (9 + 1 + 0 + 2)/4 = 3,0 ms ≤ 3,5 ms. O SRTF minimiza a espera média quando as durações são conhecidas, e o enunciado diz que elas são ("As durações das tarefas são conhecidas previamente pelo escalonador").
- **C) ❌** — A espera média real do RR q = 2 é **5,0 ms** (6,25 ms na convenção inversa da fila): viola o SLA. Os **1,5 ms** são a média do tempo de **resposta** (até a 1ª execução: 0, 0, 2, 4). Pega quem confunde resposta com espera, justamente o critério em que o RR se destaca.
- **D) ❌** — O FCFS dá de fato 4,75 ms (esperas 0, 5, 7, 7), acima do limite: mantê-lo descumpre o SLA. A preocupação com inanição é legítima no SRTF com chegada contínua de tarefas curtas, mas se trata com envelhecimento (aging); nesta carga P1 termina em t = 16, sem inanição.

**Diferenças entre versões:**
- **Caderno × gabarito:** alternativas idênticas, letra B nos dois. A figura do caderno mostra **só o traço observado (FCFS)**; a figura do gabarito (p. 10) mostra as quatro políticas (FCFS 4,75 ms, SJF não preemptivo 4,00 ms, SRTF 3,00 ms "atende", RR q = 2 5,00 ms) e rotula a primeira como "FCFS (política atual)", nome que o enunciado do caderno não usa.
- **Convenção do Round-Robin:** só a legenda da figura do gabarito diz que "o processo que chega entra na fila antes do processo preemptado"; o caderno não fixa a convenção.
- **Apostila p. 21:** diz que "É o SRTF que gera o diagrama de Gantt da questão 6 do caderno", mas o Gantt do caderno é o do FCFS (política atual). O Gantt do SRTF está só na figura do gabarito (é o da resposta).

**⚠️ Atenção:** como o caderno não diz qual convenção usar no RR, a média do RR pode ser 5,0 ou 6,25 ms; as duas violam o SLA, então a resposta não muda. Numa versão alterada (outros bursts ou chegadas), **refaça o Gantt reavaliando a fila a cada chegada**: o erro mais comum, segundo a apostila (p. 28), é aplicar a política uma vez só, o que transforma SRTF em SJF não preemptivo.

**Conceito-chave para a prova:** turnaround = conclusão − chegada; espera = turnaround − duração; resposta = 1ª execução − chegada. SRTF (preemptivo) minimiza a espera média; SJF não preemptivo só é ótimo com chegadas simultâneas; RR otimiza o tempo de resposta, não a espera; FCFS sofre efeito comboio.

---

## Q7 — Best-fit e fragmentação externa
**Fonte:** `SISTEMAS_OPERACIONAIS - QUESTOES.docx`, p. 9 (QUESTÃO 7); gabarito em `SISTEMAS_OPERACIONAIS - GABARITO.pdf`, p. 12–13 (com figura). Também em `Slides.pdf`, p. 33 (enunciado resumido, "QUESTÃO 3 · ENADE"), p. 34 (gabarito) e p. 35 (resolução passo a passo). Citada em `MATERIAL_EXPLICATIVO.pdf`, p. 32.
**Tipo ENADE:** Resposta única (CAT 1) · Tópico 6 — Memória principal: alocação contígua, particionamento e fragmentação · Domínio: Conhecimento

**Enunciado:** (literal, caderno p. 9)

Um sistema embarcado utiliza gerenciamento de memória com partições variáveis e alocação contígua. Em determinado instante, o mapa de áreas livres da memória principal apresenta, na ordem crescente de endereço, blocos de 100 KB, 500 KB, 200 KB, 300 KB e 600 KB. Nesse momento, o sistema recebe a requisição de carga de um processo que necessita de 212 KB contíguos.

**Considerando o funcionamento das estratégias de alocação e os tipos de fragmentação, assinale a alternativa que indica corretamente a área escolhida pela estratégia best-fit e o tipo de fragmentação característico desse esquema de gerenciamento.**

[Figura do gabarito p. 12 / slides p. 35 (não está no caderno): áreas livres, em ordem de endereço, separadas por blocos ocupados: 100 KB | 500 KB | 200 KB | 300 KB | 600 KB. Pedido de 212 KB. first-fit → 500 KB (resto 288 KB); best-fit → 300 KB (resto 88 KB); worst-fit → 600 KB (resto 388 KB).]

**Alternativas** (caderno = GABARITO.pdf, p. 12–13):
- **A)** A área de 500 KB; a fragmentação característica é a interna, pois sobra espaço não utilizado dentro da partição alocada ao processo.
- **B)** A área de 300 KB; a fragmentação característica é a interna, pois a partição tem tamanho predefinido, superior ao exigido pelo processo.
- **C)** A área de 300 KB; a fragmentação característica é a externa, pois restam lacunas livres pequenas e dispersas, incapazes de atender a novos pedidos.
- **D)** A área de 600 KB; a fragmentação característica é a externa, pois a maior lacuna disponível é subdividida a cada nova alocação realizada.

**Alternativas — versão dos slides (p. 33):**
- **A)** A área de 500 KB; a fragmentação característica é a interna, pois sobra espaço não utilizado dentro da partição alocada ao processo.
- **B)** A área de 300 KB; a fragmentação característica é a externa, pois restam lacunas livres pequenas e dispersas, incapazes de atender a novos pedidos.
- **C)** A área de 300 KB; a fragmentação característica é a interna, pois a partição tem tamanho predefinido e sempre maior que o do processo.
- **D)** A área de 600 KB; a fragmentação característica é a externa, pois a maior lacuna disponível é subdividida a cada nova alocação realizada.

**Gabarito: C** (no caderno e no gabarito) **= B na versão dos slides** (300 KB + fragmentação **externa**) — _(origem: GABARITO.pdf p. 2 e 13 ("GABARITO: C"); Slides p. 34 ("GABARITO: B"))_

**Por que cada alternativa está certa ou errada** (letras do caderno; entre parênteses, a letra nos slides):
- **A) 500 KB / interna ❌** (slides A) — 500 KB é a resposta do **first-fit** (a primeira que cabe). E fragmentação interna é característica de partições **fixas**.
- **B) 300 KB / interna ❌** (slides C) — Acerta a área do best-fit e erra o tipo de fragmentação. Em partições variáveis, a partição nasce com o tamanho exato do processo; não existe "tamanho predefinido", e o desperdício fica FORA das partições. É o distrator mais próximo do gabarito.
- **C) 300 KB / externa ✅** (slides B) — O best-fit varre todas as áreas e escolhe a MENOR que comporta o pedido: entre 500, 300 e 600 KB (as que cabem 212 KB), a menor é 300 KB, com resto de 88 KB. Em alocação contígua com partições variáveis, o desperdício são lacunas livres pequenas e dispersas = fragmentação **externa**.
- **D) 600 KB / externa ❌** (slides D) — 600 KB é a resposta do **worst-fit** (a maior de todas). O tipo de fragmentação está certo, o que aumenta a plausibilidade, mas a estratégia não é a pedida.

**Diferenças entre versões:**
- **Caderno × gabarito:** alternativas idênticas e na mesma ordem; letra C nos dois.
- **Slides:** **B e C trocam de lugar**, e a letra do gabarito muda: **C (caderno/gabarito) × B (slides)**.
- Redação da alternativa "300 KB / interna": caderno "pois a partição tem tamanho predefinido, **superior ao exigido pelo processo**" × slides "pois a partição tem tamanho predefinido **e sempre maior que o do processo**".
- **Situação-problema dos slides (resumida):** "Um sistema embarcado **usa** partições variáveis **com** alocação contígua. O mapa de áreas livres apresenta, **em** ordem crescente de endereço, blocos de 100 KB, 500 KB, 200 KB, 300 KB e 600 KB. **Chega a requisição** de um processo que **precisa** de 212 KB contíguos." (o caderno diz "utiliza gerenciamento de memória com partições variáveis e alocação contígua", "Em determinado instante", "da memória principal", "Nesse momento, o sistema recebe a requisição de carga", "necessita"). Os números e o comando são iguais.
- O cabeçalho do gabarito nos slides (p. 34) diz "Tópico 6 — Memória principal: particionamento, fragmentação e relocação"; o caderno e o GABARITO.pdf, "Tópico 6 — Memória principal: alocação contígua, particionamento e fragmentação".
- Slides chamam de "QUESTÃO 3", o caderno de "questão 7". O slide p. 35 mostra os restos (288/88/388 KB) e sugere treinar o mesmo mapa com pedidos de 417, 112 e 426 KB (ver E1).

**⚠️ Atenção:** a letra correta depende da versão: **C no caderno** (versão oficial, coerente com o GABARITO.pdf), B nos slides. Memorize "300 KB + externa".

**Conceito-chave para a prova:** first-fit = primeira que cabe (mais rápida); best-fit = menor que cabe (menor resto, mas espalha lacunas minúsculas); worst-fit = maior de todas. Fragmentação interna = DENTRO da área alocada (partições fixas, última página na paginação); externa = FORA, em lacunas dispersas (partições variáveis, segmentação). Compactação resolve a externa, mas exige relocação dinâmica.

---

## Q8 — Substituição de páginas FIFO, LRU e Ótimo
**Fonte:** `SISTEMAS_OPERACIONAIS - QUESTOES.docx`, p. 10 (QUESTÃO 8); gabarito em `SISTEMAS_OPERACIONAIS - GABARITO.pdf`, p. 14–15 (com figura FIFO/LRU). Também em `Slides.pdf`, p. 42 (enunciado resumido, "QUESTÃO 4 · ENADE"), p. 43 (gabarito) e p. 44 (simulação quadro a quadro).
**Tipo ENADE:** Resposta única com cálculo aplicado (CAT 1) · Tópico 7 — Memória virtual: políticas de substituição de páginas · Domínio: Aplicação

**Enunciado:** (literal, caderno p. 10)

A arquiteta de um sistema operacional para dispositivos de borda precisa escolher a política de substituição de páginas do gerenciador de memória virtual. Para fundamentar a decisão, ela simula o comportamento de três algoritmos sobre a mesma carga de trabalho, com três quadros de página e memória inicialmente vazia.

> Cadeia de referências a páginas utilizada na simulação:
>
> 7 · 0 · 1 · 2 · 0 · 3 · 0 · 4 · 2 · 3
>
> Número de quadros disponíveis: 3. Memória inicialmente vazia (todas as faltas iniciais devem ser contabilizadas).

**Ao simular os algoritmos FIFO, LRU e Ótimo sobre a cadeia de referências apresentada, qual é o número de faltas de página produzido por cada um deles, respectivamente, e qual conclusão de projeto se sustenta a partir do resultado?**

**Alternativas** (caderno = GABARITO.pdf, p. 14–15):
- **A)** 9, 8 e 6 faltas; o algoritmo Ótimo serve apenas como referência teórica de desempenho, e o LRU é a política implementável mais próxima dele.
- **B)** 9, 9 e 8 faltas; FIFO e LRU têm desempenho equivalente nessa carga, de modo que a escolha entre eles deve considerar apenas o custo de implementação.
- **C)** 6, 5 e 3 faltas; como as primeiras cargas ocorrem em memória vazia, elas não configuram falta de página e não entram na contagem.
- **D)** 15, 13 e 9 faltas; toda referência a uma página que provoque substituição gera duas faltas, uma na retirada e outra na carga da nova página.

**Alternativas — versão dos slides (p. 42):**
- **A)** 9, 8 e 6 faltas; o algoritmo Ótimo serve apenas como referência teórica de desempenho, e o LRU é a política implementável mais próxima dele.
- **B)** 9, 9 e 6 faltas; FIFO e LRU produzem o mesmo resultado nesta cadeia, e a escolha entre eles deve recair sobre o de menor custo de implementação.
- **C)** 9, 8 e 7 faltas; o Ótimo não elimina as faltas de partida a frio e, por isso, fica apenas uma falta abaixo do LRU nesta simulação.
- **D)** 10, 8 e 6 faltas; o FIFO penaliza as páginas mais antigas mesmo quando reutilizadas, gerando uma falta a mais que o LRU nas referências repetidas.

**Gabarito: A** (nas três fontes) — _(origem: GABARITO.pdf p. 2 e 14; Slides p. 43)_

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

**Por que cada alternativa está certa ou errada** (versão do caderno; depois, os distratores dos slides):
- **A) ✅** (igual nas duas versões) — 9 (FIFO: só o 0 da 5ª posição é acerto), 8 (LRU: acertos nos 0 da 5ª e da 7ª) e 6 (Ótimo: acertos em 0, 0, 2 e 3). A conclusão também está certa: o Ótimo exige conhecer o futuro, então é limite inferior teórico; o LRU o aproxima usando o passado recente.
- **B, caderno (9, 9 e 8) ❌** — O LRU dá 8 (não 9) e o Ótimo dá 6 (não 8). A conclusão também falha: além de não haver empate, o FIFO sofre a anomalia de Belady e o LRU (algoritmo de pilha) não, então o custo de implementação não é o único critério.
- **C, caderno (6, 5 e 3) ❌** — Não conta as 3 faltas compulsórias (memória vazia), que são faltas legítimas e que o enunciado manda contar: 9 − 3, 8 − 3, 6 − 3.
- **D, caderno (15, 13 e 9) ❌** — Conta duas faltas por substituição. Uma substituição é **um** evento de falta (retira a vítima e carrega a nova no mesmo tratamento): 3 + 2×6 = 15, 3 + 2×5 = 13, 3 + 2×3 = 9.
- **B, slides (9, 9 e 6) ❌** — Trata o LRU como FIFO. Na 6ª referência o LRU expulsa a 1, não a 0, e por isso acerta na 7ª. Quem "empata" os dois não simulou.
- **C, slides (9, 8 e 7) ❌** — Ótimo mal simulado: expulsar a 2 (em vez da 1, que nunca mais aparece) na 6ª referência gera uma falta extra na 9ª. O Ótimo nunca perde para o LRU. A primeira parte da frase ("não elimina as faltas de partida a frio") é verdadeira, mas o número está errado.
- **D, slides (10, 8 e 6) ❌** — Conta a 5ª referência (página 0, já residente) como falta do FIFO. Acerto não gera substituição: é erro de contagem.

**Diferenças entre versões:**
- **Caderno × gabarito:** alternativas idênticas; letra A nos dois.
- **A** (correta) é idêntica nas três fontes.
- **B:** caderno "9, 9 e **8**; FIFO e LRU têm desempenho equivalente nessa carga, de modo que a escolha entre eles deve considerar apenas o custo de implementação" × slides "9, 9 e **6**; FIFO e LRU produzem o mesmo resultado nesta cadeia, e a escolha entre eles deve recair sobre o de menor custo de implementação".
- **C:** caderno "6, 5 e 3" (sem as faltas compulsórias) × slides "9, 8 e 7" (Ótimo mal simulado).
- **D:** caderno "15, 13 e 9" (duas faltas por substituição) × slides "10, 8 e 6" (acerto contado como falta).
- **Situação-problema dos slides (resumida):** "…precisa escolher a política de substituição de páginas. Para fundamentar a decisão, simula três algoritmos sobre a mesma carga, com três quadros e memória inicialmente vazia." O caderno acrescenta "do gerenciador de memória virtual", "ela simula **o comportamento de** três algoritmos", "carga **de trabalho**" e "três quadros **de página**". Dados de suporte e comando idênticos.
- Slides chamam de "QUESTÃO 4", o caderno de "questão 8". O slide p. 44 traz a tabela do Ótimo; a figura do gabarito só traz FIFO e LRU e dá o total do Ótimo (6).

**⚠️ Atenção:** a resposta é A nas duas versões, mas os distratores mudam; a prova pode trazer qualquer combinação deles. Se a cadeia ou o número de quadros mudar, simule de novo (empate de vítima no Ótimo não altera o total).

**Conceito-chave para a prova:** faltas compulsórias contam; substituição = 1 falta; FIFO tira a mais antiga e sofre anomalia de Belady (1-2-3-4-1-2-5-1-2-3-4-5: 9 faltas com 3 quadros, 10 com 4 — conferido); LRU tira a menos recentemente usada, é de pilha (sem Belady) e precisa de apoio de hardware; Ótimo tira a usada mais tarde ou nunca, não é implementável e serve de referência.

---

## Q9 — Thrashing, working set, TLB e alocação de quadros
**Fonte:** `SISTEMAS_OPERACIONAIS - QUESTOES.docx`, p. 11 (QUESTÃO 9); gabarito em `SISTEMAS_OPERACIONAIS - GABARITO.pdf`, p. 16–17 (com figura da curva de Denning). Citada em `MATERIAL_EXPLICATIVO.pdf`, p. 41 ("a armadilha que a questão 9 do caderno explora"). Não aparece nos slides.
**Tipo ENADE:** Afirmativas múltiplas (CAT 2) · Tópico 7 — Working set, TLB, thrashing e políticas de alocação de quadros · Domínio: Análise

**Enunciado:** (literal, caderno p. 11)

Um servidor de aplicação apresenta degradação severa de desempenho. O monitoramento mostra utilização de CPU abaixo de 8%, fila de E/S do disco permanentemente saturada e taxa de faltas de página duas ordens de grandeza acima do valor histórico. A quantidade de processos residentes vinha sendo aumentada gradualmente ao longo da semana.

**Considerando os conceitos de memória virtual e o diagnóstico do cenário apresentado, avalie as afirmativas a seguir.**

I. O quadro descrito caracteriza thrashing, situação em que a utilização da CPU despenca em meio a intensa atividade de paginação, e que ocorre quando o conjunto de páginas ativas (working set) dos processos residentes excede o número de quadros disponíveis na memória principal.

II. Ampliar ainda mais o grau de multiprogramação é a medida corretiva adequada, pois, havendo mais processos prontos, o escalonador consegue manter a CPU ocupada enquanto os demais aguardam a conclusão das operações de E/S de página.

III. A TLB é uma memória associativa que armazena as traduções de páginas mais recentemente utilizadas; um acerto na TLB dispensa a consulta à tabela de páginas residente na memória principal para concluir a tradução do endereço.

IV. Sob política de substituição global, um processo pode tomar quadros de outro e, por isso, sua taxa de faltas de página passa a depender do comportamento dos demais processos, ao passo que, na política local, essa taxa depende apenas do próprio comportamento.

**É correto apenas o que se afirma em**

[Figura do gabarito, p. 16 (não está no caderno): utilização da CPU × grau de multiprogramação. A curva sobe ("cada processo ainda tem quadros suficientes") até o "ponto de virada" e depois despenca (THRASHING: "o working set não cabe — mais paginação que trabalho útil").]

**Julgamento das afirmativas:**
- **I — Verdadeira.** CPU abaixo de 8% + disco saturado + faltas duas ordens de grandeza acima do normal, depois de aumentar os processos residentes, é o retrato do thrashing; o critério é o working set (somado, dos processos residentes) não caber nos quadros.
- **II — Falsa.** É a medida que **agrava** o problema: mais processos significa menos quadros por processo, mais faltas e mais colapso (o ciclo vicioso do escalonador de longo prazo que, vendo a CPU ociosa, admite mais processos). O cenário já mostra isso: a quantidade de processos vinha aumentando. O certo é **reduzir** o grau de multiprogramação, suspendendo processos.
- **III — Verdadeira.** Definição correta de TLB (memória associativa com as traduções recentes) e do efeito do acerto (dispensa o acesso extra à tabela de páginas na memória).
- **IV — Verdadeira.** Distingue corretamente alocação global e local, inclusive o efeito colateral da global: o desempenho de cada processo passa a depender dos demais.

**Alternativas:**
- **A)** I e II.
- **B)** II e III.
- **C)** I, III e IV.
- **D)** I, II e IV.

**Gabarito: C** — _(origem: GABARITO.pdf, p. 2 e p. 16)_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Aceita II, justamente a intervenção que aprofunda o colapso, e deixa de fora III e IV, que são corretas.
- **B) ❌** — Aceita II e rejeita I (o diagnóstico correto) e IV. Pega quem sabe TLB mas não liga os três indicadores ao thrashing.
- **C) ✅** — I, III e IV corretas; II é a única falsa.
- **D) ❌** — Acerta I e IV, mas inclui II. É o distrator mais próximo: atrai quem identificou o fenômeno e raciocinou só em "manter a CPU ocupada".

**Diferenças entre versões:** caderno × gabarito: alternativas idênticas, letra C nos dois. A justificativa do gabarito para IV fala em "efeito colateral da global sobre a previsibilidade de desempenho"; a afirmativa do caderno diz o mesmo com outras palavras ("sua taxa de faltas de página passa a depender do comportamento dos demais processos").

**⚠️ Atenção:** o gabarito está certo. Numa versão alterada, os números (8% de CPU, "duas ordens de grandeza") podem mudar; o diagnóstico não: CPU baixa + disco saturado + faltas em alta = thrashing, e o remédio é **reduzir** a multiprogramação, nunca aumentá-la.

**Conceito-chave para a prova:** thrashing = CPU baixa + disco saturado + faltas altas → **reduzir** a multiprogramação (suspender processos); prevenção por modelo de working set ou PFF (frequência de faltas). TLB: TEA = h·(ε + t) + (1 − h)·(ε + 2t). Alocação local isola o processo; a global adapta melhor, mas contamina.

---

## Q10 — Métodos de alocação em disco
**Fonte:** `SISTEMAS_OPERACIONAIS - QUESTOES.docx`, p. 12 (QUESTÃO 10); gabarito em `SISTEMAS_OPERACIONAIS - GABARITO.pdf`, p. 18 (com figura). Ver `MATERIAL_EXPLICATIVO.pdf`, p. 45–46 (palavras-chave para "questão de associação"). Não aparece nos slides como questão (só a figura no slide p. 47).
**Tipo ENADE:** Associação de colunas (CAT 2) · Tópico 8 — Sistemas de arquivos: métodos de alocação em disco · Domínio: Conhecimento

**Enunciado:** (literal, caderno p. 12)

Ao especificar o sistema de arquivos de um equipamento de aquisição de dados, uma equipe de projeto avalia como os blocos de cada arquivo serão distribuídos no disco. A decisão precisa levar em conta o desempenho no acesso sequencial e no acesso direto, a ocorrência de fragmentação e o custo de estruturas auxiliares.

> **Coluna 1 — Métodos de alocação**
> 1. Alocação contígua
> 2. Alocação encadeada
> 3. Alocação indexada
>
> **Coluna 2 — Características**
>
> ( ) Cada bloco do arquivo guarda um ponteiro para o bloco seguinte, o que elimina a fragmentação externa, mas torna o acesso direto ineficiente, pois exige percorrer a cadeia desde o início.
>
> ( ) O arquivo ocupa um conjunto de blocos sequenciais no disco, o que oferece o melhor desempenho em leitura sequencial e permite acesso direto por cálculo simples, mas provoca fragmentação externa e dificulta o crescimento do arquivo.
>
> ( ) Um bloco dedicado reúne os ponteiros para todos os blocos de dados do arquivo, o que preserva a eficiência do acesso direto e elimina a fragmentação externa, ao custo do espaço ocupado pela estrutura de índice.

**Relacione os métodos de alocação de arquivos em disco da primeira coluna com as características apresentadas na segunda coluna e assinale a alternativa que contém a sequência correta.**

[Figura do gabarito, p. 18 (não está no caderno; a mesma ideia está no slide p. 47): o mesmo arquivo de 4 blocos num disco de 20 blocos (0–19). Contígua: blocos 6, 7, 8, 9 — "diretório: início = 6, tamanho = 4 · acesso direto: bloco = 6 + i · sofre fragmentação externa". Encadeada: blocos 2 → 8 → 15 → 18 — "diretório: início = 2, fim = 18 · acesso direto exige percorrer a cadeia". Indexada: bloco de índice 5 → {2, 8, 15, 18} — "acesso direto eficiente · custa espaço para o índice".]

**Alternativas:**
- **A)** 1 – 2 – 3
- **B)** 3 – 1 – 2
- **C)** 2 – 3 – 1
- **D)** 2 – 1 – 3

**Gabarito: D** — _(origem: GABARITO.pdf, p. 2 e p. 18)_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Troca as duas primeiras: atribui à contígua o encadeamento por ponteiros, o que contradiz a contiguidade (o próximo bloco sai por cálculo, não precisa ser armazenado).
- **B) ❌** — Associa a 1ª característica à indexada e a 3ª à encadeada. É plausível porque as duas usam ponteiros; a diferença é onde eles ficam: espalhados nos blocos (encadeada) ou centralizados num bloco de índice (indexada).
- **C) ❌** — Acerta a 1ª e inverte as duas últimas: dá à contígua o bloco de índice e à indexada a contiguidade física. Pega quem não distingue "endereço calculado" de "endereço tabelado".
- **D) ✅** — 1ª (ponteiro em cada bloco, sem fragmentação externa, acesso direto ruim) = **encadeada (2)**; 2ª (blocos sequenciais, cálculo simples, fragmentação externa, crescimento difícil) = **contígua (1)**; 3ª (bloco dedicado com os ponteiros, custo do índice) = **indexada (3)**.

**Diferenças entre versões:** caderno × gabarito: alternativas idênticas, letra D nos dois. Nos slides o tema aparece só como figura (p. 47), sem questão.

**⚠️ Atenção:** na prova a ordem das características (e, portanto, a sequência correta) pode mudar. Associe pelas palavras-chave, não pela posição.

**Conceito-chave para a prova:** "ponteiro em cada bloco" = encadeada (FAT = encadeada com tabela à parte); "blocos sequenciais / cálculo / fragmentação externa" = contígua; "bloco de índice / tabela de ponteiros" = indexada (inode com ponteiros diretos e indiretos; ext4 usa extents). Acesso sequencial e crescimento → encadeada; acesso aleatório → indexada; arquivos que não mudam → contígua.

---

## Q11 — Projeto de armazenamento com journaling
**Fonte:** `SISTEMAS_OPERACIONAIS - QUESTOES.docx`, p. 13 (QUESTÃO 11); gabarito em `SISTEMAS_OPERACIONAIS - GABARITO.pdf`, p. 19. Base teórica em `MATERIAL_EXPLICATIVO.pdf`, p. 46–47 e slide p. 48. Não aparece nos slides como questão.
**Tipo ENADE:** Afirmativas múltiplas (CAT 2), propostas de projeto · Tópico 8 — Projeto de solução de armazenamento, journaling e espaços livres · Domínio: Aplicação

**Enunciado:** (literal, caderno p. 13)

Um hospital vai implantar um servidor Linux para o arquivo de imagens de exames. Os requisitos são: arquivos individuais de 2 GB a 40 GB; leitura frequente de trechos específicos de cada exame, em posições arbitrárias do arquivo; e garantia de que uma queda de energia não deixe o volume em estado inconsistente nem exija horas de verificação para voltar ao ar.

**Com o objetivo de projetar a solução de armazenamento que atenda aos requisitos de desempenho e de integridade descritos, analise as propostas formuladas pela equipe de infraestrutura.**

I. Adotar um sistema de arquivos com journaling, como ext4 ou XFS, atende ao requisito de integridade: o registro prévio das operações em um diário permite que, após uma queda de energia, a recuperação se dê pela reaplicação ou pelo descarte das transações incompletas, dispensando a varredura completa do volume.

II. A alocação indexada é preferível à encadeada para os arquivos de imagem, pois preserva a eficiência do acesso direto a blocos arbitrários, necessária à leitura de regiões específicas de exames de grande porte.

III. A escolha do sistema FAT32 atenderia melhor ao cenário, uma vez que sua tabela de alocação centralizada oferece journaling nativo e comporta arquivos individuais do porte exigido pelos exames.

IV. A gerência de espaços livres por mapa de bits facilita a localização de conjuntos de blocos contíguos, o que é útil para reduzir a fragmentação dos arquivos de grande porte gravados no volume.

**Devem compor a solução apenas as propostas**

**Julgamento das propostas:**
- **I — Correta.** Descreve bem o journaling e o ganho de tempo na recuperação (sem varrer o volume inteiro, sem "horas de verificação"), atendendo ao requisito de integridade.
- **II — Correta.** A leitura de trechos em posições arbitrárias exige localizar qualquer bloco diretamente: alocação indexada (inodes/extents). A encadeada obrigaria percorrer a cadeia.
- **III — Incorreta.** Dois erros graves: o FAT32 **não tem journaling**, e seu limite de **4 GB por arquivo** inviabiliza exames de 2 a 40 GB.
- **IV — Correta.** Mapa de bits = um bit por bloco; fica fácil achar sequências contíguas livres e reduzir a fragmentação de arquivos grandes.

**Alternativas:**
- **A)** I e III.
- **B)** I, II e IV.
- **C)** II e III.
- **D)** I, III e IV.

**Gabarito: B** — _(origem: GABARITO.pdf, p. 2 e p. 19)_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Aceita III (FAT32 sem journaling e limitado a 4 GB) e descarta II e IV, que são corretas.
- **B) ✅** — I, II e IV atendem a integridade, acesso aleatório e gestão de espaço livre; III é a única que não deve entrar.
- **C) ❌** — Inclui III e rejeita I, a solução direta para a integridade. Pega quem pensa só no padrão de acesso e esquece a consistência dos metadados após falha.
- **D) ❌** — O distrator mais atraente: junta duas corretas (I e IV) com a incorreta (III) e exclui II. Atrai quem associa a "tabela de alocação centralizada" do FAT a uma estrutura de índice com as mesmas garantias de um diário.

**Diferenças entre versões:** caderno × gabarito: alternativas idênticas, letra B nos dois. A justificativa do gabarito para IV acrescenta "vantagem que a lista encadeada de blocos livres não oferece", que não está no texto da proposta IV do caderno.

**⚠️ Atenção:** o gabarito está certo. Nuance: no modo padrão do ext4 (data=ordered) só os metadados vão para o diário (apostila p. 47); isso basta para o requisito do caderno ("não deixe o volume em estado inconsistente"). Em versões alteradas, procure as palavras-chave: "queda de energia / integridade" → journaling; "arquivos > 4 GB" → FAT32 eliminado; "posições arbitrárias / acesso aleatório" → indexada; "achar blocos contíguos livres" → mapa de bits.

**Conceito-chave para a prova:** journaling grava a operação no diário ANTES de aplicá-la; recuperação lê só o diário (redo/descartar). ext4 (modos data=ordered padrão, data=journal, data=writeback) e XFS (arquivos muito grandes) têm journaling; NTFS também (com ACL); FAT32 não tem journaling nem permissões e limita arquivos a 4 GB.

---

## Q12 — Técnicas de E/S, spooling, cache e permissões
**Fonte:** `SISTEMAS_OPERACIONAIS - QUESTOES.docx`, p. 14 (QUESTÃO 12); gabarito em `SISTEMAS_OPERACIONAIS - GABARITO.pdf`, p. 20–21 (com figura). Também em `Slides.pdf`, p. 51 (enunciado resumido, "QUESTÃO 5 · ENADE") e p. 52 (gabarito). Citada em `MATERIAL_EXPLICATIVO.pdf`, p. 48 ("a de afirmativa negativa do caderno").
**Tipo ENADE:** Afirmativa negativa — assinale a INCORRETA (CAT 1) · Tópico 9 — Gerência de E/S, DMA, spooling, cache e proteção de recursos · Domínio: Compreensão

**Enunciado:** (literal, caderno p. 14)

Ao revisar a configuração de um servidor que acumula as funções de arquivo e de impressão, um administrador de sistemas elabora um documento técnico com as premissas que orientaram suas decisões sobre o subsistema de entrada e saída. O documento será submetido à validação da equipe de arquitetura, que precisa identificar eventuais premissas equivocadas antes da aprovação.

**Considerando o funcionamento do subsistema de entrada e saída e os mecanismos de proteção de recursos, assinale a alternativa que apresenta uma afirmação INCORRETA.**

**Alternativas:** (iguais no caderno, no gabarito e nos slides)
- **A)** Na E/S por acesso direto à memória (DMA), o controlador transfere blocos inteiros entre o dispositivo e a memória principal e interrompe o processador apenas ao final da transferência, reduzindo a sobrecarga da CPU em relação à E/S por interrupção.
- **B)** O spooling desacopla a aplicação do dispositivo ao gravar a saída em uma área intermediária em disco, permitindo que vários processos submetam trabalhos simultaneamente enquanto um processo servidor os envia à impressora, um de cada vez.
- **C)** O buffer cache mantém em memória principal blocos de disco recentemente acessados e aproveita o princípio da localidade de referência para reduzir o número de acessos físicos ao dispositivo.
- **D)** Em sistemas Linux, as permissões de leitura, escrita e execução aplicadas ao proprietário, ao grupo e aos demais usuários são verificadas pelo núcleo, e o bit de execução em um diretório controla a possibilidade de atravessá-lo para alcançar seu conteúdo.
- **E)** Na E/S programada por polling, o processador delega ao controlador o controle completo da transferência e permanece livre para executar outros processos, sendo por isso a técnica mais eficiente para dispositivos de alta taxa de transferência.

[Figura do gabarito, p. 20 (não está no caderno): três caixas. E/S PROGRAMADA (polling) — "a CPU fica 100% presa durante toda a transferência": a CPU escreve o comando e fica em espera ocupada, testando o registrador de status em laço, e transfere byte a byte, ela mesma. E/S POR INTERRUPÇÃO — "libera a CPU entre os eventos, mas uma interrupção por byte": a CPU dispara a operação e vai executar outro processo; o controlador interrompe a cada byte/palavra pronta; a CPU move o dado do controlador para a memória. E/S POR DMA — "menor sobrecarga — indispensável em disco e rede": a CPU programa o controlador de DMA (endereço, contagem); o DMA transfere o bloco INTEIRO direto para a memória; só ao final gera UMA interrupção.]

**Gabarito: E** (nas três fontes) — _(origem: GABARITO.pdf p. 2 e 21; Slides p. 52)_

**Por que cada alternativa está certa ou errada** (o comando pede a INCORRETA):
- **A) ❌ (afirmação correta, não é a resposta)** — Definição exata do DMA: uma interrupção por bloco, em vez de uma por byte/palavra.
- **B) ❌ (afirmação correta)** — Descreve fielmente o spooling: fila em disco que torna um dispositivo dedicado (impressora) utilizável de forma concorrente; um daemon envia um trabalho por vez.
- **C) ❌ (afirmação correta)** — Buffer cache de disco, fundamentado na localidade de referência.
- **D) ❌ (afirmação correta)** — O núcleo verifica as permissões rwx (dono/grupo/outros); em diretório, x = atravessar e r = listar.
- **E) ✅ (é a afirmação INCORRETA → gabarito)** — O polling faz o oposto: a CPU fica em **espera ocupada**, testando o registrador de status em laço e movendo os dados ela mesma, byte a byte. É a técnica de MAIOR sobrecarga de CPU e a menos indicada para dispositivos rápidos. O texto descreve, na verdade, o DMA.

**Diferenças entre versões:**
- **Caderno × gabarito × slides:** comando e alternativas idênticos; gabarito E nas três fontes. Slides "QUESTÃO 5", caderno "questão 12".
- **Situação-problema dos slides (resumida):** "Ao revisar a configuração de um servidor que acumula as funções de arquivo e de impressão, um administrador **redige** as premissas que orientaram suas decisões sobre o subsistema de entrada e saída. **A equipe de arquitetura precisa identificar premissas equivocadas antes de aprovar o documento.**" O caderno diz "um administrador **de sistemas elabora um documento técnico com** as premissas…" e "**O documento será submetido à validação da** equipe de arquitetura, **que** precisa identificar **eventuais** premissas equivocadas antes **da aprovação**."
- As justificativas do gabarito trazem "CORRETA (e por isso não é a resposta)" para A–D; as dos slides são resumidas.

**Conceito-chave para a prova:** polling = CPU presa 100% (espera ocupada); por interrupção = CPU livre entre eventos, uma interrupção por byte/palavra; DMA = bloco inteiro e UMA interrupção no fim (menor sobrecarga). Buffering = cópia em trânsito; caching = cópia extra para reuso; spooling = fila em disco para dispositivo dedicado. chmod 754 = rwxr-xr--.

---

## E1 — Exercício sugerido de first-fit, best-fit e worst-fit
**Fonte:** `Slides.pdf`, p. 35 (nota de rodapé da resolução da Questão 3 dos slides = Q7 do caderno: "o mesmo mapa é o exercício clássico de Silberschatz (100, 500, 200, 300, 600 KB) — treinem também com pedidos de 417, 112 e 426 KB").
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
