# Redes de Computadores — Questões e Gabarito Comentado

**Squad responsável:** Squad 1 (Guilherme Ayres Camarini, Henrique Martins da Luz, João Pedro Loureiro Lourenço, Leonardo Moraes Culler, Stefano Augusto Rebelo Moretti)

**Materiais analisados:**
| Arquivo | Páginas | Tipo | Questões encontradas (páginas) |
|---|---|---|---|
| `Preparatorio ENADE 2026 - Redes de Computadores.pdf` | 19 | Slides. Só a p. 1 tem texto (nomes dos alunos); as p. 2–19 são imagem e foram todas renderizadas e lidas | Q1–Q5, rotuladas no slide como "Questão 1, 5, 6, 8 e 11" (enunciados nas p. 4, 7, 10, 13, 16; gabarito e análise dos distratores nas p. 5, 8, 11, 14, 17; fundamentação teórica nas p. 3, 6, 9, 12, 15) |
| `Manual de Referencia Redes de Computadores.pdf` | 59 | Apostila (texto) | Q6–Q14, os boxes "Questão comentada (estilo ENADE)" (p. 10, 14, 19, 26, 32, 38, 44, 50, 58 do PDF), e mais 12 exercícios resolvidos ("Estudo de Caso"), E1–E12, no Apêndice (p. 8, 13, 15, 19, 22, 23, 26, 28, 30, 36, 40, 46) |

> Paginação do Manual: cito sempre a página **do PDF**. A página impressa no rodapé é a do PDF menos 1 (ex.: p. 26 do PDF = "Página 25").

**Resumo:** **14 questões objetivas** foram encontradas: 5 nos slides (todas com 4 alternativas, A–D) e 9 no Manual (todas com 5 alternativas, A–E). **As 14 têm gabarito no próprio material**: os slides trazem "Gabarito Oficial e Análise dos Distratores" e o Manual traz "Resposta" com justificativa. **Nenhuma ficou sem gabarito.** Conferi cada gabarito de forma independente, com os cálculos de sub-rede, CIDR, prefixo mais longo e sobrecarga refeitos em Python. **Nenhum gabarito está errado.** Há só pontos de atenção de redação, listados em ⚠️. O Manual tem ainda **12 exercícios resolvidos** (Estudos de Caso, discursivos/de cálculo), transcritos no Apêndice com a resposta esperada. Todos foram conferidos e estão corretos.

> ⚠️ **Possível material incompleto:** nos slides, as questões se chamam "Questão 1", "Questão 5", "Questão 6", "Questão 8" e "Questão 11". As questões 2, 3, 4, 7, 9 e 10 não aparecem no PDF. Pode existir um banco maior de questões do Squad 1 que não foi entregue, ou a numeração segue outro critério que o material não explica.

> Legenda: ✅ correta · ❌ incorreta · ⚠️ ponto de atenção (gabarito do material duvidoso, ambiguidade, versão divergente)

