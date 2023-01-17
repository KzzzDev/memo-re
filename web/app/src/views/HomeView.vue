<template>
  <div class="html">
    <div class="wrapper">
      <div class="main-wrap">
          <div class="header-nav">
            <div class="flex">
              <p><router-link to="/SignUp">新規登録</router-link></p>
              <p><router-link to="/SignIn">サインイン</router-link></p>
            </div>
          </div>
        <div class="section1">
          <div class="section1-wrap">
            <h1 class="main-h1">消えない記憶を未来へ</h1>
            <img src="/media/images/logo.png" alt="logo" class="logo">
          </div>
        </div>
      </div>
      <div id="page_top"><a href="#"></a></div>
      <div class="section2">
        <h1 class="section2-h1">memo:Reとは？</h1>
        <p class="section2-text">memo:Reはあなたの記憶をAIによって画像生成し、お互いに生成した記憶を交換することで<br>
          人生の充実度を上げることを目的としたアプリです。<br>
          日常の何気ないできごとや、感動した経験、後世に残したい記憶などをみんなで共有しましょう！
        </p>
        <div class="section2-person">
          <div class="person-wrap">
            <p>旅行の記憶を共有したい</p>
            <img src="/media/images/woman.png" alt="">
          </div>
          <div class="arrow-img">
            <img src="/media/images/arrow-p.png" alt="">
            <img src="/media/images/arrow-b.png" alt="">
          </div>
          <div class="person-wrap">
            <p>学校での日々を共有したい！</p>
            <img src="/media/images/man.png" alt="">
          </div>
          <div class="arrow-img">
            <img src="/media/images/arrow-b2.png" alt="">
            <img src="/media/images/arrow-y.png" alt="">
          </div>
          <div class="person-wrap">
            <p>昔の自慢話を共有したい！</p>
            <img src="/media/images/papa.png" alt="">
          </div>
        </div>
      </div> 

      <div class="section3">
        <h1>memo:Reで出来ること</h1>
        <div class="content-wrap">
          <img src="/media/images/sc-1.png" alt="">
          <div class="content-text">
            <h1>記憶の保存</h1>
            <p>あなたの記憶を保存します！<br>
              ノートとして保存できるのでいつでも見返す<br>
              ことができます。<br>
              日々のできごとや、感動した経験などの残し<br>
              たい記憶などを自由に保存しましょう。
              </p>
          </div>
        </div>
        <div class="content-wrap">
          <div class="content-text2">
            <h1>記憶の共有</h1>
            <p>あなたの記憶を共有できます！<br>
              送りたい相手に記憶を共有、欲しい記憶に<br>
              共有申請を送ることができます！<br>
              たくさん記憶を共有して充実度を上げ<br>
              ていきましょう！
              </p>
          </div>
          <img src="/media/images/sc-2.png" alt="">
        </div>
        <div class="content-wrap">
          <img src="/media/images/sc-3.png" alt="">
          <div class="content-text">
            <h1>記憶の一覧表示</h1>
            <p>あなたの記憶を一覧にできます。<br>
              自分で保存した記憶と相手からもらった記憶<br>
              を一覧をして表示することができます！<br>
              記憶をたくさん作成して、自分の記憶を沢山<br>
              増やしていきましょう！
              </p>
          </div>
        </div>
      </div> 

      <div class="section4">
        <h1>memo:Reを使えば<br>
          人生がもっと充実！！</h1>
          <div class="content4-wrap">
            <div class="content-text2">
              <p>楽しい旅の記憶を</p>
            </div>
            <img src="/media/images/ai1.png" alt="">
          </div>
          <div class="content4-wrap">
            <img src="/media/images/ai2.png" alt="">
            <div class="content-text">
              <p>幻想的な夢の記憶を</p>
            </div>
          </div>
          <div class="content4-wrap">
            <div class="content-text2">
              <p>感動の体験を</p>
            </div>
            <img src="/media/images/ai3.png" alt="">
          </div>
          <div class="content4-wrap">
            <img src="/media/images/ai4.png" alt="">
            <div class="content-text">
              <p>夢で見た記憶だって作れる</p>
            </div>
          </div>
      </div>

      <div class="section5">
        <h1>さっそくmemo:Reを<br>
          使ってみましょう！</h1>
          <div class="section5-wrap">
            <img src="/media/images/logo.png" alt="logo">
            <div class="btn-wrap">
              <p class="new-btn"><router-link to="/SignUp">新規登録</router-link></p>
              <p class="login-btn"><router-link to="/SignIn">サインイン</router-link></p>
            </div>
          </div>
      </div>

      <footer><small>&copy;memo:Re</small></footer>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: "HomeView",
  components: {},
  methods: {},
  mounted: function(){}
};
</script>
<style scoped>
@import "https://use.fontawesome.com/releases/v5.6.4/css/all.css";
h1 {
  font-size: 64px;
  font-weight: bold;
  margin: 0;
  color: #313131;
}
p{
  margin: 0;
}
.wrapper {
  width: 100%;
  height: 100vh;
  position: relative;
  margin: 0;
}
.canvas-wrap{
  position: fixed;
  z-index: 1;
}
.main-wrap{
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  z-index: 10;
}
.header-nav{
  position: absolute;
  top:30px;
  right: 120px;
}
.header-nav div{
  text-decoration: none;
}
.header-nav div p{
  font-size: 18px;
  font-weight: bold;
  color: black;
  font-weight: 500;
  margin-left: 30px;
}
.header-nav div p :hover{
  color: #FF6DE8;
}
.section1{
  padding-top: 16%;
  color: black;
}
.section1-wrap{
  text-align: center;
}
.logo{
  width:298px;
  height:290px;
  display:inline-block;
}
.section2{
  margin-top: 180px;
  text-align: center;
  position: relative;
  z-index: 10;
  padding: 90px 0;
  background-color:rgba(252, 252, 252, 0.8);
}
.section2-text{
  font-size: 20px;
  text-align: left;
  display: inline-block;
  margin-top: 60px;
  line-height: 2.8rem;
  font-weight: 500;
}
.section2-person{
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 90px;
}
.person-wrap p{
  margin-bottom: 20px;
  font-size: 16px;
  font-weight: 500;
}
.person-wrap img{
  width: 115px;
  height: 176px;
}
.arrow-img{
  width: 160px;
}
.arrow-img img{
  margin-top: 10px;
}
.section3{
  margin-top: 120px;
  text-align: center;
  position: relative;
  z-index: 10;
  padding: 90px 0;
  background-color:rgba(252, 252, 252, 0.8);
}
.section3 h1{
  margin-bottom: 80px;
}
.content-wrap{
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  margin-bottom: 90px;
}
.content-wrap img{
  width: 440px;
  height: 248px;
}
.content-text{
  text-align: left;
  margin-left: 30px;
  line-height: 1.75;
}
.content-text h1 {
  font-size: 32px;
  margin-bottom: 0;
}
.content-text p {
  font-size: 20px;
}
.content-text2{
  text-align: left;
  line-height: 1.75;
  margin-right: 30px;
}
.content-text2 h1 {
  font-size: 32px;
  margin-bottom: 0;
}
.content-text2 p {
  font-size: 20px;
}
.section4{
  margin-top: 120px;
  text-align: center;
  position: relative;
  z-index: 10;
  padding: 90px 0;
  background-color:rgba(252, 252, 252, 0.8);
}
.section4 h1 {
  margin-bottom: 90px;
}
.content4-wrap{
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  margin-bottom: 90px;
}
.content4-wrap p{
  font-size: 24px;
}
.content4-wrap img{
  width: 485px;
  height: 328px;
}
.section5{
  margin-top: 120px;
  text-align: center;
  position: relative;
  z-index: 10;
  padding: 90px 0;
  background-color:rgba(252, 252, 252, 0.8);
}
.section5 h1 {
  margin-bottom: 90px;
}
.section5-wrap{
  display: flex;
  justify-content: center;
  align-items: center;
}
.section5-wrap img{
  width: 300px;
  height: 290px;
}
.btn-wrap a{
  font-size: 32px;
  text-decoration: none;
}
.new-btn{
  background-color: #FF6DE8;
  color: #f9f9f9;
  padding: 10px 20px;
  border-radius: 5px;
  display: block;
  margin-bottom: 20px;
}
.new-btn:hover{
  background-color: rgb(255, 0, 230);
  color: #f9f9f9;
}
.login-btn{
  background-color: #6D8DFF;
  color: #f9f9f9;
  padding: 10px 54px;
  border-radius: 5px;
}
.login-btn:hover{
  background-color: rgb(35, 83, 255);
  color: #f9f9f9;
}
footer{
  margin-top: 60px;
  height: 80px;
  background-color: rgb(38, 38, 38);
  color: #f9f9f9;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  z-index: 10;
}
#page_top{
  width: 80px;
  height: 80px;
  position: fixed;
  right: 30px;
  bottom: 50px;
  background: #3f98ef;
  opacity: 0.6;
  border-radius: 50%;
  z-index: 100;
}
#page_top a{
  position: relative;
  display: block;
  width: 80px;
  height: 80px;
  text-decoration: none;
}
#page_top a::before{
  font-family: 'Font Awesome 5 Free';
  font-weight: 900;
  content: '\f102';
  font-size: 25px;
  color: #fff;
  position: absolute;
  width: 25px;
  height: 25px;
  top: -5px;
  bottom: 0;
  right: 0;
  left: 0;
  margin: auto;
  text-align: center;
}
</style>
