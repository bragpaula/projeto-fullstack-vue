<!-- src/views/NovaMensagemView.vue -->
<template>
  <div>
    <h1 class="titulo">➕ Nova Mensagem</h1>

    <MensagemForm @adicionar="salvar" />

    <button class="voltar" @click="router.back()">⬅ Voltar</button>
  </div>
</template>

<script setup>
import MensagemForm from '@/components/MensagemForm.vue'
import { criarMensagem } from '@/services/mensagensService.js'
import { useRouter } from 'vue-router'

const router = useRouter()

async function salvar(dados) {
  try {
    await criarMensagem(dados)
    router.push('/mensagens')
  } catch (e) {
    alert(e?.message || 'Erro ao criar mensagem.')
  }
}
</script>

<style scoped>
.voltar {
  margin-top: 12px;
  padding: 6px 12px;
}
</style>

