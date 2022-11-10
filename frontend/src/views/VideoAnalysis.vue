<template>
  <div id="layout">
    <Video></Video>
    <div id="modal-wrapper">
      <div class="info-header">
        <router-link to="/">
          <div class="exit-button"></div>
        </router-link>
        <div class="match-winrate">
          <div class="match-info">
            <span>승리확률</span>
            <span>{{ this.team1 }}</span>
            <span>{{ this.team2 }}</span>
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
        <div class="teaminfo-modal">
          <div class="open-button">
            <div class="team-icon">
              <img class="flag" src="@/assets/flags/arg-flag.png" />
            </div>
            <div class="open-icon">
              <img class="icon" src="@/assets/icons/right-double-arrow.png" />
            </div>
          </div>
        </div>
        <div class="teaminfo-modal">
          <div class="open-button">
            <div class="open-icon">
              <img
                class="icon rotate180"
                src="@/assets/icons/right-double-arrow.png"
              />
            </div>
            <div class="team-icon">
              <img class="flag" src="@/assets/flags/fra-flag.png" />
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
      videoTimestamp: "00:00 / 00:18",
      team1: "아르헨티나",
      team2: "프랑스",
      team1_winrate: 38,
      team2_winrate: 62,
    };
  },
  mounted() {
    const video = document.querySelector("Video");
    // console.dir(video);
    // console.log(video.clientWidth, video.clientHeight);
    video.addEventListener("ended", (ev) => {
      console.log(ev);
    });
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
      console.dir(video);

      const modal = document.getElementById("modal-wrapper");
      console.log(modal);

      modal.style.width = `${video.clientWidth}px`;
      modal.style.height = `${video.clientHeight}px`;

      const layout = document.getElementById("layout");
      const posY = (layout.clientHeight - video.clientHeight) / 2;
      modal.style.top = `${posY}px`;
    },
    videoPlay() {
      const video = document.querySelector("Video");
      this.playToggle = this.playToggle ? false : true;
      // console.log(video.paused, this.playToggle);

      if (video.paused) {
        video.play();
      } else {
        video.pause();
      }
    },
    soundMute() {
      this.muteToggle = this.muteToggle ? false : true;
      const video = document.querySelector("Video");
      video.muted = this.muteToggle;
    },
    keydownEvent(ev) {
      // console.log(ev.keyCode);
      if (ev.keyCode === 32) {
        this.videoPlay();
      }
    },
  },
};
</script>

<style scoped>
/* 기본 설정 */
img {
  object-fit: cover;
}
div {
  box-sizing: border-box;
}
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
}
/* 팀 정보 모달 */
.teaminfo-modal {
  position: absolute;
  top: 50%;
  width: 80px;
  height: 50px;
  display: flex;
  align-items: center;
}
.teaminfo-modal:first-child {
  left: 0;
}
.teaminfo-modal:nth-child(2) {
  right: 0;
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
.team-icon {
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
</style>
