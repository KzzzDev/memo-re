<template>
  <div class="wrap">
    <div class="image"><img src="@/assets/logo.png" alt="ロゴ" /></div>
    <h1>サインイン</h1>
    <div class="innerwrap">
      <p>メールアドレス</p>
      <input v-model="email" type="text" class="text" />
      <br />
      <p>パスワード</p>
      <input v-model="password" type="password" class="text" />
      <br />
      <div class="button">
        <button @click="SignIn()">サインイン</button>
      </div>
      <div class="signup">
        <router-link to="/SignUp">新規登録</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { API_SERVER } from "@/assets/config.js";
export default {
  name: "SignIn",
  components: {},
  data() {
    return {
      password: null,
      email: null,
      data: [],
    };
  },
  methods: {
    SignIn() {
      const requestBody = {
        password: this.password,
        email: this.email,
      };
      axios
        .post(API_SERVER + "/api/v1/auth/jwt/create/", requestBody)
        .then((response) => {
          this.data = response.data;
          const token = response.data.access;
          let user = null;
          console.log("ログイン成功");
          console.log(token);
          //ユーザー情報取得
          axios
            .get(API_SERVER + "/api/v1/auth/users/me/", {
              headers: { Authorization: "JWT " + token },
            })
            .then((response2) => {
              user = response2.data.id;
              this.$cookies.set("access", token, 60 * 50);
              //console.log(this.$cookies.get("access"));
              localStorage.setItem("id", user);
              console.log("成功");
              this.$router.push({ name: "myPage" });
            })
            .catch(() => {
              //エラー回避用
              console.log("ログイン失敗");
            });
        })
        .catch(() => {
          //エラー回避用
          console.log("ログイン失敗");
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
.signup {
  margin-top: 20px;
  font-size: 14px;
  text-align: center;
}
</style>
