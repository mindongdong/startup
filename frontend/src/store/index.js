import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    currentVideo: null,
  },
  getters: {
    getCurrentVideo(state) {
      return state.currentVideo;
    },
  },
  mutations: {
    setCurrentVideo(state, videoData) {
      state.currentVideo = videoData;
    },
  },
});
