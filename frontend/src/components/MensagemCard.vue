<!-- src/components/MensagemCard.vue -->
<template>
  <article class="card">
    <header class="card-header">
      <slot name="titulo"></slot>
    </header>

    <section class="card-body">
      <slot name="conteudo"></slot>
    </section>

    <footer class="card-footer">
      <div class="meta">
        <small class="autor">👤 <slot name="autor"></slot></small>
        <small class="data">🕒 <slot name="data"></slot></small>
      </div>

      <div class="acoes">
        <RouterLink :to="`/mensagens/${id}`" class="btn ver">💬 Ver</RouterLink>
        <button v-if="isOwner" class="btn editar" @click="onEditar" aria-label="Editar mensagem">✏️ Editar</button>
        <button v-if="isOwner" class="btn remover" @click="onRemover" aria-label="Remover mensagem">🗑️ Excluir</button>
      </div>
    </footer>

    
  </article>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { computed } from 'vue'
import { getUserId } from '@/services/authService.js'

/* Props: id é necessário para identificar qual item a ação afeta */
const props = defineProps({
  id: {
    type: [String, Number],
    required: true
  },
  usuarioId: {
    type: [String, Number],
    default: null
  }
})

const userId = computed(() => getUserId())
const isOwner = computed(() => {
  if (!props.usuarioId || !userId.value) return false
  return String(props.usuarioId) === String(userId.value)
})

/* Declare explicitamente os eventos que o componente pode emitir */
const emit = defineEmits(['editar', 'remover'])

function onEditar() {
  emit('editar', props.id)
}

function onRemover() {
  emit('remover', props.id)
}
</script>

<style scoped>
.card {
  padding: 14px;
  border-radius: 10px;
  border: 1px solid #e6e9ef;
  background: #fff;
  box-shadow: 0 4px 12px rgba(16,24,40,0.04);
}
.card-header { font-weight: 700; color:#111827; margin-bottom:8px; }
.card-body { color:#374151; margin-bottom:10px; white-space:pre-wrap; }
.card-footer { display:flex; justify-content:space-between; align-items:center; gap:12px; }
.meta { color:#6b7280; display:flex; gap:8px; font-size:0.9rem; }
.acoes { display:flex; gap:8px; }
.btn { padding:6px 10px; border-radius:8px; border:none; cursor:pointer; font-weight:600; text-decoration:none; display:inline-block; }
.btn.ver { background:#10b981; color:#fff; }
.btn.editar { background:#3b82f6; color:#fff; }
.btn.remover { background:#ef4444; color:#fff; }
.btn:hover { opacity:0.95; }
</style>