<template>
  <div class="fixed">
    <div class="gl-wrap">
      <div class="gl-global">
        <router-link to="/myPage" class="image"
          ><img src="@/assets/logo.png" alt="ロゴ"
        /></router-link>
        <!-- <div class="image"><img src="@/assets/logo.png" alt="ロゴ" /></div> -->
        <ul>
          <li><router-link to="/MyPage">Profile</router-link></li>
          <li><router-link to="/CreateImage">Create</router-link></li>
          <li @click="GlobalSide(0)" class="pointer">Friend</li>
          <li @click="GlobalSide(1)" class="pointer">Search</li>
          <li @click="GlobalSide(2)" class="pointer">Notice</li>
        </ul>
        <p class="logout pointer" @click="Logout()">Logout</p>
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
      <div class="side" v-if="sideSearch">
        <h3>ユーザー検索</h3>
        <hr />
      </div>
      <div class="side" v-if="sideNotice">
        <h3>通知BOX</h3>
        <hr />
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
    };
  },
  computed: {},
  watch: {
    $route() {
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
      this.$router.push("/FriendPage/");
      // this.$router.go({path: "/FriendPage", force: true});
    },
    Logout() {
      this.$cookies.remove("access");
      this.$router.push("/SignIn");
      return;
    },
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
  margin-left: 56px;
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
  left: 56px;
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
</style>
