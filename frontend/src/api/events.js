import http from "@/utils/http";

export const getEvents = async () => {
  try{
    const response = await http.get("/events/");
    return response.data;
  } catch (error) {
    console.error("Erreur lors de la récupération des événements :", error);
  }
};

export const createEvent = async (event) => {
  const response = await http.post("/events/", event);
  return response.data;
};
