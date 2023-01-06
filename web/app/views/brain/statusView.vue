<template>
  <div class="status-wrapper">
    <div class="status-info mt-24">
      <StatusMain :noteStatus="dummyNoteStatus"/>
    </div>
    <div class="status-list mt-16 py-2 w-10/12 mx-auto flex gap-6">
      <router-link v-for="note in dummyOtherNoteList" :to="'/note/'+note.id" :key="note.id">
        <img :src="note.img_uri" alt="" class="w-28 h-28 shadow-lg">
      </router-link>

      <!--      <img src="../../public/images/brains/img001.png" alt="" class="w-28 h-28 shadow-lg">-->
      <!--      <img src="../../public/images/brains/img001.png" alt="" class="w-28 h-28 shadow-lg">-->
      <!--      <img src="../../public/images/brains/img001.png" alt="" class="w-28 h-28 shadow-lg">-->
      <!--      <img src="../../public/images/brains/img001.png" alt="" class="w-28 h-28 shadow-lg">-->
      <!--      <img src="../../public/images/brains/img001.png" alt="" class="w-28 h-28 shadow-lg">-->
      <!--      <img src="../../public/images/brains/img001.png" alt="" class="w-28 h-28 shadow-lg">-->
      <!--      <img src="../../public/images/brains/img001.png" alt="" class="w-28 h-28 shadow-lg">-->
      <!--      <img src="../../public/images/brains/img001.png" alt="" class="w-28 h-28 shadow-lg">-->
      <!--      <img src="../../public/images/brains/img001.png" alt="" class="w-28 h-28 shadow-lg">-->
    </div>
  </div>
</template>

<script>
import StatusMain from '../../component/brain/statusMain.vue';

export default {
  name: 'status',
  data() {
    return {
      dummyNoteStatus: {
        text_uri: "日曜日の午後にお母さんとピクニックレジャーシートをしいて緑がたくさんの公園でサンドイッチやフルーツをたくさん食べた！去年もきたけど今年もたくさん人がいた。来年もたくさん人がいるかなあ。いると思うよ。いるといいなあ来年も楽しみだ！ピクニックピクニック楽しいピクニック来年もたくさん歩きたいな！来年もたくさん人がいるかなあ。いると思うよ。いるといいなあ来年も楽しみだ！ピクニックピクニック楽しいピクニック来年もたくさん歩きたいな！",
        keyword: ["ピクニック", "ランチ", "公園"], // APIで受け取る際はStringをsplitしてArrayにする。
        title: "楽しいピクニック",
        image_uri:"https://images.unsplash.com/photo-1515405295579-ba7b45403062?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80"
      },
      dummyOtherNoteList: [
        {
          id: 2,
          img_uri: "https://images.unsplash.com/photo-1558865869-c93f6f8482af?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2081&q=80"
        },
        {
          id: 3,
          img_uri: "https://images.unsplash.com/photo-1536098561742-ca998e48cbcc?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2036&q=80"
        },
        {
          id: 4,
          img_uri: "https://images.unsplash.com/photo-1462331940025-496dfbfc7564?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=911&q=80"
        },
        {
          id: 5,
          img_uri: "https://images.unsplash.com/photo-1460661419201-fd4cecdf8a8b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80"
        },
      ]
    }
  },
  components: {
    StatusMain
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
