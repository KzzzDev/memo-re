<template>
  <form @submit.prevent="login">
    <input type="text" autocomplete="username" v-model="email" />
    <input type="password" autocomplete="password" v-model="password" />
    <input type="submit" value="ログイン" />
  </form>
</template>

<script setup lang="ts">
import { ref } from "vue";

import { useBackend } from "../../lib/compositions";
import { logIn } from "../../lib/network";

const email = ref("");
const password = ref("");

const { data, error, refresh: login } = useBackend(logIn, false, { email, password });
</script>

<style scoped></style>
