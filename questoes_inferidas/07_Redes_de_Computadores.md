# Redes de Computadores — Questões INFERIDAS (prováveis questões do banco do squad que não temos)

> ⚠️ **Atenção:** estas questões NÃO constam nos materiais. Foram elaboradas para cobrir os subtópicos do material do
> Squad 1 que não têm questão conhecida, imitando o estilo das questões do squad. Servem para estudo dirigido.
> As questões reais conhecidas estão em `../questoes_por_topico/07_Redes_de_Computadores.md`.

**Base usada:**
- `Preparatorio ENADE 2026 - Redes de Computadores.pdf` (19 p., todas renderizadas e lidas): p. 2 ("Matriz Curricular de Redes de Computadores — 9 Eixos Temáticos", com a descrição de cada tema), p. 3–17 (Questões 1, 5, 6, 8 e 11, cada uma com slide de "Fundamentação Teórica", enunciado "Versão Íntegra" e "Gabarito Oficial e Análise dos Distratores"), p. 18 ("Plano Estratégico": rigor conceitual, precisão operacional, *trade-offs* de protocolos).
- `Manual de Referencia Redes de Computadores.pdf` (59 p.): sumário (p. 2–3), Tabela 1 com os 9 temas da Matriz de Referência (p. 4), capítulos 1 a 9 (p. 5–58), 9 "Questões comentadas" e 12 "Estudos de Caso". **Cito sempre a página do PDF** (a página impressa no rodapé é a do PDF menos 1), como no arquivo de questões conhecidas.
- `Estrutura de Questões sob o padrão do ENADE.pdf` (guia do professor): os 10 tipos de questão e o modelo de *prompt* ("forneça 4 alternativas", "atitude: buscar precisão... recusando-se a confiar em intuições vagas").
- Todos os cálculos (atrasos, Shannon, VLSM, agregação, NAT, fragmentação, IPv6/EUI-64, Dijkstra, Bellman-Ford, CRC, pare e espere, timeout do TCP, RTTs do HTTP, RSA, Diffie-Hellman, recuo exponencial) foram refeitos em Python 3.

**Estilo identificado do squad:**
- **Slides (Questões 1, 5, 6, 8, 11):** título "ENADE • QUESTÃO N (TIPO)"; **Dado de Suporte (Texto-Base)** longo, entre aspas, citando KUROSE & ROSS (2013, 6ª ed.) ou STALLINGS (2014), "Adaptado"; **Situação-Problema** profissional (laboratório, analista com Wireshark, engenheiro recebendo um bloco IP, auditoria Wi-Fi, startup); **Comando** com "exigindo rigor (técnico/matemático)"; **4 alternativas (A–D)**, longas e de tamanho parecido, muitas vezes com uma frase explicativa embutida; slide de "Gabarito Oficial e Análise dos Distratores" explicando cada erro pelo "rigor" e pelas "armadilhas comerciais/intuitivas". Gabaritos conhecidos: B, D, B, C, A.
- **Manual (9 "Questões comentadas"):** enunciado curto, **5 alternativas (A–E)** numa linha, "Resposta: (X)" com justificativa curta que explica os distratores. Tipos usados: resposta única (7), afirmativa incompleta (1), afirmativas múltiplas (1). Gabaritos: 8 × B e 1 × A (o squad tende a pôr a correta em B).
- Os textos-base das questões inferidas abaixo são **paráfrases no estilo do squad** ("Adaptado"); para não inventar, não indico número de página dos livros.

---

## Como foi deduzida a lógica da numeração dos slides (Questões 2, 3, 4, 7, 9 e 10)

**Fatos dos slides:**

| Nº no slide | Tipo declarado no título | Etiqueta do slide de fundamentação | Tema(s) da Matriz (slide p. 2 / Manual Tabela 1) | Gabarito |
|---|---|---|---|---|
| Questão 1 | Interpretação | "Tema 3 & Camadas OSI" | T3 (+T1) | B |
| Questão 5 | Associação | "Tema 2 & Estrutura de Dados" | T2 | D |
| Questão 6 | Alternativas constantes V/F | "Temas 4 e 5" | T4 + T5 | B |
| Questão 8 | Associação | "Tema 8 & Wi-Fi (802.11)" | T8 + T9 | C |
| Questão 11 | Afirmativas múltiplas | "Tema 6 & Aplicações Práticas" | T6 | A |

**O que a numeração NÃO é:**
- Não é a ordem dos temas: se fosse, a Questão 1 seria do Tema 1, e a Questão 8 (Tema 8) não poderia vir antes da Questão 11 (Tema 6).
- Não é a ordem dos tipos no guia do professor (resposta única → afirmativa incompleta → lacunas → interpretação → afirmativa negativa → afirmativas múltiplas → alternativas constantes → associação → asserção-razão → ordenação): a Questão 1 é "interpretação" (4º tipo) e a Questão 11 é "afirmativas múltiplas" (6º tipo).

**Hipótese 1 — tipos (evidência forte):** o guia do professor lista **10 tipos** de questão. As 5 questões dos slides usam só **4 tipos distintos** (associação aparece duas vezes). Faltam **exatamente 6 tipos** — resposta única, afirmativa incompleta, lacunas, afirmativa negativa, asserção-razão e ordenação — e faltam **exatamente 6 números** (2, 3, 4, 7, 9 e 10). Um banco de **11 questões = os 10 tipos do guia + 1 repetido (associação)** explica a contagem. Por isso cada questão faltante abaixo usa um tipo diferente desses seis.

**Hipótese 2 — temas (evidência boa):** o slide p. 2 descreve o conteúdo de cada tema, e cada questão dos slides cobre literalmente um pedaço dessa descrição (ex.: T9 "segurança (WPA2/WPA3, 802.1X, PMF)" = Questão 8; T3 "Hubs, Switches, Roteadores ... domínios de colisão/broadcast" = Questão 1). Os pedaços da descrição **sem questão nos slides** são os candidatos naturais: T1 "camadas do modelo OSI ... arquitetura cliente-servidor e P2P"; T3 "topologias físicas/lógicas"; T4 "IPv6"; T5 "switches L2/L3 e quadros Ethernet"; T7 "funcionamento e portas dos protocolos essenciais: HTTP/HTTPS, DNS, SMTP, FTP e DHCP" (único tema sem nenhuma questão nos slides); T8 "firewalls, VPNs (IPsec, TLS), criptografia simétrica/assimétrica"; T9 "redes 4G/5G, SDN e IoT".

**Hipótese 3 — posição (evidência fraca, é a melhor leitura possível):** as etiquetas combinam temas vizinhos ("Tema 3 & Camadas OSI", "Temas 4 e 5", "Tema 8 & Wi-Fi", "Tema 6 & Aplicações Práticas"), o que sugere um banco numerado em **blocos temáticos contíguos**, e os números faltantes ficam ao lado da questão do mesmo bloco. Além disso, as questões dos slides de categoria 1 do guia (interpretação) abrem o banco, e as de categoria 2 vêm depois, então as de categoria 3 (asserção-razão, ordenação) provavelmente ficam no fim (9 e 10). Resultado proposto:

| Bloco | Nº | Tema provável | Tipo provável | ID aqui | Gabarito proposto |
|---|---|---|---|---|---|
| Interconexão e OSI (T1/T3/T5) | 1 | T3 equipamentos (conhecida) | Interpretação | — | B |
| | **2** | T1 camadas OSI + cliente-servidor/P2P | **Lacunas** | I1 | C |
| | **3** | T3 topologias física × lógica | **Afirmativa incompleta** | I2 | A |
| | **4** | T5 switches L2/L3, VLAN, STP, quadro Ethernet | **Resposta única** | I3 | D |
| TCP/IP (T2) | 5 | T2 encapsulamento (conhecida) | Associação | — | D |
| Endereçamento e roteamento (T4/T5) | 6 | T4+T5 sub-redes, RIP × OSPF (conhecida) | Alternativas constantes | — | B |
| | **7** | T4 IPv6 | **Afirmativa negativa** | I4 | C |
| Segurança (T8/T9) | 8 | T8+T9 segurança Wi-Fi (conhecida) | Associação | — | C |
| | **9** | T8 criptografia simétrica × assimétrica (TLS) | **Asserção-razão** | I5 | A |
| Aplicação e transporte (T7/T6) | **10** | T7 DHCP → ARP → DNS → TCP/TLS → HTTP (portas) | **Ordenação** | I6 | D |
| | 11 | T6 TCP × UDP (conhecida) | Afirmativas múltiplas | — | A |

Com isso, **todos os 9 temas** ficam com ao menos uma questão "própria" no banco de 11, e o gabarito fica equilibrado (A: 3, B: 2, C: 3, D: 3).
**Confiança:** alta para "os 6 tipos que faltam"; média para os temas; baixa para qual número leva qual tema. Alternativa plausível: as Questões 9/10 serem de T9 (5G/SDN/IoT) em vez de T8/T7, ou o banco ter uma Questão 12 sobre SDN/5G. Por isso SDN (I34) e 5G (I33) aparecem nas questões adicionais com prioridade alta/média.

---

## Mapa de cobertura

"Questão conhecida" = Q1–Q14 e E1–E12 do arquivo `../questoes_por_topico/07_Redes_de_Computadores.md` (Q1–Q5 = slides; Q6–Q14 = questões comentadas do Manual; E = estudos de caso, que são exercícios discursivos, não questões objetivas). Páginas = PDF do Manual (salvo indicação "slide").

