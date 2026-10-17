# Segurança da Informação — Questões e Gabarito Comentado

**Squad responsável:** Squad 4 (Enrico Nalini Genaro, Giovani Maia Tirapani, Giovanna Santos Silva, Murilo Vinicius de Faveri, Rafael Platero Brandani, Thais Gabriel)
**Materiais analisados:**
| Arquivo | Páginas | Tipo | Questões encontradas (páginas) |
|---|---|---|---|
| `Aula Enade - Segurança da Informação.pdf` | 20 | Slides | Q1–Q4, questões do squad no estilo ENADE com gabarito comentado (p. 5–6, 9–10, 13–14, 17–18); Q9, "Questões para análise" discursivas (p. 16) |
| `Material Completo - Segurança da Informação.pdf` | 28 | Apostila (material explicativo) | Q5–Q8, questões oficiais do ENADE (2017 Q15, 2017 Q16, 2021 Q12, 2021 Q24) reproduzidas de forma resumida, com gabarito oficial e julgamento de cada afirmação (p. 23–25; citadas também nas p. 12, 15, 21 e 26) |

**Resumo:** 9 questões encontradas. 8 trazem gabarito no próprio material: Q1–Q4 com gabarito comentado nos slides e Q5–Q8 com gabarito oficial do Inep citado na apostila. 1 é discursiva e não tem resposta no material (Q9, resposta esperada elaborada aqui).
- As 4 questões objetivas dos slides (Q1–Q4) **não aparecem na apostila**. As 4 questões oficiais da apostila (Q5–Q8) **não aparecem nos slides**. Nenhuma questão está repetida entre os dois arquivos, então não há "duas versões" de uma mesma questão. Há, porém, pares do mesmo tema (Q3 ↔ Q5, Q4 ↔ Q7, Q1/Q2 ↔ Q8) e diferenças de definição entre slides e apostila. Tudo isso está registrado na seção [Comparação entre os dois arquivos](#comparação-entre-os-dois-arquivos).
- Nas questões Q5–Q8 a apostila **não reproduz o enunciado completo nem as alternativas A–E** da prova oficial. Ela traz apenas o tema, as afirmações resumidas, o julgamento de cada uma e a letra do gabarito oficial.

> Legenda: ✅ correta · ❌ incorreta · ⚠️ ponto de atenção (gabarito do material duvidoso, ambiguidade, versão divergente)

## Índice
1. [Q1 — Princípios de segurança no prontuário eletrônico](#q1--princípios-de-segurança-no-prontuário-eletrônico)
2. [Q2 — Escolha de mecanismos criptográficos para telemedicina](#q2--escolha-de-mecanismos-criptográficos-para-telemedicina)
3. [Q3 — ARP spoofing e proteção com TLS](#q3--arp-spoofing-e-proteção-com-tls)
4. [Q4 — LGPD dados sensíveis anonimização e pseudonimização](#q4--lgpd-dados-sensíveis-anonimização-e-pseudonimização)
5. [Q5 — ENADE 2017 Q15 ARP spoofing em rede Wi-Fi](#q5--enade-2017-q15-arp-spoofing-em-rede-wi-fi)
6. [Q6 — ENADE 2017 Q16 segurança como processo e ética](#q6--enade-2017-q16-segurança-como-processo-e-ética)
7. [Q7 — ENADE 2021 Q12 LGPD](#q7--enade-2021-q12-lgpd)
8. [Q8 — ENADE 2021 Q24 criptografia de ponta a ponta](#q8--enade-2021-q24-criptografia-de-ponta-a-ponta)
9. [Q9 — Biometria facial para controle de presença](#q9--biometria-facial-para-controle-de-presença)
10. [Comparação entre os dois arquivos](#comparação-entre-os-dois-arquivos)
11. [Outros conteúdos em formato de exercício e observações gerais](#outros-conteúdos-em-formato-de-exercício-e-observações-gerais)

---

## Q1 — Princípios de segurança no prontuário eletrônico
**Fonte:** `Aula Enade - Segurança da Informação.pdf`, p. 5 (enunciado) e p. 6 (gabarito comentado). Não consta na apostila.
**Tipo ENADE:** Afirmativas múltiplas ("É correto o que se afirma em"), com situação-problema descrita em ocorrências

**Enunciado:**
Um hospital de grande porte modernizou sua infraestrutura de tecnologia implementando um sistema de Prontuário Eletrônico do Paciente (PEP). A arquitetura de segurança da informação adotada engloba controle de acesso baseado em papéis (RBAC), criptografia simétrica (AES-256) para dados em repouso, assinaturas digitais baseadas em infraestrutura de chave pública (ICP) com certificados X.509 para prescrições, além de replicação de servidores para alta disponibilidade.

Durante uma auditoria de conformidade com a ISO/IEC 27001 e a LGPD, foram registradas as seguintes ocorrências:

**I.** Um técnico de enfermagem utilizou temporariamente as credenciais de acesso de um médico plantonista — obtidas por negligência na guarda de senha — para visualizar históricos clínicos de pacientes alocados em alas sob a responsabilidade de outra equipe, sem que o sistema disparasse alertas de desvio de perfil, embora o acesso tenha sido registrado em log.

**II.** Um ataque de negação de serviço distribuído (DDoS) exauriu os recursos da infraestrutura de borda, tornando o PEP inacessível por 45 minutos nas unidades de terapia intensiva e violando o Acordo de Nível de Serviço (SLA) de continuidade operacional.

**III.** Uma prescrição digital foi assinada com a chave privada de um médico, mas, devido a uma vulnerabilidade na função de hash subjacente (geradora de colisões), um atacante conseguiu alterar o conteúdo do arquivo prescrito sem que a verificação da assinatura digital pela farmácia apontasse falha.

**IV.** Um administrador de banco de dados mal-intencionado alterou diretamente os registros de um diagnóstico sensível na tabela transacional; contudo, visto que o armazenamento utilizava criptografia simétrica convencional (AES-256) voltada exclusivamente à confidencialidade, a adulteração passou despercebida pelos mecanismos de verificação de integridade.

Considerando os conceitos fundamentais da Segurança da Informação, avalie as afirmativas a seguir:

**I.** A ocorrência I evidencia uma falha grave de _confidencialidade_ e de controle de acesso, comprometendo também a confiabilidade da autoria devido ao compartilhamento inadequado de credenciais.

**II.** A ocorrência II caracteriza uma violação direta da propriedade de _disponibilidade_, essencial em ambientes críticos de saúde onde a demora na informação pode colocar vidas em risco.

**III.** A ocorrência III ilustra um comprometimento da _integridade_, demonstrando que a fragilidade na função matemática de _hash_ que alimenta a assinatura digital pode quebrar a garantia de imutabilidade do documento.

**IV.** A ocorrência IV reforça que cifras simétricas tradicionais focadas na _confidencialidade_ (como o AES em modos básicos) não garantem, por si sós, a _integridade_ dos dados contra modificações não autorizadas.

É correto o que se afirma em:

**Alternativas:**
- **A)** Apenas I e II.
- **B)** Apenas III e IV.
- **C)** Apenas I, II e III.
- **D)** Apenas II, III e IV.
- **E)** I, II, III e IV.

**Gabarito: E** — _(origem: gabarito do próprio material, p. 6: "Alternativa correta: E (I, II, III e IV)")_

**Julgamento das afirmativas:**
- **I — Verdadeira.** O técnico viu prontuários de pacientes fora da sua equipe e do seu papel. É acesso por pessoa não autorizada, ou seja, quebra de **confidencialidade** e falha de controle de acesso: o RBAC foi contornado com credencial alheia e não houve alerta de desvio de perfil. O log grava a conta do médico, não a pessoa que agiu, então a **autenticidade/responsabilização (não repúdio)** também fica comprometida. Gabarito do material: "a auditoria não conseguirá vincular a ação ao agente real".
- **II — Verdadeira.** O DDoS deixou o sistema inacessível quando ele era necessário, em plena UTI. É violação de **disponibilidade**. A replicação de servidores não basta contra exaustão da borda.
- **III — Verdadeira.** A assinatura digital é calculada sobre o **resumo (hash)** do documento. Se o hash admite colisões, dois conteúdos diferentes geram o mesmo resumo e a assinatura continua válida para o conteúdo adulterado. A **integridade** (e a autenticidade do conteúdo) deixa de ser garantida.
- **IV — Verdadeira.** O AES em modos sem autenticação (ECB, CBC, CTR) só garante **confidencialidade**. Sem MAC/HMAC ou modo autenticado (AES-GCM, CCM), uma alteração não é detectada. Gabarito do material: "não previne modificações maliciosas [...] se não houver mecanismos integrados de autenticação de mensagens ou hashing (como o AES-GCM ou uso de HMAC)".

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Deixa de fora III e IV, que são verdadeiras. Atrai quem só reconhece os casos óbvios: acesso indevido e DDoS.
- **B) ❌** — Deixa de fora I e II, justamente as violações mais diretas de confidencialidade e disponibilidade.
- **C) ❌** — Exclui IV. É a armadilha de quem acha que "AES-256 é forte, logo protege tudo". Criptografia simétrica sem modo autenticado não garante integridade.
- **D) ❌** — Exclui I. Atrai quem acha que o caso é "só" de autenticação, ou que o registro em log resolve o problema. Houve acesso por pessoa não autorizada, e isso é quebra de confidencialidade.
- **E) ✅** — As quatro afirmativas associam corretamente cada ocorrência ao princípio violado.

**⚠️ Atenção:**
- No slide, os termos destacados aparecem com **asteriscos literais**, restos de formatação Markdown: "\*confidencialidade\*", "\*disponibilidade\*", "\*integridade, demonstrando…" (asterisco sem fechamento), "\*hash que alimenta…". Aqui eles foram transcritos em itálico. O sentido não muda.
- Ocorrências e afirmativas usam a **mesma numeração I–IV**, o que pode confundir. A afirmativa *n* comenta a ocorrência *n*.
- Na ocorrência IV, o problema real é um **insider com acesso legítimo** ao banco. Mesmo com AES-GCM, quem altera os dados pelo próprio SGBD, que tem as chaves, gera dados "íntegros" do ponto de vista criptográfico. Contra isso, os controles são trilha de auditoria protegida, separação de funções e mínimo privilégio. A afirmativa IV, como afirmação geral ("AES em modo básico não garante integridade"), continua correta, e o gabarito E se mantém.

**Conceito-chave para a prova:** Confidencialidade = só quem tem autorização acessa. Integridade = detectar ou impedir alteração. Disponibilidade = acessível quando necessário. Autenticidade/não repúdio = atribuir a ação a quem a fez. Hash fraco (com colisões) quebra a integridade da assinatura. AES sem modo autenticado (GCM) ou HMAC não garante integridade.

---

## Q2 — Escolha de mecanismos criptográficos para telemedicina
**Fonte:** `Aula Enade - Segurança da Informação.pdf`, p. 9 (enunciado) e p. 10 (gabarito comentado). Não consta na apostila.
**Tipo ENADE:** Resposta única (situação-problema + escolha da combinação mais adequada)

**Enunciado:**
Um grande conglomerado hospitalar está estruturando sua nova plataforma digital de telemedicina e gestão de prontuários eletrônicos em nuvem. A arquitetura exige que o sistema atenda simultaneamente a três pilares rigorosos:

**1. Dados em Repouso:** Armazenamento massivo de exames de imagem de alta resolução e prontuários volumosos em bancos de dados relacionais, exigindo alta performance de leitura/escrita e proteção robusta contra vazamentos.
**2. Dados em Trânsito:** Comunicação síncrona, de baixíssima latência e criptografada entre os aplicativos móveis dos médicos em campo e a infraestrutura central de servidores via internet aberta.
**3. Integridade e Autenticidade Transacional:** Assinatura digital de prescrições médicas de alta complexidade com validade jurídica perante órgãos reguladores (ICP-Brasil).

A equipe de arquitetura de segurança da informação foi encarregada de selecionar os mecanismos criptográficos ideais para cumprir os requisitos de desempenho, confidencialidade, integridade e conformidade regulatória.

Considerando as propriedades matemáticas e operacionais dos algoritmos e protocolos de segurança, qual é a combinação de mecanismos técnica e arquiteturalmente mais adequada?

**Alternativas:**
- **A)** Empregar criptografia assimétrica (RSA com chaves de 4096 bits) tanto para o armazenamento em repouso quanto para o tráfego de rede, visto que o uso exclusivo de chaves públicas e privadas elimina a necessidade de gestão complexa de chaves simétricas e garante máxima segurança matemática.
- **B)** Utilizar criptografia simétrica de bloco (como o AES-256 em modo autenticado GCM) para os dados em repouso e o protocolo TLS moderno para os dados em trânsito (utilizando criptografia assimétrica apenas no handshake para autenticação e troca segura de chaves, e simétrica para o fluxo contínuo de dados), garantindo desempenho, confidencialidade e integridade integradas.
- **C)** Aplicar funções criptográficas de dispersão unidirecional (como o SHA-3/512) para cifrar e proteger o conteúdo dos dados tanto em repouso quanto em trânsito, aproveitando a propriedade de irreversibilidade do hash para impedir qualquer visualização indevida por terceiros.
- **D)** Adotar algoritmos de derivação de chaves e salting (como Argon2id) em conjunto com criptografia assimétrica pura para todo o tráfego de rede, dispensando o uso de protocolos de sessão para simplificar a camada de transporte e evitar sobrecarga de processamento.
- **E)** Utilizar exclusivamente assinaturas digitais baseadas em curvas elípticas (ECDSA) para a cifra de grandes volumes de dados em repouso e em trânsito, pois a eficiência matemática das curvas elípticas substitui com vantagens o desempenho do AES em qualquer cenário de armazenamento.

