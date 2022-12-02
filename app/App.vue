<template>
  <header>

  </header>

  <main>
    <!-- main内にRouter View配置 -->
    <router-view/>
  </main>

  <footer>
    <!--    Footer使わないかも-->
  </footer>

</template>

<script setup lang="ts">
import { useI18n } from "vue-i18n";

import MClickMe from "./component/MClickMeButton.vue";

import messages from "./public/locales/ja.json";

const localeOptions = ["ja", "en"];

const { t, setLocaleMessage, locale: current } = useI18n<{ message: typeof messages }, typeof localeOptions[number]>();

const change = (ev: Event) => {
  if (!(ev.target instanceof HTMLSelectElement)) {
    return;
  }

  changeLocale(ev.target.value);
};

const changeLocale = (locale: typeof localeOptions[number]) =>
  fetch(`locales/${locale}.json`)
    .then((res) => res.json())
    .then((message) => setLocaleMessage(locale, message))
    .then(() => (current.value = locale))
    .then(() => document.querySelector("html")?.setAttribute("lang", locale));



</script>

<style>


</style>
