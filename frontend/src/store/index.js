import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    currentVideo: null,
    currentInterval: null,
    currentAudio: null,
    currentTime: 0,
    currentFrame: 0,
    currentSwapCount: 0,
    toggleList: {
      info: false,
      mute: false,
      change: false,
      components: false,
    },
    components: [
      {
        index: 1,
        items: [
          {
            title: "PlayerStats",
          },
          {
            title: "MatchStats",
          },
          {
            title: "item 5",
          },
        ],
      },
      {
        index: 2,
        items: [
          {
            title: "item 2",
          },
          {
            title: "item 3",
          },
          {
            title: "item 6",
          },
        ],
      },
    ],
    unactivateComponents: [],
  },
  getters: {
    getCurrentVideo(state) {
      return state.currentVideo;
    },
    getCurrentAudio(state) {
      return state.currentAudio;
    },
    getCurrentInterval(state) {
      return state.currentInterval;
    },
    getCurrentTime(state) {
      return state.currentTime;
    },
    getCurrentFrame(state) {
      return state.currentFrame;
    },
    getSwapCount(state) {
      return state.currentSwapCount;
    },
    getToggleList(state) {
      return state.toggleList;
    },
    getComponents(state) {
      return state.components;
    },
    getUnactivateComponents(state) {
      return state.unactivateComponents;
    },
  },
  mutations: {
    setCurrentVideo(state, videoData) {
      state.currentVideo = videoData;
    },
    setCurrentAudio(state, audioData) {
      state.currentAudio = audioData;
    },
    setCurrentInterval(state, intervalData) {
      state.currentInterval = intervalData;
    },
    setCurrentFrame(state, frameData) {
      state.currentFrame = frameData;
    },
    clearCurrentInterval(state) {
      state.currentInterval = null;
    },
    setCurrentTime(state, timeData) {
      state.currentTime = timeData;
    },
    setSwapCount(state, swapCountData) {
      state.currentSwapCount += swapCountData;
    },
    setToggleList(state, targetToggle) {
      state.toggleList[targetToggle] = !state.toggleList[targetToggle];
    },
    updateComponents(state, componentsData) {
      state.components = componentsData;
    },
    updateUnactivateComponents(state, unactivateComponentsData) {
      state.unactivateComponents = unactivateComponentsData;
    },
  },
});
