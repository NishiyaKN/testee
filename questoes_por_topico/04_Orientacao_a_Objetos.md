# Orientação a Objetos — Questões e Gabarito Comentado

**Squad responsável:** Squad 10
**Materiais analisados:**
| Arquivo | Páginas | Tipo | Questões encontradas (páginas) |
|---|---|---|---|
| `Apresentação Orientacao a Objetos.pdf` | 34 | Slides ("Revisão técnica · ENADE · Computação") | Q1–Q6, objetivas no estilo ENADE, todas com gabarito comentado (p. 3–33). Cada questão ocupa 5 slides: enunciado → cenário → alternativas → gabarito comentado → conceito consolidado |
| `Material sobre Orientação a Objetos.pdf` | 25 (numeração impressa 1–22 começa na p. 4 do PDF) | Material explicativo (apostila) | Nenhuma questão objetiva. Exercícios discursivos sem gabarito: Q7 "Verificação rápida" (p. 9), Q8 "Atividade 1" (p. 22–23), Q9 "Atividade 2" (p. 23), Q10 "Atividade 3" (p. 23) |

**Resumo:** 10 questões encontradas.
- **6 objetivas no estilo ENADE (Q1–Q6)**, todas nos slides e todas **com gabarito dado pelo próprio material**, com justificativa de cada alternativa. Têm **4 alternativas (A–D)**, não 5. Na prova pode aparecer uma alternativa E.
- **4 exercícios discursivos (Q7–Q10)** na apostila, **sem gabarito no material** (resolvidos aqui).
- Nenhuma questão aparece repetida entre os dois arquivos. A apostila é a base teórica das questões dos slides (as referências cruzadas estão em cada questão).
- Gabaritos conferidos de forma independente. O código Java de Q1 foi **compilado e executado (OpenJDK 21): imprime `175.0`**, confirmando o gabarito D. Os códigos de Q2, Q4 e Q6 também compilam.

> Legenda: ✅ correta · ❌ incorreta · ⚠️ ponto de atenção (gabarito do material duvidoso, ambiguidade, versão divergente)

