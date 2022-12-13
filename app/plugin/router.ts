import { createRouter, createWebHistory } from "vue-router";

export default createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: "/",
            component: import("../views/user/loginView.vue"),
            name: "login"
        },
        {
            path: "/signUp",
            component: import("../views/user/signUpView.vue"),
            name: "signUp"
        },
        {
            path: "/mypage",
            component: import("../views/user/mypageView.vue"),
            name: "mypage"
        },
        {
            path: "/friends",
            component: import("../views/friend/listView.vue"),
            name: "friend list"
        },
        {
            path: "/brain",
            component: import("../views/brain/listView.vue"),
            name: "brain list"
        },
        {
            path: "/brains/status",
            component: import("../views/brain/statusView.vue"),
            name: "brain status"
        },
        {
            path: "/create",
            component: import("../views/brain/createView.vue"),
            name: "create view"
        }
    ],
    strict: true,

});
