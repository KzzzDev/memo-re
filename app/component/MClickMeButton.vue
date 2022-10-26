<template>
  <button type="button" @click="click++">Click me</button>
  <p>{{ $tc("click", click) }}</p>
</template>

<script setup lang="ts">
import { ref } from "vue";

const prop = defineProps({
  start: {
    type: Number,
    required: true,
  },
});

const click = ref(prop.start);
</script>