## Índice
1. [Q1 — Polimorfismo, vinculação dinâmica e field shadowing](#q1--polimorfismo-vinculação-dinâmica-e-field-shadowing)
2. [Q2 — Herança x composição (sensor IoT)](#q2--herança-x-composição-sensor-iot)
3. [Q3 — UML: multiplicidades e composição (clínica veterinária)](#q3--uml-multiplicidades-e-composição-clínica-veterinária)
4. [Q4 — Padrão Strategy e OCP (cálculo de frete)](#q4--padrão-strategy-e-ocp-cálculo-de-frete)
5. [Q5 — Classe abstrata x interface (dispositivos IoT)](#q5--classe-abstrata-x-interface-dispositivos-iot)
6. [Q6 — Encapsulamento e Tell, Don't Ask (conta bancária)](#q6--encapsulamento-e-tell-dont-ask-conta-bancária)
7. [Q7 — Verificação rápida: classe, objeto, contrato, sobrecarga e igualdade](#q7--verificação-rápida-classe-objeto-contrato-sobrecarga-e-igualdade)
8. [Q8 — Atividade 1: diagnóstico de conceitos](#q8--atividade-1-diagnóstico-de-conceitos)
9. [Q9 — Atividade 2: refatoração por composição](#q9--atividade-2-refatoração-por-composição)
10. [Q10 — Atividade 3: validação de diagrama UML](#q10--atividade-3-validação-de-diagrama-uml)
11. [Apêndice — Outros itens do material e observações](#apêndice--outros-itens-do-material-e-observações)

---

## Q1 — Polimorfismo, vinculação dinâmica e field shadowing
**Fonte:** `Apresentação Orientacao a Objetos.pdf`, p. 3 (enunciado), p. 4 (cenário/código), p. 5 (alternativas), p. 6 (gabarito comentado), p. 7 (conceito consolidado)
**Tipo ENADE:** Resposta única (interpretação de código + avaliação de projeto)

**Enunciado:**

QUESTÃO 1 · QUESTÃO AUTORAL NO ESTILO ENADE

CONTEXTUALIZAÇÃO
A implementação de regras de negócio em sistemas orientados a objetos frequentemente se vale do padrão comportamental Template Method, que define o esqueleto de um algoritmo na superclasse e delega etapas específicas para as subclasses. A forma como os atributos e métodos interagem nesse cenário exige compreensão rigorosa sobre escopo, encapsulamento e vinculação (binding).

COMANDO
Considerando os princípios de polimorfismo, vinculação dinâmica (dynamic binding) e boas práticas de encapsulamento, avalie o comportamento do código executado na classe SistemaPrincipal e a qualidade arquitetural da decisão de implementação adotada na relação de herança. Assinale a alternativa tecnicamente adequada:

QUESTÃO 1 · CENÁRIO: **Qual o valor impresso por p.processar(100.0)?**

```java
public abstract class ProcessadorDeRegra {
    protected double fatorMultiplicador = 1.5;

    public double processar(double valorBase) {
        return (valorBase * fatorMultiplicador) + calcularTaxaExtra();
    }

    protected double calcularTaxaExtra() {
        return 10.0;
    }
}

public class ProcessadorComplexo extends ProcessadorDeRegra {
    protected double fatorMultiplicador = 2.0;

    @Override
    protected double calcularTaxaExtra() {
        return 25.0;
    }
}

public class SistemaPrincipal {
    public static void main(String[] args) {
        ProcessadorDeRegra p = new ProcessadorComplexo();
        System.out.println(p.processar(100.0));
    }
}
```

Qual alternativa é tecnicamente adequada?

**Alternativas:**
- **A)** A saída será 225.0, pois a vinculação dinâmica seria aplicada tanto ao método calcularTaxaExtra() (25.0) quanto ao atributo fatorMultiplicador (2.0) da subclasse. O projeto teria alta coesão, pois delega às subclasses a gestão de seus próprios estados e comportamentos.
- **B)** A saída será 160.0, pois a tipagem da referência p forçaria vinculação estática para TODOS os membros e métodos de ProcessadorDeRegra. O projeto seria excelente em segurança e manutenibilidade, blindando o método principal contra alterações das subclasses.
- **C)** A saída será 225.0, pois a subclasse redefiniria a alocação de memória do atributo fatorMultiplicador para 2.0. O projeto aumentaria indevidamente o acoplamento, pois obrigaria a classe base a conhecer e invocar estados modificados pelas subclasses.
- **D)** A saída será 175.0, pois fatorMultiplicador (1.5) sofre vinculação estática pela classe base, enquanto calcularTaxaExtra() (25.0) sofre vinculação dinâmica. O projeto é inadequado: o shadowing quebra o encapsulamento; o estado deveria ser configurado via construtores, não recriado nas subclasses.

**Gabarito: D** — _(origem: gabarito do próprio material, p. 6; conferido executando o código em Java 21: saída `175.0`)_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Supõe que atributos são polimórficos como os métodos. Daí o cálculo errado (100 × 2.0) + 25 = 225.0. Também trata o shadowing como boa prática de coesão, e ele é uma falha de projeto.
- **B) ❌** — Ignora a sobrescrita (`@Override`) de `calcularTaxaExtra()` e supõe vinculação estática também para métodos: (100 × 1.5) + 10 = 160.0. O tipo declarado da referência não impede o despacho dinâmico de métodos de instância. Além disso, a alternativa trata a ausência de polimorfismo como vantagem de segurança.
- **C) ❌** — Chega ao mesmo valor errado de A (225.0) e erra ao falar em "redefinir a alocação de memória do atributo". Nada é realocado: o objeto `ProcessadorComplexo` passa a ter **dois** campos, `ProcessadorDeRegra.fatorMultiplicador = 1.5` e `ProcessadorComplexo.fatorMultiplicador = 2.0`, e o novo campo apenas **oculta** o da superclasse.
- **D) ✅** — `processar()` está definido na superclasse. Dentro dele, `fatorMultiplicador` significa `this.fatorMultiplicador`, e nesse ponto `this` tem tipo estático `ProcessadorDeRegra`. Campos são resolvidos em compilação pelo tipo estático, então o valor lido é **1.5**. Já `calcularTaxaExtra()` é método de instância sobrescrito: o despacho é dinâmico pelo tipo real do objeto (`ProcessadorComplexo`), então o valor é **25.0**. Cálculo: **(100 × 1.5) + 25 = 175.0**. No plano arquitetural, o field shadowing cria dois estados "fatorMultiplicador" distintos no mesmo objeto. A correção é inicializar o valor herdado via construtor (ex.: `super(2.0)`) ou expor um método polimórfico `getFator()` (justificativa do material, p. 6).

**⚠️ Atenção:** O gabarito está correto. Um detalhe pode ser explorado numa versão alterada: o slide p. 7 diz que "o tipo DECLARADO da referência decide qual campo é acessado". Aqui o que conta é o tipo estático **no ponto em que o campo é lido**, ou seja, dentro de `processar()` da superclasse, e não o tipo declarado de `p`. Variações testadas em Java 21:

| Variação do código | Saída |
|---|---|
| Original | **175.0** |
| `ProcessadorComplexo p = new ProcessadorComplexo();` (referência do tipo da subclasse) | **175.0** (continua igual, porque o campo é lido dentro do código da superclasse) |
| Em `main`: `p.fatorMultiplicador` com `p` declarado como `ProcessadorDeRegra` / como `ProcessadorComplexo` | 1.5 / 2.0 |
| Subclasse **não** redeclara o campo e atribui `fatorMultiplicador = 2.0` no construtor (ou `super(2.0)`) | **225.0** |
| Subclasse também sobrescreve `processar()` com o mesmo corpo | 225.0 |
| Base usa `getFator()` e a subclasse sobrescreve `getFator()` retornando 2.0 | 225.0 |
| `calcularTaxaExtra()` `private` na base, ou `static` nas duas classes (sem override real) | 160.0 |

**Conceito-chave para a prova:** atributo usa vinculação estática (tipo estático, em compilação). Método de instância sobrescrito usa vinculação dinâmica (classe real do objeto, em execução). Métodos `static` e `private` não são despachados dinamicamente. Redeclarar o campo na subclasse (shadowing) não altera o campo lido pela superclasse.

---

## Q2 — Herança x composição (sensor IoT)
**Fonte:** `Apresentação Orientacao a Objetos.pdf`, p. 8 (enunciado), p. 9 (cenário/código), p. 10 (alternativas), p. 11 (gabarito comentado), p. 12 (conceito consolidado). Base teórica na apostila, p. 12–13 (§4.2.1 e §4.2.4, "Quando preferir composição").
**Tipo ENADE:** Resposta única (análise de projeto)

**Enunciado:**

QUESTÃO 2 · QUESTÃO AUTORAL NO ESTILO ENADE

CONTEXTUALIZAÇÃO
Um arquiteto de software está revisando o código desenvolvido por um programador júnior para o módulo de controle de um sistema de Internet das Coisas (IoT) voltado para automação industrial. O sistema precisa lidar com diversos sensores que coletam dados e, quando necessário, emitem alertas de segurança enviando dados através da rede. O programador propôs a estrutura apresentada a seguir para resolver a necessidade de comunicação de rede e o comportamento de atuação do sensor de temperatura.

COMANDO
Avaliando a estrutura de herança e implementação apresentada no código, e considerando os impactos dessa decisão sobre o acoplamento, coesão, extensibilidade e a semântica estrutural da orientação a objetos, qual alternativa apresenta a análise técnica mais adequada?

QUESTÃO 2 · CENÁRIO: **A herança de ComunicadorRede é uma boa decisão de projeto?**

```java
public class ComunicadorRede {
    public void estabelecerConexao(String ip) {
        // Lógica de infraestrutura para handshake e conexão TCP/IP
    }
    public void enviarPacote(byte[] dados) {
        // Lógica genérica de roteamento e envio de pacotes na rede
    }
}

public interface DispositivoAtuador {
    void acionarAlerta(String mensagem);
}

// Modelagem proposta pelo desenvolvedor
public class SensorTemperaturaSmart extends ComunicadorRede
        implements DispositivoAtuador {
    private double temperaturaAtual;

    public void medirTemperatura() {
        // Lógica de hardware que atualiza temperaturaAtual
    }

    @Override
    public void acionarAlerta(String mensagem) {
        if (this.temperaturaAtual > 40.0) {
            enviarPacote(mensagem.getBytes()); // reaproveita método herdado
        }
    }
}
```

Qual alternativa é tecnicamente adequada?

**Alternativas:**
- **A)** A implementação da interface está incorreta, pois interfaces em Java serviriam para simular herança múltipla de ESTADO; a ação de alerta deveria migrar para uma superclasse abstrata para herdar atributos.
- **B)** A herança simples atende ao princípio de especialização, tornando o sensor um subtipo de comunicador. A falha estaria no uso da interface, que impediria o reaproveitamento do código do método de acionamento.
- **C)** A herança de ComunicadorRede é inadequada por não representar uma relação semântica "é-um" adequada, expondo métodos de infraestrutura ao domínio do sensor e podendo quebrar a substituibilidade esperada. O reaproveitamento de código de rede deveria ocorrer por composição.
- **D)** A modelagem é correta e eficiente, pois a herança garante reaproveitamento nativo do envio de dados, evitando duplicação de código e compensando a falta de herança múltipla na linguagem.

