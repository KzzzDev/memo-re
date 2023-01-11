import {createRouter, createWebHistory} from "vue-router";

export default createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: "/",
            component: () => import("../views/user/signInView.vue"),
            name: "login"
        },
        {
            path: "/login",
            component: () => import("../views/user/signInView.vue"),
            name: "login"
        },
        {
            path: "/signUp",
            component: () => import("../views/user/signInView.vue"),
            name: "signUp"
        },
        {
            path: "/mypage",
            component: () => import("../views/brain/listView.vue"),
            name: "mypage"
        },
        {
            //
            path: "/brain/:UserId",
            component: () => import("../views/brain/listView.vue"),
            name: "brain list"
        },
        {
            //ノート詳細
            path: "/note/:UserId/:NoteId",
            component: () => import("../views/brain/statusView.vue"),
            name: "brain status"
        },

        {
            path: "/create",
            component: () => import("../views/brain/createView.vue"),
            name: "create view"
        }
    ],
    strict: true,

});