**Gabarito: B** — _(origem: gabarito do próprio material, p. 10: "Alternativa correta: B")_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — A criptografia assimétrica é ordens de grandeza mais lenta que a simétrica. Usá-la para gigabytes de imagens e prontuários criaria um gargalo inaceitável (gabarito, p. 10). Além disso, o RSA só cifra blocos menores que o módulo (cerca de 446 bytes com RSA-4096/OAEP), por isso na prática só é usado para cifrar chaves. O RSA também não "elimina a gestão de chaves": exige PKI, certificados e revogação.
- **B) ✅** — Dados em repouso volumosos pedem cifra simétrica rápida. O AES-256-**GCM** é modo autenticado e entrega confidencialidade e integridade juntas. Em trânsito, o **TLS** é um esquema **híbrido**: usa assimétrica (RSA/ECDHE/ECDSA) no handshake para autenticar o servidor por certificado e negociar a chave de sessão, e depois cifra simétrica autenticada para o fluxo de dados (gabarito, p. 10).
- **C) ❌** — Hash **não cifra**. É unidirecional, serve para resumo e integridade, e nem o próprio dono consegue recuperar os dados. "Cifrar com SHA-3" tornaria os prontuários irrecuperáveis.
- **D) ❌** — Argon2id é uma função de derivação/hash de **senhas**, feita de propósito para ser lenta e cara em memória, contra força bruta e tabelas rainbow. Não serve para cifrar fluxos de dados. Dispensar um protocolo de sessão (TLS) e usar assimétrica pura para todo o tráfego é inseguro e lento.
- **E) ❌** — ECDSA é algoritmo de **assinatura**, não de cifragem. Não cifra dados e não substitui o AES. As curvas elípticas são eficientes para assinatura e troca de chaves (ECDHE), não para cifragem em massa.

