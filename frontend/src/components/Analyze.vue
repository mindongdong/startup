<template>
  <ul class="playerBox__list" ref="playerBox">
    <li
      class="playerBox__item"
      @click="boxClick"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">E.마르티네즈</div>
    </li>
    <li
      class="playerBox__item"
      @click="boxClick"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">N.타글리아피코</div>
    </li>
    <li
      class="playerBox__item"
      @click="boxClick"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">N.오타멘디</div>
    </li>
    <li
      class="playerBox__item"
      @click="boxClick"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">C.로메로</div>
    </li>
    <li
      class="playerBox__item"
      @click="boxClick"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">N.몰리나</div>
    </li>
    <li
      class="playerBox__item"
      @click="boxClick"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">A.막알리스테르</div>
    </li>
    <li
      class="playerBox__item"
      @click="boxClick"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">E.페르난데스</div>
    </li>
    <li
      class="playerBox__item"
      @click="boxClick"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">R.데 파울</div>
    </li>
    <li
      class="playerBox__item"
      @click="boxClick"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">A.디 마리아</div>
    </li>
    <li
      class="playerBox__item"
      @click="boxClick"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">J.알바레스</div>
    </li>
    <li
      class="playerBox__item"
      @click="boxClick"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">L.메시</div>
    </li>
    <li
      class="playerBox__item"
      @click="boxClick"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">H.요리스</div>
    </li>
    <li
      class="playerBox__item"
      @click="boxClick"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">J.쿤데</div>
    </li>
    <li
      class="playerBox__item"
      @click="boxClick"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">R.바란</div>
    </li>
    <li
      class="playerBox__item"
      @click="boxClick"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">D.우파메카노</div>
    </li>
    <li
      class="playerBox__item"
      @click="boxClick"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">T.에르난데스</div>
    </li>
    <li
      class="playerBox__item"
      @click="boxClick"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">A.추아메니</div>
    </li>
    <li
      class="playerBox__item"
      @click="boxClick"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">A.라비오</div>
    </li>
    <li
      class="playerBox__item"
      @click="boxClick"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">O.뎀벨레</div>
    </li>
    <li
      class="playerBox__item"
      @click="boxClick"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">A.그리즈만</div>
    </li>
    <li
      class="playerBox__item"
      @click="boxClick"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">K.음바페</div>
    </li>
    <li
      class="playerBox__item"
      @click="boxClick"
      @mouseover="showCompoenets"
      @mouseleave="hideCompoenets"
    >
      <div class="playerBox__name">O.지루</div>
    </li>
  </ul>
</template>

<script>
export default {
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
    };
  },
  name: "Analyze",
  methods: {
    showCompoenets(ev) {
      const name = ev.target.childNodes[0];
      name.style.display = "block";
    },
    hideCompoenets(ev) {
      const name = ev.target.childNodes[0];
      name.style.display = "none";
    },
    boxClick(ev) {
      console.log(ev.target);
      // Access the parent component
      const parentComponent = this.$parent;
      const grandparentComponent = parentComponent.$parent;
      //ev.target이 부모 태그의 몇번째 자식인지 출력하는 코드
      let index = Array.prototype.indexOf.call(
        ev.target.parentNode.childNodes,
        ev.target,
      );
      console.log(index);
      if (index > 10) {
        grandparentComponent.setDetailIndex(false, index - 11);
      } else {
        grandparentComponent.setDetailIndex(true, index);
      }
    },
    toggleBox(num) {
      const playerBox_list = this.$refs.playerBox.childNodes;
      let index = this.toggle_list.indexOf(num);

      if (index !== -1) {
        // If num exists in the array, remove it
        this.toggle_list.splice(index, 1);
        playerBox_list[num].classList.remove("select");
        playerBox_list[num].dispatchEvent(new Event("mouseleave"));
      } else {
        // If num does not exist in the array, add it
        this.toggle_list.push(num);
        playerBox_list[num].classList.add("select");
        playerBox_list[num].dispatchEvent(new Event("mouseover"));
      }
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
          const zero = Object.values(prediction).every(x => x === 0);
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
  /* display: none; */
  position: absolute;
  z-index: 9998;
  cursor: pointer;
  /* border: 2px solid red; */
  justify-content: center;
  align-items: center;
  /* border: none; */
  border: 1px solid rgba(255, 255, 255, 0.303);
  background: rgba(255, 255, 255, 0.15);
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
  top: -60%;
  display: none;
  height: auto;
  font-size: 1rem;
  text-align: center;
  white-space: nowrap;
}
</style>
