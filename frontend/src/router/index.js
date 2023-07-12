import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      redirect: "/main",
    },
    {
      path: "/main",
      component: () => import("@/views/MainPage.vue"),
    },
    {
      path: "/viewer",
      component: () => import("@/views/VideoAnalysis"),
    },
    {
      path: "/proViewer",
      component: () => import("@/views/ProViewer"),
    },
    {
      path: "/begginerViewer",
      component: () => import("@/views/BegginerViewer"),
    },
  ],
});
