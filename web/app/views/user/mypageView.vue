<template>
  <h1>
    <img src="/images/logo.png" alt="" width="96" />
    My Page
  </h1>

  <template v-if="editing">
    <input type="text" placeholder="E-mail" v-model="email" />
    <p class="error">{{ emailE.error.value }}</p>
    <input type="password" placeholder="Password" v-model="pass" />
    <p class="error">{{ passE.error.value }}</p>
    <input type="password" placeholder="確認用Password" v-model="passC" />
    <p class="error">{{ passCE.error.value }}</p>
    <button type="button" @click="tryUpdateInfo">登録</button>
  </template>

  <template v-else>
    <input type="text" placeholder="E-mail" readonly :value="email" />
    <button type="button" @click="editing = true">編集</button>
  </template>
</template>

<script setup lang="ts">
import validator from "validator";
import { ref } from "vue";

import { not, useError } from "../../lib";

const editing = ref(false);

const { data: email, ...emailE } = useError("alicewhite@example.com", [not(validator.isEmail)], {
  defaultMessage: "メールアドレスを入力してください",
  immediately: false,
});

const { data: pass, ...passE } = useError(
  "",
  [
    (str) => validator.isEmpty(str) && "パスワードを入力してください",
    (str) => !validator.isStrongPassword(str) && "８文字以上大小英数字と符号を組み合わせたパスワードにしてください",
  ],
  { immediately: false }
);

const { data: passC, ...passCE } = useError("", [(str) => str != pass.value && "入力したパスワードと一致しません"], {
  immediately: false,
});

const tryUpdateInfo = () => {};
</script>

<style scoped></style>
