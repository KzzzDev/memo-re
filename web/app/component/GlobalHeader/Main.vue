<template>
  <header>
    <div class="icon-menu">
      <img src="" alt="logo image" id="header-logo">
    </div>
    <div class="link-menu">
      <header-link  />
    </div>
    <div class="notice-menu">

    </div>
  </header>
</template>

<script lang="ts">
import HeaderLink from "./Link.vue";

export default {
  name:"GlobalHeader",
  components: {HeaderLink}
}
</script>

<style scoped>
  header{
    width: 20%;
    height: 100%;
    position: fixed;
    top: 0;
    left: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
</style>