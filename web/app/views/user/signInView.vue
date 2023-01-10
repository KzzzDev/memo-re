<template>
  <div class="w-full flex　flex-col items-center" style="padding-right: 12%">
    <div class="modal border shadow w-1/3 flex flex-col p-10">
      <img src="../../public/images/logo.png" class="w-24 h-24 mx-auto" alt="">
      <p class="mt-4 mb-2 mx-auto text-xl text-gray-500">サインアップ</p>
      <label for="signup-mail-address" class="mt-4 mb-2 text-xl text-gray-500">メール</label>
      <input id="signup-mail-address" class="bg-gray-50 p-2 rounded-xl shadow-inner" type="email" v-model="Forms.Mail">
      <label for="signup-password" class="mt-4 mb-2 text-xl text-gray-500">パス</label>
      <input id="signup-password" class="bg-gray-50 p-2 rounded-xl shadow-inner" type="password"
             v-model="Forms.PassWord">
      <label for="signup-check-password" class="mt-4 mb-2 text-xl text-gray-500">パス（確認用）</label>
      <input id="signup-check-password" class="bg-gray-50 p-2 rounded-xl shadow-inner" type="password"
             v-model="Forms.CheckPassWord">

      <button class="w-1/2 mx-auto mt-5 p-3 bg-blue-200" type="submit" @click="submit">作成</button>

    </div>
    <div class="w-1/3 flex justify-end">
      <router-link class="mr-3" to="/login">サインイン</router-link>
    </div>
  </div>
</template>

<script lang="ts">
import axios from "axios";
import {defineComponent} from "vue"
import {callAPI} from "../../lib/AxiosAccess";
import {setToken} from "../../lib/auth";

export default defineComponent({
  name: "sign up view",
  data() {
    return {
      Forms: {
        Mail: "hogehoge@example.com",
        PassWord: "aaaa12345",
        CheckPassWord: "",
      }
    }
  },
  beforeMount() {
    // if (this.$store.getters.isLogin){
    //   this.$router.push("/mypage")
    // }
  },
  methods: {
    submit: async function () {
      const jwtCreateBody = {
        email: this.Forms.Mail,
        password: this.Forms.PassWord
      }
      const res = await callAPI("auth/jwt/create/","POST", false,jwtCreateBody)
      setToken(res.data.access)

      const getMyDataResponse = await callAPI("auth/users/me/","GET", true)
      await this.$store.dispatch("setUserId",getMyDataResponse.data.id)

    }
  }
})
</script>


<style scoped>


</style>
