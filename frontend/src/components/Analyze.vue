<template>
  <ul class="playerBox__list" ref="playerBox">
    <li
      class="playerBox__item"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">E.마르티네즈</div>
    </li>
    <li
      class="playerBox__item"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">N.타글리아피코</div>
    </li>
    <li
      class="playerBox__item"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">N.오타멘디</div>
    </li>
    <li
      class="playerBox__item"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">C.로메로</div>
    </li>
    <li
      class="playerBox__item"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">N.몰리나</div>
    </li>
    <li
      class="playerBox__item"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">A.막알리스테르</div>
    </li>
    <li
      class="playerBox__item"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">E.페르난데스</div>
    </li>
    <li
      class="playerBox__item"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">R.데 파울</div>
    </li>
    <li
      class="playerBox__item"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">A.디 마리아</div>
    </li>
    <li
      class="playerBox__item"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">J.알바레스</div>
    </li>
    <li
      class="playerBox__item"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">L.메시</div>
    </li>
    <li
      class="playerBox__item"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">H.요리스</div>
    </li>
    <li
      class="playerBox__item"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">J.쿤데</div>
    </li>
    <li
      class="playerBox__item"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">R.바란</div>
    </li>
    <li
      class="playerBox__item"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">D.우파메카노</div>
    </li>
    <li
      class="playerBox__item"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">T.에르난데스</div>
    </li>
    <li
      class="playerBox__item"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">A.추아메니</div>
    </li>
    <li
      class="playerBox__item"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">A.라비오</div>
    </li>
    <li
      class="playerBox__item"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">O.뎀벨레</div>
    </li>
    <li
      class="playerBox__item"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">A.그리즈만</div>
    </li>
    <li
      class="playerBox__item"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">K.음바페</div>
    </li>
    <li
      class="playerBox__item"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">O.지루</div>
    </li>
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
    showCompoenets(ev) {
      console.dir(ev.target);
      const name = ev.target.childNodes[0];
      name.style.display = "block";
    },
    hideCompoenets(ev) {
      console.dir(ev.target);
      const name = ev.target.childNodes[0];
      name.style.display = "none";
    },
  },
  watch: {
    predictionList(newValue, oldValue) {
      // do something with the new value of predictionList
      // console.log("New predictionList value:", newValue);
      // console.log(newValue["length"]);
      const playerBox_list = this.$refs.playerBox.childNodes;
      const video = this.$store.getters.getCurrentVideo;
      if (newValue["22"] == 1) {
        for (let i = 0; i < newValue.length; i++) {
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
      } else {
        for (let i = 0; i < newValue.length - 1; i++) {
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
  /* display: none; */
  position: absolute;
  z-index: 9999;
  cursor: pointer;
  border: 2px solid red;
  justify-content: center;
  align-items: center;
  /* transition: all 1ms; */
  border: none;
}
.playerBox__item:hover {
  display: flex;
  border: 1px solid rgba(255, 255, 255, 0.303);
  background: rgba(255, 255, 255, 0.15);
  z-index: 9999;
}
.playerBox__name {
  position: relative;
  top: -2.5rem;
  display: none;
  height: auto;
  font-size: 1rem;
  text-align: center;
  white-space: nowrap;
}
</style>
