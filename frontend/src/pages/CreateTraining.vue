<template>
  <v-app>
    <v-container>
      <v-row justify="center">
        <v-col cols="12" md="8">
          <h1 class="text-center">Création d'un programme sportif</h1>
          <v-divider class="mb-4"></v-divider>

          <v-card outlined class="mb-4">
            <v-card-title>Titre du programme</v-card-title>
            <v-card-text>
              <v-text-field v-model="title" label="Titre"></v-text-field>
            </v-card-text>
          </v-card>
          <v-card outlined class="mb-4">
            <v-card-title>Thème</v-card-title>
            <v-card-text>
              <v-radio-group v-model="pickedTheme" @change="fetchExercises(pickedTheme)">
                <v-radio
                  v-for="category in categories"
                  :key="category.id"
                  :label="category.name"
                  :value="category.id"
                ></v-radio>
              </v-radio-group>
            </v-card-text>
          </v-card>

          <v-card outlined class="mb-4">
            <v-card-title>Objectif</v-card-title>
            <v-card-text>
              <v-radio-group v-model="pickedGoal">
                <v-radio
                  v-for="goal in goals"
                  :key="goal.id"
                  :label="goal.name"
                  :value="goal.id"
                ></v-radio>
              </v-radio-group>
            </v-card-text>
          </v-card>

          <v-card outlined class="mb-4">
            <v-card-title>Difficulté</v-card-title>
            <v-card-text>
              <v-radio-group v-model="difficulty">
                <v-radio label="Facile" value="Facile"></v-radio>
                <v-radio label="Intermédiaire" value="Intermédiaire"></v-radio>
                <v-radio label="Difficile" value="Difficile"></v-radio>
              </v-radio-group>
            </v-card-text>
          </v-card>

          <v-card outlined v-if="pickedTheme" class="mb-4">
            <v-card-title>Exercices</v-card-title>
            <v-card-text>
              <v-list lines="ones">
                <v-list-item
                  v-for="exercise in exercises"
                  :key="exercise.id"
                  class="exercise-item"
                  density="compact"
                >
                  <v-checkbox
                    :label="exercise.name"
                    :value="exercise.id"
                    v-model="selectedExercises"
                    density="compact"
                  ></v-checkbox>
                </v-list-item>
              </v-list>
            </v-card-text>
          </v-card>
          <v-card outlined class="mb-4">
            <v-card-title>Description</v-card-title>
            <v-card-text>
              <v-textarea v-model="description" label="Description du programme"></v-textarea>
            </v-card-text>
          </v-card>

          <v-btn color="primary" block @click="handleSubmit">
            Soumettre
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import { postTraining } from "../api/trainings.js";
import { getCategories } from "../api/category.js";
import { getGoals } from "../api/goal.js";
import { getExercisesByCategory } from "../api/exercises.js";

export default {
  data() {
    return {
      title: '',
      pickedTheme: null,
      pickedGoal: null,
      difficulty: null,
      goals: [],
      description: '', 
      categories: [],
      exercises: [],
      selectedExercises: [],
    };
  },
  methods: {
    async fetchCategories() {
      this.categories = await getCategories();
    },
    async fetchGoals() {
      this.goals = await getGoals();
    },
    async fetchExercises(categoryId) {
      this.exercises = await getExercisesByCategory(categoryId);
    },
    async handleSubmit() {
      const payload = {
        title: this.title,
        category_id: this.pickedTheme,
        goal_id: this.pickedGoal,
        difficulty: this.difficulty,
        description: this.description,
        exercises: this.selectedExercises,
      };

      await postTraining(payload);
      this.snackbar = true;
      this.resetForm();

    },
    resetForm() {
      this.title = "";
      this.pickedTheme = null;
      this.pickedGoal = null;
      this.difficulty = null;
      this.description = "";
      this.selectedExercises = [];
    },
  },
  mounted() {
    this.fetchGoals();
    this.fetchCategories();
  },
};
</script>

<style scoped>
.text-center {
  text-align: center;
}
.exercise-item {
  margin: 0;
  padding: 5px 0;
  display: flex;
  align-items: center;
}
</style>
