import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import CreateImage from "../views/CreateImage.vue";
import PreviewImage from "../views/PreviewImage.vue";
import SignUp from "../views/SignUp.vue";
import SignIn from "../views/SignIn.vue";
import MyPage from "../views/MyPage.vue";
import ImageView from "../views/ImageView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/signUp",
    name: "signUp",
    component: SignUp,
  },
  {
    path: "/signIn",
    name: "signIn",
    component: SignIn,
  },
  {
    path: "/myPage",
    name: "myPage",
    component: MyPage,
  },
  {
    path: "/createImage",
    name: "createImage",
    component: CreateImage,
  },
  {
    path: "/previewImage",
    name: "previewImage",
    component: PreviewImage,
  },
  {
    path: "/imageView",
    name: "imageView",
    component: ImageView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
