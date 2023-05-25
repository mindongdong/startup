<template>
  <div class="layout" ref="videoLayout">
    <Stream></Stream>
    <Analyze ref="analyzeRef" :predictionList="predictionList"></Analyze>
    <Wrapper :currentTime="currentTime" :percent="percent"></Wrapper>
  </div>
</template>

<script>
import Stream from "@/components/Stream.vue";
import Analyze from "@/components/Analyze.vue";
import Wrapper from "@/components/VideoWrapper.vue";
import { getTrackingInfo } from "@/api/index";

export default {
  name: "Video",
  components: {
    Stream,
    Analyze,
    Wrapper,
  },
  data() {
    return {
      currentTime: "00:00:00 / 00:00:00",
      percent: 0,
      predictionList: [],
    };
  },
  methods: {
    async timeUpdate() {
      const video = this.$store.getters.getCurrentVideo;
      const currentTime = video.currentTime;
      const duration = video.duration;
      const percent = (currentTime / duration) * 100;
      this.percent = percent;

      let seconds = Math.floor(currentTime % 60);
      let minutes = Math.floor((currentTime / 60) % 60);
      let hours = Math.floor(currentTime / 3600);

      if (seconds < 10) {
        seconds = "0" + seconds;
      }
      if (minutes < 10) {
        minutes = "0" + minutes;
      }
      if (hours < 10) {
        hours = "0" + hours;
      }

      let durationHours = Math.floor(duration / 3600);
      let durationMinutes = Math.floor((duration / 60) % 60);
      let durationSeconds = Math.floor(duration % 60);

      if (durationHours < 10) {
        durationHours = "0" + durationHours;
      }
      if (durationMinutes < 10) {
        durationMinutes = "0" + durationMinutes;
      }
      if (durationSeconds < 10) {
        durationSeconds = "0" + durationSeconds;
      }

      this.currentTime =
        hours +
        ":" +
        minutes +
        ":" +
        seconds +
        " / " +
        durationHours +
        ":" +
        durationMinutes +
        ":" +
        durationSeconds;
    },
    async getPrediction() {
      // const video = this.$store.getters.getCurrentVideo;
      // const currentFrame = this.$store.getters.getCurrentFrame;
      // if (swapCount === 0) {
      //   const frame = {
      //     frame: video.webkitDecodedFrameCount,
      //   };
      //   //프레임 store에 저장
      //   this.$store.commit("setCurrentFrame", frame.frame + 3);
      //   console.log(video.webkitDecodedFrameCount, currentFrame, frame.frame);
      //   const response = await getTrackingInfo(frame);
      //   this.predictionList = response.data;
      // } else {
      //   const frame = {
      //     frame: currentFrame,
      //   };
      //   //프레임 store에 저장
      //   this.$store.commit("setCurrentFrame", frame.frame + 3);
      //   console.log(video.webkitDecodedFrameCount, currentFrame, frame.frame);
      //   const response = await getTrackingInfo(frame);
      //   this.predictionList = response.data;
      // }
      const video = this.$store.getters.getCurrentVideo;
      const videoTime = video.currentTime;
      console.log(videoTime);
      const frame = {
        //change int
        frame: parseInt(videoTime * 27) - 1,
      };
      const response = await getTrackingInfo(frame);
      this.predictionList = response.data;
    },
  },
};
</script>

<style scoped>
.layout {
  width: 72rem;
  height: 40.5rem;
  width: calc(100% - 2rem);
  height: 0;
  padding-bottom: 56.25%;
  position: absolute;
  top: 1rem;
  left: 1rem;
  border-radius: 1rem;
}
</style>
