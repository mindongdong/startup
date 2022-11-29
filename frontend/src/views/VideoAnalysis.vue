<template>
  <div id="layout">
    <Video @loadedmetadata="videoData"></Video>
    <div id="modal-wrapper">
      <div class="info-header">
        <router-link to="/">
          <div class="exit-button"></div>
        </router-link>
        <div class="match-winrate">
          <div class="match-info">
            <span>승리확률</span>
            <span>{{ this.team1_name }}</span>
            <span>{{ this.team2_name }}</span>
          </div>
          <div class="progress-bar__container">
            <div class="progress-bar">
              <span class="progress-bar__text">{{ this.team1_winrate }}</span>
            </div>
            <div class="progress-bar">
              <span class="progress-bar__text">{{ this.team2_winrate }}</span>
            </div>
          </div>
        </div>
      </div>
      <div class="modal-content">
        <div
          class="teaminfo-modal left"
          v-bind:class="{ openBtn__left: team1_open }"
        >
          <div class="open-button" @click="openTeam1Modal">
            <div class="team-icon">
              <img class="flag" src="@/assets/flags/arg-flag.png" />
            </div>
            <div class="open-icon">
              <img
                class="icon"
                v-bind:class="{ rotate180: team1_open }"
                src="@/assets/icons/right-double-arrow.png"
              />
            </div>
          </div>
        </div>
        <div
          class="teaminfo-modal right"
          v-bind:class="{ openBtn__right: team2_open }"
        >
          <div class="open-button" @click="openTeam2Modal">
            <div class="open-icon">
              <img
                class="icon rotate180"
                v-bind:class="{ rotate360: team2_open }"
                src="@/assets/icons/right-double-arrow.png"
              />
            </div>
            <div class="team-icon">
              <img class="flag" src="@/assets/flags/fra-flag.png" />
            </div>
          </div>
        </div>
        <div class="teaminfo__lineup left" v-bind:class="{ open: team1_open }">
          <ul class="teaminfo__player">
            <li class="teaminfo__column">
              <div class="teaminfo__number">번호</div>
              <div class="teaminfo__name">선수</div>
              <div class="teaminfo__position">포지션</div>
            </li>
            <li
              class="teaminfo__column"
              v-for="(player, idx) in team1"
              :key="idx"
              @click="clickPlayer"
            >
              <div class="teaminfo__number">{{ player.number }}</div>
              <div class="teaminfo__name">{{ player.name }}</div>
              <div class="teaminfo__position">{{ player.position }}</div>
            </li>
          </ul>
        </div>
        <div class="teaminfo__lineup right" v-bind:class="{ open: team2_open }">
          <ul class="teaminfo__player">
            <li class="teaminfo__column">
              <div class="teaminfo__number">번호</div>
              <div class="teaminfo__name">선수</div>
              <div class="teaminfo__position">포지션</div>
            </li>
            <li
              class="teaminfo__column"
              v-for="(player, idx) in team2"
              :key="idx"
              @click="clickPlayer"
            >
              <div class="teaminfo__number">{{ player.number }}</div>
              <div class="teaminfo__name">{{ player.name }}</div>
              <div class="teaminfo__position">{{ player.position }}</div>
            </li>
          </ul>
        </div>
        <div class="playerinfo__modal">
          <div class="playerinfo__profile">
            <div class="profile__row">
              <img class="profile__img" src="" />
            </div>
            <div class="profile__row">
              <div class="profile__name"></div>
              <div class="profile__team"></div>
              <div class="profile__national"></div>
              <div class="profile__position"></div>
            </div>
          </div>
        </div>
      </div>
      <div class="video-control">
        <div class="video-progress"></div>
        <div class="video-tools">
          <div class="video-tools__column">
            <div class="button-wrapper">
              <div class="play-button" @click="videoPlay">
                <img
                  class="icon"
                  v-if="this.playToggle"
                  src="@/assets/icons/pause.png"
                />
                <img class="icon" v-else src="@/assets/icons/play.png" />
              </div>
            </div>
            <div class="button-wrapper">
              <div class="playrate-button">
                <img class="icon rotate180" src="@/assets/icons/playrate.png" />
              </div>
            </div>
            <div class="button-wrapper">
              <div class="sound-button" @click="soundMute">
                <img
                  class="icon"
                  v-if="muteToggle"
                  src="@/assets/icons/mute.png"
                />
                <img class="icon" v-else src="@/assets/icons/sound.png" />
              </div>
            </div>
          </div>
          <div class="video-tools__column">
            <div class="timestamp">
              {{ videoTimestamp }}
            </div>
          </div>
          <div class="video-tools__column">
            <div class="button-wrapper">
              <div class="fullscreen-button">
                <img
                  class="icon icon-large2"
                  src="@/assets/icons/full-screen.png"
                />
              </div>
            </div>
            <div class="button-wrapper">
              <div class="setting-button">
                <img class="icon icon-large" src="@/assets/icons/setting.png" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Video from "@/components/Video.vue";

