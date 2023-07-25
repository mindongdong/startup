<template>
  <div class="layout">
    <h1 class="title">슈팅 데이터</h1>
    <canvas ref="soccerCanvas" :width="canvasWidth" :height="canvasHeight">
    </canvas>
  </div>
</template>

<script>
import {getMatchShots} from "@/api/index.js";
export default {
  name: "AttackSeq",
  data() {
    return {
      canvasWidth: 350, // adjust based on your need
      canvasHeight: 228.846153846, // adjust based on your need
      timeInterval: null,
      shotData: null,
      team1Goals: null,
      team2Goals: null,
      failedShots: null,
    };
  },
  computed: {
    goalColorDict() {
      return {
        독일: "blue",
        대한민국: "red",
      };
    },
    shotColorDict() {
      return {
        독일: "#38F4BB",
        대한민국: "#FE6666",
      };
    },
  },
  async mounted() {
    this.drawPitch();
    this.timeInterval = setInterval(async () => {
      const response = await getMatchShots(this.$store.getters.getCurrentTime);
      this.team1Goals = response.data.team1;
      this.team2Goals = response.data.team2;
      this.failedShots = response.data.failed_shots;
      this.drawShotData(this.team1Goals);
      this.drawShotData(this.team2Goals);
      this.drawShotData(this.failedShots);
    }, 2000);
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
        2 * Math.PI,
      );
      context.stroke();

      // Draw the center spot
      context.beginPath();
      context.arc(
        this.canvasWidth / 2,
        this.canvasHeight / 2,
        2,
        0,
        2 * Math.PI,
      );
      context.fill();

      // Draw penalty areas
      this.drawRectangle(
        context,
        this.canvasWidth - 200 / 3,
        (this.canvasHeight - 440 / 3) / 2,
        200 / 3,
        440 / 3,
      );
      this.drawRectangle(
        context,
        0,
        (this.canvasHeight - 440 / 3) / 2,
        200 / 3,
        440 / 3,
      );

      // Draw goal areas
      this.drawRectangle(
        context,
        this.canvasWidth - 100 / 3,
        (this.canvasHeight - 180 / 3) / 2,
        100 / 3,
        180 / 3,
      );
      this.drawRectangle(
        context,
        0,
        (this.canvasHeight - 180 / 3) / 2,
        100 / 3,
        180 / 3,
      );

      // Draw penalty spots
      this.drawCircle(
        context,
        this.canvasWidth - 230 / 3,
        this.canvasHeight / 2,
        2,
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
    drawShotData(shotData) {
      let canvas = this.$refs.soccerCanvas;
      let context = canvas.getContext("2d");

      if (shotData === this.failedShots) {
        shotData.forEach(shot => {
          let x = shot.x;
          let y = shot.y;
          let canvasX = this.scaleX(x);
          let canvasY = this.scaleY(y);
          context.beginPath();
          context.arc(
            canvasX,
            canvasY,
            Math.sqrt(shot.xg) * 35,
            0,
            Math.PI * 2,
            false,
          ); // size is now related to xg
          context.fillStyle = this.shotColorDict[shot.team_name];
          context.fill();
        });
      } else {
        const goals = shotData.goals;
        const teamName = shotData.name;
        // Prepare for drawing. As an example, we'll draw team1Goals here.
        goals.forEach(goal => {
          let x = goal.x;
          let y = goal.y;

          // Transform x and y from the event's coordinate system to SVG's coordinate system.
          // This function depends on the actual size of your SVG and your event's coordinate system.
          // Here we simply use x and y as is.
          let canvasX = this.scaleX(x);
          let canvasY = this.scaleY(y);

          // Example drawing: draw a red circle for each goal
          context.beginPath();
          context.arc(
            canvasX,
            canvasY,
            Math.sqrt(goal.xg) * 35,
            0,
            Math.PI * 2,
            false,
          ); // size is now related to xg
          context.fillStyle = this.goalColorDict[teamName];
          context.fill();
        });
      }
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
      // This function depends on the actual size of your SVG and your event's coordinate system.
      // Here we simply use y as is.
      const calY = this.canvasHeight / 68;
      y = y * calY;
      return y;
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
