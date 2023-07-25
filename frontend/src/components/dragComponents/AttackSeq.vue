<template>
  <div class="layout">
    <h1 class="title">공격 시퀀스</h1>
    <canvas ref="soccerCanvas" :width="canvasWidth" :height="canvasHeight">
      <!-- <svg v-if="attackSeqData">
        <g
          v-for="(eventIndex, i) in Object.keys(attackSeqData.start_x)"
          :key="i"
        >
          <circle
            :cx="scaleX(attackSeqData.start_x[eventIndex])"
            :cy="scaleY(attackSeqData.start_y[eventIndex])"
            r="5"
            :fill="colorDict[attackSeqData.team_name[eventIndex]]"
          />
          <line
            v-if="attackSeqData.end_x[eventIndex]"
            v-bind="{
              x1: scaleX(attackSeqData.start_x[eventIndex]),
              y1: scaleY(attackSeqData.start_y[eventIndex]),
              x2: scaleX(attackSeqData.end_x[eventIndex]),
              y2: scaleY(attackSeqData.end_y[eventIndex]),
            }"
            stroke="blue"
            stroke-width="2"
            marker-end="url(#arrow)"
          />
        </g>
      </svg> -->
    </canvas>
  </div>
</template>

<script>
import { getAttackSequence } from "@/api/index.js";
export default {
  name: "AttackSeq",
  data() {
    return {
      canvasWidth: 350, // adjust based on your need
      canvasHeight: 228.846153846, // adjust based on your need
      timeInterval: null,
      attackSeqData: null,
      currentIndex: 0,
    };
  },
  computed: {
    colorDict() {
      return {
        독일: "blue",
        대한민국: "red",
      };
    },
  },
  watch: {
    attackSeqData: {
      handler() {
        this.$nextTick(() => {
          // The DOM is updated. Now you can perform any post-update operations.
          this.drawSequenceData();
        });
      },
      deep: true,
    },
  },
  mounted() {
    this.drawPitch();
    this.timeInterval = setInterval(async () => {
      const response = await getAttackSequence(
        this.$store.getters.getCurrentTime
      );
      this.attackSeqData = response.data.attack_sequence;
      this.currentIndex = response.data.index;
      console.log(this.attackSeqData);
    }, 1000);
  },
  methods: {
    drawPitch() {
      let canvas = this.$refs.soccerCanvas;
      let context = canvas.getContext("2d");

      // Set pitch color
      context.fillStyle = "#3e8e41"; // set as per your requirement

      // Draw the outer rectangle
      context.fillRect(0, 0, this.canvasWidth, this.canvasHeight);

      // Set line color
      context.strokeStyle = "#ffffff"; // set as per your requirement
      context.lineWidth = 2;

      // Draw the boundary lines
      context.strokeRect(1, 1, this.canvasWidth - 3, this.canvasHeight - 3);

      // Draw the center line
      context.beginPath();
      context.moveTo(this.canvasWidth / 2, 5);
      context.lineTo(this.canvasWidth / 2, this.canvasHeight - 5);
      context.stroke();

      // Draw the center circle
      context.beginPath();
      context.arc(
        this.canvasWidth / 2,
        this.canvasHeight / 2,
        26.6666666667,
        0,
        2 * Math.PI
      );
      context.stroke();

      // Draw the center spot
      context.beginPath();
      context.arc(
        this.canvasWidth / 2,
        this.canvasHeight / 2,
        2,
        0,
        2 * Math.PI
      );
      context.fill();

      // Draw penalty areas
      this.drawRectangle(
        context,
        this.canvasWidth - 200 / 3,
        (this.canvasHeight - 440 / 3) / 2,
        200 / 3,
        440 / 3
      );
      this.drawRectangle(
        context,
        0,
        (this.canvasHeight - 440 / 3) / 2,
        200 / 3,
        440 / 3
      );

      // Draw goal areas
      this.drawRectangle(
        context,
        this.canvasWidth - 100 / 3,
        (this.canvasHeight - 180 / 3) / 2,
        100 / 3,
        180 / 3
      );
      this.drawRectangle(
        context,
        0,
        (this.canvasHeight - 180 / 3) / 2,
        100 / 3,
        180 / 3
      );

      // Draw penalty spots
      this.drawCircle(
        context,
        this.canvasWidth - 230 / 3,
        this.canvasHeight / 2,
        2
      );
      this.drawCircle(context, 230 / 3, this.canvasHeight / 2, 2);
    },
    drawRectangle(context, x, y, width, height) {
      context.beginPath();
      context.rect(x, y, width, height);
      context.stroke();
    },
    drawCircle(context, x, y, radius) {
      context.beginPath();
      context.arc(x, y, radius, 0, 2 * Math.PI);
      context.fill();
    },
    scaleX(x) {
      // Transform x from the event's coordinate system to SVG's coordinate system.
      // This function depends on the actual size of your SVG and your event's coordinate system.
      // Here we simply use x as is.
      return x;
    },
    scaleY(y) {
      // Transform y from the event's coordinate system to SVG's coordinate system.
      // This function depends on the actual size of your SVG and your event's coordinate system.
      // Here we simply use y as is.
      return y;
    },
    drawSequenceData() {
      let canvas = this.$refs.soccerCanvas;
      let context = canvas.getContext("2d");

      // Loop over the attack sequence data
      for (let eventIndex in this.attackSeqData.start_x) {
        // Extract start and end positions
        let adjust_start_x,
          adjust_start_y = this.adjustCoordinates(
            this.attackSeqData.start_x[eventIndex],
            this.attackSeqData.start_y[eventIndex]
          );
        let adjust_end_x,
          adjust_end_y = this.adjustCoordinates(
            this.attackSeqData.end_x[eventIndex],
            this.attackSeqData.end_y[eventIndex]
          );
        let startX = this.scaleX(adjust_start_x);
        let startY = this.scaleY(adjust_start_y);
        let endX = this.scaleX(adjust_end_x);
        let endY = this.scaleY(adjust_end_y);

        // Draw circle at start position
        context.beginPath();
        context.arc(adjust_start_x, adjust_start_y, 5, 0, 2 * Math.PI, false);
        context.fillStyle =
          this.colorDict[this.attackSeqData.team_name[eventIndex]];
        context.fill();

        // Draw line to end position, if it exists
        if (this.attackSeqData.end_x[eventIndex]) {
          context.beginPath();
          context.moveTo(startX, startY);
          context.lineTo(endX, endY);
          context.strokeStyle = "blue";
          context.stroke();
        }
      }
    },
    adjustCoordinates(x, y) {
      const originalWidth = 104;
      const originalHeight = 68;
      const scale_x = this.canvasWidth / originalWidth;
      const scale_y = this.canvasHeight / originalHeight;
      const adjustedStartX = x * scale_x;
      const adjustedStartY = y * scale_y;
      console.log(adjustedStartX, adjustedStartY);
      return adjustedStartX, adjustedStartY;
    },
  },
  beforeDestroy() {
    clearInterval(this.timeInterval);
  },
};
</script>

<style scoped>
.title {
  color: white;
  font-size: 1.5rem;
  padding: 0.5rem;
}
.layout {
  width: 100%;
  height: 100%;
}
canvas {
  border: 1px solid #000;
}
</style>
