# Orientação a Objetos — Questões INFERIDAS (prováveis questões do banco do squad que não temos)

> ⚠️ **Atenção:** estas questões NÃO constam nos materiais. Foram elaboradas para cobrir os subtópicos do material do
> Squad 10 que não têm questão conhecida, imitando o estilo das questões do squad. Servem para estudo dirigido.
> As questões reais conhecidas estão em `../questoes_por_topico/04_Orientacao_a_Objetos.md`.

**Base usada:**
- `Material sobre Orientação a Objetos.pdf` (25 p., apostila "Guia ampliado alinhado à Matriz de Referência"), lida por inteiro. A apostila segue a Matriz de Referência do squad: **8 tópicos em 4 unidades** (Unidade 1: Tópicos 1–2; Unidade 2: Tópicos 3–5; Unidade 3: Tópicos 6–7; Unidade 4: Tópico 8), mais 4 exemplos integradores (§7) e 3 atividades (§8). **As páginas citadas são as do PDF.** A numeração impressa é a do PDF menos 3 (a pág. impressa 1 é a p. 4 do PDF). As figuras das p. 5, 6, 8, 15 e 17 foram renderizadas e conferidas.
- `Apresentação Orientacao a Objetos.pdf` (34 p., slides "Revisão técnica · ENADE · Computação"), lida por inteiro. Contém as 6 questões conhecidas (Q1–Q6), cada uma em 5 slides: enunciado, cenário, alternativas, gabarito comentado e "conceito consolidado".
- **Estilo identificado do squad** (Q1–Q6): título "QUESTÃO N · QUESTÃO AUTORAL NO ESTILO ENADE", blocos **CONTEXTUALIZAÇÃO** e **COMANDO**, depois um **CENÁRIO** com uma pergunta-título em negrito e quase sempre um código Java (ou tabela de regras), fechado por "Qual alternativa é tecnicamente adequada?". São sempre **4 alternativas (A–D)**, longas e de tamanho parecido, quase sempre em duas partes (resultado/diagnóstico + avaliação de projeto). Todas as 6 são de **resposta única**, com gabaritos D, C, B, A, C, D. Os distratores exploram confusões conceituais nomeadas no "gabarito comentado" (atributo polimórfico, interface com estado, herança para reúso, padrão errado, `protected` como solução). As referências citadas são Bloch (*Effective Java*), GoF, R. C. Martin, OMG UML 2.5.1, Fowler (Modelo Anêmico), Sommerville e Oracle Java Tutorials. A apostila acrescenta Liskov & Wing, Parnas, JLS SE 21 e Refactoring.Guru.
- **Tipos usados aqui:** a maioria é resposta única, igual ao squad. Para cobrir variações prováveis, há 1 questão de afirmativas múltiplas (I6), 1 de asserção-razão (I11), 1 de associação (I14) e 1 de análise de instâncias (I13), todas com 4 alternativas.
- **Todo código Java foi compilado e executado (OpenJDK 21.0.12)**, inclusive as variações citadas nas explicações: as que não compilam e as que mudam a saída.
- **Limitação importante:** o slide 2 diz que "as 6 questões integram os 8 tópicos da Matriz de Referência; alguns tópicos são avaliados conjuntamente". Isso sugere que o banco do squad pode ser só Q1–Q6. Mesmo assim, o Tópico 8 (Observer, Mediator, Singleton), a classe de associação, a igualdade (`equals`/`hashCode`), a sobrecarga e a subtipagem comportamental não têm questão objetiva própria. Por isso esses temas recebem prioridade Alta abaixo.

## Mapa de cobertura
| # | Subtópico (material) | Páginas | Questão conhecida | Questão inferida | Prioridade |
|---|---|---|---|---|---|
| 1 | T1 §3.1.1 Classe, objeto, identidade, estado e comportamento; operação como contrato; construtor não é operação chamada depois da criação (+ glossário §2.1) | Apostila p. 6–7 | Q7 e Q8 item 1 (discursivas, parcial) | I2 (agrupado com §3.1.2) | Média |
| 2 | T1 §3.1.2 Exemplo `Conta` que preserva sua invariante (pré-condição, pós-condição, invariante) | p. 7–8 | Q6 cobre só o setter e o Tell, Don't Ask. O contrato só aparece em Q7 (discursiva) | **I2** | Alta |
| 3 | T1 §3.1.3 Igualdade: `==` (identidade) x `equals` (igualdade lógica) x `hashCode` | p. 8 | Q7 item 4 (discursiva) | **I1** | Alta |
| 4 | T1 §3.1.3 Sobrecarga (o retorno não conta) e operações `static` (fora do despacho polimórfico) | p. 8 | Q7 item 3 (discursiva) | I7 (agrupado com §4.3.1) | Alta |
| 5 | T1 §3.1.4 Esquema de abstração e despacho (Fig. 3, cliente → `Forma`) | p. 8 | Q1 (despacho dinâmico) | — (variação provável: `areaTotal(List<Forma>)` sem `instanceof`) | — |
| 6 | T1 §3.1.5 Decisões de projeto (tabela: campo público/privado, instância/`static`, mutabilidade, `equals`/`hashCode`, herança/composição) | p. 8–9 | Q2 e Q6 (parcial) | Agrupado em I1 (chave mutável), I4 (mutabilidade) e I7 (`static`) | Média |
| 7 | T1 §3.1.6 Verificação rápida | p. 9 | Q7 (discursiva) | Versões objetivas em I1, I2 e I7 | — |
| 8 | T2 §3.2.1 Duas formas de abstração (tabela classe abstrata x interface) | p. 9 | **Q5** | — (variação: classe abstrata sem método abstrato é válida) | — |
| 9 | T2 §3.2.2 Depender do contrato (`Exportador`, `ServicoDeRelatorios`, esqueleto `AbstractList`) | p. 10 | Q9 (discursiva, parcial) | **I3** | Média |
| 10 | T2 §3.2.3 Critério de escolha; evolução de interface pública (método abstrato x `default`); limites do compilador | p. 10 | Q5 (só o critério) | I3 (agrupado) | Média |
| 11 | T3 §4.1.1 Encapsular não é apenas esconder campos + quadro "Erro recorrente" | p. 11–12 | **Q6** | — | — |
| 12 | T3 §4.1.2 Não vazar a representação (`Agenda`, `List.copyOf`) | p. 11 | — | **I4** | Alta |
| 13 | T3 §4.1.3 Checklist de encapsulamento (`final` ≠ imutável; `protected` por conveniência) | p. 11 | — (só listado no apêndice) | I4 (agrupado) | Média |
| 14 | T4 §4.2.1 Três sentidos de herança (tipo, implementação, estado); subclasse ≠ subtipo; Java x C++ x Python (MRO C3) | p. 12 | — | **I6** | Média |
| 15 | T4 §4.2.2 Especialização coesa (`Forma`/`Circulo`: `super(...)`, construtores não herdados, `@Override`) | p. 12–13 | Q1 (só field shadowing) | I6 (agrupado) | Média |
| 16 | T4 §4.2.3 Herança múltipla por interfaces e conflito de métodos `default` | p. 13 | Q5 (várias interfaces, sem conflito) | **I5** | Alta |
| 17 | T4 §4.2.4 Quando preferir composição | p. 13 | **Q2** | — | — |
| 18 | T5 §4.3.1 Tipo estático, classe dinâmica e despacho (tabela sobrecarga / sobrescrita / ocultação / campo / genérico) | p. 13–14 | Q1 (sobrescrita + campo) | **I7** | Alta |
| 19 | T5 §4.3.2 Subtipagem comportamental (Liskov e Wing; uso de `instanceof`) | p. 14 | Q2 cita o LSP só como justificativa | **I8** | Alta |
| 20 | T6 §5.1.1 O que um diagrama de classes modela; visibilidade `+ - # ~` | p. 14 | — | **I9** | Média |
| 21 | T6 §5.1.2 Como ler multiplicidade (tabela de notações) | p. 14–15 | **Q3** | — | — |
| 22 | T6 §5.1.3 Procedimento de modelagem (7 passos) | p. 15 | — | Agrupado em I13 (passo 6: testar com instâncias mínimas, máximas e inválidas) | Baixa |
| 23 | T6 §5.1.4 Classe de associação (`Matricula`) | p. 15 | Q10 (discursiva) | **I10**, I11 | Alta |
| 24 | T6 §5.1.5 Limitações da UML; cardinalidade ≠ ordem/unicidade (`ordered`, `unique`, `Set` x `List`) | p. 15 | Q10 (discursiva, parcial) | **I11** | Média |
| 25 | T7 §5.2.1–5.2.3 Associação, agregação compartilhada e composição: critério de decisão, "composição ≠ `new`/classe interna/destrutor", "menor semântica suficiente" | p. 15–16 | Q3 (só a notação UML num caso dado) | **I12** | Alta |
| 26 | T8 §6.1.1 Como ler um padrão (23 padrões GoF em 3 grupos) + §6.1.5 Comparação dos três padrões (tabela) | p. 16–17, 20 | Q4 (só como distratores) | **I14** | Alta |
| 27 | T8 §6.1.2 Observer: notificação extensível (`ProductCatalog`) | p. 17–18 | Q4 (distrator C) | **I15** | Alta |
| 28 | T8 §6.1.3 Mediator: coordenação centralizada (`FormMediator`, `RegistrationDialog`) | p. 18–19 | — | **I16** | Alta |
| 29 | T8 §6.1.4 Singleton: unicidade em escopo real (Holder, `enum`, custo do acesso global, injeção) | p. 19–20 | Q4 (distrator D); Q8 item 6 (discursiva) | **I17** | Alta |
| 30 | T8 §6.2 Como escolher um padrão sem decorar nomes (tabela de decisão; Fig. 5) | p. 17, 20 | — | **I18** | Alta |
| 31 | §7.1 Integração 1: Carrinho, composição e Strategy | p. 20–21 | Q4 (Strategy) | A parte de composição foi para I12 | — |
| 32 | §7.2 Integração 2: Pedido, UML e invariantes (tabela de instâncias válidas/inválidas) | p. 21–22 | — | **I13** | Média |
| 33 | §7.3 Integração 3: Checkout com Mediator e Observer | p. 22 | — | I18 (agrupado) | Alta |
| 34 | §7.4 Integração 4: Biblioteca e classe de associação | p. 22 | Q10 (discursiva análoga) | I10 | Alta |
| 35 | §8 Atividades 1–3 (diagnóstico, refatoração, validação UML) | p. 22–23 | **Q8, Q9, Q10** | — | — |
| 36 | Seções dos slides: Q1 Polimorfismo/Template Method/shadowing · Q2 Herança x composição/LSP · Q3 UML · Q4 Strategy/OCP · Q5 Abstrata x interface · Q6 Encapsulamento/Tell, Don't Ask/Modelo Anêmico | Slides p. 3–34 | **Q1–Q6** | — | — |

**Resumo:** 36 subtópicos (35 da apostila + as seções dos slides, agrupadas). 9 já estão cobertos por questões conhecidas (linhas 5, 7, 8, 11, 17, 21, 31, 35 e 36). Os outros 27 não têm questão objetiva conhecida e são cobertos aqui por **18 questões inferidas**; alguns subtópicos pequenos foram agrupados, como indicado na tabela. **Gabaritos:** A = 5 (I5, I9, I11, I16, I18) · B = 4 (I1, I8, I10, I15) · C = 4 (I2, I4, I6, I12) · D = 5 (I3, I7, I13, I14, I17).

