<template>
  <div class="layout">
    <img class="background-image" src="@/assets/background.png" />
    <ul class="playlist">
      <li class="playlist__item" @click="goToViewer">
        <div class="playlist__contentBox">
          <img class="playlist__thumnail" src="@/assets/content_1.jpeg" />
          <p class="playlist__time">{{ duration }}</p>
        </div>
        <div class="playlist__text">
          <p class="playlist__title">[2022 WC] FRANCE VS ARGENTINA</p>
        </div>
      </li>
      <li class="playlist__item" @click="goToViewer">
        <div class="playlist__contentBox">
          <img class="playlist__thumnail" src="@/assets/content_1.jpeg" />
          <p class="playlist__time">{{ duration }}</p>
        </div>
        <div class="playlist__text">
          <p class="playlist__title">[2022 WC] FRANCE VS ARGENTINA</p>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      duration: "00:05:53",
    };
  },
  methods: {
    goToViewer() {
      this.$router.push("/viewer");
    },
  },
};
</script>

<style scoped>
img {
  object-fit: cover;
  user-drag: none;
  -webkit-user-drag: none;
  user-select: none;
  -moz-user-select: none;
  -webkit-user-select: none;
  -ms-user-select: none;
}
.layout {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
}
.background-image {
  position: absolute;
  top: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.playlist {
  width: 90%;
  height: 90%;
  z-index: 9998;
  display: flex;
  flex-wrap: wrap;
  gap: 0;
}
.playlist__item {
  width: 384px;
  height: 256px;
  margin-right: 6rem;
  cursor: pointer;
  background: rgba(0, 0, 0, 0.5);
  border-radius: 5px;
}
.playlist__item:nth-of-type(3n) {
  margin-right: 0;
}
.playlist__contentBox {
  width: 384px;
  height: 216px;
  position: relative;
}
.playlist__thumnail {
  width: 100%;
  height: 100%;
  border-radius: 5px 5px 0 0;
}
.playlist__time {
  position: absolute;
  bottom: 5px;
  right: 5px;
  width: 4.5rem;
  height: 1.5rem;
  font-size: 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0, 0, 0, 0.8);
  color: white;
  border-radius: 5px;
}
.playlist__text {
  width: 100%;
  height: calc(100% - 216px);
  display: flex;
  align-items: center;
  padding-left: 1rem;
  box-sizing: border-box;
}
.playlist__title {
  font-size: 1rem;
  /* font-weight: bolder; */
  color: white;
}
</style>
