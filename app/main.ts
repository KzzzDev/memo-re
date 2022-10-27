import { createApp } from "vue";
import { createI18n } from "vue-i18n";

import App from "./App.vue";

import en from "./public/i18n/en/main.json";
import ja from "./public/i18n/ja/main.json";

const i18n = createI18n({
  locale: "ja",
  fallbackFormat: "en",
  messages: { en, ja },
});

createApp(App).use(i18n).mount("#app");
