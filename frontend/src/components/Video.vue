<template>
  <div class="layout" ref="videoLayout">
    <Stream></Stream>
    <Analyze ref="analyzeRef" :predictionList="predictionList"></Analyze>
    <Wrapper
      ref="wrapperRef"
      :currentTime="currentTime"
      :totalTime="totalTime"
    ></Wrapper>
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
      currentTime: 0,
      totalTime: 0,
      predictionList: [],
    };
  },
  methods: {
    timeUpdate(currentTime, duration) {
      this.currentTime = currentTime;
      this.totalTime = duration;
    },
    async getPrediction() {
      const video = this.$store.getters.getCurrentVideo;
      const videoTime = parseFloat(video.currentTime) + 4653.0;
      // console.log("video time: " + videoTime);
      const frame = parseInt(videoTime * 29.970156368607) + 14;
      // console.log(frame);
      const response = await getTrackingInfo(frame);
      this.predictionList = response.data;
    },
    videoChange() {
      this.$refs.wrapperRef.changeClick();
      const video = this.$store.getters.getCurrentVideo;
      video.currentTime = 0;
      this.$store.commit("setCurrentTime", 0);
      video.play();
    },
  },
};
</script>

<style scoped>
.layout {
  width: calc(100% - 2rem);
  height: 0;
  padding-bottom: 56.25%;
  position: absolute;
  top: 1rem;
  left: 1rem;
  border-radius: 1rem;
}
</style>
