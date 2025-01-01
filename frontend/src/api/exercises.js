import http from "@/utils/http";

export const getExercisesByCategory = async (categoryId) => {
    try {
        const response = await http.get(`exercises/category/${categoryId}`
        );
        return response.data;
      } catch (error) {
        console.error("Erreur lors de la récupération des exercices.", error);
    }
}