<template>
  <div class="layout">
    <h1 class="title">공격 시퀀스</h1>
    <canvas ref="soccerCanvas" :width="canvasWidth" :height="canvasHeight">
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
      indexList: [],
    };
  },
  computed: {
    colorDict() {
      return {
        독일: "rgba(150, 230, 180, 1)",
        대한민국: "rgba(255,99,132,1)",
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
      this.indexList = Object.keys(response.data.attack_sequence.start_x);
      this.filteredIndexList = this.indexList.filter(
        (index) => index <= this.currentIndex
      );
      // console.log(this.indexList);
    }, 1000);
  },
  methods: {
    drawPitch() {
      let canvas = this.$refs.soccerCanvas;
      let context = canvas.getContext("2d");

      // Set pitch color
      context.fillStyle = "rgba(0,0,0,0.3)"; // set as per your requirement

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
      const calX = this.canvasWidth / 104;
      x = x * calX;
      return x;
    },
    scaleY(y) {
      // Transform y from the event's coordinate system to SVG's coordinate system.
      const calY = this.canvasHeight / 68;
      y = y * calY;
      return y;
    },
    reverseX(x) {
      const calX = this.canvasWidth / 104;
      x = (104 - x) * calX; // Subtract x from the maximum X value (104)
      return x;
    },
    reverseY(y) {
      const calY = this.canvasHeight / 68;
      y = (68 - y) * calY; // Subtract y from the maximum Y value (68)
      return y;
    },
    drawSequenceData() {
      let canvas = this.$refs.soccerCanvas;
      let context = canvas.getContext("2d");

      context.clearRect(0, 0, this.canvasWidth, this.canvasHeight);
      this.drawPitch();

      let period = this.$store.getters.getCurrentTime < 2882 ? "1H" : "2H";
      // period가 1H일 때는 독일이 reverseX, reverseY 적용 한국은 reverseY만 적용
      // period가 2H일 때는 독일은 reverseY만 적용 한국은 reverseX, reverseY 적용
      let first_idx = this.filteredIndexList[0];

      this.filteredIndexList.forEach((eventIndex) => {
        let teamName = this.attackSeqData.team_name[first_idx];
        console.log(period, teamName);
        let reverseBoolean =
          (teamName === "대한민국" && period === "1H") ||
          (teamName === "독일" && period === "2H")
            ? true
            : false;
        let circle_startX = reverseBoolean
          ? this.scaleX(this.attackSeqData.start_x[eventIndex])
          : this.reverseX(this.attackSeqData.start_x[eventIndex]);
        let circle_startY = reverseBoolean
          ? this.reverseY(this.attackSeqData.start_y[eventIndex])
          : this.scaleY(this.attackSeqData.start_y[eventIndex]);
        let line_startX = reverseBoolean
          ? this.scaleX(this.attackSeqData.start_x[eventIndex - 1])
          : this.reverseX(this.attackSeqData.start_x[eventIndex - 1]);
        let line_startY = reverseBoolean
          ? this.reverseY(this.attackSeqData.start_y[eventIndex - 1])
          : this.scaleY(this.attackSeqData.start_y[eventIndex - 1]);
        let line_endX = reverseBoolean
          ? this.scaleX(this.attackSeqData.end_x[eventIndex - 1])
          : this.reverseX(this.attackSeqData.end_x[eventIndex - 1]);
        let line_endY = reverseBoolean
          ? this.reverseY(this.attackSeqData.end_y[eventIndex - 1])
          : this.scaleY(this.attackSeqData.end_y[eventIndex - 1]);

        // Draw circle at start position
        context.beginPath();
        context.arc(circle_startX, circle_startY, 5, 0, 2 * Math.PI, false);
        context.fillStyle =
          this.colorDict[this.attackSeqData.team_name[eventIndex]];
        context.fill();

        // Draw line to end position, if it exists
        if (this.attackSeqData.end_x[eventIndex - 1]) {
          context.beginPath();
          context.moveTo(line_startX, line_startY);
          context.lineTo(line_endX, line_endY);
          context.strokeStyle =
            this.colorDict[this.attackSeqData.team_name[eventIndex - 1]];
          context.stroke();
        }
      });
    },
  },
  beforeDestroy() {
    clearInterval(this.timeInterval);
  },
};
</script>

<style scoped>
.title {
  width: 95%;
  color: white;
  font-size: 1rem;
  text-align: center;
  padding: 0.5rem;
  margin-bottom: 0.5rem;
  border-bottom: 2px solid rgba(0, 0, 0, 0.3);
}
.layout {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
canvas {
  border: 1px solid #000;
}
</style>
