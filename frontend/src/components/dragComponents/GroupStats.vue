<template>
  <div class="layout">
    <header class="option">
      <v-select :items="players" label="Select a player"></v-select>
      <div class="option__select"></div>
    </header>
    <main class="rankTable"></main>
  </div>
</template>

<script>
import {getMatchLineup, getGroupStats} from "@/api/index.js";
export default {
  name: "GroupStats",
  data() {
    return {
      groupStats: [],
      player_list: [],
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
    const players = Object.values(lineup.data);
    console.log(players);
    this.player_list = players[0].concat(players[1]);
  },
};
</script>

<style scoped>
.layout {
  width: 100%;
  height: 100%;
}
</style>
