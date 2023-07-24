<template>
  <div class="layout">
    <header class="option">
      <h1 class="option__description">선수</h1>
      <div class="dropdown">
        <select v-model="selectedPlayer">
          <option disabled value="">Select</option>
          <option disabled value="">{{ home_teamName }}</option>
          <option v-for="player in home_lineup" :key="player">
            {{ player }}
          </option>
          <option disabled value="">{{ away_teamName }}</option>
          <option v-for="player in away_lineup" :key="player">
            {{ player }}
          </option>
        </select>
      </div>
      <h1 class="option__description">기록</h1>
      <div class="dropdown">
        <select v-model="selectedRecord">
          <option disabled value="">Select</option>
          <option v-for="record in Object.keys(this.recordDict)" :key="record">
            {{ record }}
          </option>
        </select>
      </div>
    </header>
    <main class="rankTable"></main>
  </div>
</template>

<script>
import { getMatchLineup, getGroupStats } from "@/api/index.js";
export default {
  name: "PlayerStats",
  data() {
    return {
      selectedPlayer: "",
      selectedRecord: "",
      groupStats: [],
      home_teamName: "",
      away_teamName: "",
      home_lineup: [],
      away_lineup: [],
      recordDict: {
        득점: "goals",
        도움: "assists",
        자책골: "own_goals",
        슛: "total_shots",
        "유효 슛": "shots_on_target",
        파울: "fouls",
        오프사이드: "offsides",
        "옐로 카드": "yellow_cards",
        "레드 카드": "red_cards",
        "패스 횟수": "total_passes",
        "패스 성공률": "pass_accuracy",
      },
    };
  },
  methods: {
    async getGroupStats() {
      const response = await getGroupStats();
      this.groupStats = response.data;
    },
  },
  async mounted() {
    const lineup = await getMatchLineup(this.$store.getters.getCurrentTime);
    console.log(lineup.data);
    const team_list = Object.keys(lineup.data);
    this.home_teamName = team_list[0];
    this.away_teamName = team_list[1];
    this.home_lineup = lineup.data[team_list[0]];
    this.away_lineup = lineup.data[team_list[1]];
  },
};
</script>

<style scoped>
.layout {
  width: 100%;
  height: 100%;
}
.option {
  background-color: black;
  padding: 20px;
  display: flex;
  align-items: center;
}

.option__description {
  color: white;
  font-size: 0.9rem;
  margin-right: 0.5rem;
}

.dropdown {
  position: relative;
  display: inline-block;
  margin-right: 20px;
}

.dropdown select {
  background-color: transparent;
  color: white;
  padding: 10px;
  border: 1px solid white;
  border-radius: 5px;
  font-size: 0.9rem;
  appearance: none; /* this will remove the default arrow in some browsers */
  width: 100px;
  outline: none;
}

.dropdown::after {
  /* create a custom dropdown arrow */
  content: "⌄";
  font-size: 10px;
  position: absolute;
  right: 10px;
  top: 15px;
  color: white;
}
</style>
