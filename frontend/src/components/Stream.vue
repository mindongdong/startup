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
      <!-- <source :src="videoSource_3min" type="video/mp4" /> -->
    </video>
    <audio
      ref="audioPlayer1"
      :src="audioSource_off"
      autoplay
      @loadeddata="audioData"
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
      videoSource_3min: "http://localhost:3000/video/3min.mp4",
      videoSource_voronoi: "http://localhost:3000/video/3min_voronoi.mp4",
      // audioSource_off: "http://localhost:3000/audio/audioTest.mp3",
      // audioSource_on: "http://localhost:3000/audio/audioTest2.mp3",
      audioSource_off: "http://localhost:3000/audio/3min_audio.mp3",
      audioSource_on: "http://localhost:3000/audio/3min_audio_on.mp3",
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
      //프레임 정상화
      const currentFrame = this.$store.getters.getCurrentFrame;
      const swapCount = this.$store.getters.getSwapCount;
      console.log(ev.target.webkitDecodedFrameCount, currentFrame);
      console.log(swapCount);
      // if (currentFrame === 0) {
      //   this.$store.commit("setCurrentFrame", -2);
      // } else {
      //   this.$store.commit(
      //     "setCurrentFrame",
      //     -ev.target.webkitDecodedFrameCount + currentFrame - 1 - swapCount,
      //   );
      // }
      this.$store.commit("setCurrentVideo", ev.target);

      // 인터벌 실행
      const interval = setInterval(() => {
        this.$parent.getPrediction();
      }, 100);
      this.$store.commit("setCurrentInterval", interval);
    },
    timeUpdate() {
      this.$parent.timeUpdate();
      this.$store.commit("setCurrentTime", this.$refs.videoPlayer.currentTime);
      console.log(this.$refs.videoPlayer.currentTime);
    },
    pause() {
      this.$refs.audioPlayer1.pause();
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