**Gabarito: C** — _(origem: gabarito do próprio material, p. 11)_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Erro conceitual grave: interfaces **não** armazenam estado de instância. Os campos de uma interface são constantes `public static final`, então interfaces não servem para "simular herança múltipla de estado". O uso da interface `DispositivoAtuador` no cenário está correto.
- **B) ❌** — Aceita a premissa falsa de "especialização" entre sensor e comunicador e culpa a interface por não reaproveitar código, papel que nunca foi dela. A interface define um contrato.
- **C) ✅** — `SensorTemperaturaSmart` não **é um** `ComunicadorRede`. Ele **usa** capacidades de rede para enviar alertas. Herdar só para reaproveitar `enviarPacote()` expõe `estabelecerConexao()`/`enviarPacote()` a qualquer cliente do sensor e pode violar a substituibilidade (LSP). A correção é a composição: o sensor deve ter um atributo privado do tipo `ComunicadorRede` (ou, melhor, uma interface de canal de comunicação injetada) e delegar a ele. A interface `DispositivoAtuador` está correta: define um contrato de comportamento sem acoplar implementação.
- **D) ❌** — Supõe que o propósito da herança é evitar duplicação de código a qualquer custo. Ignora o acoplamento rígido resultante, que engessa a evolução (ex.: adicionar Bluetooth quebraria a herança). Também está errado dizer que herdar "compensa" a falta de herança múltipla: Java já tem herança múltipla de tipo por interfaces.

**Conceito-chave para a prova:** herança modela "é-um" (subtipo substituível, LSP). Composição modela "tem-um"/"usa". Nunca herde apenas para reaproveitar código: "prefira composição à herança" (Effective Java, item 18, 3ª ed.; GoF). Interface = contrato sem estado de instância.

---

## Q3 — UML: multiplicidades e composição (clínica veterinária)
**Fonte:** `Apresentação Orientacao a Objetos.pdf`, p. 13 (enunciado), p. 14 (cenário/regras), p. 15 (diagrama correto), p. 16 (alternativas), p. 17 (gabarito comentado), p. 18 (conceito consolidado). Base teórica na apostila, p. 14–16 (§5.1.2 "Como ler multiplicidade" e §5.2 "Associação, agregação e composição").
**Tipo ENADE:** Resposta única (tradução de regras de negócio para UML / associação)

**Enunciado:**

QUESTÃO 3 · QUESTÃO AUTORAL NO ESTILO ENADE

CONTEXTUALIZAÇÃO
A correta tradução de regras de negócio para a estrutura estática de um software é uma etapa crítica na engenharia de requisitos e no projeto orientado a objetos, garantindo que o sistema imponha as restrições de integridade do domínio antes mesmo da implementação do código-fonte.

COMANDO
Considerando a correspondência rigorosa entre o modelo UML e as regras de negócio apresentadas, analise os relacionamentos e avalie qual alternativa traduz corretamente as associações, papéis e multiplicidades para o Diagrama de Classes:

QUESTÃO 3 · CENÁRIO: **Traduzindo regras de negócio em relacionamentos UML**

| Relação | Regra de negócio |
|---|---|
| **Veterinário ↔ Atendimento** | Um Veterinário pode realizar diversos Atendimentos ao longo do mês, mas também pode não ter realizado nenhum. Cada Atendimento é de responsabilidade de exatamente um Veterinário. |
| **Tutor ↔ Animal** | Um Animal deve possuir um e apenas um Tutor legal vinculado. Para existir no sistema, um Tutor precisa ter sob sua responsabilidade um ou mais Animais. |
| **Atendimento ↔ Receituário** | Ao final do Atendimento, o sistema pode gerar no máximo um Receituário. Um Receituário tem pertencimento estrutural e ciclo de vida associado ao Atendimento que o gerou. |

Qual alternativa traduz corretamente as multiplicidades?

**Alternativas:**
- **A)** Tutor-Animal: [1..*] em ambos os lados (muitos-para-muitos). Veterinário-Atendimento: [0..*] no lado do Atendimento. Atendimento-Receituário: Herança, com Receituário especializando Atendimento.
- **B)** Tutor-Animal: [1] no Tutor e [1..*] no Animal. Veterinário-Atendimento: [1] no Veterinário e [0..*] no Atendimento. Atendimento-Receituário: Composição (losango no Atendimento [1]), multiplicidade [0..1] no Receituário.
- **C)** Tutor-Animal: [1..*] no Tutor e [1] no Animal. Veterinário-Atendimento: [0..*] no Veterinário e [1] no Atendimento. Atendimento-Receituário: Agregação (losango vazio no Receituário [0..1]).
- **D)** Tutor-Animal: [1] no Tutor e [0..*] no Animal. Veterinário-Atendimento: [1..*] apontando para Atendimento. Atendimento-Receituário: Associação simples, multiplicidade [1..*] em Receituário.

**Gabarito: B** — _(origem: gabarito do próprio material, p. 17; diagrama correspondente na p. 15)_

[Figura do slide p. 15, "Diagrama de Classes Correto": (1) `Tutor` —— `Animal` (associação simples), com **1** junto a Tutor e **1..*** junto a Animal. (2) `Veterinário` —— `Atendimento` (associação simples, vertical), com **1** junto a Veterinário e **0..*** junto a Atendimento. (3) `Atendimento` ◆—— `Receituário`: losango **preenchido** encostado em Atendimento (composição), com **1** junto a Atendimento e **0..1** junto a Receituário. Legenda: "Losango preenchido = composição: o Receituário tem ciclo de vida associado ao Atendimento". "Leitura explícita: cada Animal → 1 Tutor; cada Tutor → 1..* Animais; cada Atendimento → 1 Veterinário; cada Veterinário → 0..* Atendimentos; cada Atendimento → 0..1 Receituário".]

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Propõe muitos-para-muitos entre Tutor e Animal, o que ignora "um e apenas um Tutor". Modela Receituário como **herança** de Atendimento, mas um receituário não "é um" atendimento: ele é **gerado** por um atendimento. (O trecho "[0..*] no lado do Atendimento" está certo, mas o resto invalida a alternativa.)
- **B) ✅** — Tutor (1) — Animal (1..*): cada animal tem exatamente um tutor e cada tutor tem um ou mais animais. Veterinário (1) — Atendimento (0..*): cada atendimento pertence a exatamente um veterinário e um veterinário pode ter zero ou muitos atendimentos. Atendimento–Receituário: **composição** (losango preenchido no lado do todo, Atendimento, com multiplicidade 1), porque o receituário tem pertencimento estrutural e ciclo de vida ligado ao atendimento. Multiplicidade **0..1** no Receituário, que é opcional e único.
- **C) ❌** — Inverte a leitura das multiplicidades: põe 1..* no Tutor e 1 no Animal, 0..* no Veterinário e 1 no Atendimento. Também confunde composição com **agregação** (losango vazio) e coloca o losango na classe **parte** (Receituário) em vez do **todo**.
- **D) ❌** — Usa 0..* no Animal, o que fere "um ou mais Animais". Usa 1..* para Atendimento, o que fere "pode não ter realizado nenhum" (este erro o slide não cita). Troca a composição por associação simples com 1..* no Receituário, tornando o receituário obrigatório e múltiplo, o oposto de "no máximo um".

**⚠️ Atenção:**
1. Nos slides, o diagrama com a resposta (p. 15) aparece **antes** das alternativas (p. 16). Na prova, a questão deve vir sem o diagrama.
2. A multiplicidade se lê **a partir de uma instância do lado oposto**: o número junto a Animal (1..*) diz quantos animais cada tutor tem. Alternativas que "invertem os lados" (como C) são a pegadinha principal.
3. Há uma diferença de rigor entre os materiais. O slide p. 18 afirma que, na agregação, "a parte pode existir independentemente do conjunto". A apostila (p. 16, §5.2.2) ressalva que a UML 2.5.1 **não** atribui semântica operacional universal à agregação compartilhada e que o losango vazio deve ser usado com cautela. Para a prova vale a leitura usual: agregação = losango vazio, todo–parte fraco; composição = losango preenchido no todo, parte exclusiva e com ciclo de vida dependente.

