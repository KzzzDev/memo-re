import { createI18n } from "vue-i18n";

import en from "../public/i18n/en/main.json";
import ja from "../public/i18n/ja/main.json";

export default createI18n({
  locale: "ja",
  fallbackFormat: "en",
  messages: { en, ja },
});
