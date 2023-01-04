<template>
  <div class="wrapper w-full flex justify-center mt-20">
    <div class="modal-wrap w-6/12 py-16 border-solid border-2 shadow-md">
      <h1 class="text-4xl text-center mb-12">共有しますか？</h1>
      <div class="wrapper w-full">
        <img src="../../public/images/brains/img001.png" alt="" class="w-28 h-28 shadow-lg rounded-full mx-auto">
        <p class="user-name text-center my-4">たかし</p>
        <div class="img-wrap flex justify-center gap-4">
          <img src="../../public/images/brains/img001.png" alt="" class="w-20 h-20 shadow-lg">
          <img src="../../public/images/brains/img001.png" alt="" class="w-20 h-20 shadow-lg">
          <img src="../../public/images/brains/img001.png" alt="" class="w-20 h-20 shadow-lg">
          <img src="../../public/images/brains/img001.png" alt="" class="w-20 h-20 shadow-lg">
          <img src="../../public/images/brains/img001.png" alt="" class="w-20 h-20 shadow-lg">
        </div>
      </div>
      <div class="button flex justify-center gap-6 mt-12">
        <button class="w-32 bg-gray-400 text-white py-3 rounded-md">キャンセル</button>
        <button class="w-32 bg-red-700 text-white py-3 rounded-md">共有</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name:'shareImage',
  components: {

  }
};
</script>

<style scoped>
.status-list{
  overflow-x: scroll;
}
.status-list img{
  flex-shrink: 0;
}
</style>
