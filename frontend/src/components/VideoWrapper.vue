<template>
  <div class="modal-wrapper" @keydown.space.prevent="videoPlay">
    <div class="info-header">
      <router-link to="/">
        <div class="exit-button"></div>
      </router-link>
      <div class="video-tools__column">
        <!-- <div class="button-wrapper">
            <div class="play-button" @click="videoPlay">
              <img
                class="icon"
                v-if="playToggle"
                src="@/assets/icons/pause.png"
              />
              <img class="icon" v-else src="@/assets/icons/play.png" />
            </div>
          </div> -->
        <!-- <div class="button-wrapper">
            <div class="playrate-button">
              <img class="icon rotate180" src="@/assets/icons/playrate.png" />
            </div>
          </div> -->
        <div class="button-wrapper">
          <div class="sound-button" @click="soundMute">
            <img class="icon" v-if="muteToggle" src="@/assets/icons/mute.png" />
            <img class="icon" v-else src="@/assets/icons/sound.png" />
          </div>
        </div>
        <div class="button-wrapper">
          <div class="change-button" @click="videoSwap">
            <img
              class="icon"
              v-if="!changeToggle"
              @click="changeToggle = !changeToggle"
              src="@/assets/icons/change.png"
            />
            <img
              class="icon_on"
              v-else
              src="@/assets/icons/change.png"
              @click="changeToggle = !changeToggle"
            />
          </div>
        </div>
      </div>
    </div>
    <div class="modal-content"></div>
    <div class="video-control">
      <div class="video-progress"></div>
      <div class="video-tools">
        <!-- <div class="video-tools__column"> -->
        <!-- <div class="timestamp">
            {{ currentTime }}
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
          </div> -->
        <!-- <div class="button-wrapper">
            <div class="setting-button">
              <img class="icon icon-large" src="@/assets/icons/setting.png" />
            </div>
          </div> -->
        <!-- </div> -->
      </div>
    </div>
  </div>
</template>

<script>
import Hls from "hls.js";
export default {
  name: "VideoWrapper",
  props: {
    currentTime: {
      type: String,
      default: "00:00:00 / 00:00:00",
    },
    percent: {
      type: Number,
      default: 0,
    },
  },
  data() {
    return {
      playToggle: true,
      muteToggle: false,
      sourceToggle: false,
      changeToggle: false,
      currentData: 0,
      videoSource_m3u8: "http://localhost:3000/video/video.m3u8",
      videoSource_voronoi_m3u8:
        "http://localhost:3000/video/video_voronoi.m3u8",
      videoSource_off_m3u8: "http://localhost:3000/video/output.m3u8",
      videoSource_on_m3u8: "http://localhost:3000/video/output_on.m3u8",
      videoSource_off: "http://localhost:3000/video/video_off.mp4",
      videoSource_on: "http://localhost:3000/video/video_on.mp4",
      audioSource_off: "http://localhost:3000/audio/audioTest.mp3",
      audioSource_on: "http://localhost:3000/audio/audioTest2.mp3",
    };
  },
  methods: {
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
      const audio = this.$store.getters.getCurrentAudio;
      if (audio[0].muted) {
        audio[0].muted = false;
        audio[1].muted = true;
      } else {
        audio[0].muted = true;
        audio[1].muted = false;
      }
    },
    videoSwap() {
      if (!this.sourceToggle) {
        this.setupPlayer(this.videoSource_voronoi_m3u8);
      } else {
        this.setupPlayer(this.videoSource_m3u8);
      }
      this.sourceToggle = !this.sourceToggle;
    },
    setupPlayer(source) {
      const video = this.$store.getters.getCurrentVideo;
      const currentFrame = this.$store.getters.getCurrentFrame;
      console.log(video.webkitDecodedFrameCount, currentFrame);
      // this.$store.commit(
      //   "setCurrentFrame",
      //   video.webkitDecodedFrameCount + currentFrame,
      // );
      this.$store.commit("setSwapCount", 1);
      // 인터벌 멈추고
      clearInterval(this.$store.getters.getCurrentInterval);

      if (Hls.isSupported()) {
        if (this.hls) {
          this.hls.destroy();
        }
        this.hls = new Hls();
        this.hls.loadSource(source);
        this.hls.attachMedia(video);
        this.hls.on(Hls.Events.MANIFEST_PARSED, () => {
          video.play();
        });
      }

      video.currentTime = this.$store.getters.getCurrentTime;
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
  width: calc(100% - 2rem);
  height: calc(100% - 2rem);
  position: absolute;
  left: 0;
  top: 0;
  z-index: 9997;
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
  padding-left: 1rem;
  position: absolute;
  left: calc(50% - 4rem);
  width: 10rem;
  height: 2rem;
  display: flex;
  align-items: center;
  justify-content: space-around;
  z-index: 9999;
  border-top-left-radius: 10px;
  border-bottom-left-radius: 10px;
  background: rgba(0, 0, 0, 0.3);
}
/* .video-tools__column:hover {
  background: rgba(0, 0, 0, 0.3);
} */
.video-tools__column:first-child {
  /* box-sizing: initial;
  padding-right: 10px;
  border-right: 1px solid hsla(0, 0%, 100%, 0.5); */
}
.video-tools__column:nth-child(2) {
  /* margin-left: 20px; */
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
  width: 1.8rem;
  height: 1.8rem;
  /* border-radius: 10%;
  opacity: 0.5;
  cursor: pointer; */
  /* position: relative;
  margin-right: 20px; */
}
.flag {
  cursor: pointer;
  width: 30px;
  height: 20px;
  object-fit: cover;
}
.icon {
  width: 1.8rem;
  height: 1.8rem;
  border-radius: 10%;
  opacity: 0.5;
  cursor: pointer;
  /* cursor: pointer;
  width: 1.25rem;
  height: 1.25rem;
  filter: invert(100%) sepia(0%) saturate(0%) hue-rotate(93deg) brightness(103%)
    contrast(103%); */
}
.icon:hover {
  opacity: 1;
}
.icon_on {
  width: 1.8rem;
  height: 1.8rem;
  border-radius: 10%;
  opacity: 0.8;
  cursor: pointer;
  /* cursor: pointer;
  width: 1.25rem;
  height: 1.25rem;
  filter: invert(100%) sepia(0%) saturate(0%) hue-rotate(93deg) brightness(103%)
    contrast(103%); */
}
.icon_on:hover {
  opacity: 1;
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
