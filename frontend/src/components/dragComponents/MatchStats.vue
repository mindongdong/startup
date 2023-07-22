<template>
  <div class="layout">
    <h1 class="title">실시간 기록</h1>
    <header class="option">
      <h1 class="option__description">팀</h1>
      <div class="dropdown">
        <select v-model="selectedTeam" @change="fetchMatchStats">
          <option value="">전체</option>
          <option :value="home_teamName">{{ home_teamName }}</option>
          <option :value="away_teamName">{{ away_teamName }}</option>
        </select>
      </div>
      <h1 class="option__description">기록</h1>
      <div class="dropdown">
        <select v-model="selectedRecord" @change="fetchMatchStats">
          <option
            v-for="record in Object.keys(this.recordDict)"
            :key="record"
            :value="recordDict[record]"
          >
            {{ record }}
          </option>
        </select>
      </div>
    </header>
    <div class="chart">
      <Bar :data="chartData" :options="chartOptions" :style="chartStyle" />
    </div>
  </div>
</template>

<script>
import { getMatchLineup, getMatchStats } from "@/api/index.js";
import { Bar } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
} from "chart.js";

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
);
export default {
  name: "MatchStats",
  components: { Bar },
  data() {
    return {
      selectedTeam: "",
      selectedRecord: "",
      matchStats: [],
      filteredStats: [],
      home_teamName: "",
      away_teamName: "",
      home_lineup: [],
      away_lineup: [],
      player_list: [],
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
      timeInterval: null,
    };
  },
  computed: {
    chartData() {
      return {
        labels: this.filteredStats.map(
          (item) => item.player_name + " (" + item.team_name + ")"
        ),
        datasets: [
          {
            label:
              this.selectedRecord.charAt(0).toUpperCase() +
              this.selectedRecord.slice(1),
            data: this.filteredStats.map((item) => item[this.selectedRecord]),
            backgroundColor: "#f87979",
          },
        ],
      };
    },
    chartOptions() {
      return {
        responsive: true,
        scales: {
          x: {
            title: {
              display: true,
              text: "Player",
            },
          },
          y: {
            title: {
              display: true,
              text: this.selectedRecord,
            },
          },
        },
      };
    },
    chartStyle() {
      return {
        width: "100%",
        height: "100%",
        color: "white",
      };
    },
  },
  methods: {
    async fetchMatchStats() {
      console.log(this.selectedTeam, this.selectedRecord);
      if (this.selectedRecord) {
        const response = await getMatchStats(
          this.$store.getters.getCurrentTime
        );
        this.matchStats = response.data;

        this.filteredStats = this.matchStats
          .filter(
            (item) =>
              this.selectedTeam === "" || item.team_name === this.selectedTeam
          )
          .map((item) => ({
            player_name: item.player_name,
            team_name: item.team_name,
            [this.selectedRecord]: item[this.selectedRecord],
          }));
        console.log(this.filteredStats);
      }
    },
  },
  created() {
    this.selectedRecord = Object.values(this.recordDict)[0];
  },
  async mounted() {
    const lineup = await getMatchLineup(this.$store.getters.getCurrentTime);
    const team_list = Object.keys(lineup.data);
    this.home_teamName = team_list[0];
    this.away_teamName = team_list[1];
    this.home_lineup = lineup.data[team_list[0]];
    this.away_lineup = lineup.data[team_list[1]];
    this.player_list = this.home_lineup.concat(this.away_lineup);
    this.timeInterval = setInterval(async () => {
      const response = await getMatchStats(this.$store.getters.getCurrentTime);
      this.matchStats = response.data;
      this.filteredStats = this.matchStats
        .filter(
          (item) =>
            this.selectedTeam === "" || item.team_name === this.selectedTeam
        )
        .map((item) => ({
          player_name: item.player_name,
          team_name: item.team_name,
          [this.selectedRecord]: item[this.selectedRecord],
        }));
      console.log(this.filteredStats);
    }, 2000);
  },
  beforeDestroy() {
    clearInterval(this.timeInterval);
  },
};
</script>

<style scoped>
.layout {
  width: 100%;
  height: 100%;
}
.title {
  color: white;
  font-size: 1rem;
}
.option {
  background-color: black;
  padding: 10px;
  display: flex;
  align-items: center;
}

.option__description {
  color: white;
  font-size: 0.8rem;
  margin-right: 0.5rem;
}

.dropdown {
  position: relative;
  display: flex;
  align-items: center;
  margin-right: 20px;
}

.dropdown select {
  background-color: transparent;
  color: white;
  padding: 4px;
  border: 1px solid white;
  border-radius: 5px;
  font-size: 0.8rem;
  appearance: none; /* this will remove the default arrow in some browsers */
  width: 80px;
  outline: none;
}

.dropdown::after {
  /* create a custom dropdown arrow */
  content: "⌄";
  font-size: 10px;
  position: absolute;
  right: 10px;
  top: 5px;
  color: white;
}

.chart {
  width: 100%;
  height: 100%;
  padding: 10px;
}
</style>
