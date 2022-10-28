import { createI18n } from "vue-i18n";

import ja from "../public/locales/ja.json";

export default createI18n<[typeof ja], "ja">({
  locale: "ja",
  messages: { ja },
  legacy: false,
});
