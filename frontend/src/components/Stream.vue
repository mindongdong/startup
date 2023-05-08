<template>
  <div>
    <video
      id="my-player"
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
      <source :src="videoSource" type="video/mp4" />
    </video>
    <audio
      ref="audioPlayer1"
      :src="audioSource1"
      autoplay
      @loadeddata="audioData"
    ></audio>
    <audio
      ref="audioPlayer2"
      :src="audioSource2"
      autoplay
      @loadeddata="audioData"
      muted
    ></audio>
  </div>
</template>

<script>
export default {
  name: "Stream",
  data() {
    return {
      videoSource: "http://localhost:3000/video/videoTest.mp4",
      audioSource1: "http://localhost:3000/audio/audioTest.mp3",
      audioSource2: "http://localhost:3000/audio/audioTest2.mp3",
    };
  },
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

<style scoped></style>