| # | Subtópico (material) | Páginas | Questão conhecida | Questão inferida | Prioridade |
|---|---|---|---|---|---|
| 1 | 1.1–1.2 Componentes (borda, acesso, núcleo) e classificação PAN/LAN/MAN/WAN | 5–6 | — | I7 (agrupado com 1.3) | Baixa |
| 2 | 1.3 Comutação de circuitos × pacotes; multiplexação estatística; *store-and-forward* | 6–7 | — | I7 | Média |
| 3 | 1.4 Métricas: atraso nodal (4 componentes), intensidade de tráfego, vazão/gargalo, produto banda-atraso | 7–8 | só E1 (exercício) | I8 | Alta |
| 4 | 1.5 Protocolos (sintaxe/semântica/temporização); serviço × interface × protocolo | 8–9 | — | I9 | Média |
| 5 | 1.6 Modelo OSI: funções das camadas, PDUs, comunicação vertical/horizontal (+ slide p. 2, Tema 1: "cliente-servidor e P2P") | 9–10; slide 2 | Q6 (diagnóstico por camadas) | I1 = **Questão 2 dos slides** | Alta |
| 6 | 2.1–2.2 TCP/IP 4 × 5 camadas, melhor esforço, princípio fim a fim, ampulheta | 11–12 | parcial (Q2) | I9 (agrupado com 1.5) | Média |
| 7 | 2.3 Encapsulamento e PDUs | 12 | Q2 (slides, "Questão 5") | — (variação provável: itens da Coluna 2 em outra ordem) | — |
| 8 | 2.3.1–2.3.2 Desencapsulamento (EtherType, Protocolo, porta) e endereços por camada (IP fim a fim × MAC salto a salto) | 12–13 | — | I10 | Alta |
| 9 | 2.4 Eficiência e sobrecarga | 13 | Q7, E2 | — (variação: pedir eficiência 200/246 ou incluir preâmbulo) | — |
| 10 | 2.5 Pacote de ponta a ponta (DHCP → ARP → DNS → TCP/TLS → HTTP) | 14 | — | I6 = **Questão 10 dos slides** | Alta |
| 11 | 3.1 Conceitos de transmissão, dB, Nyquist e Shannon | 14–15 | só E3 (exercício) | I11 | Alta |
| 12 | 3.2–3.3 Meios guiados (par trançado, coaxial, fibra mono/multimodo) e não guiados (espectro) | 15–17 | — | I12 | Média |
| 13 | 3.4 Topologias física × lógica; malha n(n−1)/2 | 16–18 | — | I2 = **Questão 3 dos slides** | Alta |
| 14 | 3.5 Equipamentos de interconexão; domínios de colisão e broadcast | 18–19 | Q1 (slides), Q8, E4 | — (variação: contagem de domínios como em E4) | — |
| 15 | 4.1 Datagrama IPv4 (TTL, fragmentação, checksum) + ICMP (5.3.2) | 20; 29 | — | I13 | Média |
| 16 | 4.2–4.3 Estrutura IPv4, classes, máscara, CIDR, operação AND | 20–22 | Q3 (slides "Questão 6"), Q9, E5, E7 | — | — |
| 17 | 4.4–4.4.1 Sub-redes e "número mágico" | 22 | Q3 (slides), Q9, E5 | — | — |
| 18 | 4.4.2–4.4.3 VLSM e agregação de rotas | 22–23 | só E6 (exercício) | I14 | Alta |
| 19 | 4.5 Endereços especiais/privados, APIPA, CGNAT e NAT/NAPT | 23–24 | — | I15 | Alta |
| 20 | 4.6 IPv6 (abreviação, tipos, SLAAC/EUI-64, cabeçalho, transição) | 24–26 | — | I4 = **Questão 7 dos slides** | Alta |
| 21 | 5.1 Encaminhamento × roteamento; prefixo mais longo | 26–27 | Q10 | — | — |
| 22 | 5.2 Estado de enlace × vetor de distâncias (RIP × OSPF) | 27 | Q3 (slides "Questão 6", afirm. III e IV) | — | — |
| 23 | 5.2.1 Algoritmo de Dijkstra | 27–28 | só E8 (exercício) | I16 | Alta |
| 24 | 5.2.2 Bellman-Ford e contagem ao infinito | 28 | — | I17 | Média |
| 25 | 5.3 Sistemas autônomos, IGP × EGP, BGP (escolha de rota) | 29 | — | I18 | Média |
| 26 | 5.4.1 Detecção de erros: paridade, checksum, CRC | 29–30 | só E9 (exercício) | I19 | Alta |
| 27 | 5.4.2 Acesso múltiplo, CSMA/CD e recuo exponencial (+ 9.1–9.2.2 CSMA/CA, terminal oculto, RTS/CTS) | 30–31; 50–52 | — | I20 | Média |
| 28 | 5.4.3 MAC e quadro Ethernet; 5.4.5 VLANs e STP; switch de camada 3 (3.5.3) | 31; 19 | — | I3 = **Questão 4 dos slides** | Alta |
| 29 | 5.4.4 ARP e ARP spoofing | 31 | — | I10 (agrupado) | Média |
| 30 | 6.1–6.2 Serviços de transporte, portas (faixas IANA) e sockets | 32–33 | parcial (Q12 cita portas) | I21 | Média |
| 31 | 6.3 UDP | 33 | Q5 (slides "Questão 11"), Q7 | — | — |
| 32 | 6.4 Transferência confiável: pare e espere, Go-Back-N, repetição seletiva | 33–34 | — | I22 | Alta |
| 33 | 6.5.1–6.5.3, 6.5.5–6.5.6 TCP: seq/ACK em bytes, três vias, SYN flood, encerramento, retransmissão rápida, controle de fluxo | 34–36 | — | I23 | Alta |
| 34 | 6.5.4 Estimativa do RTT e timeout | 35–36 | só E10 (exercício) | I24 | Média |
| 35 | 6.5.7 Controle de congestionamento (Reno, AIMD) | 36–37 | Q11 | — (variação: 3 ACKs duplicados ou Figura 14) | — |
| 36 | 6.6 Quadro-resumo TCP × UDP | 38 | Q5 (slides) | — | — |
| 37 | 7.1 Arquiteturas cliente-servidor × P2P | 38 | — | I1 (lacuna V) | Média |
| 38 | 7.2.1 / 7.2.4 HTTP: mensagens, métodos (seguro/idempotente), códigos de status, cookies, cache | 38–40 | parcial (Q12, afirm. I) | I26 | Média |
| 39 | 7.2.2–7.2.3 Persistência, RTTs, HTTP/2, HTTP/3 e QUIC | 40 | só E11 (exercício) | I25 | Alta |
| 40 | 7.3 DNS: hierarquia, consulta recursiva × iterativa, registros, DNSSEC/DoH | 40–42 | parcial (Q6, Q12 afirm. III) | I27 | Alta |
| 41 | 7.4 E-mail: SMTP, POP3, IMAP, SPF/DKIM/DMARC | 42–43 | parcial (Q12, afirm. IV) | I28 | Baixa |
| 42 | 7.5 FTP | 43–44 | Q12 (afirm. II) | — | — |
| 43 | 7.6 DHCP (DORA), SSH, SNMP, NTP | 44 | — | I6 (DHCP/DORA é um dos itens) | Média |
| 44 | 8.1–8.2 Propriedades de segurança (CID+) e ameaças | 45 | — | I29 | Média |
| 45 | 8.3 Criptografia simétrica × assimétrica, Kerckhoffs, DH, hash/assinatura, PKI, TLS | 45–47 | — | I5 = **Questão 9 dos slides** | Alta |
| 46 | 8.3.2 RSA com números pequenos (+ Tabela 24, DH) | 46–47 | só E12 (exercício) | I30 | Média |
| 47 | 8.4 Firewalls (tipos, ordem das regras, DMZ, IDS/IPS) + 8.6 defesa em profundidade e Zero Trust | 48–50 | — | I31 | Alta |
| 48 | 8.5–8.5.1 VPN (site a site × acesso remoto) | 49–50 | Q13 | — | — |
| 49 | 8.5.2 IPsec (AH, ESP, IKE, modo transporte × túnel) | 49–50 | — (Q13 só pede "VPN") | I32 | Média |
| 50 | 9.1–9.2.3 Enlaces sem fio, arquitetura 802.11, CSMA/CA, gerações do Wi-Fi | 50–52 | — | I20 (agrupado) | Média |
| 51 | 9.2.4 Segurança no Wi-Fi | 52; slides 12–14 | Q4 (slides "Questão 8") | — | — |
| 52 | 9.3–9.4 Redes celulares (4G/5G) e mobilidade | 52–54 | — (5G só aparece como distrator na Q14) | I33 | Média |
| 53 | 9.5 SDN, OpenFlow, NFV | 54–55 | — | I34 | Alta |
| 54 | 9.6 Computação em nuvem, borda e CDN | 55–56 | — | I35 | Média |
| 55 | 9.7 IoT (LPWAN, MQTT/CoAP, desafios) | 56–58 | Q14 | — | — |

**Resumo:** **55 subtópicos** mapeados; **14** já cobertos integralmente por questões objetivas conhecidas (linhas 7, 9, 14, 16, 17, 21, 22, 31, 35, 36, 42, 48, 51, 55); **41** sem questão objetiva própria (7 deles só tinham estudo de caso, e 5 só cobertura parcial numa afirmativa). Foram escritas **35 questões inferidas**: **6 correspondem às Questões 2, 3, 4, 7, 9 e 10 faltantes dos slides** (I1–I6, 4 alternativas, estilo dos slides) e **29 são adicionais** (I7–I35, 5 alternativas, estilo do Manual). Gabaritos: slides I1–I6 = C, A, D, C, A, D; adicionais I7–I35 = A 6, B 6, C 6, D 6, E 5.

---

## Índice

