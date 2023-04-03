<template>
  <div id="layout">
    <img class="background-image" src="@/assets/background.png" />
    <div class="contents-container">
      <Video></Video>
      <div class="team-info">
        <div class="team__container">
          <div class="team__card">
            <div class="team__playerInfo">
              <p class="playerInfo__name">킬리안 음바페(Kylian Mbappe)</p>
              <div class="playerInfo__detail">
                <div class="playerInfo__detail--col">
                  <p class="playerInfo__detailInfo">파리 생제르망(PSG)</p>
                  <p class="playerInfo__detailInfo">프랑스</p>
                  <p class="playerInfo__detailInfo">1998년 12월 20일</p>
                  <p class="playerInfo__detailInfo">스트라이커(ST)</p>
                </div>
                <img
                  class="playerInfo__icon"
                  src="@/assets/playerIcons/스피드 드리블러.png"
                />
              </div>
              <img class="playerInfo__img" src="@/assets/player/mbappe.png" />
            </div>
          </div>
          <div class="team__icon">
            <p class="team__icon--name">프랑스</p>
            <img class="team__icon--img" src="@/assets/flags/fra-flag.png" />
          </div>
        </div>
        <div class="team__container">
          <div class="team__icon">
            <p class="team__icon--name">아르헨티나</p>
            <img class="team__icon--img" src="@/assets/flags/arg-flag.png" />
          </div>
          <div class="team__card">
            <ul class="team__playerList">
              <li class="playerList__player">
                <p class="playerList__name">10 L.메시</p>
                <img class="playerList__img" src="@/assets/player/messi.png" />
              </li>
              <li class="playerList__player">
                <p class="playerList__name">10 L.메시</p>
                <img class="playerList__img" src="@/assets/player/messi.png" />
              </li>
              <li class="playerList__player">
                <p class="playerList__name">10 L.메시</p>
                <img class="playerList__img" src="@/assets/player/messi.png" />
              </li>
              <li class="playerList__player">
                <p class="playerList__name">10 L.메시</p>
                <img class="playerList__img" src="@/assets/player/messi.png" />
              </li>
              <li class="playerList__player">
                <p class="playerList__name">10 L.메시</p>
                <img class="playerList__img" src="@/assets/player/messi.png" />
              </li>
              <li class="playerList__player">
                <p class="playerList__name">10 L.메시</p>
                <img class="playerList__img" src="@/assets/player/messi.png" />
              </li>
              <li class="playerList__player">
                <p class="playerList__name">10 L.메시</p>
                <img class="playerList__img" src="@/assets/player/messi.png" />
              </li>
              <li class="playerList__player">
                <p class="playerList__name">10 L.메시</p>
                <img class="playerList__img" src="@/assets/player/messi.png" />
              </li>
              <li class="playerList__player">
                <p class="playerList__name">10 L.메시</p>
                <img class="playerList__img" src="@/assets/player/messi.png" />
              </li>
              <li class="playerList__player">
                <p class="playerList__name">10 L.메시</p>
                <img class="playerList__img" src="@/assets/player/messi.png" />
              </li>
              <li class="playerList__player">
                <p class="playerList__name">10 L.메시</p>
                <img class="playerList__img" src="@/assets/player/messi.png" />
              </li>
            </ul>
          </div>
        </div>
      </div>
      <div class="chat">
        <div class="chat__header">
          <p class="chat__userInfo">채팅방 참여자 : 2/5 명</p>
          <div class="chat__invite">초대</div>
          <div class="header__underLine"></div>
        </div>
        <div class="chat__content">
          <div
            class="chat__liveChat"
            v-for="(message, idx) in messages"
            :key="idx"
          >
            <div class="chat__userChat" v-if="message.user != 'Me'">
              <span class="chat__userName">[AI 해설]</span><br /><br />
              <p>{{ message.text }}</p>
            </div>
            <div class="chat__myChat" v-else>
              <span class="chat__sendTarget">[{{ message.user }}]</span
              ><br /><br />
              <p>{{ message.text }}</p>
            </div>
          </div>
        </div>
        <div class="chat__box">
          <div class="chat__target">
            <div
              class="chat__targetText"
              v-bind:class="{select: !targetToggle}"
              @click="targetChange"
            >
              모두
            </div>
            <div
              class="chat__targetText"
              v-bind:class="{select: targetToggle}"
              @click="targetChange(ai)"
            >
              AI
            </div>
            에게
          </div>
          <div class="chat__input">
            <textarea
              class="chat__text"
              v-model="newMessage"
              @keydown.enter.prevent="sendMessage"
            ></textarea>
          </div>
          <div class="chat__send">
            <div class="chat__submit" @click="sendMessage">전송</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Video from "@/components/Video.vue";
