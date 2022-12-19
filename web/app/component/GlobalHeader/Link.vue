<template>
  <div class="header-link">
    <img src="" alt="" class="icon">
    <p>{{name}}</p>
  </div>
</template>

<script lang="ts">
  import {defineComponent} from "vue"
  export default defineComponent({
    name:"header-link",

  })
</script>

<style scoped>
.header-link{
  width: 100%;
  display: flex;
  justify-content: center;
}

</style>