**⚠️ Atenção:**
- A alternativa B **não trata explicitamente o pilar 3** (assinatura digital de prescrições com certificado ICP-Brasil, por exemplo RSA ou ECDSA sobre hash SHA-256). Mesmo assim, é a única alternativa sem erro técnico. Se a prova trouxer uma versão alterada em que alguma alternativa inclua "AES-GCM + TLS + **assinatura digital com certificado ICP-Brasil**", essa será a mais completa.
- O gabarito do slide tem exageros e um erro de digitação: "segurança impenetrável", "arquitetura híbrida perfeita", "(Incorretaconfundida)" na análise da C, e asteriscos literais em "\*não cifram" e "\*hash". Nada disso muda a resposta.

**Conceito-chave para a prova:** Grande volume → simétrica (AES, de preferência em modo autenticado GCM). Canal → TLS híbrido (assimétrica só no handshake). Hash não cifra. Argon2id/bcrypt/scrypt/PBKDF2 são para **senhas**. ECDSA **assina**, não cifra.

---

## Q3 — ARP spoofing e proteção com TLS
**Fonte:** `Aula Enade - Segurança da Informação.pdf`, p. 13 (enunciado) e p. 14 (gabarito comentado). Não consta na apostila (tema relacionado à Q5/ENADE 2017 Q15 da apostila).
**Tipo ENADE:** Asserção-razão

**Enunciado:**
Em uma rede corporativa legada, o setor de segurança da informação identificou vulnerabilidades críticas na Camada de Enlace (Camada 2 do modelo OSI), permitindo que agentes maliciosos executem ataques de envenenamento de cache para desviar o fluxo de pacotes de dados. Para mitigar o impacto dessa exposição sem paralisar as operações, a equipe arquitetou contramedidas baseadas em criptografia de sessão e validação estrita de certificados.

Considerando esse cenário técnico de defesa em profundidade e os protocolos envolvidos, avalie as asserções a seguir e a relação proposta entre elas:

**I.** A implementação rigorosa do protocolo TLS (Transport Layer Security) com validação mandatória de certificados e políticas de HSTS (HTTP Strict Transport Security) protege a confidencialidade e a integridade dos dados trafegados contra interceptações ativas, mesmo que o atacante tenha obtido sucesso em redirecionar o tráfego da rede local, embora o TLS não corrija a falha estrutural do protocolo ARP.

**PORQUE**

**II.** O protocolo ARP (Address Resolution Protocol) carece de mecanismos nativos de autenticação, integridade ou criptografia na Camada 2, aceitando cegamente respostas e pacotes Gratuitous ARP não solicitados, o que corrompe as tabelas de mapeamento IP-MAC dos dispositivos e viabiliza a criação furtiva de cenários de Homem no Meio (Man-in-the-Middle).

A respeito dessas asserções, assinale a opção correta:

**Alternativas:**
- **A)** As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
- **B)** As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
- **C)** A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
- **D)** A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
- **E)** As asserções I e II são proposições falsas.

**Gabarito: A** — _(origem: gabarito do próprio material, p. 14: "A alternativa correta é a A: as duas asserções são verdadeiras, e a II justifica corretamente a I.")_

**Julgamento:**
- **Asserção I — Verdadeira.** Mesmo que o ARP spoofing desvie os pacotes para o atacante, o TLS com certificado validado autentica o servidor e cifra o conteúdo com integridade. O atacante só vê dados cifrados e não consegue alterá-los sem ser detectado. O HSTS impede o rebaixamento para HTTP (SSL stripping) e impede o usuário de "aceitar" um certificado inválido. O TLS protege a aplicação, mas não conserta o ARP: é defesa em profundidade (gabarito, p. 14).
- **Asserção II — Verdadeira.** O ARP não tem autenticação. Hosts aceitam respostas não solicitadas e Gratuitous ARP, o que permite envenenar o cache IP→MAC e montar um MitM (gabarito, p. 14).
- **Relação — segundo o material, II justifica I:** "A fragilidade estrutural do ARP descrita na II [...] é exatamente a motivação lógica e técnica pela qual a contramedida descrita na I [...] se torna indispensável" (p. 14).

