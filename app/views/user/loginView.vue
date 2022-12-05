<template>
  <form @submit.prevent="tryLogin">
    <label>
      メールアドレス
      <input type="text" autocomplete="username" v-model="email" />
    </label>
    <p class="error" v-if="!!eError">{{ eError }}</p>
    <label>
      パスワード
      <input type="password" autocomplete="password" v-model="password" />
    </label>
    <p class="error" v-if="!!pError">{{ pError }}</p>
    <p v-if="!!error" class="error">メールアドレスかパスワードが間違っている</p>
    <input type="submit" value="ログイン" />
  </form>
</template>

<script setup lang="ts">
import validator from "validator";
import { computed, watch } from "vue";
import { useRouter } from "vue-router";

import { not, useBackend, useError } from "../../lib";
import { logIn } from "../../lib/network";

const { push } = useRouter();

const {
  data: email,
  error: eError,
  start: eStart,
} = useError("", [not(validator.isEmail)], {
  defaultMessage: "メールアドレスを入力してください",
  immediately: false,
});
const {
  data: password,
  error: pError,
  start: pStart,
} = useError("", [validator.isEmpty], {
  defaultMessage: "パスワードを入力してください",
  immediately: false,
});

const valid = computed(() => !(eError.value || pError.value));

const tryLogin = () => {
  eStart();
  pStart();

  if (valid) {
    login();
  }
};

const { data, error, refresh: login } = useBackend(logIn, false, { email, password });
watch(data, (value) => !!value && push({ path: "/mypage" }));
</script>

<style scoped></style>
