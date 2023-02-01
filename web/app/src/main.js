import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import VueCookies from "vue-cookies";

let app = createApp(App).use(router).use(VueCookies)
app.mount("#app");

app.config.errorHandler = (err, vm, info) => {
  console.error(`errorHandler: ${info}`, err)
  router.replace({ name: 'Error' })
}
