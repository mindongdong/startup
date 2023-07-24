<template>
  <div class="team-info">
    <div class="team-selector">
      <div
        class="team__icon"
        @click="
          detailToggle = false;
          teamHome = true;
        "
        @dblclick="flagClick"
      >
        <p class="team__icon--name" draggable="false">{{ home_teamName }}</p>
        <img
          class="team__icon--img"
          draggable="false"
          src="@/assets/flags/kor-flag.png"
        />
      </div>
      <div
        class="team__icon"
        @click="
          detailToggle = false;
          teamHome = false;
        "
        @dblclick="flagClick"
      >
        <p class="team__icon--name" draggable="false">{{ away_teamName }}</p>
        <img
          class="team__icon--img"
          draggable="false"
          src="@/assets/flags/ger-flag.png"
        />
      </div>
    </div>
    <div class="team__card" v-if="detailToggle">
      <div
        class="team__playerInfo"
        v-for="(player, idx) in home_lineup"
        :key="idx"
        v-if="detailIndex == idx"
      >
        <p class="playerInfo__name">{{ player }}</p>
        <div class="playerInfo__detail">
          <div class="playerInfo__detail--col">
            <p class="playerInfo__detailInfo">아스톤 빌라(Aston Villa)</p>
            <p class="playerInfo__detailInfo">{{ home_teamName }}</p>
            <p class="playerInfo__detailInfo">1992년 9월 2일</p>
            <p class="playerInfo__detailInfo">골키퍼(GK)</p>
          </div>
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/GK 능숙한 펀칭.png"
          />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/GK 적극적 크로스 수비.png"
          />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/스피드 드리블러.png"
          />
        </div>
        <img
          class="playerInfo__img"
          @click="imageClick"
          :src="require(`@/assets/player/${player}.png`)"
        />
      </div>
      <div>
        <img class="playerInfo__icon" src="@/assets/playerIcons/vs_white.png" />
      </div>
      <div
        class="team__playerInfo"
        v-for="(player, idx) in away_lineup"
        :key="idx"
        v-if="detailIndex == idx"
      >
        <p class="playerInfo__name">{{ player }}</p>
        <div class="playerInfo__detail">
          <div class="playerInfo__detail--col">
            <p class="playerInfo__detailInfo">아스톤 빌라(Aston Villa)</p>
            <p class="playerInfo__detailInfo">{{ away_teamName }}</p>
            <p class="playerInfo__detailInfo">1992년 9월 2일</p>
            <p class="playerInfo__detailInfo">골키퍼(GK)</p>
          </div>
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/GK 능숙한 펀칭.png"
          />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/GK 적극적 크로스 수비.png"
          />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/스피드 드리블러.png"
          />
        </div>
        <img
          class="playerInfo__img"
          @click="imageClick"
          :src="require(`@/assets/player/${player}.png`)"
        />
      </div>
    </div>
    <ul class="team__playerList" v-else-if="teamHome">
      <li
        class="playerList__player"
        v-for="(player, idx) in home_lineup"
        :key="idx"
        @click="
          detailToggle = true;
          detailIndex = idx;
        "
      >
        <p class="playerList__name">{{ player }}</p>
        <img
          class="playerList__img"
          :src="require(`@/assets/player/${player}.png`)"
        />
      </li>
    </ul>
    <ul class="team__playerList" v-else>
      <li
        class="playerList__player"
        v-for="(player, idx) in away_lineup"
        :key="idx"
        @click="
          detailToggle = true;
          detailIndex = idx;
        "
      >
        <p class="playerList__name">{{ player }}</p>
        <img
          class="playerList__img"
          :src="require(`@/assets/player/${player}.png`)"
        />
      </li>
    </ul>
  </div>
</template>

<script>
import { getMatchLineup } from "@/api/index";

