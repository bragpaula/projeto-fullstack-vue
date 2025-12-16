# 📬 Sistema de Mensagens - Projeto Full-Stack

Sistema completo de mensagens desenvolvido como atividade final, contendo frontend em Vue.js 3 e backend em Flask, com autenticação JWT, CRUD completo de mensagens e comentários.

## 🎯 Objetivo

Desenvolver um projeto full-stack completo com:
- **Frontend**: Vue.js 3 (Vite) com Vue Router
- **Backend**: Flask (Python) com SQLAlchemy
- **Autenticação**: JWT (JSON Web Tokens)
- **CRUD**: Mensagens (recurso principal) e Comentários (sub-recurso)
- **Arquitetura**: SPA com serviços Axios, filtros, UX e mensagens

---

## 🏗️ Estrutura do Projeto

```
projeto-frontend/
├── frontend/          # Aplicação Vue.js 3
│   ├── src/
│   │   ├── components/    # Componentes Vue reutilizáveis
│   │   ├── views/         # Views/páginas da aplicação
│   │   ├── router/        # Configuração do Vue Router
│   │   ├── services/      # Serviços API (Axios)
│   │   └── App.vue        # Componente raiz
│   ├── package.json
│   └── README.md
│
├── backend/           # API Flask
│   ├── src/
│   │   ├── routes/       # Rotas da API
│   │   ├── models.py     # Modelos SQLAlchemy
│   │   ├── app.py        # Aplicação Flask
│   │   └── utils.py      # Utilitários (DB)
│   ├── requirements.txt
│   └── README.md
│
└── README.md          # Este arquivo
```

---

## 🚀 Tecnologias Utilizadas

### Frontend
- **Vue.js 3** - Framework JavaScript
- **Vue Router** - Roteamento SPA
- **Vite** - Build tool e dev server
- **Axios** - Cliente HTTP
- **JavaScript (ES6+)**

### Backend
- **Flask** - Framework web Python
- **Flask-JWT-Extended** - Autenticação JWT
- **Flask-SQLAlchemy** - ORM
- **Flask-Migrate** - Migrações de banco
- **Flask-CORS** - CORS para requisições cross-origin
- **SQLite** - Banco de dados

---

## 📋 Pré-requisitos

- **Node.js** 16+ e npm
- **Python** 3.8+
- **Git**

---

## 🔧 Instalação e Execução

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd projeto-frontend
```

### 2. Backend

```bash
cd backend
pip install -r requirements.txt
cd src
python app.py
```

O backend estará rodando em `http://localhost:5000`

**📖 Mais detalhes**: Veja [backend/README.md](./backend/README.md)

### 3. Frontend

```bash
cd frontend
npm install
npm run dev
```

O frontend estará rodando em `http://localhost:5173`

**📖 Mais detalhes**: Veja [frontend/README.md](./frontend/README.md)

---

## 🔐 Credenciais de Teste

Para testar a aplicação, você pode criar uma conta através da tela de cadastro ou usar as credenciais abaixo (se já existirem no banco):

```
Email: teste@email.com
Senha: senha123
```

---

## 📡 Endpoints da API

### Autenticação
- `POST /auth/login` - Login do usuário
- `POST /auth/register` - Cadastro de novo usuário

### Mensagens
- `GET /mensagens` - Lista todas as mensagens
- `GET /mensagens/:id` - Busca uma mensagem específica
- `POST /mensagens` - Cria nova mensagem *(protegido)*
- `PUT /mensagens/:id` - Atualiza mensagem *(protegido)*
- `DELETE /mensagens/:id` - Remove mensagem *(protegido)*

### Comentários
- `GET /mensagens/:id/comentarios` - Lista comentários de uma mensagem *(protegido)*
- `POST /mensagens/:id/comentarios` - Cria novo comentário *(protegido)*
- `PUT /mensagens/comentarios/:id` - Atualiza comentário *(protegido)*
- `DELETE /mensagens/comentarios/:id` - Remove comentário *(protegido)*

---

## ✨ Funcionalidades

### ✅ CRUD Completo
- ✅ Listar, criar, editar e excluir mensagens
- ✅ Listar, criar, editar e excluir comentários
- ✅ Formulário único para criar/editar mensagens
- ✅ Validação de formulários

### 🔐 Autenticação
- ✅ Login e cadastro de usuários
- ✅ Proteção de rotas com guards
- ✅ Token JWT armazenado no localStorage
- ✅ Interceptor Axios para adicionar token automaticamente
- ✅ Redirecionamento automático em caso de 401

### 🎨 UX/UI
- ✅ Mensagens de erro e sucesso
- ✅ Estados de carregamento
- ✅ Lista vazia
- ✅ Confirmação antes de deletar
- ✅ Validação de formulários

### 🔒 Segurança
- ✅ Verificação de propriedade (só o dono pode editar/excluir)
- ✅ Autenticação JWT em rotas protegidas
- ✅ CORS configurado

---

## 📝 Variáveis de Ambiente

### Backend
Crie um arquivo `.env` na pasta `backend/src/`:

```env
SECRET_KEY=sua-chave-secreta-aqui
JWT_SECRET_KEY=sua-chave-jwt-secreta-aqui
```

### Frontend
Crie um arquivo `.env` na pasta `frontend/`:

```env
VITE_API_URL=http://localhost:5000
```

---

## 🧪 Testando a Aplicação

1. **Cadastre-se** ou faça login
2. **Crie uma mensagem** através do botão "Nova Mensagem"
3. **Visualize** a mensagem clicando em "Ver"
4. **Adicione comentários** na mensagem
5. **Edite ou exclua** suas próprias mensagens/comentários
6. **Teste** que não consegue editar/excluir mensagens de outros usuários

---

## 📚 Documentação Adicional

- [Backend README](./backend/README.md) - Documentação completa do backend
- [Frontend README](./frontend/README.md) - Documentação completa do frontend

---

## 👨‍💻 Desenvolvido por

[Seu Nome]

---

## 📄 Licença

Este projeto foi desenvolvido como atividade acadêmica.

