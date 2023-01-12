<template>
  <div class="wrapper flex justify-center">
    <div class="left-contents w-5/12 relative">
      <h1 class="text-3xl mt-4">{{ noteStatus.title }}</h1>
      <div class="show-mark absolute right-36 top-0 mt-4">
        <img src="../../public/images/eye.png" alt="" class="w-8 h-8">
        <p>公開</p>
      </div>
      <div class="tag flex flex-wrap gap-2 mt-4">
        <div class="bg-blue-500 text-white rounded-full text-center w-auto px-5 py-3  flex items-center items-center"
           v-for="(tag,index) in noteStatus.keyword.split(',')"
           :key="index"
        >
        <p>  {{ tag }}</p>
        </div>
      </div>
      <p class="main-txt mt-10 w-96">
        {{ noteStatus.text_uri }}
      </p>
      <button @click="$emit('request')"
          v-if="!previewMode&&isFriend" class="bg-pink-400 text-white rounded-md text-center w-32 py-1 absolute bottom-0 right-36">
        記憶をもらう
      </button>
    </div>
    <div class="right-contents w-5/12">
      <img :src="noteStatus.image_uri" alt="" class="w-10/12 h-8/12">
    </div>
  </div>
</template>

<script lang="js">
import {defineComponent} from "vue"

export default defineComponent({
  name: "status-main",
  data() {
    return {
    }
  },
  props: {
    previewMode: {
      type: Boolean,
      default: false
    },
    noteStatus: {
      type: Object,
      default: {}
    }
  },
  computed:{
    isFriend(){
     return this.noteStatus.user != this.$store.getters.getUserId
    }
  }
})
</script>

<style scoped>

</style>
