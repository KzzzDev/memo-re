<template>
  <div class="w-full flex justify-center" style="padding-right: 12%">
    <div class="modal border shadow w-1/3 flex flex-col p-10">

      <img  src="../../public/images/logo.png" class="w-24 h-24 mx-auto" alt="">
      <p class="mt-4 mb-2 mx-auto text-xl text-gray-500">サインアップ</p>
      <label for="signup-mail-address" class="mt-4 mb-2 text-xl text-gray-500">メール</label>
      <input id="signup-mail-address" class="bg-gray-50 p-2 rounded-xl shadow-inner" type="email" v-model="Forms.Mail">
      <label for="signup-password" class="mt-4 mb-2 text-xl text-gray-500">パス</label>
      <input id="signup-password" class="bg-gray-50 p-2 rounded-xl shadow-inner" type="password" v-model="Forms.PassWord">
      <label for="signup-check-password" class="mt-4 mb-2 text-xl text-gray-500">パス</label>
      <input id="signup-check-password" class="bg-gray-50 p-2 rounded-xl shadow-inner" type="password" v-model="Forms.CheckPassWord">
      <label for="signup-user-name" class="mt-4 mb-2 text-xl text-gray-500">表示名</label>
      <input id="signup-user-name" class="bg-gray-50 p-2 rounded-xl shadow-inner" type="text" v-model="Forms.UserName">
      <br>
      <button class="w-1/2 mx-auto mt-5 p-3 bg-blue-200" type="submit">作成</button>

    </div>
  </div>
</template>

<script lang="ts">
import axios from "axios";
import {defineComponent} from "vue"

export default defineComponent({
  name: "sign up view",
  data() {
    return {
      Forms: {
        Mail: "",
        PassWord: "",
        CheckPassWord:"",
        UserName: ""
      }
    }
  },
  methods: {
    submit: async function () {
      console.log(this.Forms)
      const PostParams = new URLSearchParams()
//      PostParams.append("userid", 1)
      //    PostParams.append("username", this.Forms.UserName)
      PostParams.append("password", this.Forms.PassWord)
      PostParams.append("email", this.Forms.Mail)
      const res = await axios.post("http://localhost:8000//api/v1/auth/jwt/create")
      console.log(res)
    }
  }
})
</script>

<!--<script setup lang="ts">-->
<!--import validator from "validator";-->
<!--import { computed, watch } from "vue";-->
<!--import { useRouter } from "vue-router";-->

<!--import { not, useBackend, useError } from "../../lib";-->
<!--import { registerUser } from "../../lib/network";-->

<!--const { push } = useRouter();-->

<!--const {-->
<!--  data: email,-->
<!--  error: eError,-->
<!--  start: eStart,-->
<!--} = useError("", [not(validator.isEmail)], {-->
<!--  defaultMessage: "メールアドレスを入力してください",-->
<!--  immediately: false,-->
<!--});-->
<!--const {-->
<!--  data: password,-->
<!--  error: pError,-->
<!--  start: pStart,-->
<!--} = useError(-->
<!--  "",-->
<!--  [-->
<!--    validator.isEmpty,-->
<!--    (str) => !validator.isStrongPassword(str) && "８文字以上大小英数字と符号を組み合わせたパスワードにしてください",-->
<!--  ],-->
<!--  {-->
<!--    defaultMessage: "パスワードを入力してください",-->
<!--    immediately: false,-->
<!--  }-->
<!--);-->
<!--const {-->
<!--  data: name,-->
<!--  error: nError,-->
<!--  start: nStart,-->
<!--} = useError("", [validator.isEmpty], { defaultMessage: "ユーザー名を入力してください", immediately: false });-->

<!--const valid = computed(() => !(eError.value || pError.value || nError.value));-->

<!--const trySignUp = () => {-->
<!--  [eStart, pStart, nStart].map((fn) => fn());-->

<!--  if (valid) {-->
<!--    signUp();-->
<!--  }-->
<!--};-->

<!--const { data, error, refresh: signUp } = useBackend(registerUser, false, { email, password, name });-->
<!--watch(data, (value) => !!value && push({ path: "/" }));-->
<!--</script>-->

<style scoped>


</style>
