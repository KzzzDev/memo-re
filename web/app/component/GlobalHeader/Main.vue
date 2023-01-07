<template>
  <header >
    <div class="logo-area">
      <router-link to="/">
        <img src="../../public/images/logo.png" alt="logo image" id="header-logo">
      </router-link>
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
  <div id="modal-area">
    <friend-modal v-if="$store.getters.isFriendModalOpen"/>
    <search-modal v-if="$store.getters.isSearchModalOpen"/>
    <notice-modal v-if="$store.getters.isNoticeModalOpen"/>
  </div>

</template>

<script lang="ts">
import HeaderLink from "./Link.vue"
import FriendModal from "../modal/friend.vue";
import SearchModal from "../modal/search.vue"
import NoticeModal from "../modal/notice.vue"

export default {
  name: "GlobalHeader",
  components: {FriendModal, HeaderLink, SearchModal, NoticeModal}
}
</script>

<style scoped>
header {
  background: #505058;
  width: 15%;
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


#modal-area {
  position: fixed;
  top: 0;
  left: 12%;
  z-index: 2;
}

</style>
