<template>
  <div class="fixed">
    <div class="gl-wrap">
      <div class="gl-global">
        <router-link to="/myPage" class="image"
          ><img src="@/assets/logo.png" alt="ロゴ"
        /></router-link>
        <!-- <div class="image"><img src="@/assets/logo.png" alt="ロゴ" /></div> -->
        <ul>
          <li><router-link to="/MyPage">マイページ</router-link></li>
          <li><router-link to="/CreateImage">ノート作成</router-link></li>
          <li><router-link to="/Timeline">タイムライン</router-link></li><br>
          <li @click="GlobalSide(0)" class="pointer">フレンド</li>
          <li @click="GlobalSide(1)" class="pointer">検索</li>
          <li @click="GlobalSide(2)" class="pointer">通知</li>
        </ul>
        <p class="produceButton pointer"><router-link to="/produce" >開発者紹介</router-link></p>
        <p class="logout pointer" @click="Logout()">ログアウト</p>
      </div>
      <!-- フレンド -->
      <div class="side" v-if="sideFriend">
        <div class="flex sideTitle">
          <h3>フレンドリスト</h3>
          <p class="closeSide pointer" @click="GlobalSide(0)">×</p>
        </div>
        <hr />
        <div v-for="data in glData" v-bind:key="data">
          <div
            class="flex gl-friendWrap"
            @click="ToFriend(data.id, data.icon_uri, data.username)"
          >
            <div class="gl-friendImg">
              <img :src="data.icon_uri" alt="フレンドアイコン" />
            </div>
            <p class="overflow">{{ data.username }}</p>
          </div>
        </div>
      </div>
      <div class="side gl-search" v-if="sideSearch">
        <div class="flex sideTitle">
          <h3>ユーザー検索</h3>
          <p class="closeSide pointer" @click="GlobalSide(1)">×</p>
        </div>
        <hr />
        <div class="flex wrap">
          <input v-model="searchText" type="text" class="text" @keypress.enter="Search()">
          <button @click="Search()">検索</button>
        </div>
        <hr />
        <p v-if="arrayFlag" style="text-align:center;margin-top:6px;">見つかりませんでした</p>
        <div v-for="data in searchData" v-bind:key="data">
          <div
            class="flex gl-friendWrap"
            @click="ToFriend(data.id, data.icon_uri, data.username)"
          >
            <div class="gl-friendImg">
              <img :src="data.icon_uri" alt="フレンドアイコン" />
            </div>
            <p class="overflow">{{ data.username }}</p>
          </div>
        </div>
      </div>
      <div class="side" v-if="sideNotice">
        <div class="flex sideTitle">
          <h3>通知BOX</h3>
          <p class="closeSide pointer" @click="GlobalSide(2)">×</p>
        </div>
        <hr />
        <div class="flex gl-noticeButton">
          <button @click="NoticeButton(0)">友達申請</button>
          <button @click="NoticeButton(1)">共有申請</button>
        </div>
        <!-- 友達申請 -->
        <template v-if="reqFlag == true">
          <div v-for="data in searchReqData" v-bind:key="data">
            <div
              class="flex gl-noticeWrap"
              @click="FriendModal(data.username,data.icon_uri,data.user_from)"
            >
              <div class="gl-friendImg">
                <img :src="data.icon_uri" alt="フレンドアイコン" />
              </div>
              <div>
                <p>{{ data.username }}</p>
                <p class="searchText">フレンド申請されています</p>
              </div>
            </div>
          </div>
        </template>
        <!-- 共有申請 -->
        <template v-else>
          <div v-for="data in noteReqData" v-bind:key="data">
            <div
              class="flex gl-shareWrap"
              @click="ShareModal(data.username, data.icon_uri, data.image_uri,data.user_to,data.user_from,data.note,data.get)"
            >
              <div class="gl-friendImg">
                <img :src="data.icon_uri" alt="フレンドアイコン" />
              </div>
              <div v-if="data.get">
                <p>{{ data.username }}</p>
                <p class="shareText">あなたの画像の共有を申請されています</p>
              </div>
              <div v-else>
                <p>{{ data.username }}</p>
                <p class="shareText">画像の共有を申請されています</p>
              </div>
            </div>
          </div>
        </template>

      </div>
      <div class="friendModal" v-if="searchFlag">
        <div class="modalWrap">
          <h2>フレンド申請を受け入れますか？</h2>
          <div class="gl-modalImg">
            <img :src="sModalIcon" alt="フレンドアイコン" />
          </div>
          <p class="modalText">{{ sModalUser }}</p>
          <div class="flex button">
            <button class="cancel" @click="Accept(0,0,sModalId,null)">拒否</button>
            <button class="accept" @click="Accept(0,1,sModalId,null)">承認</button>
          </div>
          <p class="close" @click="Cancel(0)">閉じる</p>
        </div>
      </div>
      <div class="friendModal" v-if="shareFlag">
        <div class="shareModalWrap">
          <h2>ノート共有申請を受け入れますか？</h2>
          <p class="shareModalText">{{ sModalUser }}</p>
          <div class="gl-shareModalIcon">
            <img :src="sModalIcon" alt="フレンドアイコン" />
          </div>

          <div class="gl-shareModalImg">
            <img :src="sModalImage" alt="フレンドアイコン" />
          </div>

          <div class="flex button">
            <button class="cancel" @click="Accept(1,0,sModalId,sModalNote)">拒否</button>
            <button class="accept" @click="Accept(1,1,sModalId,sModalNote)">承認</button>
          </div>
          <p class="close" @click="Cancel(1)">閉じる</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { API_SERVER, ICON_URL ,IMG_URL } from "@/assets/config.js";
