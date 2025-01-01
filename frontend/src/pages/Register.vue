<template>
    <div class="register-page">
      <div class="register-container">
        <h1>Créer un compte</h1>
        <form @submit.prevent="handleRegister">
          <div class="form-group">
            <label for="username">Nom d'utilisateur</label>
            <input
              type="text"
              id="username"
              v-model="formData.username"
              placeholder="Entrez votre nom d'utilisateur"
              required
            />
          </div>
          <div class="form-group">
            <label for="email">Email</label>
            <input
              type="email"
              id="email"
              v-model="formData.email"
              placeholder="Entrez votre email"
              required
            />
          </div>
          <div class="form-group">
            <label for="password">Mot de passe</label>
            <input
              type="password"
              id="password"
              v-model="formData.password"
              placeholder="Entrez votre mot de passe"
              required
            />
          </div>
          <div class="form-group">
            <label for="confirm-password">Confirmer le mot de passe</label>
            <input
              type="password"
              id="confirm-password"
              v-model="formData.confirmPassword"
              placeholder="Confirmez votre mot de passe"
              required
            />
          </div>
          <button type="submit" class="btn">S'inscrire</button>
          <p class="login-link">
            Vous avez déjà un compte ?
            <router-link to="/login">Connectez-vous ici</router-link>
          </p>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  import { register } from "@/api/auth";
  
  export default {
    name: "Register",
    data() {
      return {
        formData: {
          username: "",
          email: "",
          password: "",
          confirmPassword: "",
        },
      };
    },
    methods: {
      async handleRegister() {
        if (this.formData.password !== this.formData.confirmPassword) {
          alert("Les mots de passe ne correspondent pas.");
          return;
        }
  
        await register({
          username: this.formData.username,
          email: this.formData.email,
          password: this.formData.password,
        });
        alert("Inscription réussie ! Vous pouvez maintenant vous connecter.");
        this.$router.push("/login");
      },
    },
  };
  </script>
  
  <style scoped>
  .register-page {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background-color: #f4f4f4;
  }
  
  .register-container {
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
  
  .login-link {
    margin-top: 1rem;
    font-size: 0.9rem;
  }
  
  .login-link a {
    color: #007bff;
    text-decoration: none;
  }
  
  .login-link a:hover {
    text-decoration: underline;
  }
  </style>
  