# Segurança da Informação — Questões INFERIDAS (prováveis questões do banco do squad que não temos)

> ⚠️ **Atenção:** estas questões NÃO constam nos materiais. Foram elaboradas para cobrir os subtópicos do material do
> Squad 4 que não têm questão conhecida, imitando o estilo das questões do squad. Servem para estudo dirigido.
> As questões reais conhecidas estão em `../questoes_por_topico/08_Seguranca_da_Informacao.md`.

**Base usada:**
- `Material Completo - Segurança da Informação.pdf` (apostila, 28 p.). Estrutura usada como lista de subtópicos: 4 unidades e 16 seções numeradas (Unidade 1, §1–4, p. 5–9; Unidade 2, §5–6.1, p. 10–13; Unidade 3, §7–9.1, p. 14–18; Unidade 4, §10–13, p. 19–21; §14 "Relações com outras matérias", p. 21–23; §15 "Como o ENADE avalia", p. 23–25; §16 "Quadros de revisão rápida", p. 25–26). Também foram consultados o "Mapa de cobertura da matriz" (p. 3), as figuras 1–7 (renderizadas e conferidas) e as tabelas.
- `Aula Enade - Segurança da Informação.pdf` (slides, 20 p.). São 4 temas, cada um com **2 slides de conteúdo + 1 questão**: Tema 1 (p. 3–4 + Q1), Tema 2 (p. 7–8 + Q2), Tema 3 (p. 11–12 + Q3), Tema 4 (p. 15–16 + Q4). Vários slides de conteúdo (p. 4, 8, 11, 12, 16) não têm questão conhecida. Por isso receberam prioridade alta.
- Estilo identificado do squad (Q1–Q4): **5 alternativas (A–E)**. Cenários longos da **área da saúde** (hospital, PEP, telemedicina, holding de saúde) que citam ISO/IEC 27001, LGPD, ICP-Brasil e ANPD. Tipos usados: **afirmativas múltiplas** com 4 afirmativas (Q1, com "ocorrências" numeradas; Q4) e alternativas "Apenas I e II." … "I, II, III e IV."; **resposta única** ("qual é a combinação … mais adequada?", Q2); **asserção-razão** ("A respeito dessas asserções, assinale a opção correta:", Q3). Os distratores exploram confusões clássicas (hash × cifragem, Argon2id × cifra, pseudonimização × anonimização). Para variar, como pede o guia, também foram usados associação, ordenação e afirmativa negativa, sempre com a mesma estrutura de enunciado.

## Mapa de cobertura
| # | Subtópico (material) | Páginas | Questão conhecida | Questão inferida | Prioridade |
|---|---|---|---|---|---|
| 1 | Conceito de SI (pessoas, processos, tecnologia; dado × informação) e princípios: CID, autenticidade, responsabilização, não repúdio | Apostila p. 5–6 (Fig. 1); slides p. 3 | Q1 (também Q8) | — (variação provável: associação "ocorrência × princípio" do slide 3, incluindo **Responsabilização**, que só a apostila lista) | — |
| 2 | Ativo, ameaça, vulnerabilidade, evento, incidente, controle e risco; cadeia causal | Apostila p. 6, p. 25; slides p. 4 | — | I1 | Alta |
| 3 | Matriz de risco 5×5, risco inerente × residual, exemplo de análise de risco | Apostila p. 7 (Fig. 2), p. 26 | — | I2 | Alta |
| 4 | Classificação de controles (finalidade, natureza, momento, responsabilidade) e defesa em profundidade | Apostila p. 8 (Fig. 3) | — | I3 | Média |
| 5 | Dependabilidade e resiliência: MTBF, MTTR, disponibilidade, RTO, RPO; "Armadilha comum" do backup | Apostila p. 8–9, p. 26 | — | I4 | Alta |
| 6 | Fundamentos de criptografia e comparação de mecanismos (AES, assimétrica, hash) | Apostila p. 10–11 (Fig. 4); slides p. 7 | Q2, Q8 (Q1-III/IV) | — (variação provável: Q2 com os pilares trocados, ou com alternativa que inclua a assinatura ICP-Brasil) | — |
| 7 | Criptografia simétrica, AES, IV/nonce | Apostila p. 11 | Q8 (II, III), Q2 | — | — |
| 8 | Assimétrica, certificados, PKI e validação de certificado; HMAC × assinatura (não repúdio) | Apostila p. 10–11; slides p. 7–8 | parcial: só Q8-I (verificação com chave pública) | I5 | Alta |
| 9 | Hash de senhas: salt, pepper, KDF (Argon2id, scrypt, bcrypt, PBKDF2) | Apostila p. 11–12 | — (Argon2id só como distrator da Q2-D) | I6 | Alta |
| 10 | TLS e "Limite do TLS" | Apostila p. 12 | Q3, Q5, Q2-B | — (variação provável: endpoint comprometido, certificado inválido aceito, log em texto claro) | — |
| 11 | Identificação, autenticação, autorização, auditoria e accountability | Apostila p. 12; slides p. 11 | — | I7 | Alta |
| 12 | Fatores de autenticação, MFA genuíno e métodos × resistência a phishing (SMS, TOTP, push, FIDO2, biometria) | Apostila p. 12–13; slides p. 11 | — | I8 | Alta |
| 13 | Modelos de controle de acesso: DAC, MAC, RBAC, ABAC, ReBAC | Apostila p. 13; slides p. 11 | — (RBAC só aparece no cenário da Q1) | I9 | Alta |
| 14 | Mínimo privilégio, privilégio efetivo, Zero Trust e segmentação ("negar por padrão", DMZ, VLAN, microsegmentação) | Apostila p. 13, p. 15, p. 26; slides p. 11 | — | I10 (agrupa §6.1 final e §7.1, que são curtos) | Média |
| 15 | ARP spoofing e MITM | Apostila p. 14 (Fig. 5), p. 23–24; slides p. 12 | Q3, Q5 | — | — |
| 16 | Outros ataques e defesas: phishing, DNS spoofing, evil twin, DoS/DDoS, varredura, sequestro de sessão | Apostila p. 14; slides p. 12 | — (phishing e fator humano só na Q6) | I11 | Alta |
| 17 | Limites do firewall | Apostila p. 14–15 | Q5-II | — | — |
| 18 | Hardening, práticas de endpoint e segredos, nuvem (responsabilidade compartilhada) | Apostila p. 15–16 | — | I13 | Média |
| 19 | Tipos de código malicioso (vírus, worm, trojan, ransomware, spyware, rootkit, bot) | Apostila p. 16 | — | I12 | Alta |
| 20 | Injeção SQL e consultas parametrizadas | Apostila p. 17, p. 26; slides p. 12 | — | I14 | Alta |
| 21 | APIs, controle de acesso quebrado (IDOR), JWT, banco de dados, segredos, SSDF e OWASP | Apostila p. 16–17 (Fig. 7); slides p. 12 (exemplo `/api/alunos/105`) | — | I15 | Alta |
| 22 | Modelagem de ameaças: STRIDE | Apostila p. 17–18 | — | I16 | Média |
| 23 | Governança e SGSI: ISO/IEC 27001, NIST CSF 2.0, documentos, papéis e indicadores | Apostila p. 19, p. 15 (Fig. 6) | parcial: Q6 (segurança é processo) | I17 | Média |
| 24 | Tratamento de riscos: evitar, mitigar, transferir/compartilhar, aceitar | Apostila p. 19, p. 7 | — | I18 | Média |
| 25 | Gestão de incidentes (NIST SP 800-61 Rev. 3) e cadeia de custódia | Apostila p. 19–20 | — | I19 | Média |
| 26 | Continuidade de negócios e recuperação: BIA, sites frio/morno/quente, alta disponibilidade × backup, ransomware | Apostila p. 20, p. 9, p. 25–26; slides p. 12 | — | I20 | Alta |
| 27 | LGPD: dado pessoal e sensível, anonimização, pseudonimização, tratamento | Apostila p. 21, p. 25; slides p. 15 | Q4, Q7 | — | — |
| 28 | LGPD: direitos do titular e papel da ANPD | Apostila p. 21, p. 24 | Q7 | — | — |
| 29 | LGPD: agentes (controlador, operador, encarregado), princípios, bases legais e consentimento, privacy by design, privacidade × segurança, biometria | Apostila p. 20–21; slides p. 15–16 | parcial: Q9 (discursiva) | I21 | Alta |
| 30 | Ética profissional, fator humano, segurança como processo | Apostila p. 21, p. 24 | Q6 | — | — |
| 31 | Relações com outras matérias: sistemas distribuídos, IA, segurança física e ambiental | Apostila p. 21–23 | — | I22 | Baixa |
| 32 | Como o ENADE avalia; questões oficiais 2017/2021 | Apostila p. 23–25 | Q5–Q8 | — | — |
| 33 | Quadros de revisão rápida (confusões frequentes, controle pelo objetivo, fórmulas, checklist) | Apostila p. 25–26 | transversal | — (o conteúdo foi usado nos distratores de I1, I4, I6, I14, I20 etc.) | — |

**Resumo:** 33 subtópicos. 10 já cobertos por questões conhecidas (linhas 1, 6, 7, 10, 15, 17, 27, 28, 30, 32), 1 transversal sem questão própria (linha 33) e 22 sem cobertura ou com cobertura só parcial. Foram inferidas **22 questões (I1–I22)**, uma por subtópico descoberto. Gabaritos: A = 5 (I4, I7, I10, I16, I22) · B = 4 (I2, I5, I11, I17) · C = 4 (I3, I6, I14, I21) · D = 4 (I1, I9, I13, I19) · E = 5 (I8, I12, I15, I18, I20).