## Índice
1. [I1 — Identidade x igualdade lógica: `==`, `equals` e `hashCode`](#i1--identidade-x-igualdade-lógica--equals-e-hashcode)
2. [I2 — Contrato da operação: pré-condição, pós-condição e invariante (`Conta`)](#i2--contrato-da-operação-pré-condição-pós-condição-e-invariante-conta)
3. [I3 — Depender do contrato e evolução de uma interface pública (`default`)](#i3--depender-do-contrato-e-evolução-de-uma-interface-pública-default)
4. [I4 — Vazamento da representação: getter que devolve a coleção interna](#i4--vazamento-da-representação-getter-que-devolve-a-coleção-interna)
5. [I5 — Herança múltipla por interfaces e conflito de métodos `default`](#i5--herança-múltipla-por-interfaces-e-conflito-de-métodos-default)
6. [I6 — Sentidos de herança, subclasse x subtipo e construtores (afirmativas)](#i6--sentidos-de-herança-subclasse-x-subtipo-e-construtores-afirmativas)
7. [I7 — Sobrecarga x sobrescrita x ocultação de método `static`](#i7--sobrecarga-x-sobrescrita-x-ocultação-de-método-static)
8. [I8 — Subtipagem comportamental (Liskov): subtipo com pré-condição mais forte](#i8--subtipagem-comportamental-liskov-subtipo-com-pré-condição-mais-forte)
9. [I9 — UML: visibilidade e o que o diagrama de classes (não) modela](#i9--uml-visibilidade-e-o-que-o-diagrama-de-classes-não-modela)
10. [I10 — Classe de associação e regras além da multiplicidade (biblioteca)](#i10--classe-de-associação-e-regras-além-da-multiplicidade-biblioteca)
11. [I11 — Cardinalidade não é unicidade: limites da UML (asserção-razão)](#i11--cardinalidade-não-é-unicidade-limites-da-uml-asserção-razão)
12. [I12 — Associação, agregação ou composição? (Carrinho, Item e Produto)](#i12--associação-agregação-ou-composição-carrinho-item-e-produto)
13. [I13 — Testando o modelo com instâncias válidas e inválidas (Pedido)](#i13--testando-o-modelo-com-instâncias-válidas-e-inválidas-pedido)
14. [I14 — Classificação e custos dos padrões GoF (associação)](#i14--classificação-e-custos-dos-padrões-gof-associação)
15. [I15 — Observer: notificação, cancelamento de inscrição e cópia da lista](#i15--observer-notificação-cancelamento-de-inscrição-e-cópia-da-lista)
16. [I16 — Mediator: teia de referências cruzadas em um formulário](#i16--mediator-teia-de-referências-cruzadas-em-um-formulário)
17. [I17 — Singleton com Holder: segurança, limites e custo do acesso global](#i17--singleton-com-holder-segurança-limites-e-custo-do-acesso-global)
18. [I18 — Escolhendo o padrão pelo problema, sem decorar nomes (checkout)](#i18--escolhendo-o-padrão-pelo-problema-sem-decorar-nomes-checkout)
19. [Quadro-resumo de gabaritos](#quadro-resumo-de-gabaritos)

---

## I1 — Identidade x igualdade lógica: `==`, `equals` e `hashCode`
**Subtópico coberto:** Tópico 1, §3.1.3 "Sobrecarga, igualdade e operações estáticos" (apostila p. 8) e linha "equals/hashCode" da tabela §3.1.5 (p. 9).
**Por que é provável:** a apostila enuncia a regra (`==` testa identidade, `equals` expressa igualdade lógica, e quem redefine `equals` precisa respeitar o contrato de `hashCode`). A tabela de decisões repete o risco, e a "Verificação rápida" (p. 9) pede exatamente essa diferença. Nenhuma questão objetiva conhecida cobra o tema.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única (interpretação de código + avaliação de projeto)

**Enunciado:**

QUESTÃO I1 · QUESTÃO INFERIDA NO ESTILO ENADE

CONTEXTUALIZAÇÃO (situação-problema)
Em sistemas orientados a objetos, comparar objetos exige distinguir **identidade** de **igualdade lógica**. Uma equipe de comércio eletrônico mantém o catálogo de produtos em memória e usa um `HashSet` para impedir duplicidades. Um desenvolvedor redefiniu a igualdade da classe `Produto` para que dois objetos com o mesmo SKU sejam considerados iguais, mas o relatório de catálogo continua exibindo produtos duplicados.

COMANDO
Considerando a diferença entre identidade e igualdade lógica e o contrato exigido pelas estruturas baseadas em hash em Java, avalie a saída do programa e a qualidade da decisão de implementação. Assinale a alternativa tecnicamente adequada:

CENÁRIO (dados de suporte): **Qual a saída do programa e por que há duplicidade?**
```java
import java.util.HashSet;
import java.util.Set;

class Produto {
    private final String sku;

    public Produto(String sku) { this.sku = sku; }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Produto)) return false;
        return sku.equals(((Produto) o).sku);
    }
    // hashCode() não foi redefinido
}

public class Cadastro {
    public static void main(String[] args) {
        Produto a = new Produto("SKU-1");
        Produto b = new Produto("SKU-1");
        Set<Produto> produtos = new HashSet<>();
        produtos.add(a);
        produtos.add(b);
        System.out.println((a == b) + " " + a.equals(b) + " " + produtos.size());
    }
}
```
_Considere que o `hashCode()` herdado de `Object` devolve valores diferentes para `a` e `b`._

Qual alternativa é tecnicamente adequada?

**Alternativas:**
- **A)** A saída será `true true 1`, pois a redefinição de `equals` faz o operador `==` passar a comparar o conteúdo dos objetos. O projeto está correto: `equals` é suficiente para que o `HashSet` descarte `b` como duplicata.
- **B)** A saída será `false true 2`. `==` testa identidade, e `a` e `b` são instâncias distintas; `equals` expressa a igualdade lógica por SKU; mas o `HashSet` localiza os elementos primeiro pelo `hashCode`. O projeto viola o contrato `equals`/`hashCode`: `hashCode` deveria ser redefinido com base no mesmo campo `sku`.
- **C)** A saída será `false true 1`, pois o `HashSet` usa exclusivamente `equals` para detectar duplicidade. O projeto está adequado, e redefinir `hashCode` serviria apenas para otimizar o desempenho da busca, sem alterar o resultado.
- **D)** A saída será `false false 2`, pois um `equals` que recebe `Object` não sobrescreve o método herdado e caracteriza uma sobrecarga. O problema seria resolvido trocando a assinatura `equals(Object)` por `equals(Produto)`.

**Gabarito: B**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Para referências, `==` **sempre** testa identidade. Redefinir `equals` não muda o operador (Java não tem sobrecarga de operadores). Como `a` e `b` foram criados com dois `new`, `a == b` é `false`. Sem `hashCode` coerente, o `HashSet` também não descarta `b`.
- **B) ✅** — Executado em Java 21, imprime **`false true 2`**. O `HashSet` (implementado sobre `HashMap`) usa o `hashCode` para escolher o compartimento e só chama `equals` entre elementos com o mesmo hash. Com o `hashCode` de `Object`, baseado em identidade, `b` fica com outro hash e entra como elemento novo. Correção: `@Override public int hashCode() { return sku.hashCode(); }` (ou `Objects.hash(sku)`). Com ela, a saída passa a ser `false true 1` (testado). O próprio `javac -Xlint` avisa: _"Class Produto overrides equals, but neither it nor any superclass overrides hashCode method"_.
- **C) ❌** — O `HashSet` não usa só `equals`. O contrato determina que objetos iguais por `equals` tenham o mesmo `hashCode`. Quebrar o contrato muda o **resultado** (aceita duplicatas), não apenas o desempenho.
- **D) ❌** — Inverte a pegadinha. `equals(Object o)` com `@Override` **é** a sobrescrita correta. Quem cria uma sobrecarga é `equals(Produto)`, que não substitui `Object.equals(Object)`, e as coleções continuam chamando a versão herdada. Teste: com `equals(Produto)` e `hashCode` correto, `c.equals((Object) d)` dá `false` e o `HashSet` fica com 2 elementos.

**Base no material:** p. 8: "Em Java, `==` para referências testa identidade. `equals` expressa igualdade lógica quando a classe define esse contrato. Se `equals` for redefinido, o contrato de `hashCode` também precisa ser respeitado para uso em estruturas baseadas em hash [8]". Tabela p. 9: "equals/hashCode — Definir uma noção de igualdade estável e adequada ao domínio — Chaves mutáveis podem tornar objetos difíceis de localizar em HashSet". "Verificação rápida" p. 9: "Explique a diferença entre identidade (==) e igualdade lógica (equals)".
**Conceito-chave para a prova:** `==` = identidade. `equals` = igualdade lógica definida pela classe. Redefiniu `equals`, redefina `hashCode` com os **mesmos** campos. Variação provável (tabela p. 9): se o campo usado no `hashCode` mudar **depois** da inserção, `set.contains(obj)` passa a devolver `false` mesmo com o objeto dentro do conjunto (testado: `contains=false`, `size=1`). Use campos imutáveis na igualdade.

---

## I2 — Contrato da operação: pré-condição, pós-condição e invariante (`Conta`)
**Subtópico coberto:** Tópico 1, §3.1.1 (operação = nome, parâmetros, retorno, contrato, implementação; construtor) e §3.1.2 "Exemplo: uma conta que preserva sua invariante" (p. 7–8). Também o glossário §2.1, verbete "Operação" (p. 6).
**Por que é provável:** a "Verificação rápida" (p. 9) pede: "Indique pré-condição, pós-condição e invariante no exemplo Conta". O glossário põe como pergunta de controle "Qual pré-condição e pós-condição a operação garante?". Q6 usa uma conta, mas cobra o setter e o Tell, Don't Ask, não o contrato.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única

**Enunciado:**

QUESTÃO I2 · QUESTÃO INFERIDA NO ESTILO ENADE

CONTEXTUALIZAÇÃO (situação-problema)
O significado de uma operação não se esgota em seu corpo. O cliente também depende de pré-condições, pós-condições, invariantes e efeitos observáveis. Antes de liberar a classe `Conta` para outros módulos de um sistema financeiro, a equipe de arquitetura precisa documentar o contrato da classe e justificar por que sua regra fundamental não pode ser violada pelos clientes.

COMANDO
Considerando os conceitos de contrato de operação e de invariante de classe, analise a implementação e assinale a alternativa que identifica corretamente uma pré-condição e uma pós-condição da operação `sacar`, a invariante da classe e o mecanismo que preserva essa invariante:

CENÁRIO (dados de suporte): **Qual é o contrato da classe Conta?**
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

Qual alternativa é tecnicamente adequada?

**Alternativas:**
- **A)** Pré-condição de `sacar`: `saldoCentavos >= 0` ao final do saque. Pós-condição: `valorCentavos > 0`. Invariante: `saldoCentavos > 0` em qualquer estado, garantida pelo modificador `private`, que por si só impede transições inválidas.
- **B)** Pré-condição de `sacar`: o construtor deve ser executado novamente antes de cada saque para revalidar o saldo. Pós-condição: lançar `IllegalStateException`. Invariante: o `id` pode ser alterado, desde que não fique em branco.
- **C)** Pré-condição de `sacar`: `0 < valorCentavos <= saldoCentavos`. Pós-condição: o novo saldo é igual ao saldo anterior menos `valorCentavos`. Invariante: `saldoCentavos >= 0`, estabelecida pelo construtor e preservada porque só `depositar` e `sacar`, que validam suas pré-condições, alteram o saldo.
- **D)** Pré-condição de `sacar`: `valorCentavos > 0`. Pós-condição: `saldoCentavos >= 0`. Invariante: `saldoCentavos >= 0`, que permaneceria garantida mesmo com um `setSaldoCentavos(long)` público, pois o campo continuaria `private`.

**Gabarito: C**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Troca pré e pós-condição: `valor > 0` é exigência **antes** da execução, e "saldo >= 0 depois" é efeito da invariante. A invariante "> 0" também está errada: saldo zero é permitido (testado: o construtor aceita saldo inicial 0, e sacar o saldo inteiro deixa 0). E atribui a garantia só ao `private`, o "Erro recorrente" da p. 12.
- **B) ❌** — O construtor não é uma operação chamada depois da criação: ele só participa da criação e da inicialização (p. 7). Lançar exceção é a **reação** à violação da pré-condição, não uma pós-condição. O `id` é `final` e nunca muda.
- **C) ✅** — Pré-condição completa de `sacar`: valor positivo (`exigirValorPositivo`) e não maior que o saldo (senão `IllegalStateException`, sem mudar o estado). Pós-condição: `saldo_novo = saldo_anterior − valor`. Invariante: `saldoCentavos >= 0` (e também `id` não nulo, não vazio e imutável). O construtor estabelece um estado inicial válido, e as únicas operações que mudam o saldo verificam suas pré-condições, então a invariante se mantém em todo estado observável.
- **D) ❌** — A pré-condição indicada está incompleta, e "saldo >= 0" é a invariante, não a pós-condição específica de `sacar`. O erro decisivo é a afirmação final: um setter público irrestrito permitiria `setSaldoCentavos(-500)`. Campo `private` com setter livre é encapsulamento fraco (p. 11–12).

**Base no material:** p. 7: "O corpo não esgota o significado do operação: o cliente também depende de pré-condições, pós-condições, invariantes e efeitos observáveis. Em Java, o construtor participa da criação e inicialização; ele não é um operação chamado depois da criação". p. 7–8: "A regra `saldoCentavos >= 0` é uma invariante da classe. A implementação não expõe um `setSaldo` irrestrito [...] O construtor estabelece uma condição inicial válida. `depositar` e `sacar` verificam suas pré-condições e preservam a invariante".
**Conceito-chave para a prova:** pré-condição = o que o cliente precisa garantir **antes** da chamada. Pós-condição = o que a operação garante **depois**. Invariante = o que vale em **todo** estado observável. O construtor estabelece a invariante e as operações de domínio a preservam. `private` + setter livre não protege nada. A apostila usa `long` em centavos para evitar erro de arredondamento.

---

## I3 — Depender do contrato e evolução de uma interface pública (`default`)
**Subtópico coberto:** Tópico 2, §3.2.2 "Exemplo: depender do contrato" e §3.2.3 "Critério de escolha" (apostila p. 10).
**Por que é provável:** a apostila traz código pronto (`Exportador`, `ExportadorCsv`, `ServicoDeRelatorios`) e alertas fáceis de virar distratores: "Adicionar operação abstrato a uma interface pública pode quebrar implementadores. Um operação default reduz parte da ruptura de compilação, mas não resolve automaticamente a compatibilidade semântica" e "Um compilador verifica assinaturas e visibilidade; não prova pós-condições". Q5 cobre só a escolha entre classe abstrata e interface.
**Prioridade:** Média
**Tipo ENADE:** Resposta única (decisão de projeto)

**Enunciado:**

QUESTÃO I3 · QUESTÃO INFERIDA NO ESTILO ENADE

CONTEXTUALIZAÇÃO (situação-problema)
Uma equipe de plataforma mantém uma biblioteca interna de relatórios. O `ServicoDeRelatorios` depende apenas da interface `Exportador`, recebida pelo construtor, e mais de vinte classes de outras equipes já implementam essa interface (CSV, PDF, JSON, XML...). Surge um novo requisito: cada exportador deve informar a extensão do arquivo gerado, para que o serviço monte o nome do arquivo.

COMANDO
Considerando o papel das interfaces como contratos, os efeitos da evolução de uma interface pública sobre os implementadores existentes e os limites do que o compilador consegue verificar, assinale a alternativa que apresenta a decisão de projeto tecnicamente adequada:

CENÁRIO (dados de suporte): **Como evoluir o contrato Exportador sem quebrar quem já o implementa?**
```java
public interface Exportador {
    String exportar(Relatorio relatorio);
    // novo requisito: informar a extensão do arquivo (ex.: "csv", "pdf")
}

public final class ExportadorCsv implements Exportador {
    @Override
    public String exportar(Relatorio relatorio) {
        return relatorio.linhas().stream()
                .map(linha -> String.join(";", linha))
                .collect(java.util.stream.Collectors.joining("\n"));
    }
}

public final class ServicoDeRelatorios {
    private final Exportador exportador;

    public ServicoDeRelatorios(Exportador exportador) {
        this.exportador = java.util.Objects.requireNonNull(exportador);
    }

    public String gerar(Relatorio relatorio) {
        return exportador.exportar(relatorio);
    }
}
```

Qual alternativa é tecnicamente adequada?

**Alternativas:**
- **A)** Declarar `String extensao();` como método abstrato é a opção mais segura: os implementadores existentes continuam compilando, e o compilador passa a provar que cada implementação devolve uma extensão coerente com o formato exportado.
- **B)** Declarar na interface o campo `String extensao = "txt";`, que cada implementação poderá alterar no próprio construtor, pois interfaces em Java passaram a admitir estado mutável por instância desde a introdução dos métodos `default`.
- **C)** Converter `Exportador` em classe abstrata com o campo `protected String extensao`, pois assim cada implementador poderá estender, ao mesmo tempo, `Exportador` e as outras classes-base de que já depende, sem nenhuma alteração nos implementadores.
- **D)** Declarar `extensao()` como método `default` reduz a ruptura de compilação, pois os implementadores existentes herdam uma implementação padrão. Porém, isso não garante compatibilidade semântica: o compilador verifica assinaturas e visibilidade, não pós-condições, e o novo contrato precisa ser documentado e testado.

**Gabarito: D**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Um método abstrato novo **quebra** todos os implementadores existentes (testado: _"ExportadorCsv is not abstract and does not override abstract method extensao() in Exportador"_). E o compilador não prova coerência semântica (pós-condições), só assinaturas e visibilidade.
- **B) ❌** — Campos de interface são implicitamente `public static final`: são constantes do tipo, não estado por instância. Atribuir valor no construtor do implementador não compila (testado: _"cannot assign a value to static final variable extensao"_). Métodos `default` não mudaram isso.
- **C) ❌** — Uma classe Java tem **uma única** superclasse direta. Os implementadores que já estendem outra classe não poderiam estender `Exportador`, e todos teriam de trocar `implements` por `extends`, o que é uma ruptura maior. A classe abstrata só seria preferível se as implementações precisassem compartilhar estado protegido, validação e uma sequência de passos (p. 10).
- **D) ✅** — `default String extensao() { return "txt"; }` mantém os implementadores compilando (testado) e o serviço continua dependendo só do contrato. Mas um `ExportadorPdf` antigo passaria a responder "txt" até sobrescrever o método. A compilação não quebra, mas o significado pode quebrar em silêncio. Por isso é preciso documentar a pós-condição e testar cada implementação. A apostila cita ainda a combinação interface (contrato) + classe abstrata esqueleto, como `AbstractList<E>`.

