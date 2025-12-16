// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import { isAuthenticated } from '@/services/authService.js'

// Importação das views
import MensagensView from '@/views/MensagensView.vue'
import NovaMensagemView from '@/views/NovaMensagemView.vue'
import EditarMensagemView from '@/views/EditarMensagemView.vue'
import DetalhesMensagemView from '@/views/DetalhesMensagemView.vue'
import LoginView from '@/views/LoginView.vue'
import CadastroView from '@/views/CadastroView.vue'

// Guard de autenticação
function requireAuth(to, from, next) {
  if (isAuthenticated()) {
    next()
  } else {
    next({ name: 'login', query: { redirect: to.fullPath } })
  }
}

// Guard para rotas públicas (redireciona se já estiver autenticado)
function requireGuest(to, from, next) {
  if (isAuthenticated()) {
    next({ name: 'mensagens' })
  } else {
    next()
  }
}

const router = createRouter({
  history: createWebHistory(),

  routes: [
    {
      path: '/',
      redirect: '/mensagens'
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
      beforeEnter: requireGuest
    },
    {
      path: '/cadastro',
      name: 'cadastro',
      component: CadastroView,
      beforeEnter: requireGuest
    },
    {
      path: '/mensagens',
      name: 'mensagens',
      component: MensagensView,
      beforeEnter: requireAuth
    },
    {
      path: '/mensagens/nova',
      name: 'mensagens-nova',
      component: NovaMensagemView,
      beforeEnter: requireAuth
    },
    {
      path: '/mensagens/:id',
      name: 'mensagens-detalhes',
      component: DetalhesMensagemView,
      props: true,
      beforeEnter: requireAuth
    },
    {
      path: '/mensagens/editar/:id',
      name: 'mensagens-editar',
      component: EditarMensagemView,
      props: true,
      beforeEnter: requireAuth
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'not-found',
      component: () => import('@/views/NotFoundView.vue')
    }
  ]
})

export default router