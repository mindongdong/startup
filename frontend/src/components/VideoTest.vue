<template>
  <div class="layout" ref="videoLayout1">
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
    <canvas id="canvas"></canvas>
    <video id="video2" v-if="videoURL" ref="videoPlayer2">
      <source :src="videoURL" type="video/mp4" />
    </video>
    <video
      muted
      id="video"
      v-if="videoURL"
      ref="videoPlayer"
      @loadedmetadata="analyzeStart"
      controls
    >
      <source :src="videoURL" type="video/mp4" />
    </video>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      videoURL: require("@/assets/1280720.mp4"),
      intervalID: null,
      videoPlayer: null,
      videoPlayer2: null,
      isSyncing: false,
    };
  },
  mounted() {
    this.videoPlayer = this.$refs.videoPlayer;
    this.videoPlayer2 = this.$refs.videoPlayer2;
  },
  methods: {
    analyzeStart() {
      this.intervalID = setInterval(() => {
        this.analyzeFrame();
      }, 100);
    },
    analyzeFrame() {
      // if (!this.isVideoValid) {
      //   return;
      // }
      const video = this.$refs.videoPlayer;
      const video2 = this.$refs.videoPlayer2;
      const canvas = document.getElementById("canvas");
      const playerBox_list = document.querySelectorAll(".playerBox__item");
      const playerBox = this.$refs.playerBox;
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      const ctx = canvas.getContext("2d");
      ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
      const startTime = new Date();
      let predictions = {};
      playerBox.width = video.width;
      playerBox.height = video.height;
      canvas.toBlob(
        (blob) => {
          const reader = new FileReader();
          reader.readAsDataURL(blob);
          reader.onload = () => {
            const base64Image = reader.result.split("base64,")[1];

            axios({
              method: "POST",
              url: "https://detect.roboflow.com/fyp-amjew/4",
              params: {
                api_key: "k1dUNOCKVqguMSj0ldH6",
              },
              data: base64Image,
              headers: {
                "Content-Type": "application/x-www-form-urlencoded",
              },
            })
              .then(function (response) {
                const endTime = new Date();
                const elapsedTime = endTime - startTime;
                console.log(`작업 시간: ${elapsedTime}ms`);
                if (elapsedTime < 1000) {
                  console.log(response.data);
                  predictions = response.data["predictions"];
                  for (var i = 0; i < 22; i++) {
                    if (i < predictions["length"]) {
                      const prediction = predictions[i];

                      const kx = 1152 / 1280;
                      const ky = 648 / 720;

                      playerBox_list[i].style.left =
                        (prediction.x - (prediction.width * 1.1) / 2) * kx +
                        "px";
                      playerBox_list[i].style.top =
                        (prediction.y - (prediction.height * 1.1) / 2) * ky -
                        20 +
                        "px";
                      playerBox_list[i].style.width =
                        prediction.width * 1.2 * kx + "px";
                      playerBox_list[i].style.height =
                        prediction.height * 1.2 * ky + "px";
                      playerBox_list[i].style.display = "flex";
                    } else {
                      playerBox_list[i].style.display = "none";
                    }
                  }
                  if (!video.paused) {
                    if (video2.paused) {
                      if (video.currentTime >= 0.5) {
                        video2.currentTime = video.currentTime - 0.5;
                        video2.play();
                      }
                    }
                  } else {
                    video2.currentTime = video.currentTime;
                    video2.pause();
                  }
                }
              })
              .catch(function (error) {
                console.log(error.message);
              });
          };
        },
        "image/jpeg",
        0.95
      );
    },
  },
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#canvas {
  width: 100%;
  position: absolute;
  display: none;
}
.playerBox__list {
  position: absolute;
  z-index: 9998;
}
.playerBox__item {
  display: none;
  position: absolute;
  z-index: 9998;
  cursor: pointer;
  border: 1px solid red;
}
.playerBox__item:hover {
  border: 2px solid red;
}
#video {
  width: 100%;
  position: absolute;
  opacity: 0;
  top: 0;
  left: 0;
  z-index: 9999;
}
#video2 {
  width: 100%;
  position: absolute;
  top: 0;
  left: 0;
  z-index: 15;
}
ul {
  list-style: none;
}
.layout {
  width: 72rem;
  height: 40.5rem;
  position: absolute;
  top: 1rem;
  left: 1rem;
  border-radius: 1rem;
}
</style>