**Base no material:** p. 10: "`ServicoDeRelatorios` depende de `Exportador`, não de `ExportadorCsv`. Um teste pode fornecer uma implementação controlada. Uma classe abstrata seria preferível se as implementações precisassem compartilhar estado protegido [...]" e "Um compilador verifica assinaturas e visibilidade; não prova pós-condições, invariantes nem substituibilidade comportamental. Adicionar operação abstrato a uma interface pública pode quebrar implementadores. Um operação default reduz parte da ruptura de compilação, mas não resolve automaticamente a compatibilidade semântica". p. 9: "Campos declarados em interfaces são constantes `public static final`, não estado mutável por instância".
**Conceito-chave para a prova:** dependa do contrato (interface) e receba a implementação pelo construtor, o que facilita dublês de teste. Método abstrato novo em interface pública quebra implementadores. Método `default` evita a quebra de compilação, mas não garante a semântica. Compilador ≠ prova de contrato.

---

## I4 — Vazamento da representação: getter que devolve a coleção interna
**Subtópico coberto:** Tópico 3, §4.1.2 "Exemplo: não vazar a representação" e §4.1.3 "Checklist de encapsulamento" (apostila p. 11). Também a frase de §3.1.3 (p. 8): "Uma coleção privada também pode vazar se um getter devolver a própria coleção modificável".
**Por que é provável:** é um exemplo de código próprio do tópico (`Agenda` com `List.copyOf`), reforçado no checklist ("Alguma referência mutável interna é devolvida [...] sem cópia?" e "A imutabilidade é real ou apenas a referência é final?") e no quadro "Erro recorrente". Q6 cobre o setter público, não o vazamento por getter.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única (interpretação de código + avaliação de projeto)

**Enunciado:**

QUESTÃO I4 · QUESTÃO INFERIDA NO ESTILO ENADE

CONTEXTUALIZAÇÃO (situação-problema)
Um sistema acadêmico limita o número de alunos por turma. O desenvolvedor declarou a lista de alunos como `private final` e criou uma operação `matricular` que valida a capacidade, acreditando que isso basta para proteger a regra. Durante os testes de fronteira, a equipe de qualidade encontrou turmas com mais alunos que o permitido.

COMANDO
Considerando o encapsulamento como preservação da abstração e das invariantes, e não apenas como ocultação de campos, avalie o valor impresso e a decisão de implementação. Assinale a alternativa tecnicamente adequada:

CENÁRIO (dados de suporte): **A regra de capacidade da turma está protegida?**
```java
import java.util.ArrayList;
import java.util.List;

final class Turma {
    private static final int CAPACIDADE = 2;
    private final List<String> alunos = new ArrayList<>();

    public void matricular(String aluno) {
        if (alunos.size() >= CAPACIDADE)
            throw new IllegalStateException("turma lotada");
        alunos.add(aluno);
    }

    public List<String> getAlunos() {
        return alunos;
    }
}

public class Secretaria {
    public static void main(String[] args) {
        Turma t = new Turma();
        t.matricular("Ana");
        t.matricular("Bia");
        t.getAlunos().add("Caio");
        System.out.println(t.getAlunos().size());
    }
}
```

Qual alternativa é tecnicamente adequada?

**Alternativas:**
- **A)** Imprime `2`, pois o modificador `final` no campo `alunos` torna a lista imutável e a chamada `add("Caio")` é ignorada. A classe está bem encapsulada, pois o campo é `private` e a única alteração prevista passa por `matricular`.
- **B)** Não compila, pois um campo `private` não pode ser modificado fora da classe, nem mesmo por meio da referência devolvida pelo getter. A classe está bem encapsulada, e o compilador garante a invariante de capacidade.
- **C)** Imprime `3`: o getter devolve a referência da coleção interna mutável, e o cliente burla a regra de capacidade sem passar por `matricular`; `final` apenas impede reatribuir a referência. A correção é devolver uma cópia não modificável, como `List.copyOf(alunos)`.
- **D)** Imprime `3`, e a correção adequada é declarar `getAlunos()` como `final`, o que impede que clientes alterem a lista devolvida e preserva a invariante de capacidade sem necessidade de cópias.

**Gabarito: C**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Confunde referência `final` com objeto imutável. `final` impede só `alunos = outraLista`. O `ArrayList` continua mutável e `add` funciona. Saída real: `3`.
- **B) ❌** — `private` controla o acesso ao **nome** do campo, não ao objeto referenciado. Quem recebe a referência pelo getter pode chamar qualquer método público do `ArrayList`. O código compila e roda. Além disso, a visibilidade é uma restrição verificada pelo compilador, não uma garantia de invariantes (p. 11).
- **C) ✅** — Executado em Java 21, imprime **3**: a turma de capacidade 2 ficou com 3 alunos sem passar por `matricular`. Com `return List.copyOf(alunos);`, a tentativa `getAlunos().add("Caio")` lança `UnsupportedOperationException` e o tamanho continua 2 (testado). Ressalva da apostila: `List.copyOf` não torna os **elementos** imutáveis nem resolve concorrência. Resolve o vazamento daquela coleção.
- **D) ❌** — Método `final` impede **sobrescrita** em subclasses. Não tem relação com a mutabilidade do objeto devolvido, então a lista continua vazando.

**Base no material:** p. 11: "Uma classe com campo privado pode continuar mal encapsulada se expuser setters irrestritos, retornar referências mutáveis internas ou usar `protected` apenas como atalho para subclasses" e "`List.copyOf` impede que o cliente modifique a coleção interna por meio do retorno. Isso não torna os elementos automaticamente imutáveis [...]". Checklist p. 11, itens 4 e 7. p. 8: "Uma referência `final` não torna automaticamente imutável o objeto referenciado. Uma coleção privada também pode vazar se um getter devolver a própria coleção modificável".
**Conceito-chave para a prova:** encapsular = controlar **quais transições de estado** o contrato permite. Getter que devolve coleção mutável interna vaza a representação. `final` na referência ≠ objeto imutável. Corrija com cópia defensiva/não modificável (`List.copyOf`) e operações de domínio (`matricular`).

---

## I5 — Herança múltipla por interfaces e conflito de métodos `default`
**Subtópico coberto:** Tópico 4, §4.2.3 "Herança múltipla por interfaces" (apostila p. 13).
**Por que é provável:** a apostila insiste que "a formulação rigorosa não é 'Java tem' ou 'Java não tem' herança múltipla sem qualificação" e cita o conflito de `default` ("a classe pode precisar resolver o conflito explicitamente"). O exemplo usa as interfaces `Exportavel` e `Auditavel`, as mesmas que reaparecem em Q5. Q5 cobra a escolha abstrata x interface, não o conflito.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única (interpretação de código)

**Enunciado:**

QUESTÃO I5 · QUESTÃO INFERIDA NO ESTILO ENADE

CONTEXTUALIZAÇÃO (situação-problema)
Para que relatórios possam ser exportados e auditados, uma equipe modelou duas capacidades como interfaces. Para evitar código repetido, cada interface ganhou um método `default` com uma descrição padrão. A classe `Relatorio` implementa as duas capacidades.

COMANDO
Considerando as regras de herança múltipla de tipo em Java e a resolução de conflitos entre métodos `default`, avalie a saída do programa e o comportamento do compilador caso a sobrescrita em `Relatorio` seja removida. Assinale a alternativa tecnicamente adequada:

CENÁRIO (dados de suporte): **O que acontece quando duas interfaces oferecem o mesmo método default?**
```java
interface Exportavel {
    default String descricao() { return "exportavel"; }
}

interface Auditavel {
    default String descricao() { return "auditavel"; }
}

final class Relatorio implements Exportavel, Auditavel {
    @Override
    public String descricao() {
        return Exportavel.super.descricao() + "+" + Auditavel.super.descricao();
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println(new Relatorio().descricao());
    }
}
```

Qual alternativa é tecnicamente adequada?

**Alternativas:**
- **A)** Imprime `exportavel+auditavel`. Se a sobrescrita em `Relatorio` for removida, o código deixa de compilar, pois a classe herda dois métodos `default` não relacionados com a mesma assinatura e precisa resolver o conflito explicitamente. Java oferece herança múltipla de tipo por interfaces, mas não múltiplas superclasses de estado.
- **B)** Imprime `exportavel`, pois, em caso de conflito, Java aplica a ordem da cláusula `implements` (a primeira interface vence), de modo semelhante à MRO C3 do Python. A sobrescrita em `Relatorio` é redundante e pode ser removida sem efeito.
- **C)** Não compila, pois Java proíbe que uma classe implemente duas interfaces que declarem métodos com a mesma assinatura. Para combinar as duas capacidades, seria necessário herdar de duas classes abstratas.
- **D)** Imprime `exportavel+auditavel`. Ao remover a sobrescrita, o código continuaria compilando e imprimiria `auditavel`, pois a última interface listada sobrescreve a anterior, como ocorre com as bases virtuais em C++.

**Gabarito: A**

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — Executado em Java 21, imprime **`exportavel+auditavel`**. `Interface.super.metodo()` chama explicitamente a versão `default` de cada interface. Sem a sobrescrita, o compilador rejeita (testado): _"types Exportavel and Auditavel are incompatible; class Relatorio inherits unrelated defaults for descricao() from types Exportavel and Auditavel"_. Esta é a formulação rigorosa da apostila: herança múltipla **de tipo** (e de comportamento `default`) por interfaces, sem múltiplas superclasses de estado e implementação.
- **B) ❌** — Java não escolhe pela ordem do `implements`, e a sobrescrita não é redundante. A MRO C3 é um mecanismo do Python, citado na apostila só como comparação.
- **C) ❌** — Java permite implementar várias interfaces com métodos de mesma assinatura. Se ambas fossem abstratas, uma única implementação satisfaria as duas. Só o conflito entre dois `default` exige resolução. E Java não permite estender duas classes.
- **D) ❌** — Não existe a regra "a última interface vence". Bases virtuais são um recurso do C++ para compartilhar o subobjeto-base no problema do diamante, sem relação com a resolução de `default` em Java.

**Base no material:** p. 13: "Java tem herança múltipla de tipo por interfaces, mas não permite múltiplas superclasses de estado e implementação como C++. Se duas interfaces fornecerem o mesmo operação default, a classe pode precisar resolver o conflito explicitamente". p. 12: "C++ permite várias classes-base; bases virtuais tratam o compartilhamento de um subobjeto-base no problema do diamante. Python usa [...] a MRO C3".
**Conceito-chave para a prova:** uma classe Java pode implementar várias interfaces, mas estender só uma classe. Dois `default` iguais e não relacionados causam erro de compilação até a classe sobrescrever o método (e, se quiser, delegar com `X.super.m()`). "Java não tem herança múltipla" é uma frase incompleta.

---

## I6 — Sentidos de herança, subclasse x subtipo e construtores (afirmativas)
**Subtópico coberto:** Tópico 4, §4.2.1 "Três sentidos de herança" e §4.2.2 "Exemplo Java: especialização coesa" (apostila p. 12–13).
**Por que é provável:** a seção traz distinções do tipo "pegadinha" (subclasse ≠ subtipo; construtores não são herdados; `@Override` verifica a intenção; Java x C++ x Python) e o exemplo `Forma`/`Circulo`, que serve de cenário. Nenhuma questão conhecida cobra esses pontos (Q1 trata de field shadowing, Q2 de composição).
**Prioridade:** Média
**Tipo ENADE:** Afirmativas múltiplas (adaptado para 4 alternativas)

**Enunciado:**

QUESTÃO I6 · QUESTÃO INFERIDA NO ESTILO ENADE

