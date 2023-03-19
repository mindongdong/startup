<template>
  <div>
    <video
      id="my-player"
      class="video-js"
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
    return {
      audioContext: null,
      processor: null,
      audioDataChannel: null,
    };
  },
  mounted() {
    const video = document.getElementById("my-player");
    // console.dir(video);
    this.audioContext = new AudioContext();
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
.video-js .vjs-control-bar {
  display: none;
}
</style>
