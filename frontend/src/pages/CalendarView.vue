<template>
  <v-app>
    <v-container>
      <h1>Mon Planning</h1>
      <FullCalendar :options="calendarOptions" />
    </v-container>

    <v-dialog v-model="dialog.visible" max-width="500px">
      <v-card>
        <v-card-title>{{ dialog.title }}</v-card-title>
        <v-card-text>
          <p><strong>Description :</strong> {{ dialog.description }}</p>
          <p><strong>Exercices :</strong></p>
          <ul>
            <li v-for="exercise in dialog.exercises" :key="exercise.id">
              {{ exercise.name }}
            </li>
          </ul>
        </v-card-text>
        <v-card-actions>
          <v-btn text @click="dialog.visible = false">Fermer</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-app>
</template>

<script>
import FullCalendar from "@fullcalendar/vue3";
import dayGridPlugin from "@fullcalendar/daygrid";
import timeGridPlugin from "@fullcalendar/timegrid";
import interactionPlugin from "@fullcalendar/interaction";
import { getEvents } from "@/api/events";
import { getTrainingDetails } from "@/api/trainings";

export default {
  components: {
    FullCalendar,
  },
  data() {
    return {
      calendarOptions: {
        plugins: [dayGridPlugin, timeGridPlugin, interactionPlugin],
        initialView: "dayGridMonth",
        events: [],
        eventClick: this.handleEventClick,
      },
      dialog: {
        visible: false,
        title: "",
        description: "",
        exercises: [],
      },
    };
  },
  methods: {
    async fetchEvents() {
      const response = await getEvents();
      this.calendarOptions.events = response.map((event) => ({
        id: event.training_id,
        title: event.title,
        start: event.start_time,
        end: event.end_time,
      }));
    },
    async handleEventClick(info) {

    const trainingId = info.event.id;
    const trainingDetails = await getTrainingDetails(trainingId);
    this.dialog.title = trainingDetails.title;
    this.dialog.description = trainingDetails.description;
    this.dialog.exercises = trainingDetails.exercises;
    this.dialog.visible = true;
    },
  },
  mounted() {
    this.fetchEvents();
  },
};
</script>

<style scoped>
.v-container {
  margin-top: 20px;
}

ul{
  list-style-type: none;
}
</style>
