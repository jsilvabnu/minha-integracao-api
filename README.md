# API de Gerenciamento de Biblioteca

Uma API REST desenvolvida em FastAPI para gerenciar um sistema de biblioteca com MySQL.

## 🚀 Funcionalidades

- **Gestão de Usuários**: Clientes e Funcionários
- **Gestão de Livros**: Cadastro de livros e cópias
- **Gestão de Empréstimos**: Controle de empréstimos e devoluções
- **Gestão de Empresas**: Cadastro de empresas

## 📋 Pré-requisitos

- Python 3.8+
- MySQL 8.0+
- pip (gerenciador de pacotes Python)

## 🔧 Instalação

### 1. Clone o repositório
```bash
git clone <url-do-repositorio>
cd minha-integracao-api
```

### 2. Configure o ambiente virtual (recomendado)
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Execute o script de configuração
```bash
python setup.py
```

Este script irá:
- Instalar todas as dependências
- Criar o arquivo `.env` com as configurações padrão
- Criar o banco de dados MySQL
- Testar a conexão

### 4. Configuração manual (opcional)

Se preferir configurar manualmente:

1. **Instale as dependências**:
```bash
pip install -r requirements.txt
```

2. **Configure o banco de dados**:
   - Crie um banco de dados MySQL chamado `meu_projeto`
   - Ou copie o arquivo `config.env.example` para `.env` e ajuste as configurações

3. **Configure as variáveis de ambiente**:
```bash
# Copie o arquivo de exemplo
cp config.env.example .env

# Edite o arquivo .env com suas configurações
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=sua_senha
DB_NAME=meu_projeto
```

## 🏃‍♂️ Executando a aplicação

```bash
python main.py
```

A API estará disponível em: http://127.0.0.1:5000

## 📚 Endpoints da API

### Verificação de Status
- `GET /` - Verifica se a API está online

### Usuários
- Rotas para gerenciar usuários (clientes e funcionários)

### Livros
- Rotas para gerenciar livros e cópias

### Empréstimos
- Rotas para gerenciar empréstimos

### Empresas
- Rotas para gerenciar empresas

## 🗄️ Estrutura do Banco de Dados

### Tabelas principais:
- `user` - Usuários base (polimórfico)
- `cliente` - Clientes da biblioteca
- `funcionario` - Funcionários da biblioteca
- `book` - Livros
- `book_copy` - Cópias de livros
- `borrow` - Empréstimos
- `empresa` - Empresas

## 🔍 Testando a API

### 1. Verificar se está funcionando:
```bash
curl http://127.0.0.1:5000/
```

### 2. Usar o script de teste:
```bash
python test_db.py
```

## 🛠️ Desenvolvimento

### Estrutura do projeto:
```
minha-integracao-api/
├── app/
│   ├── models/          # Modelos SQLAlchemy
│   └── routers/         # Rotas da API
├── database.py          # Configuração do banco
├── main.py             # Aplicação principal
├── requirements.txt    # Dependências
├── setup.py           # Script de configuração
└── test_db.py         # Script de teste
```

### Adicionando novos modelos:
1. Crie o modelo em `app/models/`
2. Importe no `app/models/__init__.py`
3. Execute `python main.py` para criar as tabelas

## 🐛 Solução de Problemas

### Erro de conexão com MySQL:
1. Verifique se o MySQL está rodando
2. Confirme as credenciais no arquivo `.env`
3. Verifique se o banco `meu_projeto` existe

### Erro de dependências:
```bash
pip install -r requirements.txt
```

### Erro de autenticação MySQL:
```bash
pip install cryptography
```

## 📝 Licença

Este projeto está sob a licença MIT.

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request
