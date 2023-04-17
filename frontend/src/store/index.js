import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    currentVideo: null,
    currentInterval: null,
  },
  getters: {
    getCurrentVideo(state) {
      return state.currentVideo;
    },
    getCurrentInterval(state) {
      return state.currentInterval;
    },
  },
  mutations: {
    setCurrentVideo(state, videoData) {
      state.currentVideo = videoData;
    },
    setCurrentInterval(state, intervalData) {
      state.currentInterval = intervalData;
    },
    clearCurrentInterval(state) {
      state.currentInterval = null;
    },
  },
});
