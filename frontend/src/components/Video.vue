<template>
  <div class="layout" ref="videoLayout">
    <Stream></Stream>
    <Analyze></Analyze>
    <Wrapper></Wrapper>
  </div>
</template>

<script>
import Stream from "@/components/Stream.vue";
import Analyze from "@/components/Analyze.vue";
import Wrapper from "@/components/VideoWrapper.vue";

export default {
  components: {
    Stream,
    Analyze,
    Wrapper,
  },
  data() {
    return {};
  },
};
</script>

<style scoped>
.layout {
  width: 72rem;
  height: 40.5rem;
  position: absolute;
  top: 1rem;
  left: 1rem;
  border-radius: 1rem;
}
</style>