**Parte 1 — Questões 2, 3, 4, 7, 9 e 10 faltantes dos slides (4 alternativas, A–D)**
1. [I1 — Questão 2 (Lacunas): camadas OSI e arquitetura P2P](#i1--questão-2-lacunas-camadas-osi-e-arquitetura-p2p)
2. [I2 — Questão 3 (Afirmativa incompleta): topologia física × lógica](#i2--questão-3-afirmativa-incompleta-topologia-física--lógica)
3. [I3 — Questão 4 (Resposta única): VLANs, switch L3 e STP](#i3--questão-4-resposta-única-vlans-switch-l3-e-stp)
4. [I4 — Questão 7 (Afirmativa negativa): IPv6](#i4--questão-7-afirmativa-negativa-ipv6)
5. [I5 — Questão 9 (Asserção-razão): criptografia híbrida no TLS](#i5--questão-9-asserção-razão-criptografia-híbrida-no-tls)
6. [I6 — Questão 10 (Ordenação): do DHCP ao HTTP GET](#i6--questão-10-ordenação-do-dhcp-ao-http-get)

**Parte 2 — Questões adicionais (5 alternativas, A–E)**

7. [I7 — Comutação de circuitos × pacotes](#i7--comutação-de-circuitos--pacotes)
8. [I8 — Atraso fim a fim](#i8--atraso-fim-a-fim)
9. [I9 — Protocolos, camadas e modelo TCP/IP](#i9--protocolos-camadas-e-modelo-tcpip)
10. [I10 — Endereços em cada camada e ARP](#i10--endereços-em-cada-camada-e-arp)
11. [I11 — Shannon e Nyquist](#i11--shannon-e-nyquist)
12. [I12 — Escolha do meio de transmissão](#i12--escolha-do-meio-de-transmissão)
13. [I13 — Fragmentação IPv4](#i13--fragmentação-ipv4)
14. [I14 — VLSM e agregação de rotas](#i14--vlsm-e-agregação-de-rotas)
15. [I15 — Endereços privados, APIPA e NAPT](#i15--endereços-privados-apipa-e-napt)
16. [I16 — Dijkstra a partir de z](#i16--dijkstra-a-partir-de-z)
17. [I17 — Bellman-Ford (vetor de distâncias)](#i17--bellman-ford-vetor-de-distâncias)
18. [I18 — Escolha de rota no BGP](#i18--escolha-de-rota-no-bgp)
19. [I19 — Cálculo do CRC](#i19--cálculo-do-crc)
20. [I20 — CSMA/CD × CSMA/CA](#i20--csmacd--csmaca)
21. [I21 — Portas e sockets](#i21--portas-e-sockets)
22. [I22 — Pare e espere e janela](#i22--pare-e-espere-e-janela)
23. [I23 — TCP: sequência, ACK, três vias e controle de fluxo](#i23--tcp-sequência-ack-três-vias-e-controle-de-fluxo)
24. [I24 — Timeout do TCP](#i24--timeout-do-tcp)
25. [I25 — RTTs do HTTP persistente e não persistente](#i25--rtts-do-http-persistente-e-não-persistente)
26. [I26 — Métodos e códigos HTTP, cache](#i26--métodos-e-códigos-http-cache)
27. [I27 — Resolução DNS](#i27--resolução-dns)
28. [I28 — POP3 × IMAP e SPF/DKIM/DMARC](#i28--pop3--imap-e-spfdkimdmarc)
29. [I29 — Ameaças × propriedades de segurança](#i29--ameaças--propriedades-de-segurança)
30. [I30 — RSA com números pequenos](#i30--rsa-com-números-pequenos)
31. [I31 — Regras de firewall](#i31--regras-de-firewall)
32. [I32 — IPsec: ESP em modo túnel](#i32--ipsec-esp-em-modo-túnel)
33. [I33 — 5G: eMBB, URLLC, mMTC e fatiamento](#i33--5g-embb-urllc-mmtc-e-fatiamento)
34. [I34 — SDN e tabela OpenFlow](#i34--sdn-e-tabela-openflow)
35. [I35 — IaaS, PaaS, SaaS e CDN](#i35--iaas-paas-saas-e-cdn)

---

# Parte 1 — Questões 2, 3, 4, 7, 9 e 10 faltantes dos slides

> Estilo dos slides: título "ENADE • QUESTÃO N (TIPO)", texto-base com citação, situação-problema, comando com "exigindo rigor", 4 alternativas. A numeração "Questão N" é a **hipótese** explicada acima.

## I1 — Questão 2 (Lacunas): camadas OSI e arquitetura P2P
**Subtópico coberto:** Tema 1 — "Camadas do modelo OSI, funções de encapsulamento, arquitetura cliente-servidor e P2P" (slide p. 2); Manual 1.6.1 (p. 10) e 7.1 (p. 38).
**Por que é provável:** o Tema 1 é o primeiro da Matriz e não tem questão própria nos slides (a Questão 1 só cita "Camadas OSI" na etiqueta). O slide p. 2 lista exatamente "camadas OSI" e "cliente-servidor e P2P". "Lacunas" é um dos 6 tipos que o squad ainda não usou, e é o formato natural para "função de cada camada".
**Prioridade:** Alta
**Tipo ENADE:** Lacunas (Cat. 1) — rótulo provável: "ENADE • QUESTÃO 2 (LACUNAS)"

**Enunciado:**

**Dado de Suporte (Texto-Base):** "Para reduzir a complexidade de projeto, os protocolos de rede são organizados em camadas, cada uma oferecendo serviços à camada imediatamente superior e utilizando os serviços da camada inferior. [...] Cada camada de um nó conversa logicamente com a camada de mesmo nível do nó remoto, por meio dos cabeçalhos que acrescenta. Quanto à arquitetura das aplicações, no modelo cliente-servidor há um hospedeiro sempre ligado que atende a requisições de muitos clientes; no modelo P2P, pares conectados de forma intermitente comunicam-se diretamente, atuando ao mesmo tempo como clientes e servidores." (KUROSE, James F.; ROSS, Keith W. Redes de Computadores e a Internet: Uma Abordagem Top-Down. 6ª ed. São Paulo: Pearson Education do Brasil, 2013. Adaptado.)

**Situação-Problema:** Na integração de novos estagiários do centro de operações de rede (NOC) da universidade, o coordenador entregou um "guia de bolso" para que cada incidente seja registrado na camada OSI correta. O guia também resume a arquitetura do novo serviço que distribui imagens de máquinas virtuais (arquivos de dezenas de GB) aos laboratórios, que precisa continuar rápido mesmo com centenas de downloads simultâneos na primeira semana do semestre. Trecho do guia:

"No Modelo OSI, a camada de ___(I)___ organiza os bits em quadros, entrega dados entre nós vizinhos e utiliza endereços físicos (MAC); a camada de ___(II)___ é responsável pelo endereçamento lógico e pela escolha do caminho entre redes distintas; a camada de ___(III)___ provê comunicação fim a fim entre processos, identificados por portas, e pode garantir entrega confiável e ordenada; e a camada de ___(IV)___ trata da sintaxe e da semântica da informação, como conversão de códigos de caracteres, compressão e criptografia. Para o serviço de imagens, adotou-se a arquitetura ___(V)___: cada laboratório que conclui o download passa também a enviar partes do arquivo aos demais, de modo que cada novo participante traz demanda, mas também capacidade de servir."

**Comando:** Exigindo rigor conceitual para não confundir as funções de camadas adjacentes do Modelo de Referência OSI nem os modelos de arquitetura de aplicação, assinale a alternativa que preenche corretamente as lacunas I, II, III, IV e V, respectivamente:

**Alternativas:**
- **A)** enlace – transporte – rede – apresentação – cliente-servidor.
- **B)** física – rede – transporte – sessão – par a par (P2P).
- **C)** enlace – rede – transporte – apresentação – par a par (P2P).
- **D)** enlace – rede – sessão – aplicação – par a par (P2P).

**Gabarito: C**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Troca rede e transporte: põe o endereçamento lógico/roteamento no transporte e as portas na rede (mesmo erro que o squad aponta no distrator A da Questão 5). E chama de cliente-servidor uma arquitetura em que os próprios clientes servem os demais: no cliente-servidor, quem atende é um servidor sempre ligado, e a capacidade não cresce com o número de clientes.
- **B) ❌** — A camada física transmite bits brutos e "não entende o significado dos bits"; quem monta quadros e usa MAC é o enlace (L2). E a sessão controla diálogo, sincronização e *checkpoints*; codificação, compressão e criptografia são da apresentação.
- **C) ✅** — I enlace (quadros, nós vizinhos, MAC); II rede (IP, roteamento); III transporte (fim a fim entre processos, portas, confiabilidade); IV apresentação (códigos de caracteres, compressão, criptografia); V P2P (autoescalabilidade: cada par traz demanda e capacidade, como no BitTorrent).
- **D) ❌** — Põe as portas e a entrega confiável na sessão (são do transporte) e as funções de sintaxe/semântica na aplicação (são da apresentação). É a "camada vizinha" errada, a pegadinha clássica do OSI.

**Base no material:** Manual p. 9 (Figura 2: camadas, PDUs e exemplos), p. 10 (1.6.1 "Função de cada camada", 1.6.2 comunicação vertical/horizontal), p. 38 (7.1 "Par a par (P2P) ... autoescalabilidade ... BitTorrent"); slide p. 2 (descrição do Tema 1).
**Conceito-chave para a prova:** L1 bits/sinal; L2 quadro/MAC/vizinhos; L3 pacote/IP/roteamento; L4 segmento/portas/fim a fim; L5 diálogo/sincronização; L6 codificação/compressão/criptografia; L7 protocolos do usuário. P2P = autoescalável; cliente-servidor = servidor sempre ligado com endereço fixo.

---

## I2 — Questão 3 (Afirmativa incompleta): topologia física × lógica
**Subtópico coberto:** Tema 3 — "topologias físicas/lógicas" (slide p. 2); Manual 3.4, Tabela 6 e equação (8) (p. 16–18).
**Por que é provável:** "topologias físicas/lógicas" está escrito na descrição do Tema 3 do slide p. 2 e não aparece em nenhuma questão conhecida. O Manual tem tabela de vantagens/desvantagens, fórmula da malha e a frase-pegadinha "uma rede com hub é fisicamente uma estrela, mas logicamente um barramento".
**Prioridade:** Alta
**Tipo ENADE:** Afirmativa incompleta (Cat. 1) — rótulo provável: "ENADE • QUESTÃO 3 (AFIRMATIVA INCOMPLETA)"

**Enunciado:**

**Dado de Suporte (Texto-Base):** "A topologia física define como os dispositivos estão fisicamente conectados à rede, enquanto a topologia lógica descreve como os dados efetivamente circulam entre eles. [...] Em uma topologia em malha completa, cada dispositivo possui um enlace dedicado ponto a ponto com todos os demais; para n nós, são necessários n(n − 1)/2 enlaces, o que torna a solução robusta, porém cara e de difícil instalação." (FOROUZAN, Behrouz A. Comunicação de Dados e Redes de Computadores. 4ª ed. Porto Alegre: AMGH, 2010. Adaptado.)

**Situação-Problema:** Um laboratório legado tem 12 estações, cada uma ligada por um cabo próprio a um hub central. Na reunião de revisão, um consultor afirmou que, "como cada computador tem seu próprio cabo até o equipamento central, a rede já é uma estrela pura, em que cada quadro vai direto ao destinatário". Outro sugeriu "eliminar o equipamento central e ligar todos com todos, porque a malha completa é a opção mais barata e resolve o ponto único de falha". Você foi chamado para dar o parecer técnico.

**Comando:** Exigindo rigor técnico para distinguir o arranjo físico dos cabos do comportamento lógico da transmissão, e recusando argumentos intuitivos de custo, complete corretamente a afirmação: "A rede do laboratório..."

**Alternativas:**
- **A)** ...tem topologia física em estrela e lógica em barramento, pois o hub repete cada sinal para todas as portas; a falha de um cabo isola só uma estação, o hub é ponto único de falha e a malha completa exigiria 66 enlaces.
- **B)** ...tem topologia física e lógica em estrela, pois o hub entrega cada quadro apenas na porta do destinatário; a malha completa exigiria 24 enlaces, custo comparável ao do cabeamento em estrela atual.
- **C)** ...tem topologia física em barramento e lógica em anel, pois os quadros circulam de estação em estação até o destino; a malha completa exigiria 132 enlaces, um para cada par ordenado de estações.
- **D)** ...tem topologia física em estrela e lógica em anel com passagem de *token*, o que elimina colisões; o rompimento de qualquer cabo derruba toda a rede, como ocorre no barramento.

**Gabarito: A**

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — Fisicamente é estrela (cabo por estação até o centro). Logicamente é barramento, porque o hub (L1) copia tudo para todas as portas, e todos disputam o mesmo meio (um domínio de colisão). Pela Tabela 6, na estrela "a falha de um cabo afeta só um nó", mas o equipamento central é ponto único de falha. Malha com n = 12: 12 × 11 / 2 = **66 enlaces** (conferido).
- **B) ❌** — Atribui ao hub a filtragem por destino, que é do switch (tabela MAC). O "24" (2n) não segue a fórmula da malha, e a malha cresce com n², então não tem custo "comparável".
- **C) ❌** — O cabeamento não é barramento (não há um cabo único compartilhado), e não há circulação em anel. 132 = n(n − 1) conta cada enlace duas vezes; o correto divide por 2.
- **D) ❌** — Hub não implementa passagem de *token* (isso é do *token ring*), então há colisões. E o rompimento de um cabo na estrela só afeta uma estação; "um rompimento derruba tudo" é desvantagem do barramento.

**Base no material:** Manual p. 16 (3.4: "Uma rede com hub ... é fisicamente uma estrela, mas logicamente um barramento"), p. 17 (Figura 5 e Tabela 6), p. 17–18 (equação 8: E = n(n−1)/2; "com 5 nós são 10 enlaces; com 50 nós, 1.225"); p. 18 (3.5.1 hub: mesmo domínio de colisão, half-duplex).
**Conceito-chave para a prova:** topologia física = como os cabos estão; lógica = como os dados circulam. Hub = estrela física + barramento lógico. Malha completa: n(n−1)/2 enlaces, crescimento Θ(n²). Estrela: falha de cabo isola 1 nó, falha do centro derruba todos.

---

## I3 — Questão 4 (Resposta única): VLANs, switch L3 e STP
**Subtópico coberto:** Tema 5 — "switches L2/L3 e quadros Ethernet" (slide p. 2); Manual 5.4.3 (quadro Ethernet), 5.4.5 (VLANs e STP), p. 31; 3.5.3 (switch de camada 3), p. 19.
**Por que é provável:** a Questão 6 dos slides cobriu só a metade "RIP × OSPF" do Tema 5. A outra metade da descrição ("switches L2/L3 e quadros Ethernet") não tem questão. É também a continuação natural da Questão 1 (lá o requisito era manter **um** domínio de broadcast; aqui é separar vários).
**Prioridade:** Alta
**Tipo ENADE:** Resposta única (Cat. 1) — rótulo provável: "ENADE • QUESTÃO 4 (RESPOSTA ÚNICA)"

**Enunciado:**

**Dado de Suporte (Texto-Base):** "Uma VLAN permite que uma única infraestrutura física de LAN comutada seja dividida em várias redes locais virtuais, cada uma constituindo um domínio de broadcast próprio. Nos enlaces de tronco entre switches, os quadros recebem uma etiqueta (padrão IEEE 802.1Q) que identifica a VLAN de origem; o tráfego entre VLANs distintas precisa ser roteado. [...] Como os quadros Ethernet não possuem campo de tempo de vida, enlaces redundantes entre switches exigem um protocolo que elimine laços." (KUROSE & ROSS, 2013. Adaptado.)

**Situação-Problema:** Depois da troca do equipamento central do laboratório (Questão 1), a universidade ligou à mesma infraestrutura de switches os setores Financeiro, Secretaria Acadêmica e uma rede de Visitantes. A auditoria apontou que: (i) ARP requests e demais broadcasts de um setor chegam a todos os outros; (ii) um notebook de visitante conseguiu capturar quadros de broadcast do Financeiro; (iii) a equipe quer ligar os switches de andar com enlaces redundantes, formando um laço físico, para aumentar a disponibilidade. Restrições: não há verba para cabeamento separado por setor, e o Financeiro continua precisando acessar o servidor da Secretaria.

**Comando:** Com base no texto de apoio e exigindo rigor técnico sobre o funcionamento da camada de enlace, assinale a decisão de projeto tecnicamente adequada:

**Alternativas:**
- **A)** Manter um único domínio de camada 2 sem VLANs, pois o autoaprendizado da tabela MAC passa a encaminhar os quadros FF:FF:FF:FF:FF:FF somente para a porta do setor de destino, isolando os broadcasts de cada departamento.
- **B)** Criar VLANs IEEE 802.1Q por setor e ligar os switches redundantes sem STP, pois o campo TTL do cabeçalho do quadro Ethernet descarta automaticamente os quadros que entrarem em laço entre os switches.
- **C)** Criar VLANs IEEE 802.1Q por setor e interligá-las por um hub central que, operando na camada 1, encaminha os quadros entre VLANs com base na etiqueta de 12 bits de cada quadro.
- **D)** Criar VLANs IEEE 802.1Q por setor (cada uma um domínio de broadcast, com etiqueta de 4 bytes e VLAN ID de 12 bits nos troncos), rotear entre elas num switch de camada 3 e manter o STP ativo nos enlaces redundantes.

**Gabarito: D**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — O switch **inunda** broadcasts (e destinos desconhecidos) para todas as portas, menos a de origem. Sem VLAN, continua havendo um único domínio de broadcast, e os problemas (i) e (ii) permanecem.
- **B) ❌** — O quadro Ethernet **não tem TTL** (o TTL é do datagrama IP). Num laço sem STP, um broadcast circula para sempre (*broadcast storm*). O STP (IEEE 802.1D) bloqueia portas até a topologia virar árvore e reativa-as se um enlace falhar.
- **C) ❌** — Hub é L1: só repete bits, não lê etiquetas nem MAC. Comunicação entre VLANs exige roteador ou switch de camada 3.
- **D) ✅** — VLANs separam os domínios de broadcast sem cabeamento novo (resolve i e ii). A tag 802.1Q de 4 bytes, com VLAN ID de 12 bits, identifica a VLAN nos troncos. O switch L3 roteia entre VLANs em hardware (Financeiro ↔ Secretaria), e o STP permite a redundância sem *broadcast storm* (resolve iii).

**Base no material:** Manual p. 18 (3.5.2: inundação de broadcast; "a menos que se usem VLANs"), p. 19 (3.5.3: "switch de camada 3 (roteia entre VLANs em hardware)"), p. 31 (5.4.3 quadro Ethernet II, Figura 10: preâmbulo 8, MAC 6+6, tipo 2, dados 46–1500, FCS 4; 5.4.5 VLANs e STP).
**Conceito-chave para a prova:** VLAN = domínio de broadcast separado na mesma infraestrutura; 802.1Q = tag de 4 bytes, VLAN ID de 12 bits; entre VLANs só com roteador/switch L3. Ethernet não tem TTL → laço sem STP = *broadcast storm*.

---

## I4 — Questão 7 (Afirmativa negativa): IPv6
**Subtópico coberto:** Tema 4 — "Endereçamento IPv4/IPv6" (slide p. 2); Manual 4.6 (p. 24–26), Tabelas 12 e 13, box "Erro comum".
**Por que é provável:** a Questão 6 dos slides cobriu IPv4 (sub-redes /26); a parte "IPv6" da descrição do Tema 4 não tem questão em lugar nenhum. O Manual dedica 2 páginas, uma tabela comparativa e um box "Erro comum" (o "::" duplo), que é material típico de distrator. "Afirmativa negativa" é um dos tipos não usados.
**Prioridade:** Alta
**Tipo ENADE:** Afirmativa negativa (Cat. 1) — rótulo provável: "ENADE • QUESTÃO 7 (AFIRMATIVA NEGATIVA)"

**Enunciado:**

**Dado de Suporte (Texto-Base):** "O esgotamento do espaço de endereços IPv4 motivou o desenvolvimento do IPv6, cujo endereço tem 128 bits. Além de ampliar o endereçamento, o novo protocolo simplificou o datagrama: o cabeçalho passou a ter 40 bytes de comprimento fixo, o checksum foi eliminado e a fragmentação e a remontagem deixaram de ser feitas nos roteadores intermediários. [...] Como não é possível migrar toda a Internet de uma só vez, mecanismos de transição, como a pilha dupla e o tunelamento, permitem a convivência das duas versões." (KUROSE & ROSS, 2013. Adaptado.)

**Situação-Problema:** Uma operadora regional, sem conseguir novos blocos IPv4 (o LACNIC esgotou seu estoque regular em 2020), decidiu implantar pilha dupla em toda a rede. Um analista júnior preparou um relatório técnico com quatro afirmações para orientar a equipe de campo. Antes de publicá-lo, o engenheiro responsável precisa identificar a afirmação que levaria a equipe a configurar os equipamentos de forma errada.

**Comando:** Exigindo rigor técnico sobre a especificação do IPv6 e recusando abreviações "intuitivas", assinale a alternativa **INCORRETA**:

**Alternativas:**
- **A)** O endereço 2001:0db8:0000:0000:0000:ff00:0042:8329 pode ser escrito como 2001:db8::ff00:42:8329, omitindo os zeros à esquerda de cada grupo e substituindo uma única sequência de grupos zerados por "::".
- **B)** O cabeçalho IPv6 tem tamanho fixo de 40 bytes e não possui checksum; os roteadores não fragmentam datagramas, tarefa que cabe somente à origem, após descobrir a MTU do caminho.
- **C)** O endereço 2001:db8:0:0:1:0:0:1 pode ser abreviado como 2001:db8::1::1, pois o "::" pode aparecer mais de uma vez, desde que cada ocorrência substitua o mesmo número de grupos zerados.
- **D)** Como o IPv6 não possui broadcast, a descoberta do endereço físico de um vizinho, feita no IPv4 pelo ARP em broadcast, passa a ser feita pelo NDP (ICMPv6), com mensagens multicast.

**Gabarito: C** (a afirmativa incorreta)

**Por que cada alternativa está certa ou errada:**
- **A) ❌ (afirmativa verdadeira)** — É o exemplo do próprio Manual. Conferido em Python: `2001:db8::ff00:42:8329`.
- **B) ❌ (afirmativa verdadeira)** — Tabela 13: 40 bytes fixos, sem checksum, fragmentação "apenas origem". Os campos de fragmentação e as opções foram substituídos por cabeçalhos de extensão.
- **C) ✅ (afirmativa INCORRETA)** — Pela RFC 5952, o "::" **só pode aparecer uma vez**; com dois, não há como saber quantos zeros há em cada um. A forma correta é **2001:db8::1:0:0:1** (com empate entre as sequências de zeros, comprime-se a primeira). Conferido em Python. É exatamente o box "Erro comum" do Manual.
- **D) ❌ (afirmativa verdadeira)** — O IPv6 não tem broadcast. O NDP (sobre ICMPv6) substitui o ARP e usa multicast (Tabelas 12 e 13).

**Base no material:** Manual p. 24 (4.6.1: abreviação, box "Erro comum"; 4.6.2: "O IPv6 não tem broadcast"), p. 25 (Tabela 12 tipos/prefixos; 4.6.3 SLAAC/EUI-64; 4.6.4 cabeçalho de 40 bytes; Tabela 13 IPv4 × IPv6), p. 26 (4.6.5 pilha dupla, tunelamento, NAT64/DNS64).
**Conceito-chave para a prova:** 128 bits, 8 grupos hexadecimais; zeros à esquerda podem sair e "::" só uma vez. Cabeçalho de 40 B fixo, sem checksum, roteador não fragmenta. Sem broadcast (multicast + NDP). fe80::/10 link-local, fc00::/7 ULA, 2000::/3 global, ::1 loopback. EUI-64: insere FFFE no meio do MAC e inverte o 7º bit (00:1A:2B:3C:4D:5E → 021a:2bff:fe3c:4d5e).

---

## I5 — Questão 9 (Asserção-razão): criptografia híbrida no TLS
**Subtópico coberto:** Tema 8 — "criptografia simétrica/assimétrica", "VPNs (IPsec, TLS)" (slide p. 2); Manual 8.3.1–8.3.6 (p. 45–47).
**Por que é provável:** a Questão 8 dos slides, embora etiquetada "Tema 8", trata só de Wi-Fi (conteúdo listado no Tema 9). A parte central do Tema 8 (criptografia, TLS, firewalls, VPN) ficou sem questão nos slides. O Manual termina a seção 8.3.6 com a frase-síntese "a assimétrica é usada só no início ... a simétrica cifra todo o resto", que é uma relação de causa e efeito pronta para asserção-razão (tipo não usado).
**Prioridade:** Alta
**Tipo ENADE:** Asserção-razão (Cat. 3) — rótulo provável: "ENADE • QUESTÃO 9 (ASSERÇÃO-RAZÃO)"

**Enunciado:**

**Dado de Suporte (Texto-Base):** "A criptografia de chave pública é computacionalmente muito mais custosa que a criptografia simétrica; por isso, raramente é usada para cifrar grandes volumes de dados. Seu papel principal está na autenticação das partes e na distribuição de chaves: uma vez estabelecida uma chave de sessão secreta, os dados passam a ser protegidos por um algoritmo simétrico." (STALLINGS, William, 2014. Adaptado.)

**Situação-Problema:** Uma fintech passou por auditoria do seu aplicativo móvel, que se comunica com o servidor via HTTPS (TLS 1.3). O auditor questionou por que o aplicativo não cifra todas as mensagens diretamente com RSA de 2.048 bits, "já que a criptografia de chave pública é mais segura". O arquiteto de segurança respondeu com as asserções a seguir.

I. No TLS 1.3, a criptografia assimétrica (o certificado digital do servidor e a troca de chaves Diffie-Hellman efêmera) é empregada apenas no *handshake*, para autenticar o servidor e combinar uma chave de sessão, enquanto todo o volume de dados da sessão é cifrado com uma cifra simétrica autenticada, como o AES-GCM.

**PORQUE**

II. A criptografia simétrica é computacionalmente muito mais rápida que a assimétrica, mas exige que as partes compartilhem previamente uma chave secreta, problema de distribuição de chaves que a criptografia de chave pública e o Diffie-Hellman resolvem.

**Comando:** Exigindo rigor técnico ao avaliar a arquitetura criptográfica e recusando a intuição de que "chave pública é sempre mais segura", a respeito dessas asserções, assinale a opção correta:

**Julgamento:**
- **Asserção I — Verdadeira.** No TLS, o certificado autentica o servidor, o DH efêmero faz o acordo de chave (com sigilo futuro obrigatório no TLS 1.3), e os dados vão com AES-GCM (confidencialidade e integridade).
- **Asserção II — Verdadeira.** A simétrica é rápida e cifra o volume de dados, mas tem o problema da distribuição de chaves, resolvido pela assimétrica e pelo DH.
- **Relação:** a II **explica** a I. O esquema híbrido existe justamente para unir a velocidade da simétrica com a solução de distribuição de chaves da assimétrica.

**Alternativas:**
- **A)** As asserções I e II são verdadeiras, e a II é uma justificativa correta da I, pois o esquema híbrido une a velocidade da cifra simétrica à distribuição segura de chaves da assimétrica.
- **B)** As asserções I e II são verdadeiras, mas a II não é uma justificativa correta da I, pois o esquema híbrido é adotado apenas por compatibilidade com navegadores antigos.
- **C)** A asserção I é verdadeira, e a II é falsa, pois a criptografia assimétrica é a mais rápida e só não cifra os dados por limitação de tamanho da chave.
- **D)** A asserção I é falsa, e a II é verdadeira, pois no TLS 1.3 todos os dados da sessão são cifrados com a chave privada do servidor.

**Gabarito: A**

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — As duas asserções são verdadeiras e a II é a razão da I (Manual p. 47: "a assimétrica é usada só no início, para autenticar e combinar uma chave de sessão; a simétrica cifra todo o resto").
- **B) ❌** — A relação de causa existe. "Compatibilidade com navegadores antigos" é justificativa inventada; o TLS 1.3 inclusive removeu algoritmos antigos.
- **C) ❌** — Inverte o desempenho: a simétrica é que "é muito rápida" (Manual 8.3.1). É o erro do auditor da situação-problema.
- **D) ❌** — Cifrar com a chave **privada** do remetente produz assinatura (qualquer um decifra com a pública), não confidencialidade. E a I é verdadeira.

