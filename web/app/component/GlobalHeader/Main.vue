<template>
  <header>
    <div class="logo-area">
      <img src="../../public/images/logo.png" alt="logo image" id="header-logo">
    </div>
    <div class="link-area">
      <header-link link-text="Profile"/>
      <header-link link-text="Make"/>
      <header-link link-text="Friend"/>
      <header-link link-text="Search"/>
      <header-link link-text="Notice"/>
    </div>
    <div class="logout-area">
      <header-link link-text="Logout"/>
    </div>

  </header>
</template>

<script lang="ts">
import HeaderLink from "./Link.vue"

export default {
  name: "GlobalHeader",
  components: {HeaderLink}
}
</script>

<style scoped>
header {
  background: #505058;
  width: 12%;
  height: 100%;
  position: fixed;
  top: 0;
  left: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.logo-area {
  height: 30%;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}


#header-logo {
  width: 80px;
}

.link-area {
  width: 100%;
  height: 50%;
}


.logout-area {
  width: 100%;
  height: 20%;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  position: relative;
}


</style>