## Índice
**Slides (Preparatório ENADE 2026)**
1. [Q1 — Substituição do equipamento central do laboratório](#q1--substituição-do-equipamento-central-do-laboratório)
2. [Q2 — Encapsulamento TCP-IP e PDUs](#q2--encapsulamento-tcp-ip-e-pdus)
3. [Q3 — Sub-redes /26 e RIP x OSPF](#q3--sub-redes-26-e-rip-x-ospf)
4. [Q4 — Segurança Wi-Fi ameaça x contramedida](#q4--segurança-wi-fi-ameaça-x-contramedida)
5. [Q5 — TCP x UDP em casos de uso](#q5--tcp-x-udp-em-casos-de-uso)

**Manual de Referência (Questões comentadas)**

6. [Q6 — Diagnóstico por camadas OSI](#q6--diagnóstico-por-camadas-osi)
7. [Q7 — Tamanho do quadro e sobrecarga com UDP](#q7--tamanho-do-quadro-e-sobrecarga-com-udp)
8. [Q8 — Troca de hubs por switches](#q8--troca-de-hubs-por-switches)
9. [Q9 — Máscara para no mínimo 500 hosts](#q9--máscara-para-no-mínimo-500-hosts)
10. [Q10 — Casamento do prefixo mais longo](#q10--casamento-do-prefixo-mais-longo)
11. [Q11 — TCP Reno após timeout](#q11--tcp-reno-após-timeout)
12. [Q12 — Protocolos da camada de aplicação](#q12--protocolos-da-camada-de-aplicação)
13. [Q13 — Acesso remoto seguro com VPN](#q13--acesso-remoto-seguro-com-vpn)
14. [Q14 — IoT com sensores de nível de rio](#q14--iot-com-sensores-de-nível-de-rio)

**Apêndice: Estudos de Caso (exercícios resolvidos do Manual)**

15. [E1 — Atraso fim a fim](#e1--atraso-fim-a-fim)
16. [E2 — Eficiência do quadro Ethernet](#e2--eficiência-do-quadro-ethernet)
17. [E3 — Capacidade de Shannon e Nyquist](#e3--capacidade-de-shannon-e-nyquist)
18. [E4 — Contagem de domínios de colisão e broadcast](#e4--contagem-de-domínios-de-colisão-e-broadcast)
19. [E5 — Divisão de /24 em 4 sub-redes](#e5--divisão-de-24-em-4-sub-redes)
20. [E6 — Planejamento VLSM](#e6--planejamento-vlsm)
21. [E7 — Rede de um host com máscara /20](#e7--rede-de-um-host-com-máscara-20)
22. [E8 — Dijkstra a partir do nó u](#e8--dijkstra-a-partir-do-nó-u)
23. [E9 — Cálculo do CRC](#e9--cálculo-do-crc)
24. [E10 — Timeout do TCP](#e10--timeout-do-tcp)
25. [E11 — RTTs para carregar uma página HTTP](#e11--rtts-para-carregar-uma-página-http)
26. [E12 — RSA com números pequenos](#e12--rsa-com-números-pequenos)

---

## Q1 — Substituição do equipamento central do laboratório
**Fonte:** `Preparatorio ENADE 2026 - Redes de Computadores.pdf`, p. 4 (enunciado, slide "ENADE • QUESTÃO 1 (INTERPRETAÇÃO) — Enunciado e Situação-Problema", selo "Versão Íntegra"), p. 5 (gabarito e análise) e p. 3 (fundamentação: "Equipamentos de Interconexão & Domínios de Rede", Tema 3 & Camadas OSI)
**Tipo ENADE:** Interpretação (resposta única, 4 alternativas)

**Enunciado:**

**Dado de Suporte (Texto-Base):** "Os switches segmentam a rede em múltiplos domínios de colisão, estabelecendo um domínio de colisão individual por porta. [...] Diferentemente dos hubs e repetidores, que operam na camada física encaminhando bits para todas as interfaces simultaneamente, um switch opera na camada de enlace filtrando e encaminhando quadros (frames) baseando-se no endereço MAC de destino impresso no cabeçalho. Já os roteadores vão além: operando na camada de rede, eles limitam não apenas os domínios de colisão, mas também os domínios de broadcast, delimitando fronteiras de sub-redes lógicas."
(Fonte: KUROSE, James F.; ROSS, Keith W. Redes de Computadores e a Internet: Uma Abordagem Top-Down. 6ª ed. São Paulo: Pearson Education do Brasil, 2013. p. 331-334. Adaptado.)

**Situação-Problema:** Considere a infraestrutura de rede do laboratório de pesquisas de uma universidade. Atualmente, 50 estações de trabalho estão interconectadas a um único equipamento central "X". O monitoramento de desempenho constatou uma drástica degradação na rede: a taxa de colisões de quadros (acionando constantemente o algoritmo de recuo exponencial do CSMA/CD) chegou a 45% do tráfego total. Preocupada, a direção administrativa sugeriu trocar o equipamento "X" por um "Hub Enterprise Class 1000BASE-T" de uma marca famosa, acreditando intuitivamente que a compra do equipamento mais rápido e caro resolveria o gargalo, independentemente de sua arquitetura lógica. Como requisito técnico inegociável, o administrador de redes definiu que todas as estações de trabalho devem obrigatoriamente permanecer na mesma sub-rede lógica IP (ou seja, no mesmo domínio de broadcast) para não quebrar a comunicação de um software de simulação científica utilizado no laboratório.

**Comando:** Com base no texto de apoio, nos preceitos de arquitetura do Modelo de Referência OSI e exigindo rigor técnico na escolha que rejeite argumentos puramente comerciais, analise o cenário apresentado e avalie qual é a decisão de projeto tecnicamente adequada para substituir o equipamento "X":

**Alternativas:**
- **A)** Substituir o equipamento central por um novo Hub Gigabit Ethernet. Embora opere apenas na Camada Física (L1), o aumento exponencial na velocidade de transmissão isola falhas e reduz o domínio de colisão geral da rede.
- **B)** Substituir o equipamento central por um Switch Ethernet. Operando na Camada de Enlace (L2), este dispositivo encaminha quadros com base no endereço MAC, dividindo a rede em múltiplos domínios de colisão distintos.
- **C)** Substituir o equipamento central por um Roteador de Borda. Operando na Camada de Rede (L3), este equipamento realiza o isolamento de tráfego por endereços IP, mantendo todos obrigatoriamente no mesmo domínio de broadcast.
- **D)** Substituir o equipamento central por uma cascata de novos Hubs. Essa decisão, comercialmente otimizada, garante a vazão de rede sem necessitar de custoso processamento de cabeçalhos lógicos na Camada de Enlace do modelo OSI.

**Gabarito: B** — _(origem: gabarito do próprio material, p. 5, "Alternativa Correta: (B)")_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Um hub, por mais rápido que seja (Gigabit, "Enterprise"), continua sendo camada 1: só repete sinais elétricos para todas as portas. Todas as portas seguem em **um único domínio de colisão**. Velocidade não cria filtragem lógica. A alternativa explora o apelo comercial ("Gigabit", "Enterprise"), que o material chama de falta de rigor na arquitetura L1/L2.
- **B) ✅** — O switch (L2) lê o MAC de destino, consulta a tabela MAC e comuta o quadro só para a porta certa. Cada porta vira um domínio de colisão (são "N" domínios, um por porta), o que elimina as colisões do CSMA/CD. Ao mesmo tempo, o switch **mantém um único domínio de broadcast**, porque quadros FF:FF:FF:FF:FF:FF continuam sendo inundados para todas as portas. Assim, as 50 estações continuam na mesma sub-rede IP, que é o requisito inegociável.
- **C) ❌** — O roteador de fato opera na L3 e isola colisões. O erro está em dizer que ele "mantém todos obrigatoriamente no mesmo domínio de broadcast": roteadores **segmentam e bloqueiam broadcast**, e cada interface é uma sub-rede IP distinta. Essa escolha violaria o requisito do administrador.
- **D) ❌** — Hubs em cascata não resolvem o problema; pioram. Em redes CSMA/CD de camada 1, mais hubs **aumentam o domínio de colisão** e o tempo de propagação, gerando mais colisões e detecções tardias. "Comercialmente otimizada" é a armadilha.

**⚠️ Atenção:** a questão tem só 4 alternativas (A–D), e o ENADE usa 5. Além disso, as alternativas já trazem parte da justificativa. Numa versão alterada, espere uma 5ª alternativa (por exemplo, "switch de camada 3 com VLANs separadas" ou "repetidor"). Ela também estaria errada se quebrasse o domínio de broadcast único ou não separasse colisões.

**Questão relacionada:** Q8 (Manual), com o mesmo conceito (troca hub → switch) e outro enunciado.

**Conceito-chave para a prova:** Hub (L1) = 1 domínio de colisão e 1 de broadcast. Switch (L2) = 1 domínio de colisão **por porta** e 1 de broadcast (sem VLAN). Roteador (L3) separa colisão **e** broadcast (um por interface). Se o requisito é "mesma sub-rede/mesmo broadcast" e o problema são colisões, a resposta é o switch.

---

## Q2 — Encapsulamento TCP-IP e PDUs
**Fonte:** `Preparatorio ENADE 2026 - Redes de Computadores.pdf`, p. 7 (enunciado, slide "ENADE • QUESTÃO 5 (ASSOCIAÇÃO) — Enunciado e Mapeamento de Colunas", "Versão Íntegra"), p. 8 (gabarito) e p. 6 (fundamentação: "Modelo TCP/IP, Encapsulamento & PDUs", Tema 2)
**Tipo ENADE:** Associação (4 alternativas)

**Enunciado:**

**Dado de Suporte (Texto-Base):** "À medida que um pacote desce pelas camadas da pilha de protocolos do nó emissor, cada camada adiciona seu próprio cabeçalho ao pacote recebido da camada superior, um processo estrutural conhecido como encapsulamento. [...] A carga útil (payload) de uma camada inferior consiste invariavelmente no pacote inteiro (cabeçalho e dados embutidos) repassado pela camada imediatamente superior. Na recepção, ocorre o processo inverso de desencapsulamento." (KUROSE & ROSS, 2013, p. 34-36. Adaptado.)

**Situação-Problema:** Um analista de segurança da informação está investigando um incidente de vazamento de dados. Ele utiliza um analisador de protocolos (Wireshark) para destrinchar uma requisição HTTP POST interceptada que carrega credenciais em texto claro. Para mapear com precisão onde cada informação trafegou e como ela foi empacotada pelo sistema operacional do invasor, o analista precisa reconstruir mentalmente o percurso de encapsulamento dessa requisição, associando corretamente a ação de inserção de cabeçalhos e as Unidades de Dados de Protocolo (PDUs) às respectivas camadas do modelo TCP/IP.

| Coluna 1: Camadas TCP/IP | Coluna 2: Ações / PDUs |
|---|---|
| 1. Camada de Aplicação | ( ) Anexa o cabeçalho contendo as portas lógicas para garantir o multiplexamento de processos da máquina, formando a PDU chamada Segmento. |
| 2. Camada de Transporte | ( ) Gera a carga útil original, englobando os dados de formulário e o cabeçalho HTTP POST, formando a PDU conhecida como Mensagem. |
| 3. Camada de Internet (ou Rede) | ( ) Insere os endereços físicos (MAC) e o trailer de verificação de erros (FCS), encapsulando os dados na PDU denominada Quadro (Frame). |
| 4. Camada de Acesso à Rede (ou Enlace/Física) | ( ) Adiciona o cabeçalho contendo endereços IP lógicos (origem e destino) para roteamento, formando a PDU chamada Datagrama. |

**Comando:** Aplicando seus conhecimentos sobre encapsulamento e exigindo rigor para não confundir as funções por semelhança de nomenclatura entre os modelos OSI e TCP/IP, assinale a alternativa que apresenta a sequência correta de associação de cima para baixo:

**Alternativas:**
- **A)** A sequência correta de associação é 3, 1, 4, 2. O encapsulamento associa erroneamente as portas lógicas à camada de Internet, a mensagem HTTP à Aplicação, os quadros MAC ao Acesso à Rede e os endereços IP à camada de Transporte.
- **B)** A sequência correta de associação é 4, 1, 3, 2. O encapsulamento associa erroneamente as portas lógicas ao Acesso à Rede, a mensagem HTTP à Aplicação, os quadros MAC à camada de Internet e os endereços IP à camada de Transporte.
- **C)** A sequência correta de associação é 1, 2, 3, 4. O encapsulamento associa erroneamente as portas lógicas à camada de Aplicação, a mensagem HTTP ao Transporte, os quadros MAC à camada de Internet e os endereços IP ao Acesso à Rede.
- **D)** A sequência correta de associação é 2, 1, 4, 3. O encapsulamento associa rigorosamente as portas lógicas à camada de Transporte, a mensagem HTTP à Aplicação, os quadros MAC ao Acesso à Rede e os endereços IP à camada de Internet.

**Gabarito: D** — _(origem: gabarito do próprio material, p. 8, "Alternativa Correta: (D)")_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Inverte Transporte e Internet. Põe as portas de multiplexação (TCP/UDP) na camada de Internet (3) e o endereçamento IP no Transporte (2). O material diz que isso mostra não distinguir roteamento de hosts de multiplexação de aplicações.
- **B) ❌** — Põe as portas no Acesso à Rede (4) e a criação de quadros MAC na camada de Internet (3), confundindo os domínios de roteadores (camada 3) e switches (camada 2).
- **C) ❌** — Inverte Aplicação com Transporte e Internet com Acesso à Rede: a Aplicação criaria o Segmento e o Transporte, a Mensagem HTTP. Isso quebra a ordem lógica da pilha.
- **D) ✅** — Portas lógicas e Segmento → **Transporte (2)**. Dados HTTP POST e Mensagem → **Aplicação (1)**. MAC, FCS e Quadro → **Acesso à Rede (4)**. IP de origem/destino e Datagrama → **Internet (3)**. Sequência **2, 1, 4, 3**.

**⚠️ Atenção:** as alternativas "entregam" o gabarito com as palavras "erroneamente" (A, B, C) e "rigorosamente" (D). Na prova, uma versão alterada provavelmente virá sem esses adjetivos, ou com a ordem dos itens da Coluna 2 embaralhada. Então memorize o mapeamento, e não a sequência numérica. Ela muda conforme a ordem dos itens.

**Questão relacionada:** Q7 (Manual), sobre o cálculo de cabeçalhos/encapsulamento.

**Conceito-chave para a prova:** PDUs no TCP/IP: Aplicação = **Mensagem**, Transporte = **Segmento** (TCP) ou datagrama de usuário (UDP) e contém as **portas**, Internet/Rede = **Datagrama/Pacote** e contém o **IP**, Acesso à Rede/Enlace = **Quadro** e contém o **MAC + FCS** (único trailer), Física = bits.

---

## Q3 — Sub-redes /26 e RIP x OSPF
**Fonte:** `Preparatorio ENADE 2026 - Redes de Computadores.pdf`, p. 10 (enunciado, slide "ENADE • QUESTÃO 6 (ALTERNATIVAS CONSTANTES V/F) — Enunciado e Julgamento de Proposições", "Versão Íntegra"), p. 11 (gabarito) e p. 9 (fundamentação: "Sub-redes CIDR & Protocolos de Roteamento", Temas 4 e 5)
**Tipo ENADE:** Alternativas constantes (julgamento V/F, 4 alternativas)

**Enunciado:**

**Dado de Suporte (Texto-Base):** "O uso de sub-redes (subnetting) permite que um único bloco de endereços IP seja dividido em redes lógicas menores, otimizando o espaço de endereçamento. Para o roteamento entre essas redes, protocolos de estado de enlace (como o OSPF) constroem um mapa topológico completo usando algoritmos de caminho mais curto baseados em métricas de custo (frequentemente associadas à largura de banda), enquanto protocolos de vetor de distâncias (como o RIP clássico) operam iterativamente baseando-se em métricas simples, como a contagem de saltos." (KUROSE & ROSS, 2013, p. 245-255. Adaptado.)

**Situação-Problema:** Um engenheiro de redes recebeu o bloco de endereços IP 192.168.50.0/24 para planejar a infraestrutura de uma organização departamental. O projeto exige a criação de 4 sub-redes iguais e a interligação dessas redes através de roteadores conectados por enlaces com diferentes capacidades de transmissão (10 Mbps, 100 Mbps e 1 Gbps). Durante a revisão do projeto técnico, o estagiário da equipe apresentou quatro afirmações sobre o endereçamento planejado e o protocolo de roteamento a ser adotado.

( ) I. Ao aplicar a máscara de sub-rede /26 (255.255.255.192) ao bloco original, a primeira sub-rede gerada (192.168.50.0) disponibilizará exatos 64 endereços IP válidos para atribuição aos computadores (hosts) dos usuários.

( ) II. Se uma impressora na segunda sub-rede for configurada com o endereço IP 192.168.50.75/26, o endereço IP de destino utilizado para envio de quadros em broadcast restritos exclusivamente à sua sub-rede será o 192.168.50.127.

( ) III. O protocolo RIP (Routing Information Protocol) é o mais recomendado para a topologia de enlaces variáveis descrita, pois seu algoritmo nativo calcula a melhor rota considerando a velocidade (largura de banda) das conexões, otimizando a latência.

( ) IV. Caso a equipe adote o protocolo OSPF, todos os roteadores pertencentes a uma mesma área lógica deverão convergir até possuírem um banco de dados de estado de enlace (LSDB) idêntico, a partir do qual calcularão as rotas.

**Comando:** Aplicando rigor matemático e técnico sobre a arquitetura de protocolos, analise as afirmações do estagiário e classifique cada uma delas como Verdadeira (V) ou Falsa (F): Assinale a alternativa que apresenta a sequência correta de classificação, lida de cima para baixo:

**Cálculo refeito (192.168.50.0/24 → 4 sub-redes iguais):** 2^b ≥ 4 ⇒ b = 2 ⇒ /24 + 2 = **/26** (255.255.255.192). Salto = 256 − 192 = 64. Bits de host = 32 − 26 = 6 ⇒ 2^6 = 64 endereços, dos quais **62 são hosts válidos**.

| Sub-rede | Rede | Hosts válidos | Broadcast |
|---|---|---|---|
| 1 | 192.168.50.0/26 | .1 a .62 | 192.168.50.63 |
| 2 | 192.168.50.64/26 | .65 a .126 | **192.168.50.127** |
| 3 | 192.168.50.128/26 | .129 a .190 | 192.168.50.191 |
| 4 | 192.168.50.192/26 | .193 a .254 | 192.168.50.255 |

192.168.50.75 AND 255.255.255.192 → 75 = 0100 1011; AND 1100 0000 = 0100 0000 = 64 ⇒ rede 192.168.50.64/26, broadcast 192.168.50.127. Conferido com Python (`ipaddress`).

**Julgamento das afirmativas:**
- **I — Falsa.** A /26 tem 64 endereços, mas só **62 são válidos** (2^6 − 2), porque o endereço de rede (.0) e o de broadcast (.63) não podem ser atribuídos. O material diz que "o rigor recusa a afirmação 'quase correta'".
- **II — Verdadeira.** .75 fica na faixa .64–.127 (2ª sub-rede). Somando 63 ao identificador .64, o último endereço, que é o broadcast, é **192.168.50.127**.
- **III — Falsa.** O RIP é vetor de distâncias e usa **só a contagem de saltos** (máx. 15). Ele ignora a largura de banda (10/100/1000 Mbps). Quem usa custo baseado em banda é o OSPF (ou o EIGRP, com métrica composta).
- **IV — Verdadeira.** No estado de enlace (OSPF), cada roteador da área recebe os LSAs por inundação até todos terem **LSDB idêntica**. Depois cada um roda Dijkstra localmente.

Sequência: **F – V – F – V**.

**Alternativas:**
- **A)** A avaliação sequencial correta das proposições analisadas é: V – V – F – F.
- **B)** A avaliação sequencial correta das proposições analisadas é: F – V – F – V.
- **C)** A avaliação sequencial correta das proposições analisadas é: F – F – V – V.
- **D)** A avaliação sequencial correta das proposições analisadas é: V – F – V – F.

**Gabarito: B** — _(origem: gabarito do próprio material, p. 11, "Alternativa Correta: (B)")_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Marca I como V (2^6 = 64 sem descontar rede e broadcast) e IV como F (não entende a LSDB idêntica do OSPF).
- **B) ✅** — F–V–F–V, como mostram o cálculo e o julgamento acima.
- **C) ❌** — Erra II (o material sugere "somar 64 ao 75" em vez de partir do identificador .64) e marca III como V, atribuindo ao RIP a métrica de banda/latência, que é do OSPF/EIGRP.
- **D) ❌** — Inverte quase tudo: não subtrai rede e broadcast (I), erra o broadcast (II), dá ao RIP a análise de enlace (III) e nega ao OSPF o mapa unificado (IV).

**⚠️ Atenção:** a afirmativa II mistura camadas ("endereço IP de destino [...] para envio de **quadros** em broadcast"). Num quadro, o broadcast de camada 2 é o MAC FF:FF:FF:FF:FF:FF. Além disso, o broadcast limitado 255.255.255.255 também não sai da sub-rede local. O endereço que a questão pede é o **broadcast direcionado da sub-rede**, 192.168.50.127, e a intenção do material (II = V) está correta. De qualquer forma, com I = F, III = F e IV = V, a única alternativa compatível é a B. A questão também tem só 4 alternativas.

**Questões relacionadas:** Q9 (Manual, /23 a partir de /16), E5 (192.168.10.0/24 em 4 × /26, mesma conta), E7 (host em /20).

**Conceito-chave para a prova:** hosts válidos = 2^(32−n) − 2. Salto = 256 − octeto da máscara. Rede = IP AND máscara; broadcast = rede + salto − 1. RIP mede **saltos** (máx. 15; 16 = infinito). OSPF usa **custo por banda**, Dijkstra e LSDB idêntica na área. Se o enunciado fala em "enlaces de capacidades diferentes", a resposta é OSPF.

---

## Q4 — Segurança Wi-Fi ameaça x contramedida
**Fonte:** `Preparatorio ENADE 2026 - Redes de Computadores.pdf`, p. 13 (enunciado, slide "ENADE • QUESTÃO 8 (ASSOCIAÇÃO) — Enunciado e Correlação Ameaça vs Solução", "Versão Íntegra"), p. 14 (gabarito) e p. 12 (fundamentação: "Segurança Sem Fio & Mecanismos de Proteção", Tema 8 & Wi-Fi 802.11)
**Tipo ENADE:** Associação (4 alternativas)

**Enunciado:**

**Dado de Suporte (Texto-Base):** "Devido à natureza de difusão de seu meio físico, as redes sem fio são inerentemente mais suscetíveis a interceptações, injeção de pacotes e falsificação de identidade do que as redes cabeadas. Para proteger o ambiente corporativo, arquitetos de rede devem implementar mecanismos de defesa em profundidade: protocolos rigorosos de criptografia garantem a confidencialidade dos dados em trânsito; o controle de acesso baseado em porta (port-based) valida a identidade dos usuários de forma centralizada; enquanto sensores e sistemas de monitoramento contínuo varrem o espectro de radiofrequência para detectar anomalias físicas e operacionais." (STALLINGS, William, 2014, p. 412-416. Adaptado.)

**Situação-Problema:** Após uma auditoria de segurança na infraestrutura wireless de uma grande corporação, a equipe de TI elaborou um relatório com quatro vulnerabilidades críticas e incidentes ocorridos no último semestre. Como engenheiro de redes responsável, você precisa aprovar o plano de ação, correlacionando rigorosamente cada risco identificado com a tecnologia de mitigação técnica apropriada para resolvê-lo.

**Coluna 1: Ameaças / Vulnerabilidades Relatadas**
1. Interceptação passiva: Leitura não autorizada do conteúdo dos quadros de dados (payload) transmitidos pelo ar por usuários legítimos.
2. Ponto de Acesso Clandestino (Rogue AP): Instalação de um roteador doméstico por um funcionário em uma porta de rede cabeada da empresa para criar um acesso Wi-Fi próprio e invisível à TI.
3. Vazamento de credencial global: Ex-colaboradores acessando o estacionamento e conectando-se à rede porque a empresa utiliza uma única senha de rede compartilhada (PSK).
4. Ataque de Deautenticação: Invasor injetando pacotes falsos de controle na rede, fingindo ser o Ponto de Acesso, para forçar a desconexão repetida de usuários legítimos.

**Coluna 2: Mecanismos de Proteção e Contramedidas**
- ( ) Adoção do padrão IEEE 802.1X integrado a um servidor RADIUS para fornecer credenciais exclusivas.
- ( ) Implementação do protocolo AES-CCMP (padrão no WPA2/WPA3) para a carga útil (payload) dos quadros.
- ( ) Ativação do recurso PMF (Protected Management Frames, padrão IEEE 802.11w) na controladora.
- ( ) Implantação de um WIPS (Wireless Intrusion Prevention System) nos Pontos de Acesso em modo monitor.

**Comando:** Exigindo rigor técnico ao associar a contramedida correta ao vetor do ataque, assinale a alternativa que apresenta a sequência correta de associação da Coluna 2, lida de cima para baixo:

**Alternativas:**
- **A)** A sequência correta de associação é 1, 3, 2, 4. Esta associação sugere erroneamente que o 802.1X atua como um cifrador contra a interceptação de pacotes de dados, e que o AES-CCMP tem como função primária revogar o acesso de ex-funcionários.
- **B)** A sequência correta de associação é 2, 4, 1, 3. Esta associação falha tecnicamente ao propor que o servidor 802.1X localiza roteadores clandestinos (Rogue APs), e que o recurso PMF serve para mitigar o vazamento da senha global.
- **C)** A sequência correta de associação é 3, 1, 4, 2. O 802.1X barra as PSKs provendo credenciais únicas; o AES-CCMP criptografa os dados contra interceptação; o PMF assina quadros contra deautenticação; e o WIPS rastreia transmissores físicos não autorizados.
- **D)** A sequência correta de associação é 4, 2, 3, 1. Esta associação inverte a arquitetura ao indicar que o 802.1X é a tecnologia usada para impedir injeção de pacotes de gerência, e que o WIPS funciona como o algoritmo de criptografia da rede.

**Gabarito: C** — _(origem: gabarito do próprio material, p. 14, "Alternativa Correta: (C)")_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Confunde a finalidade do 802.1X, que é framework de controle de acesso/autenticação e não criptografa o tráfego. Também ignora que a falha de identidade dos ex-funcionários (3) não se resolve com AES, e sim eliminando a senha compartilhada.
- **B) ❌** — Atribui ao 802.1X/RADIUS a busca por hardware clandestino (Rogue AP), que depende da análise do espectro pelo WIPS. Também troca a função do PMF, que atua sobre quadros de gerência e não sobre gestão de identidade.
- **C) ✅** — **802.1X + RADIUS → 3**: no WPA-Enterprise, cada usuário tem login próprio, revogável quando ele sai, e acaba a PSK global. **AES-CCMP → 1**: cifra o payload em voo contra sniffing. **PMF (802.11w) → 4**: dá integridade/autenticidade aos quadros de gerência e impede deautenticação forjada. **WIPS → 2**: monitora a RF continuamente e detecta e contém Rogue APs. Sequência **3, 1, 4, 2**.
- **D) ❌** — Diz que o 802.1X bloqueia injeção de quadros de controle (papel do PMF) e põe o WIPS como proteção contra leitura passiva do payload (papel da cifra CCMP).

