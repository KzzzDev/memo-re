<template>
  <div class="wrapper w-full flex justify-center mt-20">
    <div class="modal-wrap w-6/12 py-16 border-solid border-2 shadow-md">
      <h1 class="text-4xl text-center mb-12" v-show="!Finished">共有しますか？</h1>
      <h1 class="text-4xl text-center mb-12" v-show="Finished">共有されました！</h1>
      <div class="wrapper w-full">
        <img :src="this.$store.getters.getTargetUserData.icon" alt="" class="w-28 h-28 shadow-lg rounded-full mx-auto">
        <p class="user-name text-center my-4">{{ this.$store.getters.getTargetUserData.name }}</p>
        <div class="img-wrap flex justify-center gap-4">
          <img v-for="(brain,index) of SelectBrains" :key="index" :src="brain.image_uri" alt=""
               class="w-24 h-24 shadow-lg" draggable="false">
        </div>
      </div>
      <div class="button flex justify-center gap-6 mt-12" v-show="!Finished">
        <button class="w-32 bg-gray-400 text-white py-3 rounded-md" @click="cancel">キャンセル</button>
        <button class="w-32 bg-red-700 text-white py-3 rounded-md" @click="share">共有</button>
      </div>
      <div class="button flex justify-center gap-6 mt-12" v-show="Finished">
        <button class="w-32 bg-blue-700 text-white py-3 rounded-md" @click="init">
          完了
        </button>
      </div>

    </div>
  </div>
</template>

<script>
// ユーザーの情報をname,iconでそれぞれ一回ずつGetters叩いてるのでBeforeMountで一括取得してDataに格納してもいいかも
import {shareNote} from "../../dummy/brain";

export default {
  name: 'shareImage',
  data() {
    return {
      Finished: false
    }
  },
  props: {
    SelectBrains: {
      type: Array,
      default: []
    },
    TargetId:{
      type:Number,
      default: -1
    }
  },
  mounted() {
    //console.log(this.SelectBrains)
  },
  methods: {
    cancel() {
      this.$store.dispatch("offShareConfirmMode")
    },
    share() {
      console.log(this.SelectBrains)
      // API処理
      for (const note of this.SelectBrains){
        console.log(note)
        shareNote(note.noteId,this.$store.getters.getTargetUserData.userId)
      }
      this.Finished = true
    },
    init() {
      this.$store.dispatch("initShareFlags")
      this.$emit("init")
    }
  }
};
</script>

<style scoped>
.status-list {
  overflow-x: scroll;
}

.status-list img {
  flex-shrink: 0;
}
</style>