CONTEXTUALIZAÇÃO (situação-problema)
Herança pode significar herança de tipo, de implementação ou de estado, e uma linguagem pode permitir uma dessas formas sem permitir as outras. Em uma revisão de código, a equipe analisa a hierarquia de formas geométricas abaixo para decidir se ela pode servir de contrato de substituição para os clientes que calculam áreas.

COMANDO
Considerando o código apresentado e os conceitos de herança, subtipagem e construção de objetos em Java, avalie as afirmativas a seguir.

CENÁRIO (dados de suporte): **O que a herança entre Forma e Circulo garante, e o que não garante?**
```java
public abstract class Forma {
    private final String cor;

    protected Forma(String cor) {
        this.cor = java.util.Objects.requireNonNull(cor);
    }

    public String cor() { return cor; }
    public abstract double area();
}

public final class Circulo extends Forma {
    private final double raio;

    public Circulo(String cor, double raio) {
        super(cor);
        if (raio <= 0) throw new IllegalArgumentException("raio inválido");
        this.raio = raio;
    }

    @Override
    public double area() { return Math.PI * raio * raio; }
}
```

I. Construtores não são membros herdados. Como `Forma` não declara construtor sem parâmetros, o construtor de `Circulo` precisa inicializar a parte da superclasse com a chamada explícita `super(cor)`. Sem essa chamada, o código não compila.

II. Por ser subclasse de `Forma`, `Circulo` é automaticamente um subtipo comportamental de `Forma`, pois o compilador, ao aceitar o `@Override` de `area()`, comprova que a substituição preserva as pós-condições esperadas pelos clientes.

III. A anotação `@Override` permite ao compilador verificar a intenção de sobrescrita: se o método fosse declarado, por engano, como `area(int casas)`, haveria erro de compilação em vez de uma nova sobrecarga silenciosa.

IV. Dizer apenas que "Java não tem herança múltipla" é impreciso. Java tem herança múltipla de tipo por interfaces, mas não permite múltiplas superclasses de estado e implementação. C++ admite várias classes-base, e Python organiza certas hierarquias múltiplas pela MRO C3.

É correto o que se afirma em:

**Alternativas:**
- **A)** I e II, apenas.
- **B)** II e IV, apenas.
- **C)** I, III e IV, apenas.
- **D)** I, II, III e IV.

**Gabarito: C**

**Julgamento das afirmativas:**
- **I — Verdadeira.** Testado: sem `super(cor)`, o compilador acusa _"constructor Forma in class Forma cannot be applied to given types; required: String; found: no arguments"_. A subclasse inicializa a parte da superclasse por `super(...)`, e construtores não são membros herdados (p. 13).
- **II — Falsa.** "Subclasse e subtipo não são sinônimos" (p. 12). O compilador verifica assinaturas e visibilidade. Não prova pós-condições nem substituibilidade comportamental (p. 10). A herança só é legítima como subtipo se as instâncias puderem substituir as do tipo base sem quebrar expectativas documentadas (Liskov e Wing).
- **III — Verdadeira.** Testado: `@Override public double area(int casas)` gera _"method does not override or implement a method from a supertype"_. Sem a anotação, `area(int)` seria só uma sobrecarga nova, e (neste caso) `Circulo` ainda falharia por não implementar o `area()` abstrato.
- **IV — Verdadeira.** É a formulação rigorosa da p. 13, junto com a comparação C++/Python da p. 12.

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Inclui II, que é falsa.
- **B) ❌** — Inclui II e deixa de fora I e III, que são verdadeiras.
- **C) ✅** — I, III e IV são verdadeiras; II é falsa.
- **D) ❌** — Inclui II.

**Base no material:** p. 12: "Herança pode significar herança de tipo, de implementação ou de estado [...] subclasse e subtipo não são sinônimos. Uma subclasse somente deve ser usada como subtipo quando instâncias dela puderem substituir instâncias do tipo base sem quebrar expectativas documentadas [4]". p. 13: "O construtor da subclasse inicializa a parte da superclasse por `super(...)`. Construtores não são membros herdados. Operações podem ser sobrescritos; campos podem ser ocultados [...] A anotação `@Override` ajuda o compilador a verificar a intenção de sobrescrita".
**Conceito-chave para a prova:** subclasse ≠ subtipo, e a substituibilidade é comportamental, não só de assinatura. Construtor não é herdado: use `super(...)`. `@Override` transforma um erro de assinatura em erro de compilação. Java = 1 superclasse + N interfaces.

---

## I7 — Sobrecarga x sobrescrita x ocultação de método `static`
**Subtópico coberto:** Tópico 5, §4.3.1 "Tipo estático, classe dinâmica e despacho", tabela Fenômeno / Seleção / Despacho dinâmico (apostila p. 13–14). Também Tópico 1, §3.1.3 (sobrecarga resolvida em compilação; `static` fora do despacho polimórfico, p. 8) e a linha "Instância ou static" da tabela §3.1.5 (p. 9).
**Por que é provável:** a tabela da p. 13–14 compara cinco fenômenos (sobrecarga, sobrescrita, ocultação, campo, genérico). Q1 cobra só dois (sobrescrita e campo). Os outros, sobrecarga e ocultação de `static`, são o próximo passo natural do mesmo estilo "qual a saída?".
**Prioridade:** Alta
**Tipo ENADE:** Resposta única (interpretação de código)

**Enunciado:**

QUESTÃO I7 · QUESTÃO INFERIDA NO ESTILO ENADE

CONTEXTUALIZAÇÃO (situação-problema)
Em Java, o mesmo trecho de código pode envolver mecanismos de seleção diferentes: alguns são decididos em tempo de compilação, a partir do tipo estático das expressões, e outros em tempo de execução, a partir da classe real do objeto. Um desenvolvedor júnior escreveu o programa abaixo para "provar" que todo método chamado sobre uma referência é polimórfico.

COMANDO
Considerando as diferenças entre sobrecarga, sobrescrita e ocultação de métodos `static`, determine a saída do programa e assinale a alternativa que a justifica corretamente:

CENÁRIO (dados de suporte): **Qual o valor impresso pela classe Teste?**
```java
class Base {
    static String nome() { return "Base"; }
    String tipo() { return "Base"; }
}

class Derivada extends Base {
    static String nome() { return "Derivada"; }
    @Override
    String tipo() { return "Derivada"; }
}

class Impressora {
    static String imprimir(Base b)     { return "imprimir(Base)"; }
    static String imprimir(Derivada d) { return "imprimir(Derivada)"; }
}

public class Teste {
    public static void main(String[] args) {
        Base ref = new Derivada();
        System.out.println(ref.tipo() + " | " + ref.nome() + " | " + Impressora.imprimir(ref));
    }
}
```

Qual alternativa é tecnicamente adequada?

**Alternativas:**
- **A)** `Derivada | Derivada | imprimir(Derivada)`, pois em Java todos os membros, inclusive os métodos `static` e a escolha entre sobrecargas, são resolvidos em execução pela classe real do objeto referenciado por `ref`.
- **B)** `Base | Base | imprimir(Base)`, pois o tipo declarado `Base` força vinculação estática de todos os membros. A anotação `@Override` apenas documenta a intenção e não altera o método executado.
- **C)** `Derivada | Base | imprimir(Derivada)`, pois sobrescrita e sobrecarga são formas de polimorfismo dinâmico resolvidas pela classe real do objeto, enquanto apenas os métodos `static` são resolvidos pelo tipo declarado.
- **D)** `Derivada | Base | imprimir(Base)`: `tipo()` é sobrescrito e despachado dinamicamente; `nome()` é `static`, foi apenas ocultado e é resolvido pelo tipo declarado; a sobrecarga de `imprimir` é escolhida em compilação pelo tipo estático do argumento.

**Gabarito: D**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Trata tudo como despacho dinâmico. Métodos `static` pertencem ao tipo e são **ocultados**, não sobrescritos. A sobrecarga é escolhida em compilação.
- **B) ❌** — O erro simétrico (o mesmo da alternativa B de Q1): ignora que `tipo()` é método de instância sobrescrito, despachado pela classe real (`Derivada`).
- **C) ❌** — Acerta `tipo()` e `nome()`, mas erra a sobrecarga. O compilador escolhe entre `imprimir(Base)` e `imprimir(Derivada)` pelo tipo **estático** do argumento (`ref` é declarado `Base`). O objeto real não é consultado.
- **D) ✅** — Executado em Java 21: **`Derivada | Base | imprimir(Base)`**. `ref.tipo()`: sobrescrita, decidida em execução. `ref.nome()`: método `static` chamado por uma referência, resolvido pelo tipo declarado `Base` (o `javac -Xlint` avisa: _"static method should be qualified by type name, Base, instead of by an expression"_, ou seja, chamar `static` por instância é má prática). `Impressora.imprimir(ref)`: sobrecarga resolvida em compilação pelo tipo estático `Base`.

**Base no material:** p. 13: "Sobrecarga usa o nome e os parâmetros disponíveis em compilação. Sobrescrita redefine um operação herdado compatível, e a implementação de instância elegível é escolhida dinamicamente. Operações `static` são ocultados, não despachados como instância". Tabela p. 13–14: Sobrecarga → "Nome e parâmetros em compilação / Não"; Sobrescrita → "Sim, para instância elegível"; Ocultação → "Membro static redeclarado / Não como instância"; Campo → "Tipo declarado da referência". p. 8: "Sobrecarga [...] a seleção é feita em compilação. Duas declarações que diferem apenas pelo retorno não constituem sobrecarga válida".
**Conceito-chave para a prova:** **em compilação** (tipo estático): sobrecarga, campos e métodos `static`/`private`. **Em execução** (classe real): só métodos de instância sobrescritos. Retorno diferente não cria sobrecarga (erro _"method f(int) is already defined"_). Polimorfismo paramétrico (generics, `List<T>`) é outro fenômeno, com apagamento de tipos.

---

## I8 — Subtipagem comportamental (Liskov): subtipo com pré-condição mais forte
**Subtópico coberto:** Tópico 5, §4.3.2 "Subtipagem comportamental" (apostila p. 14). Também o glossário "Subtipo" (p. 6) e o checklist final (p. 24: "polimorfismo é usado para variar comportamento, não para esconder casts em série").
**Por que é provável:** o slide 2 anuncia "Liskov, acoplamento e o uso correto de interfaces" como tema de Q2, mas Q2 cobra a troca de herança por composição. A regra de Liskov e Wing ("pré-condição mais forte", "lança exceção para entradas aceitas pelo tipo base") tem texto próprio na apostila e não tem questão objetiva.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única (análise de projeto)

**Enunciado:**

QUESTÃO I8 · QUESTÃO INFERIDA NO ESTILO ENADE

CONTEXTUALIZAÇÃO (situação-problema)
Um serviço de backup foi projetado para depender apenas da abstração `Armazenamento`. Assim, o destino dos arquivos (disco local, nuvem corporativa etc.) pode variar sem alterar o cliente. Uma nova implementação para um plano gratuito de nuvem foi adicionada, e, a partir dela, backups que sempre funcionaram com o disco local passaram a falhar em produção.

COMANDO
Considerando o polimorfismo de subtipos e a disciplina de subtipagem comportamental proposta por Liskov e Wing, avalie a nova implementação e assinale a alternativa tecnicamente adequada:

CENÁRIO (dados de suporte): **ArmazenamentoNuvemGratuito é um subtipo legítimo de Armazenamento?**
```java
public interface Armazenamento {
    /** Grava o conteúdo integralmente, de qualquer tamanho.
        Lança exceção apenas se chave ou conteúdo forem nulos. */
    void gravar(String chave, byte[] conteudo);
}

public class ArmazenamentoDisco implements Armazenamento {
    @Override
    public void gravar(String chave, byte[] conteudo) {
        // grava em disco local
    }
}

public class ArmazenamentoNuvemGratuito implements Armazenamento {
    @Override
    public void gravar(String chave, byte[] conteudo) {
        if (conteudo.length > 1_000_000)
            throw new UnsupportedOperationException("limite de 1 MB");
        // envia para a nuvem
    }
}

public final class Backup {
    private final Armazenamento destino;
    public Backup(Armazenamento destino) { this.destino = destino; }
    public void executar(String chave, byte[] dados) { destino.gravar(chave, dados); }
}
```

Qual alternativa é tecnicamente adequada?

**Alternativas:**
- **A)** O projeto está correto: como o código compila e a assinatura de `gravar` é idêntica nas duas implementações, o compilador garante que qualquer classe que implemente `Armazenamento` pode substituir outra sem quebrar o `Backup`.
- **B)** Há violação da subtipagem comportamental: `ArmazenamentoNuvemGratuito` exige uma pré-condição mais forte que a do contrato e lança exceção para entradas que o tipo base aceita, quebrando um cliente que estava correto. É preciso revisar o contrato ou deixar de tratar essa classe como subtipo de `Armazenamento`.
- **C)** A correção recomendada é incluir em `Backup` um teste `instanceof ArmazenamentoNuvemGratuito`, com cast e divisão do conteúdo em partes, pois `instanceof` é o mecanismo indicado para tratar variações de comportamento entre subtipos.
- **D)** O problema é de encapsulamento, não de subtipagem: basta declarar `gravar` como `protected` em `ArmazenamentoNuvemGratuito`, impedindo que o `Backup` o invoque com conteúdos grandes e preservando a hierarquia.

**Gabarito: B**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — "Uma assinatura compatível não basta" (p. 14). O compilador verifica tipos e visibilidade, não pré e pós-condições. Teste executado: com `ArmazenamentoDisco`, um backup de 5 MB grava. Com `ArmazenamentoNuvemGratuito`, falha com `UnsupportedOperationException: limite de 1 MB`.
- **B) ✅** — O contrato documentado aceita conteúdo de qualquer tamanho. O subtipo **fortalece a pré-condição** (≤ 1 MB) e lança exceção para entradas válidas no tipo base, exatamente o caso descrito na p. 14. O cliente `Backup`, correto em relação à abstração, quebra quando a implementação concreta varia. Saídas possíveis: tornar o limite parte explícita do contrato (ex.: uma operação `tamanhoMaximo()` ou outra abstração para destinos limitados) ou não usar essa classe como `Armazenamento`.
- **C) ❌** — Espalhar `instanceof` e casts no cliente esconde a violação e recria o acoplamento que a abstração deveria eliminar. Cada novo destino limitado exigiria editar o `Backup`. A apostila só aceita `instanceof` "quando a distinção de tipo fizer parte do problema e não houver abstração comportamental melhor".
- **D) ❌** — Além de errar o diagnóstico, nem compila: um método que implementa um método de interface não pode reduzir a visibilidade (testado: _"attempting to assign weaker access privileges; was public"_).

