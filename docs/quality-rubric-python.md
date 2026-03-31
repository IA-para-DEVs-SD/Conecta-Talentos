# Rubrica de Qualidade — Projetos Python

Documento de avaliacao de qualidade para projetos Python, definindo criterios objetivos para medir e manter o padrao de excelencia do codigo.

---

## 1. Qualidade de Codigo (0 a 30 pontos)

Avalia a legibilidade, manutenibilidade e aderencia as convencoes Python (PEP 8).

| Faixa | Nivel | Descricao |
|-------|-------|-----------|
| 25-30 | Excelente | Codigo segue PEP 8 e convencoes Python (snake_case para funcoes/variaveis, PascalCase para classes, UPPER_SNAKE_CASE para constantes). Funcoes pequenas e com responsabilidade unica. Separacao clara entre camadas (controllers → services → repositories → models). Sem codigo duplicado. Type hints completos. |
| 18-24 | Bom | Codigo segue a maioria das convencoes PEP 8. Funcoes com escopo bem definido. Separacao de camadas respeitada com raras excecoes. Pouca duplicacao. Type hints nas funcoes principais. |
| 10-17 | Aceitavel | Algumas violacoes de PEP 8. Funcoes ocasionalmente longas ou com multiplas responsabilidades. Alguma duplicacao de logica entre camadas. Type hints parciais. |
| 0-9 | Insuficiente | Convencoes ignoradas. Funcoes monoliticas. Logica de negocio misturada com controle de fluxo HTTP. Duplicacao significativa. Sem type hints. |

### Checklist

- Nomenclatura consistente seguindo PEP 8 (snake_case para modulos/funcoes, PascalCase para classes)
- Funcoes com responsabilidade unica e tamanho razoavel (maximo 50 linhas)
- Separacao de camadas respeitada (controllers → services → repositories → models)
- Constantes extraidas e nomeadas (ex: MAX_FILE_SIZE_MB, MAX_PDF_PAGES, DEFAULT_SCORE)
- Type hints em funcoes publicas (parametros e retorno)
- Uso de dataclasses ou Pydantic para modelos de dados
- Imports organizados (stdlib → third-party → local)

---

## 2. Clareza da Documentacao (0 a 20 pontos)

Avalia a qualidade das docstrings, comentarios e documentacao auxiliar do projeto.

| Faixa | Nivel | Descricao |
|-------|-------|-----------|
| 17-20 | Excelente | Todos os modulos possuem docstring explicando proposito. Funcoes publicas documentadas com docstrings (Args, Returns, Raises). Comentarios inline explicam o "porque", nao o "o que". Documentacao em portugues brasileiro. |
| 12-16 | Bom | Maioria dos modulos e funcoes documentados. Docstrings presentes nas funcoes principais. Comentarios inline em pontos criticos. |
| 6-11 | Aceitavel | Documentacao parcial. Algumas funcoes sem docstrings. Comentarios esparsos ou redundantes com o codigo. |
| 0-5 | Insuficiente | Sem docstrings de modulo. Funcoes sem documentacao. Comentarios em idioma inconsistente. |

### Checklist

- Docstring de modulo no topo de cada arquivo
- Docstrings com formato Google/NumPy em funcoes publicas (Args, Returns, Raises)
- Comentarios inline explicando decisoes nao obvias
- Referencias a requisitos do design doc nos testes
- Documentacao e mensagens de usuario em portugues brasileiro
- Nomes de variaveis e funcoes autoexplicativos (snake_case)

---

## 3. Seguranca (0 a 20 pontos)

Avalia as praticas de protecao contra vulnerabilidades e abuso.

| Faixa | Nivel | Descricao |
|-------|-------|-----------|
| 17-20 | Excelente | Validacao de entrada em todas as camadas (schemas Pydantic + validacao no service layer). Autenticacao JWT com verificacao de blacklist. Rate limiting diferenciado por tipo de endpoint. Erros estruturados sem exposicao de stack traces em producao. Sanitizacao de dados antes do processamento. |
| 12-16 | Bom | Validacao presente na maioria dos endpoints. Autenticacao implementada. Rate limiting configurado. Erros tratados de forma centralizada. |
| 6-11 | Aceitavel | Validacao parcial. Autenticacao basica sem blacklist. Rate limiting generico. Alguns endpoints sem tratamento de erro adequado. |
| 0-5 | Insuficiente | Entradas nao validadas. Sem autenticacao ou autenticacao fragil. Sem rate limiting. Stack traces expostos em producao. |

