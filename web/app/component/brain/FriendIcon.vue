<template>
  <div class="friend-wrap"
       @drop.stop="drop"
       @dragover.prevent
       @dragenter.prevent>
    <img :src="FriendData.icon" alt="" class="w-32 h-32 shadow-lg rounded-full">
    <p class="text-center">{{ FriendData.name }}</p>
  </div>
</template>

<script lang="ts">
import {defineComponent} from "vue"

export default defineComponent({
  name: "FriendIcon",
  props: {
    FriendData: {
      type: Object,
      default: {}
    }
  },
  methods:{
    drop:async function(){
      //  ここでState更新
      await this.$store.dispatch("setTargetUserData",this.FriendData)

      await this.$store.dispatch("onShareConfirmMode")
    }
  }
})
</script>

<style scoped>

</style>