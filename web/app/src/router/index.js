import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import CreateImage from "../views/CreateImage.vue";
import PreviewImage from "../views/PreviewImage.vue";
import SignUp from "../views/SignUp.vue";
import SignIn from "../views/SignIn.vue";
import MyPage from "../views/MyPage.vue";
import ImageView from "../views/ImageView.vue";
import FriendPage from "../views/FriendPage";
import FriendImageView from "../views/FriendImageView.vue";
import ShareDrop from "../views/ShareDrop.vue";
import Produce from "../views/Produce.vue";
import NotFound from "../views/NotFound.vue";
import Error from "../views/Error.vue";
import Timeline from "../views/Timeline.vue";
import TimelineImage from "../views/TimelineImage.vue";
import Update from "../views/Update.vue";

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
  {
    path: "/friendPage/:user?",
    name: "friendPage",
    component: FriendPage,
  },
  {
    path: "/friendImageView",
    name: "friendImageView",
    component: FriendImageView,
  },
  {
    path: "/shareDrop",
    name: "shareDrop",
    component: ShareDrop,
  },
  {
    path: "/produce",
    name: "produce",
    component: Produce,
  },
  {
    path: "/timeline",
    name: "timeline",
    component: Timeline,
  },
  {
    path: "/timelineImage",
    name: "timelineImage",
    component: TimelineImage,
  },
  {
    path: "/update",
    name: "update",
    component: Update,
  },
  {
    path: "/500",
    name: "Error",
    component: Error,
  },
  {
    path: "/404",
    name: "notFound",
    component: NotFound,
  },
  {
    path: "/:catchAll(.*)",
    redirect: "/404",
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
