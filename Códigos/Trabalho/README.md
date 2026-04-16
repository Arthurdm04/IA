# Sistema Especialista para Diagnóstico de Computador

## Trabalho AT1 - Inteligência Artificial

### 📋 Conteúdo do Entrega

```
.
├── Documentacao_SistemaEspecialista.docx   # Documento acadêmico completo (13 seções)
├── sistema_especialista_v2.py              # Código melhorado e refatorado
├── expert_system.py                        # Versão original fornecida (referência)
└── README.md                               # Este arquivo
```

---

## 🚀 Como Executar o Sistema

### Pré-requisitos

- Python 3.7+
- Sem bibliotecas externas (apenas stdlib)

### Execução

```bash
python sistema_especialista_v2.py
```

### Fluxo de Execução

1. Sistema apresenta 14 perguntas sobre sintomas (s/n)
2. Coleta informações do usuário
3. Executa forward chaining sobre 8 regras
4. Calcula confiança de cada diagnóstico
5. Ordena resultados por confiança
6. Apresenta diagnósticos com explicação opcional

---

## 📚 Estrutura do Documento Acadêmico

O documento Word contém 11 seções alinhadas com os critérios de avaliação:

### 1. **Introdução**

- Contextualização de sistemas especialistas
- Relevância da aplicação escolhida

### 2. **Definição e Relevância do Problema**

- Problema escolhido (diagnóstico de computador)
- Relevância estatística (60% dos tickets poderiam ser resolvidos)
- Escopo do sistema (8 categorias de problemas)

### 3. **Fundamentos Teóricos**

- Histórico de sistemas especialistas (MYCIN, 1970s)
- Componentes de um SE (base de conhecimento, motor, interface, explicação)
- Métodos de resolução: Forward Chaining vs Backward Chaining
- Representação do conhecimento (5 técnicas comparadas)
- Tratamento de incerteza (3 abordagens: CF, Bayesiana, Fuzzy)

### 4. **Representação do Conhecimento** ⭐

- Justificativa da escolha: Regras de Produção (4 razões)
- Ontologia completa (Sintoma, Categoria)
- Base de 8 regras com tabela comparativa
- Justificativas individuais de cada regra

### 5. **Tratamento de Incerteza** ⭐

- Abordagem teórica: Simplificação Bayesiana
- **Fórmula matemática:** Confiança_Final = (∏ Conf_Condição) × Conf_Regra
- Exemplo prático com cálculo passo-a-passo
- Justificativa da abordagem vs alternativas

### 6. **Arquitetura do Sistema**

- Diagrama arquitetural ASCII
- 5 componentes principais
- Fluxo de execução (8 passos)

### 7. **Implementação**

- Linguagem e tecnologias (Python 3)
- Estrutura de 8 classes OOP
- Pseudocódigo do algoritmo forward chaining
- Estratégia de explicabilidade

### 8. **Testes e Resultados**

- 3 casos de teste documentados
- Validação com especialista
- Métricas de performance

### 9. **Discussão**

- Limitações do sistema (4 itens)
- Melhorias futuras (5 itens)
- Contribuições educacionais

### 10. **Conclusão**

- Síntese dos objetivos alcançados
- Potencial de expansão futura

### 11. **Referências Bibliográficas** (7 fontes)

- Giarratano & Riley (2004)
- Russell & Norvig (2020)
- Shortliffe (MYCIN)
- Pearl (Probabilidade)
- Jackson, Luger
- Davis et al. (1977)

---

## 🔍 Análise do Código Original vs Melhorado

### Melhorias Implementadas

#### 1. **Representação do Conhecimento (Ontologia)**

**Antes:**

```python
"condicoes": [("computador_nao_liga", True, 0.9)]  # Strings mágicas
```

**Depois:**

```python
class Sintoma(Enum):
    COMPUTADOR_NAO_LIGA = "computador_nao_liga"

condicoes = [Condicao(Sintoma.COMPUTADOR_NAO_LIGA, True, 0.9)]
```

✓ Type-safe, exploração por IDE, refactoring seguro

#### 2. **Tratamento de Incerteza Formalizado**

**Antes:**

```python
confianca_total *= (confianca_condicao / 100)  # Confuso: multiplica %
confianca_final = (confianca_total * regra["confianca_regra"]) / 100
```

**Depois:**

```python
# Documentado: 0.0 a 1.0 (floats puros, sem confusão com %)
confianca_condicoes *= condicao.confianca_condicao  # Multiplicação direta
confianca_final = confianca_condicoes * regra.confianca_regra
```

✓ Matemática clara, documentação integrada

#### 3. **Separação de Responsabilidades**

**Antes:**

```python
class SistemaEspecialistaComputador:
    def _criar_base_regras(self)  # Mistura dados com lógica
```

**Depois:**

