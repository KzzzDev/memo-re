<template>
  <div class="flex">
    <div class="fixedGlobal">
      <GlobalHeader />
    </div>
    <div class="wrap">
      <h1>記憶を画像にしよう</h1>
      <div class="innerWrap">
        <p class="title">題名</p>
        <p class="error" v-if="titleError">※題名を入力してください</p>
        <input v-model="title" type="text" class="text" maxlength="40" />
        <br />
        <p class="title">キーワード <span class="space">※複数入力の場合は間に,または、をつけてください。</span></p>
        <p class="error" v-if="keyError">※キーワードが入力されていません</p>
        <input
          v-model="keyword"
          type="text"
          class="text"
          maxlength="100"
          placeholder="aaa,bbb、ccc,ddd"
        />
        <br />
        <p class="title">説明</p>
        <p class="error" v-if="textError">※説明が入力されていません</p>
        <textarea
          v-model="text_uri"
          maxlength="200"
          name=""
          cols="30"
          rows="10"
          class="textarea"
        ></textarea>
        <br />
        <!-- <button @click="ImageRequest()">画像を作成</button> -->
        <button @click="ImageRequest">画像を作成</button>
      </div>
      <template v-if="loadFlag">
        <div class="loadingWrap">
          <div class="loadingContent">
            <p class="warningTitle">画像生成中</p>
            <p class="warning">生成には20秒～30秒ほど時間がかかります</p>
            <p class="warning">利用者が多いとそれ以上かかる場合もあります</p>
            <div>
              <vue-element-loading
                :active="loadFlag.length != 0"
                spinner="bar-fade-scale"
              />
            </div>
          </div>
        </div>
      </template>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { AI_SERVER } from "@/assets/config.js";
import VueElementLoading from "vue-element-loading";
import GlobalHeader from "@/components/GlobalHeader.vue";

export default {
  data() {
    return {
      loadFlag: false,
      user: localStorage.getItem("id"),
      title: "",
      keyword: "",
      text_uri: "",
      image_uri: "test.png",
      titleError: false,
      keyError: false,
      textError: false,
      keywordAry: [],
    };
  },
  name: "CreateImage",
  components: {
    VueElementLoading,
    GlobalHeader,
  },
  methods: {
    ImageRequest: async function () {
      //入力確認
      this.titleError = false;
      this.keyError = false;
      this.textError = false;
      if (this.title == "" || this.keyword == "" || this.text_uri == "") {
        if (this.title == "") {
          this.titleError = true;
        }
        if (this.keyword == "") {
          this.keyError = true;
        }
        if (this.text_uri == "") {
          this.textError = true;
        }
        return;
      }
      //API処理
      //これは残す
      this.loadFlag = true;
      // console.log(this.loadFlag);
      this.keywordAry = this.keyword.split("、");
      this.keyword = this.keywordAry.join(",");
      const requestBody = {
        user_id: this.user,
        keyword: this.keyword,
      };
      await axios
        .post(AI_SERVER + "/ai/debug", requestBody)
        .then((response) => {
          //ローカル時コメントアウト
          this.image_uri = response.data.img_file;

          // ローカルストレージ
          localStorage.setItem("title", this.title);
          localStorage.setItem("keyword", this.keyword);
          localStorage.setItem("text_uri", this.text_uri);
          localStorage.setItem("image_uri", this.image_uri);
          //画面遷移
          this.loadFlag = false;
          this.$router.push("/PreviewImage");
        })
        .catch((e) => {
          console.log(e);
          console.log("失敗");
        });
      //test
      //ローカルストレージ
      // localStorage.setItem("title", this.title);
      // localStorage.setItem("keyword", this.keyword);
      // localStorage.setItem("text_uri", this.text_uri);
      // localStorage.setItem("image_uri", this.image_uri);
      // console.log(this.keyword);
      // //画面遷移
      // this.$router.push("/PreviewImage");
      //test end

      this.loadFlag = false;
    },
  },
  created() {
    if (this.$cookies.get("access") === null) {
      this.$router.push("/SignIn");
    }
  },
};
</script>

<style scoped>
h1 {
  font-size: 24px;
  text-align: center;
  margin: 40px;
  color: #666;
  font-weight: bolder;
}
.wrap {
  /* width: 510px; */
  width: 810px;
  height: 650px;
  margin: 100px auto 0;
  /* border: solid 2px #ccc6c6; */
  border-radius: 26px;
  position: relative;
  background: #fff;
  filter: drop-shadow(0px 0px 20px #aaa);
}

.innerWrap {
  /* width: 420px; */
  width: 720px;
  margin: 0 auto;
}

.title {
  /* margin-bottom: 10px; */
  color: #000;
}

.text {
  /* width: 420px; */
  width: 720px;
  height: 40px;
  /* border: solid 2px #ccc6c6; */
  margin-top: 6px;
  margin-bottom: 20px;
  padding: 6px 0 6px 10px;
  border-radius: 10px;
  box-shadow: 0px 0px 8px 3px #ccc inset;
}
.text:focus {
  outline: none;
}

.textarea {
  resize: none;
  /* width: 420px; */
  width: 720px;
  height: 180px;
  /* border: solid 2px #ccc6c6; */
  border-radius: 14px;
  margin-top: 6px;
  margin-bottom: 20px;
  padding: 14px 10px 6px 10px;
  box-shadow: 0px 0px 8px 3px #ccc inset;
}
textarea:focus {
  outline: none;
}

button {
  float: right;
  color: #fff;
  background: #6d8dff;
  width: 160px;
  height: 54px;
  text-align: center;
  border-radius: 5px;
  box-shadow: 4px 4px 8px 3px #bbb;
}
button:hover {
  background: #7b98ff;
}

.loadingWrap {
  /* width: 510px; */
  width: 810px;
  height: 650px;
  margin: 0 auto;
  position: absolute;
  top: 0;
  left: 0;
  background: rgba(255, 255, 255, 0.6);
  border-radius: 26px;
}
.loadingContent {
  width: 300px;
  height: 200px;
  background-color: #fff;
  margin: 205px auto 0;
  border: solid 2px #ccc;
  border-radius: 20px;
}
.loadingContent p {
  font-size: 16px;
  font-weight: bold;
  text-align: center;
}
.loadingContent .warningTitle {
  margin-top: 40px;
}
.loadingContent .warning {
  font-size: 12px;
}

.loadingContent div {
  margin-top: 30px;
}
.error {
  font-size: 12px;
  color: #f00;
  /* margin-left: 10px; */
}

.space {
  font-size: 12px;
}
</style>
