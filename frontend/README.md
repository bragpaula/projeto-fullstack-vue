# 🎨 Frontend - Vue.js 3

Aplicação Single Page Application (SPA) desenvolvida em Vue.js 3 com Vite, Vue Router e Axios para consumo da API REST.

## 🚀 Tecnologias

- **Vue.js** 3.5.24 - Framework JavaScript
- **Vue Router** 4.6.3 - Roteamento SPA
- **Vite** 7.2.2 - Build tool e dev server
- **Axios** 1.13.2 - Cliente HTTP
- **JavaScript (ES6+)**

---

## 📁 Estrutura

```
frontend/
├── src/
│   ├── components/          # Componentes Vue reutilizáveis
│   │   ├── MensagemCard.vue      # Card de exibição de mensagem
│   │   ├── MensagemForm.vue      # Formulário criar/editar mensagem
│   │   ├── ComentariosList.vue   # Lista de comentários
│   │   └── ComentarioForm.vue    # Formulário criar/editar comentário
│   │
│   ├── views/                # Views/páginas da aplicação
│   │   ├── LoginView.vue         # Tela de login
│   │   ├── CadastroView.vue      # Tela de cadastro
│   │   ├── MensagensView.vue     # Lista de mensagens
│   │   ├── NovaMensagemView.vue  # Criar nova mensagem
│   │   ├── EditarMensagemView.vue # Editar mensagem
│   │   ├── DetalhesMensagemView.vue # Detalhes + comentários
│   │   └── NotFoundView.vue      # Página 404
│   │
│   ├── router/               # Configuração do Vue Router
│   │   └── index.js              # Rotas e guards de autenticação
│   │
│   ├── services/             # Serviços API
│   │   ├── api.js                # Configuração Axios + interceptors
│   │   ├── authService.js        # Autenticação (login, cadastro)
│   │   ├── mensagensService.js   # CRUD de mensagens
│   │   └── comentariosService.js # CRUD de comentários
│   │
│   ├── App.vue              # Componente raiz
│   ├── main.js              # Entry point
│   └── style.css            # Estilos globais
│
├── package.json             # Dependências e scripts
├── vite.config.js          # Configuração do Vite
└── README.md              # Este arquivo
```

---

## 🔧 Instalação

### 1. Instalar dependências

```bash
cd frontend
npm install
```

### 2. Configurar variáveis de ambiente

Crie um arquivo `.env` na pasta `frontend/`:

```env
VITE_API_URL=http://localhost:5000
```

**Nota:** Ajuste a URL se o backend estiver rodando em outra porta.

---

## 🚀 Executando

### Modo Desenvolvimento

```bash
npm run dev
```

A aplicação estará rodando em `http://localhost:5173`

### Build para Produção

```bash
npm run build
```

Os arquivos serão gerados na pasta `dist/`

### Preview da Build

```bash
npm run preview
```

---

## 🗺️ Rotas

| Rota | Componente | Descrição | Protegida |
|------|-----------|-----------|-----------|
| `/` | - | Redireciona para `/mensagens` | - |
| `/login` | `LoginView` | Tela de login | ❌ |
| `/cadastro` | `CadastroView` | Tela de cadastro | ❌ |
| `/mensagens` | `MensagensView` | Lista de mensagens | ✅ |
| `/mensagens/nova` | `NovaMensagemView` | Criar mensagem | ✅ |
| `/mensagens/:id` | `DetalhesMensagemView` | Detalhes + comentários | ✅ |
| `/mensagens/editar/:id` | `EditarMensagemView` | Editar mensagem | ✅ |
| `/:pathMatch(.*)*` | `NotFoundView` | Página 404 | - |

---

## 🔐 Autenticação

### Guards de Rota

- **`requireAuth`**: Protege rotas que precisam de autenticação
  - Redireciona para `/login` se não autenticado
  - Salva a rota original para redirecionar após login

- **`requireGuest`**: Protege rotas públicas (login/cadastro)
  - Redireciona para `/mensagens` se já autenticado

### Armazenamento

- **Token JWT**: Armazenado em `localStorage` como `auth_token`
- **Dados do usuário**: Armazenados em `localStorage` como `auth_user`

### Interceptor Axios

O interceptor em `services/api.js`:
- Adiciona automaticamente o token JWT em todas as requisições
- Trata erros 401 (não autorizado) redirecionando para login

---

## 📡 Serviços API

### `authService.js`