**Base no material:** Manual p. 45 (8.3.1 simétrica: "muito rápida ... o grande problema ... é a distribuição de chaves"; n(n−1)/2 chaves), p. 46 (8.3.2 assimétrica: confidencialidade com a pública do destinatário, assinatura com a privada do remetente; 8.3.3 DH), p. 47 (8.3.4 hash e assinatura; 8.3.5 PKI/X.509, ICP-Brasil; 8.3.6 TLS 1.3: 1 RTT, sigilo futuro, "esquema híbrido").
**Conceito-chave para a prova:** simétrica = rápida, mesma chave, problema da distribuição (n(n−1)/2 chaves). Assimétrica = par pública/privada, lenta; serve para autenticar e combinar chaves. Na prática: híbrido (TLS, IPsec). Confidencialidade → pública do destinatário; assinatura → privada do remetente sobre o hash.

---

## I6 — Questão 10 (Ordenação): do DHCP ao HTTP GET
**Subtópico coberto:** Tema 7 — "Funcionamento e portas dos protocolos essenciais: HTTP/HTTPS, DNS, SMTP, FTP e DHCP" (slide p. 2); Manual 2.5 (p. 14), 7.6 DHCP/DORA (p. 44), 7.3 DNS (p. 40–41), 6.5.2 três vias (p. 35), 8.3.6 TLS (p. 47), 5.4.4 ARP (p. 31).
**Por que é provável:** o Tema 7 é o **único** tema da Matriz sem nenhuma questão nos slides. O Manual tem a sequência pronta "um dia na vida de uma requisição web" (DHCP → ARP → DNS → TCP 443/TLS → HTTP GET), que é um procedimento ordenado, ideal para "ordenação" (tipo não usado). Ficaria vizinha da Questão 11 (transporte, "Aplicações Práticas").
**Prioridade:** Alta
**Tipo ENADE:** Ordenação (Cat. 3) — rótulo provável: "ENADE • QUESTÃO 10 (ORDENAÇÃO)"

**Enunciado:**

**Dado de Suporte (Texto-Base):** "Acompanhar tudo o que acontece desde que um usuário liga seu notebook a uma rede até receber uma página Web é uma das melhores formas de revisar a pilha de protocolos: o dispositivo precisa primeiro obter um endereço e as informações de configuração da rede, descobrir o endereço físico do roteador de saída, traduzir o nome do servidor em um endereço IP e, só então, estabelecer a conexão de transporte por meio da qual a requisição da aplicação será enviada." (KUROSE & ROSS, 2013. Adaptado.)

**Situação-Problema:** Um aluno liga o notebook, que ainda não tem endereço IP, ao Wi-Fi da faculdade e digita https://www.uscs.edu.br no navegador. Um analista de redes captura todo o tráfego no Wireshark, mas exporta os eventos fora de ordem:

- ( ) Abertura de conexão TCP com o servidor web (apresentação em três vias: SYN, SYN+ACK, ACK) na porta 443, seguida da negociação TLS.
- ( ) Troca DHCP em quatro mensagens (Discover, Offer, Request, Acknowledge), via UDP nas portas 67/68, para obter IP, máscara, gateway padrão e endereço do servidor DNS.
- ( ) Envio da requisição HTTP GET, protegida pelo TLS e encapsulada em segmento TCP, datagrama IP e quadro Wi-Fi.
- ( ) ARP Request em broadcast ("quem tem o IP do gateway?") e ARP Reply em unicast, com o MAC do gateway.
- ( ) Consulta ao servidor DNS (UDP, porta 53) para obter o endereço IP associado a www.uscs.edu.br.

