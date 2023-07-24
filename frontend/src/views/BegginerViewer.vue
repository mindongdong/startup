<template>
  <div id="layout">
    <img class="background-image" src="@/assets/background.png" />
    <div class="contents-container">
      <div class="view-mode">
        <img
          v-if="chatToggle"
          class="view-mode__chat_off"
          src="@/assets/showchat.png"
          @click="chatToggle = !chatToggle"
        />
        <img
          v-else
          class="view-mode__chat_on"
          src="@/assets/showchat.png"
          @click="chatToggle = !chatToggle"
        />
      </div>
      <Video ref="videoRef"></Video>
      <div class="info-container" v-bind:class="{hide__bottom: infoToggle}">
        <TeamInfo></TeamInfo>
      </div>
    </div>
  </div>
</template>

<script>
import Video from "@/components/Video.vue";
import TeamInfo from "@/components/TeamInfo.vue";
import {io} from "socket.io-client";

export default {
  components: {
    Video,
    TeamInfo,
  },
  data() {
    return {
      targetToggle: true,
      messages: [], // Store messages
      newMessage: "", // User input for new message
      socket: null, // WebSocket connection
      infoToggle: true,
      chatToggle: true,
      myName: "메시",
    };
  },
  async mounted() {
    const video = document.querySelector("Video");

    video.addEventListener("ended", ev => {
      // console.log(ev);
      this.playToggle = false;
    });
    video.addEventListener("timeupdate", ev => {
      if (Math.round(video.currentTime) < 10) {
        this.videoTimestamp = `00:0${Math.round(
          video.currentTime,
        )} / 00:${Math.round(video.duration)}`;
      } else {
        this.videoTimestamp = `00:${Math.round(
          video.currentTime,
        )} / 00:${Math.round(video.duration)}`;
      }
    });
    // console.log(video.duration);
  },
  methods: {
    targetChange(target) {
      if (target) {
        this.targetToggle = false;
      } else {
        this.targetToggle = true;
      }
    },
    setDetailIndex(teamHome, idx) {
      console.log(idx);
      this.infoToggle = false;
      this.detailToggle = true;
      this.detailIndex = idx;
      this.teamHome = teamHome;
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
  },
};
</script>

<style scoped>
/* 기본 설정 */
@import url("https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300&display=swap");
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
/* * {
  font-family: "Noto Sans KR", sans-serif;
} */
/* 컨테이너 크기 설정 */
#layout {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
}
.background-image {
  position: absolute;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.contents-container {
  position: relative;
  width: calc(100% - 2rem);
  height: 0;
  padding-bottom: 56.25%;
  background: rgba(255, 255, 255, 0.224);
  border-radius: 1rem;
}
.view-mode {
  position: absolute;
  padding-right: 1rem;
  top: 1rem;
  left: calc(50% - 1rem);
  width: 10rem;
  height: 2rem;
  display: flex;
  align-items: center;
  justify-content: space-around;
  z-index: 9999;
  border-top-right-radius: 10px;
  border-bottom-right-radius: 10px;
  background: rgba(0, 0, 0, 0.3);
}
/* .view-mode:hover {
  background: rgba(0, 0, 0, 0.3);
} */
.view-mode__info_off,
.view-mode__chat_off {
  width: 1.8rem;
  height: 1.8rem;
  border-radius: 10%;
  opacity: 0.5;
  cursor: pointer;
}
.view-mode__info_off:hover,
.view-mode__chat_off:hover {
  opacity: 1;
}
.view-mode__info_on,
.view-mode__chat_on {
  width: 1.8rem;
  height: 1.8rem;
  border-radius: 10%;
  opacity: 0.8;
  /* background: rgba(255, 255, 255, 0.124); */
  cursor: pointer;
}
.view-mode__info_on:hover,
.view-mode__chat_on:hover {
  opacity: 1;
}
.info-container {
  position: absolute;
  bottom: 1rem;
  left: 1rem;
  width: calc(100% - 3rem - 300px);
  height: calc(881px - 42.5rem);
  border-radius: 1rem;
  z-index: 9998;
}
.chat {
  position: absolute;
  right: 1rem;
  bottom: 1rem;
  width: 248px;
  height: calc(100% - 2rem);
  border-radius: 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  transition: right 1s;
  background: #08133a84;
  background: #0a1931c5;
  /* opacity: 0.98; */
  z-index: 9999;
}
.chat__header {
  width: 100%;
  padding: 0 1rem;
  margin-top: 0.5rem;
  height: 3.5rem;
  display: flex;
  justify-content: space-around;
  align-items: center;
  position: relative;
}
.chat__userInfo {
  height: 1.2rem;
  display: flex;
  justify-content: left;
  align-items: center;
  font-size: 1rem;
}
.chat__userName {
  max-width: 60%;
  height: 1.2rem;
  white-space: nowrap;
  overflow-x: hidden;
  font-size: 1rem;
  display: flex;
  align-items: center;
  border: none;
  background: rgba(0, 0, 0, 0);
  color: white;
}
.chat__userColor {
  width: 1.2rem;
  height: 1.2rem;
  border-radius: 50%;
  cursor: pointer;
  background: rgb(200, 20, 255);
}
.header__underLine {
  position: absolute;
  bottom: 0;
  width: 60%;
  height: 1.5px;
  background: #496adf;
}
.chat__content {
  width: 100%;
  height: calc(100% - 17rem);
  padding: 1rem;
  overflow-x: hidden;
  overflow-y: auto;
  direction: ltr;
  /* scroll-behavior: smooth;
  scroll-snap-type: y proximity; */
}
/* Customize the scrollbar background and thickness */
.chat__content::-webkit-scrollbar {
  width: 8px; /* Adjust the thickness of the scrollbar */
}

.chat__content::-webkit-scrollbar-track {
  background: rgba(
    255,
    255,
    255,
    0.1
  ); /* Set the background color of the scrollbar track */
}

.chat__content::-webkit-scrollbar-thumb {
  background: rgba(
    255,
    255,
    255,
    0.3
  ); /* Set the background color of the scrollbar thumb */
  border-radius: 8px; /* Set the border radius of the scrollbar thumb */
}
.chat__userChat,
.chat__myChat {
  position: relative;
  box-sizing: border-box;
  min-height: 1rem;
  width: fit-content;
  max-width: 100%;
  padding: 0.3rem 0.8rem;
  border-radius: 6px 0 6px 0;
  background: rgba(0, 0, 0, 0.5);
  background: #26323800;
  /* border: 2px solid rgba(0, 0, 0, 0.2); */
  color: #fff;
  color: rgba(255, 255, 255, 0.9);
  font-size: 1rem;
  line-height: 1.3rem;
}
.chat__myChat {
  margin: 0 0 0 auto;
  margin-bottom: 1rem;
  text-align: right;
}
/* .chat__userChat:after {
  content: "";
  position: absolute;
  border: 10px solid transparent;
  border-top: 10px solid rgba(0, 0, 0, 0.2);
  border-left: none;
  bottom: -22px;
  left: 10px;
}
.chat__myChat:after {
  content: "";
  position: absolute;
  border: 10px solid transparent;
  border-top: 10px solid rgba(0, 0, 0, 0.2);
  border-right: none;
  bottom: -22px;
  right: 10px;
} */
.chat__sendTarget {
  font-size: 1rem;
  color: #6e8bf4;
}
.chat__box {
  width: 90%;
  height: 12rem;
  background: rgba(56, 56, 79, 0.365);
  border-radius: 1rem;
  box-shadow: rgba(149, 149, 149, 0.24) 0px 3px 8px;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.chat__target {
  width: 90%;
  height: 2.5rem;
  display: flex;
  align-items: center;
}
.chat__targetText {
  cursor: pointer;
  width: 3.5rem;
  height: 70%;
  border-radius: 5px;
  display: flex;
  justify-content: center;
  align-items: center;
  background: rgba(38, 38, 53, 0.365);
  box-shadow: rgba(0, 0, 0, 0.12) 0px 1px 3px, rgba(0, 0, 0, 0.24) 0px 1px 2px;
}
.chat__targetText:last-child {
  margin-right: 0.5rem;
}
.select {
  background: #496adf;
}
.chat__input {
  width: 90%;
  height: 7rem;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.6);
  border-radius: 0.6rem;
}
.chat__text {
  resize: none;
  overflow: auto;
  min-height: 1rem;
  width: 90%;
  height: 90%;
  border: none;
  background: rgba(0, 0, 0, 0);
  font-size: 1rem;
  border-radius: 1rem;
}
.chat__text:focus,
.chat__userName:focus {
  outline: none;
}
.chat__send {
  width: 90%;
  height: 2.5rem;
  display: flex;
  justify-content: flex-end;
  align-items: center;
}
.chat__submit {
  width: 3.5rem;
  height: 1.5rem;
  border-radius: 0.4rem;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #496adf;
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
.open {
  width: 25%;
}
.openBtn__left {
  left: 25%;
}
.openBtn__right {
  right: 25%;
}
.open__show {
  display: flex;
}
.font__white {
  color: white;
}
.font__skyBlue {
  color: skyblue;
}
.font__purple {
  color: rgb(200, 20, 255);
}
.font__yellow {
  color: #f2ae00;
}
.yellow {
  background: #f2ae00;
}
.blue {
  background: skyblue;
}
.hide {
  display: none;
}
.hide__bottom {
  bottom: -100%;
}
.hide__right {
  right: -100%;
}
</style>