```javascript
import { login, cadastro, logout, getUser, getUserId } from '@/services/authService.js'

// Login
await login({ email: '...', senha: '...' })

// Cadastro
await cadastro({ nome: '...', email: '...', senha: '...' })

// Logout
logout()

// Obter usuário atual
const user = getUser()

// Obter ID do usuário do token
const userId = getUserId()
```

### `mensagensService.js`

```javascript
import { 
  getMensagens, 
  getMensagem, 
  criarMensagem, 
  atualizarMensagem, 
  removerMensagem 
} from '@/services/mensagensService.js'

// Listar todas
const mensagens = await getMensagens()

// Buscar uma
const mensagem = await getMensagem(id)

// Criar
await criarMensagem({ titulo: '...', conteudo: '...' })

// Atualizar
await atualizarMensagem(id, { titulo: '...', conteudo: '...' })

// Remover
await removerMensagem(id)
```

### `comentariosService.js`

```javascript
import { 
  getComentarios, 
  criarComentario, 
  atualizarComentario, 
  removerComentario 
} from '@/services/comentariosService.js'

// Listar comentários de uma mensagem
const comentarios = await getComentarios(mensagemId)

// Criar comentário
await criarComentario(mensagemId, { conteudo: '...' })

// Atualizar comentário
await atualizarComentario(id, { conteudo: '...' })

// Remover comentário
await removerComentario(id)
```

---

## 🎨 Componentes

### `MensagemCard.vue`
Card para exibir mensagem na lista.

**Props:**
- `id` - ID da mensagem
- `usuarioId` - ID do usuário dono da mensagem

**Slots:**
- `titulo` - Título da mensagem
- `conteudo` - Conteúdo da mensagem
- `autor` - Nome do autor
- `data` - Data de criação

**Eventos:**
- `@editar` - Emitido ao clicar em editar
- `@remover` - Emitido ao clicar em excluir

### `MensagemForm.vue`
Formulário único para criar/editar mensagem.

**Props:**
- `modelo` - Objeto da mensagem (null para criar, objeto para editar)

**Eventos:**
- `@adicionar` - Emitido ao salvar (recebe dados da mensagem)

### `ComentariosList.vue`
Lista e gerencia comentários de uma mensagem.

**Props:**
- `mensagemId` - ID da mensagem

**Funcionalidades:**
- Lista comentários
- Adiciona novo comentário
- Edita comentário (se for dono da mensagem)
- Remove comentário (se for dono da mensagem)

### `ComentarioForm.vue`
Formulário para criar/editar comentário.

**Props:**
- `mensagemId` - ID da mensagem
- `model` - Objeto do comentário (null para criar, objeto para editar)

**Eventos:**
- `@salvar` - Emitido ao salvar
- `@cancelar` - Emitido ao cancelar

---

## ✨ Funcionalidades

### ✅ CRUD Completo
- ✅ Listar mensagens
- ✅ Criar mensagem
- ✅ Editar mensagem (apenas dono)
- ✅ Excluir mensagem (apenas dono)
- ✅ Listar comentários
- ✅ Criar comentário
- ✅ Editar comentário (apenas dono da mensagem)
- ✅ Excluir comentário (apenas dono da mensagem)

### 🔐 Autenticação
- ✅ Login
- ✅ Cadastro
- ✅ Logout
- ✅ Proteção de rotas
- ✅ Verificação de propriedade

### 🎨 UX/UI
- ✅ Estados de carregamento
- ✅ Mensagens de erro
- ✅ Mensagens de sucesso
- ✅ Lista vazia
- ✅ Confirmação antes de deletar
- ✅ Validação de formulários
- ✅ Navegação intuitiva

---

## 🐛 Troubleshooting

### Erro de conexão com API
1. Verifique se o backend está rodando em `http://localhost:5000`
2. Verifique o arquivo `.env` com `VITE_API_URL`
3. Verifique o console do navegador para erros de CORS

### Erro 401 (Não autorizado)
1. Faça logout e login novamente
2. Verifique se o token está sendo enviado (Network tab)
3. Verifique se o token não expirou

### Rotas não funcionando
1. Certifique-se de estar usando `<RouterLink>` e não `<a>`
2. Verifique se o Vue Router está configurado em `main.js`
3. Verifique se as rotas estão definidas em `router/index.js`

---

## 📝 Notas

- O autor dos comentários é automaticamente preenchido pelo backend (não precisa informar)
- Botões de editar/excluir aparecem apenas para o dono do conteúdo
- O token JWT é decodificado para obter o ID do usuário
- Todas as requisições incluem automaticamente o token JWT via interceptor

---

## 👨‍💻 Desenvolvido por

[Seu Nome]