**⚠️ Atenção:** o texto da alternativa B não bate com a própria sequência. Lendo 2, 4, 1, 3, o PMF fica ligado ao item **1** (interceptação passiva) e o WIPS ao item **3** (vazamento da senha). A frase da alternativa, e a análise do material na p. 14, dizem que o PMF mitigaria o "vazamento da senha global". Isso não muda o gabarito (C), mas mostra que a numeração e a frase de B estão inconsistentes. Outro detalhe técnico: um 802.1X aplicado também às **portas cabeadas** do switch impediria que o roteador doméstico (item 2) fosse ligado à rede. Na associação 1-para-1 da questão, porém, o 802.1X é o único que resolve o item 3, e o WIPS é a resposta esperada para o Rogue AP. A questão também tem só 4 alternativas.

**Questão relacionada:** Q13 (Manual, segurança/VPN). O Manual, seção 9.2.4 (p. 52), também trata de WPA2 (AES-CCMP), WPA3 (SAE) e 802.1X/RADIUS (eduroam).

**Conceito-chave para a prova:** confidencialidade do payload Wi-Fi = **AES-CCMP** (WPA2/WPA3). Fim da senha compartilhada/identidade individual = **802.1X + RADIUS** (modo Enterprise). Deautenticação forjada = **PMF/802.11w**. Rogue AP = **WIPS** (APs em modo monitor). WPA3-Personal usa SAE contra ataque de dicionário offline.

