<template>
  <div class="status-wrapper">
    <div class="status-info">
      <p>a</p>
    </div>
    <div class="status-list">

    </div>
  </div>
</template>

<script>
  export default {
    name:"test",
    mounted() {
      console.log("a")
    }
  }
</script>

<style scoped>
.status-wrapper {
  display: flex;
  flex-direction: column;
}

.status-info {
  height: 75%;
  border-bottom: solid 1px;
}

.status-list {
  height: 25%;
}
</style>
