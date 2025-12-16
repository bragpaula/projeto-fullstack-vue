<!-- src/views/EditarMensagemView.vue -->
<template>
  <div>
    <h1 class="titulo">✏️ Editar Mensagem</h1>

    <!-- Estado de carregamento -->
    <div v-if="carregando" class="estado carregando">
      Carregando dados da mensagem...
    </div>

    <!-- Estado de erro -->
    <div v-else-if="erro" class="estado erro">
      {{ erro }}
    </div>

    <!-- Formulário preenchido com os dados da mensagem (modelo) -->
    <div v-else>
      <MensagemForm
        :modelo="mensagem"
        @adicionar="atualizar"
      />

      <!-- Comentários -->
      <ComentariosList :mensagem-id="mensagem.id" />
    </div>

    <button class="voltar" @click="router.back()">⬅ Voltar</button>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getMensagem, atualizarMensagem } from '@/services/mensagensService.js'
import MensagemForm from '@/components/MensagemForm.vue'
import ComentariosList from '@/components/ComentariosList.vue'
import { useRouter } from 'vue-router'

// Recebe o id da rota (router configurado com props: true)
const props = defineProps({
  id: {
    type: String,
    required: true
  }
})

const router = useRouter()
const mensagem = ref(null)
const carregando = ref(true)
const erro = ref(null)

// Carrega apenas o recurso necessário usando GET /mensagens/:id
async function carregar() {
  carregando.value = true
  erro.value = null

  try {
    const dados = await getMensagem(props.id)

    if (!dados) {
      // Caso o backend retorne vazio ou null, tratamos como não encontrado
      erro.value = 'Mensagem não encontrada.'
      // opcional: redirecionar para 404
      // router.replace('/404')
    } else {
      // Normaliza o id
      mensagem.value = {
        ...dados,
        id: dados.id ?? dados._id ?? dados.uuid ?? props.id
      }
    }
  } catch (e) {
    // Se a API retornar um objeto de erro com message, use-o:
    erro.value = e?.message || e?.msg || 'Erro ao carregar mensagem.'
  } finally {
    carregando.value = false
  }
}

// Envia os dados atualizados via PUT /mensagens/:id
async function atualizar(dados) {
  try {
    await atualizarMensagem(props.id, dados)
    alert('Mensagem atualizada com sucesso!')
    // redireciona para a listagem
    router.push('/mensagens')
  } catch (e) {
    alert(e?.message || e?.msg || 'Erro ao atualizar mensagem.')
  }
}

onMounted(carregar)
</script>

<style scoped>
.titulo {
  margin-bottom: 12px;
  font-size: 1.25rem;
}
.estado {
  padding: 12px;
  border-radius: 8px;
  margin-bottom: 12px;
}
.estado.carregando { background: #f3f4f6; color: #374151; }
.estado.erro { background: #fff1f2; color: #991b1b; border: 1px solid #fecaca; }

.voltar {
  margin-top: 14px;
  padding: 8px 14px;
  background: #e5e7eb;
  border-radius: 6px;
  border: none;
  cursor: pointer;
}
</style>