export default {
  name: "GlobalHeader",
  components: {},
  data() {
    return {
      sideFriend: false,
      sideSearch: false,
      sideNotice: false,
      sideBar: "",
      glData: [],
      searchText: "",
      searchData: [],
      searchReqData: [],
      noteReqData: [],
      reqFlag: true,
      arrayFlag: false,
      searchFlag: false,
      shareFlag: false,
      sModalUser: "",
      sModalIcon: "",
      sModalId: "",
      sModalImage: "",
      sModalNote: "",
    };
  },
  computed: {},
  watch: {
    $route: function() {
      location.reload();
    },
  },
  methods: {
    Created: async function () {
      const token = this.$cookies.get("access");
      console.log(token);
      await axios
        .get(API_SERVER + "/api/v1/friends/list/", {
          headers: { Authorization: "JWT " + token },
        })
        .then((response) => {
          this.glData = response.data;
          console.log(this.glData);
          return;
        })
        .catch((e) => {
          console.log(e);
          return;
        });
      //友達申請一覧
      await axios
        .get(API_SERVER + "/api/v1/friends/apply/", {
          headers: { Authorization: "JWT " + token },
        })
        .then((response) => {
          this.searchReqData = response.data;
          console.log(this.searchReqData);
          return;
        })
        .catch((e) => {
          console.log(e);
          return;
        });
      //ノート申請一覧
      await axios
        .get(API_SERVER + "/api/v1/brains/share/request/", {
          headers: { Authorization: "JWT " + token },
        })
        .then((response) => {
          this.noteReqData = response.data;
          console.log(this.noteReqData);
          return;
        })
        .catch((e) => {
          console.log(e);
          return;
        });
    },
    GlobalSide(num) {
      if (num == 0) {
        this.sideFriend = !this.sideFriend;
        this.sideSearch = false;
        this.sideNotice = false;
      } else if (num == 1) {
        this.sideFriend = false;
        this.sideSearch = !this.sideSearch;
        this.sideNotice = false;
      } else if (num == 2) {
        this.sideFriend = false;
        this.sideSearch = false;
        this.sideNotice = !this.sideNotice;
      }
      return;
    },
    imgSrc(uri) {
      const img = ICON_URL + uri;
      return img;
    },
    ToFriend(id, img_uri, username) {
      console.log(id);
      localStorage.setItem("friendId", id);
      localStorage.setItem("friendIcon", img_uri);
      localStorage.setItem("friendUserName", username);
      this.$router.push("/FriendPage/" + id);
      // this.$router.go({path: "/FriendPage", force: true});
    },
    FriendModal(name,icon,id) {
      console.log("ddd");
      this.searchFlag = true;
      this.sModalUser = name;
      this.sModalIcon = icon;
      this.sModalId = id;
    },
    ShareModal(name,icon,image,user_to,user_from,note,get) {
      console.log("ddd");
      this.shareFlag = true;
      this.sModalUser = name;
      this.sModalIcon = icon;
      // if (get == false) {
      //   this.sModalId = user_from;
      // } else {
      //   this.sModalId = user_to;
      // }
      this.sModalId = user_to;
      this.sModalNote = note
      this.sModalImage = IMG_URL + image
    },
    Cancel(num) {
      if (num == 0) {
        this.searchFlag = false;
      }else{
        this.shareFlag = false;
      }
    },
    Accept(num,accept,user_from,note) {
      if (num == 0) {
        //フレンド登録
        if (accept == 0){
          //拒否
          const requestBody = {
            notified: true,
            apply: false,
            rejection: true,
          };
          const token = this.$cookies.get("access");
          axios
            .patch(API_SERVER + "/api/v1/friends/apply/" + user_from + "/", requestBody, {
              headers: { Authorization: "JWT " + token },})
            .then(() => {
              this.searchFlag = false;
              location.reload();
              return;
            })
            .catch((response) => {
              this.error = response.response.data.error;
            });
        }else{
          //承認
          const requestBody = {
            notified: true,
            apply: true,
            rejection: false,
          };
          const token = this.$cookies.get("access");
          axios
            .patch(API_SERVER + "/api/v1/friends/apply/" + user_from + "/", requestBody, {
              headers: { Authorization: "JWT " + token },})
            .then(() => {
              this.searchFlag = false;
              location.reload();
              return;
            })
            .catch((response) => {
              this.error = response.response.data.error;
            });
        }
      }else{
        //ノート共有
        if (accept == 0) {
          //拒否
          const requestBody = {
            notified: true,
            apply: false,
            rejection: true,
          };
          const token = this.$cookies.get("access");
          axios
            .patch(API_SERVER + "/api/v1/brains/share/" + note + "/" + user_from + "/", requestBody, {
              headers: { Authorization: "JWT " + token },})
            .then(() => {
              this.shareFlag = false;
              location.reload();
              return;
            })
            .catch((response) => {
              this.error = response.response.data.error;
            });
        } else {
          //承認
          const requestBody = {
            notified: true,
            apply: true,
            rejection: false,
          };
          const token = this.$cookies.get("access");
          axios
            .patch(API_SERVER + "/api/v1/brains/share/" + note + "/" + user_from + "/", requestBody, {
              headers: { Authorization: "JWT " + token },})
            .then(() => {
              this.shareFlag = false;
              location.reload();
              return;
            })
            .catch((response) => {
              this.error = response.response.data.error;
            });
        }
      }
    },
    Logout() {
      this.$cookies.remove("access");
      this.$router.push("/SignIn");
      return;
    },
    //検索
    Search: async function() {
      this.arrayFlag = false;
      const token = this.$cookies.get("access");
      await axios
        .get(API_SERVER + "/api/v1/search/?get=" + this.searchText, {
          headers: { Authorization: "JWT " + token },
        })
        .then((response) => {
          this.searchData = response.data;
          console.log(this.searchData);
          if (this.searchData.length == 0) {
            this.arrayFlag = true;
          }
          return;
        })
        .catch((e) => {
          console.log(e);
          return;
        });
    },
    NoticeButton(num) {
      if (num == 0) {
        this.reqFlag = true;
      } else {
        this.reqFlag = false;
      }
    }
  },
  created() {
    this.Created();
  },
};
</script>
<style scoped>
.fixed {
  position: fixed;
  width: 170px;
}
.gl-wrap {
  position: relative;
  width: 170px;
  height: 100vh;
  background: #515058;
}
.gl-global {
  height: 100%;
  position: relative;
  padding-top: 100px;
  color: #fff;
  font-size: 18px;
}
.gl-global ul {
  margin-top: 80px;
  margin-left: 40px;
}
.gl-global li {
  width: fit-content;
  margin-bottom: 16px;
}
.image {
  display: block;
  width: 80px;
  height: 80px;
  margin: 0 auto;
}
img {
  width: 100%;
}
.gl-global p {
  position: absolute;
  left: 40px;
}
.gl-global .logout {
  bottom: 100px;
}
.side {
  position: absolute;
  top: 0;
  left: 170px;
  z-index: 10;
  width: 260px;
  height: 100vh;
  background: #e3e3e4;
  box-shadow: 1px 0px 4px 2px rgb(183, 183, 183);
}
li:hover,
.pointer:hover {
  cursor: pointer;
  color: #ff6de8;
  transition: 0.1s;
}

