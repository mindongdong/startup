import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    currentVideo: null,
    currentInterval: null,
    currentAudio: [],
    currentTime: 0,
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
  },
  mutations: {
    setCurrentVideo(state, videoData) {
      state.currentVideo = videoData;
    },
    setCurrentAudio(state, audioData) {
      state.currentAudio.push(audioData);
    },
    setCurrentInterval(state, intervalData) {
      state.currentInterval = intervalData;
    },
    clearCurrentInterval(state) {
      state.currentInterval = null;
    },
    setCurrentTime(state, timeData) {
      state.currentTime = timeData;
    },
  },
});
