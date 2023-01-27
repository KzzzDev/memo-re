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
        <p class="title">キーワード<small id="modalOpen" class="modalOpen" @click="OpneModal()">ヒント</small><span class="space">※複数入力の場合は間に,または、をつけてください。</span></p>
        <p class="error" v-if="keyError">※キーワードが入力されていません</p>
        <input
          v-model="keyword"
          type="text"
          class="text"
          maxlength="255"
          placeholder="aaa,bbb、ccc,ddd"
        />
        <br />
        <p class="title">説明</p>
        <p class="error" v-if="textError">※説明が入力されていません</p>
        <textarea
          v-model="text_uri"
          maxlength="255"
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
    <div class="modalWrap">
      <div id="easyModal" class="modal">
        <div class="modal-content">
          <div class="modal-header">
            <h1>キーワード（プロンプト）入力のコツ</h1>
            <span class="modalClose">×</span>
          </div>
          <div class="modal-body">
            <div class="modal-body-block">
              <h2>&#040;&#041;を使ってキーワードの要素を強調しよう！</h2>
              <p><code class="code">&#040;柴犬と散歩中の若い男の人&#041;、住宅街、全身、俯瞰的</code></p>
              <p>上記のように強調したいキーワードを&#040;&#041;で囲むことによって、そのキーワードが色濃く反映された画像が生成されます。特に重要視したいキーワードに使いましょう。</p>
              <p>※&#040;&#041;を2重3重にしていくと、さらに強調されます。</p>
            </div>
            <hr>
            <div class="modal-body-block">
              <h2>&#091;&#093;を使ってキーワードの要素を控えめにしよう！</h2>
              <p><code class="code">&#040;柴犬と散歩中の若い男の人&#041;、住宅街、全身、&#091;俯瞰的&#093;</code></p>
              <p>上記のように強調したいキーワードを&#091;&#093;で囲むことによって、そのキーワードが弱められた画像が生成されます。</p>
              <p>※&#091;&#093;を2重3重にしていくと、さらに弱められます。</p>
            </div>
            <hr>
            <div class="modal-body-block">
              <h2>キーワードの順番を考えよう！</h2>
              <p>最初に宣言したキーワードほど、要素が強く反映されます。反対に後ろに宣言したキーワードほど、要素が弱く反映されます。</p>
            </div>
            <hr>
            <div class="modal-body-block">
              <h2>文章でキーワードを入力してみよう！</h2>
              <p>短い単語を複数個入力するより、文章で入力する方が、イメージ通りの画像が出力される場合があります。</p>
            </div>
            <hr>
            <div class="modal-body-block">
              <h2>特定のキーワードを入れてみよう！</h2>
              <p>特定のキーワードを入力することで、画像が美しくなったり、特徴のある画像を生成することができます。このようなキーワードはたくさん存在します。</p>
            </div>
            <hr>
            <div class="modal-body-block">
              <h3>詳しくはStable Diffusionの画像出力方法のコツについて検索してみてください。是非、様々な画像を生成してみてね！！</h3>
            </div>
          </div>
        </div>
      </div>
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

    // ----------モーダル----------
    OpneModal() {
      const buttonOpen = document.getElementById('modalOpen');
      const modal = document.getElementById('easyModal');
      const buttonClose = document.getElementsByClassName('modalClose')[0];

      // ボタンがクリックされた時
      buttonOpen.addEventListener('click', modalOpen);
      function modalOpen() {
        modal.style.display = 'block';
      }

      // バツ印がクリックされた時
      buttonClose.addEventListener('click', modalClose);
      function modalClose() {
        modal.style.display = 'none';
      }

      // モーダルコンテンツ以外がクリックされた時
      addEventListener('click', outsideClose);
      function outsideClose(e) {
        if (e.target == modal) {
          modal.style.display = 'none';
        }
      }
    },
    // ----------モーダル----------
  },
  created() {
    if (this.$cookies.get("access") === null) {
      const refresh = this.$cookies.get("refresh");
      if (refresh != null) {
        console.log("リフレッシュ");
        const requestBody = {
          refresh: refresh,
        };
        axios
          .post(API_SERVER + "/api/v1/auth/jwt/refresh/", requestBody)
          .then((response) => {
            let token = response.data.access;
            this.$cookies.set("access", token, 60 * 30);
            location.reload();
          })
          .catch(() => {
            //エラー回避用
            this.$router.push("/SignIn");
          });
      }else{
        this.$router.push("/SignIn");
      }
      return;
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




/* ----------モーダル---------- */
hr {
  height:0;
  border:0;
  border-top:1px solid #ccc;
  border-bottom:1px solid #fff;
}
.modalWrap {
  position: absolute;
  width: calc(100% - 170px);
  top:0;
  left: 170px;
}
.modalOpen {
  color: #00e;
  text-decoration: underline;
  cursor: pointer;

}

.modal {
  display: none;
  position:fixed;
  z-index: 1;
  height: 100%;
  width: calc(100% - 170px);
  border-radius: 26px;
  overflow: auto;
  background-color: rgba(255,255,255,0.5);
   /*IE(Internet Explorer)・Microsoft Edgeへの対応*/
  -ms-overflow-style: none;
  /*Firefoxへの対応*/
  scrollbar-width: none;
}

 /*Google Chrome、Safariへの対応*/
.modal::-webkit-scrollbar{
  display: none;
}

.modal-content {
  background-color: #fff;
  width: 1000px;
  margin: 100px auto 100px;
  border-radius: 26px;
  box-shadow: 0 5px 8px 0 rgba(0,0,0,0.5),0 7px 20px 0 rgba(0,0,0,0.17);
  animation-name: modalopen;
  animation-duration: 1s;
}

@keyframes modalopen {
  from {opacity: 0}
  to {opacity: 1}
}

.modal-header h1 {
  margin: 1rem 0;
  font-size: 32px;
  color: #fff;
}

.modal-header {
  background: #6d8dff;
  border-radius: 26px 26px 0 0;
  padding: 3px 15px;
  display: flex;
  justify-content: space-between;
}

.modalClose {
  font-size: 2rem;
  margin: auto 0;
  color: #fff;
}

.modalClose:hover {
  cursor: pointer;
  color: #ff78f4;
}

.modal-body {
  padding: 0 20px 20px 20px;
  border-radius: 26px;
  color: #000;
  line-height: 2;
}

.modal-body-block {
  margin: 20px auto;
}

.modal-body h2 {
  font-size: 24px;
  font: bold;
}

.modal-body h3 {
  font-size: 20px;
  font: bold;
}

.code {
  padding: 0.2em 0.3em;
  border-radius: 5px;
  background: #f1f2f3;
  color: #404040;
  font-size: 0.9em;
  font-family: "Menlo", "Consolas", "monaco", "monospace", "ＭＳ ゴシック", sans-serif;
  font-size: 1em;
}
/* ----------モーダル---------- */
</style>
