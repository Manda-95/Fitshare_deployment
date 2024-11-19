<template>
  <div id="app">
    <h1>Création d'un programme sportif</h1>
    <hr />
    <div class="split-container">
      
      <div class="left-panel">
        <p><strong>Theme :</strong></p>
        <input type="radio" id="musculation" name="activity" value="Musculation" v-model="picked" @change="fetchExercises(3)">
        <label for="musculation">Musculation</label>
        <br>
        <input type="radio" id="athlétisme" name="activity" value="Athlétisme" v-model="picked" @change="fetchExercises(1)">
        <label for="athlétisme">Athlétisme</label>
        <br>
        <input type="radio" id="natation" name="activity" value="Natation" v-model="picked" @change="fetchExercises(2)">
        <label for="natation">Natation</label>

        <div v-if="picked === 'Musculation'" class="exercises">
          <p><strong>Exercices :</strong></p>
          <ul>
            <li v-for="exercise in exercises" :key="exercise.name">{{ exercise.name }}</li>
          </ul>
        </div>

        <div v-if="picked === 'Athlétisme'" class="exercises">
          <p><strong>Exercices :</strong></p>
          <ul>
            <li v-for="exercise in exercises" :key="exercise.name">{{ exercise.name }}</li>
          </ul>
        </div>

        <div v-if="picked === 'Natation'" class="exercises">
          <p><strong>Exercices :</strong></p>
          <ul>
            <li v-for="exercise in exercises" :key="exercise.name">{{ exercise.name }}</li>
          </ul>
        </div>

      </div>

      <div class="right-panel">
        <p><strong>Theme :</strong></p>
        <p>{{ picked || "Aucune activité sélectionnée" }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      picked: "", 
      exercises: [], 
    };
  },
  methods: {
    async fetchExercises(categoryId) {
      try {
        const response = await fetch(`http://localhost:8000/exercises/category/${categoryId}`);
        if (response.ok) {
          this.exercises = await response.json();
        } else {
          console.error("Erreur lors de la récupération des exercices.");
        }
      } catch (error) {
        console.error("Erreur réseau :", error);
      }
    },
  },
};
</script>
