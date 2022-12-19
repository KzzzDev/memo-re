<template>
  <div class="header-link">

    <p>{{ category }}</p>
  </div>
</template>

<script lang="ts" setup>
type Category = "Profile" | "Make" | "Share" | "Search" | "Info"

const props = defineProps<{
  category: Category
}>();

const imagePath = ""

</script>

<style scoped>
.header-link {
  width: 100%;
  height: 30px;
  display: flex;
  justify-content: center;
}

p {
  margin: 0;
  font-size: 16px;
  color: #fff;
}
</style>