export default {
  components: {
    Video,
  },
  data() {
    return {
      playToggle: false,
      muteToggle: false,
      team1OpenToggle: false,
      team2OpenToggle: true,
      videoTimestamp: "00:00 / 00:00",
      team1_name: "아르헨티나",
      team2_name: "프랑스",
      team1_winrate: 38,
      team2_winrate: 62,
      team1: [
        {
          number: 12,
          name: "프랑코 아르마니",
          position: "GK",
        },
        {
          number: 2,
          name: "가브리엘 메르카도",
          position: "RB",
        },
        {
          number: 17,
          name: "니콜라스 오타멘디",
          position: "CB",
        },
        {
          number: 6,
          name: "페데리코 파지오",
          position: "CB",
        },
        {
          number: 16,
          name: "마르코스 로호",
          position: "CB",
        },
        {
          number: 3,
          name: "니콜라스 탈리아피코",
          position: "LB",
        },
        {
          number: 19,
          name: "세르히오 아궤로",
          position: "RM",
        },
        {
          number: 15,
          name: "엔소 페레스",
          position: "RM",
        },
        {
          number: 14,
          name: "하비에르 마스체라노",
          position: "CM",
        },
        {
          number: 7,
          name: "에베르 바네가",
          position: "LM",
        },
        {
          number: 13,
          name: "막시밀리아노 메사",
          position: "RW",
        },
        {
          number: 22,
          name: "크리스티안 파본",
          position: "RW",
        },
        {
          number: 10,
          name: "리오넬 메시",
          position: "CF",
          team: "파리 생제르망",
          national: "아르헨티나",
          img: require("@/assets/player/messi.jpeg"),
        },
        {
          number: 11,
          name: "앙헬 디 마리아",
          position: "LW",
        },
      ],
      team2: [
        {
          number: 1,
          name: "위고 요리스",
          position: "GK",
        },
        {
          number: 2,
          name: "뱅자맹 파바르",
          position: "RB",
        },
        {
          number: 4,
          name: "라파엘 바란",
          position: "CB",
        },
        {
          number: 5,
          name: "사무엘 움티티",
          position: "CB",
        },
        {
          number: 21,
          name: "뤼카 에르난데스",
          position: "LB",
        },
        {
          number: 13,
          name: "은골로 캉테",
          position: "CM",
        },
        {
          number: 6,
          name: "폴 포그바",
          position: "CM",
        },
        {
          number: 10,
          name: "킬리앙 음바페",
          position: "RW",
        },
        {
          number: 20,
          name: "플로리앙 토뱅",
          position: "RW",
        },
        {
          number: 7,
          name: "앙투앙 그리즈만",
          position: "AM",
        },
        {
          number: 18,
          name: "나빌 페키르",
          position: "AM",
        },
        {
          number: 14,
          name: "블레즈 마튀이디",
          position: "LW",
        },
        {
          number: 12,
          name: "코랑탱 톨리소",
          position: "LW",
          team: "올랭피크 리옹",
          national: "프랑스",
          img: require("@/assets/player/tolisso.jpeg"),
        },
        {
          number: 9,
          name: "올리비에 지루",
          position: "CF",
        },
      ],
      team1_open: false,
      team2_open: false,
    };
  },
  mounted() {
    const video = document.querySelector("Video");
    // console.dir(video);
    // console.log(video.clientWidth, video.clientHeight);
    video.addEventListener("ended", (ev) => {
      // console.log(ev);
      this.playToggle = false;
    });
    video.addEventListener("timeupdate", (ev) => {
      // console.log(video.duration, video.currentTime);
      if (Math.round(video.currentTime) < 10) {
        this.videoTimestamp = `00:0${Math.round(
          video.currentTime
        )} / 00:${Math.round(video.duration)}`;
      } else {
        this.videoTimestamp = `00:${Math.round(
          video.currentTime
        )} / 00:${Math.round(video.duration)}`;
      }
    });
    console.log(video.duration);
    this.stageResize();
    video.addEventListener("resize", this.stageResize);
    window.addEventListener("resize", this.stageResize);
    document.addEventListener("keydown", this.keydownEvent);
    document.body.style.width = "100vw";
    document.body.style.height = "100vh";
    document.body.style.cursor = "auto";
    document.body.style.background = "black";
    document.body.style.margin = "0";
    document.body.style.padding = "0";
  },
  methods: {
    stageResize() {
      const video = document.querySelector("Video");
      // console.log(video.clientWidth, video.clientHeight);
      // console.dir(video);

      const modal = document.getElementById("modal-wrapper");
      // console.log(modal);

      modal.style.width = `${video.clientWidth}px`;
      modal.style.height = `${video.clientHeight}px`;

      const layout = document.getElementById("layout");
      const posY = (layout.clientHeight - video.clientHeight) / 2;
      const posX = (layout.clientWidth - video.clientWidth) / 2;
      modal.style.top = `${posY}px`;
      modal.style.left = `${posX}px`;
      console.log(posY, posX);
    },
    videoPlay() {
      const video = document.querySelector("Video");
      this.playToggle = !this.playToggle;
      // console.log(video.paused, this.playToggle);

      if (video.paused) {
        video.play();
      } else {
        video.pause();
      }
    },
    soundMute() {
      this.muteToggle = !this.muteToggle;
      const video = document.querySelector("Video");
      video.muted = this.muteToggle;
    },
    keydownEvent(ev) {
      // console.log(ev.keyCode);
      if (ev.keyCode === 32) {
        this.videoPlay();
      }
    },
    openTeam1Modal() {
      this.team1_open = !this.team1_open;
    },
    openTeam2Modal() {
      this.team2_open = !this.team2_open;
    },
    videoData(ev) {
      console.log(ev);
    },
    clickPlayer(ev) {
      console.log(ev);
      const str = ev.target.parentNode.innerText;
      const regex = /[^0-9]/g;
      const result = str.replace(regex, "");
      const number = parseInt(result);
      console.log(number);
      const team = window.innerWidth / 2 >= ev.clientX ? "team1" : "team2";
      console.log(team);

      const profile = document.getElementsByClassName("profile__row");
      console.dir(profile[1].childNodes);
    },
  },
};
</script>

