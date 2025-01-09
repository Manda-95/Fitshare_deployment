import http from "@/utils/http";

export const getTrainings = async () => {
  try {
    const response = await http.get("/trainings/");
    return response.data;
  } catch (error) {
    console.error("Erreur lors de la récupération des programmes :", error.response || error);
    throw new Error(
      error.response?.data?.detail || "Une erreur s'est produite lors de la récupération des programmes."
    );
  }
}

export const getTrainingDetails = async (trainingId) => {
  try{
    const response = await http.get(`/trainings/${trainingId}`);
    return response.data;
  }catch (error) {
    console.error("Erreur lors de la récupération du programme :", error.response || error);
  }
};

export const postTraining = async (trainingData) => {
  if (!trainingData.title || !trainingData.goal_id || !trainingData.category_id || !trainingData.difficulty) {
    throw new Error("Certains champs requis sont manquants.");
  }

  try {
    const response = await http.post("/trainings/", trainingData);
    return response.data;
  } catch (error) {
    console.error("Erreur lors de la création du programme :", error.response || error);
    throw new Error(
      error.response?.data?.detail || "Une erreur s'est produite lors de la création du programme."
    );
  }
};