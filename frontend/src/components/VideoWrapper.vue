<template>
  <div class="modal-wrapper" @keydown.space.prevent="videoPlay">
    <div class="info-header" @mouseover="hideTooltip">
      <router-link to="/">
        <div class="exit-button"></div>
      </router-link>
      <div class="video-tools__column">
        <div class="button-wrapper">
          <div class="sound-button">
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
    <div class="modal-content" @mouseover="hideTooltip"></div>
    <div class="video-control">
      <!-- <button @click="videoPlay">{{ playToggle ? false : true }}</button> -->
      <input
        type="range"
        min="0"
        :max="100"
        v-model="percent"
        @input="seekTime"
        @mousemove="updateTooltip"
        @mouseleave="startHideTooltip"
        :style="rangeStyle"
        class="video-control__range"
      />
      <div
        v-if="showTooltip"
        :style="{ left: `${mouseX}px` }"
        class="time-tooltip"
      >
        {{ tooltipTime }}
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
      type: Number,
      default: 0.0,
    },
    totalTime: {
      type: Number,
      default: 0.0,
    },
  },
  data() {
    return {
      playToggle: true,
      muteToggle: false,
      sourceToggle: false,
      changeToggle: false,
      currentData: 0,
      percent: 0,
      videoSource_m3u8: "http://localhost:3000/video/video.m3u8",
      videoSource_voronoi_m3u8:
        "http://localhost:3000/video/video_voronoi.m3u8",
      showTooltip: false,
      tooltipTime: "",
      tooltipStyle: {},
      mouseX: 0,
      tooltipHideTimeout: null,
    };
  },
  computed: {
    rangeStyle() {
      let progress = this.percent;
      let color1 = "#FF0000"; // color for the completed part
      let color2 = "#D3D3D3"; // color for the uncompleted part
      return `background: linear-gradient(90deg, ${color1} ${progress}%, ${color2} ${progress}%);`;
    },
  },
  watch: {
    currentTime(newTime) {
      this.percent = (newTime / this.totalTime) * 100;
    },
    totalTime(newTotal) {
      this.percent = (this.currentTime / newTotal) * 100;
    },
  },
  methods: {
    seekTime() {
      const video = this.$store.getters.getCurrentVideo;
      const seekto = video.duration * (this.percent / 100);
      video.currentTime = seekto;
      video.play();
    },
    updateTooltip(event) {
      clearTimeout(this.tooltipHideTimeout); // clear the hide tooltip timer
      const video = this.$store.getters.getCurrentVideo;
      const percent = (event.offsetX / event.target.offsetWidth) * 100;
      const time = video.duration * (percent / 100);
      let hours = Math.floor(time / 3600);
      let minutes = Math.floor((time / 60) % 60);
      let seconds = Math.floor(time % 60);
      if (seconds < 10) {
        seconds = "0" + seconds;
      }
      if (minutes < 10) {
        minutes = "0" + minutes;
      }
      if (hours < 10) {
        hours = "0" + hours;
      }
      this.mouseX = event.clientX - event.target.getBoundingClientRect().left + 10;
      this.tooltipTime = `${hours}:${minutes}:${seconds}`;
      this.tooltipStyle = {
        left: `${event.pageX}px`,
      };
      this.showTooltip = true;
    },
    startHideTooltip() {
      this.tooltipHideTimeout = setTimeout(this.hideTooltip, 100); // start the hide tooltip timer
    },
    hideTooltip() {
      this.showTooltip = false;
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
    videoSwap() {
      // const video = this.$store.getters.getCurrentVideo;
      if (!this.sourceToggle) {
        this.setupPlayer(this.videoSource_voronoi);
        // video.source = this.videoSource_voronoi;
      } else {
        this.setupPlayer(this.videoSource_3min);
        // video.source = this.videoSource_3min;
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
  width: 100%;
  height: calc(100% - 1rem);
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
  display: flex;
  align-items: flex-end;
  justify-content: center;
  position: relative;
}
.video-progress {
  width: 100%;
  height: 50%;
}
.video-control__range {
  width: 99%;
  height: 5px;
  -webkit-appearance: none;
  border-radius: 5px;
  margin-bottom: 2px;
}

.video-control__range::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 20px;
  height: 20px;
  background: #ff0000;
  border-radius: 50%;
  box-shadow: 0 0 4px 0 rgba(0, 0, 0, 0.5);
  transition: background 0.3s;
}

.video-control__range::-moz-range-thumb {
  width: 20px;
  height: 20px;
  background: #ff0000;
  border-radius: 50%;
  box-shadow: 0 0 4px 0 rgba(0, 0, 0, 0.5);
  transition: background 0.3s;
}

.video-control__range:hover::-webkit-slider-thumb {
  background: #ff4500;
}

.video-control__range:hover::-moz-range-thumb {
  background: #ff4500;
}

.video-control__range::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 20px;
  height: 20px;
  background: #ff0000;
  border-radius: 50%;
  box-shadow: 0 0 4px 0 rgba(0, 0, 0, 0.5);
  transition: background 0.3s;
}

.video-control__range::-moz-range-thumb {
  width: 20px;
  height: 20px;
  background: #ff0000;
  border-radius: 50%;
  box-shadow: 0 0 4px 0 rgba(0, 0, 0, 0.5);
  transition: background 0.3s;
}

.video-control__range:hover::-webkit-slider-thumb {
  background: #ff4500;
}

.video-control__range:hover::-moz-range-thumb {
  background: #ff4500;
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
  left: calc(50% - 10rem);
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
  padding-right: 10px;
  border-right: 1px solid hsla(0, 0%, 100%, 0.5);
}
.video-tools__column:nth-child(2) {
  /* margin-left: 20px; */
}
.video-tools__column:nth-child(3) {
  position: absolute;
  right: 10px;
}
.time-tooltip {
  position: absolute;
  padding: 5px 10px;
  color: #fff;
  background-color: rgba(0, 0, 0, 0.7);
  border-radius: 2px;
  text-align: center;
  white-space: nowrap;
  font-size: 12px;
  bottom: 1.5rem;
  transform: translateX(-50%);

  &:after {
    content: "";
    position: absolute;
    top: 100%;
    left: 50%;
    width: 0;
    height: 0;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-bottom: 5px solid rgba(0, 0, 0, 0.7);
    transform: translateX(-50%) rotate(180deg);
  }
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
