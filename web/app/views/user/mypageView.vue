<template>
  <h1>
    <img src="/images/logo.png" alt="" width="96" />
    My Page
  </h1>

  <template v-if="editing">
    <input type="text" placeholder="E-mail" v-model="email" />
    <p class="error">{{ emailE.error.value }}</p>
    <input type="password" placeholder="Password" v-model="password" />
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
import { inject, ref } from "vue";

import { UserInfo, UserInfoKey } from "../../App.vue";
import { not, useBackend, useError } from "../../lib";
import { updateUserInfo } from "../../lib/network";

// ユーザーの情報は入手出来なかったら、ログインに転移されるはずなので、あると信じる
const userInfo = inject(UserInfoKey) as UserInfo;
const editing = ref(true);

const { data: email, ...emailE } = useError(userInfo.value.email, [not(validator.isEmail)], {
  defaultMessage: "メールアドレスを入力してください",
  immediately: false,
});

const { data: password, ...passE } = useError(
  "",
  [
    (str) => validator.isEmpty(str) && "パスワードを入力してください",
    (str) => !validator.isStrongPassword(str) && "８文字以上大小英数字と符号を組み合わせたパスワードにしてください",
  ],
  { immediately: false }
);

const { data: passC, ...passCE } = useError(
  "",
  [(str) => str != password.value && "入力したパスワードと一致しません"],
  {
    immediately: false,
  }
);

const tryUpdateInfo = () => {
  const fields = [emailE, passE, passCE];

  fields.map((err) => err.start());

  if (!fields.map((fld) => !!fld.error.value).reduce((prev, next) => prev || next)) {
    updateInfo()
      .then(() => {}) // NOTE: 成功したら
      .catch(() => {}); // NOTE: 失敗したら
  }
};

const { refresh: updateInfo } = useBackend(updateUserInfo, false, userInfo.value.id ?? "current", {
  email,
  password,
});
</script>

<style scoped></style>