**Por que cada alternativa está certa ou errada:**
- **A) ✅ (gabarito do material)** — As duas asserções são verdadeiras, e o material considera que a falta de autenticação do ARP (II) explica por que é preciso proteger o canal na camada superior e por que o TLS "não corrige" o ARP (I).
- **B) ❌ (segundo o material; ver ⚠️)** — Seria a resposta para quem entende que II explica o **ataque**, não a **eficácia** do TLS.
- **C) ❌** — II é verdadeira: o ARP realmente não tem autenticação.
- **D) ❌** — I é verdadeira: com validação de certificado e HSTS, o TLS protege confidencialidade e integridade mesmo com o tráfego desviado.
- **E) ❌** — As duas asserções são verdadeiras.

**⚠️ Atenção:** A relação de justificativa é **discutível**. No modelo ENADE, "II justifica I" significa que II explica **por que I é verdadeira**. A asserção I diz que o TLS protege os dados mesmo com tráfego desviado. O motivo disso é que o TLS faz autenticação e cifragem **fim a fim, independentes das camadas inferiores**, e não o fato de o ARP não ter autenticação. A II explica por que o ataque é possível e por que a contramedida é **necessária** (o próprio gabarito usa a palavra "motivação"), não por que ela é **eficaz**. Numa leitura estrita, **B** também seria defensável. **Para a prova, o gabarito do squad é A.** Se a versão da prova vier com o mesmo texto, marque A. Se a II for reescrita de forma a não ter relação causal com a I (por exemplo, falando de outra camada ou de outro protocolo), a resposta passa a ser B.
Outros detalhes: o TLS **não** protege a disponibilidade (o atacante no meio pode descartar pacotes) nem metadados como IPs e volume de tráfego. "Criptografia de ponta a ponta", termo usado no gabarito, no TLS significa cliente↔servidor.

**Relação com o outro arquivo:** A apostila (p. 12, 14, 23–24) traz o mesmo raciocínio: "TLS limita o que um intermediário consegue ler ou alterar, mas não impede sozinho a falsificação ARP" (p. 24). Na tabela da Figura 5 (p. 14), a mitigação de ARP spoofing é "DAI, segmentação, TLS, monitoramento". Nos slides (p. 12), o controle de ARP spoofing é "Proteção e segmentação da rede" e o de MITM é "TLS e validação de certificado".

**Conceito-chave para a prova:** ARP não autentica → ARP spoofing/poisoning → MitM. A correção na camada 2 é DAI (Dynamic ARP Inspection), segmentação e entradas estáticas. TLS com validação de certificado e HSTS protege confidencialidade e integridade do conteúdo, mas não corrige o ARP nem garante disponibilidade.

---

## Q4 — LGPD dados sensíveis anonimização e pseudonimização
**Fonte:** `Aula Enade - Segurança da Informação.pdf`, p. 17 (enunciado) e p. 18 (gabarito comentado). Não consta na apostila (tema relacionado à Q7/ENADE 2021 Q12 da apostila).
**Tipo ENADE:** Afirmativas múltiplas

**Enunciado:**
Uma holding corporativa do setor de saúde e biotecnologia está estruturando um ambicioso projeto de Big Data e inteligência artificial para o desenvolvimento de modelos preditivos voltados a diagnósticos precoces. Para mitigar riscos regulatórios perante a Autoridade Nacional de Proteção de Dados (ANPD) e garantir a conformidade com a Lei Geral de Proteção de Dados (LGPD - Lei nº 13.709/2018), o comitê de governança e conformidade jurídica foi acionado para orientar a equipe de engenharia de dados sobre o ciclo de vida, a taxonomia e as técnicas de tratamento das informações dos pacientes.

Considerando os conceitos dogmáticos e legais estabelecidos pela LGPD, avalie as afirmativas a seguir:

**I.** Dados pessoais relativos à saúde humana e dados biométricos vinculados a uma pessoa natural identificada ou identificável recebem a qualificação jurídica de **dados pessoais sensíveis**, exigindo, por regra geral, o cumprimento de hipóteses legais mais restritivas para o seu tratamento e vedando o seu uso discriminatório.

**II.** A técnica de **pseudonimização** consiste no tratamento por meio do qual um dado perde a possibilidade de associação, direta ou indireta, a um indivíduo, fazendo com que, imediatamente após a sua aplicação, o conjunto de dados deixe irrevogavelmente de ser considerado dado pessoal para todos os efeitos legais da LGPD.

**III.** Para que se configure a **anonimização** efetiva sob a ótica legal da LGPD, o processo deve ser irreversível, considerando o uso de meios técnicos disponíveis e razoáveis na ocasião do tratamento; caso a associação com a pessoa possa ser restabelecida por meios lógicos ou tecnológicos viáveis, o dado permanece juridicamente classificado como pessoal.

**IV.** O conceito legal de **tratamento** de dados pessoais possui acepção ampla, abrangendo qualquer operação realizada com dados pessoais, tais como a coleta, produção, recepção, classificação, utilização, acesso, reprodução, transmissão, distribuição, processamento, arquivamento, armazenamento, eliminação ou modificação.

É correto o que se afirma em:

**Alternativas:**
- **A)** Apenas I e II.
- **B)** Apenas II e III.
- **C)** Apenas I e IV.
- **D)** Apenas II, III e IV.
- **E)** Apenas I, III e IV.

**Gabarito: E** — _(origem: gabarito do próprio material, p. 18: "A alternativa correta é a E, pois as afirmações I, III e IV estão corretas.")_

**Julgamento das afirmativas:**
- **I — Verdadeira.** Pelo art. 5º, II, dado referente à saúde e dado genético ou biométrico vinculado a pessoa natural são **dados pessoais sensíveis**. O art. 11 restringe as hipóteses de tratamento, e o princípio da não discriminação (art. 6º, IX) proíbe uso discriminatório ilícito ou abusivo.
- **II — Falsa.** A afirmativa atribui à pseudonimização a definição de **anonimização** e acrescenta "irrevogavelmente deixa de ser dado pessoal". Na pseudonimização (art. 13, § 4º), a associação **ainda é possível com informação adicional** guardada à parte pelo controlador. Por isso, dado pseudonimizado **continua sendo dado pessoal** (gabarito, p. 18).
- **III — Verdadeira.** Pelo art. 12, dado anonimizado não é dado pessoal, **salvo** se a anonimização puder ser revertida com meios próprios ou com **esforços razoáveis**. Se a reidentificação for viável, o dado continua pessoal.
- **IV — Verdadeira.** O art. 5º, X, define tratamento como "toda operação realizada com dados pessoais", com lista ampla que vai da coleta à eliminação, incluindo modificação.

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Inclui II (falsa) e omite III e IV.
- **B) ❌** — Inclui II (falsa) e omite I e IV.
- **C) ❌** — Omite III, que é verdadeira. Atrai quem acha que a III "inventou" a exigência de irreversibilidade.
- **D) ❌** — Inclui II, a armadilha central: confundir pseudonimização com anonimização.
- **E) ✅** — I, III e IV são verdadeiras e II é falsa.

