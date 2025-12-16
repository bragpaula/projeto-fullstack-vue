# 🔧 Backend - API Flask

API REST desenvolvida em Flask para o sistema de mensagens, com autenticação JWT, CRUD completo de mensagens e comentários.

## 🚀 Tecnologias

- **Flask** 3.1.2 - Framework web
- **Flask-JWT-Extended** 4.7.1 - Autenticação JWT
- **Flask-SQLAlchemy** 3.1.1 - ORM
- **Flask-Migrate** 4.1.0 - Migrações de banco
- **Flask-CORS** 5.0.0 - CORS
- **SQLite** - Banco de dados
- **Python** 3.8+

---

## 📁 Estrutura

```
backend/
├── src/
│   ├── app.py              # Aplicação Flask principal
│   ├── models.py           # Modelos SQLAlchemy (Usuario, Mensagem, Comentario)
│   ├── utils.py            # Configuração do banco de dados
│   ├── routes/
│   │   ├── usuario.py      # Rotas de autenticação (/auth)
│   │   ├── mensagem.py     # Rotas de mensagens (/mensagens)
│   │   └── comentario.py   # Rotas de comentários (/mensagens/:id/comentarios)
│   ├── migrations/         # Migrações do banco (Alembic)
│   └── instance/
│       └── database.db     # Banco SQLite (gerado automaticamente)
├── requirements.txt        # Dependências Python
└── README.md              # Este arquivo
```

---

## 🔧 Instalação

### 1. Instalar dependências

```bash
cd backend
pip install -r requirements.txt
```

### 2. Configurar variáveis de ambiente

Crie um arquivo `.env` na pasta `backend/src/`:

```env
SECRET_KEY=sua-chave-secreta-super-segura-aqui
JWT_SECRET_KEY=sua-chave-jwt-secreta-aqui
```

**Exemplo:**
```env
SECRET_KEY=minha-chave-secreta-12345
JWT_SECRET_KEY=minha-chave-jwt-67890
```

### 3. Executar migrações (se necessário)

```bash
cd src
flask db upgrade
```

---

## 🚀 Executando o Servidor

### Opção 1: Python direto

```bash
cd backend/src
python app.py
```

### Opção 2: Flask CLI

```bash
cd backend/src
flask run
```

O servidor estará rodando em `http://localhost:5000`

---

## 📡 Endpoints da API

### 🔐 Autenticação

#### `POST /auth/register`
Cadastra um novo usuário.

**Request Body:**
```json
{
  "nome": "João Silva",
  "email": "joao@email.com",
  "senha": "senha123"
}
```

**Response (201):**
```json
{
  "accessToken": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "user": {
    "nome": "João Silva",
    "email": "joao@email.com"
  }
}
```

#### `POST /auth/login`
Realiza login do usuário.

**Request Body:**
```json
{
  "email": "joao@email.com",
  "senha": "senha123"
}
```

**Response (200):**
```json
{
  "accessToken": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "user": {
    "nome": "João Silva",
    "email": "joao@email.com"
  }
}
```

---

### 📬 Mensagens

#### `GET /mensagens`
Lista todas as mensagens (público).

**Response (200):**
```json
[
  {
    "id": 1,
    "titulo": "Minha primeira mensagem",
    "conteudo": "Conteúdo da mensagem...",
    "autor": "João Silva",
    "usuario_id": 1,
    "created_at": "2024-01-15T10:30:00"
  }
]
```

#### `GET /mensagens/:id`
Busca uma mensagem específica.

**Response (200):**
```json
{
  "id": 1,
  "titulo": "Minha primeira mensagem",
  "conteudo": "Conteúdo da mensagem...",
  "autor": "João Silva",
  "usuario_id": 1,
  "created_at": "2024-01-15T10:30:00"
}
```

#### `POST /mensagens` 🔒
Cria uma nova mensagem (requer autenticação).

**Headers:**
```
Authorization: Bearer <token>
```

**Request Body:**
```json
{
  "titulo": "Nova mensagem",
  "conteudo": "Conteúdo da nova mensagem"
}
```

**Response (201):**
```json
{
  "id": 2,
  "titulo": "Nova mensagem",
  "conteudo": "Conteúdo da nova mensagem",
  "autor": "João Silva",
  "usuario_id": 1,
  "created_at": "2024-01-15T11:00:00"
}
```

