<template>
  <div class="app">
    <header class="header" v-if="isAuthenticated">
      <div class="header-content">
        <h1 class="logo">📬 Sistema de Mensagens</h1>
        <nav class="nav">
          <RouterLink to="/mensagens" class="nav-link">Mensagens</RouterLink>
          <RouterLink to="/mensagens/nova" class="nav-link">Nova Mensagem</RouterLink>
          <button class="btn-logout" @click="fazerLogout">🚪 Sair</button>
        </nav>
      </div>
    </header>
    <main class="container">
      <RouterView />
    </main>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { isAuthenticated, logout, getUser } from '@/services/authService.js'

const router = useRouter()

const user = computed(() => getUser())

function fazerLogout() {
  if (confirm('Deseja realmente sair?')) {
    logout()
    router.push('/login')
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
  background: #f9fafb;
  color: #111827;
}

.app {
  min-height: 100vh;
}

.header {
  background: #fff;
  border-bottom: 1px solid #e5e7eb;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  margin-bottom: 24px;
}

.header-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 16px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  font-size: 1.25rem;
  color: #111827;
}

.nav {
  display: flex;
  gap: 16px;
  align-items: center;
}

.nav-link {
  color: #374151;
  text-decoration: none;
  font-weight: 500;
  padding: 6px 12px;
  border-radius: 6px;
  transition: background 0.2s;
}

.nav-link:hover {
  background: #f3f4f6;
}

.nav-link.router-link-active {
  color: #3b82f6;
  background: #eff6ff;
}

.btn-logout {
  padding: 6px 12px;
  background: #ef4444;
  color: #fff;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 500;
  transition: background 0.2s;
}

.btn-logout:hover {
  background: #dc2626;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px 40px;
}
</style>