**Base no material:** p. 14: "Uma assinatura compatível não basta. Um subtipo que lança exceção para entradas aceitas pelo tipo base, exige uma pré-condição mais forte ou retorna algo fora da pós-condição pode quebrar o cliente. A análise de Liskov e Wing é uma disciplina de revisão: o sistema deve continuar correto quando a implementação concreta variar [4]" e "Use `instanceof` e casts quando a distinção de tipo fizer parte do problema e não houver abstração comportamental melhor". Glossário p. 6: "Subtipo — Tipo cujas instâncias podem substituir as do tipo base sem quebrar expectativas".
**Conceito-chave para a prova:** um subtipo **não pode** fortalecer pré-condições, enfraquecer pós-condições ou lançar exceções novas para entradas válidas do tipo base (LSP). Compilar não prova substituibilidade. `instanceof` em série no cliente é sintoma de abstração mal definida.

---

## I9 — UML: visibilidade e o que o diagrama de classes (não) modela
**Subtópico coberto:** Tópico 6, §5.1.1 "O que um diagrama de classes modela" (apostila p. 14).
**Por que é provável:** é a seção de abertura do Tópico 6 e tem conteúdo objetivo (símbolos `+ - # ~`, visão estrutural x algoritmo). Q3 cobra só multiplicidade e composição.
**Prioridade:** Média
**Tipo ENADE:** Resposta única

**Enunciado:**

QUESTÃO I9 · QUESTÃO INFERIDA NO ESTILO ENADE

CONTEXTUALIZAÇÃO (situação-problema)
Um diagrama de classes UML representa uma visão estrutural do sistema: classificadores, atributos, operações, generalizações, associações, dependências e restrições. Uma equipe recebeu o diagrama de projeto abaixo e precisa implementá-lo em Java. Um integrante sugere ainda gerar automaticamente todo o código, inclusive o cálculo do total, a partir do diagrama.

COMANDO
Considerando a notação de visibilidade da UML, sua correspondência com os modificadores de acesso de Java e o alcance de um diagrama de classes, assinale a alternativa tecnicamente adequada:

CENÁRIO (dados de suporte): **Como traduzir as visibilidades do diagrama para Java?**
```text
+---------------------------------------------------+
|                      Pedido                       |
+---------------------------------------------------+
| - numero: String                                  |
| # itens: List<ItemPedido>                         |
| ~ dataCriacao: LocalDate                          |
+---------------------------------------------------+
| + adicionarItem(produto: Produto, qtd: int): void |
| + total(): long                                   |
| - validarQuantidade(qtd: int): void               |
+---------------------------------------------------+
```

Qual alternativa é tecnicamente adequada?

**Alternativas:**
- **A)** `numero` e `validarQuantidade` são `private`; `itens` é `protected`; `dataCriacao` é declarado sem modificador (acesso de pacote); `adicionarItem` e `total` são `public`. O diagrama descreve a estrutura estática da classe, mas não especifica o algoritmo de `total()` nem a sequência de chamadas.
- **B)** `numero` e `validarQuantidade` são `private`; `itens` tem acesso de pacote; `dataCriacao` é `protected`; `adicionarItem` e `total` são `public`. Por ser um diagrama de projeto, ele especifica completamente o algoritmo de `total()`, o que permite gerar o código sem ambiguidade.
- **C)** `numero` e `validarQuantidade` são `protected`; `itens` é `private`; o símbolo `~` indica que `dataCriacao` é `static`; `adicionarItem` e `total` são `public`. O diagrama substitui os testes, pois as visibilidades garantem as invariantes de `Pedido`.
- **D)** `numero` e `validarQuantidade` são `private`; `itens` é `protected`; o símbolo `~` indica que `dataCriacao` é `final` (constante); `adicionarItem` e `total` são `public`. O diagrama de classes também representa a ordem das mensagens trocadas entre os objetos ao calcular o total.

**Gabarito: A**

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — Notação: `+` público, `-` privado, `#` protegido, `~` pacote. Em Java, o acesso de pacote é a **ausência** de modificador. O diagrama de classes é "um modelo de comunicação e análise, não uma especificação completa de algoritmos, sequência de chamadas ou código gerado automaticamente".
- **B) ❌** — Troca `#` com `~`. E o diagrama de projeto pode se aproximar das assinaturas do código, mas não define o algoritmo de `total()`.
- **C) ❌** — Inverte `-` e `#`. Em UML, `static` é indicado por **sublinhado**, não por `~`. Visibilidade não garante invariantes nem substitui testes (p. 11 e §5.1.5, p. 15).
- **D) ❌** — `~` é visibilidade de pacote, não `final`. A ordem das mensagens é assunto do diagrama de **sequência** (comportamental), não do diagrama de classes (estrutural).

**Base no material:** p. 14: "Um diagrama de classes UML representa uma visão estrutural: classificadores, atributos, operações, generalizações, associações, dependências e restrições. Ele é um modelo de comunicação e análise, não uma especificação completa de algoritmos, sequência de chamadas ou código gerado automaticamente [5] [17]" e "Os sinais de visibilidade costumam ser + para público, - para privado, # para protegido e ~ para visibilidade de pacote. Um diagrama de análise pode omitir detalhes de implementação; um diagrama de projeto pode aproximar-se das assinaturas do código".
**Conceito-chave para a prova:** `+` public · `-` private · `#` protected · `~` pacote (sem modificador em Java). Diagrama de classes = estrutura estática, sem algoritmo nem sequência de mensagens. `protected` em Java = pacote + subclasses.

---

## I10 — Classe de associação e regras além da multiplicidade (biblioteca)
**Subtópico coberto:** Tópico 6, §5.1.4 "Classe de associação" (apostila p. 15) e §7.4 "Integração 4 — Biblioteca e classe de associação" (p. 22).
**Por que é provável:** a apostila tem um exemplo integrador inteiro com as regras prontas (Leitor, Livro, Exemplar, Empréstimo), num formato muito parecido com o cenário de Q3 (tabela de regras de negócio → alternativa de modelagem). A Atividade 3 (Q10, discursiva) cobra o mesmo raciocínio. É o subtópico de UML mais destacado que ainda não tem questão objetiva.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única (tradução de regras de negócio para UML)

**Enunciado:**

QUESTÃO I10 · QUESTÃO INFERIDA NO ESTILO ENADE

CONTEXTUALIZAÇÃO (situação-problema)
A tradução de regras de negócio para o diagrama de classes exige decidir quando um relacionamento deixa de ser uma simples linha e passa a ter dados próprios, e reconhecer quais regras a multiplicidade consegue ou não expressar. Uma biblioteca universitária contratou o desenvolvimento de seu sistema de empréstimos com as regras abaixo.

COMANDO
Considerando a correspondência entre o modelo UML e as regras de negócio, o conceito de classe de associação e as limitações das multiplicidades, assinale a alternativa que apresenta a modelagem tecnicamente adequada:

CENÁRIO (dados de suporte): **Como modelar o empréstimo e garantir a regra R5?**

| Regra | Descrição |
|---|---|
| R1 | Um empréstimo é feito por exatamente um leitor; um leitor pode ter zero ou muitos empréstimos. |
| R2 | Cada empréstimo envolve exatamente um exemplar. |
| R3 | Um exemplar pertence a exatamente um livro; um livro pode ter um ou muitos exemplares. |
| R4 | Cada empréstimo registra data de retirada, data prevista, data de devolução e situação (ativo/encerrado). |
| R5 | Um exemplar não pode estar em dois empréstimos **ativos** ao mesmo tempo, mas o sistema guarda o histórico de todos os empréstimos já feitos com ele. |

Qual alternativa é tecnicamente adequada?

**Alternativas:**
- **A)** Modelar `Emprestimo` como classe com datas e situação e colocar a multiplicidade `0..1` no extremo `Emprestimo`, a partir de `Exemplar`. Assim, a própria multiplicidade garante R5, dispensando restrições adicionais.
- **B)** Modelar `Emprestimo` como classe explícita (classe de associação), pois o vínculo tem dados próprios (R4): `1` Leitor e `1` Exemplar por empréstimo, `0..*` empréstimos por leitor e por exemplar, `1` Livro por exemplar e `1..*` exemplares por livro. R5 depende de estado e datas e exige restrição adicional (OCL, consulta, teste ou regra de persistência).
- **C)** Modelar `Emprestimo` como subclasse de `Exemplar`, pois todo empréstimo é um exemplar em determinada situação. Com a herança simples do Java, cada exemplar só pode ser estendido por um empréstimo, o que garante R5.
- **D)** Modelar uma composição `Leitor ◆— Emprestimo` com multiplicidade `1` no lado de `Exemplar`. Como a composição implica parte exclusiva, a UML garante automaticamente que um exemplar não participe de dois empréstimos ativos.

**Gabarito: B**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — É a pegadinha principal. `0..1` empréstimo por exemplar proíbe o **histórico** exigido em R5: um exemplar teria no máximo um empréstimo na vida. A regra real ("no máximo um **ativo**") depende de estado e data, e cardinalidade simples não a expressa (p. 22).
- **B) ✅** — R4 dá dados próprios ao vínculo, então ele "vira uma classe" (p. 15, 22). Multiplicidades lidas a partir da instância oposta: cada `Emprestimo` → 1 `Leitor` e 1 `Exemplar`; cada `Leitor` → 0..* empréstimos; cada `Exemplar` → 0..* empréstimos (histórico) e 1 `Livro`; cada `Livro` → 1..* exemplares. R5 vai numa restrição, por exemplo em OCL: `context Exemplar inv umAtivo: self.emprestimos->select(e | e.situacao = Situacao::ATIVO)->size() <= 1`, ou num índice único parcial no banco, ou numa validação em `emprestar()` coberta por testes.
- **C) ❌** — Empréstimo não "é um" exemplar: é um **vínculo** entre leitor e exemplar. A herança simples restringe superclasses, não quantos objetos se relacionam com um exemplar.
- **D) ❌** — A composição põe o losango no lado do todo e diz que a **parte** (empréstimo) pertence a um único composto. Não controla quantos empréstimos ativos um exemplar tem. E `1` no lado de `Exemplar` é a leitura de R2, não uma garantia de R5. Usar composição sem invariante de domínio que a justifique fere a "menor semântica suficiente" (p. 16).

**Base no material:** p. 15: "Quando o relacionamento tem dados próprios, a linha pode virar uma classe. 'Aluno cursa disciplina' pode exigir semestre, nota, frequencia e situacao; nesse caso, `Matricula` representa o vínculo". p. 22: regras da Integração 4 e "A última regra não cabe apenas em multiplicidades simples porque depende do estado ativo e da data de devolução. Ela deve ser expressa por uma restrição adicional, por contrato, consulta, teste ou regra de persistência. `Emprestimo` pode ser uma classe explícita porque o relacionamento possui datas e estado próprios".
**Conceito-chave para a prova:** relacionamento com atributos próprios → classe de associação/explícita (`Matricula`, `Emprestimo`). Multiplicidade só limita a contagem. Regras que dependem de estado, tempo ou combinação de valores pedem OCL, restrição de banco, contrato ou teste.

---

## I11 — Cardinalidade não é unicidade: limites da UML (asserção-razão)
**Subtópico coberto:** Tópico 6, §5.1.2 (parágrafo final sobre ordem e unicidade), §5.1.4 (unicidade composta de `Matricula`) e §5.1.5 "Limitações da UML" (apostila p. 15).
**Por que é provável:** a apostila repete em três lugares que a cardinalidade não informa ordem, duplicidade, ciclo de vida ou temporalidade. O caso `Matricula` (mesma combinação aluno–disciplina no mesmo semestre) é dado como exemplo explícito, e o checklist final pede "cardinalidade foi separada de ordem, unicidade e navegabilidade" (p. 24). O tema rende bem uma asserção-razão.
**Prioridade:** Média
**Tipo ENADE:** Asserção-razão (adaptado para 4 alternativas)

**Enunciado:**

QUESTÃO I11 · QUESTÃO INFERIDA NO ESTILO ENADE

CONTEXTUALIZAÇÃO (situação-problema)
Em uma plataforma de cursos, a equipe modelou `Matricula` como classe de associação entre `Aluno` e `Disciplina`, com os atributos `semestre`, `nota`, `frequencia` e `situacao`, e multiplicidade `0..*` nos dois extremos. Na implementação em Java, a coleção de matrículas de cada aluno foi declarada como `List<Matricula>`. Pouco depois, o sistema registrou duas matrículas do mesmo aluno na mesma disciplina no semestre 2026.1.

COMANDO
Considerando as limitações da multiplicidade UML e a separação entre cardinalidade, ordem e unicidade, avalie as asserções a seguir e a relação proposta entre elas.

I. No modelo descrito, as multiplicidades, sozinhas, não impedem que o mesmo aluno seja matriculado duas vezes na mesma disciplina no mesmo semestre.

**PORQUE**

II. A multiplicidade expressa apenas um intervalo inclusivo de cardinalidade e não informa automaticamente ordem, unicidade, ciclo de vida ou temporalidade. Uma unicidade composta exige restrição adicional, como uma invariante OCL, uma restrição `UNIQUE` no banco ou uma validação no código.

A respeito dessas asserções, assinale a opção correta.

**Alternativas:**
- **A)** As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
- **B)** As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
- **C)** A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
- **D)** A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.

**Gabarito: A**

