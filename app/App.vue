<template>
  <header>
    <h1>{{ t("greeting") }}</h1>
  </header>

  <aside>
    <select @change="change">
      <option v-for="l in localeOptions" :key="l" :value="l">{{ l }}</option>
    </select>
  </aside>

  <main>
    <m-click-me :start="0" />
  </main>

</template>

<script setup lang="ts">
import { useI18n } from "vue-i18n";

import { useMemoRe } from "./lib";

import MClickMe from "./component/MClickMeButton.vue";

import messages from "./public/locales/ja.json";

const localeOptions = ["ja", "en"];

const { t, setLocaleMessage, locale: current } = useI18n<{ message: typeof messages }, typeof localeOptions[number]>();
const { fetch } = useMemoRe();

const change = (ev: Event) => {
  if (!(ev.target instanceof HTMLSelectElement)) {
    return;
  }

  changeLocale(ev.target.value);
};

const changeLocale = (locale: typeof localeOptions[number]) =>
  fetch<typeof messages>(`locales/${locale}.json`)
    .then((message) => setLocaleMessage(locale, message))
    .then(() => (current.value = locale))
    .then(() => document.querySelector("html")?.setAttribute("lang", locale));



</script>

<style scoped>
h1 {
  color: green;
}
</style>
