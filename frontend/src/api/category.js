import http from "@/utils/http";

export const getCategories = async () => {
    try {
        const response = await http.get("/category/");
        return response.data;
      } catch (error) {
        console.error("Erreur lors de la récupération des catégories :", error);
      }
}