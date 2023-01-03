<template>
  <div class="wrapper">
    <div class="my-pof">
      <img src="../../public/images/img001.png" alt="" class="prof-img">
      <div class="name-friend">
        <h1 class="my-name">{{ dummyUserStatus.userName }}</h1>
        <font-awesome-icon icon="fa-solid fa-gear" class="black-gear" inverse/>
      </div>
      <p class="m-id">{{dummyUserStatus.userId}}}</p>
      <p>
        <span class="m-tag" v-for="(tag,index) in dummyUserStatus.userTag" :key="index">#{{tag}}</span>
      </p>
    </div>
    <div class="my-list">
      <h1 class="list-h1">すべての記憶</h1>
      <button class="img-select" @click="toggleShareMode">共有したい記憶を選択
        <font-awesome-icon icon="fa-regular fa-share" inverse/>
      </button>
      <div class="img-wrapper">
        <BrainStatusBox brain-id="1"/>
        <BrainStatusBox brain-id="2"/>
        <BrainStatusBox brain-id="3"/>
        <BrainStatusBox brain-id="4"/>
        <BrainStatusBox brain-id="5"/>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import {defineComponent} from "vue"
import BrainStatusBox from "../../component/brain/BrainStatusBox.vue";

export default defineComponent({
  components: {BrainStatusBox},
  data() {
    return {
      dummyUserStatus:{
        userName:"ずんだもん",
        userId:"Cocororororororo",
        userTag:["おんなのこ ","ボイスロイド"]
      },
      dummyBrainArray: [{
        brainId: 0,
        imagesUrl:"../../public/images/img001"
      }
      ]
    }
  },
  beforeMount() {
    const routePath = this.$route
    console.log(routePath)
  },
  mounted() {
    this.$store.dispatch("offShareMode")
  },
  methods: {
    toggleShareMode() {
      this.$store.dispatch("toggleShareMode")
    }
  }
})
</script>

<style scoped>
* {
  font-size: 10px
}

.wrapper {
  margin-top: 50px;
  margin-left: 50px;
  margin-right: 50px;
}

.prof-img {
  width: 100px;
  height: 100px;
  border: solid 1px;
  border-radius: 100%;
  margin-right: 20px;
  float: left;
}

.name-friend {
  display: flex;
  align-items: center;
}

.my-name {
  font-size: 3.2em;
}

.black-gear {
  color: black;
  width: 28px;
  height: 28px;
  margin-left: 20px;
}

.m-id {
  font-size: 1.8em;
}

.m-tag {
  font-size: 1.4em;
}

.my-list {
  margin-top: 70px;
  clear: both;
  position: relative;
}

.list-h1 {
  font-size: 22px;
  float: left;
  margin-bottom: 50px;
}

.img-select {
  font-size: 1.6em;
  color: #ffffff;
  background-color: #3D5093;
  width: 222px;
  height: 42px;
  border-radius: 10px;
  position: absolute;
  right: 0;
}

.img-wrapper {
  clear: both;
  display: flex;
  flex-wrap: wrap;
  gap: 50px;
}

</style>
