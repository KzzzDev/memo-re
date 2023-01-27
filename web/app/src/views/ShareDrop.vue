<template>
  <div class="flex">
    <div class="fixedGlobal">
      <GlobalHeader />
    </div>
    <div class="wrap">
      <h2>共有相手にドラッグ＆ドロップ</h2>
      <div draggable="true" @dragstart="dragList($event)" class="imageBox">
        <img :src="image" alt="画像" />
      </div>
      <div class="flex friendWrap">
        <div v-for="data in friendData" v-bind:key="data">
          <div
            class="gl-friendWrap"
            @drop="dropList(data.icon_uri,data.username,data.id)"
            @dragover.prevent
            @dragenter.prevent
          >
            <div class="gl-friendImg">
              <img :src="data.icon_uri" alt="フレンドアイコン" />
            </div>
            <p>{{ data.username }}</p>
          </div>
        </div>
      </div>
      <div v-if="modal == true" class="modalWrap">
        <div class="modal">
          <h2>共有しますか？</h2>
          <div class="modalImage">
            <img :src="modalIcon" alt="アイコン">
          </div>
          <p>{{ modalUser }}</p>
          <p v-if="errorFlag == true">すでに相手から申請が来ています</p>
          <div class="flex button">
            <button class="cancel" @click="Cancel()">キャンセル</button>￥
            <button class="accept" @click="Share()">共有</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { API_SERVER } from "@/assets/config.js";
import VueElementLoading from "vue-element-loading";
import GlobalHeader from "@/components/GlobalHeader.vue";

export default {
  data() {
    return {
      friendData: [],
      image: localStorage.getItem("DropImage"),
      modal: false,
      modalIcon: null,
      modalUser: null,
      modalId: null,
      errorFlag: false,
    };
  },
  name: "CreateImage",
  components: {
    VueElementLoading,
    GlobalHeader,
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
          this.friendData = response.data;
          console.log(this.friendData);
          return;
        })
        .catch((e) => {
          console.log(e);
          return;
        });
    },
    dragList(event, dragId){
      event.dataTransfer.effectAllowed = 'move';
      event.dataTransfer.dropEffect = 'move';
      event.dataTransfer.setData('list-id',dragId);
      console.log(dragId)
    },
    dropList(icon, user ,id){
      this.modalIcon = icon;
      this.modalUser = user;
      this.modalId = id;
      this.errorFlag = false;
      this.modal = true;
    },
    Cancel() {
      this.modal = !this.modal;
    },
    Share() {
      const requestBody = {
        user_to: this.modalId,
        note: localStorage.getItem("noteId"),
        get: false,
      };
      console.log(requestBody);
      const token = this.$cookies.get("access");
      axios
        .post(API_SERVER + "/api/v1/brains/share/", requestBody, {
          headers: { Authorization: "JWT " + token },})
        .then(() => {
          console.log("成功");
          this.modal = !this.modal;
          return;
        })
        .catch(() => {
          this.errorFlag = true;
        });
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
    console.log(this.data);
  },
};
</script>

<style scoped>
.wrap {
  margin: 0 auto;
  padding-top: 60px;
  width: 900px;
  /* background: #fff; */
  position: relative;
}
h2 {
  font-size: 30px;
  font-weight: bold;
  text-align: center;
  margin-bottom: 40px;
}
.imageBox {
  width: 200px;
  height: 200px;
  background: #000;
  margin:0 auto;
}
.imageBox img {
  width: 100%;
  height: 100%;
}
.friendWrap {
  margin-top: 100px;
  padding: 20px;
  flex-wrap: wrap;
  border: dashed 4px #ccc;
}
.gl-friendWrap {
  padding: 10px 10px 10px 10px;
}
.gl-friendImg {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  overflow: hidden;
}
.gl-friendImg img {
  width: 100%;
}
.gl-friendWrap p {
  font-size: 14px;
  color: #515058;
  line-height: 40px;
  font-weight: bolder;
  text-align: center;
}
.modalWrap {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left:0;
  background: rgba(255, 255, 255, 0.4);
}
.modal {
  padding-top: 40px;
  margin: 100px auto 0;
  border-radius: 26px;
  width: 420px;
  height: 460px;
  background: #fff;
  filter: drop-shadow(0px 0px 2px rgb(111, 111, 111));
}
.modalImage {
  width: 140px;
  height: 140px;
  border-radius: 50%;
  overflow: hidden;
  margin: 0 auto;
}
.modalImage img {
  width: 100%;
}
.modal p {
  margin-top: 6px;
  font-size: 20px;
  font-weight: bold;
  text-align: center;
}
.button {
  width: 340px;
  margin: 60px auto 0;
  justify-content: space-between;
}
.modal button {
  float: right;
  color: #fff;
  width: 160px;
  height: 54px;
  text-align: center;
  border-radius: 5px;
  box-shadow: 1px 1px 1px 1px rgb(150, 150, 150);
}
.cancel {
  background: #ff78f4;
}
.cancel:hover {
  background: #ff32b1;
}
.accept {
  background: #1e4fff;
}
.accept:hover {
  background: #0015ff;
}
.modalContent .accept:hover {
  background: #0037ff;
}
</style>