<style scoped>
/* 기본 설정 */
@import url("https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300&display=swap");
img {
  object-fit: cover;
}
div {
  box-sizing: border-box;
} 
/* * {
  font-family: "Noto Sans KR", sans-serif;
} */
/* 컨테이너 크기 설정 */
#layout {
  position: relative;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}
#layout > div {
  max-width: 100vw;
  max-height: 100vh;
}
#modal-wrapper {
  position: absolute;
  left: 0;
  top: 0;
}
.left {
  left: 0;
}
.right {
  right: 0;
}
/* 상단 모달 설정 */
.info-header {
  position: relative;
  width: 100%;
  height: 20%;
}
/* 메인으로 나가는 버튼 */
.exit-button {
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  left: 10px;
  top: 25px;
  width: 30px;
  height: 30px;
  border-radius: 15px;
  background: rgba(0, 0, 0, 0.6);
}
.exit-button:after {
  position: relative;
  top: 2px;
  content: "\00d7";
  font-size: 30px;
  font-weight: 100;
  color: white;
}
/* 승률 모달 */
.match-winrate {
  width: 400px;
  height: 81px;
  position: absolute;
  top: 10px;
  right: 10px;
  background: rgba(0, 0, 0, 0.6);
  padding: 10px;
  border-radius: 1rem;
}
.match-info {
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}
.match-info span {
  color: white;
  font-size: 1rem;
}
.match-info span:nth-child(2) {
  position: absolute;
  left: 5px;
  font-size: 0.8rem;
}
.match-info span:nth-child(3) {
  position: absolute;
  right: 5px;
  font-size: 0.8rem;
}
.progress-bar__container {
  width: 100%;
  height: 2rem;
  border-radius: 2rem;
  overflow: hidden;
  transition: all 0.5s;
  will-change: transform;
  box-shadow: 0 0 5px hsla(0, 0%, 100%, 0.615);
  position: relative;
  margin-top: 10px;
}
.progress-bar {
  position: absolute;
  height: 100%;
  content: "";
  border-radius: inherit;
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  font-family: sans-serif;
}
.progress-bar:first-child {
  width: 38%;
  background-color: #e76f51;
  left: 0;
}
.progress-bar:nth-child(2) {
  width: 62%;
  background-color: #496adf;
  right: 0;
}
/* 중앙 모달 설정 */
.modal-content {
  width: 100%;
  height: 60%;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
}
/* 팀 정보 모달 */
.teaminfo-modal {
  position: absolute;
  top: 40%;
  width: 80px;
  height: 50px;
  display: flex;
  align-items: center;
  transition: all 0.5s ease;
}
.open-button {
  width: 100%;
  height: 100%;
  border-radius: 1rem;
  display: flex;
  align-items: center;
  justify-content: space-evenly;
  background: rgba(0, 0, 0, 0.5);
}
.teaminfo__lineup {
  transition: all 0.5s ease;
  display: flex;
  flex-direction: column;
  justify-content: center;
  position: absolute;
  overflow-x: hidden;
  width: 0;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  border-radius: 5%;
}
.open {
  width: 25%;
}
.openBtn__left {
  left: 25%;
}
.openBtn__right {
  right: 25%;
}
.teaminfo__player {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-evenly;
}
.teaminfo__column {
  width: 90%;
  height: 6%;
  display: flex;
  align-items: center;
  justify-content: space-evenly;
  border-bottom: 0.5px solid rgba(125, 125, 125, 0.2);
}