**Julgamento:**
- **Asserção I — Verdadeira.** É o caso citado pela própria apostila: "A multiplicidade 0..* dos dois lados não garante que a mesma combinação aluno-disciplina possa ocorrer duas vezes no mesmo semestre" (p. 15). Na implementação, `List` normalmente aceita duplicatas, o que reforça o problema.
- **Asserção II — Verdadeira.** "A multiplicidade é um intervalo inclusivo de cardinalidade" (p. 14). "A cardinalidade não informa automaticamente ordem, duplicidade, ciclo de vida ou temporalidade [...] ordered e unique são propriedades separadas" (p. 15). "Essa unicidade composta exige uma restrição adicional" (p. 15).
- **Relação — II justifica I.** I acontece justamente porque a multiplicidade só limita contagens, e a unicidade da tripla (aluno, disciplina, semestre) é outra propriedade.

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — As duas são verdadeiras e II explica I.
- **B) ❌** — II é exatamente a causa de I.
- **C) ❌** — II é verdadeira, e é o texto da apostila.
- **D) ❌** — I é verdadeira. Seria falsa só se houvesse uma restrição `{unique}` composta ou OCL, e o enunciado não traz nenhuma.

**Base no material:** p. 15 (§5.1.2, parágrafo final; §5.1.4; §5.1.5: "Mesmo com multiplicidades preenchidas, podem faltar invariantes, pré-condições, pós-condições, autorização, concorrência, temporalidade e decisões de persistência"). p. 15: "Em Java, `Set` evita duplicatas segundo seu contrato; `List` é ordenada e normalmente permite duplicatas".
**Conceito-chave para a prova:** cardinalidade ≠ ordem (`{ordered}`) ≠ unicidade (`{unique}`) ≠ temporalidade. `0..*` pode ser `Set`, `List` ou `Bag`. Unicidade composta se garante com OCL (`forAll(m1, m2 | m1 <> m2 implies ...)`), `UNIQUE(aluno_id, disciplina_id, semestre)` ou validação na operação de matrícula. Um `Set` com `equals`/`hashCode` sobre a tripla ajuda em memória, mas não substitui a restrição persistente.

---

## I12 — Associação, agregação ou composição? (Carrinho, Item e Produto)
**Subtópico coberto:** Tópico 7, §5.2.1 "Associação", §5.2.2 "Agregação compartilhada" e §5.2.3 "Composição" (apostila p. 15–16), com o exemplo de §7.1 "Integração 1 — Carrinho, composição e Strategy" (p. 20–21).
**Por que é provável:** o Tópico 7 tem tabela-resumo (Relação / Semântica mínima / Pergunta de decisão / Cuidado), um quadro "Regra editorial" ("Use a menor semântica suficiente") e a advertência "Composição UML não é sinônimo de classe interna, de `new` dentro do construtor ou de destrutor Java". Q3 cobra só a notação num caso pronto. Decidir a relação a partir do código, e não do desenho, ainda não tem questão.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única (código → modelo UML)

**Enunciado:**

QUESTÃO I12 · QUESTÃO INFERIDA NO ESTILO ENADE

CONTEXTUALIZAÇÃO (situação-problema)
Associação, agregação e composição expressam semânticas diferentes. Escolher a relação mais forte por hábito reduz a precisão do modelo. Em uma loja virtual, um carrinho contém linhas de compra e cada linha referencia um produto do catálogo. As regras de domínio são: (1) cada linha de compra (`Item`) é criada pelo carrinho, pertence a um único carrinho e é descartada com ele; (2) o mesmo `Produto` aparece em vários carrinhos e continua existindo no catálogo independentemente de qualquer carrinho.

COMANDO
Considerando a semântica mínima de cada relação UML e o princípio de usar a menor semântica suficiente, assinale a alternativa que representa corretamente as relações do código no diagrama de classes:

CENÁRIO (dados de suporte): **Que relação UML cada referência representa?**
```java
public record Produto(String sku, long precoCentavos) {}

public final class Item {
    private final Produto produto;
    private final int quantidade;

    public Item(Produto produto, int quantidade) {
        this.produto = java.util.Objects.requireNonNull(produto);
        if (quantidade <= 0) throw new IllegalArgumentException("quantidade inválida");
        this.quantidade = quantidade;
    }

    public long subtotal() { return produto.precoCentavos() * quantidade; }
}

public final class Carrinho {
    private final java.util.List<Item> itens = new java.util.ArrayList<>();

    public void adicionar(Produto produto, int quantidade) {
        itens.add(new Item(produto, quantidade));
    }

    public long total() {
        return itens.stream().mapToLong(Item::subtotal).sum();
    }
}
```

Qual alternativa é tecnicamente adequada?

**Alternativas:**
- **A)** Composição `Carrinho ◆— Item` e composição `Item ◆— Produto`, pois as duas referências são campos `private final` atribuídos na criação. Em Java, criar ou receber o objeto no construtor é o que define a composição UML.
- **B)** Agregação `Carrinho ◇— Item` e composição `Produto ◆— Item`, com o losango preenchido em `Produto`, pois o produto controla a existência das linhas de compra que o referenciam em diferentes carrinhos.
- **C)** Composição `Carrinho ◆— Item` (losango preenchido no `Carrinho`), porque cada linha pertence a um único carrinho e depende dele; associação simples `Item → Produto` (1 produto por item), porque o produto existe de forma independente. A composição decorre da regra de domínio, não do uso de `new`.
- **D)** Apenas associações simples entre todas as classes, pois Java não possui destrutores e a coleta de lixo impede que um objeto controle o ciclo de vida de outro. Logo, a composição UML não pode ser usada em modelos implementados em Java.

**Gabarito: C**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Usa o código, e não o domínio, como critério. "Composição UML não é sinônimo de classe interna, de `new` dentro do construtor ou de destrutor Java" (p. 16). `Produto` é compartilhado por vários itens e carrinhos e existe sozinho, então não pode ser parte exclusiva de um `Item`.
- **B) ❌** — Põe o losango no lado errado e inverte o todo e a parte. O produto não controla a existência dos itens. Além disso, a agregação (losango vazio) entre Carrinho e Item subestima a regra (1), que é de exclusividade e dependência, ou seja, composição.
- **C) ✅** — A regra (1) dá exclusividade (o item pertence a no máximo um carrinho) e dependência estrutural, o que justifica a composição, com o losango preenchido no **todo** (`Carrinho`, multiplicidade 1; `Item` 0..*). A regra (2) diz que o produto existe de modo independente, então basta uma associação (`Item` → exatamente 1 `Produto`; `Produto` ← 0..* itens). É a leitura da própria apostila: "Carrinho pode compor Item se as linhas tiverem identidade dependente daquele carrinho; Produto permanece associado porque existe de modo independente" (p. 21). Teste: o mesmo `Produto` em dois carrinhos dá totais `700` e `350`, cada um com seus próprios itens.
- **D) ❌** — A coleta de lixo "não traduz automaticamente todas as decisões de ciclo de vida UML" (p. 16), mas isso não impede modelar composição. A composição é um invariante de domínio (exclusividade e dependência), implementado com encapsulamento: o carrinho cria os itens e não os expõe nem compartilha.

**⚠️ Atenção (material):** na Figura 4 da apostila (p. 15, "Modelo estrutural de vendas"), o losango preenchido entre `Pedido` e `ItemPedido` está desenhado **encostado em `ItemPedido`**, a parte. Isso contradiz o texto da própria apostila ("O diamante preto fica no extremo do conjunto", p. 16) e os slides de Q3 (p. 18). Na prova, vale a regra: losango no **todo**.

**Base no material:** p. 15–16: "Associação é o relacionamento estrutural geral [...] a presença de um campo não determina sozinha a semântica do domínio"; "Agregação é uma intenção de relação conjunto–parte fraca [...] Se a informação conjunto–parte não for necessária, uma associação simples é mais precisa"; "Composição é uma agregação forte. A parte pertence a no máximo um composto por vez [...] O diamante preto fica no extremo do conjunto"; quadro "Regra editorial: Use a menor semântica suficiente". p. 21: análise de Carrinho/Item/Produto.
**Conceito-chave para a prova:** associação = usa/conhece. Agregação (◇) = conjunto–parte fraco, a parte pode ser compartilhada ou sobreviver. Composição (◆ no todo) = parte exclusiva e estruturalmente dependente. Decida pela **regra de domínio**, nunca por `new`, `final` ou classe interna. Na dúvida, use a menor semântica suficiente.

---

## I13 — Testando o modelo com instâncias válidas e inválidas (Pedido)
**Subtópico coberto:** §7.2 "Integração 2 — Pedido, UML e invariantes", com a tabela de instâncias p1–p4, c2 e i5 (apostila p. 21–22). Também §5.1.3 "Procedimento de modelagem", passo 6: "Teste o diagrama com instâncias mínimas, máximas e inválidas" (p. 15), e a Figura 4 (p. 15).
**Por que é provável:** a apostila traz uma tabela resolvida de instâncias (válida/inválida + motivo), material pronto para uma questão de análise. Q3 traduz regras em multiplicidades, mas não testa instâncias.
**Prioridade:** Média
**Tipo ENADE:** Afirmativas múltiplas / análise de instâncias (4 alternativas)

**Enunciado:**

QUESTÃO I13 · QUESTÃO INFERIDA NO ESTILO ENADE

CONTEXTUALIZAÇÃO (situação-problema)
Um modo de validar um diagrama de classes é testá-lo com instâncias mínimas, máximas e inválidas antes da implementação. Para um sistema de vendas, foram definidas as regras: cada pedido tem exatamente um cliente; um cliente pode ter zero ou muitos pedidos; cada pedido contém um ou muitos itens, em composição (cada item pertence a um único pedido); cada item referencia exatamente um produto, e um produto pode ser referenciado por zero ou muitos itens.

COMANDO
Considerando as multiplicidades e a semântica de composição do modelo, avalie as instâncias a seguir e assinale a alternativa que indica **todas e somente** as que **violam** o modelo.

CENÁRIO (dados de suporte): **Quais instâncias o modelo deve rejeitar?**

I. O cliente `c2` está cadastrado sem nenhum pedido.
II. O pedido `p3` contém o item `i7`, mas não está associado a nenhum cliente.
III. O pedido `p4` está associado ao cliente `c1`, mas não contém nenhum item.
IV. O item `i5` está contido, ao mesmo tempo, nos pedidos `p5` e `p6`.
V. O produto `x1` é referenciado por itens de três pedidos diferentes.

**Alternativas:**
- **A)** I e V, apenas.
- **B)** II e III, apenas.
- **C)** II, III e V, apenas.
- **D)** II, III e IV, apenas.

**Gabarito: D**

**Julgamento das instâncias:**
- **I — Válida.** Cliente → `0..*` pedidos permite coleção vazia (na apostila, `c2`: "0..* permite coleção vazia").
- **II — Inválida.** O extremo do cliente exige exatamente `1` (`p3`: "O extremo do cliente exige 1").
- **III — Inválida.** Pedido → `1..*` itens: um pedido sem itens viola o mínimo (`p4`).
- **IV — Inválida.** Na composição, a parte não pode ter dois contêineres (`i5`: "Parte composita não possui dois contêineres").
- **V — Válida.** `Produto` está apenas **associado** a `Item` (0..* itens por produto), então pode ser referenciado por itens de vários pedidos. Confundir essa associação com composição é a pegadinha.

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Marca justamente as duas instâncias válidas.
- **B) ❌** — Omite IV, a violação da exclusividade da composição.
- **C) ❌** — Inclui V (associação confundida com composição) e omite IV.
- **D) ✅** — II, III e IV violam, respectivamente, a multiplicidade `1` do cliente, a multiplicidade `1..*` dos itens e a exclusividade da parte na composição.

**Base no material:** p. 21: "Um caso mínimo válido é um pedido com um cliente e um item. Um pedido sem itens viola 1..*; um item compartilhado por dois pedidos viola a composição quando a regra de domínio exigir parte exclusiva". Tabela p. 22 (p1, p2, c2 válidas; p3, p4, i5 inválidas). p. 22: "A multiplicidade deve virar uma responsabilidade de objetos [...] operações como `adicionarItem` e `removerItem` precisam preservar limites, unicidade e consistência dos dois lados".
**Conceito-chave para a prova:** leia cada multiplicidade a partir de **uma** instância do lado oposto e teste os limites: 0 (vazio permitido?), 1 (obrigatório?), parte compartilhada (composição?). Associação permite compartilhamento; composição não.

---

## I14 — Classificação e custos dos padrões GoF (associação)
**Subtópico coberto:** Tópico 8, §6.1.1 "Como ler um padrão" (23 padrões em três grupos; padrão não é biblioteca pronta) e §6.1.5 "Comparação dos três padrões", tabela Categoria / Problema / Benefício / Custo (apostila p. 16–17 e 20). Também o slide p. 23 ("Diferença rápida: Strategy [...] Factory Method [...] Observer [...] Singleton").
**Por que é provável:** o OBJ-4 da Matriz é "classificação e aplicação de padrões GoF, com destaque para Observer, Mediator e Singleton" (p. 5). A apostila fecha o tópico com uma tabela comparativa, e o slide de Q4 traz uma "diferença rápida" entre padrões. Nenhuma questão conhecida cobra a classificação diretamente.
**Prioridade:** Alta
**Tipo ENADE:** Associação (4 alternativas)

**Enunciado:**

QUESTÃO I14 · QUESTÃO INFERIDA NO ESTILO ENADE

CONTEXTUALIZAÇÃO (situação-problema)
Um padrão GoF é uma solução nomeada para um problema recorrente num contexto. Não é uma biblioteca pronta, um framework ou uma receita obrigatória. O catálogo clássico reúne 23 padrões em três grupos (criacionais, estruturais e comportamentais), e cada padrão comunica intenção, participantes, consequências e custos.

COMANDO
Associe cada padrão da coluna 1 à sua descrição na coluna 2, considerando a categoria, a intenção e o custo típico de cada um.

CENÁRIO (dados de suporte): **Qual problema cada padrão resolve, e a que custo?**