**Comando:** Exigindo rigor técnico quanto às dependências entre os protocolos (o que cada etapa precisa ter obtido antes de começar), numere os eventos de 1 a 5 na ordem em que ocorrem e assinale a alternativa que apresenta a sequência correta, de cima para baixo:

**Alternativas:**
- **A)** 4, 2, 5, 3, 1.
- **B)** 3, 1, 5, 2, 4.
- **C)** 4, 2, 5, 1, 3.
- **D)** 4, 1, 5, 2, 3.

**Gabarito: D**

**Ordem correta e dependências:** 1º DHCP (sem IP, o host nem sabe quem é o gateway nem o DNS) → 2º ARP (para mandar qualquer quadro ao gateway é preciso o MAC dele) → 3º DNS (com o IP do servidor DNS, recebido no DHCP, e o MAC do gateway, resolve o nome) → 4º TCP três vias na porta 443 + TLS (precisa do IP do servidor, que veio do DNS) → 5º HTTP GET (precisa da conexão TCP/TLS). De cima para baixo: TCP = 4, DHCP = 1, HTTP = 5, ARP = 2, DNS = 3 → **4, 1, 5, 2, 3**.

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Põe o DNS em 1º e o DHCP em 2º. Sem DHCP o host não tem IP nem conhece o servidor DNS. Explora a intuição de que "traduzir o nome é a primeira coisa".
- **B) ❌** — Abre a conexão TCP (3º) antes da consulta DNS (4º). Sem o IP do servidor, não há para onde mandar o SYN.
- **C) ❌** — Põe o ARP antes do DHCP. O ARP Request leva o IP de origem e pergunta pelo IP do gateway, e o host ainda não conhece nenhum dos dois.
- **D) ✅** — DHCP → ARP → DNS → TCP/TLS → HTTP, como em Manual 2.5.

**Base no material:** Manual p. 14 (2.5 "Acompanhando um pacote de ponta a ponta", passos 1–6), p. 31 (5.4.4 ARP request em broadcast, reply em unicast), p. 33 (Tabela 17: DHCP 67/68 UDP, DNS 53, HTTPS 443), p. 35 (Figura 13, três vias), p. 41 (7.3 DNS sobre UDP 53), p. 44 (7.6 DHCP "DORA": Discover em broadcast, Offer, Request, Acknowledge; *lease*).
**Conceito-chave para a prova:** sem IP → DHCP (DORA, UDP 67/68); sem MAC do gateway → ARP; sem IP do servidor → DNS (UDP 53); sem conexão → TCP 3 vias (+TLS na 443); só então HTTP. Variação provável: ordenar só as 4 mensagens do DHCP (Discover → Offer → Request → Acknowledge) ou os passos da resolução DNS (host → DNS local → raiz → TLD → autoritativo).

---

# Parte 2 — Questões adicionais (subtópicos do Manual sem questão conhecida)

> Estilo do Manual ("Questão comentada (estilo ENADE)"): enunciado curto e 5 alternativas (A–E). Os números foram alterados em relação aos Estudos de Caso do Manual, como deve acontecer numa versão de prova.

## I7 — Comutação de circuitos × pacotes
**Subtópico coberto:** 1.3 Comutação de circuitos e de pacotes, multiplexação estatística e *store-and-forward*; agrupa 1.1 (borda/acesso/núcleo) e 1.2 (Manual p. 5–7).
**Por que é provável:** o Manual traz o exemplo numérico de Kurose (10 × 35 usuários) e uma "Analogia para fixar" (restaurante × praça de alimentação). Nenhuma questão conhecida cobra o assunto.
**Prioridade:** Média
**Tipo ENADE:** Afirmativas múltiplas

**Enunciado:**
Uma operadora vai compartilhar um enlace de 1 Mbps entre usuários que, quando ativos, transmitem a 100 kbps, mas ficam ativos apenas 10% do tempo. Avalie as afirmações:

I. Com comutação de circuitos, que reserva para cada usuário uma fração fixa da banda durante toda a sessão, o enlace atende no máximo 10 usuários.

II. Com comutação de pacotes, é possível atender 35 usuários, e a probabilidade de mais de 10 deles estarem ativos ao mesmo tempo é de aproximadamente 0,0004.

III. Na comutação de pacotes, como não há reserva de recursos, o roteador retransmite cada bit assim que ele chega, sem armazenar o pacote inteiro, o que elimina o atraso de fila.

IV. Os roteadores interligados que encaminham pacotes entre as redes formam a borda da rede, onde ficam os sistemas finais que executam as aplicações.

É correto apenas o que se afirma em:

**Alternativas:**
- **A)** I e II.
- **B)** I e III.
- **C)** II e IV.
- **D)** I, II e III.
- **E)** II, III e IV.

**Gabarito: A**

**Julgamento:**
- **I — Verdadeira.** 1 Mbps / 100 kbps = 10 circuitos, ocupados mesmo quando o usuário está calado (o "desperdício" do Manual).
- **II — Verdadeira.** Binomial com n = 35 e p = 0,1: P(X > 10) = 0,000424 (conferido em Python), ou seja, ≈ 0,0004. Atende 3,5 vezes mais usuários com risco quase nulo.
- **III — Falsa.** O roteador usa *store-and-forward*: recebe o pacote **inteiro**, guarda-o num buffer e só então o transmite. Sem reserva, os pacotes disputam o enlace, e é daí que vêm a fila e a perda.
- **IV — Falsa.** A malha de roteadores é o **núcleo** da rede. A borda é a dos sistemas finais (hosts), e a rede de acesso liga a borda ao primeiro roteador.

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — Só I e II são verdadeiras.
- **B) ❌** — Inclui III, que nega o *store-and-forward* e a existência de filas.
- **C) ❌** — Inclui IV (confunde núcleo e borda) e exclui I.
- **D) ❌** — Inclui III.
- **E) ❌** — Inclui III e IV, falsas, e exclui I.

**⚠️ Atenção:** o Manual escreve "inferior a 0,0004"; o valor exato é 0,00042 (Kurose diz "aproximadamente 0,0004"). Se uma versão trouxer "inferior a 0,0004" como afirmativa, a intenção do squad é considerá-la verdadeira.
**Base no material:** Manual p. 6 (Figura 1: borda, acesso, núcleo; 1.2 PAN/LAN/MAN/WAN; 1.3 circuitos × pacotes, *store-and-forward*), p. 7 (ganho estatístico: 10 × 35 usuários).
**Conceito-chave para a prova:** circuitos = reserva, desempenho garantido, desperdício. Pacotes = sem reserva, multiplexação estatística, *store-and-forward*, fila e perda. A Internet usa pacotes.

---

## I8 — Atraso fim a fim
**Subtópico coberto:** 1.4 Métricas de desempenho: atrasos de transmissão e de propagação, vazão/gargalo, produto banda-atraso (Manual p. 7–8).
**Por que é provável:** o Manual tem um Estudo de Caso passo a passo, um box "Confusão clássica: transmissão × propagação" e a competência "dimensões quantitativas" da DCN. Há só o exercício E1, sem questão objetiva.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única (cálculo)

**Enunciado:**
Um pacote de 2.000 bytes atravessa, em série, dois enlaces ligados por um roteador *store-and-forward*. O enlace 1 tem taxa de 20 Mbps e 400 km; o enlace 2 tem taxa de 1 Gbps e 2.000 km. A velocidade de propagação nos dois meios é 2 × 10⁸ m/s, e os atrasos de processamento e de fila são desprezíveis. O atraso fim a fim do pacote é, aproximadamente:

**Alternativas:**
- **A)** 0,82 ms
- **B)** 8,82 ms
- **C)** 12,00 ms
- **D)** 12,82 ms
- **E)** 12,10 ms

**Gabarito: D**

**Cálculo (conferido em Python):** L = 2.000 × 8 = 16.000 bits. d_trans,1 = 16.000 / 20 × 10⁶ = 0,8 ms; d_prop,1 = 4 × 10⁵ / 2 × 10⁸ = 2 ms; d_trans,2 = 16.000 / 10⁹ = 0,016 ms; d_prop,2 = 2 × 10⁶ / 2 × 10⁸ = 10 ms. Total = 0,8 + 2 + 0,016 + 10 = **12,816 ms ≈ 12,82 ms**.

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — 0,816 ms: só os atrasos de transmissão. Esquece a propagação, que domina em WAN.
- **B) ❌** — 8,816 ms: usa 3 × 10⁸ m/s (luz no vácuo) em vez da velocidade dada no meio.
- **C) ❌** — 12 ms: só a propagação. É a "confusão clássica" ao contrário.
- **D) ✅** — Soma as duas transmissões e as duas propagações (*store-and-forward*: o roteador só retransmite depois de receber o pacote inteiro).
- **E) ❌** — 12,102 ms: usa 2.000 **bytes** como se fossem bits no atraso de transmissão (2.000/20 × 10⁶ = 0,1 ms).

**Base no material:** Manual p. 7 (equação 1, d_nodal = d_proc + d_fila + d_trans + d_prop; box "Confusão clássica"; 1.4.2 intensidade de tráfego La/R), p. 8 (1.4.3 vazão = min{R₁, …, R_N}; 1.4.4 produto banda-atraso; Estudo de Caso de 21,32 ms).
**Conceito-chave para a prova:** d_trans = L/R (não depende da distância); d_prop = d/s (não depende do tamanho). Vazão fim a fim = enlace mais lento (aqui, 20 Mbps). Produto banda-atraso do enlace 2: 10⁹ × 0,01 = 10⁷ bits (1,25 MB) "dentro do cabo". Intensidade de tráfego La/R → 1 faz a fila explodir.

---

## I9 — Protocolos, camadas e modelo TCP/IP
**Subtópico coberto:** 1.5 Protocolos e arquitetura em camadas; 2.1–2.2 camadas do TCP/IP, melhor esforço, princípio fim a fim e ampulheta (Manual p. 8–12).
**Por que é provável:** são definições formais com listas (sintaxe/semântica/temporização; serviço/interface/protocolo) e frases de contraste (OSI × TCP/IP), material típico de afirmativa negativa. Nenhuma questão conhecida cobra esses itens.
**Prioridade:** Média
**Tipo ENADE:** Afirmativa negativa

**Enunciado:**
Sobre protocolos, arquitetura em camadas e o modelo TCP/IP, assinale a alternativa **INCORRETA**.

**Alternativas:**
- **A)** Todo protocolo define sintaxe (formato e ordem dos campos), semântica (significado de cada campo e ação correspondente) e temporização (quando e em que velocidade enviar).
- **B)** Serviço é o que uma camada oferece à superior; interface é como a camada superior acessa esse serviço; protocolo é como a camada conversa com sua par no outro equipamento.
- **C)** O IP oferece um serviço de melhor esforço que, embora não garanta a entrega, assegura a ordem dos datagramas e a ausência de duplicatas.
- **D)** No modelo da ampulheta, o IP é o ponto único de convergência: qualquer aplicação funciona sobre qualquer tecnologia física, desde que ambas usem IP.
- **E)** No OSI, o modelo veio antes dos protocolos; no TCP/IP, os protocolos vieram antes do modelo, e a camada de rede é apenas sem conexão.

**Gabarito: C** (a afirmativa incorreta)

**Por que cada alternativa está certa ou errada:**
- **A) ❌ (verdadeira)** — Os três elementos de Tanenbaum (Manual 1.5).
- **B) ❌ (verdadeira)** — "Três conceitos precisam ficar bem separados" (Manual p. 9).
- **C) ✅ (INCORRETA)** — Melhor esforço significa que o IP "tenta entregar, mas não garante ordem, ausência de duplicatas nem a própria entrega" (Manual p. 10). Ordem e eliminação de duplicatas são feitas pelo TCP.
- **D) ❌ (verdadeira)** — Modelo *hourglass* (Manual 2.2), "a razão do sucesso da Internet".
- **E) ❌ (verdadeira)** — As duas diferenças OSI × TCP/IP que o Manual manda guardar (p. 12).

**Base no material:** Manual p. 8–9 (1.5), p. 10 (princípio fim a fim; 4 camadas na RFC 1122 × 5 no modelo híbrido; Figura 3), p. 12 (2.2 ampulheta).
**Conceito-chave para a prova:** IP = melhor esforço, sem conexão, sem garantias; a inteligência fica nas pontas (princípio fim a fim). TCP/IP original tem 4 camadas (aplicação, transporte, internet, acesso à rede); o híbrido de Kurose tem 5.

---

