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
          <li><router-link to="/CreateImage">ノート作成</router-link></li><br>
          <li @click="GlobalSide(0)" class="pointer">フレンド</li>
          <li @click="GlobalSide(1)" class="pointer">検索</li>
          <li @click="GlobalSide(2)" class="pointer">通知</li>
        </ul>
        <p class="logout pointer" @click="Logout()">ログアウト</p>
      </div>
      <!-- フレンド -->
      <div class="side" v-if="sideFriend">
        <h3>フレンドリスト</h3>
        <hr />
        <div v-for="data in glData" v-bind:key="data">
          <div
            class="flex gl-friendWrap"
            @click="ToFriend(data.id, data.icon_uri, data.username)"
          >
            <div class="gl-friendImg">
              <img :src="data.icon_uri" alt="フレンドアイコン" />
            </div>
            <p>{{ data.username }}</p>
          </div>
        </div>
      </div>
      <div class="side gl-search" v-if="sideSearch">
        <h3>ユーザー検索</h3>
        <hr />
        <div class="flex wrap">
          <input v-model="searchText" type="text" class="text">
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
            <p>{{ data.username }}</p>
          </div>
        </div>
      </div>
      <div class="side" v-if="sideNotice">
        <h3>通知BOX</h3>
        <hr />
        <div class="flex gl-noticeButton">
          <button @click="NoticeButton(0)">友達申請</button>
          <button @click="NoticeButton(1)">共有申請</button>
        </div>
        <!-- 友達申請 -->
        <template v-if="reqFlag == true">
          <div v-for="data in searchReqData" v-bind:key="data">
            <div
              class="flex gl-friendWrap"
              @click="ToFriend(data.id, data.icon_uri, data.username)"
            >
              <div class="gl-friendImg">
                <img :src="data.icon_uri" alt="フレンドアイコン" />
              </div>
              <p>{{ data.username }}</p>
            </div>
          </div>
        </template>
        <!-- 共有申請 -->
        <template v-else>
          <div v-for="data in noteReqData" v-bind:key="data">
            <div
              class="flex gl-friendWrap"
              @click="ToFriend(data.id, data.icon_uri, data.username)"
            >
              <div class="gl-friendImg">
                <img :src="data.icon_uri" alt="フレンドアイコン" />
              </div>
              <p>{{ data.username }}</p>
            </div>
          </div>
        </template>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { API_SERVER, ICON_URL } from "@/assets/config.js";
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
        .get(API_SERVER + "/api/v1/brains/share/request/answer", {
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
  bottom: 100px;
  left: 40px;
}
.side {
  position: absolute;
  top: 0;
  left: 170px;
  z-index: 5;
  width: 260px;
  height: 100vh;
  background: #e3e3e4;
  box-shadow: 6px 0px 8px 3px #ccc;
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

/* フレンド */
h3 {
  font-weight: bolder;
  margin: 20px 0 20px 16px;
  color: #515058;
}
.gl-friendWrap {
  padding: 10px 0 10px 10px;
}
.gl-friendWrap:hover {
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

/* ユーザー検索 */

.text {
  width: 170px;
  height: 30px;
  background: #fff;
  /* border: solid 2px #ccc6c6; */
  margin: 10px 0 0 16px;
  padding: 6px 0 6px 10px;
  border-radius: 10px;
  box-shadow: 0px 0px 6px 3px #bbb inset;
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
  background: #6d8dff;
  border-radius: 10px;
}

/* 通知 */
.gl-noticeButton button{
  width: 130px;
  height: 40px;
  text-align: center;
  box-shadow: 0px 0px 6px 3px #ccc inset;
}
.gl-noticeButton button:hover{
  background: #f1f1f1;
}
</style>