| Coluna 1 — Padrão | Coluna 2 — Descrição |
|---|---|
| 1. Observer | ( ) Padrão criacional que controla a criação de uma única instância em um escopo definido. Custo típico: estado global, dependências ocultas e testes difíceis. |
| 2. Mediator | ( ) Padrão comportamental que centraliza a colaboração entre componentes que, de outro modo, manteriam uma teia de referências cruzadas. Custo típico: o coordenador pode crescer demais. |
| 3. Singleton | ( ) Padrão comportamental que estabelece uma dependência um-para-muitos com inscrição e notificação. Custo típico: fluxo oculto e gestão de inscrições, ordem e falhas. |
| 4. Strategy | ( ) Padrão comportamental que encapsula algoritmos intercambiáveis atrás de uma interface comum, recebidos pelo contexto por composição. |

A sequência correta, de cima para baixo, é:

**Alternativas:**
- **A)** 1 – 2 – 3 – 4.
- **B)** 3 – 1 – 2 – 4.
- **C)** 4 – 2 – 1 – 3.
- **D)** 3 – 2 – 1 – 4.

**Gabarito: D**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Mantém a ordem da coluna 1. Classifica Observer como criacional e Singleton como notificação um-para-muitos.
- **B) ❌** — Troca Observer com Mediator, a confusão mais comum: Observer **notifica** receptores variáveis; Mediator **coordena** colegas conhecidos.
- **C) ❌** — Chama Strategy de criacional de instância única e Singleton de "algoritmos intercambiáveis".
- **D) ✅** — Singleton (3) é **criacional** e controla a unicidade num escopo real, ao custo de estado global, testes difíceis e dependências ocultas. Mediator (2) é **comportamental**: os colegas deixam de manter uma teia de referências, mas o mediador pode crescer demais. Observer (1) é **comportamental**, com dependência um-para-muitos com inscrição e notificação, ao custo de fluxo oculto, inscrições, ordem e falhas. Strategy (4) é **comportamental**, com algoritmos intercambiáveis por interface e composição (Q4).

**Base no material:** p. 16–17: "O catálogo clássico reúne 23 padrões em três grupos: criacionais, estruturais e comportamentais [6]. Um padrão não é biblioteca pronta, framework nem receita obrigatória [...] Singleton é criacional: controla a criação de uma instância em um escopo. Observer é comportamental: estabelece uma dependência um-para-muitos com inscrição e notificação. Mediator é comportamental: centraliza a coordenação entre componentes que poderiam manter muitas referências cruzadas". Tabela §6.1.5 (p. 20). Slide p. 23: "Strategy = algoritmos intercambiáveis (comportamental) · Factory Method = quem cria o objeto (criacional) · Observer = notificação um-para-muitos · Singleton = instância única (criacional)".
**Conceito-chave para a prova:** **criacionais**: Singleton, Factory Method. **Comportamentais**: Observer, Mediator, Strategy, Template Method. Todo padrão tem um **custo permanente**, e a apostila exige justificá-lo antes de aplicar.

---

## I15 — Observer: notificação, cancelamento de inscrição e cópia da lista
**Subtópico coberto:** Tópico 8, §6.1.2 "Observer — notificação extensível" (apostila p. 17–18).
**Por que é provável:** a apostila traz código completo (`PriceChanged`, `PriceObserver`, `ProductCatalog`) e comentários fáceis de cobrar: a cópia da lista durante a notificação, o publicador que conhece só o contrato, `java.util.Observable` depreciada e "Observer não garante por si só ordenação, entrega exatamente uma vez, persistência ou transação". Observer só aparece como distrator em Q4.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única (interpretação de código + avaliação de projeto)

**Enunciado:**

QUESTÃO I15 · QUESTÃO INFERIDA NO ESTILO ENADE

CONTEXTUALIZAÇÃO (situação-problema)
Um catálogo de produtos precisa avisar vários interessados quando um preço muda, como cache, interface e auditoria, sem conhecer suas classes concretas. Um dos interessados é um alerta de uso único, que cancela a própria inscrição após o primeiro aviso. A equipe quer saber se a remoção durante a notificação compromete a entrega aos demais observadores.

COMANDO
Considerando a intenção do padrão Observer e os cuidados de implementação apontados para ele, avalie a saída do programa e as garantias oferecidas pela solução. Assinale a alternativa tecnicamente adequada:

CENÁRIO (dados de suporte): **O que é impresso quando o preço muda duas vezes?**
```java
import java.util.*;

record PriceChanged(String sku, long oldCents, long newCents) {}

interface PriceObserver {
    void onPriceChanged(PriceChanged event);
}

final class ProductCatalog {
    private final Map<String, Long> prices = new HashMap<>();
    private final List<PriceObserver> observers = new ArrayList<>();

    public void subscribe(PriceObserver observer) {
        observers.add(Objects.requireNonNull(observer));
    }

    public void unsubscribe(PriceObserver observer) {
        observers.remove(observer);
    }

    public void changePrice(String sku, long newCents) {
        long old = prices.getOrDefault(sku, 0L);
        prices.put(sku, newCents);
        PriceChanged event = new PriceChanged(sku, old, newCents);
        for (PriceObserver observer : List.copyOf(observers))
            observer.onPriceChanged(event);
    }
}

final class AlertaUnico implements PriceObserver {
    private final ProductCatalog catalogo;
    AlertaUnico(ProductCatalog catalogo) { this.catalogo = catalogo; }

    @Override
    public void onPriceChanged(PriceChanged e) {
        System.out.println("alerta " + e.sku());
        catalogo.unsubscribe(this); // cancela a própria inscrição após o 1º aviso
    }
}

public class Main {
    public static void main(String[] args) {
        ProductCatalog catalogo = new ProductCatalog();
        catalogo.subscribe(new AlertaUnico(catalogo));
        catalogo.subscribe(e -> System.out.println("cache " + e.oldCents() + "->" + e.newCents()));
        catalogo.changePrice("A1", 500);
        catalogo.changePrice("A1", 450);
    }
}
```

Qual alternativa é tecnicamente adequada?

**Alternativas:**
- **A)** Imprime `alerta A1`, `cache 0->500`, `alerta A1` e `cache 500->450`, pois, como a notificação percorre uma cópia da lista, a chamada a `unsubscribe` não tem efeito e o alerta continua inscrito nas mudanças seguintes.
- **B)** Imprime `alerta A1`, `cache 0->500` e `cache 500->450`. A cópia protege a iteração corrente contra a remoção feita pelo próprio observador, e o cancelamento vale para as notificações seguintes. O catálogo depende apenas do contrato `PriceObserver`, não das classes concretas.
- **C)** Lança `ConcurrentModificationException` na primeira chamada a `changePrice`, pois o observador remove a si mesmo da lista enquanto ela é percorrida. Por isso, observadores nunca devem cancelar a inscrição durante uma notificação.
- **D)** Imprime as mesmas linhas da alternativa B, e o padrão Observer, por si só, garante a ordem de entrega, a entrega exatamente uma vez e a persistência do evento, dispensando um contrato adicional de falhas e cancelamento.

**Gabarito: B**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — A cópia vale só para **aquela** iteração. `unsubscribe` remove o alerta da lista original, então na segunda mudança ele não é mais notificado.
- **B) ✅** — Executado em Java 21: `alerta A1` / `cache 0->500` / `cache 500->450`. Na primeira mudança, os dois observadores da cópia são notificados, e o alerta se remove da lista original. Na segunda, só o cache. O publicador conhece apenas a interface `PriceObserver` (o lambda é aceito porque ela é funcional), que é a essência do Observer.
- **C) ❌** — Com `List.copyOf`, a lista percorrida não é a lista alterada, então não há exceção. **Detalhe testado:** sem a cópia (`for (... : observers)`), também não há exceção neste caso, mas o observador `cache` é **pulado em silêncio** na primeira mudança. Saída: `alerta A1` e `cache 500->450`. O iterador do `ArrayList` encerra antes de checar a modificação, porque o tamanho caiu para 1. É por isso que a apostila manda copiar a lista.
- **D) ❌** — A saída está certa, mas a afirmação é falsa: "Observer não garante por si só ordenação, entrega exatamente uma vez, persistência ou transação" (p. 18). A ordem aqui é só a de inscrição numa `ArrayList`. O contrato precisa definir inscrição, cancelamento, transporte do evento, exceções e ciclo de vida.

**Base no material:** p. 17: "Observer define uma dependência de um-para-muitos. Quando um publicador muda ou registra um evento, os observadores inscritos podem reagir. O publicador conhece o contrato, não as classes concretas. O contrato deve dizer como inscrever, cancelar, transportar o evento, tratar exceções e encerrar o ciclo de vida". p. 18: "A cópia da lista evita que uma inscrição ou remoção durante a notificação altere a iteração corrente. Ainda é necessário decidir reentrância, concorrência, falhas e observadores que deixam de existir. `java.util.Observable` foi depreciada desde Java 9 [...] Observer não garante por si só ordenação, entrega exatamente uma vez, persistência ou transação".
**Conceito-chave para a prova:** Observer = um publicador para N observadores variáveis, que se inscrevem e cancelam em tempo de execução, sem que o publicador conheça as classes concretas. Itere sobre uma cópia. O padrão **não** garante ordem, entrega única nem transação. `java.util.Observable` está depreciada desde o Java 9.

---

## I16 — Mediator: teia de referências cruzadas em um formulário
**Subtópico coberto:** Tópico 8, §6.1.3 "Mediator — coordenação centralizada" (apostila p. 18–19) e §7.3 "Integração 3" (p. 22: "EmailField e SubmitButton conhecem o mediador, mas não conhecem um ao outro").
**Por que é provável:** Mediator é um dos três padrões destacados na Matriz (OBJ-4), tem código próprio (`FormMediator`, `Component`, `SubmitButton`, `RegistrationDialog`) e alertas explícitos (God Object; "Mediator não é simplesmente uma fachada"). É o único dos três padrões que não aparece nem como distrator nas questões conhecidas.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única (escolha de padrão + consequências)

**Enunciado:**

QUESTÃO I16 · QUESTÃO INFERIDA NO ESTILO ENADE

CONTEXTUALIZAÇÃO (situação-problema)
Na tela de cadastro de um sistema web, os componentes `EmailField`, `PasswordField` e `SubmitButton` colaboram entre si. O botão só pode ser habilitado quando o e-mail e a senha são válidos. Na implementação atual, cada componente guarda referências para os outros. Cada novo campo, como "confirmar senha" ou "aceite dos termos", obriga a alterar todas as classes existentes.

COMANDO
Considerando a necessidade de reduzir o acoplamento entre os componentes e de localizar a lógica de coordenação da tela, assinale a alternativa que apresenta o padrão adequado e uma consequência correta de sua aplicação:

CENÁRIO (dados de suporte): **Como eliminar a teia de referências entre os componentes da tela?**
```java
class EmailField {
    PasswordField senha;
    SubmitButton botao;
    private String valor = "";

    void alterado(String novo) {
        valor = novo;
        senha.habilitar(valido());
        botao.habilitar(valido() && senha.preenchida());
    }
    boolean valido() { return valor.contains("@"); }
}

class PasswordField {
    EmailField email;
    SubmitButton botao;
    private String valor = "";
    private boolean habilitado;

    void alterado(String novo) {
        valor = novo;
        botao.habilitar(email.valido() && preenchida());
    }
    void habilitar(boolean h) { habilitado = h; }
    boolean preenchida() { return !valor.isBlank(); }
}

class SubmitButton {
    EmailField email;
    PasswordField senha;
    private boolean habilitado;

    void habilitar(boolean h) { habilitado = h; }
    void click() {
        if (habilitado && email.valido() && senha.preenchida())
            System.out.println("registrar");
    }
}
```

Qual alternativa é tecnicamente adequada?

**Alternativas:**
- **A)** Aplicar o Mediator: um `RegistrationDialog` implementa `FormMediator`, e cada componente apenas notifica o mediador de que algo aconteceu, deixando de conhecer os colegas. A coordenação fica localizada, mas o mediador deve ser dividido por contexto e delegar regras de domínio para não virar um God Object.
- **B)** Aplicar o Observer: cada campo passa a ser um publicador e todos os demais se inscrevem em todos. A teia de referências cruzadas é substituída por inscrições recíprocas, sem nenhum componente central de coordenação.
- **C)** Aplicar o Singleton a cada componente da tela, com um `getInstance()` estático, para que qualquer campo acesse os demais globalmente sem guardar referências, o que reduz o acoplamento entre eles.
- **D)** Aplicar o Mediator entendido como simples Fachada: o mediador deve concentrar, além da coordenação da tela, todas as regras de domínio do cadastro (validação de CPF, persistência, envio de e-mail), eliminando os serviços especializados.

**Gabarito: A**

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — É a estrutura da apostila (p. 18–19): `interface FormMediator { void notify(Component sender, String event); }`, componentes que guardam só o mediador (`mediator.notify(this, "click")`) e um `RegistrationDialog` que decide quem reage. Uma versão com `EmailField` e `SubmitButton` foi compilada e testada: o botão só registra depois de um e-mail válido. Um novo campo passa a exigir mudança só no mediador. Custo apontado pela apostila: o mediador pode virar um God Object. Mitigação: dividir por contexto, usar eventos tipados em vez de strings e delegar regras de domínio.
- **B) ❌** — Inscrições recíprocas de todos em todos mantêm o acoplamento N×N, agora espalhado e oculto. Observer serve para receptores **variáveis** de uma mudança. Aqui os colegas do fluxo são conhecidos e precisam de **coordenação** (p. 22: "o mediador coordena os componentes conhecidos do fluxo; o publicador notifica receptores que podem variar").
- **C) ❌** — Singleton resolve unicidade num escopo, não coordenação. Acesso global esconde as dependências em vez de reduzi-las (p. 19) e impede ter duas telas de cadastro ao mesmo tempo.
- **D) ❌** — Erra duas vezes: "Mediator não é simplesmente uma fachada: a intenção é centralizar a colaboração entre colegas" (p. 19), e concentrar regras de domínio no mediador é justamente o risco de God Object que a apostila manda evitar.

