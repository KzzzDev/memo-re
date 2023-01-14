<template>
  <div class="fixed">
    <div class="gl-wrap">
      <div class="gl-global">
        <div class="image"><img src="@/assets/logo.png" alt="ロゴ" /></div>
        <ul>
          <li><router-link to="/MyPage">Profile</router-link></li>
          <li><router-link to="/CreateImage">Create</router-link></li>
          <li @click="GlobalSide(0)" class="pointer">Friend</li>
          <li @click="GlobalSide(1)" class="pointer">Search</li>
          <li @click="GlobalSide(2)" class="pointer">Notice</li>
        </ul>
        <p class="logout pointer" @click="Logout()">Logout</p>
      </div>
      <div class="side" v-if="sideFriend">フレンド</div>
      <div class="side" v-if="sideSearch">検索</div>
      <div class="side" v-if="sideNotice">通知</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "GlobalHeader",
  components: {},
  data() {
    return {
      sideFriend: false,
      sideSearch: false,
      sideNotice: false,
      sideBar: "",
    };
  },
  methods: {
    GlobalSide(num) {
      if (num == 0) {
        this.sideFriend = !this.sideFriend;
        this.sideSearch = false;
        this.sideNotice = false;
      }else if (num == 1) {
        this.sideFriend = false;
        this.sideSearch = !this.sideSearch;
        this.sideNotice = false;
      }else if (num == 2) {
        this.sideFriend = false;
        this.sideSearch = false;
        this.sideNotice = !this.sideNotice;
      }
      return;
    },
    Logout() {
      this.$cookies.remove("access");
      this.$router.push("/SignIn");
      return;
    },
  },
};
</script>
<style scoped>
.fixed {
  position: fixed;
  width: 170px;
}
.gl-wrap {
  position: relative;
  width: 170px;
  height: 100vh;
  background: #515058;
}
.gl-global {
  height: 100%;
  position: relative;
  padding-top: 100px;
  color: #fff;
  font-size: 18px;
}
.gl-global ul {
  margin-top: 80px;
  margin-left: 56px;
}
.gl-global li {
  width:fit-content;
  margin-bottom: 16px;
}
.image {
  width: 80px;
  height: 80px;
  margin: 0 auto;
}
img {
  width: 100%;
}
.gl-global p {
  position: absolute;
  bottom: 100px;
  left: 56px;
}
.side {
  position: absolute;
  top: 0;
  left: 170px;
  z-index: 5;
  width: 260px;
  height: 100vh;
  background: #ccc6c6;
}
.pointer:hover {
  cursor: pointer;
}
</style>