**Conceito-chave para a prova:** composição = losango **preenchido** no lado do **todo**. A parte pertence a no máximo um todo, então a multiplicidade no todo é 1 ou 0..1. Agregação = losango vazio. Herança só para "é-um". Notações: 1 = exatamente um; 0..1 = opcional; 0..* (ou *) = zero ou muitos; 1..* = um ou muitos.

---

## Q4 — Padrão Strategy e OCP (cálculo de frete)
**Fonte:** `Apresentação Orientacao a Objetos.pdf`, p. 19 (enunciado), p. 20 (cenário/código), p. 21 (alternativas), p. 22 (gabarito comentado), p. 23 (conceito consolidado). Na apostila, a ideia aparece em "Integração 1 — Carrinho, composição e Strategy" (p. 20–21, interface `Desconto`). Observer e Singleton, usados aqui como distratores, estão na apostila p. 16–20 (§6.1).
**Tipo ENADE:** Resposta única (escolha de padrão de projeto)

**Enunciado:**

QUESTÃO 4 · QUESTÃO AUTORAL NO ESTILO ENADE

CONTEXTUALIZAÇÃO
A manutenção de sistemas legados frequentemente revela problemas arquiteturais decorrentes do crescimento orgânico do software. Decisões de projeto inadequadas podem levar a altos níveis de acoplamento e violações de princípios basilares da orientação a objetos, dificultando a extensibilidade.

COMANDO
Considerando a necessidade de reduzir o acoplamento, aumentar a coesão e permitir a introdução de novas modalidades sem modificar o código existente da classe CalculadoraFrete, qual padrão de projeto e respectiva estratégia de implementação resolvem arquiteturalmente o problema apresentado?

QUESTÃO 4 · CENÁRIO: **Como extensibilizar o cálculo de frete sem alterar a classe atual?**

_Contexto: a equipe precisa adicionar 4 novas modalidades de entrega (ex.: "Retirada na Loja", "Frete Internacional"). A cada nova regra, CalculadoraFrete precisa ser modificada — gerando conflitos de versão e risco de bugs em lógicas que já funcionavam._

```java
public class CalculadoraFrete {

    public double calcular(Pedido pedido, String modalidade) {
        if (modalidade.equals("PAC")) {
            // Lógica complexa de 15 linhas envolvendo dimensões e peso
            return pedido.getPeso() * 1.2;
        } else if (modalidade.equals("SEDEX")) {
            // Lógica complexa de 20 linhas com taxas de urgência
            return (pedido.getPeso() * 2.5) + 15.0;
        } else if (modalidade.equals("TRANSPORTADORA_X")) {
            // Lógica complexa de 30 linhas com pedágio e cubagem
            return (pedido.getVolume() * 1.5) + 50.0;
        }
        throw new IllegalArgumentException("Modalidade inválida");
    }
}
```

Qual padrão resolve arquiteturalmente o problema?

**Alternativas:**
- **A)** Aplicar o padrão Strategy, encapsulando cada lógica de cálculo em classes concretas distintas que implementam uma interface comum. A calculadora recebe o comportamento por composição, eliminando condicionais e respeitando o OCP.
- **B)** Aplicar o padrão Factory Method, criando uma superclasse abstrata de calculadora que delega a instanciação dos cálculos às subclasses, mantendo as condicionais centralizadas em um método criacional unificado.
- **C)** Aplicar o padrão Observer, transformando a calculadora em um Subject que emite eventos para as transportadoras (Observers), descentralizando o cálculo e permitindo adicionar modais dinamicamente.
- **D)** Aplicar o padrão Singleton na classe de cálculo, garantindo estado global compartilhado entre módulos, evitando recriação de objetos e concentrando toda a variação algorítmica em uma instância única.

**Gabarito: A** — _(origem: gabarito do próprio material, p. 22)_

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — O problema é a **variação de algoritmos** (regras de frete) concentrada numa única classe com `if/else if`, o que viola o Princípio Aberto/Fechado (aberto para extensão, fechado para modificação). O Strategy cria uma interface comum (ex.: `EstrategiaFrete { double calcular(Pedido p); }`) e classes concretas (`CalculoPac`, `CalculoSedex`, `CalculoTransportadoraX`...). A `CalculadoraFrete` passa a depender só da interface e recebe a estratégia por composição/injeção. Cada regra fica isolada na sua classe (alta coesão), e uma nova modalidade = nova classe, sem tocar no código existente.
- **B) ❌** — Factory Method é **criacional**: decide quem instancia o objeto. O problema real é encapsular **comportamentos/algoritmos** intercambiáveis. A própria alternativa admite que "as condicionais permaneceriam centralizadas".
- **C) ❌** — Observer serve para **notificação um-para-muitos** de mudanças/eventos a observadores inscritos. O problema pede um único algoritmo síncrono que devolve um valor de cálculo.
- **D) ❌** — Singleton é **criacional** e garante instância única num escopo. Não elimina condicionais, não melhora a coesão e ainda introduz estado global, prática questionável (a apostila, p. 19, lista o custo: dependências ocultas e testes difíceis).

**⚠️ Atenção:** o gabarito está correto. Uma nuance: a alternativa A diz "eliminando condicionais". O slide p. 23 é mais preciso: o Strategy tira as condicionais **do algoritmo principal/contexto**. A escolha de qual estratégia usar ainda acontece em algum lugar (na composição da aplicação, num `Map<String, EstrategiaFrete>` ou por injeção). Uma versão alterada que diga "elimina toda e qualquer decisão do sistema" seria exagerada.

**Conceito-chave para a prova:** `else if` que cresce a cada nova regra = sinal de **Strategy** (comportamental, algoritmos intercambiáveis via interface + composição) e de violação do **OCP**. Os outros: Factory Method = quem cria (criacional); Observer = notificação 1-N (comportamental); Singleton = instância única (criacional); Mediator = coordenação centralizada entre colegas (comportamental).

---

## Q5 — Classe abstrata x interface (dispositivos IoT)
**Fonte:** `Apresentação Orientacao a Objetos.pdf`, p. 24 (enunciado), p. 25 (cenário/código e requisitos), p. 26 (alternativas), p. 27 (gabarito comentado), p. 28 (conceito consolidado). Base teórica na apostila, p. 9–10 (§3.2, tabela "Classe abstrata x Interface") e p. 13 (§4.2.3, `Exportavel, Auditavel`).
**Tipo ENADE:** Resposta única (decisão de modelagem)

**Enunciado:**

QUESTÃO 5 · QUESTÃO AUTORAL NO ESTILO ENADE

CONTEXTUALIZAÇÃO
A arquitetura de sistemas orientados a objetos frequentemente exige a definição precisa de fronteiras contratuais e pontos de compartilhamento de código. A escolha inadequada entre mecanismos de abstração pode resultar em forte acoplamento, duplicação de lógica ou engessamento da evolução do software.