**⚠️ Atenção:** O gabarito comentado do slide (p. 18) **cita errado o art. 12** na justificativa da III: "salvo quando o processo de anonimização puder ser revertido com **esforço desproporcional** ou quando forem utilizados meios razoáveis". O texto da lei diz o contrário: "salvo quando o processo de anonimização [...] for revertido, utilizando exclusivamente meios próprios, ou quando, **com esforços razoáveis**, puder ser revertido". Se a reversão exige esforço **desproporcional**, o dado **continua anonimizado**. O gabarito (E) está correto, mas não decore essa frase do slide. Se a prova trocar "esforços razoáveis" por "esforço desproporcional" numa afirmativa, essa afirmativa fica **falsa**.

**Relação com o outro arquivo:** A apostila não reproduz esta questão. Ela traz as mesmas definições na p. 21 (tabela "Conceito LGPD"), na p. 24 (ENADE 2021 Q12: "dados anonimizados nunca são pessoais mesmo se a anonimização puder ser revertida" = Falsa) e na p. 25 (quadro "Anonimização e pseudonimização"). As diferenças de redação entre slides e apostila estão na seção de comparação.

**Conceito-chave para a prova:** Saúde, biometria, genética, religião, origem racial, opinião política, vida sexual e filiação sindical são dados **sensíveis**. **Anonimização** efetiva com meios razoáveis faz o dado deixar de ser pessoal; se for reversível com esforço razoável, o dado continua pessoal. **Pseudonimização** sempre deixa o dado como pessoal. **Tratamento** é qualquer operação.

---

## Q5 — ENADE 2017 Q15 ARP spoofing em rede Wi-Fi
**Fonte:** `Material Completo - Segurança da Informação.pdf`, p. 23–24, seção "15.1 Questão 15 do ENADE 2017". Também citada na p. 12 ("O ENADE 2017 usou a ideia de TLS e certificados para discutir autenticação e negociação de chaves em um cenário de ataque de homem no meio") e na p. 15 ("A questão 15 de 2017 explora exatamente a necessidade de escolher controles compatíveis com a causa do ataque"). Não consta nos slides.
**Tipo ENADE:** Afirmativas múltiplas (questão oficial do ENADE 2017, Ciência da Computação)

**Enunciado (como reproduzido no material — o texto integral, o cenário completo e as alternativas A–E da prova NÃO constam no PDF):**
Tema: ataque de homem no meio por ARP spoofing em rede Wi-Fi.

Afirmações (resumidas pelo material):

**I.** Uso de protocolo com chave pública para negociar chaves individuais, como TLS.
**II.** Firewall no ponto de acesso evita o desvio entre clientes da mesma sub-rede.
**III.** Certificado do ponto de acesso autenticável com chave pública confiável.
**IV.** Substituir chaves fracas por 128 bits e limitar dispositivos compatíveis.

**Alternativas:** não reproduzidas no material. A apostila informa apenas que a letra do gabarito oficial é **D**, que "corresponde às afirmações I, III e IV".

**Gabarito: D (I, III e IV)** — _(origem: gabarito oficial do Inep citado no material, p. 23)_

**Julgamento das afirmações (material, p. 23, complementado):**
- **I — Verdadeira.** "A autenticação criptográfica e a negociação segura ajudam a impedir que o intermediário estabeleça sessões confiáveis sem ser detectado." Chaves individuais negociadas com autenticação por chave pública (como no TLS) impedem que o MitM leia ou forje o tráfego.
- **II — Falsa.** "Firewall genérico não corrige necessariamente o envenenamento ARP. O problema exige controles de camada 2, autenticação e proteção fim a fim." Um firewall filtra fluxos conforme política, mas não autentica o AP e não impede a comunicação entre clientes na mesma camada 2 (p. 14–15).
- **III — Verdadeira.** "Certificados podem vincular identidade e chave quando a cadeia é validada." Um AP autenticável por certificado (por exemplo, 802.1X/EAP-TLS) impede o "evil twin" e a falsificação.
- **IV — Verdadeira no contexto da questão.** "Aumentar a força criptográfica e impedir modos legados reduz a vulnerabilidade de força bruta descrita no item." O material não explica o cenário original; pela redação, a prova falava de chaves curtas sujeitas a força bruta.

**Como chegar à alternativa (as alternativas não estão no material):** qualquer alternativa que contenha **II** está errada. Qualquer uma que omita I, III ou IV também. Sobra apenas a combinação "I, III e IV".

**⚠️ Atenção:** A questão está **incompleta** no material: faltam o enunciado original, os dados do cenário e o texto das alternativas. A afirmação IV é "verdadeira no contexto", e o próprio material não detalha esse contexto. Para estudar com o texto completo, consulte a prova e o gabarito oficiais do ENADE 2017 (Inep), que estão nas referências da apostila (p. 27).
"Aprendizado" do material (p. 23–24): "Não escolha um controle apenas porque ele 'é de segurança'. Relacione mecanismo e causa. ARP spoofing ocorre na resolução local IP–MAC; TLS limita o que um intermediário consegue ler ou alterar, mas não impede sozinho a falsificação ARP."

**Conceito-chave para a prova:** Contra MitM por ARP spoofing funcionam autenticação criptográfica fim a fim (TLS, certificados) e controles de camada 2 (DAI, 802.1X, segmentação). Firewall **não** resolve ARP spoofing dentro da mesma sub-rede.

---

## Q6 — ENADE 2017 Q16 segurança como processo e ética
**Fonte:** `Material Completo - Segurança da Informação.pdf`, p. 24, seção "15.2 Questão 16 do ENADE 2017". Também citada na p. 21 ("A questão 16 de 2017 reforça que segurança é processo e que ética e comportamento humano integram o problema"). Não consta nos slides.
**Tipo ENADE:** Afirmativas múltiplas (questão oficial do ENADE 2017, Ciência da Computação)

**Enunciado (como reproduzido no material — o texto integral e as alternativas NÃO constam no PDF):**
Tema: segurança como processo, fator humano, engenharia social e ética.

