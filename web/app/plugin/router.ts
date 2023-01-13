import {createRouter, createWebHistory} from "vue-router";
import {getToken} from "../lib/auth";

const router =  createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: "/",
            component: () => import("../views/user/signInView.vue"),
            name: "index"
        },
        {
            path: "/signIn",
            component: () => import("../views/user/signInView.vue"),
            name: "login"
        },
        {
            path: "/signUp",
            component: () => import("../views/user/signUpView.vue"),
            name: "signUp"
        },
        {
            path: "/mypage",
            component: () => import("../views/brain/listView.vue"),
            name: "mypage",
            meta: { requiresAuth: true },

        },
        {
            //
            path: "/brain/:UserId",
            component: () => import("../views/brain/listView.vue"),
            name: "brain list",
            meta: { requiresAuth: true }
        },
        {
            //ノート詳細
            path: "/note/:UserId/:NoteId",
            component: () => import("../views/brain/statusView.vue"),
            name: "brain status",
            meta: { requiresAuth: true }
        },

        {
            path: "/create",
            component: () => import("../views/brain/createView.vue"),
            name: "create view",
            meta: { requiresAuth: true }
        }
    ],
    strict: true,

});

router.beforeEach((to) => {
    console.log(getToken())
    if(to.meta.requiresAuth&& !getToken()){
        return {name:"login"}
    }
})

export default router