hr {
  color: #ccc;
}

.produceButton {
  margin-top: 60px;
  text-align: center;
  bottom: 180px;
}

/* フレンド */
.sideTitle {
  justify-content: space-between;
}
h3{
  font-weight: bolder;
  margin: 20px 0 20px 16px;
  color: #515058;
}
.closeSide{
  font-size: 30px;
  font-weight: bold;
  margin: 10px 10px 0 16px;
  color: #515058;
}
.gl-friendWrap,.gl-noticeWrap,.gl-shareWrap {
  padding: 10px 0 10px 10px;
}
.gl-friendWrap:hover,.gl-noticeWrap:hover,.gl-shareWrap:hover {
  cursor: pointer;
  background: #f1f1f1;
}
.gl-friendImg {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  overflow: hidden;
}
.gl-friendImg img {
  width: 100%;
}
.gl-friendWrap p {
  font-size: 14px;
  color: #515058;
  margin-left: 20px;
  line-height: 40px;
  font-weight: bolder;
}
.gl-noticeWrap p {
  font-size: 14px;
  color: #515058;
  margin-left: 20px;
  line-height: 20px;
  font-weight: bolder;
}
.gl-shareWrap p {
  font-size: 14px;
  color: #515058;
  margin-left: 20px;
  line-height: 20px;
  font-weight: bolder;
}
.gl-shareWrap .shareText {
  font-size: 8px;
}
.gl-noticeWrap .searchText {
  font-size: 12px;
  font-weight: normal;
}