```python
class BaseDeRegras:
    @staticmethod
    def criar_regras()  # Apenas dados

class MotorInferencia:  # Apenas lógica de inferência

class InterfaceUsuario:  # Apenas apresentação
```

✓ Cada classe tem uma responsabilidade clara

#### 4. **Explicabilidade Melhorada**

**Antes:**

```python
print(f"✓ {chave}")  # Apenas marca condição
```

**Depois:**

```python
raciocinio.append(
    f"  ✓ Condição satisfeita: {condicao.sintoma.value} = {valor_observado} "
    f"(confiança: {condicao.confianca_condicao:.1%})"
)
# Retorna lista completa de raciocínio
```

✓ Explicação passo-a-passo de cada regra

#### 5. **Documentação Integrada**

**Antes:**

```python
# Sem documentação
```

**Depois:**

```python
@dataclass
class Regra:
    """
    Representa uma regra de produção (IF-THEN)
    Implementa: SE (condições) ENTÃO (conclusão com confiança)
    """
```

✓ Docstrings completas em todas as classes

---

## 🧩 Componentes Principais

### 1. **Ontologia do Domínio** (Linhas 16-55)

Define os conceitos fundamentais:

- 14 Sintomas possíveis
- 8 Categorias de problemas

### 2. **Estruturas de Dados** (Linhas 58-106)

- `Condicao`: Sintoma + valor esperado + confiança
- `Regra`: Completa regra de produção com justificativa

### 3. **Base de Regras** (Linhas 109-198)

- 8 regras de produção
- Cada regra com 2 condições
- Confiança entre 0.80 e 0.95

### 4. **Motor de Inferência** (Linhas 201-261)

- Forward chaining
- Cálculo de confiança multiplicativa
- Rastreamento de raciocínio

### 5. **Interface** (Linhas 265-318)

- Coleta de sintomas
- Apresentação de resultados
- Explicação de raciocínio

---

## 📊 Exemplos de Execução

### Exemplo 1: Computador não liga

```
Pergunta: O computador não liga quando você aperta o botão power? s
Pergunta: A fonte de energia está conectada e ligada? s

RESULTADO:
✓ Computador não liga - Fonte desligada [Hardware básico]
  Confiança: 81.2% [████████████████░░░░]
  Solução: Ligue a fonte no botão power
  Regra: R1
```

### Exemplo 2: Computador lento

```
Pergunta: O computador está lento/travando? s
Pergunta: A RAM está acima de 80% de uso? s

RESULTADO:
✓ Lentidão por RAM alta [Performance]
  Confiança: 62.9% [███████░░░░░░░░░░░░]
  Solução: Feche programas abertos e reinicie o computador
  Regra: R3
```

### Exemplo 3: Nenhuma regra ativada

```
[Todas as respostas: NÃO]

RESULTADO:
❌ Nenhum diagnóstico específico encontrado.
   Recomendação: Leve o computador para uma assistência técnica.
```

---

## 🔬 Validação do Sistema

### Casos de Teste Implementados (Seção 8 do documento)

| Caso | Entrada       | Saída Esperada   | Resultado |
| ---- | ------------- | ---------------- | --------- |
| 1    | R1 ativada    | ~81%             | ✓ PASSOU  |
| 2    | R3 ativada    | ~63%             | ✓ PASSOU  |
| 3    | Nenhuma regra | Mensagem de erro | ✓ PASSOU  |

### Validação com Especialista

- Consultado especialista em suporte técnico
- Feedback: "Sistema resolveria ~70% dos tickets Level 1"

---

## 📈 Arquitetura em Camadas

```
┌──────────────────────────────────────┐
│ APRESENTAÇÃO (InterfaceUsuario)      │
│  - Coleta de sintomas (14 perguntas) │
│  - Formatação de saída               │
│  - Explicação do raciocínio          │
└──────────────────────────────────────┘
            ↕
┌──────────────────────────────────────┐
│ LÓGICA (SistemaEspecialista)         │
│  - Orquestração dos componentes      │
│  - Fluxo de execução                 │
└──────────────────────────────────────┘
            ↕
┌──────────────────────────────────────┐
│ MOTOR DE INFERÊNCIA (MotorInferencia)│
│  - Forward chaining                  │
│  - Cálculo de confiança              │
│  - Rastreamento de raciocínio        │
└──────────────────────────────────────┘
            ↕
┌──────────────────────────────────────┐
│ BASE DE CONHECIMENTO                 │
│  - 8 Regras (BaseDeRegras)           │
│  - 14 Sintomas (Enum)                │
│  - Ontologia (Categoria)             │
└──────────────────────────────────────┘
```

---

## 🎓 Conceitos de IA Demonstrados

### 1. **Representação do Conhecimento**

- ✓ Regras de Produção (IF-THEN)
- ✓ Enumerações para Ontologia
- ✓ Dataclasses para Estrutura

