<template>
  <div>
    <router-view />
  </div>
</template>

<script>
export default {
  name: "MyPage",
  components: {},
};
</script>

<style scoped>
@import "./css/destyle.css";
</style>
<style>
.flex {
  display: flex;
}
.fixedGlobal {
  width: 170px;
  z-index: 10;
}
</style>
