<template>
  <div class="wrap">
    <div class="image"><img src="@/assets/logo.png" alt="ロゴ" /></div>
    <h1>サインアップ</h1>
    <div class="innerwrap">
      <p>ユーザー名</p>
      <p>{{ error.username }}</p>
      <input v-model="username" type="text" class="text" />
      <br />
      <p>メールアドレス</p>
      <p>{{ error.email }}</p>
      <input v-model="email" type="text" class="text" />
      <br />
      <p>パスワード</p>
      <input v-model="password" type="password" class="text" />
      <br />
      <p>確認用パスワード</p>
      <p>{{ error.password }}</p>
      <input v-model="checkpass" type="password" class="text" />
      <br />
      <div class="button">
        <button @click="SignUp()">新規登録</button>
      </div>
      <div class="signin">
        <router-link to="/SignIn">サインイン</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { API_SERVER } from "@/assets/config.js";
export default {
  name: "SignUp",
  components: {},
  data() {
    return {
      username: null,
      password: null,
      checkpass: null,
      email: null,
      signUp: [],
      error: [],
    };
  },
  methods: {
    SignUp() {
      const requestBody = {
        email: this.email,
        username: this.username,
        password: this.password,
      };
      axios
        .post(API_SERVER + "/api/v1/auth/users/", requestBody)
        .then((response) => {
          this.signUp = response.data;
          console.log("success");
          console.log(this.signUp);
          this.$router.push({ name: "signIn" });
        })
        .catch((e) => {
          this.error = e.response.data;
          console.log(e);
          console.log(this.error);
        });
    },
  },
};
</script>

<style scoped>
.wrap {
  width: 630px;
  height: 680px;
  border: solid 2px #000;
  margin: 40px auto 0;
  padding-top: 60px;
}
h1 {
  text-align: center;
}
.innerwrap {
  width: 420px;
  margin: 0 auto;
}
.text {
  width: 420px;
  height: 40px;
  border: solid 2px #000;
  margin-bottom: 20px;
}
.image {
  width: 100px;
  height: 100px;
  margin: 0 auto;
}
img {
  width: 100%;
}
.button {
  width: 160px;
  margin: 0 auto;
}
button {
  color: #fff;
  background: #6d8dff;
  width: 160px;
  height: 54px;
  text-align: center;
  border-radius: 5px;
}
.signin {
  margin-top: 20px;
  font-size: 14px;
  text-align: center;
}
</style>