## Índice
1. [I1 — Ativo ameaça vulnerabilidade evento e incidente](#i1--ativo-ameaça-vulnerabilidade-evento-e-incidente)
2. [I2 — Matriz de risco e risco inerente e residual](#i2--matriz-de-risco-e-risco-inerente-e-residual)
3. [I3 — Classificação de controles e defesa em profundidade](#i3--classificação-de-controles-e-defesa-em-profundidade)
4. [I4 — Dependabilidade MTBF MTTR RTO e RPO](#i4--dependabilidade-mtbf-mttr-rto-e-rpo)
5. [I5 — Assinatura digital certificados e HMAC](#i5--assinatura-digital-certificados-e-hmac)
6. [I6 — Armazenamento de senhas com salt e KDF](#i6--armazenamento-de-senhas-com-salt-e-kdf)
7. [I7 — Identificação autenticação autorização e auditoria](#i7--identificação-autenticação-autorização-e-auditoria)
8. [I8 — MFA e resistência a phishing](#i8--mfa-e-resistência-a-phishing)
9. [I9 — Modelos de controle de acesso](#i9--modelos-de-controle-de-acesso)
10. [I10 — Zero Trust segmentação e mínimo privilégio](#i10--zero-trust-segmentação-e-mínimo-privilégio)
11. [I11 — Ataques de rede e controles correspondentes](#i11--ataques-de-rede-e-controles-correspondentes)
12. [I12 — Tipos de código malicioso](#i12--tipos-de-código-malicioso)
13. [I13 — Responsabilidade compartilhada na nuvem](#i13--responsabilidade-compartilhada-na-nuvem)
14. [I14 — Injeção SQL e consultas parametrizadas](#i14--injeção-sql-e-consultas-parametrizadas)
15. [I15 — Segurança de APIs e controle de acesso quebrado](#i15--segurança-de-apis-e-controle-de-acesso-quebrado)
16. [I16 — Modelagem de ameaças STRIDE](#i16--modelagem-de-ameaças-stride)
17. [I17 — Governança ISO 27001 e NIST CSF 2.0](#i17--governança-iso-27001-e-nist-csf-20)
18. [I18 — Tratamento de riscos](#i18--tratamento-de-riscos)
19. [I19 — Etapas da resposta a incidentes](#i19--etapas-da-resposta-a-incidentes)
20. [I20 — Continuidade de negócios e ransomware](#i20--continuidade-de-negócios-e-ransomware)
21. [I21 — LGPD agentes de tratamento princípios e bases legais](#i21--lgpd-agentes-de-tratamento-princípios-e-bases-legais)
22. [I22 — Segurança em sistemas distribuídos IA e segurança física](#i22--segurança-em-sistemas-distribuídos-ia-e-segurança-física)

---

## I1 — Ativo ameaça vulnerabilidade evento e incidente
**Subtópico coberto:** Ativos, ameaças, vulnerabilidades, evento, incidente, controle e risco (apostila §2, p. 6; slides p. 4 "Formação de um risco"; "Confusões frequentes", p. 25)
**Por que é provável:** o slide 4 é um dos dois slides de conteúdo do Tema 1, e um dos objetivos da aula (slide 2) é "Diferenciar ameaça, vulnerabilidade, risco e incidente". A Q1, única questão do Tema 1, cobra só os princípios.
**Prioridade:** Alta
**Tipo ENADE:** Afirmativas múltiplas (com elementos numerados no cenário, como as "ocorrências" da Q1)

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
Uma rede de clínicas que oferece teleconsultas mantém um portal no qual os pacientes acessam laudos, receitas e resultados de exames. Após uma auditoria interna baseada na ISO/IEC 27001, a equipe de segurança da informação descreveu o cenário de risco do portal por meio dos seguintes elementos:

**DADOS DE SUPORTE**
1. Banco de dados de laudos e prontuários, que armazena dados pessoais sensíveis dos pacientes.
2. Grupo criminoso que vem enviando às recepcionistas e-mails de phishing que imitam o setor de TI.
3. Contas administrativas do portal protegidas apenas por senha, sem MFA e sem alertas de login anômalo.
4. Registro, pelo SIEM, de 600 tentativas de login malsucedidas em 10 minutos em uma mesma conta, ainda sem evidência de acesso bem-sucedido.
5. Invasão de uma conta de recepcionista, que foi usada para exportar 3 mil laudos.
6. Implantação, após o ocorrido, de MFA resistente a phishing e de alertas de login anômalo.

Considerando os conceitos fundamentais de gestão de riscos em Segurança da Informação, avalie as afirmativas a seguir:

**I.** O elemento 1 é um ativo, o elemento 2 é uma ameaça e o elemento 3 é uma vulnerabilidade que pode ser explorada por essa ameaça.

**II.** O elemento 4 configura, por si só, um incidente de segurança, uma vez que toda ocorrência observável no ambiente corresponde a um dano já consumado.

**III.** O elemento 5 caracteriza um incidente, e o risco associado a esse cenário deve ser estimado com base na probabilidade e no impacto sobre os objetivos da organização.

**IV.** No elemento 6, o MFA atua como controle preventivo, pois reduz a probabilidade de a ameaça explorar a vulnerabilidade, e os alertas de login anômalo atuam como controle detectivo, pois reduzem o tempo até a descoberta.

**COMANDO**
É correto o que se afirma em:

**Alternativas:**
- **A)** Apenas I e II.
- **B)** Apenas I e III.
- **C)** Apenas II e IV.
- **D)** Apenas I, III e IV.
- **E)** I, II, III e IV.

**Gabarito: D**

**Julgamento das afirmativas:**
- **I — Verdadeira.** Ativo é "algo que tem valor e precisa ser protegido" (dados pessoais). Ameaça é "fonte ou evento capaz de causar dano" (criminoso). Vulnerabilidade é "fraqueza que pode ser explorada" (ausência de MFA). O slide 4 usa a mesma cadeia: Criminoso → Ausência de MFA → Conta e dados → Vazamento.
- **II — Falsa.** Evento é "ocorrência observável, ainda sem concluir que houve dano", e o exemplo da apostila é justamente "muitas tentativas de login". O evento só vira incidente se, após análise, comprometer ou ameaçar políticas e operações.
- **III — Verdadeira.** O exemplo de incidente da apostila é "conta invadida e usada para extrair dados". Risco é o "efeito da incerteza sobre objetivos, considerando probabilidade e impacto".
- **IV — Verdadeira.** A apostila diz: "Um controle preventivo reduz a probabilidade; um controle detectivo reduz o tempo até a descoberta".

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Inclui II, que confunde evento com incidente, e omite III e IV.
- **B) ❌** — Omite IV, que também é verdadeira. Atrai quem não lembra a diferença entre controle preventivo e controle detectivo.
- **C) ❌** — Inclui II (falsa) e omite I e III, que são as definições centrais do slide 4.
- **D) ✅** — I, III e IV são verdadeiras. II é falsa.
- **E) ❌** — Considera verdadeira a II, que trata evento e dano como sinônimos.

**Base no material:** apostila p. 6, tabela "Conceito / Definição operacional / Exemplo" e o parágrafo da cadeia causal ("uma ameaça explora uma vulnerabilidade, produz um evento adverso e causa impacto sobre um ativo"). Slides p. 4. Apostila p. 25: "Ameaça e vulnerabilidade", "Risco e incidente", "Vulnerabilidade e exploit".
**Conceito-chave para a prova:** A ameaça explora uma vulnerabilidade e causa impacto sobre um ativo. Evento é só a ocorrência observada, e incidente é a ocorrência que compromete ou ameaça a organização. Risco é uma possibilidade (probabilidade × impacto). Incidente é um fato que já ocorreu. Controle preventivo reduz a probabilidade, detectivo reduz o tempo até a descoberta, e corretivo ou de recuperação limita o impacto.

---

## I2 — Matriz de risco e risco inerente e residual
**Subtópico coberto:** Matriz qualitativa 5×5, priorização, risco inerente × residual e decisão da direção (apostila p. 7, Figura 2 e quadro "Risco inerente e residual"; p. 26, "Risco qualitativo")
**Por que é provável:** a apostila traz a matriz como figura, um quadro em destaque sobre risco inerente e residual e um "Exemplo de análise de risco", e repete a fórmula na revisão final. É o tipo de conteúdo que vira questão de cálculo.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única (interpretação de dados e cálculo)

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
O comitê de riscos de um hospital usa uma matriz qualitativa 5 × 5 para priorizar os riscos do Prontuário Eletrônico do Paciente (PEP). Probabilidade e impacto recebem notas de 1 (Muito baixa) a 5 (Muito alta), e o escore é o produto das notas. As faixas são: **1 a 4 = Baixo (B)**; **5 a 9 = Médio (M)**; **10 a 16 = Alto (A)**; **20 a 25 = Crítico (C)**.

**DADOS DE SUPORTE**

| Risco | Probabilidade inerente | Impacto inerente | Controles aplicados | Probabilidade residual | Impacto residual |
|---|---|---|---|---|---|
| R1 — Ransomware cifra os servidores do PEP | Alta (4) | Muito alta (5) | Backup isolado e testado, EDR e segmentação | Média (3) | Alta (4) |
| R2 — Roubo de credenciais administrativas por phishing | Muito alta (5) | Média (3) | MFA resistente a phishing e treinamento | Baixa (2) | Média (3) |
| R3 — Queda de energia que desliga os monitores da UTI | Muito baixa (1) | Muito alta (5) | Nenhum controle adicional avaliado | — | — |

**COMANDO**
Com base nesses dados e nos conceitos de análise de riscos, assinale a alternativa correta.

**Alternativas:**
- **A)** O risco inerente de R2 tem escore 15 e é classificado como Crítico, por ser o maior escore inerente entre os três riscos analisados.
- **B)** R1 tem escore inerente 20 (Crítico) e escore residual 12 (Alto). Esse risco residual deve ser reavaliado após a medição da efetividade dos controles e submetido à direção, que decide se o aceita, reduz, evita ou transfere dentro de limites definidos.
- **C)** Após os controles, R2 passa a ter escore 6 (Médio) e, por se tratar de risco residual, pode ser considerado eliminado, o que dispensa novas avaliações.
- **D)** R3 tem escore 5 (Médio) e pode ser aceito automaticamente, pois a multiplicação probabilidade × impacto define, de forma universal, a aceitabilidade de qualquer risco, mesmo que ele envolva vidas.
- **E)** O risco inerente de R1 corresponde ao escore 12, pois é a estimativa feita depois de considerados o backup isolado, o EDR e a segmentação.

**Gabarito: B**

**Cálculos:** R1 inerente = 4 × 5 = 20 (C); R1 residual = 3 × 4 = 12 (A); R2 inerente = 5 × 3 = 15 (A); R2 residual = 2 × 3 = 6 (M); R3 = 1 × 5 = 5 (M). As faixas foram conferidas na Figura 2: 5 = M, 10 = A, 16 = A, 20 = C.

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — 15 está na faixa de 10 a 16, ou seja, Alto. Além disso, o maior escore inerente é o de R1 (20), não o de R2.
- **B) ✅** — Os escores estão certos. O risco residual "permanece depois dos controles", deve ser "reavaliado após medir efetividade dos controles", e "a direção deve decidir se aceita, reduz, evita ou transfere esse risco dentro de limites definidos" (p. 7).
- **C) ❌** — Risco residual é o que **sobra** depois dos controles. Não é risco zero e não dispensa reavaliação.
- **D) ❌** — Para a apostila, a multiplicação "é uma técnica de priorização, não uma verdade matemática universal", e "um risco raro pode continuar inaceitável se o impacto envolver vidas" (p. 7). É o caso dos monitores da UTI.
- **E) ❌** — Inverte os conceitos. Risco inerente é estimado **antes** dos controles (20). O valor 12 é o residual.

**Base no material:** apostila p. 7, Figura 2 ("Matriz qualitativa de risco 5 × 5", com B/M/A/C), o parágrafo sobre priorização e o quadro "Risco inerente e residual". Apostila p. 26, "Risco qualitativo": "Multiplicar escalas de 1 a 5 é ferramenta de priorização e exige critérios explícitos".
**Conceito-chave para a prova:** Risco inerente é calculado antes dos controles, e risco residual depois deles. O residual nunca é "eliminado": a direção decide se o aceita, reduz, evita ou transfere. A matriz serve para priorizar, e um impacto sobre vidas pode tornar inaceitável até um risco raro.

---

## I3 — Classificação de controles e defesa em profundidade
**Subtópico coberto:** Classificação de controles por finalidade, natureza, momento e responsabilidade; defesa em profundidade (apostila §3, p. 8, Figura 3; cadeia causal, p. 6)
**Por que é provável:** a seção tem uma tabela de 4 dimensões com exemplos, uma figura e uma pegadinha explícita: defesa em profundidade "não significa acumular ferramentas", e "controles duplicados que falham pelo mesmo motivo oferecem pouca independência".
**Prioridade:** Média
**Tipo ENADE:** Afirmativas múltiplas

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
Após um incidente de acesso indevido, a diretoria de um hospital aprovou um pacote de controles de segurança para o Prontuário Eletrônico do Paciente (PEP), alinhado à ISO/IEC 27001.

**DADOS DE SUPORTE**
Controles aprovados:
- política institucional que exige MFA para todo acesso administrativo ao PEP;
- fechadura com registro de entrada na sala de servidores;
- SIEM com alertas de login anômalo;
- restauração do PEP a partir de backup isolado;
- revisão manual semanal dos acessos de um equipamento de ressonância magnética legado, que não suporta MFA;
- proposta de instalar em sequência, como "segunda camada", dois firewalls idênticos (mesmo fabricante, mesma versão e mesma configuração).

Considerando a classificação de controles e o conceito de defesa em profundidade, avalie as afirmativas a seguir:

**I.** A política que exige MFA para todo acesso administrativo é um controle de natureza administrativa, enquanto a fechadura com registro de entrada na sala de servidores é um controle de natureza física.

**II.** O SIEM com alertas de login anômalo é um controle detectivo, e a restauração do PEP a partir de backup isolado é um controle de recuperação, que limita o impacto e restaura a operação.

**III.** A revisão manual semanal dos acessos do equipamento legado, que não suporta MFA, funciona como controle compensatório.

**IV.** A instalação dos dois firewalls idênticos em sequência atende plenamente à defesa em profundidade, pois controles duplicados que falham pelo mesmo motivo garantem independência entre as camadas.

**COMANDO**
É correto o que se afirma em:

**Alternativas:**
- **A)** Apenas I e IV.
- **B)** Apenas II e III.
- **C)** Apenas I, II e III.
- **D)** Apenas II, III e IV.
- **E)** I, II, III e IV.

**Gabarito: C**

**Julgamento das afirmativas:**
- **I — Verdadeira.** Na dimensão "Natureza", a tabela da p. 8 traz: "Administrativo, técnico, físico". Os exemplos são "Política; firewall; controle de acesso à sala". Quanto à finalidade, os dois controles são preventivos.
- **II — Verdadeira.** Na dimensão "Finalidade", os exemplos são "MFA; SIEM; patch; restauração; aviso; revisão manual", que correspondem a preventivo, detectivo, corretivo, recuperativo, dissuasório e compensatório. A cadeia causal da p. 6 diz que o controle de recuperação "limita o impacto e restaura a operação".
- **III — Verdadeira.** Controle compensatório é o que substitui um controle que não pode ser aplicado. Na tabela, o exemplo correspondente é "revisão manual".
- **IV — Falsa.** É o inverso do texto: "Controles duplicados que falham pelo mesmo motivo oferecem pouca independência". As camadas "precisam cobrir caminhos de ataque diferentes" e "evitar dependência de um único ponto de falha" (p. 8).

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Inclui IV, a pegadinha de "acumular ferramentas", e omite II e III.
- **B) ❌** — Omite I, que é a classificação básica por natureza.
- **C) ✅** — I, II e III são verdadeiras. IV é falsa.
- **D) ❌** — Inclui IV (falsa) e omite I.
- **E) ❌** — Considera verdadeira a IV.

**Base no material:** apostila p. 8, tabela "Classificação de controles" e Figura 3 ("Um único controle pode falhar. Camadas independentes reduzem a chance de uma falha isolada comprometer todo o sistema"), além do parágrafo seguinte. Apostila p. 6, cadeia causal.
**Conceito-chave para a prova:** Quanto à natureza, os controles são administrativos (política), técnicos (firewall, MFA) ou físicos (fechadura). Quanto à finalidade, são preventivos, detectivos, corretivos, recuperativos, dissuasórios ou compensatórios. Defesa em profundidade exige camadas **independentes**, e não cópias do mesmo controle.

---

