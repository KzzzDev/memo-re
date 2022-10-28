<template>
  <header>
    <h1>{{ t("greeting") }}</h1>
  </header>

  <main>
    <m-click-me :start="0" />
  </main>
</template>

<script setup lang="ts">
import { useI18n } from "vue-i18n";

import MClickMe from "./component/MClickMeButton.vue";

import messages from "./public/locales/ja.json";

const localeOptions = ["ja", "en"];

const { t } = useI18n<{ message: typeof messages }, typeof localeOptions[number]>();
</script>

<style scoped>
h1 {
  color: green;
}
</style>
