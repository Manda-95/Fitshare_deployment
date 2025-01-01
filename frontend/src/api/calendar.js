import http from "@/utils/http";

export const addEventToCalendar = async (eventData) => {
  const response = await http.post("/events/", eventData);
  return response.data;
};
