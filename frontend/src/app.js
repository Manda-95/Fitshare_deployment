export default {
    data() {
      return {
        picked: "", 
        exercises: [], 
        selectedExercises: [], // Tableau pour stocker les exercices sélectionnés
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
  