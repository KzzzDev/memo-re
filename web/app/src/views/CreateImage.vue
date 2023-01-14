<template>
  <div class="flex">
    <div class="fixedGlobal">
      <GlobalHeader />
    </div>
    <div class="wrap">
      <h1>記憶を画像にしよう</h1>
      <div class="innerWrap">
        <p>題名</p>
        <p v-if="error">入力されていません</p>
        <input v-model="title" type="text" class="text" />
        <br />
        <p>キーワード</p>
        <input v-model="keyword" type="text" class="text" />
        <br />
        <p>説明</p>
        <textarea
          v-model="text_uri"
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
            <p>画像生成中</p>
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
      error: false,
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
      this.error = false;
      if (this.title == "" || this.keyword == "" || this.text_uri == "") {
        this.error = true;
        return;
      }
      //API処理
      this.loadFlag = true;
      console.log(this.loadFlag);
      const requestBody = {
        user_id: this.user,
        keyword: this.keyword,
      };
      await axios
        .post(AI_SERVER + "/ai/debug", requestBody)
        .then((/*response*/) => {
          // this.image_uri = response.data.img_file;

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
      // ローカルストレージ
      // localStorage.setItem('title',this.title);
      // localStorage.setItem('keyword',this.keyword);
      // localStorage.setItem('text_uri',this.text_uri);
      // localStorage.setItem('image_uri',this.image_uri);
      // console.log(this.keyword);
      // //画面遷移
      // this.$router.push('/PreviewImage');
      // //test end

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
  font-size: 22px;
  text-align: center;
  margin: 40px;
}
.wrap {
  width: 510px;
  height: 610px;
  margin: 100px auto 0;
  border: solid 2px #ccc6c6;
  position: relative;
  background: #fff;
}

.innerWrap {
  width: 420px;
  margin: 0 auto;
}

.innerWrap p {
  margin-bottom: 10px;
}

.text {
  width: 420px;
  height: 40px;
  /* border: solid 2px #ccc6c6; */
  margin-bottom: 20px;
  padding: 6px 0 6px 4px;
  border-radius: 10px;
  box-shadow:0px 0px 8px 3px #ccc inset;
}

.textarea {
  resize: none;
  width: 420px;
  height: 180px;
  /* border: solid 2px #ccc6c6; */
  border-radius: 14px;
  margin-bottom: 20px;
  padding: 6px 0 6px 4px;
  box-shadow:0px 0px 8px 3px #ccc inset;
}

button {
  float: right;
  color: #fff;
  background: #6d8dff;
  width: 160px;
  height: 54px;
  text-align: center;
  border-radius: 5px;
}

.loadingWrap {
  width: 510px;
  height: 610px;
  margin: 0 auto;
  border: solid 2px #f00;
  position: absolute;
  top: 0;
  left: 0;
  background: rgba(255, 255, 255, 0.6);
}
.loadingContent {
  width: 300px;
  height: 200px;
  background-color: #fff;
  margin: 205px auto 0;
  border: solid 2px #000;
}
.loadingContent p {
  margin-top: 20px;
  font-size: 16px;
  font-weight: bold;
  text-align: center;
}

.loadingContent div {
  margin-top: 30px;
}
</style>
