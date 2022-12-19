<template>
  <div class="link-box">
    <div class="icon-box">
      <font-awesome-icon :icon="icon" inverse/>
    </div>
    <div class="link-text-box">
      <p>{{ linkText }}</p>
    </div>
  </div>

</template>

<script lang="js">

export default {
  name: "headerLink",
  data() {
    return {
      icon: ""
    }
  },
  props: {
    linkText: {
      type: String
    }
  },
  mounted() {
    switch (this.linkText) {
      case "User":
        this.icon = "fa-regular fa-user"
        break
      case "Make":
        this.icon = "fa-regular fa-pen-to-square"
        break;
      case "Share":
        this.icon = "fa-solid fa-arrow-up-from-bracket"
        break;
      case "Friend":
        this.icon = "fa-solid fa-user-group"
        break;
      case "Search":
        this.icon = "fa-solid fa-magnifying-glass"
        break;
      case "Info":
        this.icon = "fa-solid fa-circle-info"
        break;
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