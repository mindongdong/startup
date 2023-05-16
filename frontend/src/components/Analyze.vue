<template>
  <ul class="playerBox__list" ref="playerBox">
    <li class="playerBox__item"></li>
    <li class="playerBox__item"></li>
    <li class="playerBox__item"></li>
    <li class="playerBox__item"></li>
    <li class="playerBox__item"></li>
    <li class="playerBox__item"></li>
    <li class="playerBox__item"></li>
    <li class="playerBox__item"></li>
    <li class="playerBox__item"></li>
    <li class="playerBox__item"></li>
    <li class="playerBox__item"></li>
    <li class="playerBox__item"></li>
    <li class="playerBox__item"></li>
    <li class="playerBox__item"></li>
    <li class="playerBox__item"></li>
    <li class="playerBox__item"></li>
    <li class="playerBox__item"></li>
    <li class="playerBox__item"></li>
    <li class="playerBox__item"></li>
    <li class="playerBox__item"></li>
    <li class="playerBox__item"></li>
    <li class="playerBox__item"></li>
  </ul>
</template>

<script>
import html2canvas from "html2canvas";
export default {
  props: {
    predictionList: {
      type: Array,
      default: [],
      required: true,
    },
  },
  name: "Analyze",
  methods: {
    async captureDiv() {
      const captureDiv = this.$refs.captureDiv;

      try {
        const canvas = await html2canvas(captureDiv);
        const imgData = canvas.toDataURL("image/png");
        this.downloadImage(imgData, "captured-image.png");
        // Do something with the captured image data, e.g. download the image or send it to a server
        console.log(imgData);
      } catch (error) {
        console.error("Error capturing div:", error);
      }
    },
    downloadImage(dataUrl, filename) {
      const link = document.createElement("a");
      link.href = dataUrl;
      link.download = filename;
      link.click();
      link.remove();
    },
  },
  watch: {
    predictionList(newValue, oldValue) {
      // do something with the new value of predictionList
      // console.log("New predictionList value:", newValue);
      // console.log(newValue["length"]);
      const playerBox_list = this.$refs.playerBox.childNodes;
      const video = this.$store.getters.getCurrentVideo;
      for (var i = 0; i < newValue.length; i++) {
        const prediction = newValue[i];
        const kx = video.clientWidth / 1280;
        const ky = video.clientHeight / 720;
        if (prediction != [0, 0, 0, 0]) {
          playerBox_list[i].style.left =
            (prediction[0] - prediction[2] / 100) * kx + "px";
          playerBox_list[i].style.top =
            (prediction[1] - prediction[3] / 100) * ky + "px";
          playerBox_list[i].style.width = prediction[2] * kx + "px";
          playerBox_list[i].style.height = prediction[3] * ky + "px";
          playerBox_list[i].style.display = "flex";
        } else {
          playerBox_list[i].style.display = "none";
        }
      }
    },
  },
};
</script>

<style scoped>
.playerBox__list {
  position: absolute;
  left: 0;
  top: 0;
  z-index: 9999;
}
.playerBox__item {
  display: none;
  position: absolute;
  z-index: 9999;
  cursor: pointer;
  /* border: 2px solid red; */
  transition: 1ms;
  /* border: none; */
}
.playerBox__item:hover {
  border: 1px solid rgba(255, 255, 255, 0.303);
  background: rgba(255, 255, 255, 0.15);
  z-index: 9999;
}
</style>
