<!-- src/views/DetalhesMensagemView.vue -->
<template>
  <div>
    <h1 class="titulo">📄 Detalhes da Mensagem</h1>

    <!-- Estado de carregamento -->
    <div v-if="carregando" class="estado carregando">
      ⏳ Carregando mensagem...
    </div>

    <!-- Estado de erro -->
    <div v-else-if="erro" class="estado erro">
      ⚠️ {{ erro }}
      <button class="btn-pequeno" @click="carregar">Tentar novamente</button>
    </div>

    <!-- Conteúdo da mensagem -->
    <div v-else-if="mensagem" class="mensagem-detalhes">
      <article class="card-mensagem">
        <header class="card-header">
          <h2>{{ mensagem.titulo }}</h2>
        </header>

        <section class="card-body">
          <p>{{ mensagem.conteudo }}</p>
        </section>

        <footer class="card-footer">
          <div class="meta">
            <small class="autor">👤 {{ mensagem.autor || 'Anônimo' }}</small>
            <small class="data">🕒 {{ formatarData(mensagem.data_criacao || mensagem.created_at) }}</small>
          </div>

          <div v-if="isOwner" class="acoes">
            <RouterLink :to="`/mensagens/editar/${mensagem.id}`" class="btn editar">
              ✏️ Editar
            </RouterLink>
            <button class="btn remover" @click="removerMensagem">
              🗑️ Excluir
            </button>
          </div>
        </footer>
      </article>

      <!-- Comentários -->
      <ComentariosList :mensagem-id="mensagem.id" />
    </div>

    <button class="voltar" @click="router.back()">⬅ Voltar</button>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { getMensagem, removerMensagem as removerMensagemService } from '@/services/mensagensService.js'
import { getUserId } from '@/services/authService.js'
import ComentariosList from '@/components/ComentariosList.vue'

const router = useRouter()
const route = useRoute()

const mensagem = ref(null)
const carregando = ref(true)
const erro = ref(null)

const userId = computed(() => getUserId())
const isOwner = computed(() => {
  if (!mensagem.value?.usuario_id || !userId.value) return false
  return String(mensagem.value.usuario_id) === String(userId.value)
})

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
    const id = route.params.id
    mensagem.value = await getMensagem(id)
    
    if (!mensagem.value) {
      erro.value = 'Mensagem não encontrada.'
    } else {
      // Normaliza o id
      mensagem.value.id = mensagem.value.id ?? mensagem.value._id ?? mensagem.value.uuid
    }
  } catch (e) {
    erro.value = e?.message || e?.erro || 'Erro ao carregar mensagem.'
  } finally {
    carregando.value = false
  }
}

async function removerMensagem() {
  if (!confirm('Deseja realmente excluir esta mensagem?')) return

  try {
    await removerMensagemService(mensagem.value.id)
    router.push('/mensagens')
  } catch (e) {
    alert(e?.message || 'Erro ao remover mensagem.')
  }
}

onMounted(carregar)
</script>

<style scoped>
.titulo {
  margin-bottom: 16px;
  font-size: 1.25rem;
}

.estado {
  padding: 12px;
  border-radius: 8px;
  margin-bottom: 12px;
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

.btn-pequeno {
  padding: 6px 10px;
  border-radius: 6px;
  background: #f3f4f6;
  border: 1px solid #e5e7eb;
  cursor: pointer;
  margin-top: 8px;
}

.mensagem-detalhes {
  margin-bottom: 24px;
}

.card-mensagem {
  padding: 20px;
  border-radius: 10px;
  border: 1px solid #e6e9ef;
  background: #fff;
  box-shadow: 0 4px 12px rgba(16, 24, 40, 0.04);
  margin-bottom: 24px;
}

.card-header h2 {
  font-size: 1.5rem;
  color: #111827;
  margin-bottom: 12px;
}

.card-body {
  color: #374151;
  margin-bottom: 16px;
  white-space: pre-wrap;
  line-height: 1.6;
}

.card-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
  padding-top: 16px;
  border-top: 1px solid #e5e7eb;
}

.meta {
  color: #6b7280;
  display: flex;
  gap: 12px;
  font-size: 0.9rem;
}

.acoes {
  display: flex;
  gap: 8px;
}

.btn {
  padding: 8px 12px;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 600;
  font-size: 0.9rem;
  border: none;
  cursor: pointer;
  display: inline-block;
}

.btn.editar {
  background: #3b82f6;
  color: #fff;
}

.btn.remover {
  background: #ef4444;
  color: #fff;
}

.btn:hover {
  opacity: 0.95;
}

.voltar {
  margin-top: 14px;
  padding: 8px 14px;
  background: #e5e7eb;
  border-radius: 6px;
  border: none;
  cursor: pointer;
}
</style>

