<template>
  <div class="layout">
    <div class="header">
      <router-link to="/">
        <span>go to main</span>
      </router-link>
    </div>
    <Video></Video>
  </div>
</template>

<script>
import Video from "@/components/Video.vue";
export default {
  components: {
    Video,
  },
  mounted() {
    document.body.style.width = "100vw";
    document.body.style.height = "100vh";
    document.body.style.cursor = "auto";
  },
};
</script>

<style scoped>
body {
  margin: 0;
  padding: 0;
  overflow-x: hidden;
}
.layout {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.header {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
