<!-- src/components/MensagemForm.vue -->
<template>
  <form class="form" @submit.prevent="enviarMensagem">
    <div class="grupo">
      <label for="titulo">Título</label>
      <input id="titulo"
        v-model.trim="titulo"
        type="text"
        required
        placeholder="Digite o título"
      />
    </div>

    <div class="grupo">
      <label for="conteudo">Conteúdo</label>
      <textarea id="conteudo" v-model.trim="conteudo"
        rows="4"
        required
        placeholder="Escreva a mensagem"
      ></textarea>
    </div>

    <button class="enviar" type="submit">
      {{ modelo ? "Salvar Alterações" : "Adicionar Mensagem" }}
    </button>
  </form>
</template>

<script setup>
import { ref, watch, toRefs } from 'vue'

const props = defineProps({
  modelo: {
    type: Object,
    default: null
  }
})

const emit = defineEmits(['adicionar'])

// campos reativos
const titulo = ref('')
const conteudo = ref('')

// sempre que o modelo mudar (por exemplo navegação via rota), atualizamos os campos
watch(
  () => props.modelo,
  (novo) => {
    if (novo) {
      titulo.value = novo.titulo ?? ''
      conteudo.value = novo.conteudo ?? ''
    } else {
      // sem modelo: modo criação — limpa campos
      titulo.value = ''
      conteudo.value = ''
    }
  },
  { immediate: true }
)

function enviarMensagem() {
  // validação básica (já garantida pelo required nos inputs)
  if (!titulo.value || !conteudo.value) return

  emit('adicionar', {
    titulo: titulo.value,
    conteudo: conteudo.value
    // O autor vem automaticamente do JWT no backend
  })

  // se estiver no modo criação, limpar campos
  if (!props.modelo) {
    titulo.value = ''
    conteudo.value = ''
  }
}
</script>

<style scoped>
.form {
  display: flex;
  flex-direction: column;
  gap: 14px;
  margin: 12px 0;
}
.grupo {
  display: flex;
  flex-direction: column;
}
label {
  font-weight: 600;
  margin-bottom: 6px;
}
input,
textarea {
  border: 1px solid #d1d5db;
  padding: 10px;
  border-radius: 8px;
  font-size: 14px;
  outline: none;
}
input:focus,
textarea:focus {
  border-color: #42b983;
  box-shadow: 0 0 0 4px rgba(66,185,131,0.06);
}
.enviar {
  width: fit-content;
  background: #42b983;
  color: #fff;
  border: none;
  padding: 10px 14px;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
}
.enviar:hover { opacity: 0.95; }
</style>