---

## Q5 — TCP x UDP em casos de uso
**Fonte:** `Preparatorio ENADE 2026 - Redes de Computadores.pdf`, p. 16 (enunciado, slide "ENADE • QUESTÃO 11 (AFIRMATIVAS MÚLTIPLAS) — Enunciado e Análise de Casos de Uso", "Versão Íntegra"), p. 17 (gabarito) e p. 15 (fundamentação: "Camada de Transporte: TCP vs UDP", Tema 6)
**Tipo ENADE:** Afirmativas múltiplas (4 alternativas)

**Enunciado:**

**Dado de Suporte (Texto-Base):** "O UDP tira proveito da ausência de mecanismos de estabelecimento de conexão e de manutenção de estado para transmitir dados de forma ágil, transferindo o controle para a camada de aplicação quando necessário. Já o TCP fornece um serviço de transferência de dados confiável e orientado à conexão, garantindo a entrega exata, em ordem, e implementando mecanismos complexos de controle de fluxo e de congestionamento. Contudo, essa confiabilidade ocorre à custa de uma maior sobrecarga (overhead) e de atrasos pontuais impostos pelas retransmissões." (KUROSE & ROSS, 2013, p. 153-155. Adaptado.)

**Situação-Problema:** Uma startup de desenvolvimento de software está projetando a arquitetura de rede para três novos produtos: um aplicativo de transferência segura de arquivos corporativos, um jogo on-line de tiro em primeira pessoa (FPS) competitivo, e um sistema de streaming de vídeo ao vivo (tempo real). Durante a reunião de engenharia de software, a equipe precisou julgar as características dos protocolos de transporte para definir qual utilizar em cada aplicação.

I. Para a transferência de arquivos, o uso do TCP é essencial, pois a aplicação não tolera a corrupção ou perda de bytes, dependendo dos números de sequência e das confirmações (ACKs) do TCP para garantir a remontagem íntegra dos dados no destino.

II. No desenvolvimento do jogo on-line (FPS), o TCP deve ser escolhido obrigatoriamente porque o seu mecanismo de controle de congestionamento estabiliza o envio de dados na rede, reduzindo a latência (ping) e evitando engasgos (lag) na partida.

III. No streaming de vídeo ao vivo, o UDP é frequentemente preferido, pois a perda ocasional de pacotes (gerando uma leve falha visual passageira) é mais tolerável do que o atraso na reprodução causado pelas retransmissões obrigatórias do TCP.

IV. Em redes com alta taxa de perda de pacotes no meio físico (como redes sem fio ruidosas), o TCP sempre apresentará maior velocidade e eficiência que o UDP, pois ele recupera os dados perdidos sem alterar a sua taxa de transmissão.

**Comando:** Analisando e avaliando rigorosamente a veracidade das características técnicas de funcionamento da camada de transporte para aplicações do mundo real, assinale a alternativa correta:

**Julgamento das afirmativas:**
- **I — Verdadeira.** Transferência de arquivos exige 100% de integridade. Números de sequência, ACKs e retransmissões do TCP garantem entrega completa e ordenada.
- **II — Falsa.** O TCP não "reduz o ping". Numa perda, ele obriga a esperar a retransmissão, e o *head-of-line blocking* aumenta latência e jitter. Em jogos FPS, o estado mais recente (coordenadas via UDP) vale mais que um pacote antigo entregue íntegro e atrasado.
- **III — Verdadeira.** Em tempo real, uma perda ocasional (falha visual passageira) é melhor que congelar o vídeo esperando retransmissão.
- **IV — Falsa.** O TCP interpreta perda (inclusive por ruído do meio sem fio) como **congestionamento** e reduz a janela (cwnd), derrubando a vazão. Ele altera a taxa, sim, e "sempre" é generalização falsa.

**Alternativas:**
- **A)** Estão corretas apenas as afirmativas I e III, compreendendo que o TCP garante integridade para arquivos e o UDP evita o atraso de retransmissões no streaming.
- **B)** Estão corretas apenas as afirmativas II e IV, assumindo erroneamente que os algoritmos de controle de congestionamento do TCP diminuem a latência e ignoram erros físicos.
- **C)** Estão corretas apenas as afirmativas I, II e III, julgando, de forma precipitada, que ambos os protocolos de transporte garantem a redução do tempo de resposta em jogos on-line.
- **D)** Estão corretas apenas as afirmativas II, III e IV, avaliando que o UDP se adapta a qualquer cenário, mas falhando ao superestimar o desempenho prático do TCP em enlaces sem fio.

**Gabarito: A** — _(origem: gabarito do próprio material, p. 17, "Alternativa Correta: (A)")_

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — Só I e III são verdadeiras. O material destaca a atitude de recusar generalizações como "o TCP é sempre melhor".
- **B) ❌** — II e IV são justamente as falsas: o TCP aumenta o lag ao esperar retransmissões e reduz a janela em redes sem fio com perdas.
- **C) ❌** — Inclui II. O excesso de overhead, o handshake e a ordenação estrita do TCP introduzem jitter inaceitável em jogos rápidos.
- **D) ❌** — Valida II e IV (falsas) e descarta I (verdadeira). Ignora a finalidade primária do TCP e cai na crença de que confiabilidade = velocidade em meios ruins, esquecendo partida lenta e controle de congestionamento.

**⚠️ Atenção:** nas alternativas, o próprio texto explicativo ("assumindo erroneamente", "de forma precipitada") indica as erradas, e a questão tem só 4 alternativas. Na versão de prova esses comentários devem sumir. Nuance real: plataformas de streaming "sob demanda/ao vivo" via HTTP (HLS/DASH) usam TCP. Para **tempo real interativo** (RTP/WebRTC, VoIP), o UDP é o preferido, e é isso que a afirmativa III pede.

**Questão relacionada:** Q11 (Manual, TCP Reno). Tabela 18 do Manual (p. 38): TCP × UDP.

**Conceito-chave para a prova:** TCP = conexão (3 vias), confiável, ordenado, controle de fluxo (rwnd) e de congestionamento (cwnd). Usado em arquivos, web, e-mail, SSH. UDP = sem conexão, cabeçalho de 8 bytes, sem retransmissão. Usado em DNS, VoIP, jogos, streaming em tempo real, DHCP, QUIC. Perda em Wi-Fi faz o TCP reduzir a taxa.