/* ユーザー検索 */

.text {
  width: 170px;
  height: 30px;
  background: #fff;
  /* border: solid 2px #ccc6c6; */
  margin: 10px 0 0 16px;
  padding: 6px 0 6px 10px;
  border-radius: 10px;
  box-shadow: 0px 0px 2px 2px #ccc inset;
}
.text:focus {
  outline: none;
}

.gl-search .wrap {
  margin-bottom: 10px;
}

.gl-search button {
  margin: 10px 0 0 4px;
  height: 30px;
  padding: 0 10px;
  color: #fff;
  background: #1e4fff;
  border-radius: 10px;
}

.gl-search button:hover {
  background: #0015ff;
}

/* 通知 */
.gl-noticeButton button{
  width: 130px;
  height: 40px;
  text-align: center;
  box-shadow: 0px 0px 1px 1px rgb(162, 162, 162) inset;
}
.gl-noticeButton button:hover{
  background: #f1f1f1;
}

/* モーダル */
.friendModal {
  position: absolute;
  top: 0;
  left: 170px;
  width: calc(100vw - 170px);
  height: 100%;
  background: rgba(255,255,255,0.4);
  z-index: 1;
}

.modalWrap {
  margin: 100px auto 0;
  width:420px;
  height: 500px;
  background: #fff;
  border-radius: 20px;
  filter: drop-shadow(0px 0px 2px rgb(111, 111, 111));
  padding-top: 60px;
}
.shareModalWrap {
  margin: 100px auto 0;
  width:520px;
  height: 700px;
  background: #fff;
  border-radius: 20px;
  filter: drop-shadow(0px 0px 20px #aaa);
  padding-top: 60px;
}
h2 {
  font-size: 24px;
  font-weight: bold;
  text-align: center;
  margin-bottom: 40px;
}
.gl-modalImg {
  margin: 0 auto;
  width: 140px;
  height: 140px;
  border-radius: 50%;
  overflow: hidden;
}
.gl-modalImg img {
  width: 100%;
}
.gl-shareModalImg {
  margin: 0 auto;
  width: 240px;
  height: 240px;
  overflow: hidden;
}
.gl-shareModalImg img {
  width: 100%;
}
.gl-shareModalIcon {
  margin: 10px auto 20px;
  width: 80px;
  height: 80px;
  border-radius: 50%;
  overflow: hidden;
}
.gl-shareModalIcon img {
  width: 100%;
}
.modalText {
  margin-top: 14px;
  font-size: 20px;
  font-weight: bold;
  text-align: center;
}

.shareModalText {
  margin-top: 14px;
  font-size: 14px;
  font-weight: bold;
  text-align: center;
}
.button {
  width: 340px;
  margin: 40px auto 0;
  justify-content: space-between;
}
.modalWrap button,.shareModalWrap button {
  float: right;
  color: #fff;
  width: 160px;
  height: 54px;
  text-align: center;
  border-radius: 5px;
  box-shadow: 4px 4px 8px 3px #bbb;
}
/* .button:hover {
  background: #7b98ff;
} */

.cancel {
  background: #ff78f4;
}
.cancel:hover {
  background: #ff32b1;
}

.accept {
  background: #1e4fff;
}
.accept:hover{
  background: #0015ff;
}
.modalContent .accept:hover {
  background: #7b98ff;
}

.close {
  margin-top: 40px;
  text-align: center;
}

.overflow {
  width: 170px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>
