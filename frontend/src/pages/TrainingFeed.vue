<template>
  <v-app>
    <v-container>
      <v-row>
        <v-col cols="12">
          <h1 class="text-center">Liste des Trainings</h1>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12">
          <v-text-field
            v-model="searchQuery"
            label="Rechercher un entraînement"
            outlined
            clearable
          ></v-text-field>
        </v-col>
      </v-row>

      <v-row>
        <v-col cols="12" v-for="training in filteredTrainings" :key="training.id">
          <v-card>
            <v-card-title class="card-header">
              {{ training.title }}
              <v-spacer></v-spacer>
              <v-btn icon color="primary" @click="openAddToCalendar(training)">
                <v-icon>mdi-calendar-plus</v-icon>
              </v-btn>
            </v-card-title>

            <v-card-subtitle>
              <v-chip>{{ training.category }}</v-chip>
              <v-chip>{{ training.difficulty }}</v-chip>
            </v-card-subtitle>

            <v-card-text>
              <p><strong>Objectif :</strong> {{ training.goal }}</p>
              <p><strong>Exercices :</strong></p>
              <ul>
                <li v-for="exercise in training.exercises" :key="exercise.id">
                  {{ exercise.name }}
                </li>
              </ul>

              <p v-if="training.showDetails" class="description">
                <strong>Description :</strong> {{ training.description }}
              </p>
            </v-card-text>

            <v-card-actions>
              <v-btn color="primary" text @click="training.showDetails = !training.showDetails">
                {{ training.showDetails ? 'Masquer les détails' : 'Voir les détails' }}
              </v-btn>
              <v-spacer></v-spacer>
              <v-btn text color="secondary" @click="training.showComments = !training.showComments">
                {{ training.showComments ? "Masquer" : `${training.comments.length} commentaires` }}
              </v-btn>
            </v-card-actions>

            <v-card-text v-if="training.showComments" class="comments-section">
              <p v-if="training.comments.length === 0">Aucun commentaire pour cet entraînement.</p>
              <v-divider v-else></v-divider>
              <div v-for="comment in training.comments" :key="comment.id" class="comment">
                <p><strong>{{ comment.author.username }}</strong> - {{ new Date(comment.created_at).toLocaleString() }}</p>
                <p>{{ comment.content }}</p>
                <v-divider></v-divider>
              </div>

              <div v-if="isAuthenticated" class="add-comment">
                <v-textarea
                  v-model="newComments[training.id]"
                  placeholder="Écrire un commentaire..."
                  rows="3"
                  outlined
                ></v-textarea>
                <v-btn color="primary" @click="submitComment(training.id)">Envoyer</v-btn>
              </div>
              <p v-else>Connectez-vous pour écrire un commentaire.</p>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>

      <v-dialog v-model="calendarModal.visible" max-width="500px">
        <v-card>
          <v-card-title>Ajouter au planning</v-card-title>
          <v-card-text>
            <p>Training : <strong>{{ calendarModal.training.title }}</strong></p>
            <v-text-field
              v-model="calendarModal.startTime"
              label="Heure de début (YYYY-MM-DD HH:mm)"
              type="datetime-local"
              required
            ></v-text-field>
            <v-text-field
              v-model="calendarModal.endTime"
              label="Heure de fin (YYYY-MM-DD HH:mm)"
              type="datetime-local"
              required
            ></v-text-field>
          </v-card-text>
          <v-card-actions>
            <v-btn text @click="calendarModal.visible = false">Annuler</v-btn>
            <v-btn color="primary" @click="addToCalendar">Ajouter</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-container>
  </v-app>
</template>


<script>
import { postComment } from "@/api/comments";
import { addEventToCalendar } from "@/api/calendar";
import { useAuthStore } from "@/store/auth";
import { getTrainings } from "@/api/trainings";

export default {
  data() {
    return {
      trainings: [],
      newComments: {},
      calendarModal: {
        visible: false,
        training: null,
        startTime: "",
        endTime: "",
      },
      searchQuery: "",
    };
  },
  computed: {
    isAuthenticated() {
      const authStore = useAuthStore();
      return authStore.token !== null;
    },
    filteredTrainings() {
      return this.trainings.filter((training) =>
        training.title.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    },
  },
  methods: {
    
    async submitComment(trainingId) {
      const content = this.newComments[trainingId]; 
      
      if (!content || !content.trim()) {
        alert("Le commentaire ne peut pas être vide.");
        return;
      }

      const newComment = await postComment(trainingId, content);
      const training = this.trainings.find((t) => t.id === trainingId);
      if (!training) {
        console.error(`Training avec ID ${trainingId} introuvable.`);
        return;
      }

      training.comments.push(newComment);

      this.newComments[trainingId] = "";

      if (!training.showComments) {
        training.showComments = true;
      }
    },

    async fetchTrainings() {
        const data = await getTrainings();
        this.trainings = data.map((training) => ({
          ...training,
          showDetails: false,
          showComments: false,
        }));
        this.trainings.forEach((training) => {
          this.$set(this.newComments, training.id, "");
        });
    },

    openAddToCalendar(training) {
      this.calendarModal.training = training;
      this.calendarModal.visible = true;
    },

    async addToCalendar() {
      const { training, startTime, endTime } = this.calendarModal;

      if (!startTime || !endTime) {
        alert("Veuillez renseigner les dates et heures.");
        return;
      }

      try {
        await addEventToCalendar({
          title: training.title,
          training_id: training.id,
          start_time: startTime,
          end_time: endTime,
        });

        alert("Training ajouté au planning !");
        this.calendarModal.visible = false;
      } catch (error) {
        console.error("Erreur lors de l'ajout au planning :", error);
        alert("Une erreur s'est produite lors de l'ajout au planning.");
      }
    },
  },
  mounted() {
    this.fetchTrainings();
  },
};
</script>

<style scoped>
.card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
ul{
  list-style-type: none;
}

</style>