## I4 — Dependabilidade MTBF MTTR RTO e RPO
**Subtópico coberto:** Dependabilidade e resiliência: MTBF, MTTR, disponibilidade, RTO e RPO; "Armadilha comum" do backup (apostila §4, p. 8–9; "Fórmulas e relações úteis", p. 26)
**Por que é provável:** a tabela traz um exemplo numérico (MTBF 99 h e MTTR 1 h → 99%). A fórmula reaparece na revisão (p. 26), e o checklist final pede "Defino RPO, RTO e teste de restauração". A "Armadilha comum" (backup não prova recuperabilidade; redundância não substitui backup) dá bons distratores.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única (cálculo e interpretação)

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
A equipe de infraestrutura de um hospital avaliou, ao longo de seis meses, a dependabilidade do Prontuário Eletrônico do Paciente (PEP), usado 24 horas por dia nas unidades de terapia intensiva. A diretoria definiu requisitos de recuperação e pediu um parecer sobre a situação atual.

**DADOS DE SUPORTE**
- MTBF (tempo médio entre falhas) medido: **495 horas**.
- MTTR (tempo médio para restaurar) medido: **5 horas**.
- Requisitos definidos: **RTO = 4 horas** e **RPO = 15 minutos**.
- Política atual: backup incremental **a cada 1 hora**, guardado em servidor da mesma rede; replicação síncrona para um segundo servidor no mesmo datacenter; nenhum teste de restauração realizado até hoje.
- Modelo simplificado: **Disponibilidade = MTBF ÷ (MTBF + MTTR)**.

**COMANDO**
Com base nesses dados, assinale a alternativa correta.

**Alternativas:**
- **A)** A disponibilidade estimada é de 99%. Como o tempo médio de restauração (5 h) já supera o RTO (4 h) e o intervalo de backup (1 h) permite perder até 60 minutos de transações, acima do RPO (15 min), nenhum dos dois requisitos está sendo atendido.
- **B)** A disponibilidade estimada é de 99%, e a replicação síncrona para o segundo servidor dispensa o backup, pois a redundância permite recuperar o estado anterior dos dados em caso de exclusão lógica ou de ransomware.
- **C)** A disponibilidade estimada é de 99%. Para elevá-la, a equipe deve reduzir o MTBF e aumentar o MTTR.
- **D)** O RTO é a perda máxima de dados expressa em tempo, e o RPO é o tempo máximo para restaurar o serviço. Assim, o backup a cada 1 hora atende ao RTO de 4 horas.
- **E)** A disponibilidade estimada é de 99,9%, e a existência de backups frequentes comprova a recuperabilidade do PEP, mesmo sem testes de restauração.

**Gabarito: A**

**Cálculo:** A = 495 ÷ (495 + 5) = 495 ÷ 500 = **0,99 = 99%** (conferido com python3). Backup a cada 60 min → perda potencial de até 60 min > RPO de 15 min. MTTR de 5 h > RTO de 4 h.

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — O cálculo está certo, e o RTO e o RPO estão interpretados corretamente: RTO é o "tempo máximo desejado para restaurar serviço", e RPO é a "perda máxima de dados expressa em tempo" (p. 9).
- **B) ❌** — É a "Armadilha comum": "Redundância melhora disponibilidade, mas não substitui backup quando dados íntegros precisam ser recuperados" (p. 9). A replicação síncrona copia também a exclusão ou a cifragem.
- **C) ❌** — Inverte a lógica. MTBF maior significa falhas menos frequentes, e MTTR menor significa recuperação mais rápida. Para elevar a disponibilidade, é preciso **aumentar** o MTBF e **reduzir** o MTTR.
- **D) ❌** — Troca as definições de RTO e RPO.
- **E) ❌** — Erra o cálculo (o resultado é 99%, não 99,9%) e contraria a apostila: "Backup não prova recuperabilidade. É preciso [...] testar restaurações" (p. 9).

**Base no material:** apostila p. 9, tabela MTBF/MTTR/Disponibilidade/RTO/RPO (exemplo: "MTBF 99 h e MTTR 1 h resultam em 99%") e o quadro "Armadilha comum". Apostila p. 26, "Disponibilidade simplificada A = MTBF ÷ (MTBF + MTTR)". Apostila p. 25, "Backup e redundância".
**Conceito-chave para a prova:** A = MTBF/(MTBF+MTTR). Para melhorar, aumente o MTBF e reduza o MTTR. RTO mede o tempo para voltar a operar, e RPO mede quanto dado se pode perder. Backup sem teste de restauração não prova nada, e redundância não substitui backup.

---

## I5 — Assinatura digital certificados e HMAC
**Subtópico coberto:** Criptografia assimétrica, certificados e PKI (validação do certificado); HMAC × assinatura digital (apostila §5.2, p. 11; tabela da Figura 4, p. 10–11; slides p. 7 "Criptografia e integridade" e p. 8 "Proteção de um documento digital")
**Por que é provável:** os dois slides de conteúdo do Tema 2 tratam de mecanismo × finalidade (incluindo HMAC e certificado digital) e de assinatura/certificado em um documento. A Q2 cobra só AES/TLS, e a Q8 só a verificação com chave pública. A apostila tem o quadro "Não confunda" sobre o papel das chaves.
**Prioridade:** Alta
**Tipo ENADE:** Afirmativas múltiplas

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
Uma plataforma de telemedicina emite receitas digitais assinadas pelos médicos com certificados da ICP-Brasil. As farmácias validam essas receitas antes de dispensar os medicamentos. A plataforma também envia laudos a um laboratório parceiro e quer que apenas esse laboratório consiga lê-los. A integração automática entre os sistemas do hospital e do laboratório usa HMAC-SHA-256 com uma chave secreta compartilhada pelas duas instituições.

Considerando as propriedades da criptografia assimétrica, dos certificados digitais e do HMAC, avalie as afirmativas a seguir:

**I.** Na receita digital, o médico assina com a sua chave privada, e a farmácia verifica a assinatura com a chave pública do médico, vinculada à identidade dele pelo certificado digital emitido por uma autoridade certificadora.

**II.** Para que apenas o laboratório consiga ler o laudo, a proteção de confidencialidade deve usar a chave pública do laboratório (destinatário). Assinar o laudo com a chave privada do hospital, isoladamente, não oculta o seu conteúdo.

**III.** O HMAC oferece integridade e autenticidade entre o hospital e o laboratório, mas não oferece não repúdio perante terceiros, pois as duas partes conhecem a chave secreta, e qualquer uma delas poderia ter gerado a etiqueta.

**IV.** Ao receber o certificado do médico, basta à farmácia conferir se o nome do titular corresponde ao do médico. É dispensável verificar o período de validade, a finalidade, a assinatura da autoridade certificadora e o estado de confiança (revogação) do certificado, já que a chave pública, por definição, pode ser divulgada.

**COMANDO**
É correto o que se afirma em:

**Alternativas:**
- **A)** Apenas I e II.
- **B)** Apenas I, II e III.
- **C)** Apenas I, III e IV.
- **D)** Apenas II, III e IV.
- **E)** I, II, III e IV.

**Gabarito: B**

**Julgamento das afirmativas:**
- **I — Verdadeira.** "Para assinatura, a chave privada produz a assinatura e a pública verifica. [...] Certificados digitais vinculam uma identidade a uma chave pública por meio de uma autoridade certificadora e de uma cadeia de confiança" (p. 11).
- **II — Verdadeira.** "Cifrar com a chave pública do destinatário visa confidencialidade. Assinar com a chave privada do remetente visa autenticidade e integridade" (p. 11). Na tabela, a assinatura digital "não garante sozinha" a confidencialidade do conteúdo (p. 10–11). Na prática, usa-se um esquema híbrido: uma chave simétrica cifra o laudo e é protegida com a chave pública do laboratório.
- **III — Verdadeira.** Na tabela da p. 10, o HMAC oferece "integridade e autenticidade entre quem compartilha segredo" e não garante "não repúdio perante terceiros". O slide 7 lista HMAC = "Integridade e autenticidade" e reserva o não repúdio à assinatura digital.
- **IV — Falsa.** O passo 2 da p. 11 manda validar "nome, período, finalidade, assinatura da autoridade e estado de confiança". Divulgar a chave pública não dispensa a validação: a "confiança na chave pública" é justamente o que a criptografia assimétrica não garante sozinha (tabela, p. 10).

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Omite III. Atrai quem acha que HMAC e assinatura oferecem as mesmas garantias.
- **B) ✅** — I, II e III são verdadeiras. IV é falsa.
- **C) ❌** — Inclui IV (falsa) e omite II.
- **D) ❌** — Inclui IV (falsa) e omite I, que é a base da assinatura digital.
- **E) ❌** — Considera verdadeira a IV, ignorando a validação do certificado e a revogação.

**Base no material:** apostila p. 10–11, tabela da Figura 4 (linhas "Criptografia assimétrica", "HMAC" e "Assinatura digital"); §5.2, passos 1–4 e quadro "Não confunda" ("'Criptografar com a chave privada' não é uma explicação geral adequada para assinatura digital"). Slides p. 7 e p. 8 (necessidade × solução: ocultar → criptografia; detectar alteração → hash; comprovar autoria → assinatura digital; validar a chave pública → certificado digital).
**Conceito-chave para a prova:** A assinatura é feita com a chave privada do remetente e verificada com a pública dele. O sigilo usa a chave pública do destinatário. O HMAC dá integridade e autenticidade entre as partes, mas **não** dá não repúdio. O certificado vincula identidade e chave pública e precisa ser validado: nome, período, finalidade, assinatura da AC e revogação.

---

## I6 — Armazenamento de senhas com salt e KDF
**Subtópico coberto:** Hash, senhas e derivação de chaves: salt, pepper, KDF de senha e hash comum (apostila §5.3, p. 11–12; legenda da Figura 4, p. 10: "senhas exigem KDF + salt, não hash simples")
**Por que é provável:** a seção tem uma tabela de termos e uma frase de efeito ("armazenar senhas com SHA-256 puro é inadequado"). O squad já usou Argon2id como distrator na Q2-D, sinal de que o tema está no banco.
**Prioridade:** Alta
**Tipo ENADE:** Asserção-razão

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
Uma startup de telemedicina descobriu que a tabela de usuários do seu aplicativo foi copiada por um atacante. As senhas dos pacientes estavam armazenadas como SHA-256(senha), sem salt. Para reduzir o impacto de futuros vazamentos, a equipe de engenharia propôs:
- usar uma função de derivação de senha lenta e parametrizável (Argon2id), com parâmetros de custo revisados periodicamente;
- gerar um salt único por credencial, armazenado junto ao verificador no banco de dados;
- adotar um pepper, mantido em um cofre de segredos separado do banco.

Considerando esse cenário, avalie as asserções a seguir e a relação proposta entre elas:

**I.** A substituição do SHA-256 puro pelo Argon2id com salt único por credencial dificulta ataques de força bruta e de tabelas pré-computadas sobre as credenciais vazadas, pois eleva o custo de cada tentativa e impede que senhas iguais gerem o mesmo resultado.

**PORQUE**

**II.** O salt deve ser mantido em segredo, em cofre separado do banco de dados, já que, se o atacante obtiver o salt junto com o verificador, a proteção contra pré-computação é anulada.

**COMANDO**
A respeito dessas asserções, assinale a opção correta:

**Alternativas:**
- **A)** As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
- **B)** As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
- **C)** A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
- **D)** A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
- **E)** As asserções I e II são proposições falsas.

**Gabarito: C**

**Julgamento:**
- **Asserção I — Verdadeira.** O SHA-256 é rápido, e por isso "atacantes podem testar bilhões de candidatos". Uma KDF de senha "eleva custo de cada tentativa" (Argon2id, scrypt, bcrypt, PBKDF2). O salt único "impede que senhas iguais tenham o mesmo resultado e reduz o valor de tabelas pré-computadas" (p. 11–12).
- **Asserção II — Falsa.** "O salt não precisa ser secreto" e é um "valor único armazenado junto ao verificador" (p. 11–12). Ele funciona mesmo conhecido, porque obriga o atacante a atacar cada senha separadamente. O segredo guardado à parte do banco é o **pepper** ("segredo adicional mantido separado do banco, quando adotado").
- **Relação:** como II é falsa, não há justificativa a avaliar.

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — II é falsa. A alternativa atrai quem confunde salt com pepper.
- **B) ❌** — Também exige II verdadeira.
- **C) ✅** — I é verdadeira e II é falsa.
- **D) ❌** — I é verdadeira. A combinação KDF + salt é exatamente a recomendação da apostila.
- **E) ❌** — I é verdadeira.

**Base no material:** apostila p. 11–12, §5.3 e tabela "Salt / Pepper / KDF de senha / Hash comum". Hash comum é "adequado para integridade, não para proteger senhas sozinho". Slides p. 10 (gabarito da Q2-D): Argon2id serve para "armazenamento seguro de senhas (protegendo contra ataques de força bruta e tabelas rainbow)".
**Conceito-chave para a prova:** Senhas devem passar por uma KDF lenta (Argon2id, scrypt, bcrypt, PBKDF2) com salt único. O salt **não é secreto** e fica junto do hash. O pepper é secreto e fica fora do banco. SHA-256 puro serve para integridade, não para senha.

---