.teaminfo__column:hover {
  background: rgba(181, 181, 181, 0.5);
}

.teaminfo__column:first-child:hover {
  background: rgba(0, 0, 0, 0);
}

.teaminfo__column:first-child {
  opacity: 0.6;
}

.teaminfo__number,
.teaminfo__name,
.teaminfo__position {
  color: white;
  display: flex;
  align-items: center;
  font-size: 90%;
  padding: 1%;
}
.teaminfo__number {
  width: 25%;
  height: 100%;
}
.teaminfo__name {
  width: 50%;
  height: 100%;
}
.teaminfo__position {
  width: 25%;
  height: 100%;
}

.playerinfo__modal {
  display: none;
  width: 35%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  border-radius: 30px;
  z-index: 9998;
}
.playerinfo__profile {
  width: 100%;
  height: 50%;
}
.profile__row {
  width: 50%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.profile__img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}
.profile__name {
  width: 100%;
  height: 40%;
}
.profile__team {
  width: 100%;
  height: 20%;
}
.profile__national {
  width: 100%;
  height: 20%;
}
.profile__position {
  width: 100%;
  height: 20%;
}
/* 하단 비디오 컨트롤러 설정 */
.video-control {
  width: 100%;
  height: 20%;
}
.video-progress {
  width: 100%;
  height: 50%;
}
/* 비디오 컨트롤 아이콘 */
.video-tools {
  width: 100%;
  height: 50%;
  position: relative;
  padding: 10px 32px;
  display: flex;
  align-items: flex-end;
}
.video-tools__column {
  width: 115px;
  height: 27px;
  display: flex;
  align-items: center;
  padding: 0 5px;
}
.video-tools__column:first-child {
  box-sizing: initial;
  padding-right: 10px;
  border-right: 1px solid hsla(0, 0%, 100%, 0.5);
}
.video-tools__column:nth-child(2) {
  margin-left: 20px;
}
.video-tools__column:nth-child(3) {
  position: absolute;
  right: 10px;
}
.timestamp {
  color: white;
  text-align: center;
  font-size: 1rem;
}
.button-wrapper {
  position: relative;
  margin-right: 20px;
}
.flag {
  cursor: pointer;
  width: 30px;
  height: 20px;
  object-fit: cover;
}
.icon {
  cursor: pointer;
  width: 1.25rem;
  height: 1.25rem;
  filter: invert(100%) sepia(0%) saturate(0%) hue-rotate(93deg) brightness(103%)
    contrast(103%);
}
.icon:hover {
  opacity: 0.6;
}
.icon-large {
  width: 1.75rem;
  height: 1.75rem;
}
.icon-large2 {
  width: 2rem;
  height: 2rem;
}
.rotate180 {
  transform: rotate(180deg);
}
.rotate360 {
  transform: rotate(360deg);
}
</style>
