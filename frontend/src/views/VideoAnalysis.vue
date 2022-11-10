<template>
  <div id="layout">
    <Video></Video>
    <div id="modal-wrapper">
      <div class="info-header">
        <router-link to="/">
          <span>X</span>
        </router-link>
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
    };
  },
  mounted() {
    const video = document.querySelector("Video");
    // console.dir(video);
    // console.log(video.clientWidth, video.clientHeight);
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
img {
  object-fit: cover;
}
div {
  box-sizing: border-box;
}
#layout {
  position: relative;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
#modal-wrapper {
  position: absolute;
  left: 0;
  top: 0;
}
.info-header {
  width: 100%;
  height: 20%;
}
.modal-content {
  width: 100%;
  height: 60%;
}
.video-control {
  width: 100%;
  height: 20%;
}
.video-progress {
  width: 100%;
  height: 50%;
}
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