import {io} from "socket.io-client";

export default {
  components: {
    Video,
  },
  data() {
    return {
      icon_description: {
        "주발 선호": "약한 발을 잘 사용하지 않습니다",
        "예리한 감아차기": "감아차기에 능숙합니다",
        "중거리 슛 선호": "중거리 슛을 자주 합니다",
        "얼리 크로스 선호": "얼리 크로스를 자주 합니다",
        "화려한 개인기": "다양한 개인기를 사용할 수 있습니다",
        "테크니컬 드리블러": "1:1 드리블 돌파에 능숙합니다",
        "아웃사이드 슈팅/크로스": "아웃사이드 슈팅과 크로스에 능숙합니다",
        "플레이 메이커": "팀의 중심이 되어 경기를 조율합니다",
        "칩슛 선호": "칩슛을 자주 사용합니다",
        강철몸: "부상을 잘 당하지 않습니다",
        "스피드 드리블러": "치고 달리기에 능숙합니다",
        "긴 패스 선호": "긴 패스를 자주 합니다",
        "슬라이딩 태클 선호": "슬라이딩 태클을 자주 합니다",
        "패스 마스터": "패스 스킬이 뛰어납니다",
        "파워 헤더": "강력한 헤더 슛을 할 수 있습니다",
        "팀 플레이어": "팀을 위해 희생하는 플레이를 합니다",
        리더십: "팀을 잘 이끄는 플레이어",
        "장거리 스로인": "장거리 스로인을 할 수 있습니다",
        "GK 적극적 크로스 수비": "크로스 수비시에 뛰어나가는 경향이 있습니다",
        "GK 능숙한 펀칭": "펀칭을 잘합니다",
        "스위퍼 키퍼": "수비 범위가 넓습니다",
        유리몸: "부상을 잘 당합니다",
        승부욕: "경기의 마지막까지 강한 투지를 발휘합니다",
      },
      position_description: {
        GK: "골키퍼",
        LB: "좌측 수비수",
        CB: "중앙 수비수",
        RB: "우측 수비수",
        CM: "중앙 미드필더",
        CDM: "수비형 미드필더",
        LM: "좌측 미드필더",
        RM: "우측 미드필더",
        AM: "공격형 미드필더",
        LW: "좌측 윙어",
        RW: "우측 윙어",
        ST: "스트라이커",
        CF: "중앙 공격수",
      },
      targetToggle: true,
      messages: [], // Store messages
      newMessage: "", // User input for new message
      socket: null, // WebSocket connection
    };
  },
  async mounted() {
    // Initialize WebSocket connection
    this.socket = io("http://localhost:3000");

    // Add received message to messages array
    this.socket.on("message", message => {
      this.messages.push(message);
    });
  },
  methods: {
    // stageResize() {
    //   const video = document.querySelector("Video");
    //   const modal = document.querySelector(".modal-wrapper");

    //   modal.style.width = `${video.clientWidth}px`;
    //   modal.style.height = `${video.clientHeight}px`;
    // },
    targetChange(target) {
      if (target) {
        this.targetToggle = false;
      } else {
        this.targetToggle = true;
      }
    },
    sendMessage(ev) {
      console.log(ev);
      if (!ev.isComposing) {
        // Check if message is not empty
        if (this.newMessage.trim() !== "") {
          this.messages.push({
            user: "Me",
            text: this.newMessage.trim(),
          });
          this.socket.emit("message", this.messages);
          this.newMessage = "";
        }
      }
    },
  },
};
</script>