## I10 — Endereços em cada camada e ARP
**Subtópico coberto:** 2.3.1–2.3.2 Desencapsulamento (EtherType, Protocolo, porta) e endereços em cada camada (Tabela 3); agrupa 5.4.4 ARP e ARP spoofing (Manual p. 12–13, 31).
**Por que é provável:** o Manual traz a Tabela 3, uma "Analogia para fixar" (IP = endereço do prédio, MAC = etiqueta de cada trecho, porta = apartamento) e a frase "o IP é fim a fim e o MAC é salto a salto". É pergunta clássica de prova e não tem questão conhecida.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única

**Enunciado:**
O host A (192.168.1.10) envia um datagrama ao servidor S (200.10.5.20). O caminho atravessa o roteador R1 (gateway de A) e depois o roteador R2, que entrega o datagrama a S. Não há NAT. Antes de transmitir, A usou o ARP para descobrir o MAC de R1. Considerando o quadro que trafega no enlace **entre R1 e R2**, os endereços nele contidos são:

**Alternativas:**
- **A)** IP de origem = A; IP de destino = S; MAC de origem = A; MAC de destino = S.
- **B)** IP de origem = R1; IP de destino = R2; MAC de origem = R1; MAC de destino = R2.
- **C)** IP de origem = A; IP de destino = R2; MAC de origem = A; MAC de destino = R2.
- **D)** IP de origem = R1; IP de destino = S; MAC de origem = A; MAC de destino = S.
- **E)** IP de origem = A; IP de destino = S; MAC de origem = interface de saída de R1; MAC de destino = interface de R2 nesse enlace.

**Gabarito: E**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Trata o MAC como fim a fim. O MAC só vale no enlace local; o de S nem é conhecido na rede de A.
- **B) ❌** — Os roteadores não trocam os IPs de origem e destino (sem NAT). Eles só decrementam o TTL e recalculam o checksum do cabeçalho.
- **C) ❌** — Mistura: o IP de destino continua sendo S do começo ao fim, e o MAC de origem muda a cada salto.
- **D) ❌** — Inverte a lógica: muda o IP de origem (fim a fim, não deveria mudar) e mantém os MACs de A e S (salto a salto, deveriam mudar).
- **E) ✅** — IP = fim a fim (A → S o caminho todo). MAC = salto a salto: a cada enlace o roteador desencapsula, consulta a tabela, reencapsula num novo quadro com o seu MAC de saída e o MAC do próximo salto (obtido por ARP).

**Base no material:** Manual p. 12 (2.3.1: EtherType 0x0800/0x86DD, Protocolo 6/17/1, porta 443/53), p. 13 (Tabela 3 e analogia da encomenda), p. 31 (5.4.4: ARP Request em broadcast, Reply em unicast, cache; box "Segurança": ARP spoofing, Dynamic ARP Inspection).
**Conceito-chave para a prova:** porta (16 bits) = processo; IP (32/128 bits) = interface, fim a fim; MAC (48 bits) = placa, salto a salto. ARP: IP → MAC no enlace local, sem autenticação (spoofing → MITM).

---

## I11 — Shannon e Nyquist
**Subtópico coberto:** 3.1 Conceitos básicos de transmissão, decibéis, teoremas de Nyquist e Shannon (Manual p. 14–15).
**Por que é provável:** o Manual traz Estudo de Caso (linha telefônica de 30 dB), as fórmulas destacadas e a ligação com a DCN ("conhecer os limites da computação"). Só existe o exercício E3; a armadilha "S/N em escala linear, não em dB" é perfeita para distratores.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única (cálculo)

**Enunciado:**
Um enlace de rádio ponto a ponto opera com largura de banda de 2 MHz e relação sinal-ruído de 20 dB. A capacidade máxima teórica do canal e o número aproximado de níveis de sinal que, pelo teorema de Nyquist, seriam necessários para atingir essa capacidade são, respectivamente:

**Alternativas:**
- **A)** 4,0 Mbps e 2 níveis.
- **B)** 8,8 Mbps e 5 níveis.
- **C)** 13,3 Mbps e 10 níveis.
- **D)** 26,6 Mbps e 101 níveis.
- **E)** 40,0 Mbps e 1.024 níveis.

**Gabarito: C**

**Cálculo (conferido em Python):** 20 dB ⇒ S/N = 10^(20/10) = 100. Shannon: C = 2 × 10⁶ × log₂(1 + 100) = 2 × 10⁶ × 6,658 = **13,32 Mbps**. Nyquist: 13,32 × 10⁶ = 2 × 2 × 10⁶ × log₂V ⇒ log₂V = 3,33 ⇒ **V ≈ 10 níveis**.

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — 4,0 Mbps = B·log₁₀(101) (usa logaritmo decimal), que também coincide com o Nyquist binário (2B·log₂2). Ignora o teto de Shannon.
- **B) ❌** — 8,78 Mbps = B·log₂(1 + 20): usa o valor em dB direto na fórmula, o erro que o Manual alerta ("S/N em escala linear, não em dB"). Daí V = 2^(8,78/4) ≈ 4,6 ≈ 5.
- **C) ✅** — 13,3 Mbps e ≈ 10 níveis.
- **D) ❌** — 26,6 Mbps = 2B·log₂(101): mistura o fator 2B de Nyquist com a fórmula de Shannon e toma V = 1 + S/N.
- **E) ❌** — 40 Mbps = B × 20 (multiplica a banda pelos dB), e daí V = 2^(40/4) = 1.024.

**Base no material:** Manual p. 15 (equação 5 dB = 10·log₁₀(P₂/P₁); 3 dB = metade, 10 dB = 1/10, 20 dB = 1/100; equações 6 e 7; Estudo de Caso: 3.000 Hz, 30 dB ⇒ ≈ 29,9 kbps e ≈ 32 níveis).
**Conceito-chave para a prova:** Nyquist (sem ruído): C = 2B·log₂V (mais níveis = mais taxa). Shannon (com ruído): C = B·log₂(1 + S/N), S/N linear = 10^(dB/10). Shannon é o teto que nenhuma modulação ultrapassa. Perdas e ganhos em dB se somam (−2 − 0,5 + 10 = +7,5 dB).

---

## I12 — Escolha do meio de transmissão
**Subtópico coberto:** 3.2 Meios guiados (par trançado e categorias, coaxial, fibra multimodo × monomodo) e 3.3 meios não guiados (Tabela 5) (Manual p. 15–17).
**Por que é provável:** "Meios" está no título do Tema 3 ("Meios & Interconexão") e o Manual traz a Tabela 4 (categorias de cabo), a comparação mono × multimodo e a regra "quanto maior a frequência, maior a capacidade e menor o alcance". Não há questão conhecida.
**Prioridade:** Média
**Tipo ENADE:** Resposta única

**Enunciado:**
O campus precisa interligar dois prédios distantes 3 km a 10 Gbps. O trajeto passa ao lado de uma subestação elétrica e de motores industriais (forte interferência eletromagnética), e a equipe de segurança quer dificultar grampos. A solução mais adequada é:

**Alternativas:**
- **A)** Cabo de par trançado Cat 6A, que alcança 10 Gbps e cancela as interferências pelo trançamento dos pares.
- **B)** Fibra óptica multimodo com LED ou VCSEL, mais barata, com núcleo de 50 ou 62,5 µm, adequada a qualquer distância.
- **C)** Enlace de rádio em ondas milimétricas, que tem altíssima capacidade e contorna obstáculos com facilidade.
- **D)** Fibra óptica monomodo com laser, imune a interferência eletromagnética, com baixa atenuação e alcance de dezenas de quilômetros.
- **E)** Cabo coaxial no padrão DOCSIS, cuja malha metálica garante 10 Gbps em qualquer distância.

**Gabarito: D**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Cat 6A dá 10 Gbps só até **100 m** por segmento (Tabela 4). O trançamento reduz interferência, mas cobre não é imune a ela.
- **B) ❌** — A multimodo sofre dispersão modal e fica limitada a **centenas de metros** (uso dentro de prédios e data centers).
- **C) ❌** — Ondas milimétricas têm altíssima capacidade, mas **curto alcance** e são **bloqueadas** por obstáculos (Tabela 5). É o inverso de "contorna obstáculos".
- **D) ✅** — A monomodo (núcleo de ≈ 9 µm, laser) alcança dezenas ou centenas de km, com ≈ 0,2 dB/km a 1.550 nm. A fibra é imune a interferência eletromagnética e difícil de grampear.
- **E) ❌** — Coaxial/DOCSIS é usado em TV e Internet a cabo. Nenhum meio garante taxa "em qualquer distância", porque a atenuação cresce com o comprimento.

**Base no material:** Manual p. 16 (3.2.1 par trançado, Tabela 4: Cat 5e/6/6A/8; 3.2.2 coaxial; 3.2.3 fibra: vantagens, multimodo × monomodo), p. 16–17 (3.3 e Tabela 5: rádio, micro-ondas, mmWave, infravermelho).
**Conceito-chave para a prova:** par trançado: 100 m (Cat 6 dá 10 Gbps só até 55 m; Cat 6A, até 100 m). Multimodo: centenas de m, LED/VCSEL. Monomodo: km, laser, backbones e FTTH. Sem fio: frequência maior = mais capacidade e menos alcance.

---

## I13 — Fragmentação IPv4
**Subtópico coberto:** 4.1 O datagrama IPv4: fragmentação (identificação, flags DF/MF, deslocamento em unidades de 8 bytes), TTL e checksum; ICMP (5.3.2) (Manual p. 20, 29).
**Por que é provável:** os campos do cabeçalho IPv4 aparecem em lista "Campos que mais aparecem em provas" (Figura 7), e o Tema 2 do slide p. 2 cita "estrutura do cabeçalho". Nenhuma questão conhecida cobra o datagrama IPv4. O cálculo é o exemplo clássico de Kurose (4.000 bytes, MTU 1.500).
**Prioridade:** Média
**Tipo ENADE:** Resposta única (cálculo)

**Enunciado:**
Um datagrama IPv4 de 4.000 bytes (cabeçalho de 20 bytes, sem opções) precisa atravessar um enlace com MTU de 1.500 bytes, e a flag DF está desligada. Considerando que o deslocamento (*offset*) é medido em unidades de 8 bytes, o deslocamento, o tamanho total e a flag MF do **último** fragmento são, respectivamente:

**Alternativas:**
- **A)** 2.960; 1.040 bytes; MF = 0.
- **B)** 370; 1.020 bytes; MF = 1.
- **C)** 370; 1.060 bytes; MF = 0.
- **D)** 185; 1.500 bytes; MF = 0.
- **E)** 370; 1.040 bytes; MF = 0.

**Gabarito: E**

**Cálculo (conferido em Python):** dados = 4.000 − 20 = 3.980 bytes. Cada fragmento leva no máximo 1.500 − 20 = 1.480 bytes de dados (múltiplo de 8). Fragmentos: 1.480 + 1.480 + 1.020 = 3.980 ⇒ **3 fragmentos**. Offsets: 0, 1.480/8 = 185 e 2.960/8 = **370**. O último tem 1.020 + 20 = **1.040 bytes** e **MF = 0** (os dois primeiros têm MF = 1).

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — 2.960 é o deslocamento em **bytes**. O campo usa unidades de 8 bytes (2.960/8 = 370).
- **B) ❌** — Esquece o cabeçalho de 20 bytes do próprio fragmento (1.020 são só os dados) e marca MF = 1, que é dos fragmentos que **não** são o último.
- **C) ❌** — 1.060 = 1.040 + 20: tratou os 4.000 bytes como se fossem todos dados (não descontou o cabeçalho original).
- **D) ❌** — Descreve o **segundo** fragmento (offset 185, 1.500 bytes), que ainda teria MF = 1.
- **E) ✅** — offset 370, 1.040 bytes, MF = 0.

**Base no material:** Manual p. 20 (Figura 7; "Identificação, flags e deslocamento ... remontados no destino ... DF proíbe ... MF indica que ainda há fragmentos ... deslocamento em unidades de 8 bytes"; TTL e traceroute; checksum recalculado a cada salto), p. 29 (5.3.2 ICMP: Echo 8/0, Time Exceeded 11, Destination Unreachable 3).
**Conceito-chave para a prova:** remontagem só no destino; offset × 8 = posição em bytes; MF = 0 só no último; com DF = 1 o roteador descarta e avisa por ICMP. TTL −1 por salto; em zero, descarte + ICMP tipo 11 (base do traceroute). O IPv6 não fragmenta nos roteadores.

---

## I14 — VLSM e agregação de rotas
**Subtópico coberto:** 4.4.2 VLSM e 4.4.3 agregação de rotas (superredes) (Manual p. 22–23).
**Por que é provável:** o Manual tem o "Estudo de Caso 2: Planejamento VLSM", a "regra de ouro" (maiores primeiro) e o exemplo de agregação 200.10.0.0/22. As questões conhecidas só cobram sub-redes de tamanho fixo (/26, /23); o VLSM só aparece no exercício E6.
**Prioridade:** Alta
**Tipo ENADE:** Afirmativas múltiplas (cálculo)

