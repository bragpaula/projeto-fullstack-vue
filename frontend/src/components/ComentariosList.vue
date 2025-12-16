<!-- src/components/ComentariosList.vue -->
<template>
  <div class="comentarios-container">
    <div class="comentarios-header">
      <h3>💬 Comentários ({{ comentarios.length }})</h3>
      <button v-if="!mostrarForm" class="btn-adicionar" @click="mostrarForm = true">
        ➕ Adicionar Comentário
      </button>
    </div>

    <!-- Formulário de novo comentário -->
    <div v-if="mostrarForm" class="form-comentario">
      <ComentarioForm
        :mensagem-id="mensagemId"
        @salvar="onComentarioSalvo"
        @cancelar="mostrarForm = false"
      />
    </div>

    <!-- Estados -->
    <div v-if="carregando" class="estado carregando">
      ⏳ Carregando comentários...
    </div>

    <div v-else-if="erro" class="estado erro">
      ⚠️ {{ erro }}
      <button class="btn-pequeno" @click="carregar">Tentar novamente</button>
    </div>

    <div v-else-if="comentarios.length === 0" class="estado vazio">
      🗒️ Nenhum comentário ainda. Seja o primeiro a comentar!
    </div>

    <!-- Lista de comentários -->
    <div v-else class="lista-comentarios">
      <div
        v-for="(comentario, index) in comentarios"
        :key="comentario.id || index"
        class="comentario-item"
      >
        <div class="comentario-header">
          <span class="autor">👤 {{ comentario.autor || 'Anônimo' }}</span>
          <span class="data">{{ formatarData(comentario.data_criacao || comentario.created_at) }}</span>
        </div>
        <div class="comentario-texto">{{ comentario.conteudo }}</div>
        <div v-if="isOwnerOfMessage()" class="comentario-acoes">
          <button
            class="btn-editar"
            @click="editarComentario(comentario)"
            aria-label="Editar comentário"
          >
            ✏️ Editar
          </button>
          <button
            class="btn-remover"
            @click="removerComentario(comentario.id)"
            aria-label="Remover comentário"
          >
            🗑️ Excluir
          </button>
        </div>
      </div>
    </div>

    <!-- Formulário de edição -->
    <div v-if="comentarioEditando" class="form-comentario">
      <ComentarioForm
        :model="comentarioEditando"
        :mensagem-id="mensagemId"
        @salvar="onComentarioSalvo"
        @cancelar="comentarioEditando = null"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import {
  getComentarios,
  removerComentario as removerComentarioService
} from '@/services/comentariosService.js'
import { getUserId } from '@/services/authService.js'
import ComentarioForm from './ComentarioForm.vue'

const props = defineProps({
  mensagemId: {
    type: [String, Number],
    required: true
  }
})

const comentarios = ref([])
const mensagem = ref(null) // Para verificar o dono da mensagem
const carregando = ref(true)
const erro = ref(null)
const mostrarForm = ref(false)
const comentarioEditando = ref(null)

const userId = computed(() => getUserId())

// Verifica se o usuário é dono do comentário (comentários pertencem à mensagem, então só o dono da mensagem pode editar/excluir)
function isOwnerOfMessage() {
  if (!mensagem.value || !userId.value) return false
  return String(mensagem.value.usuario_id) === String(userId.value)
}

function formatarData(iso) {
  if (!iso) return ''
  return new Date(iso).toLocaleString('pt-BR', {
    dateStyle: 'short',
    timeStyle: 'short'
  })
}

async function carregar() {
  carregando.value = true
  erro.value = null
  try {
    const lista = await getComentarios(props.mensagemId)
    comentarios.value = (lista || []).map(c => ({
      ...c,
      id: c.id ?? c._id ?? c.uuid
    }))
    
    // Carrega também a mensagem para verificar o dono
    const { getMensagem } = await import('@/services/mensagensService.js')
    mensagem.value = await getMensagem(props.mensagemId)
  } catch (e) {
    erro.value = e?.message || e?.erro || 'Falha ao carregar comentários.'
  } finally {
    carregando.value = false
  }
}

function editarComentario(comentario) {
  comentarioEditando.value = { ...comentario }
  mostrarForm.value = false
}

async function removerComentario(id) {
  if (!confirm('Deseja realmente excluir este comentário?')) return

  try {
    await removerComentarioService(id)
    comentarios.value = comentarios.value.filter(c => String(c.id) !== String(id))
  } catch (e) {
    alert(e?.message || 'Erro ao remover comentário.')
  }
}

function onComentarioSalvo() {
  carregar()
  mostrarForm.value = false
  comentarioEditando.value = null
}

onMounted(carregar)
</script>

<style scoped>
.comentarios-container {
  margin-top: 24px;
  padding: 16px;
  border-radius: 8px;
  background: #f9fafb;
  border: 1px solid #e5e7eb;
}

.comentarios-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.comentarios-header h3 {
  margin: 0;
  font-size: 1.1rem;
  color: #111827;
}

.btn-adicionar {
  padding: 8px 12px;
  background: #3b82f6;
  color: #fff;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 600;
  font-size: 0.9rem;
}

.btn-adicionar:hover {
  background: #2563eb;
}

.form-comentario {
  margin-bottom: 16px;
}

.estado {
  padding: 12px;
  border-radius: 8px;
  margin-bottom: 12px;
  text-align: center;
}

.estado.carregando {
  background: #f3f4f6;
  color: #374151;
}

.estado.erro {
  background: #fff1f2;
  color: #991b1b;
  border: 1px solid #fecaca;
}

.estado.vazio {
  color: #6b7280;
  padding: 20px;
}

.btn-pequeno {
  padding: 6px 10px;
  border-radius: 6px;
  background: #f3f4f6;
  border: 1px solid #e5e7eb;
  cursor: pointer;
  margin-top: 8px;
}

.lista-comentarios {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.comentario-item {
  padding: 12px;
  background: #fff;
  border-radius: 8px;
  border: 1px solid #e5e7eb;
}

.comentario-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
  font-size: 0.85rem;
  color: #6b7280;
}

.comentario-texto {
  color: #374151;
  margin-bottom: 8px;
  white-space: pre-wrap;
  line-height: 1.5;
}

.comentario-acoes {
  display: flex;
  gap: 8px;
}

.btn-editar,
.btn-remover {
  padding: 6px 10px;
  border-radius: 6px;
  border: none;
  cursor: pointer;
  font-size: 0.85rem;
  font-weight: 600;
}

.btn-editar {
  background: #3b82f6;
  color: #fff;
}

.btn-remover {
  background: #ef4444;
  color: #fff;
}

.btn-editar:hover,
.btn-remover:hover {
  opacity: 0.9;
}
</style>