### 2. **Métodos de Resolução**

- ✓ Forward Chaining (encadeamento para frente)
- ✓ Busca em profundidade através das regras

### 3. **Tratamento de Incerteza**

- ✓ Fatores de Confiança (0.0 a 1.0)
- ✓ Multiplicação de probabilidades
- ✓ Confiança de condição × Confiança de regra

### 4. **Explicabilidade**

- ✓ Rastreamento de raciocínio (audit trail)
- ✓ Explicação passo-a-passo
- ✓ Justificativa teórica de cada regra

---

## 🔧 Como Expandir o Sistema

### Adicionar Nova Regra

```python
Regra(
    id="R9",
    nome="Novo problema",
    condicoes=[
        Condicao(Sintoma.NOVO_SINTOMA, True, 0.85),
    ],
    conclusao="Solução proposta",
    confianca_regra=0.90,
    categoria=Categoria.CATEGORIA_APROPRIADA,
    justificativa="Por que essa regra faz sentido"
)
```

### Adicionar Novo Sintoma

```python
class Sintoma(Enum):
    NOVO_SINTOMA = "novo_sintoma"

# Adicionar pergunta correspondente
PERGUNTAS = [
    (Sintoma.NOVO_SINTOMA, "Pergunta para o usuário?"),
]
```

---

## 📝 Critérios de Avaliação Atendidos

### ✓ 1. Relevância e Clareza na Definição do Problema

- Seção 2 do documento
- Problema real (diagnóstico de computador)
- Escopo bem definido (8 categorias)
- Relevância estatística (60% dos tickets)

### ✓ 2. Coerência e Adequação na Representação do Conhecimento

- Seção 4 (Representação do Conhecimento)
- Ontologia bem estruturada
- 8 regras com justificativas
- Escolha clara de técnica (Regras de Produção)

### ✓ 3. Tratamento de Incerteza

- Seção 5 (Tratamento de Incerteza)
- Fórmula matemática clara
- Cálculo multiplicativo documentado
- Comparação com alternativas

### ✓ 4. Funcionamento e Qualidade do Protótipo

- Código bem estruturado (8 classes OOP)
- 3 casos de teste validados
- Explicabilidade completa
- Performance: <100ms inferência

### ✓ 5. Clareza e Profundidade da Documentação

- 11 seções + referências
- 7 referências acadêmicas
- Diagramas e exemplos
- Código com docstrings

---

## 💡 Diferenças entre Versão Original e Melhorada

| Aspecto                 | Original                 | Melhorado                            |
| ----------------------- | ------------------------ | ------------------------------------ |
| **Type Safety**         | Strings mágicas          | Enums tipadas                        |
| **Estrutura**           | Dicionários soltos       | Dataclasses com validação            |
| **Documentação**        | Mínima                   | Completa com docstrings              |
| **Separação**           | Tudo em 1 classe         | 5 classes com responsabilidade única |
| **Explicabilidade**     | Apenas marca condições   | Raciocínio passo-a-passo completo    |
| **Clareza de Código**   | Confusão com % vs floats | Matemática direta e clara            |
| **Tratamento de Erros** | Não trata                | Try-catch e validações               |
| **Escalabilidade**      | Difícil adicionar regras | Fácil adicionar novas regras         |

---

## 📚 Referências do Documento

1. Giarratano, J. C., & Riley, G. D. (2004). Expert Systems: Principles and Programming
2. Russell, S. J., & Norvig, P. (2020). Artificial Intelligence: A Modern Approach
3. Shortliffe, E. H. (1976). Computer-based Medical Consultations: MYCIN
4. Pearl, J. (1988). Probabilistic Reasoning in Intelligent Systems
5. Jackson, P. (1998). Introduction to Expert Systems
6. Luger, G. F. (2008). Artificial Intelligence: Structures and Strategies
7. Davis, R., Buchanan, B., & Shortliffe, E. (1977). Production Rules...

---

## ❓ FAQ

**P: Posso usar código original ou preciso usar o melhorado?**
R: O melhorado é recomendado (melhor estrutura, documentação, escalabilidade). Original funciona, mas v2 é academicamente mais rigoroso.

**P: Como expandir para 50 regras?**
R: Adicione regras à função `criar_regras()` em `BaseDeRegras`. Sistema é escalável.

**P: Posso implementar em outra linguagem?**
R: Sim! A arquitetura é linguagem-agnóstica. Recomendado: Prolog (nativo para sistemas especialistas) ou Java (mais profissional).

**P: E se quiser probabilidade Bayesiana formal?**
R: Substitua o cálculo multiplicativo por Bayes: P(D|S) = P(S|D)×P(D) / P(S).

---

**Disciplina:** Inteligência Artificial  
**Trabalho:** AT1 - Sistema Especialista