COMANDO
Considerando os requisitos de compartilhamento de estado, multiplicidade de comportamentos e a necessidade de classes de diferentes hierarquias cumprirem os mesmos contratos de forma desacoplada, avalie as alternativas de modelagem estrutural em Java e assinale a decisão de projeto tecnicamente mais adequada:

QUESTÃO 5 · CENÁRIO: **Como modelar comportamentos que cruzam hierarquias diferentes?**

```java
public abstract class DispositivoBase {
    protected String idRegistro;
    protected String enderecoRede;

    public void conectarBase() {
        // Lógica padronizada de handshake
        // e autenticação na rede
    }

    public abstract void iniciarOperacao();
}
```

NOVOS REQUISITOS
- TermostatoSmart: dispositivo padrão da rede, mas também precisa ser Controlavel (ligar/desligar remotamente) e Auditavel (registrar logs).
- CameraSeguranca: dispositivo da rede, deve ser Auditavel e TransmissorVideo.
- Auditavel também deve ser adotado por ServidorNuvem e GatewayDePagamento — módulos SEM nenhuma relação com dispositivos físicos.

_Desafio: como compartilhar estado (idRegistro, enderecoRede) e, ao mesmo tempo, permitir múltiplos comportamentos cruzando hierarquias distintas?_

Qual decisão de projeto é tecnicamente mais adequada?

**Alternativas:**
- **A)** Converter todos os elementos, incluindo DispositivoBase, em interfaces, exigindo que cada dispositivo concreto implemente do zero sua lógica de conexão e declare seus próprios atributos de registro.
- **B)** Definir Controlavel e Auditavel como classes abstratas (especializações do domínio) e refatorar DispositivoBase como interface, aproveitando a suposta capacidade de interfaces armazenarem estado mutável.
- **C)** Manter DispositivoBase como classe abstrata (reúso de estado e conexão). Modelar Controlavel e Auditavel como interfaces, permitindo múltiplos contratos no TermostatoSmart e que ServidorNuvem assuma esses comportamentos sem acoplamento indevido.
- **D)** Transformar Controlavel e Auditavel em classes abstratas. Como Java não suporta herança múltipla, organizar em hierarquia vertical: TermostatoSmart herda de Controlavel, que herda de Auditavel, que deriva de DispositivoBase.

**Gabarito: C** — _(origem: gabarito do próprio material, p. 27)_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Transformar tudo em interface, inclusive `DispositivoBase`, obriga a duplicar os atributos e a lógica de `conectarBase()` em cada dispositivo concreto, violando o DRY (Don't Repeat Yourself). Métodos `default` não resolvem: interface não guarda `idRegistro`/`enderecoRede` por instância.
- **B) ❌** — Erro técnico grave: interfaces **não** podem armazenar estado de instância mutável em Java, só constantes `public static final`. Tornar `DispositivoBase` interface inviabiliza `idRegistro` e `enderecoRede`. Além disso, com `Controlavel`/`Auditavel` como classes abstratas, `TermostatoSmart` não poderia estender as duas.
- **C) ✅** — `DispositivoBase` continua classe abstrata e compartilha **estado** (`idRegistro`, `enderecoRede`) e **comportamento concreto** (`conectarBase()`) na hierarquia "é-um" dos dispositivos IoT. `Controlavel` e `Auditavel` (e também `TransmissorVideo`) viram **interfaces**, porque são capacidades transversais ("pode-fazer"). Assim, `TermostatoSmart extends DispositivoBase implements Controlavel, Auditavel`, e `ServidorNuvem`/`GatewayDePagamento` podem implementar `Auditavel` sem herdar características de dispositivo físico.
- **D) ❌** — Cria uma hierarquia linear artificial para contornar a falta de herança múltipla de classes. Isso fere a semântica OO (um Controlavel não "é um" Auditavel) e impede `ServidorNuvem` de ser `Auditavel` sem virar também um `DispositivoBase`.

**⚠️ Atenção:** gabarito correto. Pequena imprecisão de redação em C: "que ServidorNuvem assuma **esses** comportamentos". Pelos requisitos, ServidorNuvem só precisa de `Auditavel`. Não muda a resposta.

**Conceito-chave para a prova:** estado compartilhado + hierarquia natural ("é-um") → **classe abstrata** (Java: só uma superclasse direta). Capacidade que atravessa hierarquias não relacionadas → **interface** (uma classe pode implementar várias). Interface em Java tem métodos abstratos, `default`, `static` e `private`, mas não tem estado de instância, só constantes `public static final`.

---

## Q6 — Encapsulamento e Tell, Don't Ask (conta bancária)
**Fonte:** `Apresentação Orientacao a Objetos.pdf`, p. 29 (enunciado), p. 30 (cenário/código), p. 31 (alternativas), p. 32 (gabarito comentado), p. 33 (conceito consolidado). Base teórica na apostila, p. 7–8 (§3.1.2, `Conta` com `depositar`/`sacar` e invariante `saldoCentavos >= 0`) e p. 11–12 (§4.1, "Encapsular não é apenas esconder campos" e o quadro "Erro recorrente").
**Tipo ENADE:** Resposta única (avaliação de projeto)

**Enunciado:**

QUESTÃO 6 · QUESTÃO AUTORAL NO ESTILO ENADE

CONTEXTUALIZAÇÃO
O encapsulamento é um princípio fundamental da programação orientada a objetos que vai além da simples aplicação de modificadores de visibilidade para ocultar atributos. Seu objetivo central é garantir que um objeto tenha controle exclusivo sobre seu estado interno, protegendo suas invariantes e concentrando os comportamentos que alteram esse estado. A aplicação inadequada desse princípio pode levar à criação de modelos de domínio anêmicos, nos quais os objetos atuam como meros repositórios de dados expostos, aumentando drasticamente o acoplamento estrutural e dificultando a manutenção do sistema.

COMANDO
Considerando os princípios de orientação a objetos, a preservação do estado interno das entidades e a necessidade de reduzir o acoplamento entre as classes, avalie a implementação apresentada e assinale a alternativa que descreve a decisão de projeto mais adequada para aplicar o encapsulamento neste cenário:

QUESTÃO 6 · CENÁRIO: **O encapsulamento está corretamente aplicado neste sistema bancário?**

```java
public class Conta {
    private double saldo;
    private double limiteChequeEspecial;

    public Conta(double saldo, double limiteChequeEspecial) {
        this.saldo = saldo;
        this.limiteChequeEspecial = limiteChequeEspecial;
    }
    public double getSaldo() { return saldo; }
    public void setSaldo(double saldo) { this.saldo = saldo; }
    public double getLimiteChequeEspecial() { return limiteChequeEspecial; }
}

public class ServicoTransferencia {
    public boolean transferir(Conta origem, Conta destino, double valor) {
        if (origem.getSaldo() + origem.getLimiteChequeEspecial() >= valor) {
            origem.setSaldo(origem.getSaldo() - valor);
            destino.setSaldo(destino.getSaldo() + valor);
            return true;
        }
        return false;
    }
}
```