Afirmações (resumidas pelo material):

**I.** Organizações permanecem vulneráveis diante do fator humano.
**II.** Segurança da Informação é processo, não produto.
**III.** Ética profissional é relevante.

**Alternativas:** não reproduzidas no material. A letra do gabarito oficial é **E**, "com as três afirmações consideradas corretas".

**Gabarito: E (I, II e III)** — _(origem: gabarito oficial do Inep citado no material, p. 24)_

**Julgamento das afirmações (material, p. 24):**
- **I — Verdadeira.** "O sentido cobrado é que controles técnicos não eliminam riscos de comportamento e manipulação." A engenharia social (phishing, pretexting) explora pessoas, não tecnologia. Ressalva do material: "Em prática profissional, evite tratar pessoas como causa única". Na p. 21: "Dizer que 'o humano é sempre o elo mais fraco' simplifica em excesso".
- **II — Verdadeira.** "Riscos, ativos, ameaças e tecnologia mudam; controles exigem ciclo de gestão e melhoria." É o ciclo PDCA do SGSI (ISO/IEC 27001) e as funções do NIST CSF 2.0.
- **III — Verdadeira.** "Profissionais possuem acesso privilegiado, tomam decisões e devem considerar deveres, impactos e responsabilidade."

**Como chegar à alternativa:** as três afirmações são verdadeiras, logo vale a alternativa que contém I, II e III.

**⚠️ Atenção:** Questão **incompleta** no material: faltam o enunciado (provavelmente um texto-base sobre engenharia social) e as alternativas. Numa versão alterada, desconfie de termos absolutos: "o humano é **sempre** o elo mais fraco", "um produto/ferramenta **garante** a segurança", "ética **não** é responsabilidade técnica". Esse tipo de afirmação tende a ser falsa.

**Conceito-chave para a prova:** Segurança é **processo** contínuo (gestão de riscos, melhoria contínua), não produto. O fator humano (engenharia social) exige controles administrativos (treinamento, políticas) além dos técnicos. Ética profissional faz parte da segurança.

---

## Q7 — ENADE 2021 Q12 LGPD
**Fonte:** `Material Completo - Segurança da Informação.pdf`, p. 24, seção "15.3 Questão 12 do ENADE 2021". Também citada na p. 21 ("Ponto cobrado em 2021: Dado que pode ser reidentificado com meios próprios ou esforços razoáveis não deve ser tratado automaticamente como anônimo. A ANPD fiscaliza e regulamenta dentro de sua competência, mas não 'modifica a lei'."). Não consta nos slides, mas o slide 16 repete "A ANPD não modifica leis".
**Tipo ENADE:** Afirmativas múltiplas (questão oficial do ENADE 2021, Ciência da Computação)

**Enunciado (como reproduzido no material — o texto integral e as alternativas NÃO constam no PDF):**
Tema: LGPD.

Afirmações (resumidas pelo material):

**I.** A lei restringe tratamento indiscriminado de dados sensíveis.
**II.** Dados anonimizados nunca são pessoais mesmo se a anonimização puder ser revertida.
**III.** Titular pode confirmar tratamento e pedir correção ou eliminação nas condições legais.
**IV.** ANPD fiscaliza, regula e modifica a legislação.

**Alternativas:** não reproduzidas no material. A letra do gabarito oficial é **B**, "correspondente às afirmações I e III".

**Gabarito: B (I e III)** — _(origem: gabarito oficial do Inep citado no material, p. 24)_

**Julgamento das afirmações (material, p. 24, complementado):**
- **I — Verdadeira.** "Dados sensíveis recebem regime específico e exigem hipótese legal e salvaguardas" (art. 11).
- **II — Falsa.** "Se a associação puder ser revertida por meios próprios ou esforços razoáveis, a exclusão do regime de dado pessoal não é automática" (art. 12). O erro está no "nunca".
- **III — Verdadeira.** "A LGPD prevê direitos do titular; a eliminação depende do contexto e das exceções legais." Art. 18: confirmação da existência de tratamento, acesso, correção, anonimização/bloqueio/eliminação, portabilidade etc.
- **IV — Falsa.** "A Autoridade regulamenta e fiscaliza em sua competência, mas alteração de lei depende do processo legislativo." A ANPD edita regulamentos (art. 55-J), mas não altera lei.

**Como chegar à alternativa:** I e III verdadeiras, II e IV falsas. Vale a alternativa "I e III".

**⚠️ Atenção:** Questão **incompleta** no material: faltam o enunciado e as alternativas. A afirmação II é a mesma armadilha da afirmativa III da Q4 dos slides, vista pelo lado oposto: anonimização reversível com esforço razoável **não** exclui o dado da LGPD.

**Conceito-chave para a prova:** Dado sensível tem regime restrito. Anonimizado só deixa de ser pessoal se a reversão não for possível com meios próprios nem com esforços razoáveis. O titular tem direitos de confirmação, acesso, correção e eliminação (art. 18). A ANPD regulamenta e fiscaliza, **não modifica a lei**.

---

## Q8 — ENADE 2021 Q24 criptografia de ponta a ponta
**Fonte:** `Material Completo - Segurança da Informação.pdf`, p. 24–25, seção "15.4 Questão 24 do ENADE 2021". Não consta nos slides.
**Tipo ENADE:** Afirmativas múltiplas (questão oficial do ENADE 2021, Ciência da Computação)

**Enunciado (como reproduzido no material — o texto integral, a descrição do protocolo e as alternativas NÃO constam no PDF):**
Tema: criptografia de ponta a ponta.

Afirmações (resumidas pelo material):

**I.** Chave pública do remetente permite verificar autenticidade de assinatura.
**II.** IV variável oculta padrões e pode contribuir contra repetição no protocolo descrito.
**III.** AES é simétrico porque usa um par de chaves diferentes.
**IV.** SHA-256 pode detectar alteração pela comparação de resumos.

(Na afirmação II, "IV" é o vetor de inicialização, *Initialization Vector*.)

**Alternativas:** não reproduzidas no material. A letra do gabarito oficial é **E**, "correspondente às afirmações I, II e IV".

**Gabarito: E (I, II e IV)** — _(origem: gabarito oficial do Inep citado no material, p. 24)_

