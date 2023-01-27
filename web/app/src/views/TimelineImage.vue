<template>
  <div class="flex relative">
    <div class="fixedGlobal">
      <GlobalHeader />
    </div>
    <div class="preOWrap">
      <div class="flex preOverWrap">
        <div class="preWrap">
          <div class="flex innerWrap">
            <p class="title">{{ title }}</p>
          </div>
          <ul class="flex" style="flex-wrap: wrap;">
            <li v-for="word in keyword" v-bind:key="word" class="keyword" style=" margin-bottom: 6px;">
              {{ word }}
            </li>
          </ul>
          <p class="text_uri">{{ text_uri }}</p>
          <router-link to="/timeline"><p class="button">戻る</p></router-link>
        </div>
        <div class="preImg">
          <img :src="image_uri" alt="画像" />
          <p class="time">{{ time[0] }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { IMG_URL } from "@/assets/config.js";
import GlobalHeader from "@/components/GlobalHeader.vue";
export default {
  name: "ImageView",
  data() {
    return {
      id: localStorage.getItem("friendNoteId"),
      keyword: localStorage.getItem("friendNoteKeyword").split(","),
      title: localStorage.getItem("friendNoteTitle"),
      image_uri: IMG_URL + localStorage.getItem("friendNoteImage"),
      user: localStorage.getItem("friendNoteUser"),
      text_uri: localStorage.getItem("friendNoteText"),
      data: [],
      scrollData: [],
      keywordAry: "",
      is_public: null,
      modalFlag: false,
      errorFlag: false,
      time: "",
    };
  },
  components: {
    GlobalHeader,
  },
  methods: {
  },
  created() {
    if (this.$cookies.get("access") === null) {
      this.$router.push("/SignIn");
      return;
    }
    this.time = localStorage.getItem("friendTime").split("T");
    // this.ImageData();
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
.title {
  width: 400px;
  overflow-wrap: break-word;
  font-size: 28px;
  font-weight: bolder;
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
  min-height: 400px;
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
  box-shadow: 6px 5px 6px 3px rgb(147, 147, 147);
}

.time {
  margin-top: 10px;
  font-weight: bold;
  text-align: end;
}

.button {
  float: left;
  color: #fff;
  background: #1e4fff;
  width: 160px;
  height: 54px;
  line-height: 54px;
  text-align: center;
  border-radius: 5px;
  box-shadow: 1px 2px 1px 1px rgb(194, 194, 194);
}
.button:hover {
  background: #0015ff;
}
</style>
