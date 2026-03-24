# ConectaTalentos

## 📄 RH Inteligente — Ranqueamento de Currículos com IA

> Projeto do **Grupo 4** do curso **IA para Desenvolvedores**

---

## 🎯 Objetivo

Ranquear candidatos e facilitar a decisão do RH na escolha do profissional mais adequado para cada vaga.

--- 

## ⚙️ Como Funciona

1. **Cadastro de Vagas** — O RH registra as oportunidades disponíveis.
2. **Upload de Currículo** — O RH cadastra os currículos recebidos.
3. **Extração** — Conversão de PDF para texto estruturado.
4. **Análise por LLM** — A IA compara o perfil do candidato e ranqueia os mais adequados para cada vaga.

---

## 🚀 Desafios

- Criar o melhor prompt para ler currículos, pontuar e adequar o melhor candidato para a vaga.
- Otimizar para usar a menor quantidade de tokens possíveis mantendo a eficiência da análise.

---

## 🛠️ Tecnologias

| Tecnologia | Uso |
|---|---|
| Python (Web App) | Backend e interface web |
| Extração PDF nativa | Conversão de currículo para texto |
| LLM otimizado | Análise e ranqueamento de candidatos |
| Microsoft Presidio | Anonimização de dados sensíveis (LGPD) |

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

- Python 3.11 ou superior
- pip (gerenciador de pacotes Python)

### 1. Clonar o Repositório

```bash
git clone <url-do-repositorio>
cd Conecta-Talentos
```

### 2. Criar Ambiente Virtual

**Linux/Mac:**
```bash
python -m venv .venv
source .venv/bin/activate
```

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instalar Dependências

```bash
pip install -r backend/requirements-basico.txt
```

Ou instalar manualmente:
```bash
pip install pymupdf
```

### 4. Testar a Classe ExtratorPDF

**Executar exemplos completos:**
```bash
python backend/src/exemplo_uso_extrator.py
```

**Testar com arquivo de exemplo:**
```bash
# Exibir no terminal
python backend/src/extrator_pdf.py backend/exemplo.pdf

# Salvar em arquivo
python backend/src/extrator_pdf.py backend/exemplo.pdf saida.txt
```

**Usar a classe no código:**
```python
from pathlib import Path
from backend.src.extrator_pdf import ExtratorPDF

# Criar extrator
extrator = ExtratorPDF(max_paginas=10)

# Extrair texto
resultado = extrator.extrair_texto(Path("backend/exemplo.pdf"))

# Usar resultado
print(f"Páginas: {resultado.num_paginas}")
print(f"Texto: {resultado.conteudo}")
```

### 5. Estrutura do Projeto

```
Conecta-Talentos/
├── .kiro/                           # Especificações do Kiro/IA
├── .github/                         # Configurações para Github
├── backend/                         # Backend Python
│   ├── docs/                        # Documentação
│   │   ├── base-implementacao.md
│   │   ├── classe-extrator-pdf.md
│   │   └── como-usar-extrator.md
│   ├── tests/                       # Testes automatizados
│   ├── src/                         # Código-fonte
│   │   ├── extrator_pdf.py
│   │   ├── exemplo_uso_extrator.py
│   │   └── pdf_to_text.py
│   ├── .env.example                 # Variáveis de ambiente
│   ├── exemplo.pdf                  # Arquivo de teste
│   └── requirements-basico.txt      # Dependências Python
├── scripts/                         # Scripts gerais do repositório
├── .gitignore
└── README.md
```

---

## 📚 Documentação

- **[Guia de Uso](backend/docs/como-usar-extrator.md)** - Como usar a classe ExtratorPDF
- **[Documentação Técnica](backend/docs/classe-extrator-pdf.md)** - Arquitetura e detalhes da implementação
- **[Base de Implementação](backend/docs/base-implementacao.md)** - Guia completo para implementar o sistema
- **[Requisitos](/.kiro/specs/conecta-talentos/requirements.md)** - Requisitos funcionais do sistema
- **[Design](/.kiro/specs/conecta-talentos/design.md)** - Arquitetura e design técnico

---

## 📄 Conversão de PDF para Texto

### Script Legado (pdf_to_text.py)

Script utilitário original para extrair texto de arquivos PDF.

```bash
# Exibir o texto no terminal
python backend/src/pdf_to_text.py backend/exemplo.pdf

# Salvar o texto em um arquivo
python backend/src/pdf_to_text.py backend/exemplo.pdf saida.txt
```

### Nova Classe ExtratorPDF (Recomendado)

Classe profissional com validação, tratamento de erros e documentação completa.

```bash
# Executar exemplos
python backend/src/exemplo_uso_extrator.py

# Usar diretamente
python backend/src/extrator_pdf.py backend/exemplo.pdf
```

---

## 🧪 Testes

Para testar a classe ExtratorPDF:

```bash
# Executar todos os exemplos
python backend/src/exemplo_uso_extrator.py

# Testar com arquivo específico
python backend/src/extrator_pdf.py seu_arquivo.pdf
```

---

## 🔧 Solução de Problemas

### Erro: "ModuleNotFoundError: No module named 'pymupdf'"

**Solução:**
```bash
pip install pymupdf
```

### Erro: "Arquivo não encontrado"

**Solução:** Verifique se o arquivo PDF existe no diretório atual ou forneça o caminho completo.

### Erro: "PDF tem X páginas, máximo permitido: Y"

**Solução:** Aumente o limite de páginas ao criar o extrator:
```python
extrator = ExtratorPDF(max_paginas=20)
```

---

## 📈 Roadmap