**Enunciado:**
Uma empresa recebeu o bloco 200.100.40.0/24 e precisa endereçar: Produção (120 hosts), Administração (60 hosts), Diretoria (25 hosts) e dois enlaces ponto a ponto entre roteadores. O administrador aplica VLSM, alocando as sub-redes em ordem decrescente de tamanho a partir do início do bloco. Avalie as afirmações:

I. A Produção recebe a sub-rede 200.100.40.0/25, com hosts de 200.100.40.1 a 200.100.40.126.

II. A Diretoria recebe a sub-rede 200.100.40.192/27, cujo endereço de broadcast é 200.100.40.223.

III. Após a alocação dos dois enlaces /30, sobram 24 endereços contíguos, de 200.100.40.232 a 200.100.40.255.

IV. Em outro ponto da rede, as redes 10.16.0.0/24 a 10.16.7.0/24 podem ser anunciadas por um único prefixo agregado 10.16.0.0/22.

É correto o que se afirma em:

**Alternativas:**
- **A)** I e II, apenas.
- **B)** I, II e III, apenas.
- **C)** I, III e IV, apenas.
- **D)** II e IV, apenas.
- **E)** I, II, III e IV.

**Gabarito: B**

**Cálculo (conferido em Python, `ipaddress`):**

| Segmento | Necessidade | Máscara (2^h − 2 ≥ N) | Rede | Hosts | Broadcast |
|---|---|---|---|---|---|
| Produção | 120 | /25 (126) | 200.100.40.0 | .1–.126 | .127 |
| Administração | 60 | /26 (62) | 200.100.40.128 | .129–.190 | .191 |
| Diretoria | 25 | /27 (30) | 200.100.40.192 | .193–.222 | .223 |
| Enlace 1 | 2 | /30 (2) | 200.100.40.224 | .225–.226 | .227 |
| Enlace 2 | 2 | /30 (2) | 200.100.40.228 | .229–.230 | .231 |
| Livre | — | — | 200.100.40.232 a .255 | 24 endereços | — |

Agregação: 10.16.0.0 a 10.16.7.255 = 8 redes /24 = 2³ ⇒ 24 − 3 = **/21** (10.16.0.0/21).

**Julgamento:** I — V; II — V; III — V (256 − 232 = 24); IV — **F** (/22 agrega só 4 redes /24, de 10.16.0.0 a 10.16.3.0; para 8 redes é /21).

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Deixa de fora III, que é verdadeira.
- **B) ✅** — I, II e III verdadeiras; IV falsa.
- **C) ❌** — Inclui IV e exclui II.
- **D) ❌** — Exclui I e III e inclui IV.
- **E) ❌** — Inclui IV. O erro é copiar o "/22" do exemplo do Manual, que tinha **4** redes.

**Base no material:** Manual p. 21 (Tabela 9 e equação 9: hosts = 2^h − 2), p. 22 (4.4.2 VLSM, "alocar primeiro as maiores sub-redes"), p. 23 (Estudo de Caso 2: 192.168.1.0/24 → /25, /26, /27, /30, sobram 28; 4.4.3: 200.10.0.0/24 a 200.10.3.0/24 = 200.10.0.0/22).
**Conceito-chave para a prova:** VLSM: menor máscara que atende cada setor (2^h − 2 ≥ N), em ordem decrescente. Enlace ponto a ponto = /30 (ou /31 pela RFC 3021). Agregar 2^k redes contíguas e alinhadas = tirar k bits do prefixo.

---

## I15 — Endereços privados, APIPA e NAPT
**Subtópico coberto:** 4.5 Endereços especiais (Tabela 11), privados (RFC 1918), APIPA, CGNAT e NAT/NAPT (Figura 8); agrupa 4.2.1 classes (Manual p. 21, 23–24).
**Por que é provável:** a Figura 8 traz uma tabela de tradução NAT completa, e o Manual discute os efeitos colaterais do NAT (quebra do fim a fim). Nenhuma questão conhecida cobra o assunto. A faixa 172.16.0.0/12 é pegadinha clássica.
**Prioridade:** Alta
**Tipo ENADE:** Afirmativas múltiplas

**Enunciado:**
Numa rede doméstica 192.168.0.0/24, o roteador faz NAPT com o IP público 189.40.10.7. Sua tabela de tradução contém: 189.40.10.7:6001 ↔ 192.168.0.11:51000 e 189.40.10.7:6002 ↔ 192.168.0.12:51000. Avalie as afirmações:

I. Um segmento de resposta vindo de 142.250.0.10:443 com destino 189.40.10.7:6002 será entregue ao host 192.168.0.12, na porta 51000.

II. O endereço 172.32.10.1 pertence à faixa privada da RFC 1918, assim como 172.20.10.1.

III. Um computador que se autoconfigura com um endereço 169.254.x.x indica que não obteve resposta de um servidor DHCP.

IV. O NAT preserva o princípio fim a fim, pois um host externo pode iniciar uma conexão com 192.168.0.11 sem nenhuma configuração de encaminhamento de portas.

É correto apenas o que se afirma em:

**Alternativas:**
- **A)** I e II.
- **B)** II e IV.
- **C)** I, II e III.
- **D)** I e III.
- **E)** I, III e IV.

**Gabarito: D**

**Julgamento:**
- **I — Verdadeira.** No NAPT, a **porta** pública identifica a associação. Os dois hosts usam a mesma porta interna (51000), e é a porta pública (6001 × 6002) que os distingue.
- **II — Falsa.** A faixa privada é 172.16.0.0/12 = 172.16.0.0 a **172.31**.255.255. 172.20.10.1 é privado; 172.32.10.1 **não** é (conferido em Python).
- **III — Verdadeira.** 169.254.0.0/16 = link-local/APIPA, "autoconfiguração quando o DHCP falha".
- **IV — Falsa.** O NAT **quebra** o princípio fim a fim. Um host externo não inicia conexão com um host interno sem encaminhamento de portas, o que dificulta P2P e VoIP.

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Inclui II.
- **B) ❌** — II e IV são justamente as falsas.
- **C) ❌** — Inclui II.
- **D) ✅** — Só I e III.
- **E) ❌** — Inclui IV.

**Base no material:** Manual p. 21 (Tabela 8: classes A–E; 127.x = loopback; desperdício das classes), p. 23 (Tabela 11: RFC 1918, 127.0.0.0/8, 169.254.0.0/16, 100.64.0.0/10 CGNAT, 0.0.0.0, 255.255.255.255, 224.0.0.0/4; 4.5.1 NAT/NAPT; esgotamento IANA 2011 e LACNIC 2020), p. 24 (Figura 8; efeitos colaterais do NAT).
**Conceito-chave para a prova:** privados: 10/8, 172.16/12 (até 172.31), 192.168/16. APIPA 169.254/16; CGNAT 100.64/10; loopback 127/8. NAPT traduz IP **e porta**; o NAT é "paliativo" até o IPv6 e quebra o fim a fim.

---

## I16 — Dijkstra a partir de z
**Subtópico coberto:** 5.2.1 Algoritmo de Dijkstra (estado de enlace) (Manual p. 27–28, Figura 9).
**Por que é provável:** o Manual tem a Figura 9 e uma tabela passo a passo (Estudo de Caso a partir de u), e o Tema 5 está no slide "Sub-redes CIDR & Protocolos de Roteamento". Só existe o exercício E8; rodar o mesmo grafo a partir de outro nó é a "versão alterada" mais provável.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única (algoritmo)

**Enunciado:**
Considere o grafo da Figura 9 do Manual, não direcionado, com os custos: u–v = 2, u–w = 5, u–x = 1, v–w = 3, v–x = 2, x–w = 3, w–y = 1, w–z = 5, x–y = 1, y–z = 2. Executando o algoritmo de Dijkstra **a partir do nó z**, o custo mínimo de z até u e o caminho correspondente são:

**Alternativas:**
- **A)** 4, pelo caminho z – y – x – u.
- **B)** 10, pelo caminho z – w – u.
- **C)** 8, pelo caminho z – y – w – u.
- **D)** 9, pelo caminho z – w – x – u.
- **E)** 7, pelo caminho z – y – x – v – u.

**Gabarito: A**

**Execução (conferida em Python):**

| Passo | N' | D(y),p | D(w),p | D(x),p | D(u),p | D(v),p |
|---|---|---|---|---|---|---|
| 0 | z | **2,z** | 5,z | ∞ | ∞ | ∞ |
| 1 | zy | – | 3,y | 3,y | ∞ | ∞ |
| 2 | zyw | – | – | **3,y** | 8,w | 6,w |
| 3 | zywx | – | – | – | **4,x** | 5,x |
| 4 | zywxu | – | – | – | – | **5,x** |
| 5 | zywxuv | – | – | – | – | – |

No passo 1 há empate entre w e x (ambos 3); a escolha não altera os custos finais. Custos finais: y = 2, w = 3, x = 3, u = 4, v = 5. Todos saem de z pelo enlace (z, y).

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — 2 + 1 + 1 = 4.
- **B) ❌** — Escolhe o caminho com menos saltos (pensamento de RIP), e não o de menor custo: 5 + 5 = 10.
- **C) ❌** — z–y–w custa 3, mas o enlace w–u custa 5 (total 8). Passar por x é mais barato.
- **D) ❌** — Usa o enlace direto z–w (5), mais caro que z–y–w (3): 5 + 3 + 1 = 9.
- **E) ❌** — Desvio desnecessário por v: 2 + 1 + 2 + 2 = 7.

**Base no material:** Manual p. 27 (Tabela 15 LS × DV; 5.2.1, equação 11: D(v) ← min{D(v), D(w) + c(w,v)}), p. 28 (Figura 9 e tabela do Estudo de Caso a partir de u; complexidade O(n²) ou O(|E| log n) com heap).
**Conceito-chave para a prova:** a cada passo entra em N' o nó de menor D ainda não definitivo, e relaxam-se os vizinhos. O resultado é a árvore de menores caminhos e a tabela de encaminhamento (próximo salto). OSPF/IS-IS usam Dijkstra; métrica = custo, não saltos.

---

## I17 — Bellman-Ford (vetor de distâncias)
**Subtópico coberto:** 5.2.2 Vetor de distâncias, equação de Bellman-Ford e contagem ao infinito (Manual p. 28).
**Por que é provável:** o Manual dá a equação (12), a leitura em palavras ("meu custo até y é o menor valor entre ...") e o problema da contagem ao infinito com as mitigações. A Questão 6 dos slides só diz que o RIP "opera iterativamente" com saltos; não há cálculo de DV.
**Prioridade:** Média
**Tipo ENADE:** Resposta única (cálculo)

**Enunciado:**
Num roteamento por vetor de distâncias, o roteador x tem três vizinhos: v (custo do enlace x–v = 2), w (custo 7) e y (custo 1). Os vetores de distância recebidos informam D_v(z) = 5, D_w(z) = 1 e D_y(z) = 8. Pela equação de Bellman-Ford, a nova estimativa D_x(z) e o vizinho usado como próximo salto são:

**Alternativas:**
- **A)** 8, via w.
- **B)** 9, via y.
- **C)** 1, via w.
- **D)** 7, via v.
- **E)** 3, via y e v.

**Gabarito: D**

**Cálculo:** D_x(z) = min{c(x,v) + D_v(z); c(x,w) + D_w(z); c(x,y) + D_y(z)} = min{2 + 5; 7 + 1; 1 + 8} = min{7; 8; 9} = **7, via v**.

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Escolhe o vizinho que anuncia o menor D (w diz 1), mas esquece o custo do enlace até ele (7): 7 + 1 = 8.
- **B) ❌** — Escolhe o enlace mais barato (y, custo 1), mas y está longe de z (8): 1 + 8 = 9.
- **C) ❌** — Copia o menor valor anunciado sem somar o custo do enlace.
- **D) ✅** — 2 + 5 = 7 é o mínimo; próximo salto v.
- **E) ❌** — Soma custos de enlaces sem sentido (1 + 2). O DV escolhe **um** vizinho.

**Base no material:** Manual p. 28 (equação 12; "iterativo, assíncrono e distribuído"; "boas notícias se espalham rápido, más notícias devagar"; contagem ao infinito até 16 no RIP; *split horizon*, *poisoned reverse*, *hold-down timers*), p. 27 (Tabela 15: DV troca a tabela só com vizinhos, convergência lenta, erro se propaga).
**Conceito-chave para a prova:** D_x(y) = min_v{c(x,v) + D_v(y)}. DV = Bellman-Ford distribuído (RIP; o BGP é vetor de caminhos). Contagem ao infinito: após falha de enlace, os vizinhos se enganam mutuamente até o "infinito" (16 saltos no RIP); mitigações: horizonte dividido, envenenamento reverso, *hold-down*.

---