**Julgamento das afirmações (material, p. 24–25, complementado):**
- **I — Verdadeira.** "A verificação funciona se a chave pública estiver corretamente vinculada ao remetente e o protocolo usar assinatura adequada." Assina-se com a chave **privada** do remetente e verifica-se com a **pública** dele.
- **II — Verdadeira no contexto.** "Variação por mensagem evita resultados repetidos; proteção contra replay também depende de estado, contadores ou autenticação do protocolo." Com IV/nonce diferente a cada mensagem, mensagens iguais geram cifrados diferentes. A apostila (p. 11) lembra que reutilizar o IV onde a especificação proíbe compromete confidencialidade e integridade.
- **III — Falsa.** "AES é simétrico: a mesma chave secreta é usada para cifrar e decifrar. Par pública/privada caracteriza criptografia assimétrica." A justificativa ("porque usa um par de chaves diferentes") é a definição de assimétrica.
- **IV — Verdadeira com ressalva.** "Hash detecta mudança acidental ou quando o valor esperado é confiável. Contra atacante ativo, usa-se MAC ou assinatura para autenticar o resumo." Um atacante pode recalcular o SHA-256 do conteúdo alterado. Por isso, sozinho, o hash não autentica.

**Como chegar à alternativa:** III é falsa e I, II e IV são verdadeiras. Vale a alternativa "I, II e IV".

**⚠️ Atenção:** Questão **incompleta** no material: faltam o enunciado com o protocolo descrito e as alternativas. Os julgamentos de II ("verdadeira no contexto") e IV ("verdadeira com ressalva") dependem do texto original. Numa versão alterada, se a afirmação disser que o SHA-256 "garante a autenticidade" ou "impede" a alteração por atacante, ela fica **falsa**.

**Conceito-chave para a prova:** Assinatura usa privada do remetente para assinar e pública do remetente para verificar. AES é **simétrico**, com uma única chave secreta. IV/nonce variável evita padrões repetidos. Hash detecta alteração, mas só **autentica** quando combinado com chave (HMAC) ou assinatura.

---

## Q9 — Biometria facial para controle de presença
**Fonte:** `Aula Enade - Segurança da Informação.pdf`, p. 16 (slide "Biometria para controle de presença"). Não consta na apostila; conceitos relacionados nas p. 12 (biometria como fator de autenticação) e 21 (LGPD, privacy by design).
**Tipo ENADE:** Discursiva / estudo de caso ("Questões para análise", sem resposta no material)

**Enunciado:**
Situação: Uma universidade pretende usar reconhecimento facial para registrar presença.

Questões para análise:
1. A coleta é realmente necessária?
2. Existe uma alternativa menos invasiva?
3. Qual é a finalidade?
4. Por quanto tempo os dados serão mantidos?
5. Como a biometria será protegida?
6. O estudante poderá contestar erros?
7. O sistema foi avaliado quanto a vieses?

[Quadro "Atenção" no mesmo slide: "Consentimento não é a única base legal; Consentimento não autoriza qualquer finalidade; Pseudonimização não elimina todos os riscos; A ANPD não modifica leis; Dados públicos continuam sujeitos a regras de tratamento; Coletar mais dados do que o necessário contraria a minimização."]

**Resposta esperada:** _(não consta no material — elaborada aqui com base nos slides p. 15–16, na apostila p. 12 e 21 e na LGPD)_
- **Natureza do dado:** biometria facial vinculada ao estudante é **dado pessoal sensível** (art. 5º, II). O tratamento só pode ocorrer nas hipóteses restritas do art. 11 e exige salvaguardas reforçadas.
- **1–2. Necessidade e alternativa menos invasiva:** pelo princípio da **necessidade/minimização** (art. 6º, III), se chamada, QR code, cartão ou registro no sistema acadêmico cumprem a finalidade, a biometria é **excessiva**. "Coletar mais dados do que o necessário contraria a minimização" (slide 16).
- **3. Finalidade:** deve ser específica, explícita e informada (art. 6º, I e VI). A finalidade "registrar presença" não autoriza reuso para vigilância, segurança patrimonial ou outros fins. "Consentimento não autoriza qualquer finalidade" (slide 16).
- **Base legal:** o consentimento "não é a única base legal". Na relação aluno–universidade, que tem desequilíbrio de poder, o consentimento pode não ser livre. Se a biometria for adotada, deve haver opção alternativa sem prejuízo ao aluno.
- **4. Retenção:** prazo definido e eliminação ao fim da finalidade ou do vínculo (arts. 15–16).
- **5. Proteção:** guardar **templates** em vez de imagens, com criptografia em repouso e em trânsito, controle de acesso por mínimo privilégio, logs protegidos e plano de incidentes. Biometria vazada não pode ser "trocada" (apostila p. 12: impossibilidade prática de "trocar o dedo"). Recomenda-se **Relatório de Impacto à Proteção de Dados (RIPD)** (art. 38) e privacy by design (apostila p. 21).
- **6. Contestação:** o titular tem direito de acesso e correção (art. 18) e de pedir **revisão de decisões automatizadas** (art. 20). Uma falta registrada por erro de reconhecimento deve poder ser contestada.
- **7. Vieses:** avaliar taxas de falso positivo e falso negativo por grupo demográfico, para cumprir o princípio da **não discriminação** (art. 6º, IX). Reconhecimento facial tem histórico de erro maior em certos grupos.
- **Conclusão esperada:** a universidade só deveria adotar a biometria se demonstrar necessidade e proporcionalidade, base legal adequada, transparência, segurança, retenção limitada, canal de contestação e avaliação de vieses. Caso contrário, deve preferir uma alternativa menos invasiva.

**Conceito-chave para a prova:** Biometria é dado sensível. Avalie finalidade, necessidade/minimização, base legal (consentimento não é a única nem autoriza tudo), segurança, retenção, direitos do titular (inclusive revisão de decisão automatizada) e não discriminação.

---

## Comparação entre os dois arquivos

**1. Questões repetidas:** nenhuma. As Q1–Q4 só existem nos slides e as Q5–Q8 só na apostila. A apostila não traz as questões criadas pelo squad, e os slides não reproduzem as questões oficiais do ENADE. Os pares temáticos (mesmo assunto, questões diferentes) são:

