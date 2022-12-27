<template>
   <div class="wrapper w-full">
        <img src="../../public/images/img001.png" alt="" class="w-28 h-28 shadow-lg rounded-full mx-auto" >
        <p class="user-name text-center my-4">たかし</p>
        <div class="img-wrap flex justify-center gap-4">
            <img src="../../public/images/img001.png" alt="" class="w-20 h-20 shadow-lg" >
            <img src="../../public/images/img001.png" alt="" class="w-20 h-20 shadow-lg" >
            <img src="../../public/images/img001.png" alt="" class="w-20 h-20 shadow-lg" >
            <img src="../../public/images/img001.png" alt="" class="w-20 h-20 shadow-lg" >
            <img src="../../public/images/img001.png" alt="" class="w-20 h-20 shadow-lg" >
        </div>
    </div>
</template>
  
  <script lang="js">
  
  export default {
    name: "headerLink",
    data() {
      return {
        icon: "",
        linkHref: "",
        noticeCount: 0
      }
    },
    props: {
      linkText: {
        type: String
      }
    },
  }
  
  </script>
  
  <style scoped>
  
  
  </style>