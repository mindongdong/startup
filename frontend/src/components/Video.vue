<template>
  <div class="layout" ref="videoLayout">
    <Stream></Stream>
    <Analyze :predictionList="predictionList"></Analyze>
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
      console.dir(
        video.webkitDecodedFrameCount % 7 < 4
          ? video.webkitDecodedFrameCount - (video.webkitDecodedFrameCount % 7)
          : video.webkitDecodedFrameCount +
              7 -
              (video.webkitDecodedFrameCount % 7)
      );

      const frame = {
        frame: video.webkitDecodedFrameCount,
        // frame:
        //   video.webkitDecodedFrameCount % 7 < 4
        //     ? video.webkitDecodedFrameCount -
        //       (video.webkitDecodedFrameCount % 7)
        //     : video.webkitDecodedFrameCount +
        //       7 -
        //       (video.webkitDecodedFrameCount % 7),
      };
      const response = await getTrackingInfo(frame);
      // console.log(response.data);
      this.predictionList = response.data;
    },
  },
};
</script>

<style scoped>
.layout {
  width: 72rem;
  height: 40.5rem;
  position: absolute;
  top: 1rem;
  left: 1rem;
  border-radius: 1rem;
}
</style>
