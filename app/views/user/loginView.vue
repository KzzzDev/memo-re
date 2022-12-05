<template>
  <form @submit.prevent="login">
    <input type="text" autocomplete="username" v-model="email" />
    <input type="password" autocomplete="password" v-model="password" />
    <p v-if="!!error" class="error">メールアドレスかパスワードが間違っている</p>
    <input type="submit" value="ログイン" />
  </form>
</template>

<script setup lang="ts">
import { ref, watch } from "vue";
import { useRouter } from "vue-router";

import { useBackend } from "../../lib/compositions";
import { logIn } from "../../lib/network";

const { push } = useRouter();

const email = ref("");
const password = ref("");

const { data, error, refresh: login } = useBackend(logIn, false, { email, password });
watch(data, (value) => !!value && push({ path: "/mypage" }));
</script>

<style scoped></style>
