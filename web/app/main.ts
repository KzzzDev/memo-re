import { createApp } from "vue";

import App from "./App.vue";

import { i18n, router, memoRe } from "./plugin";

import {library} from "@fortawesome/fontawesome-svg-core";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome"
import {faUserSecret} from "@fortawesome/free-solid-svg-icons";

library.add(faUserSecret)


createApp(App)
    .use(i18n)
    .use(router)
    .use(memoRe)
    .component("font-awesome-icon",FontAwesomeIcon)
    .mount("#app");
