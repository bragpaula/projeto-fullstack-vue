<!-- src/views/CadastroView.vue -->
<template>
  <div class="auth-container">
    <div class="auth-card">
      <h1 class="titulo">📝 Cadastro</h1>

      <div v-if="erro" class="erro-mensagem">
        ⚠️ {{ erro }}
      </div>

      <div v-if="sucesso" class="sucesso-mensagem">
        ✅ {{ sucesso }}
      </div>

      <form @submit.prevent="fazerCadastro" class="form">
        <div class="campo">
          <label for="nome">Nome:</label>
          <input
            id="nome"
            v-model="form.nome"
            type="text"
            required
            placeholder="Seu nome completo"
            :disabled="carregando"
          />
        </div>

        <div class="campo">
          <label for="email">Email:</label>
          <input
            id="email"
            v-model="form.email"
            type="email"
            required
            placeholder="seu@email.com"
            :disabled="carregando"
          />
        </div>

        <div class="campo">
          <label for="senha">Senha:</label>
          <input
            id="senha"
            v-model="form.senha"
            type="password"
            required
            placeholder="••••••••"
            minlength="6"
            :disabled="carregando"
          />
        </div>

        <div class="campo">
          <label for="confirmarSenha">Confirmar Senha:</label>
          <input
            id="confirmarSenha"
            v-model="form.confirmarSenha"
            type="password"
            required
            placeholder="••••••••"
            :disabled="carregando"
          />
        </div>

        <div v-if="senhasNaoConferem" class="erro-mensagem">
          ⚠️ As senhas não conferem
        </div>

        <button type="submit" class="btn-submit" :disabled="carregando || senhasNaoConferem">
          {{ carregando ? 'Cadastrando...' : 'Cadastrar' }}
        </button>
      </form>

      <div class="links">
        <p>
          Já tem conta?
          <RouterLink to="/login">Faça login aqui</RouterLink>
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { cadastro } from '@/services/authService.js'

const router = useRouter()

const form = ref({
  nome: '',
  email: '',
  senha: '',
  confirmarSenha: ''
})

const carregando = ref(false)
const erro = ref(null)
const sucesso = ref(null)

const senhasNaoConferem = computed(() => {
  return form.value.senha && form.value.confirmarSenha && 
         form.value.senha !== form.value.confirmarSenha
})

async function fazerCadastro() {
  if (senhasNaoConferem.value) {
    erro.value = 'As senhas não conferem'
    return
  }

  carregando.value = true
  erro.value = null
  sucesso.value = null

  try {
    await cadastro({
      nome: form.value.nome,
      email: form.value.email,
      senha: form.value.senha
    })
    
    sucesso.value = 'Cadastro realizado com sucesso! Redirecionando...'
    
    // Redireciona após 1 segundo
    setTimeout(() => {
      router.push('/mensagens')
    }, 1000)
  } catch (e) {
    erro.value = e?.message || e?.erro || 'Erro ao realizar cadastro. Tente novamente.'
  } finally {
    carregando.value = false
  }
}
</script>

<style scoped>
.auth-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 80vh;
  padding: 20px;
}

.auth-card {
  width: 100%;
  max-width: 400px;
  padding: 32px;
  border-radius: 12px;
  border: 1px solid #e6e9ef;
  background: #fff;
  box-shadow: 0 4px 12px rgba(16, 24, 40, 0.08);
}

.titulo {
  font-size: 1.5rem;
  margin-bottom: 24px;
  text-align: center;
  color: #111827;
}

.form {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.campo {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.campo label {
  font-weight: 600;
  color: #374151;
  font-size: 0.9rem;
}

.campo input {
  padding: 10px 12px;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  font-size: 1rem;
  transition: border-color 0.2s;
}

.campo input:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.campo input:disabled {
  background: #f3f4f6;
  cursor: not-allowed;
}

.btn-submit {
  padding: 12px;
  background: #3b82f6;
  color: #fff;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s;
  margin-top: 8px;
}

.btn-submit:hover:not(:disabled) {
  background: #2563eb;
}

.btn-submit:disabled {
  background: #9ca3af;
  cursor: not-allowed;
}

.erro-mensagem {
  padding: 12px;
  background: #fff1f2;
  color: #991b1b;
  border: 1px solid #fecaca;
  border-radius: 8px;
  margin-bottom: 16px;
  font-size: 0.9rem;
}

.sucesso-mensagem {
  padding: 12px;
  background: #f0fdf4;
  color: #166534;
  border: 1px solid #bbf7d0;
  border-radius: 8px;
  margin-bottom: 16px;
  font-size: 0.9rem;
}

.links {
  margin-top: 20px;
  text-align: center;
  color: #6b7280;
  font-size: 0.9rem;
}

.links a {
  color: #3b82f6;
  text-decoration: none;
  font-weight: 600;
}

.links a:hover {
  text-decoration: underline;
}
</style>

