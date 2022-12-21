<template>
  <h1>
    <img src="/images/logo.png" alt="" width="96" />
    My Page
  </h1>

  <template v-if="editing"> editing </template>
  <template v-else> normal </template>
</template>

<script setup lang="ts">
import { ref } from "vue";

const editing = ref(false);
</script>

<style scoped></style>
