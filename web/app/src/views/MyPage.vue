<template>
  <div class="flex">
    <div class="fixedGlobal">
      <GlobalHeader />
    </div>
    <div>
      <div class="userWrap">
        <div class="flex">
          <div class="myIcon">
            <img :src="user.icon_uri" alt="アイコン" v-cloak />
          </div>
          <div class="textWrap flex">
            <p class="username" v-cloak>{{ user.username }}</p>
            <router-link to="/Update"><img class="setting" src="/img/settings.png" alt="設定アイコン"></router-link>
          </div>
          
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
          @click="ImageView(image.id)"
        >
          <!-- <p>{{ image.title }}</p>
          <p>{{ image.text_uri }}</p> -->
          <div class="myPageImage">
            <img :src="'/media/brain/' + image.image_uri" alt="画像" />
            <div>
              <p class="opacity">{{ image.title }}</p>
            </div>
            <div class="triangle" v-if="image.is_public == false">
              <p class="active"><img src="/img/1.png" alt="画像" /></p>
            </div> 
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
  name: "MyPage",
  components: {
    GlobalHeader,
  },
  data() {
    return {
      data: [],
      user: [],
    };
  },
  methods: {
    Created: async function () {
      const token = this.$cookies.get("access");
      //console.log(token);
      await axios
        .get(API_SERVER + "/api/v1/auth/users/me/", {
          headers: { Authorization: "JWT " + token },
        })
        .then((response2) => {
          this.user = response2.data;
          console.log(this.user);
          return;
        })
        .catch((e) => {
          console.log(e);
          return;
        });
      // .get(API_SERVER + "/api/v1/brains/" + id, {
      await axios
        .get(API_SERVER + "/api/v1/brains/", {
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
    ImageView(noteId) {
      localStorage.setItem("noteId", noteId);
      this.$router.push("/imageView");
    },
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
    this.Created();
    
  },
};
</script>
<style scoped>
.userWrap {
  margin: 60px 0 0 40px;
}
.myIcon {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  overflow: hidden;
  box-shadow: 0px 0px 4px 1px rgb(80, 80, 80);
  display: flex;
  justify-content: center;
  align-items: center;
}
.myIcon img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.textWrap {
  margin: 10px 0 0 40px;
}
.textWrap p {
  margin-right: 20px;
}
.setting {
  width: 30px;
  height: 30px;
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
  box-shadow: 3px 4px 8px 2px rgb(75, 75, 75);
}
.myPageImage img {
  width: 100%;
}
.myPageImage .opacity {
  width: 178px;
  height: 178px;
  padding-left: 6px;
  text-align: center;
  line-height: 178px;
  font-weight: bold;
  color: #fff;
  background: rgba(0, 0, 0, 0.4);
  position: absolute;
  top: 1px;
  left: 1px;
  opacity: 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.myPageImage p:hover {
  opacity: 1;
  transition: 0.6s;
}
.triangle::before {
  content: "";
  top: 0;
  right: 0;
  border-bottom: 3em solid transparent;
  border-right: 3em solid rgba(255, 255, 255, 0.8); /* ラベルの色はここで変更 */
  position: absolute;
  z-index: 0;
}
.triangle::after {
  font-weight: bold;
  display: block;
  top: 5px;
  transform: rotate(45deg);
  color: #000; /* 文字色はここで変更 */
  right: 0;
  position: absolute;
  z-index: 0;
}
.active {
  position: absolute;
  width: 20px;
  top: 4px;
  right:4px;
  z-index: 1;
}
.active img {
  width:100%;
}
</style>