<template>
  <div class="status-wrapper">
    <div class="status-info mt-24">
      <Status />
    </div>
    <div class="status-list mt-16 w-10/12 mx-auto flex gap-6">
      <img src="../../public/images/img001.png" alt="" class="w-28 h-28 shadow-lg" >
      <img src="../../public/images/img001.png" alt="" class="w-28 h-28 shadow-lg" >
      <img src="../../public/images/img001.png" alt="" class="w-28 h-28 shadow-lg" >
      <img src="../../public/images/img001.png" alt="" class="w-28 h-28 shadow-lg" >
      <img src="../../public/images/img001.png" alt="" class="w-28 h-28 shadow-lg" >
      <img src="../../public/images/img001.png" alt="" class="w-28 h-28 shadow-lg" >
      <img src="../../public/images/img001.png" alt="" class="w-28 h-28 shadow-lg" >
      <img src="../../public/images/img001.png" alt="" class="w-28 h-28 shadow-lg" >
      <img src="../../public/images/img001.png" alt="" class="w-28 h-28 shadow-lg" >
      <img src="../../public/images/img001.png" alt="" class="w-28 h-28 shadow-lg" >
    </div>
  </div>
</template>

<script>
  import Status from '../../component/brain/statusMain.vue'; 
  export default {
    name:'status',
    components: {
      Status
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
