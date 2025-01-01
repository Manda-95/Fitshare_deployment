import http from "@/utils/http";

export const postComment = async (trainingId, content) => {
  if (!content || !content.trim()) {
    throw new Error("Le contenu du commentaire est vide.");
  }

  try {
    const response = await http.post(`/comments/`, {
      training_id: trainingId,
      content: content.trim(),
    });
    return response.data; // Retourner directement le commentaire créé
  } catch (error) {
    console.error("Erreur lors de l'ajout du commentaire :", error.response || error);
    throw new Error(
      error.response?.data?.detail || "Une erreur s'est produite lors de l'ajout du commentaire."
    );
  }
};
