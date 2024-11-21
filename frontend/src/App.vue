<template>
  <div id="app">
    <h1>Création d'un programme sportif</h1>
    <hr />
    <div class="split-container">
      <div class="left-panel">
        <p><strong>Thème :</strong></p>
        <input 
          type="radio" 
          id="musculation" 
          name="activity" 
          value="Musculation" 
          v-model="pickedTheme" 
          @change="fetchExercises(3)"
        />
        <label for="musculation">Musculation</label>
        <br>
        <input 
          type="radio" 
          id="athlétisme" 
          name="activity" 
          value="Athlétisme" 
          v-model="pickedTheme" 
          @change="fetchExercises(1)"
        />
        <label for="athlétisme">Athlétisme</label>
        <br>
        <input 
          type="radio" 
          id="natation" 
          name="activity" 
          value="Natation" 
          v-model="pickedTheme" 
          @change="fetchExercises(2)"
        />
        <label for="natation">Natation</label>

        <div>
          <p><strong>Objectif :</strong></p>
          <div v-for="goal in goals" :key="goal.name">
            <input
              type="radio"
              :id="goal.name"
              name="goal"
              :value="goal.name"
              v-model="pickedGoal"
            />
            <label :for="goal.name">{{ goal.name }}</label>
          </div>
        </div>

        <p><strong>Difficulté :</strong></p>
        <div>
          <input 
            type="radio" 
            id="difficulty-1" 
            name="difficulty" 
            value="1" 
            v-model="difficulty"
          />
          <label for="difficulty-1">★</label>
          <input 
            type="radio" 
            id="difficulty-2" 
            name="difficulty" 
            value="2" 
            v-model="difficulty"
          />
          <label for="difficulty-2">★★</label>
          <input 
            type="radio" 
            id="difficulty-3" 
            name="difficulty" 
            value="3" 
            v-model="difficulty"
          />
          <label for="difficulty-3">★★★</label>
          <input 
            type="radio" 
            id="difficulty-4" 
            name="difficulty" 
            value="4" 
            v-model="difficulty"
          />
          <label for="difficulty-4">★★★★</label>
          <input 
            type="radio" 
            id="difficulty-5" 
            name="difficulty" 
            value="5" 
            v-model="difficulty"
          />
          <label for="difficulty-5">★★★★★</label>
        </div>

        <div v-if="pickedTheme" class="exercises">
          <p><strong>Exercices :</strong></p>
          <ul>
            <li v-for="exercise in exercises" :key="exercise.name">
              <input 
                type="checkbox" 
                :id="exercise.name" 
                :value="exercise.name" 
                v-model="selectedExercises"
              />
              <label :for="exercise.name">{{ exercise.name }}</label>

              <span v-if="selectedExercises.includes(exercise.name)">
                :
                <input 
                  type="number" 
                  min="1" 
                  placeholder="Série" 
                  v-model="series[exercise.name]" 
                  class="serie-input"
                /> série(s) de
                <input 
                  type="number" 
                  min="1" 
                  placeholder="Répétition" 
                  v-model="repetitions[exercise.name]" 
                  class="reps-input"
                />
                répétition(s)
              </span>
            </li>

            <li v-for="(customExercise, index) in customExercises" :key="'custom-' + index">
              <input 
                type="text" 
                placeholder="Nom de l'exercice" 
                v-model="customExercise.name"
              />
              :
              <input 
                type="number" 
                min="1" 
                placeholder="Série" 
                v-model="customExercise.series" 
                class="serie-input"
              /> série(s) de
              <input 
                type="number" 
                min="1" 
                placeholder="Répétition" 
                v-model="customExercise.repetitions" 
                class="reps-input"
              />
              répétition(s)
            </li>
          </ul>
          <button @click="addCustomExercise" class="add-exercise-button">Ajouter un exercice</button>
        </div>
      </div>

      <div class="right-panel">
        <p><strong>Thème :</strong></p>
        <p>{{ pickedTheme || "Aucun thème sélectionné" }}</p>
        <p><strong>Objectif :</strong></p>
        <p>{{ pickedGoal || "Aucun objectif sélectionné" }}</p>
        <p><strong>Difficulté :</strong></p>
        <p>{{ difficulty || "Aucune difficulté sélectionnée" }}</p>
        <p><strong>Exercices sélectionnés :</strong></p>
        
        <ul>
          <li v-for="exercise in selectedExercises" :key="exercise">
            {{ exercise }} - 
            {{ series[exercise] || '0' }} série(s) de 
            {{ repetitions[exercise] || '0' }} répétition(s)
          </li>
          <li v-for="(customExercise, index) in customExercises" :key="'custom-right-' + index">
            {{ customExercise.name || 'Exercice personnalisé' }} - 
            {{ customExercise.series || '0' }} série(s) de 
            {{ customExercise.repetitions || '0' }} répétition(s)
          </li>
        </ul>
      </div>
    </div>
    <!-- Bouton "Soumettre" en bas de page -->
    <div class="submit-container">
      <button class="submit-button" @click="handleSubmit">Soumettre</button>
    </div>
  </div>
</template>

<script>
import appConfig from './app.js';

export default {
  ...appConfig,
  data() {
    return {
      ...appConfig.data(),
      goals: [],
      exercises: [],
      selectedExercises: [],
      series: {},
      repetitions: {},
      customExercises: [],
      difficulty: null,
      pickedTheme: null,
      pickedGoal: null,

    };
  },
  methods: {
    ...appConfig.methods,
    async fetchGoals() {
      try {
        const response = await fetch("http://localhost:8000/goal/");
        const data = await response.json();
        this.goals = data;
      } catch (error) {
        console.error("Erreur lors de la récupération des objectifs :", error);
      }
    },
    async handleSubmit() {
      const payload = {
        title: "Programme sportif personnalisé",
        theme: this.pickedTheme,
        goal: this.pickedGoal,
        difficulty: this.difficulty,
        exercises: this.selectedExercises.map(exercise => ({
          name: exercise,
          series: this.series[exercise] || 0,
          repetitions: this.repetitions[exercise] || 0,
        })),
      };

      try {
        const response = await fetch("http://localhost:8000/trainings/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(payload),
        });

        if (!response.ok) {
          throw new Error("Erreur lors de l'envoi des données !");
        }

        const data = await response.json();
        alert("Programme créé avec succès !");
      } catch (error) {
        console.error("Erreur :", error);
        alert("Une erreur s'est produite lors de la création du programme.");
      }
    },
  },
  mounted() {
    this.fetchGoals();
  },
};

</script>
