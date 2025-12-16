<!-- src/views/MensagensView.vue -->
<template>
  <div>
    <h1 class="titulo">📬 Mensagens</h1>

    <div class="acoes-topo">
      <RouterLink class="btn" to="/mensagens/nova">➕ Nova Mensagem</RouterLink>
    </div>

    <!-- Estados -->
    <div v-if="carregando" class="estado carregando">⏳ Carregando mensagens...</div>

    <div v-else-if="erro" class="estado erro">
      ⚠️ {{ erro }}
      <div style="margin-top:8px;">
        <button class="btn-pequeno" @click="carregar">Tentar novamente</button>
      </div>
    </div>

    <div v-else-if="mensagens.length === 0" class="estado vazio">
      🗒️ Nenhuma mensagem encontrada.
    </div>

    <!-- Lista de mensagens -->
    <div v-else class="lista-mensagens">
      <MensagemCard v-for="msg in mensagens"
        :key="msg.id"
        :id="msg.id"
        :usuario-id="msg.usuario_id"
        @editar="onEditarMensagem"
        @remover="onRemoverMensagem"
      >
        <template #titulo>{{ msg.titulo }}</template>
        <template #conteudo>{{ msg.conteudo }}</template>
        <template #autor>{{ msg.autor }}</template>
        <template #data>{{ formatarData(msg.data_criacao || msg.created_at) }}</template>
      </MensagemCard>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getMensagens, removerMensagem } from '@/services/mensagensService.js'
import MensagemCard from '@/components/MensagemCard.vue'
import { useRouter } from 'vue-router'

const mensagens = ref([])
const carregando = ref(true)
const erro = ref(null)

const router = useRouter()

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
    const lista = await getMensagens()
    // Normalize o id caso a API use _id / uuid
    mensagens.value = (lista || []).map(m => ({
      ...m,
      id: m.id ?? m._id ?? m.uuid
    }))
  } catch (e) {
    erro.value = e?.message || e?.msg || 'Falha ao carregar mensagens.'
  } finally {
    carregando.value = false
  }
}

function onEditarMensagem(id) {
  // navegação programática por nome ou caminho
  router.push({ name: 'mensagens-editar', params: { id } })
}

async function onRemoverMensagem(id) {
  if (!confirm('Deseja realmente excluir esta mensagem?')) return

  try {
    carregando.value = true
    await removerMensagem(id)
    // atualizar lista local — filtra o item removido
    mensagens.value = mensagens.value.filter(m => String(m.id) !== String(id))
  } catch (e) {
    alert(e?.message || 'Erro ao remover mensagem.')
  } finally {
    carregando.value = false
  }
}

onMounted(carregar)
</script>

<style scoped>
.titulo { font-size: 1.25rem; margin-bottom: 8px; }
.acoes-topo { margin-bottom: 12px; }
.btn { display:inline-block; padding:8px 12px; background:#42b983; color:#fff; border-radius:6px; text-decoration:none; }
.btn-pequeno { padding:6px 10px; border-radius:6px; background:#f3f4f6; border:1px solid #e5e7eb; cursor:pointer; }
.lista-mensagens { display: grid; gap: 12px; margin-top: 12px; }
.estado { padding: 12px; border-radius: 8px; margin-bottom: 12px; }
.estado.carregando { background:#f3f4f6; color:#374151; }
.estado.erro { background:#fff1f2; color:#991b1b; border:1px solid #fecaca; }
.estado.vazio { color:#6b7280; }
</style>