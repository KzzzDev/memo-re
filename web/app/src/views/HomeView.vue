<template>
  <div>
    <nav><router-link to="/SignIn">SignIn</router-link> |</nav>
    <div class="home">
      <img alt="Vue logo" src="../assets/logo.png" />
    </div>
    <button @click="Click()">ボタン</button>
    <button @click="Click2()">ボタン</button>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: "HomeView",
  components: {},
  methods: {
    Click() {
      this.$cookies.set("default_unit_second", "input_value", 10);
      console.log(this.$cookies.get("default_unit_second"));
    },
    Click2() {
      console.log(this.$cookies.get("default_unit_second"));
    },
  },
};
</script>
