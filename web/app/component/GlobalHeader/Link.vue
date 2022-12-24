<template>
  <div class="link-box">
    <div class="icon-box">
      <font-awesome-icon :icon="icon" inverse/>
    </div>
    <div class="link-text-box">
      <p @click="linkClick">{{ linkText }}</p>
      <div v-if="noticeCount>0" class="notice"><span>{{ noticeCount }}</span></div>
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
  // Mount時だと空のiconが代入されてエラーがでまくる
  beforeMount() {
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
    },
    linkClick: async function () {

      switch (this.linkText) {
        case "Profile":
          await this.$router.push("/mypage")
          break
        case "Make":
          await this.$router.push("/create")
          break;
        case "Share":
          break;
        case "Friend":
          // friend modal open
          break;
        case "Search":
          // search modal open
          break;
        case "Info":
          // info
          break;

        case "Logout":
          await this.$router.push("/logout")
          break;
        case "Notice":
          // notice modal open
          break;
      }
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

.notice{
  margin-left: 5px;
  width: 20px;
  height: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 50%;
  background: #FC7474;
  color: #ffffff;
}
</style>