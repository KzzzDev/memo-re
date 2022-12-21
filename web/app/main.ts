import {createApp} from "vue";

import App from "./App.vue";

import {i18n, router, memoRe} from "./plugin";
import "./index.css"

import {library} from "@fortawesome/fontawesome-svg-core";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome"
import {faUser, faPenToSquare} from "@fortawesome/free-regular-svg-icons";
import {
    faArrowUpFromBracket,
    faUserGroup,
    faMagnifyingGlass,
    faCircleInfo,
    faBell,
    faRightFromBracket
} from "@fortawesome/free-solid-svg-icons";

library.add(faUser, faPenToSquare, faArrowUpFromBracket, faUserGroup, faMagnifyingGlass, faCircleInfo, faBell, faRightFromBracket)


createApp(App)
    .component('font-awesome-icon', FontAwesomeIcon)
    .use(i18n)
    .use(router)
    .use(memoRe)
    .mount("#app");