## I7 — Identificação autenticação autorização e auditoria
**Subtópico coberto:** Identificação, autenticação, autorização, auditoria e accountability (apostila §6, p. 12; slides p. 11 "Da identidade à permissão"; "Confusões frequentes", p. 25)
**Por que é provável:** o slide 11 é um dos dois slides de conteúdo do Tema 3, e o objetivo da aula é "Explicar autenticação, autorização e MFA". A Q3, única questão do Tema 3, trata só de ARP/TLS. A apostila lista "autenticação versus autorização" entre as "confusões clássicas" que o ENADE explora (p. 23).
**Prioridade:** Alta
**Tipo ENADE:** Associação

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
Um hospital revisou o fluxo de acesso ao Prontuário Eletrônico do Paciente (PEP) para atender à LGPD e às recomendações de uma auditoria baseada na ISO/IEC 27001. A equipe descreveu cinco etapas do controle de identidade e acesso, ilustradas com situações do dia a dia de uma enfermeira.

**DADOS DE SUPORTE**

Coluna I — Etapas
1. Identificação
2. Autenticação
3. Autorização
4. Auditoria
5. Accountability (responsabilização)

Coluna II — Situações
( ) Cada alteração de prescrição no PEP gera um log assinado com data, hora, usuário e conteúdo alterado.
( ) O hospital proíbe contas compartilhadas, sincroniza os relógios dos servidores e protege os logs, de modo que cada ação possa ser atribuída de forma confiável a uma pessoa.
( ) A enfermeira digita seu e-mail institucional na tela de login do PEP.
( ) O PEP permite que a enfermeira visualize apenas os prontuários dos pacientes internados na ala em que está escalada.
( ) O sistema exige a senha da enfermeira e a confirmação em uma chave de segurança física.

**COMANDO**
Assinale a alternativa que apresenta a associação correta, na ordem de cima para baixo da Coluna II.

**Alternativas:**
- **A)** 4 – 5 – 1 – 3 – 2.
- **B)** 4 – 5 – 2 – 3 – 1.
- **C)** 5 – 4 – 1 – 3 – 2.
- **D)** 4 – 5 – 1 – 2 – 3.
- **E)** 3 – 5 – 1 – 4 – 2.

**Gabarito: A**

**Associação comentada:** log assinado → **Auditoria** ("O que fez e quando?", exemplo "Log assinado de alteração de nota"). Contas individuais, relógio e logs protegidos → **Accountability** ("A ação pode ser atribuída de modo confiável?"). E-mail → **Identificação** ("Quem afirma ser?"). Visualizar só a própria ala → **Autorização** ("O que pode fazer?", exemplo "Professor altera notas apenas de suas turmas"). Senha + chave de segurança → **Autenticação** ("Como prova a identidade?").

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — Todas as associações correspondem à tabela da p. 12.
- **B) ❌** — Troca identificação e autenticação. "Identificar é declarar identidade; autenticar é prová-la" (p. 25).
- **C) ❌** — Troca auditoria e accountability. A auditoria registra o que foi feito. A accountability é a capacidade de atribuir a ação a alguém de modo confiável.
- **D) ❌** — Troca autenticação e autorização. "Autenticar confirma quem; autorizar decide o que pode" (p. 25).
- **E) ❌** — Associa o log à autorização e a restrição por ala à auditoria.

**Base no material:** apostila p. 12, tabela "Etapa / Pergunta / Exemplo" (com a linha Accountability). Slides p. 11 (Identificação: e-mail; Autenticação: senha e token; Autorização: alterar somente suas turmas; Auditoria: registro no log). Apostila p. 25, "Identificação e autenticação" e "Autenticação e autorização".
**Conceito-chave para a prova:** Identificar é dizer quem é. Autenticar é provar. Autorizar é decidir o que a pessoa pode fazer. Auditar é registrar o que ela fez. Accountability é conseguir atribuir a ação a uma pessoa, o que exige conta individual, relógio sincronizado e log protegido.

---

## I8 — MFA e resistência a phishing
**Subtópico coberto:** Fatores de autenticação, MFA genuíno e métodos × resistência a phishing (apostila §6, p. 12–13; slides p. 11 "MFA"; "Escolha do controle pelo objetivo", p. 25)
**Por que é provável:** a apostila tem uma tabela de métodos com nível de resistência a phishing e a frase de destaque "Senha e PIN são ambos conhecimento". O slide 11 destaca o MFA, e o slide 12 associa phishing a "MFA, filtros e treinamento". Nenhuma questão conhecida cobra MFA.
**Prioridade:** Alta
**Tipo ENADE:** Afirmativas múltiplas

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
Uma campanha de phishing capturou as senhas de vários médicos de um hospital. Hoje, o login no Prontuário Eletrônico do Paciente (PEP) exige senha e um PIN de quatro dígitos. O comitê de segurança avalia alternativas de autenticação (código por SMS, TOTP, notificação push e chaves FIDO2/WebAuthn), seguindo a recomendação da CISA de priorizar MFA resistente a phishing.

Considerando os fatores e os métodos de autenticação, avalie as afirmativas a seguir:

**I.** A combinação atual de senha e PIN não constitui MFA genuíno, pois os dois pertencem à mesma categoria de fator: algo que o usuário sabe.

**II.** O código enviado por SMS é a opção preferencial para as contas administrativas do PEP, pois esse canal é imune a SIM swap, a redirecionamento e a phishing.

**III.** Em aprovações por notificação push simples, o usuário pode aprovar uma solicitação indevida por fadiga de aprovação. Exibir o contexto do acesso e exigir correspondência numérica (number matching) reduz esse risco.

**IV.** Autenticadores FIDO2/WebAuthn têm alta resistência a phishing e são preferíveis para contas de maior risco, mas exigem um processo de recuperação bem projetado, pois uma recuperação fraca pode contornar o MFA.

**COMANDO**
É correto o que se afirma em:

**Alternativas:**
- **A)** Apenas I e II.
- **B)** Apenas II e III.
- **C)** Apenas I, II e IV.
- **D)** Apenas II, III e IV.
- **E)** Apenas I, III e IV.

**Gabarito: E**

**Julgamento das afirmativas:**
- **I — Verdadeira.** "Dois passos do mesmo fator não constituem MFA genuíno. Senha e PIN são ambos conhecimento; senha e aplicativo autenticador combinam conhecimento e posse" (p. 12).
- **II — Falsa.** Na tabela, o código por SMS tem resistência a phishing "baixa a média", os riscos são "SIM swap, redirecionamento, phishing", e o uso é "melhor que senha isolada, mas não preferencial" (p. 12).
- **III — Verdadeira.** Push simples: resistência média, risco de "fadiga de aprovação", e a recomendação é "usar contexto e number matching" (p. 13).
- **IV — Verdadeira.** FIDO2/WebAuthn: resistência alta, riscos de "perda do autenticador e recuperação mal projetada", "preferível para contas de maior risco" (p. 13). Também: "Recuperação fraca pode contornar MFA" (p. 25).

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Inclui II (falsa) e omite III e IV.
- **B) ❌** — Inclui II e omite I, que é a definição de MFA.
- **C) ❌** — Inclui II e omite III.
- **D) ❌** — Inclui II e omite I.
- **E) ✅** — I, III e IV são verdadeiras. II é falsa.

**Base no material:** apostila p. 12–13, parágrafo sobre fatores e tabela "Método / Resistência a phishing / Riscos principais / Uso recomendado" (senha, SMS, TOTP, push simples, FIDO2/WebAuthn, biometria local), CISA e NIST SP 800-63-4. Slides p. 11 e p. 12. Apostila p. 25, "Confirmar identidade → Autenticação proporcional ao risco → Recuperação fraca pode contornar MFA".
**Conceito-chave para a prova:** MFA exige fatores de **categorias diferentes** (saber, possuir, ser): senha + PIN não é MFA. Em resistência a phishing, FIDO2 é alta, TOTP e push são médias, e SMS é baixa a média. O push simples tem o risco da fadiga de aprovação, que se reduz com number matching. A recuperação de conta precisa ser tão forte quanto o MFA.

---

## I9 — Modelos de controle de acesso
**Subtópico coberto:** Modelos de controle de acesso DAC, MAC, RBAC, ABAC e ReBAC (apostila §6.1, p. 13; slides p. 11 "RBAC")
**Por que é provável:** a apostila tem uma tabela comparativa de 5 modelos (base de decisão, ponto forte, limitação), e o slide 11 destaca o RBAC. O cenário hospitalar da Q1 já usa RBAC, então um cenário em que o RBAC deixa de bastar é uma extensão natural.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única (com cenário)

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
O Prontuário Eletrônico do Paciente (PEP) de um hospital usa controle de acesso baseado em papéis (RBAC). Para atender a exigências cada vez mais específicas, a equipe chegou a 380 papéis, como "cardiologista-UTI-noturno-tablet" e "cardiologista-UTI-diurno-desktop", e a manutenção ficou inviável.

**DADOS DE SUPORTE**
A nova política aprovada pelo comitê de segurança determina que um profissional só pode **alterar prescrições** se, ao mesmo tempo:
- tiver vínculo ativo e especialidade compatível com o caso;
- o prontuário pertencer à unidade de internação em que ele está escalado;
- a ação solicitada for "prescrever" (e não apenas "visualizar");
- o acesso ocorrer durante o seu plantão, a partir de um dispositivo gerenciado pelo hospital e com sinal de risco de login considerado baixo.

**COMANDO**
Qual modelo de controle de acesso é o mais adequado para implementar essa política, e por quê?

**Alternativas:**
- **A)** DAC (controle discricionário), pois permite que cada médico, como "proprietário" dos prontuários que cria, conceda acesso a quem julgar necessário, o que garante flexibilidade sem risco de propagação excessiva de permissões.
- **B)** MAC (controle obrigatório), pois rótulos e política central oferecem controle rígido e se ajustam dinamicamente ao horário, ao dispositivo e à localização, sem perda de flexibilidade.
- **C)** ReBAC (baseado em relacionamentos), pois a decisão deriva de grafos de relações sociais e de colaboração entre entidades, cuja análise e auditoria são simples.
- **D)** ABAC (baseado em atributos), pois a decisão combina atributos do sujeito, do recurso, da ação e do contexto e permite controle granular e dinâmico, ao custo de políticas mais complexas.
- **E)** Manter o RBAC e criar um papel para cada combinação de especialidade, unidade, turno e tipo de dispositivo, já que a administração por papéis continua simples em qualquer escala.

**Gabarito: D**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — No DAC, a decisão é do proprietário do recurso. A limitação apontada pela apostila é justamente a "propagação excessiva de permissões", o oposto do que a alternativa afirma. Além disso, o DAC não avalia contexto.
- **B) ❌** — O MAC decide por "rótulos e política central", e sua limitação é a "menor flexibilidade". Não é um modelo voltado a decisões dinâmicas por contexto.
- **C) ❌** — O ReBAC decide por "relações entre entidades" e é "natural para grafos sociais e colaboração". A limitação é "análise e auditoria exigentes", e não "simples". A política descrita usa atributos e contexto, não relações.
- **D) ✅** — A política combina atributos do **sujeito** (vínculo, especialidade, escala), do **recurso** (unidade do prontuário), da **ação** (prescrever) e do **contexto** (plantão, dispositivo, risco do login). É a definição de ABAC: "decisão granular e dinâmica", com a limitação de "políticas mais complexas" (p. 13).
- **E) ❌** — A situação descrita é a "explosão de papéis", limitação do RBAC indicada na tabela. Criar mais papéis só agrava o problema.

**Base no material:** apostila p. 13, tabela "Modelo / Decisão baseada em / Ponto forte / Limitação" (DAC, MAC, RBAC, ABAC, ReBAC). Slides p. 11 ("Destaques inferiores: MFA; Mínimo privilégio; RBAC; Separação de funções").
**Conceito-chave para a prova:** DAC: o dono decide (permissões se propagam demais). MAC: rótulos e política central (rígido). RBAC: papéis (administração simples, mas explosão de papéis). ABAC: atributos de sujeito, recurso, ação e contexto (granular e dinâmico, políticas complexas). ReBAC: relações entre entidades (grafos, auditoria exigente).

---

## I10 — Zero Trust segmentação e mínimo privilégio
**Subtópico coberto:** Mínimo privilégio, privilégio efetivo, Zero Trust (NIST SP 800-207) e segmentação de rede (apostila p. 13, quadro "Mínimo privilégio" e parágrafo sobre Zero Trust; §7.1, p. 15; "Privilégio efetivo", p. 26; slides p. 11). Agrupa subtópicos curtos.
**Por que é provável:** a apostila tem um quadro em destaque sobre mínimo privilégio, desfaz um equívoco comum ("Zero Trust não significa desconfiar de pessoas") e aponta uma armadilha da segmentação ("exceções podem reabrir a superfície"). O slide 11 destaca "Mínimo privilégio" e "Separação de funções".
**Prioridade:** Média
**Tipo ENADE:** Afirmativas múltiplas

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
A rede de um hospital era "plana": qualquer dispositivo conectado ao Wi-Fi corporativo ou à VPN alcançava o servidor do Prontuário Eletrônico do Paciente (PEP), o sistema de imagens médicas e os sistemas administrativos. Após um incidente em que o atacante se moveu lateralmente a partir de um computador da recepção, a direção decidiu adotar uma arquitetura Zero Trust e segmentar a rede.

Considerando os conceitos de Zero Trust, segmentação e mínimo privilégio, avalie as afirmativas a seguir:

**I.** Em Zero Trust, estar na rede interna ou na VPN não confere confiança implícita. Cada acesso ao PEP deve considerar identidade, dispositivo, recurso, contexto, política e sinais de risco, com verificação contínua e privilégio mínimo.

