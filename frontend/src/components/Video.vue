<template>
  <div>
    <video
      id="my-player"
      class="video-js"
      preload="auto"
      width="100%"
      height="100%"
      data-setup="{}"
    >
      <source src="@/assets/video1.mp4" type="video/mp4" />
    </video>
    <!-- <div style="margin-top: 30px">
      <p>재생속도: <span id="playback-speed">1</span></p>
      <div style="display: flex">
        <button id="speed-0.5-btn" style="margin-right: 10px">0.5</button>
        <button id="speed-0.75-btn" style="margin-right: 10px">0.75</button>
        <button id="speed-normal-btn" style="margin-right: 10px">
          1(기본)
        </button>
        <button id="speed-1.25-btn" style="margin-right: 10px">1.25</button>
        <button id="speed-1.5-btn" style="margin-right: 10px">1.5</button>
        <button id="speed-1.75-btn" style="margin-right: 10px">1.75</button>
        <button id="speed-2-btn" style="margin-right: 10px">2</button>
      </div>
    </div> -->
  </div>
</template>

<script>
export default {
  methods: {},
  mounted() {
    const video = document.getElementById("my-player");
    // console.dir(video);

    video.addEventListener("play", (ev) => {
      console.log(ev);
    });
    video.addEventListener("pause", (ev) => {
      console.log(ev);
    });
    video.addEventListener("ended", (ev) => {
      console.log(ev);
    });

    // const speed = document.getElementById("playback-speed");

    // // 재생속도를 0.5로 바꾸는 버튼
    // const speedBtn2 = document.getElementById("speed-0.5-btn");
    // speedBtn2.addEventListener("click", function handleClick() {
    //   console.log("speed-0.5-btn-click");
    //   video.playbackRate = 0.5;
    //   speed.innerHTML = "0.5";
    // });

    // // 재생속도를 0.75로 바꾸는 버튼
    // const speedBtn3 = document.getElementById("speed-0.75-btn");
    // speedBtn3.addEventListener("click", function handleClick() {
    //   console.log("speed-0.75-btn-click");
    //   video.playbackRate = 0.75;
    //   speed.innerHTML = "0.75";
    // });

    // // 재생속도를 기본(1)으로 설정하는 버튼
    // const speedBtn4 = document.getElementById("speed-normal-btn");
    // speedBtn4.addEventListener("click", function handleClick() {
    //   console.log("speed-normal-btn-click");
    //   video.playbackRate = 1;
    //   speed.innerHTML = "1";
    // });

    // // 재생속도를 1.25로 바꾸는 버튼
    // const speedBtn5 = document.getElementById("speed-1.25-btn");
    // speedBtn5.addEventListener("click", function handleClick() {
    //   console.log("speed-1.25-btn-click");
    //   video.playbackRate = 1.25;
    //   speed.innerHTML = "1.25";
    // });

    // // 재생속도를 1.5로 바꾸는 버튼
    // const speedBtn6 = document.getElementById("speed-1.5-btn");
    // speedBtn6.addEventListener("click", function handleClick() {
    //   console.log("speed-1.5-btn-click");
    //   video.playbackRate = 1.5;
    //   speed.innerHTML = "1.5";
    // });

    // // 재생속도를 1.75로 바꾸는 버튼
    // const speedBtn7 = document.getElementById("speed-1.75-btn");
    // speedBtn7.addEventListener("click", function handleClick() {
    //   console.log("speed-1.75-btn-click");
    //   video.playbackRate = 1.75;
    //   speed.innerHTML = "1.75";
    // });

    // // 재생속도를 2로 바꾸는 버튼
    // const speedBtn8 = document.getElementById("speed-2-btn");
    // speedBtn8.addEventListener("click", function handleClick() {
    //   console.log("speed-2-btn-click");
    //   video.playbackRate = 2;
    //   speed.innerHTML = "2";
    // });
  },
};
</script>

<style scoped>
.video-js .vjs-control-bar {
  display: none;
}
</style>
