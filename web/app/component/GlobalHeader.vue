<template>
  <header>
    <div class="logo-area">
      <img src="../public/images/logo.png" alt="logo image" id="header-logo" >
    </div>
    <div class="link-area">
      
    </div>
    <div class="notice-area">

    </div>
  </header>
</template>

<script lang="ts">

export default {
  name:"GlobalHeader",
  components: {HeaderLink}
}
</script>

<style scoped>
  header{
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
  .logo-area{
    height: 33%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  #header-logo{
    width: 80px;
  }

  .link-area{
    width: 100%;
    height: 50%;
  }
  .notice-area{
    width: 100%;
    height: 17%;
  }
</style>