**II.** Zero Trust significa desconfiar dos profissionais de saúde. Por isso, todo acesso deve permanecer bloqueado e só ser liberado por aprovação manual da equipe de segurança a cada requisição.

**III.** Na segmentação com regra "negar por padrão", apenas os fluxos necessários são liberados. Contudo, se o desenho ignorar administração, DNS, atualizações, monitoramento e caminhos de contingência, as exceções criadas depois podem reabrir a superfície que se pretendia reduzir.

**IV.** Para verificar se o mínimo privilégio está sendo cumprido, basta revisar o papel nominal de cada usuário, pois permissões concedidas por diferentes papéis e grupos não se somam no acesso efetivo.

**COMANDO**
É correto o que se afirma em:

**Alternativas:**
- **A)** Apenas I e III.
- **B)** Apenas II e IV.
- **C)** Apenas I, II e III.
- **D)** Apenas I, III e IV.
- **E)** I, II, III e IV.

**Gabarito: A**

**Julgamento das afirmativas:**
- **I — Verdadeira.** Zero Trust "significa não conceder confiança implícita apenas pela localização de rede. Cada acesso deve considerar identidade, dispositivo, recurso, contexto, política e sinais de risco, com verificação contínua e privilégio mínimo (NIST SP 800-207)" (p. 13).
- **II — Falsa.** "Zero Trust não significa desconfiar de pessoas" (p. 13). A verificação é contínua e baseada em política, não uma aprovação manual a cada requisição.
- **III — Verdadeira.** "Uma regra 'negar por padrão' libera apenas fluxos necessários. [...] O desenho precisa considerar administração, DNS, atualizações, monitoramento e caminhos de contingência; caso contrário, exceções podem reabrir a superfície que se pretendia reduzir" (p. 15).
- **IV — Falsa.** "Permissões concedidas por vários papéis e grupos podem se somar. Revise o acesso efetivo, não apenas o papel nominal" (p. 26).

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — I e III são verdadeiras. II e IV são falsas.
- **B) ❌** — Reúne justamente as duas afirmativas falsas.
- **C) ❌** — Inclui II, o equívoco de que Zero Trust é "desconfiar de pessoas".
- **D) ❌** — Inclui IV e ignora o privilégio efetivo.
- **E) ❌** — Considera verdadeiras II e IV.

**Base no material:** apostila p. 13 (quadro "Mínimo privilégio": "Conceda somente as permissões necessárias, pelo tempo necessário e no contexto necessário. Separe funções incompatíveis, revise acessos e revogue-os quando o vínculo mudar"; parágrafo sobre Zero Trust). Apostila p. 15, §7.1 "Segmentação e arquitetura" (DMZ, VLAN, microsegmentação, proxies). Apostila p. 25 ("Reduzir movimento lateral → Segmentação e privilégio mínimo → Regras mal mantidas criam exceções"). Apostila p. 26 ("Privilégio efetivo").
**Conceito-chave para a prova:** Zero Trust significa não ter confiança implícita por localização, com verificação contínua por identidade, dispositivo e contexto. Não é "desconfiar de pessoas". "Negar por padrão" só funciona se as exceções forem controladas. O mínimo privilégio se mede pelo acesso **efetivo**, que é a soma de papéis e grupos.

---

## I11 — Ataques de rede e controles correspondentes
**Subtópico coberto:** Phishing, DNS spoofing, evil twin, DoS/DDoS e sequestro de sessão, com as mitigações correspondentes (apostila §7, p. 14, tabela "Ataque / Mecanismo / Impacto / Mitigações combinadas"; slides p. 12 "Ataques frequentes e respectivas defesas")
**Por que é provável:** o slide 12 é inteiro uma tabela "ataque × controle", formato natural de questão de associação. A apostila amplia essa tabela na p. 14. A Q3 só usa a linha do ARP spoofing. O resumo do squad (slide 19) diz: "Ataques: cada problema exige um controle adequado".
**Prioridade:** Alta
**Tipo ENADE:** Associação

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
Os médicos de uma empresa de telemedicina atendem em campo e se conectam à plataforma a partir de hotéis, aeroportos e unidades parceiras. O relatório trimestral de incidentes registrou cinco tipos de ataque, e a equipe de segurança precisa relacionar cada um ao conjunto de controles mais adequado.

**DADOS DE SUPORTE**

Coluna I — Ataques
1. Phishing
2. DNS spoofing
3. Evil twin
4. DDoS
5. Sequestro de sessão

Coluna II — Ocorrência e controles recomendados
( ) Um ponto de acesso com o mesmo nome da rede Wi-Fi de um hotel parceiro capturou credenciais de médicos. Recomendam-se 802.1X com certificados, orientação aos usuários e VPN conforme o risco.
( ) O portal ficou indisponível após a exaustão de banda causada por tráfego vindo de milhares de origens. Recomendam-se capacidade, rate limit, CDN e acionamento do provedor.
( ) Recepcionistas receberam e-mails que imitavam o setor de TI e pediam a "revalidação" das senhas. Recomendam-se MFA, filtros e treinamento.
( ) Um token de sessão obtido por um atacante permitiu que ele usasse o portal como se fosse o médico. Recomendam-se TLS, cookies seguros, rotação e expiração dos tokens.
( ) Respostas falsas no cache do resolvedor fizeram o nome do portal apontar para um endereço malicioso. Recomendam-se DNSSEC onde aplicável, resolvedor seguro, TLS e validação.

**COMANDO**
Assinale a alternativa que apresenta a associação correta, na ordem de cima para baixo da Coluna II.

**Alternativas:**
- **A)** 3 – 4 – 1 – 2 – 5.
- **B)** 3 – 4 – 1 – 5 – 2.
- **C)** 2 – 4 – 1 – 5 – 3.
- **D)** 3 – 1 – 4 – 5 – 2.
- **E)** 1 – 4 – 3 – 5 – 2.

**Gabarito: B**

**Associação comentada:** AP que imita a rede legítima → **evil twin** (3). Exaustão de banda → **DDoS** (4). E-mail que imita a TI para roubar credenciais → **phishing** (1). Token obtido ou fixado → **sequestro de sessão** (5). Resposta ou cache DNS adulterado → **DNS spoofing** (2).

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Troca sequestro de sessão e DNS spoofing. TLS aparece nas duas mitigações, mas o mecanismo de cada ataque é diferente: token roubado em um caso, cache de nomes adulterado no outro.
- **B) ✅** — Todas as associações correspondem à tabela da p. 14 e ao slide 12.
- **C) ❌** — Associa o AP falso ao DNS spoofing e o cache adulterado ao evil twin.
- **D) ❌** — Troca DDoS e phishing.
- **E) ❌** — Troca phishing e evil twin. Os dois roubam credenciais, mas o evil twin faz isso por um ponto de acesso falso, e o phishing por mensagens enganosas.

**Base no material:** apostila p. 14, tabela de ataques (ARP spoofing, DNS spoofing, evil twin, DoS e DDoS, varredura, sequestro de sessão) e parágrafo sobre os limites do firewall. Slides p. 12 (Phishing → MFA, filtros e treinamento; MITM → TLS e validação de certificado; Ransomware → backup isolado; etc.).
**Conceito-chave para a prova:** Escolha o controle que atua sobre a **causa** do ataque. Evil twin → 802.1X, certificados e VPN. DNS spoofing → DNSSEC, resolvedor seguro e TLS. DDoS → capacidade, rate limit e CDN. Sequestro de sessão → cookies seguros, rotação e expiração. Phishing → MFA (de preferência resistente a phishing), filtros e treinamento.

---

## I12 — Tipos de código malicioso
**Subtópico coberto:** Tipos de malware: vírus, worm, trojan, ransomware, spyware/infostealer, rootkit e bot (apostila §8, p. 16)
**Por que é provável:** a apostila tem uma tabela "Tipo de código malicioso / Característica", conteúdo clássico de questão de associação, e nenhuma questão conhecida cobra malware. O slide 12 também traz ransomware.
**Prioridade:** Alta
**Tipo ENADE:** Associação

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
A equipe de resposta a incidentes de um hospital analisou cinco amostras de código malicioso encontradas em sua rede ao longo do ano e precisa classificá-las para o relatório enviado ao comitê de segurança da informação.

**DADOS DE SUPORTE**

Coluna I — Tipos de código malicioso
1. Vírus
2. Worm
3. Trojan (cavalo de Troia)
4. Ransomware
5. Rootkit

Coluna II — Amostras analisadas
( ) Um aplicativo distribuído como "calculadora de doses gratuita" instala, em segundo plano, um programa que abre acesso remoto ao computador do posto de enfermagem.
( ) Um código explora uma vulnerabilidade não corrigida no serviço de compartilhamento de arquivos e se propaga sozinho para dezenas de estações do hospital, sem ação dos usuários.
( ) Um código anexado a uma planilha de escalas só se espalha quando os funcionários abrem e executam o arquivo infectado.
( ) Os servidores do PEP têm os arquivos criptografados, e os atacantes exigem pagamento, ameaçando também publicar dados exfiltrados.
( ) Depois de obter privilégio administrativo, o atacante instala um componente que oculta seus processos e arquivos das ferramentas do sistema e mantém o privilégio obtido.

**COMANDO**
Assinale a alternativa que apresenta a associação correta, na ordem de cima para baixo da Coluna II.

**Alternativas:**
- **A)** 3 – 1 – 2 – 4 – 5.
- **B)** 2 – 3 – 1 – 4 – 5.
- **C)** 3 – 2 – 1 – 5 – 4.
- **D)** 1 – 2 – 3 – 4 – 5.
- **E)** 3 – 2 – 1 – 4 – 5.

**Gabarito: E**

**Associação comentada:** "calculadora gratuita" que executa ação maliciosa → **trojan** ("apresenta-se como legítimo para executar ação maliciosa"). Propagação autônoma por vulnerabilidade → **worm** ("propaga-se autonomamente por redes ou vulnerabilidades"). Anexado à planilha e dependente de execução → **vírus** ("anexa-se a outro arquivo e depende de execução para propagar"). Cifra e extorque, com dupla extorsão → **ransomware** ("criptografa, bloqueia ou exfiltra para extorquir"). Oculta a presença e mantém o privilégio → **rootkit**.

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Troca vírus e worm, a confusão mais comum: o vírus depende de execução, e o worm se propaga sozinho.
- **B) ❌** — Troca trojan e worm.
- **C) ❌** — Troca ransomware e rootkit.
- **D) ❌** — Segue a numeração da Coluna I sem analisar as amostras.
- **E) ✅** — Todas as associações correspondem à tabela da p. 16.

**Base no material:** apostila p. 16, tabela "Tipo de código malicioso / Característica". Ficaram fora da associação o spyware/infostealer ("coleta dados, credenciais, cookies e carteiras") e o bot ("integra o host a infraestrutura controlada remotamente"), que podem aparecer numa versão alterada. Slides p. 12: "Ransomware → Dados ficam inacessíveis → Backup isolado e restauração".
**Conceito-chave para a prova:** Vírus depende de hospedeiro e de execução. Worm se propaga sozinho. Trojan se disfarça de programa legítimo. Ransomware cifra, bloqueia ou exfiltra para extorquir. Rootkit oculta a presença. Spyware/infostealer rouba dados. Bot põe o host sob comando remoto.

---

## I13 — Responsabilidade compartilhada na nuvem
**Subtópico coberto:** Hardening, práticas essenciais (contas, serviços, segredos, backup) e segurança em nuvem com responsabilidade compartilhada (apostila §8, p. 15–16)
**Por que é provável:** a apostila tem uma frase de efeito ("'Está na nuvem' não é uma propriedade de segurança") e uma tabela de práticas essenciais. A Q2 do squad já usa um cenário de "prontuários eletrônicos em nuvem".
**Prioridade:** Média
**Tipo ENADE:** Asserção-razão

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
Um hospital migrou o seu Prontuário Eletrônico do Paciente (PEP) para máquinas virtuais em um provedor de nuvem pública, no modelo de Infraestrutura como Serviço (IaaS). Uma auditoria pós-migração encontrou: contas administrativas padrão ainda ativas nas máquinas virtuais; serviços de escuta desnecessários expostos à internet; a chave de acesso à conta do provedor gravada no código-fonte da aplicação; e backups mantidos na mesma conta de nuvem, sem versionamento. Ao receber o relatório, um diretor declarou: "Agora a segurança é problema do provedor".

Considerando esse cenário, avalie as asserções a seguir e a relação proposta entre elas:

**I.** Com a migração para o modelo IaaS, a responsabilidade pela gestão de identidades, pela configuração das máquinas virtuais e pela proteção dos prontuários passa integralmente ao provedor, pois "estar na nuvem" constitui, por si só, uma propriedade de segurança.

**PORQUE**

**II.** No modelo de responsabilidade compartilhada, o provedor protege parte da infraestrutura, enquanto o cliente continua responsável por identidades, configuração, dados e uso seguro, conforme o modelo de serviço contratado.

**COMANDO**
A respeito dessas asserções, assinale a opção correta:

**Alternativas:**
- **A)** As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
- **B)** As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
- **C)** A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
- **D)** A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
- **E)** As asserções I e II são proposições falsas.

**Gabarito: D**

