import { createRouter, createWebHistory } from "vue-router";

export default createRouter({
  history: createWebHistory(),
  routes: [{ path: "/home", redirect: "/" }],
  strict: true,
});
