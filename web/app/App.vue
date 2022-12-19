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
    /*仮でヘッダーの大きさを15％に指定。*/
    width: 85%;
    margin-left: 15%;
  }
</style>