**Julgamento:**
- **Asserção I — Falsa.** "O cliente continua responsável por identidades, configuração, dados e uso seguro conforme o modelo de serviço. 'Está na nuvem' não é uma propriedade de segurança" (p. 16). No IaaS, o sistema operacional das VMs e tudo o que roda nelas ficam com o cliente. Por isso os achados da auditoria (contas padrão, serviços expostos, segredo no código, backup sem versionamento) são do hospital.
- **Asserção II — Verdadeira.** É praticamente a frase da apostila: "Em nuvem, o provedor protege parte da infraestrutura, enquanto o cliente continua responsável [...]" (p. 16).
- **Relação:** como I é falsa, não há justificativa. A II, na verdade, **contradiz** a I.

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — I é falsa. A alternativa atrai quem lê só a II e reconhece o texto da apostila.
- **B) ❌** — Também exige I verdadeira.
- **C) ❌** — Inverte o julgamento: I é falsa e II é verdadeira.
- **D) ✅** — I é falsa e II é verdadeira.
- **E) ❌** — II é verdadeira.

**Base no material:** apostila p. 16, parágrafo sobre nuvem ("O projeto deve esclarecer responsabilidade compartilhada, região, chaves, logs, continuidade, portabilidade e dependência do provedor"). Apostila p. 15–16, hardening e tabela de práticas: "Contas: remover padrões [...]"; "Serviços: desativar o que não é necessário e limitar interfaces de escuta"; "Segredos: não gravar em código; usar cofre, rotação e escopo mínimo"; "Backup: cópias separadas, protegidas, versionadas e testadas". Apostila p. 19: "A responsabilidade não desaparece quando a execução é terceirizada".
**Conceito-chave para a prova:** Na nuvem, a responsabilidade é **compartilhada**: o provedor cuida de parte da infraestrutura, e o cliente sempre cuida de identidades, configuração e dados (no IaaS, também do SO e das aplicações). Hardening significa remover contas padrão, desativar serviços, guardar segredos em cofre e fazer backup separado e versionado.

---

## I14 — Injeção SQL e consultas parametrizadas
**Subtópico coberto:** Injeção SQL e consultas parametrizadas; riscos de aplicação do OWASP (apostila §9, p. 17, quadro "Exemplo de SQL injection" e tabela de riscos; "Escolha do controle pelo objetivo", p. 26; slides p. 12)
**Por que é provável:** o slide 12 traz "SQL Injection → Consultas parametrizadas". A apostila tem um quadro com o exemplo de concatenação e a ressalva "Escapar texto manualmente é mais frágil", e a revisão acrescenta que "Autorização ainda precisa ser verificada". Um enunciado com código é um formato comum no ENADE de Computação.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única (interpretação de código)

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
Durante um teste de intrusão no módulo de busca de pacientes do Prontuário Eletrônico do Paciente (PEP) de uma clínica, o analista digitou, no campo "nome", o texto `' OR '1'='1` e recebeu a lista completa de pacientes cadastrados, com dados de saúde.

**DADOS DE SUPORTE**
Trecho do código (Java) responsável pela busca:

```java
String sql = "SELECT * FROM pacientes WHERE nome = '" + entrada + "'";
Statement stmt = conexao.createStatement();
ResultSet rs = stmt.executeQuery(sql);
```

Com a entrada do analista, o comando enviado ao banco de dados foi:

```sql
SELECT * FROM pacientes WHERE nome = '' OR '1'='1'
```

**COMANDO**
Qual é a correção mais adequada para essa vulnerabilidade?

**Alternativas:**
- **A)** Escapar manualmente as aspas simples da entrada antes da concatenação, solução robusta que dispensa outras verificações de segurança no módulo.
- **B)** Cifrar a coluna `nome` com AES-256-GCM, pois a criptografia dos dados em repouso impede que a entrada do usuário altere a estrutura do comando SQL.
- **C)** Usar consulta parametrizada (por exemplo, `PreparedStatement` com `WHERE nome = ?`), enviando o valor separadamente do comando, de modo que a entrada não altere a estrutura SQL, e manter a verificação de autorização sobre quais pacientes o usuário pode consultar.
- **D)** Ocultar do usuário as mensagens de erro do banco de dados, o que elimina a vulnerabilidade, já que o atacante não conseguirá descobrir a estrutura das tabelas.
- **E)** Instalar um firewall de rede na borda, já que a filtragem de pacotes por porta e endereço impede que comandos SQL maliciosos cheguem ao servidor da aplicação pela porta 443.

**Gabarito: C**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — "Escapar texto manualmente é mais frágil" (p. 17). Esse tratamento depende do contexto, é fácil de errar e não dispensa outros controles.
- **B) ❌** — Confunde objetivos. A cifragem protege a confidencialidade em repouso, mas a injeção ocorre na **montagem do comando**, antes de qualquer cifragem. "Criptografia de disco protege mídia perdida, mas não impede que uma aplicação autenticada e vulnerável leia os dados" (p. 17).
- **C) ✅** — "Consultas parametrizadas enviam o valor separadamente, impedindo que a entrada altere a estrutura SQL" (p. 17). A revisão da p. 26 completa: "Prevenir injeção SQL → Consulta parametrizada → Autorização ainda precisa ser verificada".
- **D) ❌** — Esconder erros dificulta o reconhecimento do banco pelo atacante, mas a injeção continua funcionando. Basta ver que, no cenário, o ataque retornou todos os registros sem precisar de nenhuma mensagem de erro.
- **E) ❌** — O firewall "filtra tráfego conforme política, mas [...] não corrige uma aplicação vulnerável" (p. 14). A requisição maliciosa chega por um fluxo HTTPS legítimo.

**Base no material:** apostila p. 17, tabela de riscos de aplicação ("Injeção → Entrada muda o significado de comando SQL → Consultas parametrizadas e validação contextual") e quadro "Exemplo de SQL injection" ("Concatenar 'SELECT * FROM usuarios WHERE nome = ' + entrada mistura dados e comandos"). Apostila p. 26. Slides p. 12.
**Conceito-chave para a prova:** A injeção SQL acontece porque dados e comando são misturados por concatenação. A correção é a consulta parametrizada (prepared statement). Escape manual, cifragem, ocultar erros e firewall não resolvem. A parametrização também não substitui a autorização.

---

## I15 — Segurança de APIs e controle de acesso quebrado
**Subtópico coberto:** APIs, controle de acesso quebrado (IDOR), JWT, criptografia de banco de dados, segredos no código e SSDF (apostila §9, p. 16–17, Figura 7, tabela OWASP, parágrafos sobre bancos de dados e APIs; p. 16, "Segredos"; slides p. 12, "Acesso indevido em API" e exemplo `/api/alunos/105/documentos`)
**Por que é provável:** o slide 12 tem um "Exemplo prático" (trocar 105 por 106 e abrir o documento de outro aluno) que ainda não virou questão. A apostila traz o mesmo caso na tabela OWASP ("Usuário altera o ID na URL e vê registro alheio") e ressalvas sobre JWT e criptografia de disco que dão bons distratores.
**Prioridade:** Alta
**Tipo ENADE:** Afirmativas múltiplas

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
Em um portal de telemedicina, um paciente autenticado com MFA acessou os próprios exames pelo endereço `GET /api/pacientes/105/exames`. Por curiosidade, trocou 105 por 106 e conseguiu abrir os exames de outro paciente. A análise posterior mostrou que:
- a API verifica apenas se o token de sessão é válido;
- o token é um JWT assinado, cuja carga útil inclui nome, CPF e o código do diagnóstico do paciente;
- o banco de dados usa criptografia de disco;
- a chave de acesso ao serviço de envio de SMS está gravada no código-fonte, versionado em repositório compartilhado.

Considerando as boas práticas de segurança de aplicações e APIs, avalie as afirmativas a seguir:

**I.** A falha caracteriza controle de acesso quebrado: a autenticação forte do usuário não substitui a verificação, no servidor, da autorização para cada objeto e ação solicitados.

**II.** Como o JWT é assinado, o CPF e o diagnóstico contidos na carga útil estão protegidos contra leitura por terceiros, pois a assinatura garante a confidencialidade do conteúdo do token.

**III.** A criptografia de disco do banco de dados não impede esse vazamento, pois protege principalmente a mídia perdida, e não a leitura feita por uma aplicação autenticada e vulnerável.

**IV.** A chave do serviço de SMS deve sair do código-fonte e ir para um cofre de segredos, com rotação e escopo mínimo. Além disso, integrar ao ciclo de desenvolvimento práticas como requisitos de segurança, modelagem de ameaças, revisão e testes, como recomenda o NIST SSDF, ajuda a detectar falhas desse tipo antes da produção.

**COMANDO**
É correto o que se afirma em:

**Alternativas:**
- **A)** Apenas I e II.
- **B)** Apenas I e III.
- **C)** Apenas II e IV.
- **D)** Apenas II, III e IV.
- **E)** Apenas I, III e IV.

**Gabarito: E**

**Julgamento das afirmativas:**
- **I — Verdadeira.** Na tabela da p. 17: "Controle de acesso quebrado → Usuário altera o ID na URL e vê registro alheio → Autorização no servidor para cada objeto e ação". No slide 12: "Acesso indevido em API → Usuário acessa recurso de outro → Autorização no servidor". "Autenticar confirma quem; autorizar decide o que pode" (p. 25).
- **II — Falsa.** "Tokens assinados, como JWT, não são necessariamente secretos: o conteúdo pode ser legível. Assinatura verifica integridade e emissor; confidencialidade exige cifragem ou outra proteção" (p. 17). Além disso, colocar CPF e diagnóstico no token contraria a minimização.
- **III — Verdadeira.** "Criptografia de disco protege mídia perdida, mas não impede que uma aplicação autenticada e vulnerável leia os dados" (p. 17).
- **IV — Verdadeira.** Na tabela de práticas: "Segredos: não gravar em código; usar cofre, rotação e escopo mínimo" (p. 16). Sobre o SSDF: "O NIST SSDF recomenda integrar práticas de desenvolvimento seguro ao ciclo já usado pela equipe" (p. 17).

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Inclui II, a confusão entre assinatura e cifragem.
- **B) ❌** — Omite IV, que também é verdadeira.
- **C) ❌** — Inclui II e omite I, que é o diagnóstico central do caso.
- **D) ❌** — Inclui II e omite I.
- **E) ✅** — I, III e IV são verdadeiras. II é falsa.

**Base no material:** apostila p. 17 (tabela de riscos de aplicação; parágrafos "Bancos de dados exigem…" e "APIs devem autenticar o cliente, autorizar cada operação, limitar taxa e volume, validar esquema, proteger tokens, registrar eventos e evitar exposição excessiva"). Apostila p. 16 (tabela "Segredos"; Figura 7, ciclo Requisitos → Projeto → Código → Teste → Operação). Slides p. 12 (exemplo `/api/alunos/105/documentos`).
**Conceito-chave para a prova:** IDOR é controle de acesso quebrado e se corrige com autorização **no servidor**, objeto a objeto. JWT assinado não é sigiloso: a assinatura garante integridade e emissor, não confidencialidade. Criptografia de disco não protege contra a própria aplicação. Segredos ficam em cofre, nunca no código.

---

## I16 — Modelagem de ameaças STRIDE
**Subtópico coberto:** Modelagem de ameaças e STRIDE × propriedade ameaçada (apostila §9.1, p. 17–18)
**Por que é provável:** a apostila tem uma tabela de seis linhas relacionando cada ameaça STRIDE a uma propriedade, o que permite uma questão com "ocorrências" numeradas, como a Q1. Nenhuma questão conhecida cobra STRIDE.
**Prioridade:** Média
**Tipo ENADE:** Afirmativas múltiplas (com cenários numerados, como as "ocorrências" da Q1)

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
Antes de implementar um novo aplicativo de prescrição eletrônica, a equipe de uma empresa de telemedicina fez a modelagem de ameaças: decompôs a arquitetura, identificou ativos e limites de confiança e enumerou abusos usando o modelo STRIDE. Foram registrados os seguintes cenários:

**DADOS DE SUPORTE**
1. Um atacante usa um token de sessão roubado para se passar por um médico e emitir receitas.
2. Um atacante altera a dosagem de um medicamento em uma receita antes que ela chegue à farmácia.
3. Um médico nega ter cancelado uma consulta, e não existem logs protegidos que comprovem a ação.
4. Um paciente explora uma falha da API e passa a executar funções reservadas aos administradores.

Considerando a relação entre as categorias do STRIDE e as propriedades de segurança ameaçadas, avalie as afirmativas a seguir:

**I.** O cenário 1 corresponde a *Spoofing* (falsificação), que ameaça a autenticidade.

**II.** O cenário 2 corresponde a *Tampering* (adulteração), que ameaça a integridade.

**III.** O cenário 3 corresponde a *Repudiation* (repúdio), que ameaça a confidencialidade, pois a ação pode ser negada.

**IV.** O cenário 4 corresponde a *Elevation of privilege* (elevação de privilégio), que ameaça a autorização.

**COMANDO**
É correto o que se afirma em:

**Alternativas:**
- **A)** Apenas I, II e IV.
- **B)** Apenas I e II.
- **C)** Apenas II e III.
- **D)** Apenas III e IV.
- **E)** I, II, III e IV.

**Gabarito: A**

