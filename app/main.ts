import { createApp } from "vue";

import App from "./App.vue";

import { i18n, router } from "./plugin";

createApp(App).use(i18n).use(router).mount("#app");