**Base no material:** p. 18: "Mediator encapsula como um conjunto de objetos interage. Um componente sabe que algo aconteceu e notifica o mediador; não conhece [...] os colegas que serão acionados. Em uma tela, `EmailField`, `PasswordField` e `SubmitButton` podem colaborar por meio de `RegistrationMediator`". p. 19: "O benefício é localizar a coordenação. O risco é criar um God Object. Divida mediadores por contexto, use eventos tipados em vez de strings livres quando o sistema crescer e delegue regras de domínio a serviços ou objetos especializados. Mediator não é simplesmente uma fachada [...]". Tabela p. 20: "Componentes conhecem muitos colegas e a colaboração está espalhada? → Mediator → Coesão do mediador e risco de God Object".
**Conceito-chave para a prova:** Mediator = colegas conhecidos que hoje se referenciam mutuamente; a solução é que todos falem só com o mediador. Benefício: coordenação localizada. Custo: o mediador inchar (God Object). Não confunda com Observer (receptores variáveis) nem com Facade (simplificar a interface de um subsistema).

---

## I17 — Singleton com Holder: segurança, limites e custo do acesso global
**Subtópico coberto:** Tópico 8, §6.1.4 "Singleton — unicidade em escopo real" (apostila p. 19–20).
**Por que é provável:** a apostila traz o código do idioma Holder (`AppConfig`), afirmações técnicas precisas (inicialização de classe sincronizada pela especificação, criação tardia, `enum`, o que **não** se resolve) e a alternativa por injeção (`Service(Logger)`). A Atividade 1 (Q8, item 6, discursiva) pergunta se "Singleton é apenas uma forma elegante de escrever uma variável global". Singleton só aparece como distrator em Q4.
**Prioridade:** Alta
**Tipo ENADE:** Resposta única (interpretação de código + avaliação de projeto)

**Enunciado:**

QUESTÃO I17 · QUESTÃO INFERIDA NO ESTILO ENADE

CONTEXTUALIZAÇÃO (situação-problema)
Uma aplicação Java precisa de um único objeto de configuração por execução. O desenvolvedor implementou o Singleton abaixo com o idioma da classe interna (*Holder*). Na revisão, surgiram três dúvidas: se a implementação é segura com várias threads, se garante unicidade em qualquer situação e se é a melhor forma de oferecer a configuração aos serviços que precisam ser testados isoladamente.

COMANDO
Considerando a intenção do padrão Singleton, as garantias da linguagem Java sobre a inicialização de classes e os custos do acesso global, assinale a alternativa tecnicamente adequada:

CENÁRIO (dados de suporte): **O que o idioma Holder garante e o que ele não resolve?**
```java
public final class AppConfig {
    private AppConfig() {}

    private static class Holder {
        private static final AppConfig INSTANCE = new AppConfig();
    }

    public static AppConfig getInstance() {
        return Holder.INSTANCE;
    }
}
```

Qual alternativa é tecnicamente adequada?

**Alternativas:**
- **A)** O código não é seguro com várias threads, pois `getInstance()` não é `synchronized`: duas threads podem executar `new AppConfig()` ao mesmo tempo e obter instâncias diferentes. A correção obrigatória é o *double-checked locking*.
- **B)** A instância é criada assim que a classe `AppConfig` é carregada, mesmo que `getInstance()` nunca seja chamado. Em compensação, a técnica garante uma instância única universal, válida entre JVMs, carregadores de classe e processos distribuídos.
- **C)** O construtor privado é dispensável, pois a classe aninhada `Holder` já impede a criação de outras instâncias. Além disso, um `enum` não pode ser usado para implementar Singleton em Java, por não admitir construtores.
- **D)** A inicialização da classe `Holder` é sincronizada pela especificação da linguagem e só ocorre na primeira chamada de `getInstance()`, o que torna a criação tardia e segura entre threads. A técnica não resolve reflexão, múltiplos carregadores de classe nem unicidade distribuída, e o acesso global oculta dependências e dificulta testes.

**Gabarito: D**

**Por que cada alternativa está certa ou errada:**
- **A) ❌** — Não é preciso `synchronized`: a JVM inicializa a classe `Holder` uma única vez e de forma sincronizada. Teste com 100 tarefas em 8 threads: **1** instância e **1** execução do construtor.
- **B) ❌** — Erra as duas partes. A instância só é criada quando `Holder` é inicializado, na primeira chamada a `getInstance()` (teste: chamar outro método estático de `AppConfig` não cria a instância). E "uma instância" não vale entre JVMs, carregadores de classe ou processos distribuídos (p. 19).
- **C) ❌** — Sem o construtor privado, qualquer classe poderia fazer `new AppConfig()`. Um `enum` admite construtor (implicitamente privado), e a apostila diz que ele "pode ser adequado para um Singleton sem estado complexo".
- **D) ✅** — Reproduz as garantias e os limites da apostila: criação tardia e segura entre threads graças à inicialização de classe definida na JLS (cap. 12). Mas a técnica não resolve reflexão (teste: `getDeclaredConstructor().setAccessible(true)` criou uma **segunda** instância), class loaders múltiplos, ciclo de vida externo ou unicidade distribuída. O principal custo é o acesso global. Alternativa preferível: criar uma instância na composição da aplicação e injetá-la (`new Service(logger)`).

**Base no material:** p. 19: "Singleton controla a criação de uma única instância em um escopo definido. 'Uma instância' não significa uma instância universal para processos distribuídos, JVMs ou carregadores de classe diferentes. O padrão só é justificável quando criar instâncias adicionais causar dano real [...] A inicialização de classes em Java é sincronizada pela especificação; o padrão Holder aproveita essa garantia e adia a criação até a primeira chamada [23]. Um enum pode ser adequado [...]. Nenhuma dessas técnicas resolve automaticamente reflexão, múltiplos class loaders, ciclo de vida externo ou unicidade distribuída. O principal custo é o acesso global: dependências ficam ocultas, o estado pode persistir entre testes e a substituição por um dublê fica difícil". p. 20: `Service(Logger logger)` e "Há uma única instância no contexto, mas Service não precisa conhecer uma política global de criação".
**Conceito-chave para a prova:** Singleton é **criacional**: construtor privado + acesso estático (Holder ou `enum`). Holder = criação tardia e segura entre threads, sem `synchronized`. Unicidade só no escopo (JVM/class loader), e a reflexão a quebra. Custo: acesso global. Prefira uma instância única **injetada**. A unicidade precisa ser requisito real, não conveniência de acesso.

---

## I18 — Escolhendo o padrão pelo problema, sem decorar nomes (checkout)
**Subtópico coberto:** §6.2 "Como escolher um padrão sem decorar nomes", com a tabela de decisão Pergunta / Candidato / Verificação seguinte e a Figura 5, árvore "Que mudança precisa ser isolada?" (apostila p. 17 e 20). Também §7.3 "Integração 3 — Checkout com Mediator e Observer" (p. 22) e a Tese orientadora ("padrão GoF somente quando o problema justificar a estrutura adicional", p. 4).
**Por que é provável:** a apostila dá uma tabela de decisão pronta e um exemplo integrador que combina os três padrões do Tópico 8 com a opção "solução simples". É o formato de questão mais direto para o OBJ-4 ("classificação e aplicação de padrões"), no mesmo espírito de Q4 (descrever o problema e escolher o padrão).
**Prioridade:** Alta
**Tipo ENADE:** Resposta única (associação de requisitos a soluções)

**Enunciado:**

QUESTÃO I18 · QUESTÃO INFERIDA NO ESTILO ENADE

CONTEXTUALIZAÇÃO (situação-problema)
Antes de implementar um padrão de projeto, é recomendável descrever o problema em uma frase sem usar o nome do padrão e verificar se uma solução mais simples basta. A equipe de um módulo de checkout de comércio eletrônico levantou os quatro requisitos abaixo.

COMANDO
Considerando a intenção, o problema típico e o custo de cada alternativa, assinale a opção que associa corretamente cada requisito à solução mais adequada:

CENÁRIO (dados de suporte): **Que solução cada requisito pede?**

| Requisito | Descrição |
|---|---|
| (1) | Na tela de checkout, `EmailField`, `CupomField` e `SubmitButton` precisam colaborar (o botão só é habilitado quando e-mail e cupom são válidos). Hoje cada componente guarda referência para os demais. |
| (2) | Quando o preço de um produto muda, o cache, a interface e a auditoria precisam reagir. Novos receptores podem ser incluídos ou removidos em tempo de execução. |
| (3) | A configuração da aplicação (endereço do gateway de pagamento, tempos limite) deve ser única no contexto da aplicação, mas os serviços precisam ser testados isoladamente com configurações de teste. |
| (4) | O cálculo da taxa de embalagem é uma fórmula fixa, usada em um único ponto do sistema, sem variação prevista. |

Qual alternativa é tecnicamente adequada?

**Alternativas:**
- **A)** (1) Mediator; (2) Observer; (3) uma única instância criada na composição da aplicação e injetada nos serviços; (4) chamada direta, sem padrão, pois um padrão não traria benefício mensurável.
- **B)** (1) Observer; (2) Mediator; (3) Singleton com `getInstance()` chamado dentro de cada serviço; (4) Strategy, para permitir futuras variações da fórmula.
- **C)** (1) Mediator; (2) Singleton, para que haja um único preço global; (3) Observer, para notificar a configuração; (4) Mediator, para centralizar o cálculo.
- **D)** (1) Mediator; (2) Observer implementado com `java.util.Observable`, o modelo atual recomendado; (3) Singleton com acesso global; (4) Observer, para que a taxa seja notificada a cada pedido.

**Gabarito: A**

**Por que cada alternativa está certa ou errada:**
- **A) ✅** — (1) "Componentes conhecem muitos colegas e a colaboração está espalhada?" → **Mediator**. (2) "Muitos objetos precisam reagir a mudanças e o conjunto muda em tempo de execução?" → **Observer**. (3) "Deve existir uma única instância [...]?" → "Singleton **ou instância injetada**". Como os serviços precisam de testes isolados, a apostila prefere a instância criada na composição da aplicação e injetada (p. 20 e 22: "A configuração é criada na composição da aplicação e injetada, em vez de ser global por conveniência"). (4) "O problema pode ser resolvido com chamada direta ou dependência injetada?" → **solução simples**.
- **B) ❌** — Inverte Mediator e Observer em (1) e (2). Em (3), o acesso global atrapalha os testes isolados exigidos. Em (4), aplica Strategy a uma fórmula sem variação prevista, estrutura extra sem benefício mensurável.
- **C) ❌** — Singleton não notifica receptores (2), Observer não resolve unicidade (3) e Mediator não serve para isolar um cálculo único (4).
- **D) ❌** — Acerta (1) e o padrão de (2), mas indica `java.util.Observable`, depreciada desde o Java 9 (p. 18). (3) contraria o requisito de teste isolado, e (4) aplica um padrão sem problema que o justifique.

**Base no material:** p. 20, tabela de decisão: Observer ("Muitos objetos precisam reagir a mudanças e o conjunto muda em tempo de execução?"), Mediator ("Componentes conhecem muitos colegas e a colaboração está espalhada?"), Singleton ou instância injetada ("Deve existir uma única instância em um escopo explicitamente definido?"), Solução simples ("O problema pode ser resolvido com chamada direta ou dependência injetada? O padrão acrescentaria benefício mensurável?"). p. 22 (§7.3): `CheckoutDialog` como mediador, `ProductCatalog` conhecendo só `PriceObserver`, `CacheInvalidator` e `AuditListener` como assinantes, e a configuração injetada. p. 4: "padrão GoF somente quando o problema justificar a estrutura adicional".
**Conceito-chave para a prova:** primeiro descreva o problema sem o nome do padrão. Colegas conhecidos que precisam de coordenação → Mediator. Receptores variáveis de um evento → Observer. Unicidade real → Singleton, de preferência instância única **injetada**. Sem variação nem acoplamento a resolver → nenhum padrão.

---

## Quadro-resumo de gabaritos
| Questão | Subtópico (apostila) | Tipo | Gabarito |
|---|---|---|---|
| I1 | T1 §3.1.3 — `==` x `equals` x `hashCode` | Resposta única (código) | **B** |
| I2 | T1 §3.1.1–3.1.2 — contrato de `Conta` | Resposta única | **C** |
| I3 | T2 §3.2.2–3.2.3 — evolução de interface (`default`) | Resposta única | **D** |
| I4 | T3 §4.1.2–4.1.3 — vazamento da representação | Resposta única (código) | **C** |
| I5 | T4 §4.2.3 — conflito de `default` | Resposta única (código) | **A** |
| I6 | T4 §4.2.1–4.2.2 — sentidos de herança / construtores | Afirmativas múltiplas | **C** |
| I7 | T5 §4.3.1 — sobrecarga x sobrescrita x `static` | Resposta única (código) | **D** |
| I8 | T5 §4.3.2 — subtipagem comportamental (LSP) | Resposta única (código) | **B** |
| I9 | T6 §5.1.1 — visibilidade UML | Resposta única | **A** |
| I10 | T6 §5.1.4 / §7.4 — classe de associação (biblioteca) | Resposta única | **B** |
| I11 | T6 §5.1.4–5.1.5 — cardinalidade ≠ unicidade | Asserção-razão | **A** |
| I12 | T7 §5.2 / §7.1 — associação x agregação x composição | Resposta única (código) | **C** |
| I13 | §7.2 / §5.1.3 — instâncias válidas e inválidas | Análise de instâncias | **D** |
| I14 | T8 §6.1.1 / §6.1.5 — classificação GoF | Associação | **D** |
| I15 | T8 §6.1.2 — Observer | Resposta única (código) | **B** |
| I16 | T8 §6.1.3 — Mediator | Resposta única (código) | **A** |
| I17 | T8 §6.1.4 — Singleton (Holder) | Resposta única (código) | **D** |
| I18 | T8 §6.2 / §7.3 — escolha de padrão (checkout) | Resposta única | **A** |

Distribuição: **A = 5 · B = 4 · C = 4 · D = 5** (18 questões).