**Julgamento das afirmativas:**
- **I — Verdadeira.** "Spoofing → Autenticidade → Alguém pode fingir ser outra entidade?" (p. 18).
- **II — Verdadeira.** "Tampering → Integridade → Dados ou código podem ser alterados?"
- **III — Falsa.** O cenário é mesmo de *Repudiation*, mas a propriedade ameaçada é a **responsabilização**: "A ação pode ser negada por falta de evidência?". Confidencialidade corresponde a *Information disclosure* ("Informação pode vazar?").
- **IV — Verdadeira.** "Elevation of privilege → Autorização → Alguém pode obter capacidade maior que a permitida?"

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — I, II e IV são verdadeiras. III associa o repúdio à propriedade errada.
- **B) ❌** — Omite IV, que também é verdadeira.
- **C) ❌** — Inclui III (falsa) e omite I e IV.
- **D) ❌** — Inclui III e omite I e II.
- **E) ❌** — A categoria da III está certa, mas a propriedade não. É a pegadinha central da questão.

**Base no material:** apostila p. 17–18, §9.1 ("Um processo simples inclui decompor a arquitetura, identificar ativos e limites de confiança, enumerar abusos, priorizar riscos e definir controles verificáveis") e tabela "STRIDE / Propriedade ameaçada / Pergunta". Apostila p. 5–6, princípio da Responsabilização ("É possível atribuir ações a uma entidade?").
**Conceito-chave para a prova:** S → autenticidade. T → integridade. R → responsabilização (não repúdio). I → confidencialidade. D → disponibilidade. E → autorização. A modelagem de ameaças é feita **antes** da implementação.

---

## I17 — Governança ISO 27001 e NIST CSF 2.0
**Subtópico coberto:** Governança e Sistema de Gestão (SGSI): ISO/IEC 27001, funções do NIST CSF 2.0, hierarquia documental, papéis e indicadores (apostila §10, p. 19; Figura 6, p. 15)
**Por que é provável:** a apostila dedica uma figura às seis funções do NIST CSF 2.0 e uma tabela a política, norma, procedimento, guia e registro. O checklist pede "Explico funções do NIST CSF 2.0". A Q1 do squad já cita auditoria ISO/IEC 27001.
**Prioridade:** Média
**Tipo ENADE:** Afirmativa negativa (assinale a INCORRETA)

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
Um hospital decidiu implantar um Sistema de Gestão de Segurança da Informação (SGSI) para o seu Prontuário Eletrônico do Paciente (PEP) e para os serviços de telemedicina. O comitê responsável reuniu-se para alinhar conceitos de governança, documentação, papéis e frameworks de referência antes de redigir os primeiros documentos.

**COMANDO**
Considerando os conceitos de governança e gestão de segurança da informação, assinale a alternativa **INCORRETA**.

**Alternativas:**
- **A)** A ISO/IEC 27001 especifica requisitos para um Sistema de Gestão de Segurança da Informação baseado em risco e em melhoria contínua.
- **B)** O NIST CSF 2.0 organiza seus resultados em cinco funções (Identificar, Proteger, Detectar, Responder e Recuperar) e deixa a governança fora do escopo do framework.
- **C)** "Todo acesso administrativo ao PEP exige MFA" é um exemplo de política, enquanto "como revogar a conta de um profissional desligado" é um exemplo de procedimento.
- **D)** Ao terceirizar a operação do datacenter, o hospital continua responsável pela segurança da informação, pois a responsabilidade não desaparece quando a execução é terceirizada, e os fornecedores devem atender às obrigações contratuais.
- **E)** Indicadores como cobertura de MFA e tempo para corrigir vulnerabilidades críticas devem ter definição, fonte, periodicidade, meta e responsável, pois uma métrica pode ser manipulada ou perder contexto.

**Gabarito: B**

**Por que cada alternativa está certa ou errada:**
- **A) ❌ (afirmação correta)** — É a definição da p. 19: "A ISO IEC 27001 especifica requisitos para um Sistema de Gestão de Segurança da Informação baseado em risco e melhoria contínua".
- **B) ✅ (afirmação INCORRETA, portanto o gabarito)** — O NIST CSF 2.0 tem **seis** funções: "Governar, Identificar, Proteger, Detectar, Responder e Recuperar" (p. 19). Na Figura 6 (p. 15), as seis funções aparecem em volta da "Gestão do risco cibernético". A versão de cinco funções, sem "Governar", é a do CSF anterior (1.x).
- **C) ❌ (afirmação correta)** — Os dois exemplos estão na tabela da p. 19. A política "expressa direção e regras de alto nível", e o procedimento "explica sequência operacional".
- **D) ❌ (afirmação correta)** — "A responsabilidade não desaparece quando a execução é terceirizada" e "fornecedores atendem obrigações contratuais" (p. 19).
- **E) ❌ (afirmação correta)** — "Uma métrica pode ser manipulada ou perder contexto, por isso deve ter definição, fonte, periodicidade, meta e responsável" (p. 19).

**Base no material:** apostila p. 19, §10 (governança × gestão; ISO/IEC 27001; NIST CSF 2.0; tabela Política / Norma interna / Procedimento / Guia / Registro e evidência; papéis; indicadores). Apostila p. 15, Figura 6, "Funções do NIST Cybersecurity Framework 2.0" ("As funções do NIST CSF 2.0 são contínuas e interdependentes").
**Conceito-chave para a prova:** O NIST CSF 2.0 tem **6 funções**: Governar, Identificar, Proteger, Detectar, Responder e Recuperar. "Governar" é a novidade da versão 2.0. A ISO/IEC 27001 define requisitos de SGSI baseados em risco e melhoria contínua. Política dá a direção, norma traz o requisito específico, procedimento descreve o passo a passo, guia orienta, e registro serve de evidência. Terceirizar a execução não terceiriza a responsabilidade.

---

## I18 — Tratamento de riscos
**Subtópico coberto:** Respostas ao risco: evitar, mitigar, transferir ou compartilhar, aceitar (apostila §10.1, p. 19; quadro "Risco inerente e residual", p. 7)
**Por que é provável:** a apostila apresenta uma tabela "Resposta / Quando faz sentido / Exemplo" e retoma as quatro decisões no quadro da p. 7. Pegadinha prevista no material: o seguro transfere a parte financeira "sem eliminar deveres legais".
**Prioridade:** Média
**Tipo ENADE:** Associação

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
Depois de calcular o risco residual dos sistemas de um hospital, o comitê de riscos precisa registrar, para cada caso, a resposta adotada, conforme o apetite a risco aprovado pela diretoria.

**DADOS DE SUPORTE**

Coluna I — Respostas ao risco
1. Evitar
2. Mitigar
3. Transferir ou compartilhar
4. Aceitar

Coluna II — Decisões do comitê
( ) Contratar um seguro cibernético e incluir cláusulas de responsabilidade no contrato com o provedor de nuvem, sabendo que os deveres legais do hospital perante a LGPD permanecem.
( ) Registrar formalmente, com prazo de revisão e responsável, a decisão de manter um risco residual baixo que cabe no apetite a risco aprovado.
( ) Retirar da internet um servidor legado de agendamento, sem suporte do fabricante, cujo benefício não compensa o risco.
( ) Implantar MFA e segmentação de rede para reduzir a probabilidade e o impacto de acessos indevidos ao PEP.

**COMANDO**
Assinale a alternativa que apresenta a associação correta, na ordem de cima para baixo da Coluna II.

**Alternativas:**
- **A)** 2 – 4 – 1 – 3.
- **B)** 3 – 1 – 4 – 2.
- **C)** 1 – 4 – 3 – 2.
- **D)** 2 – 1 – 4 – 3.
- **E)** 3 – 4 – 1 – 2.

**Gabarito: E**

**Associação comentada:** seguro e contrato → **transferir ou compartilhar** ("outra parte assume parcela financeira ou operacional"; exemplo: "Seguro e contrato, sem eliminar deveres legais"). Registro de decisão sobre risco que cabe no apetite → **aceitar** ("Registrar decisão, prazo e responsável"). Retirar o serviço legado → **evitar** ("A atividade não compensa o risco"; exemplo: "Retirar serviço legado da internet"). MFA e segmentação → **mitigar** ("Controles reduzem probabilidade ou impacto"; exemplo: "MFA e segmentação").

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Trata o seguro como mitigação e a contratação de controles como transferência.
- **B) ❌** — Confunde aceitar com evitar. Aceitar é manter o risco formalmente, e evitar é eliminar a atividade.
- **C) ❌** — Trata o seguro como "evitar", como se ele eliminasse o risco e os deveres legais.
- **D) ❌** — Erra todas as associações.
- **E) ✅** — 3 – 4 – 1 – 2, conforme a tabela da p. 19.

**Base no material:** apostila p. 19, §10.1, tabela "Resposta / Quando faz sentido / Exemplo". Apostila p. 7: "A direção deve decidir se aceita, reduz, evita ou transfere esse risco dentro de limites definidos".
**Conceito-chave para a prova:** Evitar é eliminar a atividade. Mitigar é aplicar controles. Transferir é passar a parte financeira ou operacional (seguro, contrato) **sem** transferir os deveres legais. Aceitar é uma decisão formal da direção, com registro, prazo e responsável, para riscos dentro do apetite.

---

## I19 — Etapas da resposta a incidentes
**Subtópico coberto:** Gestão de incidentes segundo o NIST SP 800-61 Rev. 3, etapas e cadeia de custódia (apostila §11, p. 19–20)
**Por que é provável:** a apostila apresenta as etapas em lista ordenada e um quadro em destaque sobre cadeia de custódia. O checklist pede "Explico [...] ciclo de resposta". Uma sequência de etapas é o formato ideal para questão de ordenação.
**Prioridade:** Média
**Tipo ENADE:** Ordenação

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
Em uma madrugada, o SIEM de um hospital alertou para a cifragem em massa de arquivos em servidores do Prontuário Eletrônico do Paciente (PEP), indício de ransomware. O plano de resposta a incidentes do hospital segue o NIST SP 800-61 Rev. 3, integrado ao NIST CSF 2.0, e prevê as ações abaixo, listadas fora de ordem.

**DADOS DE SUPORTE**
I. Erradicar a causa: remover o código malicioso, corrigir a vulnerabilidade explorada e trocar as credenciais e os segredos comprometidos.
II. Confirmar o evento e preservar evidências, registrando origem, coletor, data, método, hash e armazenamento de cada evidência (cadeia de custódia).
III. Conter o incidente, isolando os segmentos afetados sem destruir evidências nem ampliar o impacto.
IV. Recuperar o PEP em etapas, a partir de backup íntegro, monitorando recaídas e validando a integridade dos dados.
V. Classificar a gravidade, identificar ativos, dados e dependências afetados e acionar os papéis técnicos, jurídicos, de comunicação e a direção, conforme o plano.
VI. Documentar as decisões, comunicar o incidente quando exigido (por exemplo, à ANPD e aos titulares) e acompanhar as melhorias decorrentes das lições aprendidas.

**COMANDO**
Assinale a alternativa que apresenta a ordem correta das ações.

**Alternativas:**
- **A)** II, III, V, I, IV, VI.
- **B)** V, II, III, IV, I, VI.
- **C)** II, V, I, III, IV, VI.
- **D)** II, V, III, I, IV, VI.
- **E)** III, II, V, IV, I, VI.

**Gabarito: D**

**Ordem comentada (apostila p. 20):** (1) confirmar o evento e preservar evidências → II; (2–3) classificar a gravidade, os ativos e as dependências e acionar os papéis conforme o plano → V; (4) conter sem destruir evidências → III; (5) erradicar a causa e trocar segredos → I; (6) recuperar em etapas e validar a integridade → IV; (7) documentar, comunicar e acompanhar melhorias → VI.

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Põe a contenção antes da classificação e do acionamento dos papéis. O plano prevê classificar e acionar primeiro, para não improvisar.
- **B) ❌** — Classifica antes de confirmar o evento e recupera antes de erradicar a causa, o que permite a reinfecção.
- **C) ❌** — Erradica antes de conter, enquanto o ataque ainda se propaga.
- **D) ✅** — Segue a sequência da p. 20.
- **E) ❌** — Contém antes de confirmar o evento e preservar evidências, com risco de destruí-las, e recupera antes de erradicar.

**Base no material:** apostila p. 20, parágrafo do NIST SP 800-61 Rev. 3 ("detecção e análise estabelecem o que aconteceu; contenção limita propagação; erradicação remove causa; recuperação restaura com segurança; lições aprendidas corrigem processos e controles") e lista de etapas (numerada no PDF de 5 a 11 por erro de formatação). Quadro "Cadeia de custódia": "Preservar evidência pode conflitar com restaurar rapidamente; o plano deve definir critérios e autoridade para a decisão". A comunicação à ANPD e aos titulares (art. 48 da LGPD) é conhecimento padrão que concretiza o "comunicar quando exigido" da apostila.
**Conceito-chave para a prova:** A ordem é: confirmar e preservar evidências → classificar e acionar → **conter** → **erradicar** → **recuperar** → documentar e aprender. Conter vem antes de erradicar, e erradicar vem antes de recuperar. A cadeia de custódia registra origem, coletor, data, método, hash e transferências.

---

