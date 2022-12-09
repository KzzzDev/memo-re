<template>
  <form @submit.prevent="trySignUp">
    <label>
      メールアドレス
      <input type="text" autocomplete="username" v-model="email" />
    </label>
    <p class="error" v-if="eError">{{ eError }}</p>
    <label>
      パスワード
      <input type="password" autocomplete="new-password" v-model="password" />
    </label>
    <p class="error" v-if="pError">{{ pError }}</p>
    <label>
      ユーザー名
      <input type="text" v-model="name" />
    </label>
    <p class="error" v-if="nError">{{ nError }}</p>
    <p class="error" v-if="error">{{ error }}</p>
    <input type="submit" value="登録" />
  </form>
</template>

<script setup lang="ts">
import validator from "validator";
import { computed, watch } from "vue";
import { useRouter } from "vue-router";

import { not, useBackend, useError } from "../../lib";
import { registerUser } from "../../lib/network";

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
} = useError(
  "",
  [
    validator.isEmpty,
    (str) => !validator.isStrongPassword(str) && "８文字以上大小英数字と符号を組み合わせたパスワードにしてください",
  ],
  {
    defaultMessage: "パスワードを入力してください",
    immediately: false,
  }
);
const {
  data: name,
  error: nError,
  start: nStart,
} = useError("", [validator.isEmpty], { defaultMessage: "ユーザー名を入力してください", immediately: false });

const valid = computed(() => !(eError.value || pError.value || nError.value));

const trySignUp = () => {
  [eStart, pStart, nStart].map((fn) => fn());

  if (valid) {
    signUp();
  }
};

const { data, error, refresh: signUp } = useBackend(registerUser, false, { email, password, name });
watch(data, (value) => !!value && push({ path: "/" }));
</script>

<style scoped></style>
