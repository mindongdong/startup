import axios from "axios";

const instance = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

function getMatchInfo(match) {
  return instance.post("/routes/matches/info", match);
}

export { getMatchInfo };