---

## Q6 — Diagnóstico por camadas OSI
**Fonte:** `Manual de Referencia Redes de Computadores.pdf`, p. 10 (impressa 9), seção 1.6.3, box "Questão comentada (estilo ENADE)"
**Tipo ENADE:** Resposta única (5 alternativas)

**Enunciado:**
Um técnico percebe que dois computadores da mesma sala não se comunicam. O LED da placa de rede de um deles está apagado. Em seguida, após trocar o cabo, os computadores se enxergam, mas o navegador ainda não abre um site pelo nome, apenas pelo endereço IP. Assinale a alternativa que indica, respectivamente, as camadas OSI dos dois problemas.

**Alternativas:**
- **A)** Enlace e Rede
- **B)** Física e Aplicação
- **C)** Física e Transporte
- **D)** Rede e Sessão
- **E)** Enlace e Apresentação

**Gabarito: B** — _(origem: resposta do próprio material, p. 10)_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — "Pegadinha comum", segundo o material: o cabo não é "enlace", e sim meio físico. E o segundo problema não é de rede, porque o acesso por IP funciona, logo o roteamento está OK.
- **B) ✅** — O LED apagado, resolvido com a troca do cabo, indica falha de **sinal/meio, camada física (1)**. Abrir o site pelo IP e não pelo nome indica falha na **resolução de nomes (DNS)**, que é protocolo da **camada de aplicação (7)**.
- **C) ❌** — A primeira camada está certa, mas o transporte funciona: a conexão TCP ao site pelo IP é estabelecida.
- **D) ❌** — A camada de rede funciona (há alcance por IP), e o DNS não é protocolo de sessão.
- **E) ❌** — O cabo é camada 1, não 2. O DNS é aplicação, não apresentação (apresentação = codificação, compressão, criptografia).

**Conceito-chave para a prova:** sintoma físico (LED, cabo, conector, sinal) = camada 1. "Funciona pelo IP, mas não pelo nome" = DNS = camada de aplicação. Se o "ping pelo IP" funciona, as camadas 1–3 estão OK.

---

## Q7 — Tamanho do quadro e sobrecarga com UDP
**Fonte:** `Manual de Referencia Redes de Computadores.pdf`, p. 14 (impressa 13), seção 2.5, box "Questão comentada (estilo ENADE)"
**Tipo ENADE:** Resposta única, com cálculo (5 alternativas)

**Enunciado:**
Uma aplicação envia 200 bytes de dados usando UDP sobre IPv4 sem opções, em um enlace Ethernet. Considerando os cabeçalhos de transporte, de rede e de enlace (14 bytes), além do trailer FCS (4 bytes), o tamanho do quadro e a porcentagem de sobrecarga são, aproximadamente:

**Alternativas:**
- **A)** 228 bytes e 12,3%
- **B)** 246 bytes e 18,7%
- **C)** 242 bytes e 17,4%
- **D)** 258 bytes e 22,5%
- **E)** 238 bytes e 16,0%

**Gabarito: B** — _(origem: resposta do próprio material, p. 14)_

**Cálculo refeito:** UDP = 8 bytes, IPv4 sem opções = 20 bytes, Ethernet = 14 bytes, FCS = 4 bytes. Quadro = 14 + 20 + 8 + 200 + 4 = **246 bytes**. Sobrecarga = (14 + 20 + 8 + 4) / 246 = 46/246 = 0,18699 ≈ **18,7%**.

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — 228 = 200 + 20 + 8. Só os cabeçalhos de rede e transporte, sem Ethernet e FCS. 28/228 = 12,3%.
- **B) ✅** — 246 bytes; 46/246 ≈ 18,7%.
- **C) ❌** — 242 = 246 − 4. Esquece o FCS. 42/242 = 17,4%.
- **D) ❌** — 258 = 14 + 20 + **20** + 200 + 4. Usa o cabeçalho TCP (20 bytes) no lugar do UDP. 58/258 = 22,5%.
- **E) ❌** — 238 = 14 + 20 + 200 + 4. Esquece o cabeçalho UDP. 38/238 = 16,0%. O material não comenta esta alternativa; a dedução é minha.

**⚠️ Atenção:** a sobrecarga é calculada sobre o **total do quadro** (46/246). Uma versão alterada pode pedir a sobrecarga sobre os dados (46/200 = 23%), a eficiência (200/246 ≈ 81,3%) ou incluir preâmbulo/SFD (8 bytes) e IFG (12 bytes), como no Estudo de Caso E2. Leia o que o enunciado considera.

**Questão relacionada:** Q2 (slides, encapsulamento) e E2 (eficiência TCP/IPv4/Ethernet).

**Conceito-chave para a prova:** cabeçalhos mínimos: UDP 8 B, TCP 20 B, IPv4 20 B (até 60), IPv6 40 B fixo, Ethernet 14 B + FCS 4 B. Payload Ethernet de 46 a 1500 B (MTU), quadro mínimo de 64 B. MSS padrão = 1500 − 40 = 1460 B.

---

## Q8 — Troca de hubs por switches
**Fonte:** `Manual de Referencia Redes de Computadores.pdf`, p. 19 (impressa 18), seção 3.5.3, box "Questão comentada (estilo ENADE)"
**Tipo ENADE:** Afirmativa incompleta / resposta única (5 alternativas)

**Enunciado:**
Uma rede local com 40 computadores ligados a hubs apresenta lentidão nos horários de pico. O administrador substitui os hubs por switches, sem alterar mais nada. Sobre o efeito dessa troca, é correto afirmar que:

**Alternativas:**
- **A)** o número de domínios de broadcast aumenta, reduzindo o tráfego de ARP.
- **B)** o número de domínios de colisão aumenta, e cada porta passa a poder operar em full-duplex.
- **C)** os computadores passam a estar em redes IP diferentes.
- **D)** o tráfego de broadcast deixa de ser propagado.
- **E)** não há mudança de desempenho, pois ambos operam na camada 2.

**Gabarito: B** — _(origem: resposta do próprio material, p. 19)_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — O switch (sem VLAN) **não** separa broadcast. Continua 1 domínio de broadcast, e o ARP request continua chegando a todos.
- **B) ✅** — O switch cria **um domínio de colisão por porta** e permite **full-duplex**, eliminando colisões.
- **C) ❌** — O switch não altera o endereçamento IP. Só um roteador (ou VLANs + L3) separaria redes IP.
- **D) ❌** — Broadcasts (FF:FF:FF:FF:FF:FF) continuam inundados para todas as portas.
- **E) ❌** — O hub é camada **1**, não 2. Há ganho de desempenho, sim.

**Questão relacionada:** Q1 (slides). O conceito é o mesmo, mas Q1 exige ainda o requisito "mesmo domínio de broadcast" e descarta o roteador. Ver também E4 (contagem de domínios).

**Conceito-chave para a prova:** troca hub → switch: domínios de colisão aumentam (1 por porta), domínio de broadcast continua 1, half-duplex → full-duplex, IP inalterado.

---

## Q9 — Máscara para no mínimo 500 hosts
**Fonte:** `Manual de Referencia Redes de Computadores.pdf`, p. 26 (impressa 25), fim da seção 4.6, box "Questão comentada (estilo ENADE)"
**Tipo ENADE:** Resposta única, com cálculo (5 alternativas)

**Enunciado:**
Um administrador precisa dividir a rede 10.20.0.0/16 de forma que cada sub-rede comporte pelo menos 500 hosts, maximizando o número de sub-redes. Qual máscara deve ser usada e quantas sub-redes serão obtidas?

**Alternativas:**
- **A)** /23 e 128 sub-redes
- **B)** /24 e 256 sub-redes
- **C)** /22 e 64 sub-redes
- **D)** /23 e 64 sub-redes
- **E)** /25 e 512 sub-redes

**Gabarito: A** — _(origem: resposta do próprio material, p. 26)_

**Cálculo refeito (conferido em Python):**

| Máscara | Bits de host h | Hosts válidos (2^h − 2) | Bits emprestados (n − 16) | Sub-redes (2^b) | Atende ≥ 500? |
|---|---|---|---|---|---|
| /22 | 10 | 1022 | 6 | 64 | Sim, mas não maximiza |
| **/23** | **9** | **510** | **7** | **128** | **Sim (máximo de sub-redes)** |
| /24 | 8 | 254 | 8 | 256 | Não |
| /25 | 7 | 126 | 9 | 512 | Não |

2^h − 2 ≥ 500 ⇒ h = 9 (2^9 − 2 = 510; h = 8 daria 254). Máscara = 32 − 9 = **/23** (255.255.254.0). Bits emprestados = 23 − 16 = 7 ⇒ 2^7 = **128 sub-redes** (10.20.0.0/23, 10.20.2.0/23, ..., 10.20.254.0/23).

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — /23 é a maior máscara (menor sub-rede) que comporta 500 hosts (510). Dá 128 sub-redes.
- **B) ❌** — /24 comporta só 254 hosts por sub-rede.
- **C) ❌** — /22 atende (1022 hosts), mas gera só 64 sub-redes, sem maximizar.
- **D) ❌** — A máscara está certa, mas a contagem está errada: 7 bits emprestados dão 128, não 64. O 64 corresponde ao /22.
- **E) ❌** — /25 comporta só 126 hosts.

**Questões relacionadas:** Q3 (slides), E5, E6, E7.

