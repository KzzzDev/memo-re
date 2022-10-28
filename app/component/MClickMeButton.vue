<template>
  <button type="button" @click="click++">Click me</button>
  <p>{{ t("click", click) }}</p>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { useI18n } from "vue-i18n";

import messages from "../public/locales/ja.json";

const { t } = useI18n<{ message: typeof messages }>();

const prop = defineProps({
  start: {
    type: Number,
    required: true,
  },
});

const click = ref(prop.start);
</script>
