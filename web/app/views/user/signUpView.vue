<template>
  <div class="w-full flex　flex-col items-center" style="padding-right: 12%">
    <div class="modal border shadow w-1/2 flex flex-col p-10">
      <img src="../../public/images/logo.png" class="w-24 h-24 mx-auto" alt="">
      <p class="mt-4 mb-2 mx-auto text-xl text-gray-500">サインアップ</p>
      <label for="signup-mail-address" class="mt-4 mb-2 text-xl text-gray-500">メール</label>
      <input id="signup-mail-address" class="bg-gray-50 p-2 rounded-xl shadow-inner" type="email" v-model="Forms.Mail">
      <label for="signup-password" class="mt-4 mb-2 text-xl text-gray-500">パス</label>
      <input id="signup-password" class="bg-gray-50 p-2 rounded-xl shadow-inner" type="password"
             v-model="Forms.PassWord">
      <label for="signup-check-password" class="mt-4 mb-2 text-xl text-gray-500">パス</label>
      <input id="signup-check-password" class="bg-gray-50 p-2 rounded-xl shadow-inner" type="password"
             v-model="Forms.CheckPassWord">
      <label for="signup-user-name" class="mt-4 mb-2 text-xl text-gray-500">表示名</label>
      <input id="signup-user-name" class="bg-gray-50 p-2 rounded-xl shadow-inner" type="text" v-model="Forms.UserName">
      <br>
      <button class="w-1/2 mx-auto mt-5 p-3 bg-blue-200" type="submit" @click="submit">作成</button>

    </div>
    <div class="w-1/2 flex justify-end mt-2">
      <router-link class="mr-3" to="/signIn">サインイン</router-link>
    </div>
  </div>
</template>

<script lang="ts">
import {defineComponent} from "vue"
import {callAPI} from "../../lib/AxiosAccess";
import {setToken} from "../../lib/auth";

export default defineComponent({
  name: "sign up view",
  data() {
    return {
      Forms: {
        Mail: "hogehoge@example.com",
        PassWord: "aaaa123456",
        CheckPassWord: "",
        UserName: "hoge2"
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
      if (!this.Forms.Mail || !this.Forms.PassWord || !this.Forms.CheckPassWord || !this.Forms.UserName) {
        this.$store.dispatch("updateToast", "必要な情報が足りません。")
        return
      }
      if (this.Forms.PassWord != this.Forms.CheckPassWord){
        this.$store.dispatch("updateToast","確認用パスワードが一致しません。")
      }
      try {

        const body = {
          username: this.Forms.UserName,
          email: this.Forms.Mail,
          password: this.Forms.PassWord,
        }

        await callAPI("auth/users/", "POST", false, body)
        const jwtCreateBody = {
          email: this.Forms.Mail,
          password: this.Forms.PassWord
        }
        const res = await callAPI("auth/jwt/create/", "POST", false, jwtCreateBody)
        setToken(res.data.access)
        const getMyDataResponse = await callAPI("auth/users/me/", "GET", true)
        await this.$store.dispatch("setUserId", getMyDataResponse.data.id)

        await this.$router.push("/mypage")
      } catch (e) {
        this.$store.dispatch("updateToast", "サインアップに失敗しました。")
      }
    }
  }
})
</script>


<style scoped>


</style>