**Conceito-chave para a prova:** escolha h pelo **número de hosts** (2^h − 2 ≥ N) e depois conte as sub-redes por **bits emprestados em relação à rede original** (2^(n_novo − n_original)). "Maximizar sub-redes" = menor h que atende.

---

## Q10 — Casamento do prefixo mais longo
**Fonte:** `Manual de Referencia Redes de Computadores.pdf`, p. 32 (impressa 31), fim da seção 5.4, box "Questão comentada (estilo ENADE)"
**Tipo ENADE:** Resposta única (5 alternativas)

**Enunciado:**
Um roteador possui as seguintes rotas: 10.0.0.0/8 → R1; 10.1.0.0/16 → R2; 10.1.2.0/24 → R3; 0.0.0.0/0 → R4. Os pacotes destinados a 10.1.2.9, 10.1.5.7 e 172.16.0.1 serão enviados, respectivamente, para:

**Alternativas:**
- **A)** R1, R1 e R4
- **B)** R3, R2 e R4
- **C)** R3, R2 e R1
- **D)** R2, R2 e R4
- **E)** R3, R1 e R4

**Gabarito: B** — _(origem: resposta do próprio material, p. 32)_

**Cálculo refeito (conferido em Python):**

| Destino | Casa com | Vence (mais longo) |
|---|---|---|
| 10.1.2.9 | /8, /16, /24, /0 | 10.1.2.0/24 → **R3** |
| 10.1.5.7 | /8, /16, /0 (não está em 10.1.2.0/24) | 10.1.0.0/16 → **R2** |
| 172.16.0.1 | só /0 | 0.0.0.0/0 → **R4** |

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Erro de escolher a primeira rota que casa (a menos específica, /8), e não a mais longa.
- **B) ✅** — R3, R2, R4 pela regra do prefixo mais longo.
- **C) ❌** — 172.16.0.1 não pertence a 10.0.0.0/8. Só casa a rota padrão (R4).
- **D) ❌** — Ignora a /24 para 10.1.2.9, que é mais específica que a /16.
- **E) ❌** — 10.1.5.7 está em 10.1.0.0/16, mais específica que a /8.

**Conceito-chave para a prova:** *longest prefix match*: entre as rotas que casam, vence a de **maior máscara**. A rota padrão 0.0.0.0/0 casa com tudo e só é usada se nada mais casar. O Manual (Tabela 14, p. 27) tem exemplo análogo: 200.23.22.161 → /21 (interface 0), 200.23.24.170 → /24 (interface 1), 8.8.8.8 → padrão (interface 3). Conferido.

---

## Q11 — TCP Reno após timeout
**Fonte:** `Manual de Referencia Redes de Computadores.pdf`, p. 38 (impressa 37), seção 6.6, box "Questão comentada (estilo ENADE)"
**Tipo ENADE:** Resposta única (5 alternativas)

**Enunciado:**
Uma conexão TCP opera com cwnd = 20 MSS e ssthresh = 32 MSS quando o transmissor detecta um *timeout*. Considerando o TCP Reno, após o evento os valores de cwnd e ssthresh serão, respectivamente:

**Alternativas:**
- **A)** 10 MSS e 20 MSS
- **B)** 1 MSS e 10 MSS
- **C)** 1 MSS e 16 MSS
- **D)** 10 MSS e 10 MSS
- **E)** 20 MSS e 32 MSS

**Gabarito: B** — _(origem: resposta do próprio material, p. 38)_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Divide a cwnd por 2 e põe o ssthresh igual à cwnd antiga. Não é nenhuma reação do Reno.
- **B) ✅** — Em qualquer perda, o novo ssthresh = cwnd **atual**/2 = 20/2 = **10 MSS**. Como foi **timeout**, a cwnd volta a **1 MSS** e recomeça a partida lenta.
- **C) ❌** — Usa a metade do **ssthresh anterior** (32/2 = 16), e não a metade da cwnd.
- **D) ❌** — 10 e 10 seria a reação a **3 ACKs duplicados** (cwnd cai pela metade).
- **E) ❌** — Nada muda, o que ignora o evento de perda.

**⚠️ Atenção (não altera o gabarito):** no Reno "de livro", após 3 ACKs duplicados a cwnd vai para ssthresh + 3 MSS (= 13) durante a recuperação rápida e só depois "desinfla" para ssthresh (= 10). O Manual simplifica para "cwnd cai pela metade" (10). Se uma versão alterada trouxer "13 MSS e 10 MSS" para o caso de 3 ACKs duplicados, essa é a forma estrita do Kurose.

**Questão relacionada:** Q5 (slides, TCP × UDP). A Figura 14 do Manual (p. 37) traz o dente de serra: ssthresh inicial 16; na rodada 11, cwnd 22 com 3 ACKs dup. → 11; na rodada 16, cwnd 15 com timeout → ssthresh 7 e cwnd 1.

**Conceito-chave para a prova:** perda ⇒ ssthresh = cwnd/2 (sempre a cwnd atual). Timeout ⇒ cwnd = 1 MSS (partida lenta). 3 ACKs duplicados ⇒ cwnd ≈ cwnd/2 (AIMD). Abaixo do ssthresh o crescimento é exponencial (dobra por RTT); acima, linear (+1 MSS por RTT).

---

## Q12 — Protocolos da camada de aplicação
**Fonte:** `Manual de Referencia Redes de Computadores.pdf`, p. 44 (impressa 43), seção 7.6, box "Questão comentada (estilo ENADE)"
**Tipo ENADE:** Afirmativas múltiplas (5 alternativas)

**Enunciado:**
Sobre protocolos da camada de aplicação, avalie as afirmações:

I. O HTTP é um protocolo sem estado; por isso, aplicações web usam cookies para manter sessões de usuário.

II. O FTP envia comandos e dados pela mesma conexão TCP, na porta 21.

III. Consultas DNS normalmente usam UDP porque são pequenas e o custo de estabelecer conexão seria proporcionalmente alto.

IV. O SMTP é usado tanto para enviar quanto para ler mensagens da caixa postal do destinatário.

É correto apenas o que se afirma em:

**Julgamento das afirmativas:**
- **I — Verdadeira.** O HTTP é *stateless*. Cookies (Set-Cookie/Cookie) mantêm sessões, carrinhos e login.
- **II — Falsa.** O FTP usa **duas conexões**: controle na porta 21, sempre aberta e "fora da banda", e dados em conexão separada (porta 20 no modo ativo ou porta alta no passivo).
- **III — Verdadeira.** O DNS usa principalmente UDP/53 (consultas pequenas, sem custo de handshake). O TCP fica para respostas grandes e transferência de zona, por isso o "normalmente".
- **IV — Falsa.** O SMTP é protocolo de **envio (push)**. A leitura usa IMAP, POP3 ou HTTPS (webmail), que são protocolos de puxar (pull).

**Alternativas:**
- **A)** I e II
- **B)** I e III
- **C)** II e IV
- **D)** I, III e IV
- **E)** II, III e IV

**Gabarito: B** — _(origem: resposta do próprio material, p. 44)_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Inclui II, que é falsa.
- **B) ✅** — Só I e III são verdadeiras.
- **C) ❌** — II e IV são as duas falsas.
- **D) ❌** — Inclui IV (SMTP não lê caixa postal).
- **E) ❌** — Inclui II e IV, falsas, e exclui I, verdadeira.

**Conceito-chave para a prova:** HTTP sem estado → cookies. FTP: controle 21 + dados 20/porta alta, com estado de sessão, texto claro (alternativas seguras: FTPS e SFTP/SSH 22). DNS: UDP 53 (TCP para respostas grandes/zona). SMTP: 25/587, só envio. POP3: 110/995. IMAP: 143/993.

---

## Q13 — Acesso remoto seguro com VPN
**Fonte:** `Manual de Referencia Redes de Computadores.pdf`, p. 50 (impressa 49), seção 8.6, box "Questão comentada (estilo ENADE)"
**Tipo ENADE:** Resposta única (5 alternativas)

**Enunciado:**
Uma empresa deseja que seus funcionários acessem, a partir de casa, um sistema interno que não está exposto à Internet, com garantia de confidencialidade e autenticação. Qual solução atende melhor a esse requisito?

**Alternativas:**
- **A)** Publicar o sistema com NAT estático e liberar a porta no firewall.
- **B)** Implantar uma VPN de acesso remoto com autenticação multifator.
- **C)** Usar um IDS na borda da rede.
- **D)** Configurar uma VLAN exclusiva para os funcionários remotos.
- **E)** Trocar o protocolo de aplicação por FTP.

**Gabarito: B** — _(origem: resposta do próprio material, p. 50)_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Expõe o sistema na Internet e não garante confidencialidade nem autenticação forte.
- **B) ✅** — A VPN cria túnel cifrado sobre a Internet (confidencialidade). A autenticação multifator garante que só funcionários legítimos entram.
- **C) ❌** — O IDS só **detecta** e alerta. Não protege nem provê o acesso.
- **D) ❌** — VLAN é segmentação de camada 2 na rede **local**. Não leva o usuário de casa, pela Internet, até a rede interna.
- **E) ❌** — O FTP transmite usuário, senha e dados em **texto claro**.

**Questão relacionada:** Q4 (slides, segurança Wi-Fi).

**Conceito-chave para a prova:** VPN de acesso remoto (usuário individual) × site a site (gateways entre redes). IPsec: AH (integridade, sem sigilo), ESP (sigilo + integridade), IKE (chaves/SAs); modo transporte (host a host) × túnel (gateways, cifra o datagrama inteiro). Alternativas: VPN SSL/TLS (443) e WireGuard.

---

