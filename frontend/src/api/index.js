import axios from "axios";

const instance = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

const nodeInstance = axios.create({
  baseURL: "http://localhost:3000",
});

function getMatchInfo(match) {
  return instance.post("/routes/matches/info", match);
}

function getAudioStream() {
  return nodeInstance.get("/audio");
}

export {getMatchInfo, getAudioStream};
