import axios from "axios";

const instance = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

function getTrackingInfo(frame) {
  return instance.get(`/routes/tracking/info/${frame}`);
}

function getMatchLineup(current_time) {
  return instance.get(`/routes/matches/lineup/${current_time}`);
}

function getMatchEvents(Events) {
  return instance.post("/routes/matches/events", Events);
}

function getMatchStats(current_time) {
  return instance.get(`/routes/matches/stats/${current_time}`);
}

function getGroupStats(Player) {
  return instance.post("/routes/matches/group", Player);
}

function getPlayerStats(player_name) {
  return instance.get(`/routes/matches/player/${player_name}`);
}

function getAttackSequence(current_time) {
  return instance.get(`/routes/matches/sequence/${current_time}`);
}

function getMatchShots(current_time) {
  return instance.get(`/routes/matches/shots${current_time}`);
}

function getMatchSetPieces(current_time) {
  return instance.get(`/routes/matches/setpieces${current_time}`);
}

export {
  getTrackingInfo,
  getMatchLineup,
  getMatchEvents,
  getMatchStats,
  getGroupStats,
  getPlayerStats,
  getAttackSequence,
  getMatchShots,
  getMatchSetPieces,
};