## Q14 — IoT com sensores de nível de rio
**Fonte:** `Manual de Referencia Redes de Computadores.pdf`, p. 58 (impressa 57), seção 9.7.3, box "Questão comentada (estilo ENADE)"
**Tipo ENADE:** Resposta única (5 alternativas)

**Enunciado:**
Uma prefeitura quer instalar centenas de sensores de nível de rio espalhados por vários quilômetros, alimentados por bateria, que enviam uma leitura de poucos bytes a cada 5 minutos. A combinação de tecnologias mais adequada é:

**Alternativas:**
- **A)** Wi-Fi 6 e HTTP/2
- **B)** LoRaWAN e MQTT
- **C)** Bluetooth Low Energy e FTP
- **D)** 5G mmWave e SMTP
- **E)** Fibra óptica e HTTP/3

**Gabarito: B** — _(origem: resposta do próprio material, p. 58)_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Wi-Fi tem alcance de dezenas de metros e consumo alto para bateria. HTTP/2 é pesado para dispositivos limitados.
- **B) ✅** — Longo alcance (km), baixíssimo consumo e poucos dados formam o perfil de **LPWAN (LoRaWAN)**. O **MQTT** é leve (cabeçalho mínimo de 2 bytes), do tipo publicar/assinar via broker, ideal para leituras periódicas.
- **C) ❌** — BLE alcança dezenas de metros. FTP é inadequado para telemetria.
- **D) ❌** — 5G em ondas milimétricas tem alcance ainda menor e alto consumo. SMTP é e-mail.
- **E) ❌** — Fibra até centenas de sensores espalhados seria cara e inviável. HTTP/3 é pesado.

**Conceito-chave para a prova:** IoT de longo alcance e baixo consumo = LPWAN (LoRaWAN, NB-IoT, Sigfox); trade-off alcance × taxa × energia. MQTT (pub/sub, TCP, broker, QoS 0/1/2) × CoAP ("HTTP enxuto" sobre UDP). 5G: eMBB, URLLC (~1 ms) e mMTC (até 1 milhão de dispositivos/km²).

---

# Apêndice — Estudos de Caso (exercícios resolvidos do Manual)

> Não são questões objetivas. São exercícios discursivos/de cálculo resolvidos passo a passo no `Manual de Referencia Redes de Computadores.pdf`, nos boxes "Estudo de Caso". Estão aqui porque uma questão de prova pode reaproveitar os mesmos dados. Refiz e conferi todos os cálculos (Python). **Todos estão corretos.**

## E1 — Atraso fim a fim
**Fonte:** Manual, p. 8 (impressa 7), seção 1.4.4, "Estudo de Caso: Cálculo do Atraso Fim a Fim"
**Tipo:** Exercício resolvido (cálculo)

**Enunciado:** Um arquivo é dividido em pacotes de 1.500 bytes. Cada pacote atravessa dois enlaces em série, ligados por um roteador. Os dados são: Enlace 1: taxa R1 = 10 Mbps, comprimento 1.000 km. Enlace 2: taxa R2 = 100 Mbps, comprimento 3.000 km. Velocidade de propagação nos dois meios: s = 2 × 10^8 m/s. Atrasos de processamento e fila desprezíveis.

**Resposta esperada:** L = 1500 × 8 = 12.000 bits. d_trans,1 = 12.000/10×10^6 = 1,2 ms; d_trans,2 = 12.000/100×10^6 = 0,12 ms. d_prop,1 = 10^6 m / 2×10^8 = 5 ms; d_prop,2 = 3×10^6 / 2×10^8 = 15 ms. Total (store-and-forward) = 1,2 + 5 + 0,12 + 15 = **21,32 ms**. Interpretação do material: mesmo sendo 10 vezes mais rápido, o enlace 2 contribui com o maior atraso por ser mais longo. Em WAN, a propagação domina; em LAN, a transmissão.

**Verificação:** ✅ conferido.

**Conceito-chave:** d_nodal = d_proc + d_fila + d_trans + d_prop. d_trans = L/R (não depende da distância). d_prop = d/s (não depende do tamanho).

---

## E2 — Eficiência do quadro Ethernet
**Fonte:** Manual, p. 13 (impressa 12), seção 2.4, "Estudo de Caso: Eficiência de um Quadro Ethernet com TCP/IPv4"
**Tipo:** Exercício resolvido (cálculo)

**Enunciado:** Uma aplicação envia dados por TCP sobre IPv4 e Ethernet, com o tamanho máximo de carga útil do Ethernet (MTU) de 1.500 bytes. Considere cabeçalhos mínimos (sem opções).

**Resposta esperada:** Dados = 1500 − 20 (IPv4) − 20 (TCP) = **1460 bytes (MSS)**. Quadro = 14 + 1500 + 4 = 1518 bytes. Somando preâmbulo + SFD (8) e intervalo entre quadros (12), cada quadro ocupa 1538 bytes. ε = 1460/1538 ≈ **0,949 (94,9%)**. Em 1 Gbps, isso dá ≈ 949 Mbps de dados de aplicação. Com 1 byte de dados, o quadro mínimo é de 64 bytes + 20 = 84, e ε = 1/84 ≈ **1,2%**. Daí o algoritmo de Nagle.

**Verificação:** ✅ conferido (1460/1538 = 0,9493; 1/84 = 0,0119).

**Conceito-chave:** ε = dados úteis / (dados + cabeçalhos + trailers). Observe se o enunciado inclui preâmbulo e IFG.

---

## E3 — Capacidade de Shannon e Nyquist
**Fonte:** Manual, p. 15 (impressa 14), seção 3.1.2, "Estudo de Caso: Capacidade de uma Linha Telefônica"
**Tipo:** Exercício resolvido (cálculo)

**Enunciado:** Uma linha telefônica analógica tem largura de banda de aproximadamente 3.000 Hz e relação sinal-ruído de 30 dB. Qual a capacidade máxima teórica?

**Resposta esperada:** 30 dB = 10·log10(S/N) ⇒ S/N = 10^3 = 1000. Shannon: C = 3000 × log2(1 + 1000) ≈ 3000 × 9,97 ≈ **29,9 kbps**. Níveis pelo Nyquist: 29.900 = 2 × 3000 × log2 V ⇒ log2 V ≈ 4,98 ⇒ **V ≈ 32 níveis**. Por isso o acesso discado "travou" perto de 33,6 kbps.

**Verificação:** ✅ conferido (C = 29.901,7 bps; V = 2^4,98 ≈ 31,6 ≈ 32).

**Conceito-chave:** Nyquist (sem ruído): C = 2B·log2 V. Shannon (com ruído): C = B·log2(1 + S/N), com S/N **linear** (converter de dB: S/N = 10^(dB/10)). 3 dB = metade, 10 dB = 1/10, 20 dB = 1/100.

---

## E4 — Contagem de domínios de colisão e broadcast
**Fonte:** Manual, p. 19 (impressa 18), seção 3.5.3, "Estudo de Caso: Contando Domínios de Colisão e de Broadcast"
**Tipo:** Exercício resolvido

**Enunciado:** Uma empresa tem a seguinte rede: um roteador com duas interfaces LAN. Na interface 1 está ligado um switch de 8 portas, com 5 computadores e um hub (o hub tem 4 computadores ligados). Na interface 2 está ligado outro switch com 6 computadores. Quantos domínios de colisão e de broadcast existem?

**Resposta esperada:** **Broadcast: 2** (um por interface do roteador). **Colisão: 14**. Switch 1: 5 portas com PCs + 1 porta com o hub (o hub e seus 4 PCs formam um único domínio) + 1 porta para o roteador = 7. Switch 2: 6 PCs + 1 porta para o roteador = 7. Observação do material: em full-duplex não há colisão na prática, mas a contagem continua sendo cobrada assim em provas.

**Verificação:** ✅ conferido.

**Conceito-chave:** cada porta de switch em uso = 1 domínio de colisão. Hub inteiro = 1 domínio de colisão. Cada interface de roteador = 1 domínio de broadcast.

---

## E5 — Divisão de /24 em 4 sub-redes
**Fonte:** Manual, p. 22 (impressa 21), seção 4.4.1, "Estudo de Caso 1: Dividindo 192.168.10.0/24 em 4 Sub-redes Iguais"
**Tipo:** Exercício resolvido (sub-redes)

**Enunciado:** Dividir 192.168.10.0/24 em 4 sub-redes iguais.

**Resposta esperada:** 2^b ≥ 4 ⇒ b = 2 ⇒ **/26** (255.255.255.192). Bloco = 2^(32−26) = 64 endereços, 62 hosts.

| Sub-rede | Endereço de rede | Faixa de hosts | Broadcast |
|---|---|---|---|
| 1 | 192.168.10.0/26 | .1 a .62 | 192.168.10.63 |
| 2 | 192.168.10.64/26 | .65 a .126 | 192.168.10.127 |
| 3 | 192.168.10.128/26 | .129 a .190 | 192.168.10.191 |
| 4 | 192.168.10.192/26 | .193 a .254 | 192.168.10.255 |

Na mesma seção, a Tabela 10 (AND de 192.168.10.37 com /26) dá rede **192.168.10.0** e broadcast **192.168.10.63**.

**Verificação:** ✅ conferido (Python `ipaddress`). É a mesma conta da Q3 (slides), só com outro bloco.

---

## E6 — Planejamento VLSM
**Fonte:** Manual, p. 23 (impressa 22), seção 4.4.2, "Estudo de Caso 2: Planejamento VLSM para uma Empresa"
**Tipo:** Exercício resolvido (VLSM)

