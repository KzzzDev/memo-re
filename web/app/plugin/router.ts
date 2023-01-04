import { createRouter, createWebHistory } from "vue-router";

export default createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: "/",
            component: () => import("../views/user/loginView.vue"),
            name: "login"
        },

        {
            path: "/status",
            component: () => import("../component/brain/statusMain.vue"),
            name: "status"
        },
        {
            path: "/shareImage",
            component: () => import("../component/user/shareImage.vue"),
            name: "shareImage"
        },

        {
            path: "/signUp",
            component: () => import("../views/user/signUpView.vue"),
            name: "signUp"
        },
        {
            path: "/mypage",
            component: () => import("../views/brain/listView.vue"),
            name: "mypage"
        },
        {
            path: "/brain/:UserId",
            component: () => import("../views/brain/listView.vue"),
            name: "brain list"
            // MypageとPathが同じだがcomponent内でRouteを確認し処理を変えるようにしてます。
        },
        {
            path: "/brain/status",
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