<style scoped>
/* 기본 설정 */
@import url("https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300&display=swap");
img {
  object-fit: contain;
  user-drag: none;
  -webkit-user-drag: none;
  user-select: none;
  -moz-user-select: none;
  -webkit-user-select: none;
  -ms-user-select: none;
}
div {
  box-sizing: border-box;
  color: white;
}
/* * {
  font-family: "Noto Sans KR", sans-serif;
} */
/* 컨테이너 크기 설정 */
#layout {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
}
.background-image {
  position: absolute;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.contents-container {
  position: relative;
  /* width: calc(100% - 4rem);
  height: calc(100% - 4rem); */
  width: 1448px;
  height: 881px;
  background: rgba(255, 255, 255, 0.224);
  border-radius: 1rem;
}
.team-info {
  position: absolute;
  bottom: 1rem;
  left: 1rem;
  width: 72rem;
  height: calc(881px - 43.5rem);
  border-radius: 1rem;
  background: #08133ac4;
  display: flex;
}
.team__container {
  width: 50%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.team__card {
  width: 75%;
  height: calc(100% - 2rem);
  background: rgba(56, 56, 79, 0.365);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: rgba(62, 133, 188, 0.8) 0px 1px 1px,
    rgba(62, 133, 188, 0.8) 0px 2px 2px, rgba(0, 0, 0, 0.07) 0px 4px 4px,
    rgba(0, 0, 0, 0.07) 0px 8px 8px, rgba(0, 0, 0, 0.07) 0px 16px 16px;
}
.team__playerInfo {
  width: 90%;
  height: 90%;
  background: rgba(17, 17, 33, 0.55);
  border-radius: 1rem;
  position: relative;
}
.playerInfo__name {
  font-size: 1rem;
  font-weight: 800;
  margin: 0.8rem;
}
.playerInfo__detail {
  width: calc(100% - 11.5rem);
  height: calc(100% - 3.5rem);
  margin-left: 0.8rem;
  background: rgba(58, 65, 123, 0.378);
  border-radius: 1rem;
  display: flex;
  align-items: center;
}
.playerInfo__detail--col {
  width: 60%;
  height: 90%;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}
.playerInfo__detailInfo {
  margin-left: 0.4rem;
  font-size: 0.8rem;
}
.playerInfo__icon {
  width: 4rem;
  height: 4rem;
}
.playerInfo__img {
  position: absolute;
  right: 0;
  bottom: 0;
  width: 10rem;
  height: 10rem;
}
.team__icon {
  width: 15%;
  height: 5rem;
  border-radius: 1rem;
  background: rgba(17, 17, 33, 0.55);
  margin: 0 1rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.team__icon--img {
  width: 2rem;
  height: 2rem;
}
.team__playerList {
  width: 100%;
  height: 100%;
  overflow-x: auto;
  white-space: nowrap;
  display: flex;
  align-items: center;
}
.playerList__player {
  width: 5.5rem;
  height: 8rem;
  background: rgba(17, 17, 33, 0.55);
  margin-left: 1rem;
  border-radius: 0.5rem;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  flex-shrink: 0; /* add this property to keep the width fixed */
}
.playerList__name {
  width: 100%;
  height: 10%;
  font-size: 0.9rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  justify-content: center;
  position: absolute;
  top: 4px;
}
.playerList__img {
  width: 100%;
  height: 90%;
  position: absolute;
  bottom: 0;
}
/* Customize the scrollbar background and thickness */
.team__playerList::-webkit-scrollbar {
  height: 8px; /* Adjust the thickness of the scrollbar */
}

.team__playerList::-webkit-scrollbar-track {
  background: rgba(
    255,
    255,
    255,
    0.1
  ); /* Set the background color of the scrollbar track */
}

.team__playerList::-webkit-scrollbar-thumb {
  background: rgba(
    255,
    255,
    255,
    0.3
  ); /* Set the background color of the scrollbar thumb */
  border-radius: 8px; /* Set the border radius of the scrollbar thumb */
}
.chat {
  position: absolute;
  right: 1rem;
  bottom: 1rem;
  width: calc(1448px - 75rem);
  height: calc(881px - 2rem);
  border-radius: 1rem;
  background: #08133ac4;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.chat__header {
  width: 100%;
  margin-top: 0.5rem;
  height: 3.5rem;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}
.chat__userInfo {
  width: 65%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.chat__invite {
  width: 3rem;
  height: 1.5rem;
  border-radius: 0.6rem;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #496adf;
}
.header__underLine {
  position: absolute;
  bottom: 0;
  width: 60%;
  height: 1.5px;
  background: #496adf;
}
.chat__content {
  width: 100%;
  height: calc(100% - 17rem);
  padding: 1rem;
  overflow-x: hidden;
  overflow-y: auto;
  direction: ltr;
}
/* Customize the scrollbar background and thickness */
.chat__content::-webkit-scrollbar {
  width: 8px; /* Adjust the thickness of the scrollbar */
}

.chat__content::-webkit-scrollbar-track {
  background: rgba(
    255,
    255,
    255,
    0.1
  ); /* Set the background color of the scrollbar track */
}

.chat__content::-webkit-scrollbar-thumb {
  background: rgba(
    255,
    255,
    255,
    0.3
  ); /* Set the background color of the scrollbar thumb */
  border-radius: 8px; /* Set the border radius of the scrollbar thumb */
}
.chat__userChat,
.chat__myChat {
  position: relative;
  box-sizing: border-box;
  min-height: 3rem;
  width: fit-content;
  max-width: 100%;
  padding: 0.5rem 0.8rem;
  border-radius: 6px 0 6px 0;
  background: rgba(100, 170, 0, 0.1);
  border: 2px solid rgba(100, 170, 0, 0.1);
  color: #fff;
  font-size: 0.9rem;
  line-height: 1.1rem;
  margin-bottom: 1.5rem;
}
.chat__myChat {
  margin: 0 0 0 auto;
  margin-bottom: 1.5rem;
}
.chat__userChat:after {
  content: "";
  position: absolute;
  border: 10px solid transparent;
  border-top: 10px solid rgba(100, 170, 0, 0.2);
  border-left: none;
  bottom: -22px;
  left: 10px;
}
.chat__myChat:after {
  content: "";
  position: absolute;
  border: 10px solid transparent;
  border-top: 10px solid rgba(100, 170, 0, 0.2);
  border-right: none;
  bottom: -22px;
  right: 10px;
}
.chat__userName {
  font-size: 1rem;
  color: #e76f51;
}
.chat__sendTarget {
  font-size: 1rem;
  color: #6e8bf4;
}
.chat__box {
  width: 90%;
  height: 12rem;
  background: rgba(56, 56, 79, 0.365);
  border-radius: 1rem;
  box-shadow: rgba(149, 149, 149, 0.24) 0px 3px 8px;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.chat__target {
  width: 90%;
  height: 2.5rem;
  display: flex;
  align-items: center;
}
.chat__targetText {
  cursor: pointer;
  width: 3.5rem;
  height: 70%;
  border-radius: 5px;
  display: flex;
  justify-content: center;
  align-items: center;
  background: rgba(38, 38, 53, 0.365);
  box-shadow: rgba(0, 0, 0, 0.12) 0px 1px 3px, rgba(0, 0, 0, 0.24) 0px 1px 2px;
}
.chat__targetText:last-child {
  margin-right: 0.5rem;
}
.select {
  background: #496adf;
}
.chat__input {
  width: 90%;
  height: 7rem;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.6);
  border-radius: 0.6rem;
}
.chat__text {
  resize: none;
  overflow: auto;
  min-height: 1rem;
  width: 90%;
  height: 90%;
  border: none;
  background: rgba(0, 0, 0, 0);
  font-size: 1rem;
  border-radius: 1rem;
}
.chat__text:focus {
  outline: none;
}
.chat__send {
  width: 90%;
  height: 2.5rem;
  display: flex;
  justify-content: flex-end;
  align-items: center;
}
.chat__submit {
  width: 3.5rem;
  height: 1.5rem;
  border-radius: 0.4rem;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #496adf;
}
.flag {
  cursor: pointer;
  width: 30px;
  height: 20px;
  object-fit: cover;
}
.icon {
  cursor: pointer;
  width: 1.25rem;
  height: 1.25rem;
  filter: invert(100%) sepia(0%) saturate(0%) hue-rotate(93deg) brightness(103%)
    contrast(103%);
}
.icon:hover {
  opacity: 0.6;
}
.icon-large {
  width: 1.75rem;
  height: 1.75rem;
}
.icon-large2 {
  width: 2rem;
  height: 2rem;
}
.rotate180 {
  transform: rotate(180deg);
}
.rotate360 {
  transform: rotate(360deg);
}
.open {
  width: 25%;
}
.openBtn__left {
  left: 25%;
}
.openBtn__right {
  right: 25%;
}
.open__show {
  display: flex;
}
.font__white {
  color: white;
}
.font__skyBlue {
  color: skyblue;
}
.font__purple {
  color: rgb(200, 20, 255);
}
.font__yellow {
  color: #f2ae00;
}
.hide {
  display: none;
}
</style>
