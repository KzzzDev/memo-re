import { createApp } from "vue";

import App from "./App.vue";

import { i18n } from "./plugin";

createApp(App).use(i18n).mount("#app");
