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
<style>
@import "./css/destyle.css";
* {
  font-family:'ヒラギノ角ゴ Pro W3',sans-serif;
}
.flex {
  display: flex;
}
.fixedGlobal {
  width: 170px;
  z-index: 10;
}
.overWrap {
  padding-top: 40px;
}
</style>
