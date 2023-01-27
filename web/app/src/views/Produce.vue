<template>
  <div class="flex">
    <div class="fixedGlobal">
      <GlobalHeader />
    </div>
    <div class="preOWrap">
      <h2>開発メンバー</h2>
      <div class="flex wrap">
        <div class="box0">
          <div>
            <h3>PM</h3>
            <p>キム・ウンス</p>
          </div>
        </div>
        <div class="innerWrap">
          <div class="flex nameWrap">
            <div class="box box1">
              <div class="innerBox">
                <h3>WEBインフラ</h3>
                <p>原一将</p>
                <p>吉田充利</p>
                <p>キム・ウンス</p>
              </div>
              <div class="innerBox">
                <h3>WEBバックエンド</h3>
                <p>原一将</p>
                <p>吉田充利</p>
              </div>
            </div>

            <div class="box box2">
              <div class="innerBox">
                <h3>AIインフラ</h3>
                <p>宮島大輝</p>
              </div>
              <div class="innerBox">
                <h3>AIバックエンド</h3>
                <p>宮島大輝</p>
              </div>
              <div class="innerBox">
                <h3>AI画像生成</h3>
                <p>キム・ウンス</p>
              </div>
            </div>      
            
            <div class="box box3">
              <div class="innerBox">
                <h3>フロント</h3>
                <p>宮島大輝</p>
              </div>
              <div class="innerBox">
                <h3>デザイン</h3>
                <p>本荘俊介</p>
                <p>田中あみ</p>
                <p>宇野そら</p>
              </div>
            </div>
            
            <div class="box box4">
              <div class="innerBox">
                <h3>動画作成</h3>
                <p>キム・ウンス</p>
              </div>
              <div class="innerBox">
                <h3>技術調査</h3>
                <p>チョウ・サワ</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import GlobalHeader from "@/components/GlobalHeader.vue";
export default {
  name: "ImageView",
  components: {
    GlobalHeader,
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
.preOWrap {
  width: calc(100vw - 170px);
  padding: 100px 0 0 100px;
}

.wrap, .nameWrap{
  flex-wrap: wrap;
}
.innerWrap {
  max-width: 1200px;

}
h2 {
  font-size: 30px;
  font-weight: bold;
}
.box0 {
  margin: 20px 200px 40px 0;
  padding-left: 40px;
}

.box0 p {
  font-size: 24px;
  font-weight: bolder;
}
.box{
  width:400px;
  height: 400px;
  margin: 0 80px 80px 0;
  background: #ccc;
  border-radius: 40px;
  filter: drop-shadow(0px 0px 20px #aaa);
  padding: 40px
}
.box p {
  margin-bottom: 8px;
}
.innerBox {
  margin-bottom: 20px;
}
.box1{
  background: #A7BAFE;
}
.box2{
  background: #FCFF6D;
}

.box3{
  background: #fda7f1;
}

h3 {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 14px;
}
</style>
