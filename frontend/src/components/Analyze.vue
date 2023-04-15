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
      // console.dir(playerBox_list);
      for (var i = 0; i < 22; i++) {
        if (i < newValue["length"]) {
          const prediction = newValue[i];
          const kx = 1152 / 1280;
          const ky = 648 / 720;
          // console.log(prediction);
          // console.log(playerBox_list[i]);

          if (prediction.width < 150) {
            playerBox_list[i].style.left =
              (prediction.x - prediction.width / 2) * kx + "px";
            playerBox_list[i].style.top =
              (prediction.y - prediction.height / 2) * ky + "px";
            playerBox_list[i].style.width = prediction.width * kx + "px";
            playerBox_list[i].style.height = prediction.height * ky + "px";
            playerBox_list[i].style.display = "flex";
          } else {
            playerBox_list[i].style.display = "none";
          }

          // playerBox_list[i].style.left =
          //   (prediction.x - prediction.width / 2) * kx + "px";
          // playerBox_list[i].style.top =
          //   (prediction.y - prediction.height / 2) * ky + "px";
          // playerBox_list[i].style.width = prediction.width * kx + "px";
          // playerBox_list[i].style.height = prediction.height * ky + "px";
          // playerBox_list[i].style.display = "flex";
        } else {
          playerBox_list[i].style.display = "none";
        }
      }
      // console.log("new value", newValue);
    },
  },
  // computed: {
  //   predictionListWithLabels() {
  //     console.log(this.predictionList);
  //     return this.predictionList;
  //   },
  // },
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
  border: 2px solid red;
  /* transition: all 100ms; */
}
.playerBox__item:hover {
  border: 3px solid rgba(0, 13, 255, 0.4);
  z-index: 9999;
}
</style>