export default {
  name: "Team",
  props: {},
  data() {
    return {
      teamHome: true,
      detailToggle: false,
      detailIndex: 0,
      home_teamName: "",
      away_teamName: "",
      home_lineup: [],
      away_lineup: [],
    };
  },
  async mounted() {
    const lineup = await getMatchLineup(1);
    console.log(lineup.data);
    const team_list = Object.keys(lineup.data);
    this.home_teamName = team_list[0];
    this.away_teamName = team_list[1];
    this.home_lineup = lineup.data[team_list[0]];
    this.away_lineup = lineup.data[team_list[1]];
    console.log(this.home_lineup);
  },
  methods: {
    flagClick(ev) {
      console.dir(ev.target);
      if (ev.target.localName === "p") {
        console.log(ev.target.innerText);
        if (ev.target.innerText === "아르헨티나") {
          for (let i = 0; i < 11; i++) {
            this.$refs.videoRef.$refs.analyzeRef.toggleBox(i);
          }
        } else if (ev.target.innerText === "프랑스") {
          for (let i = 11; i < 22; i++) {
            this.$refs.videoRef.$refs.analyzeRef.toggleBox(i);
          }
        }
      } else if (ev.target.localName === "img") {
        console.log(ev.target.parentNode.children[0].innerText);
        if (ev.target.parentNode.children[0].innerText === "아르헨티나") {
          for (let i = 0; i < 11; i++) {
            this.$refs.videoRef.$refs.analyzeRef.toggleBox(i);
          }
        } else if (ev.target.parentNode.children[0].innerText === "프랑스") {
          for (let i = 11; i < 22; i++) {
            this.$refs.videoRef.$refs.analyzeRef.toggleBox(i);
          }
        }
      } else if (ev.target.localName === "div") {
        console.log(ev.target.children[0].innerText);
        if (ev.target.children[0].innerText === "아르헨티나") {
          for (let i = 0; i < 11; i++) {
            this.$refs.videoRef.$refs.analyzeRef.toggleBox(i);
          }
        } else if (ev.target.children[0].innerText === "프랑스") {
          for (let i = 11; i < 22; i++) {
            this.$refs.videoRef.$refs.analyzeRef.toggleBox(i);
          }
        }
      }
    },
    imageClick(ev) {
      const url = ev.target.src;
      let match = url.match(/(arg|fr)_(\d+)\./);
      if (match) {
        let label = match[1];
        let number = parseInt(match[2]);
        console.log(label + "_" + number);
        if (label === "fr") {
          this.$refs.videoRef.$refs.analyzeRef.toggleBox(number + 11);
        } else {
          this.$refs.videoRef.$refs.analyzeRef.toggleBox(number);
        }
      }
    },
  },
};
</script>

<style scoped>
.team-info {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  background: rgba(0, 4, 25, 0.7);
  border-radius: 1rem;
  z-index: 9998;
  color: rgb(218, 222, 218);
  font-weight: 300;
}
.team-selector {
  display: flex;
  height: 100%;
  flex-direction: column;
  justify-content: space-evenly;
  /* align-items: center; */
}
.team__container {
  width: 50%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.team__card {
  width: 100%;
  height: 95%;
  display: flex;
  align-items: center;
}
.team__playerInfo {
  width: 100%;
  height: 90%;
  background: rgba(17, 17, 33, 0.55);
  border-radius: 1rem;
  position: relative;
}
.playerInfo__name {
  font-size: 1rem;
  font-weight: 800;
  margin: 0.8rem;
  margin-left: 1.3rem;
}
.playerInfo__detail {
  width: calc(100% - 13.5rem);
  height: calc(100% - 3.5rem);
  margin-left: 0.8rem;
  padding-left: 0.5rem;
  background: rgba(58, 65, 123, 0.378);
  border-radius: 1rem;
  display: flex;
  align-items: center;
  justify-items: space-evenly;
}
.playerInfo__detail--col {
  width: 80%;
  height: 90%;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}
.playerInfo__detailInfo {
  margin-left: 0.4rem;
  font-size: 0.8rem;
}
.playerInfo__icon {
  width: 5rem;
  height: 5rem;
  margin: 0.2rem;
}
.playerInfo__img {
  position: absolute;
  right: 0;
  bottom: 0;
  width: 11.5rem;
  height: 16rem;
  cursor: pointer;
  object-position: center;
  object-fit: contain;
  opacity: 0.8;
}
.team__icon {
  width: 5rem;
  height: 5rem;
  border-radius: 1rem;
  background: rgba(0, 4, 25, 0.7);
  margin: 0 1rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.team__icon--img {
  width: 2rem;
  height: 2rem;
  opacity: 0.8;
}
.team__playerList {
  width: 89%;
  height: 95%;
  overflow-x: auto;
  white-space: nowrap;
  display: flex;
  align-items: center;
}
.playerList__player {
  width: 7rem;
  height: 10.5rem;
  background: rgba(0, 4, 25, 0.7);
  margin-left: 1rem;
  border-radius: 0.5rem;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  flex-shrink: 0; /* add this property to keep the width fixed */
}
.playerList__name {
  width: 100%;
  height: 10%;
  font-size: 0.9rem;
  font-weight: 400;
  display: flex;
  align-items: center;
  justify-content: center;
  position: absolute;
  top: 4px;
}
.playerList__img {
  width: 95%;
  height: 85%;
  position: absolute;
  bottom: 0;
  object-position: center;
  object-fit: contain;
  opacity: 0.8;
}
/* Customize the scrollbar background and thickness */
.team__playerList::-webkit-scrollbar {
  height: 8px; /* Adjust the thickness of the scrollbar */
}

.team__playerList::-webkit-scrollbar-track {
  background: rgba(
    255,
    255,
    255,
    0.1
  ); /* Set the background color of the scrollbar track */
}

.team__playerList::-webkit-scrollbar-thumb {
  background: rgba(
    255,
    255,
    255,
    0.3
  ); /* Set the background color of the scrollbar thumb */
  border-radius: 8px; /* Set the border radius of the scrollbar thumb */
}
</style>