Qual decisão aplica corretamente o encapsulamento?

**Alternativas:**
- **A)** O encapsulamento já está correto: os atributos são private, impedindo acesso direto. Getters e setters transferem adequadamente a lógica de alteração de estado ao serviço externo, favorecendo a coesão.
- **B)** A visibilidade deve ser flexibilizada para protected, permitindo que ServicoTransferencia acesse as propriedades sem intermediários, centralizando as regras de negócio no mesmo pacote.
- **C)** O estado interno deveria ser imutável, evitando efeitos colaterais. O encapsulamento ideal seria remover os setters e exigir que o serviço recrie instâncias de Conta com os valores consolidados a cada transação.
- **D)** A classe deve concentrar a responsabilidade sobre suas invariantes: remover o setSaldo e criar operações como sacar(valor) e depositar(valor) dentro de Conta. Isso protege o estado interno e reduz o acoplamento com o serviço.

**Gabarito: D** — _(origem: gabarito do próprio material, p. 32)_

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Confunde "atributos `private` + getters/setters públicos" com bom encapsulamento. Com `setSaldo` público, qualquer cliente põe o saldo em qualquer valor sem validação. É o sintoma clássico do **Modelo de Domínio Anêmico** (Fowler): a regra de negócio fica no serviço e a entidade vira um contêiner de dados.
- **B) ❌** — Ampliar a visibilidade para `protected` só piora: em Java, `protected` dá acesso ao pacote inteiro **e** às subclasses. O estado interno fica mais exposto em vez de concentrado na própria classe.
- **C) ❌** — Confunde encapsulamento com imutabilidade estrita. `Conta` é uma entidade com ciclo de vida e estado que muda legitimamente. O que importa é a mudança ser validada e executada pela própria classe. Recriar a conta a cada transação não faz sentido semântico.
- **D) ✅** — Remove o `setSaldo` público e cria `sacar(valor)`/`depositar(valor)` **dentro** de `Conta`. A conta passa a proteger sua invariante (saldo não pode ficar abaixo de −limite do cheque especial) e a validar pré-condições (valor > 0). O `ServicoTransferencia` só pede à conta que execute a operação ("Tell, Don't Ask": `origem.sacar(valor); destino.depositar(valor);`) e deixa de conhecer os detalhes do cálculo, o que reduz o acoplamento.

**⚠️ Atenção:** gabarito correto. Um teste executado com o código do cenário mostra mais falhas que o design atual permite: `transferir(origem, destino, -1000)` retorna `true` e **aumenta** o saldo da origem (valor negativo não é validado), e `setSaldo(-999999)` é aceito sem checagem. Isso reforça a alternativa D. Detalhe extra (não cobrado na questão): a apostila (p. 8) usa `long` em centavos em vez de `double` para evitar erros de arredondamento com dinheiro.

**Conceito-chave para a prova:** encapsulamento ≠ "private + getters/setters". É o objeto controlar as próprias transições de estado e preservar suas invariantes. Tell, Don't Ask: `conta.sacar(valor)` em vez de `conta.setSaldo(conta.getSaldo() - valor)`. Encapsulamento ≠ imutabilidade. `protected` amplia o acesso, não restringe.

---

## Q7 — Verificação rápida: classe, objeto, contrato, sobrecarga e igualdade
**Fonte:** `Material sobre Orientação a Objetos.pdf`, p. 9 (pág. impressa 6), §3.1.6 "Verificação rápida". Refere-se ao exemplo `Conta` das p. 7–8 (§3.1.2) e ao §3.1.3 (p. 8).
**Tipo ENADE:** Discursiva (perguntas de revisão, sem gabarito no material)

**Enunciado:**
3.1.6 Verificação rápida
- Explique por que classe e objeto não são sinônimos.
- Indique pré-condição, pós-condição e invariante no exemplo Conta.
- Diga por que um retorno diferente não torna duas declarações uma sobrecarga válida.
- Explique a diferença entre identidade (==) e igualdade lógica (equals).

Exemplo `Conta` a que o item 2 se refere (apostila, p. 7–8):
```java
public final class Conta {
    private final String id;
    private long saldoCentavos;

    public Conta(String id, long saldoInicialCentavos) {
        if (id == null || id.isBlank())
            throw new IllegalArgumentException("id obrigatório");
        if (saldoInicialCentavos < 0)
            throw new IllegalArgumentException("saldo inicial negativo");
        this.id = id;
        this.saldoCentavos = saldoInicialCentavos;
    }

    public String id() { return id; }
    public long saldoCentavos() { return saldoCentavos; }

    public void depositar(long valorCentavos) {
        exigirValorPositivo(valorCentavos);
        saldoCentavos += valorCentavos;
    }

    public void sacar(long valorCentavos) {
        exigirValorPositivo(valorCentavos);
        if (valorCentavos > saldoCentavos)
            throw new IllegalStateException("saldo insuficiente");
        saldoCentavos -= valorCentavos;
    }

    private static void exigirValorPositivo(long valor) {
        if (valor <= 0)
            throw new IllegalArgumentException("valor inválido");
    }
}
```

**Resposta esperada** _(não consta no material — resolvido aqui com base no próprio texto da apostila)_:
1. **Classe x objeto:** a classe é um **tipo**, uma unidade de descrição: declara atributos, operações, construtores e regras de acesso. Estabelece o vocabulário e as restrições. O objeto é uma **instância concreta** desse tipo, com **identidade** própria, **estado** atual (valores em dado momento) e **comportamento** acessível. Uma classe pode ter muitas instâncias, e dois objetos com os mesmos valores continuam objetos distintos.
2. **Contrato da `Conta`:**
   - **Pré-condições:** construtor: `id` não nulo e não em branco, `saldoInicialCentavos >= 0`. `depositar`: `valorCentavos > 0`. `sacar`: `valorCentavos > 0` **e** `valorCentavos <= saldoCentavos`. Se forem violadas, é lançada `IllegalArgumentException`/`IllegalStateException` e o estado não muda.
   - **Pós-condições:** construtor: conta criada com `id` válido e saldo = saldo inicial. `depositar`: saldo novo = saldo anterior + valor. `sacar`: saldo novo = saldo anterior − valor.
   - **Invariante:** `saldoCentavos >= 0` sempre (também: `id` não nulo/não vazio e imutável, por ser `final`). Ela se mantém porque não há `setSaldo` irrestrito: só existem operações de domínio que verificam pré-condições.
3. **Retorno diferente não é sobrecarga:** a assinatura usada para sobrecarga é **nome + lista de tipos de parâmetros**, sem o tipo de retorno. A seleção entre sobrecargas é feita em **compilação** pelos argumentos. Duas declarações `int f(int)` e `double f(int)` têm a mesma assinatura e o compilador rejeita (testado: `error: method f(int) is already defined`). Numa chamada como `f(1);`, com o retorno descartado, não haveria como escolher.
4. **`==` x `equals`:** para referências, `==` testa **identidade** (se as duas referências apontam para o mesmo objeto). `equals` expressa **igualdade lógica** conforme o contrato definido pela classe (o padrão herdado de `Object` também compara identidade). Ex.: `new String("ok") == new String("ok")` → `false`, `.equals(...)` → `true`. Quem redefine `equals` deve redefinir `hashCode` de forma coerente para o objeto funcionar em `HashSet`/`HashMap`.

