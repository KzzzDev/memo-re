import { createApp } from "vue";

import App from "./App.vue";

import { i18n, router, memoRe } from "./plugin";

createApp(App).use(i18n).use(router).use(memoRe).mount("#app");
