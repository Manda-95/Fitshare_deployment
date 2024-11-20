<template>
  <div id="app">
    <h1>Création d'un programme sportif</h1>
    <hr />
    <div class="split-container">
      
      <div class="left-panel">
        <p><strong>Theme :</strong></p>
        <input 
          type="radio" 
          id="musculation" 
          name="activity" 
          value="Musculation" 
          v-model="picked" 
          @change="handleThemeChange(3)"
        />
        <label for="musculation">Musculation</label>
        <br>
        <input 
          type="radio" 
          id="athlétisme" 
          name="activity" 
          value="Athlétisme" 
          v-model="picked" 
          @change="handleThemeChange(1)"
        />
        <label for="athlétisme">Athlétisme</label>
        <br>
        <input 
          type="radio" 
          id="natation" 
          name="activity" 
          value="Natation" 
          v-model="picked" 
          @change="handleThemeChange(2)"
        />
        <label for="natation">Natation</label>

        <div v-if="picked" class="exercises">
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
          </ul>
          <ul>
            <li v-for="(customExercise, index) in customExercises" :key="'custom-' + index">
              <input 
                type="text" 
                v-model="customExercise.name" 
                placeholder="Nom de l'exercice"
                class="custom-input"
              />
              :
              <input 
                type="number" 
                min="1" 
                v-model="customExercise.series" 
                placeholder="Nb séries" 
                class="serie-input"
              /> série(s) de
              <input 
                type="number" 
                min="1" 
                v-model="customExercise.repetitions" 
                placeholder="Nb répétitions" 
                class="reps-input"
              />
              répétition(s)
            </li>
          </ul>
          <button @click="addCustomExercise" class="add-exercise-button">Ajouter un exercice</button>
        </div>
      </div>

      <div class="right-panel">
        <p><strong>Theme :</strong></p>
        <p>{{ picked || "Aucune activité sélectionnée" }}</p>
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
  </div>
</template>

<script>
import appConfig from './app.js';

export default {
  ...appConfig,
  data() {
    return {
      ...appConfig.data(),
      series: {},
      repetitions: {},
      customExercises: [], 
    };
  },
  methods: {
    ...appConfig.methods,
    handleThemeChange(categoryId) {
      this.selectedExercises = [];
      this.series = {};
      this.repetitions = {};
      this.customExercises = []; 
      this.fetchExercises(categoryId);
    },
    addCustomExercise() {
      this.customExercises.push({
        name: "",
        series: "",
        repetitions: "",
      });
    },
  },
};
</script>