**Enunciado:** A empresa recebeu o bloco 192.168.1.0/24 e precisa de: Vendas (100 hosts), TI (50 hosts), RH (20 hosts) e um enlace ponto a ponto entre dois roteadores (2 hosts).

**Resposta esperada:** menor máscara por setor (2^h − 2 ≥ necessidade): Vendas 2^7 − 2 = 126 → /25; TI 2^6 − 2 = 62 → /26; RH 2^5 − 2 = 30 → /27; Enlace 2^2 − 2 = 2 → /30. Alocação em ordem decrescente:

| Setor | Máscara | Rede | Hosts utilizáveis | Broadcast |
|---|---|---|---|---|
| Vendas | /25 | 192.168.1.0 | .1 a .126 | .127 |
| TI | /26 | 192.168.1.128 | .129 a .190 | .191 |
| RH | /27 | 192.168.1.192 | .193 a .222 | .223 |
| Enlace WAN | /30 | 192.168.1.224 | .225 a .226 | .227 |
| Livre | – | 192.168.1.228 a 192.168.1.255 (reserva) | | |

Com /25 fixo só caberiam 2 setores. Com VLSM, os 4 cabem e ainda **sobram 28 endereços**.

**Verificação:** ✅ conferido (256 − 228 = 28).

**Conceito-chave:** em VLSM, aloque **as maiores sub-redes primeiro**. Enlace ponto a ponto = /30 (ou /31, RFC 3021). Agregação: 200.10.0.0/24 a 200.10.3.0/24 = 200.10.0.0/22 (também conferido).

---

## E7 — Rede de um host com máscara /20
**Fonte:** Manual, p. 26 (impressa 25), seção 4.6.5, "Estudo de Caso 3: Identificando a Rede de um Host com Máscara Não Trivial"
**Tipo:** Exercício resolvido (sub-redes)

**Enunciado:** Um host tem o endereço 172.16.45.130/20. Determine a rede, o broadcast, a faixa de hosts e a quantidade de hosts utilizáveis.

**Resposta esperada:** /20 = 255.255.240.0, e o octeto "interessante" é o 3º. Salto = 256 − 240 = 16 (redes em 0, 16, 32, 48...). 45 fica entre 32 e 47 ⇒ **Rede 172.16.32.0/20**, **Broadcast 172.16.47.255**, **Faixa 172.16.32.1 a 172.16.47.254**, **Hosts = 2^12 − 2 = 4.094**. Conferência em binário: 45 = 0010 1101 AND 1111 0000 = 0010 0000 = 32.

**Verificação:** ✅ conferido (Python `ipaddress`).

---

## E8 — Dijkstra a partir do nó u
**Fonte:** Manual, p. 28 (impressa 27), seção 5.2.1, Figura 9 e "Estudo de Caso: Executando Dijkstra a partir do Nó u"
**Tipo:** Exercício resolvido (algoritmo)

**Enunciado:** [Figura 9: grafo não direcionado com nós u, v, w, x, y, z e custos: u–v (2), u–w (5), u–x (1), v–w (3), v–x (2), x–w (3), w–y (1), w–z (5), x–y (1), y–z (2).] Executar Dijkstra a partir de u (cada célula = distância, predecessor; "–" = nó já em N').

**Resposta esperada (tabela do material):**

| Passo | N' | D(v),p | D(w),p | D(x),p | D(y),p | D(z),p |
|---|---|---|---|---|---|---|
| 0 | u | 2,u | 5,u | **1,u** | ∞ | ∞ |
| 1 | ux | **2,u** | 4,x | – | 2,x | ∞ |
| 2 | uxv | – | 4,x | – | **2,x** | ∞ |
| 3 | uxvy | – | **3,y** | – | – | 4,y |
| 4 | uxvyw | – | – | – | – | **4,y** |
| 5 | uxvywz | – | – | – | – | – |

No passo 1 há empate entre v e y (ambos 2); o material escolhe v. Custos finais: v = 2, x = 1, y = 2, w = 3, z = 4. Tabela de encaminhamento de u: v pelo enlace (u,v); x, y, w e z pelo enlace (u,x).

**Verificação:** ✅ conferido (Dijkstra em Python: D = {v:2, x:1, y:2, w:3, z:4}; predecessores w←y, z←y, y←x).

**Conceito-chave:** estado de enlace = Dijkstra, O(n²) simples ou O(|E| log n) com heap. Vetor de distâncias = Bellman-Ford distribuído, D_x(y) = min_v {c(x,v) + D_v(y)}, sujeito à contagem ao infinito (mitigada por split horizon, poisoned reverse e hold-down).

---

## E9 — Cálculo do CRC
**Fonte:** Manual, p. 30 (impressa 29), seção 5.4.1, "Estudo de Caso: Calculando o CRC"
**Tipo:** Exercício resolvido (cálculo)

**Enunciado:** Dados D = 101110 e gerador G = 1001 (portanto r = 3). Quais bits de CRC (R) devem ser enviados?

**Resposta esperada:** acrescentar 3 zeros (101110000) e dividir por 1001 com XOR (módulo 2):
```
101110000   <- dados + 3 zeros
1001        <- XOR com G
---------
001010000
  1001      <- XOR com G (alinhado ao primeiro 1)
---------
000011000
    1001
---------
000001010
     1001
---------
000000011   <- resto R = 011
```
**R = 011**. Quadro transmitido: **101110 011**. No receptor, 101110011 ÷ 1001 deve dar resto 0. O CRC com r bits detecta todas as rajadas de até r bits.

**Verificação:** ✅ conferido (resto 011; verificação dá resto 000).

---

## E10 — Timeout do TCP
**Fonte:** Manual, p. 36 (impressa 35), seção 6.5.4, "Estudo de Caso: Calculando o Timeout do TCP"
**Tipo:** Exercício resolvido (cálculo)

**Enunciado:** Situação atual: EstimatedRTT = 100 ms e DevRTT = 10 ms. Chega uma nova medição: SampleRTT = 120 ms. (Fórmulas: DevRTT = (1 − β)·DevRTT + β·|SampleRTT − EstimatedRTT|, com β = 0,25; EstimatedRTT = (1 − α)·EstimatedRTT + α·SampleRTT, com α = 0,125; TimeoutInterval = EstimatedRTT + 4·DevRTT.)

**Resposta esperada:** DevRTT = 0,75 × 10 + 0,25 × |120 − 100| = 7,5 + 5 = **12,5 ms** (com o EstimatedRTT antigo, como manda a RFC 6298). EstimatedRTT = 0,875 × 100 + 0,125 × 120 = **102,5 ms**. TimeoutInterval = 102,5 + 4 × 12,5 = **152,5 ms**. A cada timeout, o intervalo dobra (recuo exponencial).

**Verificação:** ✅ conferido.

---

## E11 — RTTs para carregar uma página HTTP
**Fonte:** Manual, p. 40 (impressa 39), seção 7.2.2, "Estudo de Caso: Tempo para Carregar uma Página"
**Tipo:** Exercício resolvido (cálculo)

**Enunciado:** Uma página tem um arquivo HTML base e 10 imagens pequenas, todas no mesmo servidor. Desconsidere o tempo de transmissão e considere apenas o RTT. Quantos RTTs são necessários em cada caso? (a) Não persistente, sem paralelismo; (b) Persistente, sem paralelismo (sem pipelining); (c) Persistente com paralelismo.

**Resposta esperada:** (a) 2 RTT por objeto (1 de handshake TCP + 1 de requisição/resposta) × 11 objetos = **22 RTT**. (b) 1 de handshake + 1 do HTML + 10 das imagens = **12 RTT**. (c) 1 de handshake + 1 do HTML + 1 para todas as imagens = **3 RTT**. Com RTT = 50 ms, o tempo cai de 1,1 s para 150 ms.

**Verificação:** ✅ conferido (22 × 50 = 1100 ms; 3 × 50 = 150 ms).

**Conceito-chave:** HTTP/1.0 não persistente. HTTP/1.1 persistente. HTTP/2 binário, multiplexado, HPACK (mas com HOL blocking no TCP). HTTP/3 sobre QUIC/UDP, com 1-RTT/0-RTT.

---

## E12 — RSA com números pequenos
**Fonte:** Manual, p. 46 (impressa 45), seção 8.3.2, "Estudo de Caso: RSA com Números Pequenos"
**Tipo:** Exercício resolvido (cálculo)

**Enunciado:** Gerar as chaves RSA com p = 5 e q = 11, escolher e = 3, cifrar m = 8 e decifrar.

**Resposta esperada:** n = 5 × 11 = 55; z = (5 − 1)(11 − 1) = 40; e = 3 (coprimo com 40); d com e·d ≡ 1 (mod 40): 3 × 27 = 81 = 2 × 40 + 1 ⇒ **d = 27**. Chave pública (55, 3); privada (55, 27). Cifrar: c = 8^3 mod 55 = 512 mod 55 = **17**. Decifrar: 17^27 mod 55 = **8**. A segurança vem da dificuldade de fatorar n grande (2.048 bits).

**Verificação:** ✅ conferido (pow(3, −1, 40) = 27; 8^3 mod 55 = 17; 17^27 mod 55 = 8). O exemplo de Diffie-Hellman da Tabela 24 (p. 47) também confere: p = 23, g = 5, a = 6, b = 15 ⇒ A = 8, B = 19, segredo = 2.

**Conceito-chave:** confidencialidade = cifrar com a **pública do destinatário**. Assinatura = cifrar o hash com a **privada do remetente**. Na prática o esquema é híbrido: assimétrica para autenticar e combinar a chave, simétrica (AES-GCM) para os dados (TLS 1.3).