## I18 — Escolha de rota no BGP
**Subtópico coberto:** 5.3 Roteamento na Internet: sistemas autônomos, IGP × EGP, Tabela 16 e critérios de escolha do BGP (Manual p. 29).
**Por que é provável:** o Manual lista a ordem de decisão do BGP e destaca que "o BGP não busca necessariamente o caminho mais rápido". A Tabela 16 compara RIP, OSPF, IS-IS, EIGRP e BGP com portas e métricas, que dão bons distratores. Não há questão conhecida sobre roteamento inter-AS.
**Prioridade:** Média
**Tipo ENADE:** Resposta única

**Enunciado:**
O provedor AS 65010 recebe, por BGP, duas rotas para o prefixo 177.50.0.0/16. Rota 1: *local preference* 200 e AS-PATH com 4 sistemas autônomos. Rota 2: *local preference* 100 e AS-PATH com 2 sistemas autônomos. Seguindo a ordem de decisão descrita no Manual, o BGP escolherá:

**Alternativas:**
- **A)** a Rota 2, porque o BGP sempre escolhe o menor AS-PATH, que corresponde ao caminho de menor latência.
- **B)** a Rota 1, porque a maior *local preference*, definida pela política do administrador, é avaliada antes do comprimento do AS-PATH.
- **C)** a Rota 2, porque o OSPF executado entre os sistemas autônomos calcula o menor custo com base na largura de banda.
- **D)** as duas rotas, em balanceamento, porque o BGP divide o tráfego igualmente entre caminhos para o mesmo prefixo.
- **E)** nenhuma delas, porque o BGP roda sobre UDP 520 e descarta rotas com mais de 15 saltos.

**Gabarito: B**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — O AS-PATH é só o 2º critério. Além disso, menos ASes não significa menor latência: o BGP segue **política e acordos comerciais**, não o caminho mais rápido.
- **B) ✅** — Ordem: (1) maior *local preference*; (2) menor AS-PATH; (3) próximo salto mais próximo (batata quente); (4) desempates. A Rota 1 vence no 1º critério.
- **C) ❌** — O OSPF é IGP (intra-AS). Entre ASes, o único EGP usado na prática é o BGP.
- **D) ❌** — O Manual não descreve balanceamento como regra do BGP; ele escolhe a melhor rota pelos critérios em ordem.
- **E) ❌** — UDP 520 e limite de 15 saltos são do **RIP**. O BGP roda sobre **TCP 179** e evita laços pelo AS-PATH.

**Base no material:** Manual p. 29 (5.3: AS e ASN; IGP foca desempenho, EGP foca política; Tabela 16; "Como o BGP escolhe a rota?"; 5.3.2 ICMP).
**Conceito-chave para a prova:** intra-AS (IGP: RIP, OSPF, IS-IS, EIGRP) = desempenho; inter-AS (EGP: BGP-4) = política. BGP: vetor de caminhos, TCP 179, AS-PATH evita laços, local pref > AS-PATH > batata quente. OSPF: protocolo IP 89, áreas (área 0 = backbone).

---

## I19 — Cálculo do CRC
**Subtópico coberto:** 5.4.1 Detecção de erros: paridade simples e bidimensional, checksum e CRC (Manual p. 29–30).
**Por que é provável:** o Manual tem o Estudo de Caso do CRC com divisão XOR detalhada e o Tema 5 cita "quadros Ethernet" (FCS = CRC-32). Só existe o exercício E9; trocar D e G é a versão alterada natural.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única (cálculo)

**Enunciado:**
Um enlace usa CRC com gerador G = 1011 (r = 3). Para os dados D = 110101, os bits de CRC (R) e o quadro transmitido são, respectivamente:

**Alternativas:**
- **A)** R = 011; quadro 110101011.
- **B)** R = 1111; quadro 1101011111.
- **C)** R = 110; quadro 110101110.
- **D)** R = 111; quadro 111110101.
- **E)** R = 111; quadro 110101111.

**Gabarito: E**

**Cálculo (divisão módulo 2, conferida em Python):**
```
110101000   <- D + 3 zeros
1011        <- XOR
---------
011001000
 1011
---------
001111000
  1011
---------
000100000
   1011
---------
000001100
     1011
---------
000000111   <- resto R = 111
```
Quadro: D seguido de R = **110101 111**. Verificação: 110101111 ÷ 1011 dá resto 000.

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — 011 é o resto do exemplo do Manual (D = 101110, G = 1001). Decorar o resultado não serve quando os dados mudam.
- **B) ❌** — Acrescenta r = 4 bits (o tamanho de G). O gerador tem r + 1 bits, então R tem r = 3 bits.
- **C) ❌** — 110 é o resto da divisão **decimal** comum (424 mod 11 = 6), com "vai um" e empréstimos. O CRC usa XOR, sem "vai um".
- **D) ❌** — O resto está certo, mas foi colocado **antes** dos dados. O quadro é D seguido de R.
- **E) ✅** — R = 111, quadro 110101111.

**Base no material:** Manual p. 29 (5.4: serviços do enlace; 5.4.1 paridade simples, paridade 2D que corrige 1 bit, checksum em complemento de 1, CRC; Ethernet usa CRC-32), p. 30 (Estudo de Caso: passos 1–3, verificação no receptor; "detecta todas as rajadas de até r bits").
**Conceito-chave para a prova:** acrescentar r zeros (r = grau de G = nº de bits de G − 1), dividir por XOR, anexar o resto. Receptor: resto ≠ 0 ⇒ descarta. Paridade simples falha com 2 bits invertidos; a 2D detecta e corrige erro de 1 bit; checksum é usado no IP/TCP/UDP.

---

## I20 — CSMA/CD × CSMA/CA
**Subtópico coberto:** 5.4.2 Protocolos de acesso múltiplo e CSMA/CD com recuo exponencial binário; 5.4.3 tamanho mínimo do quadro; agrupa 9.1–9.2.3 (terminal oculto, CSMA/CA, RTS/CTS) (Manual p. 30–31, 50–52).
**Por que é provável:** a Questão 1 dos slides cita o "recuo exponencial do CSMA/CD", e o Manual explica a fórmula de K e a Figura 21 (terminal oculto). Nenhuma questão conhecida cobra acesso ao meio.
**Prioridade:** Média
**Tipo ENADE:** Afirmativas múltiplas

**Enunciado:**
Avalie as afirmações sobre o controle de acesso ao meio em redes locais:

I. No CSMA/CD, após a terceira colisão consecutiva de um quadro, o nó sorteia K em {0, 1, …, 7} e espera K × 512 tempos de bit; num Ethernet de 10 Mbps, a espera máxima é de 358,4 µs.

II. O Wi-Fi utiliza CSMA/CD, porque o ponto de acesso detecta as colisões e avisa as estações com um sinal de *jam*.

III. No problema do terminal oculto, duas estações que não se escutam, mas alcançam o mesmo AP, transmitem ao mesmo tempo; o uso opcional de RTS/CTS mitiga o problema, pois o CTS do AP é ouvido inclusive pelas estações "ocultas".

IV. O tamanho mínimo do quadro Ethernet (64 bytes) existe para que, no meio compartilhado, a transmissão dure o suficiente para a colisão ser detectada antes do fim do envio.

É correto o que se afirma em:

**Alternativas:**
- **A)** I e II, apenas.
- **B)** II e III, apenas.
- **C)** I, III e IV, apenas.
- **D)** II, III e IV, apenas.
- **E)** I, II, III e IV.

**Gabarito: C**

**Julgamento:**
- **I — Verdadeira.** K ∈ {0, …, 2^min(n,10) − 1}; com n = 3, K ∈ {0, …, 7}. Tempo de bit a 10 Mbps = 0,1 µs; 512 tempos de bit = 51,2 µs; máximo 7 × 51,2 = **358,4 µs** (conferido).
- **II — Falsa.** O Wi-Fi usa **CSMA/CA** (prevenção). Um rádio não consegue "ouvir" enquanto transmite e há o terminal oculto, por isso não dá para detectar colisões; usa-se ACK na camada de enlace e recuo aleatório.
- **III — Verdadeira.** Figura 21 e 9.2.2 do Manual.
- **IV — Verdadeira.** 46 bytes mínimos de dados ⇒ 64 bytes de quadro (Manual 5.4.3).

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Inclui II.
- **B) ❌** — Inclui II e exclui I e IV.
- **C) ✅** — I, III e IV.
- **D) ❌** — Inclui II e exclui I.
- **E) ❌** — Inclui II.

**Base no material:** Manual p. 29–30 (5.4.2: divisão de canal TDMA/FDMA/CDMA, acesso aleatório ALOHA/CSMA/CSMA/CD/CSMA/CA, revezamento), p. 31 (CSMA/CD, *jam*, recuo exponencial; Figura 10; tamanho mínimo), p. 50–51 (9.1 atenuação, interferência, multipercurso, SNR × BER, adaptação de taxa; Figura 21), p. 51–52 (9.2.1 BSS/ESS/ad hoc, beacon; 9.2.2 DIFS/SIFS/ACK/RTS-CTS; Tabela 26 gerações).
**Conceito-chave para a prova:** Ethernet compartilhado = CSMA/CD (detecta e recua); com switch full-duplex, não há colisões. Wi-Fi = CSMA/CA (evita, com ACK e recuo que congela com canal ocupado; RTS/CTS contra terminal oculto). Wi-Fi 6 = OFDMA; 6E = faixa de 6 GHz; Wi-Fi 7 = canais de 320 MHz.

---

## I21 — Portas e sockets
**Subtópico coberto:** 6.1 Serviços da camada de transporte e 6.2 portas (faixas IANA, Tabela 17) e sockets (demultiplexação UDP × TCP) (Manual p. 32–33).
**Por que é provável:** o slide p. 2 do Tema 7 enfatiza "portas"; o Manual traz a Tabela 17 e a diferença dupla × quádrupla. Nenhuma questão conhecida cobra demultiplexação.
**Prioridade:** Média
**Tipo ENADE:** Resposta única

**Enunciado:**
Um servidor (IP 200.1.1.10) executa um serviço HTTPS (TCP 443) e um servidor DNS (UDP 53). Dois navegadores de uma mesma residência, atrás de NAT (mesmo IP público 189.40.10.7), conectam-se à porta 443 com as portas de origem 50001 e 50002. Ao mesmo tempo, dois hosts de redes diferentes enviam consultas à porta 53. É correto afirmar que:

**Alternativas:**
- **A)** os dois fluxos TCP chegam ao mesmo socket, pois têm o mesmo IP e a mesma porta de destino, e o servidor os separa pelo número de sequência.
- **B)** os fluxos TCP vão para sockets distintos, porque o socket TCP é identificado pela quádrupla (IP e porta de origem, IP e porta de destino); já as consultas UDP chegam ao mesmo socket, identificado por (IP de destino, porta de destino).
- **C)** as consultas UDP vão para sockets distintos, pois o UDP mantém estado de conexão por cliente, como o TCP.
- **D)** as portas 50001 e 50002 são portas bem conhecidas (0 a 1.023), reservadas pela IANA para navegadores.
- **E)** como o TCP e o UDP garantem atraso máximo, o servidor DNS responderá às duas consultas dentro de um prazo fixo.

**Gabarito: B**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — O TCP demultiplexa pela quádrupla; as portas de origem diferentes (50001 × 50002) já separam os sockets. O número de sequência ordena bytes dentro de **uma** conexão.
- **B) ✅** — É a diferença descrita no Manual: um servidor web na 443 "cria um socket separado para cada cliente conectado"; no UDP, datagramas de origens diferentes para a mesma porta chegam ao mesmo socket.
- **C) ❌** — O UDP é sem conexão e sem estado; por isso o servidor DNS aguenta muitos clientes.
- **D) ❌** — 50001 e 50002 estão na faixa **dinâmica/efêmera** (49.152 a 65.535), escolhida pelo SO para o lado cliente. Bem conhecidas = 0 a 1.023; registradas = 1.024 a 49.151.
- **E) ❌** — "Nenhum dos dois protocolos oferece garantia de atraso máximo ou de vazão mínima" (Manual 6.1).

**Base no material:** Manual p. 32 (6.1 serviços: multiplexação, checksum, confiabilidade/fluxo/congestionamento só no TCP; sem garantia de atraso; 6.2 faixas IANA; socket UDP = dupla), p. 33 (Tabela 17 de portas; socket TCP = quádrupla).
**Conceito-chave para a prova:** porta = 16 bits. 0–1.023 bem conhecidas; 1.024–49.151 registradas (3306 MySQL, 3389 RDP, 5432 PostgreSQL); 49.152–65.535 efêmeras. UDP: socket = (IP dst, porta dst). TCP: socket = (IP src, porta src, IP dst, porta dst). Portas: 20/21 FTP, 22 SSH, 23 Telnet, 25/587 SMTP, 53 DNS, 67/68 DHCP, 80 HTTP, 110 POP3, 123 NTP, 143 IMAP, 161/162 SNMP, 443 HTTPS, 993 IMAPS.
