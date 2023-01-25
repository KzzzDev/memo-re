<template>
  <div class="flex">
    <div class="fixedGlobal">
      <GlobalHeader />
    </div>
    <div>
      <div class="userWrap">
        <div class="flex">
          <div class="myIcon"><img :src="friendIcon" alt="アイコン" v-cloak></div>
          <div class="textWrap">
            <p class="username" v-cloak>{{ friendUsername }}</p>
          </div>
          <template v-if="friendReqFlag == false">
            <button class="friendReq" @click="FriendReq(id)">フレンド申請</button>
          </template>
          <template v-else>
            <p class="friendReq">フレンド申請済み</p>
          </template> 
        </div>
        <div class="flex buttonWrap">
          <h2>すべての記憶</h2>
        </div>
      </div>
      <div class="imageWrap">
        <div
          v-for="image in data"
          v-bind:key="image"
          class="imageBox"
          @click="ImageView(image.id,image.keyword,image.title,image.image_uri,image.user,image.text_uri,image.created_at)"
        >     
          <!-- <p>{{ image.title }}</p>
          <p>{{ image.text_uri }}</p> -->
          <div class="myPageImage">
            <img :src="'/media/brain/' + image.image_uri" alt="画像" />
            <p class="opacity">{{ image.title }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { API_SERVER } from "@/assets/config.js";
import GlobalHeader from "@/components/GlobalHeader.vue";

export default {
  name: "FriendPage",
  components: {
    GlobalHeader,
  },
  data() {
    return {
      friendUsername: localStorage.getItem("friendUserName"),
      friendIcon: localStorage.getItem("friendIcon"),
      data: [],
      user: [],
      id: localStorage.getItem("friendId"),
      friendReqFlag: false,
    };
  },
  methods: {
    Created: async function () {
      const userId = localStorage.getItem("friendId");
      const token = this.$cookies.get("access");
      console.log(token);
      await axios
        .get(API_SERVER + "/api/v1/brains/friends/" + userId +"/", {
          headers: { Authorization: "JWT " + token },
        })
        .then((response) => {
          this.data = response.data;
          console.log(this.data);
          return;
        })
        .catch((e) => {
          console.log(e);
          return;
        });
    },
    ImageView(id,keyword,title,image_uri,user,text_uri,time) {
      localStorage.setItem("friendNoteId", id);
      localStorage.setItem("friendNoteKeyword", keyword);
      localStorage.setItem("friendNoteTitle", title);
      localStorage.setItem("friendNoteImage", image_uri);
      localStorage.setItem("friendNoteUser", user);
      localStorage.setItem("friendNoteText", text_uri);
      localStorage.setItem("friendTime",time)
      this.$router.push("/friendImageView");
    },
    FriendReq: async function() {
      const token = this.$cookies.get("access");
      const requestBody = {
        user_to: this.id,
      };
      await axios
        .post(API_SERVER + "/api/v1/friends/", requestBody, {
          headers: { Authorization: "JWT " + token },
        })
        .then(() => {
          this.friendReqFlag = true;
          console.log("成功");
        })
        .catch((e) => {
          this.friendReqFlag = true;
          console.log(e);
          console.log("失敗");
        });
    },
  },
  created() {
    if (this.$cookies.get("access") === null) {
      this.$router.push("/SignIn");
      return;
    }
    this.Created();
  },
};
</script>
<style scoped>
.userWrap{
  margin: 60px 0 0 40px;
}
.myIcon {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  overflow: hidden;
}
.myIcon img {
  width: 100%;
}
.textWrap {
  margin: 10px 0 0 40px;
}
.username {
  font-size: 32px;
  font-weight: bold;
}
.buttonWrap {
  margin-top: 60px;
  width: calc(100vw - 260px);
  justify-content: space-between;
  flex-wrap: wrap;
}
.buttonWrap h2 {
  font-weight: bolder;
}
.buttonWrap button {
  color: #fff;
  font-size: 16px;
  background: #6d8dff;
  padding: 6px 12px;
  border-radius: 5px;
}
h2 {
  font-size: 22px;
  line-height: 30px;
}
.imageWrap {
  padding-left: 20px;
  width: calc(100vw - 190px);
  display: flex;
  /* justify-content: space-between; */
  flex-wrap: wrap;
}
.imageBox {
  margin: 16px;
}
.imageBox:hover {
  cursor: pointer;
}
.myPageImage {
  border: solid 1px #ccc;
  width: 180px;
  position: relative;
  box-shadow:8px 6px 8px 3px #999;
}
.myPageImage img {
  width: 100%;
}

.myPageImage p{
  width: 176px;
  height: 176px;
  text-align: center;
  line-height: 176px;
  font-weight: bold;
  color: #fff;
  background: rgba(0,0,0,0.4);
  position: absolute;
  top: 0;
  left: 0;
  opacity: 0;
}
.myPageImage p:hover{
  opacity: 1;
  transition: 0.6s;
}

.friendReq {
  margin: 10px 0 0 40px;
  height: 30px;
  line-height: 30px;
  padding: 0 10px;
  color: #fff;
  background: #6d8dff;
  border-radius: 10px;
}
</style>
