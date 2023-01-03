<template>
    <div class="wrapper w-max mx-auto">
        <h1 class="text-4xl text-center mt-10">共有相手にドラック&ドロップ</h1>
        <img src="../../public/images/brains/img001.png" alt="" class="w-36 h-36 shadow-lg mx-auto mt-16">
        <div class="img-wrap flex justify-center mt-10 gap-4">
            <img v-for="(brain,index) of SelectBrains" :key="index" :src="'../'+brain.imagesUrl" alt="" class="w-24 h-24 shadow-lg">
        </div>
        <div class="user-wrap p-16 w-11/12 mx-auto mt-16 border-4 border-dashed flex flex-wrap justify-center gap-8">
            <div class="friend-wrap">
                <img src="../../public/images/brains/img001.png" alt="" class="w-32 h-32 shadow-lg rounded-full">
                <p class="text-center">フレンド名前</p>
            </div>
            <div class="friend-wrap">
                <img src="../../public/images/brains/img001.png" alt="" class="w-32 h-32 shadow-lg rounded-full">
                <p class="text-center">フレンド名前</p>
            </div>
            <div class="friend-wrap">
                <img src="../../public/images/brains/img001.png" alt="" class="w-32 h-32 shadow-lg rounded-full">
                <p class="text-center">フレンド名前</p>
            </div>
            <div class="friend-wrap">
                <img src="../../public/images/brains/img001.png" alt="" class="w-32 h-32 shadow-lg rounded-full">
                <p class="text-center">フレンド名前</p>
            </div>
            <div class="friend-wrap">
                <img src="../../public/images/brains/img001.png" alt="" class="w-32 h-32 shadow-lg rounded-full">
                <p class="text-center">フレンド名前</p>
            </div>
            <div class="friend-wrap">
                <img src="../../public/images/brains/img001.png" alt="" class="w-32 h-32 shadow-lg rounded-full">
                <p class="text-center">フレンド名前</p>
            </div>
            <div class="friend-wrap">
                <img src="../../public/images/brains/img001.png" alt="" class="w-32 h-32 shadow-lg rounded-full">
                <p class="text-center">フレンド名前</p>
            </div>
        </div>
    </div>
</template>

<script  lang="ts">
import {defineComponent} from "vue"
export default defineComponent({
  name:"ShareSelect",
  props:{
    SelectBrains:{
      type:Array,
      default:[]
    }
  }
})
</script>

<style scoped>

</style>
