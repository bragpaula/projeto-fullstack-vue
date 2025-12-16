// src/services/authService.js
import api from './api.js'

const TOKEN_KEY = 'auth_token'
const USER_KEY = 'auth_user'

/**
 * Realiza login do usuário
 * POST /auth/login
 */
export async function login(credenciais) {
  try {
    const resposta = await api.post('/auth/login', credenciais)
    const { accessToken, user } = resposta.data
    
    // Armazena token e usuário no localStorage
    localStorage.setItem(TOKEN_KEY, accessToken)
    if (user) {
      localStorage.setItem(USER_KEY, JSON.stringify(user))
    }
    
    return { accessToken, user }
  } catch (erro) {
    throw erro.response?.data || {
      erro: 'NetworkError',
      message: 'Falha ao realizar login.',
      status: 500
    }
  }
}

/**
 * Realiza cadastro de novo usuário
 * POST /auth/register ou /auth/cadastro (depende do seu backend)
 */
export async function cadastro(dados) {
  try {
    const resposta = await api.post('/auth/register', dados)
    const { accessToken, user } = resposta.data
    
    // Armazena token e usuário no localStorage
    localStorage.setItem(TOKEN_KEY, accessToken)
    if (user) {
      localStorage.setItem(USER_KEY, JSON.stringify(user))
    }
    
    return { accessToken, user }
  } catch (erro) {
    throw erro.response?.data || {
      erro: 'NetworkError',
      message: 'Falha ao realizar cadastro.',
      status: 500
    }
  }
}

/**
 * Faz logout removendo token e usuário do localStorage
 */
export function logout() {
  localStorage.removeItem(TOKEN_KEY)
  localStorage.removeItem(USER_KEY)
}

/**
 * Verifica se o usuário está autenticado
 */
export function isAuthenticated() {
  return !!localStorage.getItem(TOKEN_KEY)
}

/**
 * Retorna o token armazenado
 */
export function getToken() {
  return localStorage.getItem(TOKEN_KEY)
}

/**
 * Retorna o usuário armazenado
 */
export function getUser() {
  const userStr = localStorage.getItem(USER_KEY)
  if (!userStr) return null
  try {
    return JSON.parse(userStr)
  } catch {
    return null
  }
}

/**
 * Retorna o ID do usuário do token JWT
 * Flask-JWT-Extended armazena o identity no campo 'sub'
 */
export function getUserId() {
  const token = getToken()
  if (!token) return null
  
  try {
    // Decodifica o JWT (formato: header.payload.signature)
    const parts = token.split('.')
    if (parts.length !== 3) return null
    
    const payload = parts[1]
    if (!payload) return null
    
    // Decodifica base64 (adiciona padding se necessário)
    let base64 = payload.replace(/-/g, '+').replace(/_/g, '/')
    while (base64.length % 4) {
      base64 += '='
    }
    
    const decoded = JSON.parse(atob(base64))
    
    // Flask-JWT-Extended usa 'sub' para armazenar o identity (user_id)
    return decoded.sub || decoded.identity || null
  } catch (e) {
    console.error('Erro ao decodificar token:', e)
    return null
  }
}

