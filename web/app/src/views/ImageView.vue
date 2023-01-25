<template>
  <div class="flex">
    <div class="fixedGlobal">
      <GlobalHeader />
    </div>
    <div class="preOWrap">
      <div class="flex preOverWrap">
        <div class="preWrap">
          <div class="flex innerWrap">
            <p class="title">{{ data.title }}</p>
            <template v-if="this.is_public === true">
              <p class="public" @click="Public(0)"><img src="/img/11.png" alt="画像" /></p>
            </template>
            <template v-else>
              <p class="public" @click="Public(1)"><img src="/img/1.png" alt="画像" /></p>
            </template>
          </div>
          <ul class="flex">
            <li v-for="word in keywordAry" v-bind:key="word" class="keyword">
              {{ word }}
            </li>
          </ul>
          <p class="text_uri">{{ data.text_uri }}</p>
        </div>
        <div class="preImg">
          <img :src="data.image_uri" alt="画像" />
          <p class="time">{{ time[0] }}</p>
        </div>
      </div>
      <button @click="BtnClick()">この画像を共有する</button>
      <div class="scrWrap">
        <ul class="flex">
          <li
            v-for="img in scrollData"
            v-bind:key="img"
            class="scrImg"
            @click="ImageView(img.id, img.title, img.keyword,img.img_uri, img.text_uri, img.is_public ,img.created_at)"
          >
            <!-- {{ img.is_public }} -->
            <img :src="ImgSrc(img.image_uri)" alt="画像" />
            <p class="opacity">{{ img.title }}</p>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { API_SERVER, IMG_URL } from "@/assets/config.js";
import GlobalHeader from "@/components/GlobalHeader.vue";
export default {
  name: "ImageView",
  data() {
    return {
      data: [],
      scrollData: [],
      keywordAry: "",
      is_public: null,
      time: "",
    };
  },
  components: {
    GlobalHeader,
  },
  methods: {
    ImageData: async function () {
      const noteId = localStorage.getItem("noteId");
      const token = this.$cookies.get("access");
      await axios
        .get(API_SERVER + "/api/v1/brains/" + noteId + "/", {
          headers: { Authorization: "JWT " + token },
        })
        .then((response) => {
          this.data = response.data;
          this.data.image_uri = IMG_URL + this.data.image_uri;
          this.keywordAry = this.data.keyword.split(",");
          this.is_public = this.data.is_public;
          this.time = this.data.created_at.split("T");
          //console.log(this.data);
          console.log("成功");
          return;
        })
        .catch((e) => {
          console.log(e);
          // this.$router.push({ name: "myPage" });
          return;
        });
    },
    ScrollData: async function () {
      const token = this.$cookies.get("access");
      // .get(API_SERVER + "/api/v1/brains/" + id, {
      await axios
        .get(API_SERVER + "/api/v1/brains/", {
          headers: { Authorization: "JWT " + token },
        })
        .then((response) => {
          this.scrollData = response.data;
          //console.log(this.scrollData);
          return;
        })
        .catch((e) => {
          console.log(e);
          return;
        });
    },
    ImgSrc(img_uri) {
      const img = IMG_URL + img_uri;
      return img;
    },
    ImageView(noteId,title,keyword,img_uri, text_uri, is_public, time) {
      //console.log("click");
      localStorage.setItem("noteId", noteId);
      this.data.title = title;
      this.keywordAry = keyword.split(",");
      this.data.img_uri = IMG_URL + img_uri;
      this.data.text_uri = text_uri;
      this.is_public = is_public;
      this.time = time.split("T");
      // this.$router.go({ path: this.$router.currentRoute.path, force: true });
    },
    Public: async function (flag) {
      if (flag === 0) {
        this.is_public = false;
      } else {
        this.is_public = true;
      }
      const requestBody = {
        is_public: this.is_public,
      };
      const noteId = localStorage.getItem("noteId");
      const token = this.$cookies.get("access");
      // .post(API_SERVER + "/api/v1/brains/" + this.user, requestBody, {
      await axios
        .patch(API_SERVER + "/api/v1/brains/" + noteId + "/", requestBody, {
          headers: { Authorization: "JWT " + token },
        })
        .then(() => {
          console.log("成功");
          return;
        })
        .catch((e) => {
          console.log(e);
          return;
        });

      this.scrollData.forEach(data => {
        if (data.id == noteId) {
          data.is_public = !data.is_public;
        }
      });
    },
    //共有のボタンクリック
    BtnClick() {
      localStorage.setItem("DropImage",this.data.image_uri);
      this.$router.push("/ShareDrop");
      return;
    },
  },
  created() {
    if (this.$cookies.get("access") === null) {
      this.$router.push("/SignIn");
      return;
    }
    this.ImageData();
    this.ScrollData();
  },
};
</script>

<style scoped>
.preOWrap {
  margin: 0 auto;
  padding-top: 100px;
  width: 900px;
}
.preOverWrap {
  justify-content: space-between;
  flex-wrap: wrap;
}
.preWrap {
  width: 400px;
}
.innerWrap {
  justify-content: space-between;
  flex-wrap: wrap;
}
.innerWrap img {
  width: 30px;
}
.title {
  font-size: 28px;
  font-weight: bolder;
}
.public {
  font-weight: bolder;
  line-height: 32px;
  cursor: pointer;
}
.text_uri {
  font-size: 18px;
}
.keyword {
  color: #fff;
  font-size: 16px;
  background: #6d8dff;
  padding: 4px 8px;
  margin-right: 10px;
  border-radius: 5px;
}
.text_uri {
  width: 400px;
  word-wrap: break-word;
  margin-top: 60px;
  line-height: 24px;
}
.preImg {
  width: 360px;
}
.preImg img {
  width: 100%;
  border-radius: 20px;
}
.scrWrap {
  margin-top: 60px;
}
.scrWrap ul {
  width: 900px;
  overflow-x: scroll;
}
.scrImg {
  position: relative;
  width: 120px;
  height: 120px;
  margin-right: 30px;
  cursor: pointer;
}
.scrImg img {
  width: 120px;
}

.scrImg p {
  font-size: 12px;
  width: 120px;
  height: 120px;
  text-align: center;
  line-height: 120px;
  font-weight: bold;
  color: #fff;
  background: rgba(0, 0, 0, 0.4);
  position: absolute;
  top: 0;
  left: 0;
  opacity: 0;
}
.scrImg p:hover {
  opacity: 1;
  transition: 0.6s;
}

button {
  margin-top: 40px;
  color: #fff;
  background: #F88CDF;
  padding: 10px 26px;
  border-radius: 10px;
}

.time {
  margin-top: 10px;
  font-weight: bold;
  text-align: end;
}
</style>
