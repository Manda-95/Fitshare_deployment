<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-app-bar-title>FitShare</v-app-bar-title>
      <v-spacer></v-spacer>

      <div v-if="!isSmallScreen" class="d-flex">
        <v-btn text color="white" @click="navigateTo('TrainingFeed')">Liste des Trainings</v-btn>
        <v-btn text color="white" @click="navigateTo('CreateTraining')">Créer un Training</v-btn>
        <v-btn text color="white" @click="navigateTo('EventCalendar')">Planning</v-btn>
      </div>

      <v-menu
        v-model="menu"
        offset-y
        right
      >
        <template #activator="{ props }">
          <v-avatar
            v-bind="props"
            class="cursor-pointer"
            color="grey darken-3"
          >
            <v-icon>{{ isAuthenticated ? "mdi-account-circle" : "mdi-account" }}</v-icon>
          </v-avatar>
        </template>

        <v-list>
          <v-list-item v-if="isAuthenticated" @click="logout">
            <v-list-item-title>Déconnexion</v-list-item-title>
          </v-list-item>
          <v-list-item v-else @click="navigateTo('Login')">
            <v-list-item-title>Connexion</v-list-item-title>
          </v-list-item>
          <v-list-item v-if="!isAuthenticated" @click="navigateTo('Register')">
            <v-list-item-title>S'inscrire</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>

    <v-main>
      <v-container>
        <router-view></router-view>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import { useAuthStore } from "@/store/auth";

export default {
  name: "App",
  data() {
    return {
      menu: false,
      isSmallScreen: false,
    };
  },
  computed: {
    isAuthenticated() {
      const authStore = useAuthStore();
      return authStore.token !== null;
    },
  },
  methods: {
    navigateTo(routeName) {
      this.$router.push({ name: routeName });
      this.menu = false;
    },
    logout() {
      const authStore = useAuthStore();
      authStore.logout();
      this.menu = false;
    },
    updateScreenSize() {
      this.isSmallScreen = window.innerWidth < 960;
    },
  },
  mounted() {
    this.updateScreenSize();
    window.addEventListener("resize", this.updateScreenSize);
  },
  beforeUnmount() {
    window.removeEventListener("resize", this.updateScreenSize);
  },
};
</script>

<style scoped>
.v-app-bar-title {
  font-weight: bold;
  font-size: 24px;
}

.cursor-pointer {
  cursor: pointer;
}
</style>
