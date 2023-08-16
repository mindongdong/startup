<template>
  <div id="layout">
    <img class="background-image" src="@/assets/background_pro.png" />
    <div class="contents-container">
      <Video ref="videoRef"></Video>
      <div
        class="info-container"
        v-if="this.$store.getters.getToggleList['info']"
      >
        <TeamInfo ref="teamInfoRef"></TeamInfo>
      </div>
      <div
        class="drag-area"
        v-if="isComponentVisible"
        v-for="component in components"
        :key="component.index"
      >
        <draggable
          class="drag-component"
          :list="component.items"
          :group="{ name: 'component' }"
        >
          <div
            class="drag-content"
            v-for="item in component.items"
            :key="item.title"
          >
            <component :is="resolveComponent(item.title)"></component>
          </div>
        </draggable>
      </div>
    </div>
  </div>
</template>

<script>
import Video from "@/components/Video.vue";
import TeamInfo from "@/components/TeamInfo.vue";
import PlayerStats from "@/components/dragComponents/PlayerStats.vue";
import MatchStats from "@/components/dragComponents/MatchStats.vue";
import AttackSeq from "@/components/dragComponents/AttackSeq.vue";
import ShotStats from "@/components/dragComponents/ShotStats.vue";
import draggable from "vuedraggable";
import { mapGetters } from "vuex";

export default {
  components: {
    Video,
    TeamInfo,
    draggable,
    PlayerStats,
    MatchStats,
    AttackSeq,
    ShotStats,
  },
  data() {
    return {
      targetToggle: true,
      detailIndex: 0,
      teamHome: true,
      home_teamName: "",
      away_teamName: "",
      home_lineup: [],
      away_lineup: [],
    };
  },
  async mounted() {
    const video = document.querySelector("Video");

    video.addEventListener("ended", (ev) => {
      // console.log(ev);
      this.playToggle = false;
    });
  },
  computed: {
    isComponentVisible() {
      return this.$store.getters.getToggleList["components"];
    },
    ...mapGetters(["getComponents", "getUnactivateComponents"]),
    components: {
      get() {
        return this.getComponents;
      },
      set(value) {
        this.updateComponents(value);
      },
    },
    unactivate_components: {
      get() {
        return this.getUnactivateComponents;
      },
      set(value) {
        this.updateUnactivateComponents(value);
      },
    },
  },
  methods: {
    resolveComponent(title) {
      if (this.$options.components[title]) {
        console.log(title);
        return title;
      }
      return "div"; // Fallback to 'div' if the component does not exist
    },
    targetChange(target) {
      if (target) {
        this.targetToggle = false;
      } else {
        this.targetToggle = true;
      }
    },
    setDetailIndex(teamHome, idx) {
      this.$refs.teamInfoRef.setDetailIndex(teamHome, idx);
    },
    imageClick(player) {
      this.$refs.videoRef.$refs.analyzeRef.toggleBox(player);
    },
  },
};
</script>

<style scoped>
/* 기본 설정 */
@import url("https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300&display=swap");
img {
  object-fit: contain;
  user-drag: none;
  -webkit-user-drag: none;
  user-select: none;
  -moz-user-select: none;
  -webkit-user-select: none;
  -ms-user-select: none;
}
div {
  box-sizing: border-box;
  color: white;
}
/* * {
  font-family: "Noto Sans KR", sans-serif;
} */
/* 컨테이너 크기 설정 */
#layout {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
}
.background-image {
  position: absolute;
  width: 100%;
  height: 100%;
  /* filter: blur(5px); */

  object-fit: cover;
}
.contents-container {
  position: relative;
  width: calc(100% - 2rem);
  height: 0;
  margin: 4.5rem;
  padding-bottom: 54.5%;
  /* padding-bottom: 2rem; */
  border-radius: 1rem;
  background: rgba(60, 60, 60, 0.5);
  /* backdrop-filter: blur(5px); */
  /* box-shadow: 1px 1px 2px 2px rgba(100, 100, 100, 1),
    0px 0px 1px 4px rgba(255, 217, 244, 0.711), 0px 1px 5px 3px rgba(0, 0, 0, 1); */
  box-shadow: 0px 0px 1px 1px rgba(255, 217, 244, 0.711),
    0px 1px 5px 1px rgba(0, 0, 0, 1);
}
.contents-container:hover {
  background: rgba(71, 71, 71, 0.5);
  box-shadow: 0px 0px 1px 1px rgba(255, 217, 244, 0.711),
    0px 2px 8px 1px rgba(0, 0, 0, 1);
}
.view-mode {
  position: absolute;
  padding-right: 1rem;
  top: 1rem;
  left: calc(50% - 1rem);
  width: 10rem;
  height: 2rem;
  display: flex;
  align-items: center;
  justify-content: space-around;
  z-index: 9999;
  border-top-right-radius: 10px;
  border-bottom-right-radius: 10px;
  background: rgba(0, 0, 0, 0.3);
}
/* .view-mode:hover {
  background: rgba(0, 0, 0, 0.3);
} */
.info-container {
  position: absolute;
  bottom: 6rem;
  left: calc(50% - 33rem);
  width: 66rem;
  height: calc(881px - 42.5rem);
  border-radius: 1rem;
  z-index: 9998;
}
.drag-layout {
  width: 100%;
  height: 100%;
  position: relative;
}
.drag-area {
  position: absolute;
  top: 10rem;
  left: -4rem;
  width: calc((100% - 62rem) / 2);
  height: calc(100% - 20rem);
  cursor: pointer;
  z-index: 9999;
}
.drag-area:last-child {
  left: calc(100% + 4rem - calc((100% - 62rem) / 2));
}
.drag-component {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
  font-size: 1.5rem;
  cursor: pointer;
  z-index: 9999;
}
.drag-content {
  width: 100%;
  height: 45%;
  margin-bottom: 0.4rem;
  background: rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(5px);
  border-radius: 1rem;
  transition: all 0.3s ease;
}
.drag-content:hover {
  background: rgba(0, 0, 0, 0.6);
  box-shadow: 0px 2px 6px -1px rgba(0, 0, 0, 1);
}
.flag {
  cursor: pointer;
  width: 30px;
  height: 20px;
  object-fit: cover;
}
.icon {
  cursor: pointer;
  width: 1.25rem;
  height: 1.25rem;
  filter: invert(100%) sepia(0%) saturate(0%) hue-rotate(93deg) brightness(103%)
    contrast(103%);
}
.icon:hover {
  opacity: 0.6;
}
.icon-large {
  width: 1.75rem;
  height: 1.75rem;
}
.icon-large2 {
  width: 2rem;
  height: 2rem;
}
.rotate180 {
  transform: rotate(180deg);
}
.rotate360 {
  transform: rotate(360deg);
}
.open {
  width: 25%;
}
.openBtn__left {
  left: 25%;
}
.openBtn__right {
  right: 25%;
}
.open__show {
  display: flex;
}
.font__white {
  color: white;
}
.font__skyBlue {
  color: skyblue;
}
.font__purple {
  color: rgb(200, 20, 255);
}
.font__yellow {
  color: #f2ae00;
}
.yellow {
  background: #f2ae00;
}
.blue {
  background: skyblue;
}
.hide {
  display: none;
}
.hide__bottom {
  bottom: -100%;
}
.hide__right {
  right: -100%;
}
</style>