### Checklist

- Validacao com Pydantic schemas em todos os endpoints que recebem dados
- Validacao duplicada no service layer para seguranca em profundidade
- Middleware de autenticacao verifica token, blacklist e existencia do usuario
- Rate limiting diferenciado por tipo de endpoint (ex: uploads, analise IA)
- Excecoes customizadas com mapeamento de codigos HTTP padronizado
- Stack traces suprimidos em producao (verificacao de ambiente)
- Senhas com hash bcrypt/argon2 e requisito minimo de 8 caracteres
- Dados sensiveis sanitizados/anonimizados antes de persistir

---

## 4. Estrategia de Testes e Verificacao de Propriedades (0 a 30 pontos)

Avalia a abrangencia, sofisticacao e confiabilidade da suite de testes. Este criterio valoriza especialmente a adocao de testes baseados em propriedades (property-based testing) com hypothesis para validar invariantes matematicos e regras de negocio.

| Faixa | Nivel | Descricao |
|-------|-------|-----------|
| 25-30 | Excelente | Testes unitarios para cada modulo com pytest. Testes de propriedade (PBT) com hypothesis validando invariantes matematicos. Testes e2e cobrindo fluxo completo do usuario. Infraestrutura de teste com banco em memoria isolado por teste. Fixtures e geradores customizados para dados realistas. |
| 18-24 | Bom | Testes unitarios na maioria dos modulos. Alguns testes de propriedade para logica critica. Teste e2e do fluxo principal. Fixtures bem organizadas. |
| 10-17 | Aceitavel | Testes unitarios parciais. Sem testes de propriedade. Testes e2e basicos. Fixtures inconsistentes ou frageis. |
| 0-9 | Insuficiente | Cobertura de testes baixa. Sem testes de propriedade ou e2e. Testes frageis ou dependentes de estado externo. |

### Checklist

- Cada modulo possui arquivo de teste correspondente (test_*.py)
- Testes de propriedade com hypothesis validando invariantes (ex: score entre 0-100, listas nao vazias)
- Propriedades matematicas verificadas com hypothesis strategies customizadas
- Teste e2e cobrindo fluxo completo com TestClient do FastAPI
- Banco em memoria (SQLite :memory:) isolado por teste com fixtures
- Fixtures pytest organizadas em conftest.py
- Referencias explicitas aos requisitos nos testes
- Cleanup adequado com fixtures de escopo apropriado (function/module/session)
- Cobertura de testes >80% medida com pytest-cov

---

## Como Usar Esta Rubrica

1. Antes de abrir um PR, revise o codigo contra os checklists de cada criterio
2. Na code review, use os niveis (Excelente → Insuficiente) para classificar cada aspecto
3. Priorize correcoes de itens classificados como Insuficiente ou Aceitavel
4. O objetivo minimo para merge e Bom em todos os criterios

---

## Pontuacao de Referencia

| Criterio | Pontos Minimos | Pontos Ideais |
|----------|----------------|---------------|
| Qualidade de Codigo | 18 (Bom) | 25+ (Excelente) |
| Documentacao | 12 (Bom) | 17+ (Excelente) |
| Seguranca | 12 (Bom) | 17+ (Excelente) |
| Testes | 18 (Bom) | 25+ (Excelente) |
| TOTAL | 60/100 | 85+/100 |

### Niveis de Qualidade

- 90-100 pontos: Excelente — Codigo de producao pronto para escala
- 75-89 pontos: Bom — Codigo solido com pequenas melhorias necessarias
- 60-74 pontos: Aceitavel — Codigo funcional mas precisa de refatoracao
- 0-59 pontos: Insuficiente — Codigo precisa de revisao significativa