**Conceito-chave para a prova:** sobrecarga = mesmo nome, parâmetros diferentes, resolvida em compilação, retorno não conta. Sobrescrita = mesma assinatura na subclasse, resolvida em execução. `==` = identidade. `equals` = igualdade lógica, sempre junto com `hashCode`.

---

## Q8 — Atividade 1: diagnóstico de conceitos
**Fonte:** `Material sobre Orientação a Objetos.pdf`, p. 22–23 (págs. impressas 19–20), §8.1 "Atividade 1 — Diagnóstico de conceitos"
**Tipo ENADE:** Discursiva (julgamento de afirmativas: correta / incorreta / incompleta, com justificativa). Pode virar uma questão de afirmativas múltiplas na prova.

**Enunciado:**
Para cada afirmação, indique se é correta, incorreta ou incompleta e justifique:
1. "Classe e objeto são a mesma coisa em níveis diferentes."
2. "Uma interface é sempre apenas uma lista de operações abstratos."
3. "Se duas classes compartilham código, uma deve herdar da outra."
4. "1 no extremo Cliente significa que há um único cliente no sistema."
5. "Qualquer coleção de filhos é composição."
6. "Singleton é apenas uma forma elegante de escrever uma variável global."

Uma resposta forte não se limita a marcar verdadeiro ou falso. Ela apresenta o contrato, o escopo e o caso-limite que sustentam a decisão.

**Resposta esperada** _(não consta no material — resolvido aqui com base no próprio texto da apostila)_:
1. **Incorreta.** Classe é um tipo/descrição (vocabulário e restrições). Objeto é uma instância concreta com identidade, estado e comportamento (apostila p. 7). Caso-limite: dois objetos da mesma classe com valores idênticos continuam distintos (`==` falso).
2. **Incorreta.** Em Java moderno, interfaces podem declarar métodos abstratos, **`default`**, **`static`** e **`private`**, além de constantes `public static final` (apostila p. 9). O que uma interface **não** tem é estado mutável por instância. Caso-limite: duas interfaces com o mesmo método `default` obrigam a classe a resolver o conflito explicitamente (p. 13).
3. **Incorreta.** Herança só se justifica com relação de subtipagem estável ("é-um"), em que a subclasse pode substituir a base sem quebrar expectativas (Liskov). Para reaproveitar código sem subtipagem, use **composição/delegação** (p. 10 e 13). Caso-limite: sensor que herda de `ComunicadorRede` só para enviar pacotes (Q2).
4. **Incorreta.** A multiplicidade se lê **a partir de uma instância do extremo oposto**: "1 no lado de Cliente" quer dizer que **cada pedido** se relaciona com exatamente um cliente. Não diz quantos clientes existem no sistema (p. 14).
5. **Incorreta.** Ter uma coleção (List/Set) não define a semântica. Composição exige que a parte pertença a **no máximo um** composto por vez e que o composto controle seu ciclo de vida. Senão é **associação** (ex.: Item → Produto, que existe sozinho) ou **agregação** (ex.: Equipe–Jogador). Use "a menor semântica suficiente" (p. 16). Ex. válido de composição: Pedido–ItemPedido, quando o item pertence só àquele pedido.
6. **Incompleta** (tem algo de verdade). Singleton é um padrão **criacional** que controla a criação de **uma única instância num escopo definido** (construtor privado + acesso estático, ex.: Holder idiom). Só se justifica quando instâncias extras causam dano real. "Única" não vale entre JVMs, class loaders ou processos distribuídos. Mas o seu principal custo é justamente o do acesso global: dependências ocultas, estado que persiste entre testes e dificuldade de usar dublês (p. 19). Alternativa preferível: criar uma instância na composição da aplicação e **injetá-la**.

**Conceito-chave para a prova:** os seis itens são "pegadinhas clássicas". Herança ≠ reuso, multiplicidade se lê do lado oposto, coleção ≠ composição, interface moderna tem `default`/`static`/`private` mas não tem estado, e Singleton é criacional, com custo de acesso global.

---

## Q9 — Atividade 2: refatoração por composição
**Fonte:** `Material sobre Orientação a Objetos.pdf`, p. 23 (pág. impressa 20), §8.2 "Atividade 2 — Refatoração por composição"
**Tipo ENADE:** Discursiva (exercício prático de refatoração, sem gabarito no material)

**Enunciado:**
Comece com uma classe RelatorioService que instancia diretamente ExportadorCsv, LoggerGlobal e RepositorioBanco. Refatore-a para depender de interfaces e receber as implementações pelo construtor.
Compare:
- quantidade de dependências concretas;
- facilidade de fornecer dublês em testes;
- clareza das pré-condições;
- possibilidade de substituir uma implementação;
- custo adicional de interfaces e composição.

**Resposta esperada** _(não consta no material — proposta de resolução; o esboço "depois" foi compilado e executado em Java 21)_:

Antes (acoplado a classes concretas):
```java
public class RelatorioService {
    private final ExportadorCsv exportador = new ExportadorCsv();
    private final LoggerGlobal logger = LoggerGlobal.getInstance();
    private final RepositorioBanco repositorio = new RepositorioBanco();
    // ...
}
```

Depois (depende de contratos; as implementações chegam pelo construtor):
```java
interface Exportador { String exportar(Relatorio r); }
interface Logger { void info(String msg); }
interface RepositorioRelatorios { Relatorio buscar(long id); }

final class RelatorioService {
    private final Exportador exportador;
    private final Logger logger;
    private final RepositorioRelatorios repositorio;

    RelatorioService(Exportador exportador, Logger logger, RepositorioRelatorios repositorio) {
        this.exportador = java.util.Objects.requireNonNull(exportador);
        this.logger = java.util.Objects.requireNonNull(logger);
        this.repositorio = java.util.Objects.requireNonNull(repositorio);
    }

    String gerar(long id) {
        Relatorio relatorio = repositorio.buscar(id);
        logger.info("gerando relatório " + id);
        return exportador.exportar(relatorio);
    }
}
// Composição da aplicação: new RelatorioService(new ExportadorCsv(), new ConsoleLogger(), new RepositorioBanco());
```

| Critério | Antes | Depois |
|---|---|---|
| Dependências concretas no serviço | 3 (`ExportadorCsv`, `LoggerGlobal`, `RepositorioBanco`) | 0. O serviço só conhece 3 interfaces, e as classes concretas são escolhidas na composição da aplicação |
| Dublês em testes | Difícil: exige banco real, e o logger global guarda estado entre testes | Fácil: basta passar fakes/lambdas pelo construtor |
| Clareza das pré-condições | Ocultas (dependências criadas por dentro) | Explícitas no construtor (`requireNonNull`) |
| Substituir implementação | Exige editar o serviço | Trocar `ExportadorCsv` por um `ExportadorPdf` sem tocar no serviço (OCP) |
| Custo | Menos tipos | Mais interfaces/arquivos, uma indireção a mais e montagem na composição da aplicação. Interface artificial com uma só implementação pode não compensar |

