<template>
  <div class="flex">
    <div class="fixedGlobal">
      <GlobalHeader />
    </div>
    <div>
      <div class="userWrap">
        <div class="flex">
          <div class="myIcon" v-cloak><img :src="user.icon_uri" alt="アイコン"></div>
          <div class="textWrap">
            <p class="username" v-cloak>{{ user.username }}</p>
          </div>
        </div>
        <div class="flex buttonWrap">
          <h2>すべての記憶</h2>
          <button>申請したい記憶を選択</button>
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
      console.log(token);
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
    },
    ImageView(noteId) {
      localStorage.setItem("noteId", noteId);
      this.$router.push("/imageView");
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
  margin: 20px;
}
.imageBox:hover {
  cursor: pointer;
}
.myPageImage {
  width: 180px;
  position: relative;
}
.myPageImage img {
  width: 100%;
}

.myPageImage p{
  width: 180px;
  height: 180px;
  text-align: center;
  line-height: 180px;
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
}
</style>
