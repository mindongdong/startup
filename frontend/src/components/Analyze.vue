<template>
  <ul class="playerBox__list" ref="playerBox">
    <li
      class="playerBox__item"
      v-for="(player, index) in home_lineup"
      :key="player"
      @click="boxClick(index)"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">{{ player }}</div>
    </li>
    <li
      class="playerBox__item"
      v-for="(player, index) in away_lineup"
      :key="player"
      @click="boxClick(index + 11)"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">{{ player }}</div>
    </li>
  </ul>
</template>

<script>
import { getMatchLineup } from "@/api/index.js";
export default {
  name: "Analyze",
  props: {
    predictionList: {
      type: Array,
      default: [],
      required: true,
    },
  },
  data() {
    return {
      toggle_list: [],
      home_teamName: "",
      away_teamName: "",
      home_lineup: [],
      away_lineup: [],
      player_list: [],
    };
  },
  async mounted() {
    const lineup = await getMatchLineup(this.$store.getters.getCurrentTime);
    console.log(lineup.data);
    const team_list = Object.keys(lineup.data);
    this.home_teamName = team_list[0];
    this.away_teamName = team_list[1];
    this.home_lineup = lineup.data[team_list[0]];
    this.away_lineup = lineup.data[team_list[1]];
    this.player_list = this.home_lineup.concat(this.away_lineup);
    console.log(this.home_lineup);
  },
  methods: {
    showCompoenets(ev) {
      const name = ev.target.childNodes[0];
      name.style.display = "block";
    },
    hideCompoenets(ev) {
      const name = ev.target.childNodes[0];
      name.style.display = "none";
    },
    boxClick(index) {
      // Access the parent component
      const parentComponent = this.$parent;
      const grandparentComponent = parentComponent.$parent;
      //ev.target이 부모 태그의 몇번째 자식인지 출력하는 코드
      // let index = Array.prototype.indexOf.call(
      //   ev.target.parentNode.childNodes,
      //   ev.target
      // );
      console.log(index);
      if (index > 10) {
        grandparentComponent.setDetailIndex(false, index - 11);
      } else {
        grandparentComponent.setDetailIndex(true, index);
      }
    },
    toggleBox(player) {
      const playerBox_list = this.$refs.playerBox.childNodes;
      console.log(player, this.player_list);
      const num = this.player_list.indexOf(player);
      console.log("num: " + num);
      let index = this.toggle_list.indexOf(num);

      if (index !== -1) {
        this.toggle_list.splice(index, 1);
        playerBox_list[num].classList.remove("select");
        playerBox_list[num].dispatchEvent(new Event("mouseleave"));
      } else {
        this.toggle_list.push(num);
        playerBox_list[num].classList.add("select");
        playerBox_list[num].dispatchEvent(new Event("mouseover"));
      }

      // const playerBox_list = this.$refs.playerBox.childNodes;
      // let index = this.toggle_list.indexOf(num);

      // if (index !== -1) {
      //   this.toggle_list.splice(index, 1);
      // playerBox_list[num].classList.remove("select");
      // playerBox_list[num].dispatchEvent(new Event("mouseleave"));
      // } else {
      //   this.toggle_list.push(num);
      // playerBox_list[num].classList.add("select");
      // playerBox_list[num].dispatchEvent(new Event("mouseover"));
      // }
    },
  },
  watch: {
    predictionList(newValue, oldValue) {
      // do something with the new value of predictionList
      // console.log("New predictionList value:", newValue);
      // console.log(newValue["length"]);
      const playerBox_list = this.$refs.playerBox.childNodes;
      const video = this.$store.getters.getCurrentVideo;
      if (newValue["22"] == 1) {
        for (let i = 0; i < newValue.length; i++) {
          const prediction = newValue[i];
          const kx = video.clientWidth / 1280;
          const ky = video.clientHeight / 720;
          const zero = Object.values(prediction).every((x) => x === 0);
          if (!zero) {
            playerBox_list[i].style.left =
              (prediction[0] - prediction[2] / 100) * kx + "px";
            playerBox_list[i].style.top =
              (prediction[1] - prediction[3] / 100) * ky + "px";
            playerBox_list[i].style.width = prediction[2] * kx + "px";
            playerBox_list[i].style.height = prediction[3] * ky + "px";
            playerBox_list[i].style.display = "flex";
            if (Object.values(this.toggle_list).indexOf(i) !== -1) {
              playerBox_list[i].childNodes[0].style.display = "block";
            }
          } else {
            playerBox_list[i].style.display = "none";
            playerBox_list[i].childNodes[0].style.display = "none";
          }
        }
      } else {
        for (let i = 0; i < newValue.length - 1; i++) {
          playerBox_list[i].style.display = "none";
        }
      }
    },
  },
};
</script>

<style scoped>
.playerBox__list {
  position: absolute;
  left: 0;
  top: 0;
  z-index: 9998;
}
.playerBox__item {
  display: none;
  position: absolute;
  z-index: 9998;
  cursor: pointer;
  /* border: 2px solid red; */
  justify-content: center;
  align-items: center;
  transition: all 0.1s ease-in-out;
  /* border: 1px solid rgba(255, 255, 255, 0.303);
  background: rgba(255, 255, 255, 0.15); */
}
.playerBox__item:hover {
  display: flex;
  border: 1px solid rgba(255, 255, 255, 0.303);
  background: rgba(255, 255, 255, 0.15);
  z-index: 9998;
}
.select {
  display: flex;
  border: 1px solid rgba(255, 255, 255, 0.303);
  background: rgba(255, 255, 255, 0.15);
  z-index: 9998;
}
.playerBox__name {
  position: relative;
  top: -70%;
  height: auto;
  font-size: 1rem;
  text-align: center;
  white-space: nowrap;
}
/* playerBox__name에 :after 이용해서 아래 방향 화살표를 만들어줘 */
.playerBox__name:after {
  content: "";
  position: absolute;
  bottom: -1rem;
  left: 50%;
  transform: translateX(-50%);
  border: 0.5rem solid transparent;
  border-top-color: rgba(255, 255, 255, 1);
}
</style>