**Conceito-chave para a prova:** inversão de dependência + injeção pelo construtor = baixo acoplamento e testabilidade. É o mesmo raciocínio da apostila em `ServicoDeRelatorios`/`Exportador` (p. 10) e no `Service(Logger)` como alternativa ao Singleton (p. 19–20).

---

## Q10 — Atividade 3: validação de diagrama UML
**Fonte:** `Material sobre Orientação a Objetos.pdf`, p. 23 (pág. impressa 20), §8.3 "Atividade 3 — Validação de diagrama UML". Relacionada ao §5.1.4 "Classe de associação" (p. 15) e às Integrações 2 e 4 (p. 21–22).
**Tipo ENADE:** Discursiva (modelagem UML aberta, sem gabarito no material)

**Enunciado:**
Modele uma plataforma de cursos. O modelo deve conter Aluno, Curso, Disciplina e Matricula. Inclua multiplicidades, papéis, ordem e unicidade quando forem relevantes. Crie quatro instâncias válidas e quatro inválidas. Explique quais regras precisam de OCL, restrição de banco ou código além da multiplicidade.

**Resposta esperada** _(não consta no material — proposta de resolução; outras modelagens justificadas também são aceitáveis)_:

Modelo proposto, seguindo o exemplo da apostila (p. 15: "Aluno cursa disciplina" vira `Matricula`, com semestre, nota, frequência e situação):
- `Curso` 1..* —— 1..* `Disciplina` (papel "grade curricular"). Associação simples, porque uma disciplina pode ser compartilhada entre cursos e existe sem um curso específico. Pode ser `{ordered}` por período.
- `Aluno` 0..* —— 1 `Curso` (cada aluno está vinculado a exatamente um curso; um curso pode ter zero ou muitos alunos).
- `Matricula` como **classe de associação** entre `Aluno` e `Disciplina`, com atributos `semestre`, `nota`, `frequencia`, `situacao`. Cada matrícula liga exatamente 1 aluno e 1 disciplina. Um aluno tem 0..* matrículas (`{ordered}` por semestre). Uma disciplina tem 0..* matrículas.

Instâncias:

| Instância | Estado | Válida? | Motivo |
|---|---|---|---|
| V1 | Curso c1 com disciplina d1; aluno a1 em c1; matrícula m1(a1, d1, 2026.1) | Sim | Caso mínimo completo |
| V2 | Aluno a2 em c1 sem matrículas | Sim | 0..* permite coleção vazia |
| V3 | Disciplina d2 de c1 sem matrículas no semestre | Sim | 0..* do lado de Matricula |
| V4 | a1 com m1(d1, 2026.1) reprovado e m2(d1, 2026.2) | Sim | Mesma disciplina em semestres diferentes (refazer) |
| I1 | Matrícula sem aluno | Não | O extremo Aluno exige 1 |
| I2 | Curso sem nenhuma disciplina | Não | Viola 1..* |
| I3 | a1 com duas matrículas em d1 no mesmo semestre 2026.1 | Não | Viola a unicidade composta (aluno, disciplina, semestre), **que a multiplicidade não captura** |
| I4 | a1 (curso c1) matriculado em d9, que não pertence a c1 | Não | Regra entre associações, que a multiplicidade não captura |

Regras que exigem mais que multiplicidade:
- **OCL:**
  ```
  context Aluno inv matriculaUnicaPorSemestre:
    self.matriculas->forAll(m1, m2 | m1 <> m2 implies
      not (m1.disciplina = m2.disciplina and m1.semestre = m2.semestre))
  context Matricula inv disciplinaDoCurso:
    self.aluno.curso.disciplinas->includes(self.disciplina)
  context Matricula inv notaValida:
    self.nota >= 0 and self.nota <= 10
  ```
- **Banco de dados:** `UNIQUE(aluno_id, disciplina_id, semestre)` e `CHECK (nota BETWEEN 0 AND 10)`. Chaves estrangeiras `NOT NULL` para os extremos com multiplicidade 1.
- **Código:** a criação de matrícula passa por um método (ex.: `aluno.matricular(disciplina, semestre)`) que valida as regras e não expõe a coleção interna mutável (`List.copyOf`, como na apostila p. 11).

**Conceito-chave para a prova:** multiplicidade expressa só cardinalidade mínima/máxima. Ordem (`{ordered}`), unicidade (`{unique}`), unicidade composta, regras que dependem de estado ou de tempo e restrições entre associações precisam de OCL, restrição de banco ou código (apostila p. 15, §5.1.4–5.1.5, e p. 22, Integração 4).

---

## Apêndice — Outros itens do material e observações

**Itens em forma de pergunta que não são exercícios** (registrados para não haver omissão; não foram contados como questões):
- Apostila p. 11, §4.1.3 "Checklist de encapsulamento". São 7 perguntas de revisão de projeto: (1) Qual invariante deve ser sempre verdadeira? (2) Quais operações públicas alteram o estado? (3) Cada operação verifica pré-condições e preserva pós-condições? (4) Alguma referência mutável interna é devolvida ou armazenada sem cópia? (5) `protected` é um contrato deliberado de extensão ou apenas conveniência? (6) O cliente depende de comportamento ou de uma representação concreta? (7) A imutabilidade é real ou apenas a referência é final?
- Apostila p. 5–7: colunas "Pergunta condutora" (tabela das unidades) e "Pergunta de controle" (glossário).
- Apostila p. 20 (§6.2): tabela de decisão de padrões ("Muitos objetos precisam reagir a mudanças...?" → Observer; "Componentes conhecem muitos colegas...?" → Mediator; "Deve existir uma única instância...?" → Singleton ou instância injetada; "Resolve com chamada direta ou dependência injetada?" → solução simples).
- Apostila p. 22 (§7.3): perguntas de revisão do checkout ("quem cancela inscrições? O evento ocorre antes ou depois da persistência? O mediador contém coordenação ou regra de domínio? Qual é o escopo da configuração?").
- Apostila p. 21–22 (§7.2): tabela resolvida de instâncias válidas/inválidas do modelo Pedido (p1, p2, c2 válidas; p3 sem cliente, p4 sem itens e i5 compartilhado por p5 e p6 inválidas). Pode virar questão de multiplicidade.

**Erros de edição na apostila** (não afetam as questões):
- p. 13: o código traz `.mapPendênciauble(Forma::area)`. O correto é `.mapToDouble(Forma::area)` (parece que um localizar/substituir trocou "ToDo" por "Pendência").
- Em todo o texto, "método" parece ter sido trocado por "operação", o que deixou erros de concordância ("Um operação", "operações abstratos", "operação default").

**Cobertura:** as 6 questões dos slides cobrem polimorfismo, herança x composição, UML/multiplicidade/composição, Strategy/OCP, abstrata x interface e encapsulamento. O Tópico 8 da apostila (Observer, Mediator e Singleton) só aparece como distrator em Q4. Classe de associação e sobrecarga/`equals` só aparecem nos exercícios discursivos da apostila (Q7, Q10).
