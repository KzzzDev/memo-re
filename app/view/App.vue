<template>
  <header>
    <h1>{{ $t("greeting") }}</h1>
  </header>

  <main>
    <m-click-me :start="0" />
  </main>
</template>

<script setup lang="ts">
import MClickMe from "../component/MClickMeButton.vue";
</script>

<style scoped>
h1 {
  color: green;
}
</style>