- [x] Classe ExtratorPDF implementada
- [x] Documentação completa
- [x] Especificações (requirements e design)
- [ ] Classe Anonimizador (Microsoft Presidio)
- [ ] Classe AnalisadorLLM (OpenAI)
- [ ] Interface Web (FastAPI)
- [ ] Testes automatizados
- [ ] Deploy em produção

---

## 👥 Integrantes — Grupo 4

| Nome |
|---|
| Gustavo da Rosa Heidemann |
| Halan Germano Bacca |
| Ismael Lunkes Pereira |
| Leandro da Silva Gerolim |
| Mariana Cristina da Silva Gabriel |
| Pedro Santos da Mota |

---

## 📊 Diagrama UML — Fluxos do Sistema

O diagrama abaixo unifica todos os requisitos e user stories do sistema ConectaTalentos, mostrando como os fluxos se conectam desde o cadastro de vagas até a visualização do ranking final.

```mermaid
flowchart TD
    subgraph REQ1["Req 1 — Cadastro de Vagas"]
        A1([RH acessa o sistema]) --> A2[Preenche dados da vaga\ntítulo, descrição, requisitos técnicos,\nexperiência mínima, competências]
        A2 --> A3{Campos obrigatórios\npreenchidos?}
        A3 -- Não --> A4[Exibe erro de validação]
        A4 --> A2
        A3 -- Sim --> A5[(Persiste vaga no banco)]
        A5 --> A6[Vaga cadastrada com sucesso]
        A6 --> A7[Listar / Editar vagas existentes]
    end

    subgraph REQ2["Req 2 — Upload de Currículos"]
        B1([RH seleciona vaga]) --> B2[Faz upload de arquivo]
        B2 --> B3{Formato é PDF?}
        B3 -- Não --> B4[Retorna mensagem de erro descritiva]
        B4 --> B2
        B3 -- Sim --> B5[(Armazena PDF original)]
        B5 --> B6[Associa currículo à vaga]
        B6 --> B7[Upload concluído — aceita múltiplos PDFs]
    end

    subgraph REQ3["Req 3 — Extração de Texto"]
        C1([PDF armazenado]) --> C2[Extrator_PDF processa documento]
        C2 --> C3{PDF válido e legível?\nMáx 10 páginas}
        C3 -- Não --> C4[Retorna erro específico\nReq 10 — log de erro]
        C3 -- Sim --> C5[Converte em Texto Estruturado\npreserva seções e parágrafos]
    end

    subgraph REQ4["Req 4 — Anonimização LGPD"]
        D1([Texto extraído]) --> D2[Anônimizador — Microsoft Presidio]
        D2 --> D3[Substitui dados sensíveis:\nNome → NOME\nCPF → CPF\nEndereço → ENDEREÇO\nTelefone → TELEFONE\nEmail → EMAIL]
        D3 --> D4{Anonimização OK?}
        D4 -- Falha --> D5[Registra erro em log\ncontinua sem anonimização\nReq 10]
        D4 -- Sim --> D6[Texto anonimizado pronto\ninfo profissional preservada]
        D5 --> D6
    end

    subgraph REQ6["Req 6 — Otimização de Tokens"]
        E1([Texto anonimizado]) --> E2[Remove texto redundante\ne irrelevante]
        E2 --> E3{Texto > 2000 tokens?}
        E3 -- Sim --> E4[Resume seções menos relevantes]
        E3 -- Não --> E5[Monta Prompt Otimizado\nformato JSON / lista estruturada]
        E4 --> E5
        E5 --> E6[Inclui apenas:\n- requisitos-chave da vaga\n- seções relevantes do currículo]
    end

    subgraph REQ5["Req 5 — Análise e Ranqueamento LLM"]
        F1([Prompt otimizado]) --> F2[Analisador_LLM compara\nperfil vs requisitos da vaga]
        F2 --> F3{LLM disponível?}
        F3 -- Não --> F4[Exibe erro e permite\nreprocessamento — Req 10]
        F3 -- Sim --> F5[Atribui Score 0-100]
        F5 --> F6[Gera justificativa textual]
        F6 --> F7[Identifica pontos fortes]
        F7 --> F8[Identifica gaps / lacunas]
        F8 --> F9[Gera Ranking ordenado\npor Score decrescente]
    end

    subgraph REQ9["Req 9 — Persistência"]
        G1[(Persiste resultados:\nScores, justificativas, rankings)]
        G2[Recuperação após reinicialização]
        G3[Exclusão de vaga remove\ncurrículos e análises associadas]
    end

    subgraph REQ7["Req 7 — Visualização de Resultados"]
        H1([RH acessa ranking da vaga]) --> H2[Exibe lista: Score, arquivo\ndo currículo, resumo da justificativa]
        H2 --> H3[Expandir para ver justificativa\ncompleta, pontos fortes e gaps]
        H2 --> H4[Ordenar por Score ou nome]
        H2 --> H5[Filtrar por Score mínimo]
    end

    subgraph REQ8["Req 8 — Interface Web"]
        I1[Navegador Web — responsivo desktop]
        I2[Páginas: Cadastro de Vagas\nUpload de Currículos\nVisualização de Rankings]
        I3[Feedback visual: loading,\nprogresso, mensagens de erro]
    end

    %% Conexões entre os fluxos
    A6 --> B1
    B7 --> C1
    C5 --> D1
    D6 --> E1
    E6 --> F1
    F9 --> G1
    G1 --> H1

    %% Interface Web engloba tudo
    I1 --> A1
    I1 --> B1
    I1 --> H1
    I2 -.- I3
```

---

## 📝 Licença

Projeto acadêmico — uso educacional.
