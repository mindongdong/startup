<template>
  <video
    id="my-player"
    preload="auto"
    width="100%"
    height="100%"
    data-setup="{}"
    autoplay
    @loadeddata="videoData"
  >
    <!-- <source src="@/assets/video.mp4" type="video/mp4" /> -->
    <source src="http://localhost:3000/video" type="video/mp4" />
  </video>
</template>

<script>
export default {
  methods: {
    videoData(ev) {
      console.log(ev);
      this.$store.commit("setCurrentVideo", ev.target);
    },
  },
};
</script>

<style scoped></style>
