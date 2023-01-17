<template>
  <div class="overWrap">
    <div class="wrap">
      <div class="image"><img src="@/assets/logo.png" alt="ロゴ" /></div>
      <h1>サインイン</h1>
      <div class="innerwrap">
        <p>メールアドレス<span v-if="errorMail" class="errorSpan">※メールアドレスが入力されていません</span></p>
        <input v-model="email" type="text" class="text" />
        <br />
        <p>パスワード　　<span v-if="errorPass"  class="errorSpan">※パスワードが入力されていません</span></p>
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
      password: "",
      email: "",
      data: [],
      errorMail: false,
      errorPass: false,
    };
  },
  methods: {
    SignIn() {
      this.error = false;
      this.errorMail = false;
      this.errorPass = false;
      if (this.password == "" || this.email == "") {
        if (this.email == "") {
          this.errorMail = true;
        }
        if (this.password == "") {
          this.errorPass = true;
        }
        console.log("だめです！")
        return;
      }
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
  width: 510px;
  height: 560px;
  margin: 0 auto;
  padding-top: 60px;
  border-radius: 26px;
  background: #fff;
  filter: drop-shadow(0px 0px 20px #aaa);
}
h1 {
  font-size: 24px;
  font-weight: bolder;
  text-align: center;
  margin-bottom: 20px;
  color: #666;
}
.innerwrap {
  width: 420px;
  margin: 0 auto;
}
.text {
  width: 420px;
  height: 40px;
  /* border: solid 2px #ccc6c6; */
  margin: 4px 0 20px;
  padding: 6px 0 6px 10px;
  border-radius: 10px;
  box-shadow:0px 0px 8px 3px #ccc inset;
}
.text:focus {
  outline: none;
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
  margin-top: 20px;
  box-shadow:4px 4px 8px 3px #bbb;
}
button:hover {
  background: #7b98ff;
}
.signup {
  margin-top: 20px;
  font-size: 14px;
  text-align: center;
}
.errorSpan {
  font-size: 12px;
  color: #f00;
  margin-left: 10px;
}
</style>