## I20 — Continuidade de negócios e ransomware
**Subtópico coberto:** Continuidade de negócios e recuperação: BIA; continuidade × recuperação de desastre × resposta a incidentes; backups; sites frio, morno e quente; alta disponibilidade (apostila §12, p. 20; "Armadilha comum", p. 9; p. 25–26; slides p. 12, "Ransomware → Backup isolado e restauração")
**Por que é provável:** o slide 12 liga ransomware a "backup isolado e restauração", e a apostila tem uma tabela de estratégias com a ressalva de que a alta disponibilidade "não corrige exclusão lógica ou ransomware", repetida nas revisões (p. 9, p. 25 e p. 26). O cenário hospitalar segue o estilo do squad.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única (com cenário)

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
Um ransomware cifrou os servidores do Prontuário Eletrônico do Paciente (PEP) de um hospital. O hospital mantém um site quente com replicação síncrona dos dados e faz backups diários em um compartilhamento de rede permanentemente conectado ao domínio, nunca testados. Os requisitos aprovados são RTO de 4 horas e RPO de 15 minutos. Em reunião de crise, o comitê discute como retomar o atendimento nas UTIs e no pronto-socorro.

**COMANDO**
Considerando os conceitos de continuidade de negócios e recuperação, assinale a alternativa correta.

**Alternativas:**
- **A)** O site quente com replicação síncrona garante a recuperação de dados íntegros, pois a alta disponibilidade corrige a exclusão lógica e a cifragem provocadas por ransomware.
- **B)** Continuidade de negócios, recuperação de desastre e resposta a incidentes são sinônimos, de modo que um único plano genérico atende às três necessidades.
- **C)** Um site frio seria a melhor alternativa para cumprir o RTO de 4 horas, pois oferece retorno rápido com baixo custo.
- **D)** A existência dos backups diários no compartilhamento de rede comprova a recuperabilidade do PEP e dispensa testes de restauração.
- **E)** A replicação para o site quente pode propagar a cifragem, por isso a recuperação depende de backup isolado, protegido, versionado e com restauração testada. A Análise de Impacto no Negócio (BIA) deve identificar processos essenciais, como prescrição e monitoramento em UTI, e suas dependências, para definir prioridades de retomada.

**Gabarito: E**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Na tabela da p. 20, a alta disponibilidade "reduz falha de componente", mas "não corrige exclusão lógica ou ransomware". O site quente tem o "risco de replicar corrupção".
- **B) ❌** — "Continuidade mantém operação mínima; recuperação de desastre restaura tecnologia; resposta a incidentes trata o evento de segurança. Os planos se conectam, mas não são sinônimos" (p. 20).
- **C) ❌** — O site frio tem "baixo custo", mas "recuperação lenta e maior configuração". Retorno rápido é característica do site quente.
- **D) ❌** — "Backup não prova recuperabilidade" (p. 9). Além disso, uma "cópia online pode ser cifrada junto" (p. 26). Backup diário também não atende a um RPO de 15 minutos.
- **E) ✅** — Reúne as recomendações do material: "Recuperar após ransomware → Backup isolado e restauração testada" (p. 26); "Backup: cópias separadas, protegidas, versionadas e testadas" (p. 16); e a BIA "identifica processos essenciais, dependências e consequências da interrupção" (p. 20).

**Base no material:** apostila p. 20, §12 e tabela "Estratégia / Vantagem / Cuidado" (backup completo/incremental/diferencial, sites frio, morno e quente, alta disponibilidade). Apostila p. 9, "Armadilha comum". Apostila p. 25, "Backup e redundância". Apostila p. 26, "Recuperar após ransomware". Slides p. 12.
**Conceito-chave para a prova:** Redundância e alta disponibilidade **não** substituem backup, porque replicam também a cifragem. Contra ransomware, use backup isolado, versionado e com restauração testada. Site frio é barato e lento, site morno é intermediário, e site quente é rápido e caro (e pode replicar corrupção). A BIA define o que retomar primeiro. Continuidade, recuperação de desastre e resposta a incidentes são planos distintos.

---

## I21 — LGPD agentes de tratamento princípios e bases legais
**Subtópico coberto:** LGPD: controlador, operador e encarregado; princípios (finalidade, necessidade/minimização etc.); consentimento como uma das bases legais; privacy by design; privacidade × segurança; biometria (apostila §13, p. 20–21; slides p. 15–16, quadro "Atenção")
**Por que é provável:** o slide 16 (biometria facial) só aparece como "questões para análise" discursivas (Q9). O quadro "Atenção" do slide ("Consentimento não autoriza qualquer finalidade", "Coletar mais dados do que o necessário contraria a minimização") e a tabela da apostila sobre controlador, operador e encarregado ainda não têm versão objetiva.
**Prioridade:** Alta
**Tipo ENADE:** Afirmativas múltiplas

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
Uma rede de clínicas decidiu implantar reconhecimento facial na recepção para o check-in dos pacientes. A rede definiu a finalidade e os meios do tratamento e contratou uma empresa de tecnologia para processar as imagens em nuvem, seguindo as instruções da rede. No formulário de cadastro, os pacientes assinalam uma caixa de consentimento. O projeto prevê armazenar as imagens cifradas e com controle de acesso, e a diretoria cogita reutilizá-las futuramente em campanhas de marketing.

Considerando a Lei Geral de Proteção de Dados Pessoais (LGPD — Lei nº 13.709/2018), avalie as afirmativas a seguir:

**I.** A rede de clínicas, que decide sobre o tratamento, é a controladora. A empresa contratada, que processa as imagens em nome dela, é a operadora. O encarregado atua como canal de comunicação entre os agentes de tratamento, os titulares e a ANPD.

**II.** Como o consentimento foi coletado no cadastro, a rede pode reutilizar as imagens faciais em campanhas de marketing e em qualquer outra finalidade futura, pois o consentimento é a base legal que autoriza qualquer tratamento.

**III.** Pelo princípio da necessidade (minimização), se um documento com foto ou um QR code atender à finalidade de check-in, a coleta de biometria facial pode ser excessiva. A solução deve ter finalidade específica, prazo de retenção definido e segurança proporcional, desde o projeto (privacy by design).

**IV.** Como as imagens serão armazenadas cifradas e com controle de acesso, o tratamento é necessariamente legítimo e proporcional, pois segurança da informação e privacidade são conceitos equivalentes.

**COMANDO**
É correto o que se afirma em:

**Alternativas:**
- **A)** Apenas I e II.
- **B)** Apenas II e IV.
- **C)** Apenas I e III.
- **D)** Apenas I, III e IV.
- **E)** I, II, III e IV.

**Gabarito: C**

**Julgamento das afirmativas:**
- **I — Verdadeira.** Pela tabela da p. 21: o controlador "decide sobre o tratamento"; o operador "trata dados em nome do controlador"; o encarregado é o "canal entre agentes, titulares e ANPD conforme a lei e regulamentação" (art. 5º, VI, VII e VIII).
- **II — Falsa.** "Consentimento é apenas uma das bases legais e não deve ser usado como resposta automática para qualquer tratamento" (p. 21). O quadro do slide 16 diz: "Consentimento não é a única base legal; Consentimento não autoriza qualquer finalidade". O reuso para marketing viola o princípio da finalidade.
- **III — Verdadeira.** O slide 16 pergunta "A coleta é realmente necessária? Existe uma alternativa menos invasiva?" e afirma: "Coletar mais dados do que o necessário contraria a minimização". Privacy by design inclui "minimização, [...] retenção definida, [...] segurança proporcional" (p. 21).
- **IV — Falsa.** "Segurança e privacidade se sobrepõem, mas não são iguais: um tratamento pode ser tecnicamente seguro e ainda ser excessivo ou sem base legal" (p. 21).

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Inclui II, o erro de achar que o consentimento autoriza tudo.
- **B) ❌** — Reúne as duas afirmativas falsas.
- **C) ✅** — I e III são verdadeiras. II e IV são falsas.
- **D) ❌** — Inclui IV, que confunde segurança com privacidade.
- **E) ❌** — Considera verdadeiras II e IV.

**Base no material:** apostila p. 20–21, §13 (tabela "Conceito LGPD"; princípios: "finalidade, adequação, necessidade, livre acesso, qualidade, transparência, segurança, prevenção, não discriminação e responsabilização"; parágrafo sobre privacy by design). Apostila p. 25: "Privacidade governa tratamento justo e proporcional; segurança protege contra eventos adversos". Apostila p. 26: "Atender necessidade da LGPD → Minimização e base legal adequada → Consentimento não é a única base". Slides p. 15–16.
**Conceito-chave para a prova:** O controlador decide, o operador executa em nome do controlador, e o encarregado é o canal com titulares e ANPD. O consentimento é **uma** das bases legais e não autoriza qualquer finalidade. A necessidade (minimização) obriga a escolher a alternativa menos invasiva. Tratamento seguro não é, só por isso, tratamento legítimo.

---

## I22 — Segurança em sistemas distribuídos IA e segurança física
**Subtópico coberto:** Relações da segurança com outras matérias: sistemas distribuídos e dependabilidade, inteligência artificial, segurança física e ambiental (apostila §14, §14.1–14.3, p. 21–23)
**Por que é provável:** a apostila dedica uma seção com tabela "Área / Relação / Exemplo de questão integrada" e três subseções. O ENADE costuma cobrar a integração entre áreas. A prioridade é baixa porque os slides não tratam do tema.
**Prioridade:** Baixa
**Tipo ENADE:** Afirmativas múltiplas

**Enunciado:**

**SITUAÇÃO-PROBLEMA**
Um grupo hospitalar está modernizando sua plataforma digital. O projeto inclui: um Prontuário Eletrônico do Paciente (PEP) distribuído, com réplicas em várias unidades; um assistente de triagem baseado em modelo de linguagem (LLM), que lê as queixas digitadas pelos pacientes e consulta dados do PEP; e um novo datacenter próprio. O comitê de segurança avaliou os riscos de cada componente.

Considerando as relações entre a Segurança da Informação e outras áreas da Computação, avalie as afirmativas a seguir:

**I.** No PEP distribuído, falhas parciais e mensagens atrasadas, duplicadas ou fora de ordem exigem autenticação de serviços, limitação de repetição, idempotência e sincronização de tempo. Além disso, alta disponibilidade sem consistência pode servir dados clínicos incorretos.

**II.** No assistente de triagem, textos maliciosos inseridos pelos usuários podem caracterizar *prompt injection*, e dados de treinamento adulterados podem caracterizar envenenamento de dados. Contra esses riscos, controles tradicionais como inventário, controle de acesso, validação, monitoramento e governança continuam válidos.

**III.** Como o PEP terá autenticação forte e criptografia em trânsito, controles físicos no datacenter, como zonas de acesso, registro de visitantes, climatização, UPS e descarte seguro de mídias, tornam-se dispensáveis, pois a segurança lógica independe do ambiente físico.

**IV.** No PEP distribuído, priorizar a consistência e eliminar as réplicas remove os pontos únicos de falha do sistema, pois a redundância é a principal causa de indisponibilidade em sistemas distribuídos.

**COMANDO**
É correto o que se afirma em:

**Alternativas:**
- **A)** Apenas I e II.
- **B)** Apenas I e III.
- **C)** Apenas II e IV.
- **D)** Apenas I, II e IV.
- **E)** I, II, III e IV.

**Gabarito: A**

**Julgamento das afirmativas:**
- **I — Verdadeira.** "Sistemas distribuídos falham parcialmente [...]; mensagens podem atrasar, duplicar ou chegar fora de ordem. Segurança exige autenticar serviços, proteger segredos, limitar repetição, lidar com idempotência, sincronizar tempo e manter observabilidade. Alta disponibilidade sem consistência pode servir dados incorretos" (p. 22).
- **II — Verdadeira.** "Exemplos: envenenamento de dados, entrada adversarial, extração de modelo, prompt injection em aplicações com LLM [...]. Controles tradicionais continuam válidos: inventário, acesso, validação, monitoramento, testes, governança, minimização e resposta" (p. 22).
- **III — Falsa.** "A segurança lógica pode falhar se alguém retirar um disco não criptografado ou conectar equipamento à rede interna" (p. 23). Os controles físicos complementam os lógicos e não podem ser dispensados.
- **IV — Falsa.** É o contrário: "consistência sem redundância pode criar ponto único de falha" (p. 22). A redundância **reduz** a falha de componente.

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — I e II são verdadeiras. III e IV são falsas.
- **B) ❌** — Inclui III, a ideia de que a segurança lógica dispensa a física.
- **C) ❌** — Inclui IV (falsa) e omite I.
- **D) ❌** — Inclui IV, que inverte o papel da redundância.
- **E) ❌** — Considera verdadeiras III e IV.

**Base no material:** apostila p. 21–22, tabela "Relações com outras matérias da Computação" (Sistemas Distribuídos: "Manter integridade sob falhas"; IA e Dados: "Avaliar risco de modelo e dataset"). Apostila p. 22, §14.1 e §14.2. Apostila p. 22–23, §14.3 ("Ameaças físicas incluem acesso não autorizado, furto, incêndio, água, calor e perda de energia. Controles combinam zonas, identificação, registro de visitantes, detecção, climatização, UPS, gerador e descarte seguro").
**Conceito-chave para a prova:** Em sistemas distribuídos, alta disponibilidade sem consistência gera dados errados, e consistência sem redundância cria um ponto único de falha. Os riscos de IA (prompt injection, envenenamento, extração de modelo) pedem os mesmos controles clássicos. Segurança física e segurança lógica se complementam.
