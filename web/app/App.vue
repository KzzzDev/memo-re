<template>
  <GlobalHeader/>
  <main>
    <router-view/>
  </main>
</template>

<script lang="ts">
import GlobalHeader from "./component/GlobalHeader/Main.vue";

export default {
  components: {GlobalHeader}
}
</script>

<style>
  main{
    /*仮でヘッダーの大きさを20％に指定。*/
    width: 80%;
    margin-left: 20%;
  }
</style>
