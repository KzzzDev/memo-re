<template>
  <div class="link-box">
    <div class="icon-box">
      <font-awesome-icon :icon="icon" inverse/>
    </div>
    <div class="link-text-box">
      <p>{{ linkText }}</p>
      <p v-if="noticeCount>0">{{ noticeCount }}</p>
    </div>
  </div>

</template>

<script lang="js">

export default {
  name: "headerLink",
  data() {
    return {
      icon: "",
      linkHref: "",
      noticeCount: 0
    }
  },
  props: {
    linkText: {
      type: String
    }
  },
  mounted() {
    switch (this.linkText) {
      case "Profile":
        this.icon = "fa-regular fa-user"
        this.linkHref = "/mypage"
        break
      case "Make":
        this.icon = "fa-regular fa-pen-to-square"
        this.linkHref = "/create"
        break;
      case "Share":
        this.icon = "fa-solid fa-arrow-up-from-bracket"
        this.linkHref = "/share"
        break;
      case "Friend":
        this.icon = "fa-solid fa-user-group"
        this.linkHref = "/friends"
        break;
      case "Search":
        this.icon = "fa-solid fa-magnifying-glass"
        this.linkHref = "/search"
        break;
      case "Info":
        this.icon = "fa-solid fa-circle-info"
        this.linkHref = "/info"
        break;

      case "Logout":
        this.icon = "fa-solid fa-right-from-bracket"
        this.linkHref = "/logout"
        break;
      case "Notice":
        this.icon = "fa-solid fa-bell"
        this.linkHref = "/notice"
        this.getNoticeCount()
        break;
    }
  },
  methods: {
    getNoticeCount() {
      // API処理
      this.noticeCount = 4
    }
  }
}

</script>

<style scoped>


.link-box {
  width: 100%;
  height: 36px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.icon-box {
  display: flex;
  width: 40%;
  justify-content: flex-end;
}

.link-text-box {
  display: flex;
  width: 60%;
  justify-content: flex-start;
}

.link-text-box p {
  font-size: 18px;
  margin: 0 0 0 16px;
  color: #ffffff;
}
</style>