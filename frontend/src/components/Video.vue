<template>
  <div>
    <video
      id="my-player"
      class="video-js"
      preload="auto"
      width="100%"
      height="100%"
      data-setup="{}"
      @play="onPlay"
    >
      <source src="@/assets/video.mp4" type="video/mp4" />
    </video>
  </div>
</template>

<script>
export default {
  data() {
    return {
      audioContext: null,
      processor: null,
      audioDataChannel: null,
    };
  },
  mounted() {
    const video = document.getElementById("my-player");
    // console.dir(video);
    this.audioContext = new AudioContext();
    video.addEventListener("pause", (ev) => {
      console.log(ev);
    });
    video.addEventListener("ended", (ev) => {
      console.log(ev);
    });
  },
  methods: {
    // async onPlay() {
    //   // Get the video element
    //   const video = document.querySelector("Video");
    //   // Create a new MediaElementAudioSourceNode from the video element
    //   const sourceNode = this.audioContext.createMediaElementSource(video);
    //   // Create a new AudioWorkletNode to process the audio data
    //   await this.audioContext.audioWorklet.addModule(
    //     "/audio/audio-processor.js"
    //   );
    //   this.processor = new AudioWorkletNode(
    //     this.audioContext,
    //     "audio-processor"
    //   );
    //   this.audioDataChannel = this.processor.port;
    //   // Connect the sourceNode to the processorNode
    //   sourceNode.connect(this.processor);
    //   // Connect the processorNode to the destination (i.e. the speakers)
    //   this.processor.connect(this.audioContext.destination);
    //   // Set up the message event listener to receive the processed audio data
    //   this.audioDataChannel.onmessage = (event) => {
    //     const audioData = event.data;
    //     console.log(audioData);
    //     // use the processed audio data in your AI model
    //   };
    // },
  },
};
</script>

<style scoped>
.video-js .vjs-control-bar {
  display: none;
}
</style>
