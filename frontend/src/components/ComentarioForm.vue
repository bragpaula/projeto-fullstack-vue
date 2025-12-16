<!-- src/components/ComentarioForm.vue -->
<template>
  <form @submit.prevent="salvar" class="form-comentario">
    <div class="campo">
      <label for="texto">Comentário:</label>
      <textarea
        id="texto"
        v-model="form.texto"
        required
        placeholder="Digite seu comentário..."
        rows="3"
        :disabled="carregando"
      ></textarea>
    </div>

    <div class="acoes">
      <button type="submit" class="btn-salvar" :disabled="carregando">
        {{ carregando ? 'Salvando...' : (model ? 'Atualizar' : 'Comentar') }}
      </button>
      <button
        type="button"
        class="btn-cancelar"
        @click="cancelar"
        :disabled="carregando"
      >
        Cancelar
      </button>
    </div>
  </form>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import {
  criarComentario,
  atualizarComentario
} from '@/services/comentariosService.js'

const props = defineProps({
  model: {
    type: Object,
    default: null
  },
  mensagemId: {
    type: [String, Number],
    required: true
  }
})

const emit = defineEmits(['salvar', 'cancelar'])

const form = ref({
  texto: ''
})

const carregando = ref(false)

onMounted(() => {
  if (props.model) {
    // Modo edição: preenche campos
    form.value = {
      texto: props.model.conteudo || props.model.texto || ''
    }
  }
})

async function salvar() {
  if (!form.value.texto.trim()) {
    alert('O comentário não pode estar vazio.')
    return
  }

  carregando.value = true

  try {
    if (props.model) {
      // Atualizar - precisa do id do comentário
      await atualizarComentario(props.model.id, {
        texto: form.value.texto,
        conteudo: form.value.texto
      })
    } else {
      // Criar - passa mensagemId e dados
      await criarComentario(props.mensagemId, {
        texto: form.value.texto,
        conteudo: form.value.texto
      })
    }

    emit('salvar')
  } catch (e) {
    alert(e?.message || e?.erro || 'Erro ao salvar comentário.')
  } finally {
    carregando.value = false
  }
}

function cancelar() {
  emit('cancelar')
}
</script>

<style scoped>
.form-comentario {
  padding: 12px;
  background: #fff;
  border-radius: 8px;
  border: 1px solid #e5e7eb;
}

.campo {
  display: flex;
  flex-direction: column;
  gap: 6px;
  margin-bottom: 12px;
}

.campo label {
  font-weight: 600;
  color: #374151;
  font-size: 0.9rem;
}

.campo input,
.campo textarea {
  padding: 8px 10px;
  border: 1px solid #d1d5db;
  border-radius: 6px;
  font-size: 0.95rem;
  font-family: inherit;
  resize: vertical;
}

.campo input:focus,
.campo textarea:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.campo input:disabled,
.campo textarea:disabled {
  background: #f3f4f6;
  cursor: not-allowed;
}

.autor-info {
  padding: 8px;
  background: #f3f4f6;
  border-radius: 6px;
  color: #6b7280;
  font-size: 0.9rem;
}

.acoes {
  display: flex;
  gap: 8px;
  margin-top: 12px;
}

.btn-salvar,
.btn-cancelar {
  padding: 8px 16px;
  border-radius: 6px;
  border: none;
  cursor: pointer;
  font-weight: 600;
  font-size: 0.9rem;
}

.btn-salvar {
  background: #3b82f6;
  color: #fff;
}

.btn-salvar:hover:not(:disabled) {
  background: #2563eb;
}

.btn-cancelar {
  background: #f3f4f6;
  color: #374151;
  border: 1px solid #e5e7eb;
}

.btn-cancelar:hover:not(:disabled) {
  background: #e5e7eb;
}

.btn-salvar:disabled,
.btn-cancelar:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
</style>

