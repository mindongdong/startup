<template>
  <div class="layout" ref="videoLayout">
    <video
      id="my-player"
      preload="auto"
      width="100%"
      height="100%"
      data-setup="{}"
      @play="onPlay"
    >
      <source src="@/assets/video.mp4" type="video/mp4" />
    </video>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
  mounted() {
    const video = document.getElementById("my-player");
    // console.dir(video);
    video.addEventListener("pause", (ev) => {
      console.log(ev);
    });
    video.addEventListener("ended", (ev) => {
      console.log(ev);
    });
  },
  methods: {},
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
#my-player {
  border-radius: 1rem;
}
</style>
