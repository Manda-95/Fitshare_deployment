<template>
    <div class="login-page">
      <div class="login-container">
        <h1>Connexion</h1>
        <form @submit.prevent="handleLogin">
          <div class="form-group">
            <label for="username">Nom d'utilisateur</label>
            <input
              type="text"
              id="username"
              v-model="username"
              placeholder="Entrez votre nom d'utilisateur"
              required
            />
          </div>
          <div class="form-group">
            <label for="password">Mot de passe</label>
            <input
              type="password"
              id="password"
              v-model="password"
              placeholder="Entrez votre mot de passe"
              required
            />
          </div>
          <button type="submit" class="btn">Se connecter</button>
          <p class="register-link">
            Pas encore inscrit ?
            <router-link to="/register">Créer un compte</router-link>
          </p>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  import { useAuthStore } from "@/store/auth";
  
  export default {
    name: "Login",
    data() {
      return {
        username: "",
        password: "",
      };
    },
    methods: {
      async handleLogin() {
        try {
          const authStore = useAuthStore();
          await authStore.authenticate(this.username, this.password);
          this.$router.push("/");
        } catch (error) {
            console.error(error);
          alert("Échec de la connexion. Veuillez vérifier vos informations.");
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .login-page {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background-color: #f4f4f4;
  }
  
  .login-container {
    background: white;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    max-width: 400px;
    width: 100%;
    text-align: center;
  }
  
  h1 {
    margin-bottom: 1.5rem;
    font-size: 1.8rem;
    color: #333;
  }
  
  .form-group {
    margin-bottom: 1rem;
    text-align: left;
  }
  
  label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: bold;
    color: #555;
  }
  
  input {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 1rem;
  }
  
  input:focus {
    border-color: #007bff;
    outline: none;
  }
  
  .btn {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 0.75rem 1rem;
    border-radius: 4px;
    font-size: 1rem;
    cursor: pointer;
    width: 100%;
  }
  
  .btn:hover {
    background-color: #0056b3;
  }
  
  .register-link {
    margin-top: 1rem;
    font-size: 0.9rem;
  }
  
  .register-link a {
    color: #007bff;
    text-decoration: none;
  }
  
  .register-link a:hover {
    text-decoration: underline;
  }
  </style>
  