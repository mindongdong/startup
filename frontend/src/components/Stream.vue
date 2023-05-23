<template>
  <div>
    <video
      id="my-player"
      ref="videoPlayer"
      preload="auto"
      width="100%"
      height="100%"
      data-setup="{}"
      autoplay
      @loadeddata="videoData"
      @timeupdate="timeUpdate"
      @pause="pause"
      @seeking="timeUpdate"
    >
      <!-- <source src="http://localhost:3000/video" type="video/mp4" /> -->
      <!-- <source :src="videoSource_off" type="video/mp4" /> -->
    </video>
    <audio
      ref="audioPlayer1"
      :src="audioSource_off"
      autoplay
      @loadeddata="audioData"
    ></audio>
    <audio
      ref="audioPlayer2"
      :src="audioSource_on"
      autoplay
      @loadeddata="audioData"
      muted
    ></audio>
  </div>
</template>

<script>
import Hls from "hls.js";

export default {
  name: "Stream",
  data() {
    return {
      videoSource_m3u8: "http://localhost:3000/video/video.m3u8",
      videoSource_off_m3u8: "http://localhost:3000/video/output.m3u8",
      videoSource_on_m3u8: "http://localhost:3000/video/output_on.m3u8",
      videoSource_off: "http://localhost:3000/video/video_off.mp4",
      videoSource_on: "http://localhost:3000/video/video_on.mp4",
      audioSource_off: "http://localhost:3000/audio/audioTest.mp3",
      audioSource_on: "http://localhost:3000/audio/audioTest2.mp3",
      hls: null,
    };
  },
  mounted() {
    if (Hls.isSupported()) {
      this.hls = new Hls();
      this.hls.loadSource(this.videoSource_m3u8);
      this.hls.attachMedia(this.$refs.videoPlayer);
      this.hls.on(Hls.Events.MANIFEST_PARSED, () => {
        this.$refs.videoPlayer.play();
      });
    }
  },
  beforeDestroy() {
    if (this.hls) {
      this.hls.destroy();
    }
  },
  methods: {
    videoData(ev) {
      console.dir(ev);
      this.$store.commit("setCurrentVideo", ev.target);
      const interval = setInterval(() => {
        this.$parent.getPrediction();
      }, 100);
      this.$store.commit("setCurrentInterval", interval);
    },
    timeUpdate() {
      this.$parent.timeUpdate();
      this.$store.commit("setCurrentTime", this.$refs.videoPlayer.currentTime);
      this.$refs.audioPlayer1.currentTime = this.$refs.videoPlayer.currentTime;
      this.$refs.audioPlayer2.currentTime = this.$refs.videoPlayer.currentTime;
    },
    pause() {
      this.$refs.audioPlayer1.pause();
      this.$refs.audioPlayer2.pause();
    },
    audioData(ev) {
      console.log(ev);
      this.$store.commit("setCurrentAudio", ev.target);
    },
  },
};
</script>

<style scoped>
#my-player {
  border-radius: 1rem;
}
</style>
