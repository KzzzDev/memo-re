<template>
    <div class=" w-full flex flex-col items-center">
        <h1 class="text-4xl text-center mt-10">共有相手にドラック&ドロップ</h1>
        <div class="w-36 h-36 mx-auto mt-16 relative">
          <img :src="SelectBrains[0].image_uri" alt="" class="w-36 h-36 shadow-lg relative z-50" draggable="true">
          <div class="w-36 h-36 shadow-lg absolute top-3 left-3 z-20 bg-gray-300"/>
          <div class="w-36 h-36 shadow-lg absolute top-6 left-6 z-10 bg-gray-200"/>
        </div>

        <div class="img-wrap flex justify-center mt-10 gap-4">
            <img v-for="(brain,index) of SelectBrains" :key="index" :src="brain.image_uri" alt="" class="w-24 h-24 shadow-lg" draggable="false">
        </div>
        <div class="user-wrap p-16 w-11/12  mt-16 border-4 border-dashed flex flex-wrap justify-start gap-10">
            <FriendIcon v-for="friend of dummyFriendList" :key="friend.id" :FriendData="friend" />

        </div>
    </div>
</template>

<script  lang="ts">
import {defineComponent} from "vue"
import FriendIcon from "../../component/brain/FriendIcon.vue"
import {getFriendList} from "../../dummy/brain";
export default defineComponent({
  name:"ShareSelect",
  components:{
    FriendIcon
  },
  data(){
    return{
      dummyFriendList:[

      ]
    }
  },
  props:{
    SelectBrains:{
      type:Array,
      default:[]
    }
  },
  mounted() {
    this.dummyFriendList = getFriendList(this.$store.getters.getUserId)
  }
})
</script>

<style scoped>

</style>