| Questão dos slides | Questão da apostila com o mesmo tema | Ponto comum / diferença |
|---|---|---|
| Q3 (ARP spoofing + TLS, asserção-razão) | Q5 (ENADE 2017 Q15, ARP spoofing em Wi-Fi) | Ambas: TLS e certificados protegem o conteúdo, mas não corrigem o ARP. A Q5 acrescenta que **firewall não resolve** ARP spoofing na mesma sub-rede e cita chaves de 128 bits. A Q3 acrescenta **HSTS**. |
| Q4 (LGPD: sensível, pseudonimização, anonimização, tratamento) | Q7 (ENADE 2021 Q12, LGPD) | Ambas cobram dado sensível e anonimização reversível = continua pessoal. A Q7 cobra também **direitos do titular** e "**ANPD não modifica a lei**". A Q4 cobra **pseudonimização** e o conceito amplo de **tratamento**. |
| Q1 (CIA; hash com colisão; AES sem integridade) e Q2 (AES-GCM, TLS, hash não cifra) | Q8 (ENADE 2021 Q24, criptografia de ponta a ponta) | Ambas: AES é simétrico; hash detecta alteração mas não cifra; assinatura usa chave privada/pública. A Q8 acrescenta **IV/nonce** e a ressalva de que hash sozinho não protege contra atacante ativo. |
| — | Q6 (ENADE 2017 Q16, processo, fator humano e ética) | Sem questão correspondente nos slides. Os slides só tocam o tema em "Phishing → MFA, filtros e treinamento" (p. 12). |

**2. Diferenças de definição e de redação entre slides e apostila** (úteis se a prova alterar termos):

| Tema | Slides (`Aula Enade…`) | Apostila (`Material Completo…`) |
|---|---|---|
| Princípios | p. 3: 5 princípios (Confidencialidade, Integridade, Disponibilidade, Autenticidade, Não repúdio). Resumo p. 19 cita só CIA. | p. 5–6: 6 princípios, acrescenta **Responsabilização** ("É possível atribuir ações a uma entidade?") entre Autenticidade e Não repúdio. |
| Pergunta da Integridade | "Os dados permanecem corretos?" | "É possível detectar ou impedir alteração indevida?" |
| Hash | p. 7: "Verificação de integridade", sem ressalva. | p. 10 e 25: hash sozinho **não garante** autoria nem protege contra atacante ativo; "Hash simples não identifica autor"; para isso, MAC ou assinatura. |
| AES | Q1/Q2: AES em modos básicos (CBC/ECB) não garante integridade; GCM sim. | p. 10: "AES: Confidencialidade; com modo autenticado, integridade". p. 11: blocos de 128 bits, chaves de 128/192/256 bits, IV/nonce. Conteúdo coerente. |
| Etapas de identidade | p. 11: Identificação, Autenticação, Autorização, Auditoria. Exemplo de autenticação: "Senha e Token". | p. 12: acrescenta **Accountability**. Exemplo: "Senha + chave de segurança"; auditoria = "Log assinado de alteração de nota". Também: "Senha e PIN são ambos conhecimento" (não é MFA). |
| Controle para ARP spoofing | p. 12: "Proteção e segmentação da rede" (TLS aparece só para MITM). | p. 14: "DAI, segmentação, TLS, monitoramento". |
| Dado pessoal sensível | p. 15: "Biometria, saúde, religião e origem racial". | p. 21: lista completa (origem racial ou étnica, convicção religiosa, opinião política, saúde, vida sexual, genética ou biometria vinculada). |
| Anonimização | p. 15: "Associação razoável com a pessoa deixa de ser possível". | p. 21: "Uso de meios razoáveis disponíveis para retirar possibilidade de associação direta ou indireta". p. 25: "Anonimização efetiva rompe associação razoável". |
| Pseudonimização | p. 15: "Associação depende de informação adicional" (slide grafa "**Pseudominização**", erro de digitação). | p. 21: "Substitui identificadores, mas permite reidentificação com informação adicional protegida". |
| Tratamento | p. 15: "Coleta, uso, armazenamento, compartilhamento ou eliminação". Q4-IV traz a lista longa do art. 5º, X. | p. 21: "Operações como coleta, uso, acesso, armazenamento, comunicação e eliminação". |
| Princípios da LGPD | p. 15: Finalidade, Necessidade, Transparência, Segurança, Prevenção. Resumo p. 19: "finalidade, necessidade, proteção e direitos do titular". | p. 21: lista completa (finalidade, adequação, necessidade, livre acesso, qualidade, transparência, segurança, prevenção, não discriminação, responsabilização). |
| Gabaritos | Q1–Q4 com gabarito comentado próprio. | Q5–Q8 com gabarito **oficial** do Inep (2017 Q15 = D; 2017 Q16 = E; 2021 Q12 = B; 2021 Q24 = E). Os julgamentos de cada afirmação são coerentes com as letras indicadas. |

---

## Outros conteúdos em formato de exercício e observações gerais
Estes conteúdos **não são questões** no material, mas aparecem como situação + solução e podem virar questões de associação na prova:
- **Slides p. 3 — prontuário médico:** acesso sem autorização → confidencialidade; diagnóstico alterado → integridade; sistema não abre → disponibilidade; site falso se passa pelo portal → autenticidade; médico nega ter assinado receita digital → não repúdio.
- **Slides p. 4 — formação de um risco:** Ameaça (criminoso) → Vulnerabilidade (ausência de MFA) → Ativo (conta e dados acadêmicos) → Impacto (vazamento e alteração de notas). Controles: MFA, alertas, logs e recuperação.
- **Slides p. 8 — proteção de um documento digital (contrato pela internet):** ocultar conteúdo → criptografia; detectar alteração → hash; comprovar autoria → assinatura digital; validar a chave pública → certificado digital.
- **Slides p. 12 — ataque × controle:** Phishing → MFA, filtros e treinamento; MITM → TLS e validação de certificado; ARP spoofing → proteção e segmentação da rede; SQL Injection → consultas parametrizadas; Ransomware → backup isolado e restauração; acesso indevido em API → autorização no servidor. Exemplo: `/api/alunos/105/documentos` trocado por `106` abre o documento de outro aluno (controle de acesso quebrado/IDOR).
- **Apostila p. 9 — disponibilidade:** A = MTBF ÷ (MTBF + MTTR). Exemplo: MTBF 99 h e MTTR 1 h → 99/100 = **99%**. RTO = tempo máximo para restaurar (ex.: 4 h); RPO = perda máxima de dados em tempo (ex.: 15 min).
- **Apostila p. 18 — STRIDE:** Spoofing→Autenticidade; Tampering→Integridade; Repudiation→Responsabilização; Information disclosure→Confidencialidade; Denial of service→Disponibilidade; Elevation of privilege→Autorização.

Observações de formatação do material (não afetam questões): na apostila, as listas numeradas das p. 20 (resposta a incidentes, itens "5." a "11.") e p. 23 (estratégia ENADE, itens "12." a "17.") começam com numeração errada, continuando a contagem de listas anteriores. A p. 20 dos slides é só imagem ("Alguma Pergunta? / Agradecemos a Atenção!") e não contém questão. Todas as 48 páginas (20 + 28) foram lidas, e as páginas com figura ou tabela foram renderizadas e conferidas visualmente.
