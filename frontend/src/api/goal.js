import http from "@/utils/http";

export const getGoals = async () => {
    try {
        const response = await http.get("/goal");
        return response.data;
      } catch (error) {
        console.error("Erreur lors de la récupération des objectifs :", error);
      }
}