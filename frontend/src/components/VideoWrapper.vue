<template>
  <div class="modal-wrapper" @keydown.space.prevent="videoPlay">
    <div class="info-header">
      <router-link to="/">
        <div class="exit-button"></div>
      </router-link>
      <div class="match-winrate">
        <div class="match-info">
          <img
            class="icon"
            @click="leftArrowClick"
            src="@/assets/icons/left-arrow.png"
          />
          <span>{{ data_name }}</span>
          <span>{{ team1_name }}</span>
          <span>{{ team2_name }}</span>
          <img
            class="icon"
            @click="rightArrowClick"
            src="@/assets/icons/right-arrow.png"
          />
        </div>
        <div class="progress-bar__container">
          <div class="progress-bar">
            <span class="progress-bar__text">{{ team1_winrate }}</span>
          </div>
          <div class="progress-bar">
            <span class="progress-bar__text">{{ team2_winrate }}</span>
          </div>
        </div>
      </div>
    </div>
    <div class="modal-content"></div>
    <div class="video-control">
      <div class="video-progress"></div>
      <div class="video-tools">
        <div class="video-tools__column">
          <div class="button-wrapper">
            <div class="play-button" @click="videoPlay">
              <img
                class="icon"
                v-if="playToggle"
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
</template>

<script>
export default {
  data() {
    return {
      playToggle: true,
      muteToggle: false,
      videoTimestamp: "00:00 / 00:00",
      data_name: "승리확률",
      team1_name: "아르헨티나",
      team2_name: "프랑스",
      team1_winrate: 38,
      team2_winrate: 62,
      dataList: [
        {
          name: "승리 확률",
          team1__percent: 42,
          team2__percent: 58,
        },
        {
          name: "점유율",
          team1__percent: 60,
          team2__percent: 40,
        },
        {
          name: "볼 경합 성공률",
          team1__percent: 52,
          team2__percent: 48,
        },
      ],
      currentData: 0,
    };
  },
  methods: {
    leftArrowClick() {
      this.currentData -= 1;
      if (this.currentData == -1) {
        this.currentData = 2;
      }
      const progress = document.getElementsByClassName("progress-bar");

      this.data_name = this.dataList[this.currentData]["name"];
      this.team1_winrate = this.dataList[this.currentData]["team1__percent"];
      this.team2_winrate = this.dataList[this.currentData]["team2__percent"];
      progress[0].style.width =
        this.dataList[this.currentData]["team1__percent"] + "%";
      progress[1].style.width =
        this.dataList[this.currentData]["team2__percent"] + "%";
    },
    rightArrowClick() {
      this.currentData += 1;
      if (this.currentData == 3) {
        this.currentData = 0;
      }
      const progress = document.getElementsByClassName("progress-bar");

      this.data_name = this.dataList[this.currentData]["name"];
      this.team1_winrate = this.dataList[this.currentData]["team1__percent"];
      this.team2_winrate = this.dataList[this.currentData]["team2__percent"];
      progress[0].style.width =
        this.dataList[this.currentData]["team1__percent"] + "%";
      progress[1].style.width =
        this.dataList[this.currentData]["team2__percent"] + "%";
    },
    videoPlay() {
      const video = this.$store.getters.getCurrentVideo;
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
      const video = this.$store.getters.getCurrentVideo;
      video.muted = this.muteToggle;
    },
  },
};
</script>

<style scoped>
img {
  object-fit: contain;
  user-drag: none;
  -webkit-user-drag: none;
  user-select: none;
  -moz-user-select: none;
  -webkit-user-select: none;
  -ms-user-select: none;
}
div {
  box-sizing: border-box;
  color: white;
}
.modal-wrapper {
  width: 72rem;
  height: 40.5rem;
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
  cursor: pointer;
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  left: 1rem;
  top: 2rem;
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
.match-info span:nth-child(3) {
  position: absolute;
  left: 5px;
  font-size: 0.8rem;
}
.match-info span:nth-child(4) {
  position: absolute;
  right: 5px;
  font-size: 0.8rem;
}
.match-info img {
  width: 15px;
  height: 15px;
  margin: 0 10px;
  object-fit: contain;
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
  transition: all 0.5s;
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
  width: 42%;
  background-color: #e76f51;
  left: 0;
}
.progress-bar:nth-child(2) {
  width: 58%;
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
</style>
