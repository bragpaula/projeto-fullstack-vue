// src/services/comentariosService.js
import api from './api.js'

/**
 * Lista comentários de uma mensagem específica.
 * GET /mensagens/<id>/comentarios
 */
export async function getComentarios(mensagemId) {
  try {
    const resposta = await api.get(`/mensagens/${mensagemId}/comentarios`)
    return resposta.data
  } catch (erro) {
    throw erro.response?.data || {
      erro: 'NetworkError',
      message: 'Falha ao carregar comentários.',
      status: 500
    }
  }
}

/**
 * Busca um único comentário por ID.
 * Não existe endpoint específico no backend, mas podemos usar a lista
 */
export async function getComentario(id) {
  // Como não há endpoint específico, retornamos null
  // ou podemos buscar de outra forma se necessário
  return null
}

/**
 * Cria um novo comentário.
 * POST /mensagens/<id>/comentarios
 */
export async function criarComentario(mensagemId, dados) {
  try {
    // O backend espera 'conteudo' (não 'texto') e o autor vem do JWT
    const resposta = await api.post(`/mensagens/${mensagemId}/comentarios`, {
      conteudo: dados.texto || dados.conteudo
    })
    return resposta.data
  } catch (erro) {
    throw erro.response?.data || {
      erro: 'NetworkError',
      message: 'Falha ao criar comentário.',
      status: 500
    }
  }
}

/**
 * Atualiza um comentário existente.
 * PUT /mensagens/comentarios/<id>
 */
export async function atualizarComentario(id, dados) {
  try {
    // O backend espera 'conteudo' (não 'texto')
    const resposta = await api.put(`/mensagens/comentarios/${id}`, {
      conteudo: dados.texto || dados.conteudo
    })
    return resposta.data
  } catch (erro) {
    throw erro.response?.data || {
      erro: 'NetworkError',
      message: 'Falha ao atualizar comentário.',
      status: 500
    }
  }
}

/**
 * Remove um comentário.
 * DELETE /mensagens/comentarios/<id>
 */
export async function removerComentario(id) {
  try {
    const resposta = await api.delete(`/mensagens/comentarios/${id}`)
    return resposta.data
  } catch (erro) {
    throw erro.response?.data || {
      erro: 'NetworkError',
      message: 'Falha ao remover comentário.',
      status: 500
    }
  }
}
