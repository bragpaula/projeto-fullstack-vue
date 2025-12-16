<!-- src/views/LoginView.vue -->
<template>
  <div class="auth-container">
    <div class="auth-card">
      <h1 class="titulo">🔐 Login</h1>

      <div v-if="erro" class="erro-mensagem">
        ⚠️ {{ erro }}
      </div>

      <form @submit.prevent="fazerLogin" class="form">
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
            :disabled="carregando"
          />
        </div>

        <button type="submit" class="btn-submit" :disabled="carregando">
          {{ carregando ? 'Entrando...' : 'Entrar' }}
        </button>
      </form>

      <div class="links">
        <p>
          Não tem conta?
          <RouterLink to="/cadastro">Cadastre-se aqui</RouterLink>
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { login } from '@/services/authService.js'

const router = useRouter()
const route = useRoute()

const form = ref({
  email: '',
  senha: ''
})

const carregando = ref(false)
const erro = ref(null)

async function fazerLogin() {
  carregando.value = true
  erro.value = null

  try {
    await login({
      email: form.value.email,
      senha: form.value.senha
    })
    
    // Redireciona para a página que o usuário tentou acessar ou para mensagens
    const redirect = route.query.redirect || '/mensagens'
    router.push(redirect)
  } catch (e) {
    erro.value = e?.message || e?.erro || 'Erro ao fazer login. Verifique suas credenciais.'
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

