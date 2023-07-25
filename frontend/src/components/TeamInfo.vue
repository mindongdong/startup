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
        <!-- <p class="team__icon--name" draggable="false">{{ home_teamName }}</p> -->
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
        <!-- <p class="team__icon--name" draggable="false">{{ away_teamName }}</p> -->
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
          <div class="playerInfo__detail--icons">
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
          <div class="playerInfo__detail--icons">
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
    const lineup = await getMatchLineup(this.$store.getters.getCurrentTime);
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
  background: rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(10px);
  /* box-shadow: 0px 0px 8px 5px rgba(255, 255, 255, 0.3); */
  /* box-shadow: 0px 2px 8px -1px rgba(0, 0, 0, 1); */
  border-radius: 1rem;
  z-index: 9998;
  color: rgb(218, 222, 218);
  font-weight: 400;
  transition: all 0.3s ease;
}
.team-info:hover {
  background: rgba(0, 0, 0, 0.35);
  box-shadow: 0px 2px 6px -1px rgba(0, 0, 0, 1);
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
  background: rgba(0, 0, 0, 0.5);
  /* box-shadow: 0px 0px 3px rgba(0, 0, 0, 0.7); */
  /* backdrop-filter: blur(10px); */
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
  background: rgba(0, 0, 0, 0.5);
  box-shadow: 0px 0px 3px rgba(0, 0, 0, 0.7);
  border-radius: 0.5rem;
  /* backdrop-filter: blur(10px);  border-radius: 1rem; */
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
.playerInfo__detail--icons {
  flex-direction: column;
}
.playerInfo__icon {
  width: 2rem;
  height: 2rem;
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
  opacity: 0.9;
}

.team__icon {
  width: 4rem;
  height: 4rem;
  border-radius: 50%;
  background: rgba(0, 0, 0, 0.5);
  /* box-shadow: 0px 0px 3px rgba(0, 0, 0, 0.7); */
  /* backdrop-filter: blur(10px); */
  margin: 0 0.5rem 0 1rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  object-fit: contain;
  transition: all 0.3s ease;
}
.team__icon:hover {
  /* margin-top: -1px; */
  background: rgba(40, 40, 40, 0.5);
  box-shadow: 0px 1px 4px -1px rgba(0, 0, 0, 1);
}
.team__icon--img {
  width: 2rem;
  height: 2rem;
  opacity: 0.9;
  transition: all 0.3s ease; /* 애니메이션을 추가합니다. */
}
.team__icon--img:hover {
  width: 2.2rem;
  height: 2.2rem;
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
  top: -0.25rem;
  width: 6.5rem;
  height: 10rem;
  background: rgba(0, 0, 0, 0.5);
  /* box-shadow: 0px 0px 3px rgba(0, 0, 0, 0.7); */
  /* backdrop-filter: blur(10px); */
  margin-left: 1rem;
  border-radius: 0.5rem;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  flex-shrink: 0; /* add this property to keep the width fixed */
  transition: all 0.5s ease; /* 애니메이션을 추가합니다. */
}
.playerList__player:hover {
  width: 7.5rem;
  height: 10.5rem;
  background: rgba(19, 19, 19, 0.5);
  box-shadow: 0px 2px 4px -1px rgba(0, 0, 0, 1);
  transition: all 0.3s ease; /* 애니메이션을 추가합니다. */
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
  opacity: 1;
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