#### `PUT /mensagens/:id` 🔒
Atualiza uma mensagem (requer autenticação + ser o dono).

**Headers:**
```
Authorization: Bearer <token>
```

**Request Body:**
```json
{
  "titulo": "Título atualizado",
  "conteudo": "Conteúdo atualizado"
}
```

**Response (200):** Mensagem atualizada

**Response (403):** Acesso negado (não é o dono)

#### `DELETE /mensagens/:id` 🔒
Remove uma mensagem (requer autenticação + ser o dono).

**Headers:**
```
Authorization: Bearer <token>
```

**Response (204):** Sem conteúdo (sucesso)

**Response (403):** Acesso negado (não é o dono)

---

### 💬 Comentários

#### `GET /mensagens/:id/comentarios` 🔒
Lista comentários de uma mensagem (requer autenticação).

**Headers:**
```
Authorization: Bearer <token>
```

**Response (200):**
```json
[
  {
    "id": 1,
    "conteudo": "Ótima mensagem!",
    "autor": "Maria Santos",
    "mensagem_id": 1,
    "data_criacao": "2024-01-15T12:00:00"
  }
]
```

#### `POST /mensagens/:id/comentarios` 🔒
Cria um novo comentário (requer autenticação).

**Headers:**
```
Authorization: Bearer <token>
```

**Request Body:**
```json
{
  "conteudo": "Novo comentário"
}
```

**Response (201):** Comentário criado

#### `PUT /mensagens/comentarios/:id` 🔒
Atualiza um comentário (requer autenticação + ser dono da mensagem).

**Headers:**
```
Authorization: Bearer <token>
```

**Request Body:**
```json
{
  "conteudo": "Comentário atualizado"
}
```

**Response (200):** Comentário atualizado

**Response (403):** Acesso negado

#### `DELETE /mensagens/comentarios/:id` 🔒
Remove um comentário (requer autenticação + ser dono da mensagem).

**Headers:**
```
Authorization: Bearer <token>
```

**Response (204):** Sem conteúdo (sucesso)

**Response (403):** Acesso negado

---

## 🔒 Autenticação JWT

Todas as rotas marcadas com 🔒 requerem autenticação via JWT.

**Como usar:**
1. Faça login ou cadastro para obter o `accessToken`
2. Inclua o token no header `Authorization`:
   ```
   Authorization: Bearer <accessToken>
   ```

**Validação:**
- O token é validado automaticamente pelo Flask-JWT-Extended
- Rotas protegidas verificam se o usuário é o dono do recurso
- Em caso de token inválido ou expirado, retorna 401

---

## 🗄️ Banco de Dados

### Modelos

#### Usuario
- `id` (Integer, PK)
- `nome` (String)
- `email` (String, único)
- `senha` (String, hash)

#### Mensagem
- `id` (Integer, PK)
- `usuario_id` (Integer, FK -> Usuario)
- `titulo` (String)
- `conteudo` (String)
- `autor` (String)
- `created_at` (DateTime)

#### Comentario
- `id` (Integer, PK)
- `mensagem_id` (Integer, FK -> Mensagem)
- `conteudo` (String)
- `autor` (String)
- `created_at` (DateTime)

### Migrações

```bash
# Criar nova migração
flask db migrate -m "descrição"

# Aplicar migrações
flask db upgrade

# Reverter migração
flask db downgrade
```

---

## 🐛 Troubleshooting

### Erro de CORS
Se estiver tendo problemas de CORS, verifique:
1. O CORS está configurado em `app.py`
2. A origem do frontend está correta (`http://localhost:5173`)
3. O servidor foi reiniciado após mudanças

### Erro de banco de dados
```bash
# Recriar banco de dados
rm instance/database.db
flask db upgrade
```

### Erro de importação
Certifique-se de estar na pasta `backend/src` ao executar:
```bash
cd backend/src
python app.py
```

---

## 📝 Notas

- O banco de dados SQLite é criado automaticamente na primeira execução
- As senhas são armazenadas com hash usando `werkzeug.security`
- O autor das mensagens/comentários é automaticamente preenchido com o nome do usuário logado
- Apenas o dono da mensagem pode editar/excluir mensagens e comentários

---

## 👨‍💻 Desenvolvido por

Paula Braga

