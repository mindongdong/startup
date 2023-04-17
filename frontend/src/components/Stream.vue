<template>
  <video
    id="my-player"
    preload="auto"
    width="100%"
    height="100%"
    data-setup="{}"
    autoplay
    @loadeddata="videoData"
    @timeupdate="timeUpdate"
  >
    <!-- <source src="@/assets/video.mp4" type="video/mp4" /> -->
    <source src="http://localhost:3000/video" type="video/mp4" />
  </video>
</template>

<script>
export default {
  name: "Stream",
  methods: {
    videoData(ev) {
      console.log(ev);
      this.$store.commit("setCurrentVideo", ev.target);
      const interval = setInterval(() => {
        this.$parent.getPrediction();
      }, 100);
      this.$store.commit("setCurrentInterval", interval);
    },
    timeUpdate() {
      this.$parent.timeUpdate();
    },
  },
};
</script>

<style scoped></style>
