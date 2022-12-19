<template>
  <GlobalHeader/>
  <main>
    <router-view/>
  </main>
</template>

<script lang="ts">
import GlobalHeader from "./component/GlobalHeader.vue";

export default {
  components: {GlobalHeader}
}
</script>

<style>
  main{
    /*仮でヘッダーの大きさを12％に指定。*/
    width: 88%;
    margin-left: 12%;
  }
</style>
