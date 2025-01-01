import { createRouter, createWebHistory } from "vue-router";
import Login from "@/pages/Login.vue";
import Register from "@/pages/Register.vue";
import CreateTraining from "@/pages/CreateTraining.vue";
import TrainingFeed from "@/pages/TrainingFeed.vue";
import CalendarView from "@/pages/CalendarView.vue";
import { useAuthStore } from "@/store/auth";

const routes = [
  {
    path: "/",
    redirect: "/training",
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
  },
  {
    path: "/training",
    name: "TrainingFeed",
    component: TrainingFeed,
  },
  {
    path: "/training/create",
    name: "CreateTraining",
    component: CreateTraining,
    meta: { requiresAuth: true },
  },
  {
    path: "/event/",
    name: "EventCalendar",
    component: CalendarView,
    meta: { requiresAuth: true },
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();
  if (to.meta.requiresAuth && !authStore.isAuthenticated()) {
    next({
      name: "Login",
      query: { redirect: to.fullPath },
    });
  } else {
    next();
  }
});

export default router;
