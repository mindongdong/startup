<template>
  <div id="layout">
    <Video @loadedmetadata="videoData"></Video>
    <div id="modal-wrapper">
      <div class="info-header">
        <router-link to="/">
          <div class="exit-button"></div>
        </router-link>
        <div class="match-winrate">
          <div class="match-info">
            <span>승리확률</span>
            <span>{{ this.team1_name }}</span>
            <span>{{ this.team2_name }}</span>
          </div>
          <div class="progress-bar__container">
            <div class="progress-bar">
              <span class="progress-bar__text">{{ this.team1_winrate }}</span>
            </div>
            <div class="progress-bar">
              <span class="progress-bar__text">{{ this.team2_winrate }}</span>
            </div>
          </div>
        </div>
      </div>
      <div class="modal-content">
        <div
          class="teaminfo-modal left"
          v-bind:class="{openBtn__left: team1_open}"
        >
          <div class="open-button" @click="openTeam1Modal">
            <div class="team-icon">
              <img class="flag" src="@/assets/flags/arg-flag.png" />
            </div>
            <div class="open-icon">
              <img
                class="icon"
                v-bind:class="{rotate180: team1_open}"
                src="@/assets/icons/right-double-arrow.png"
              />
            </div>
          </div>
        </div>
        <div
          class="teaminfo-modal right"
          v-bind:class="{openBtn__right: team2_open}"
        >
          <div class="open-button" @click="openTeam2Modal">
            <div class="open-icon">
              <img
                class="icon rotate180"
                v-bind:class="{rotate360: team2_open}"
                src="@/assets/icons/right-double-arrow.png"
              />
            </div>
            <div class="team-icon">
              <img class="flag" src="@/assets/flags/fra-flag.png" />
            </div>
          </div>
        </div>
        <div class="teaminfo__lineup left" v-bind:class="{open: team1_open}">
          <ul class="teaminfo__player" v-bind:class="{open__show: team1_open}">
            <li class="teaminfo__column">
              <div class="teaminfo__number">번호</div>
              <div class="teaminfo__name">선수</div>
              <div class="teaminfo__position">포지션</div>
              <div class="teaminfo__icon">특성</div>
            </li>
            <li
              class="teaminfo__column"
              v-for="(player, idx) in team1"
              :key="idx"
              @click="clickPlayer"
            >
              <div class="teaminfo__number">{{ player.number }}</div>
              <div class="teaminfo__name">{{ player.name }}</div>
              <div class="teaminfo__position">{{ player.position }}</div>
              <div class="teaminfo__icon">
                <img
                  class="teaminfo__iconImg"
                  @mouseover="openDesc"
                  @mouseleave="closeDesc"
                  :src="
                    require('@/assets/playerIcons/' +
                      `${player.icon1}` +
                      '.png')
                  "
                />
                <div class="teaminfo__iconDesc">
                  {{ player.icon1 | matchingDesc(icon_description) }}
                </div>
              </div>
            </li>
          </ul>
        </div>
        <div class="teaminfo__lineup right" v-bind:class="{open: team2_open}">
          <ul class="teaminfo__player" v-bind:class="{open__show: team2_open}">
            <li class="teaminfo__column">
              <div class="teaminfo__number">번호</div>
              <div class="teaminfo__name">선수</div>
              <div class="teaminfo__position">포지션</div>
              <div class="teaminfo__icon">특성</div>
            </li>
            <li
              class="teaminfo__column"
              v-for="(player, idx) in team2"
              :key="idx"
              @click="clickPlayer"
            >
              <div class="teaminfo__number">{{ player.number }}</div>
              <div class="teaminfo__name">{{ player.name }}</div>
              <div class="teaminfo__position">{{ player.position }}</div>
              <div class="teaminfo__icon">
                <img
                  class="teaminfo__iconImg"
                  @mouseover="openDesc"
                  @mouseleave="closeDesc"
                  :src="
                    require('@/assets/playerIcons/' +
                      `${player.icon1}` +
                      '.png')
                  "
                />
                <div class="teaminfo__iconDesc">
                  {{ player.icon1 | matchingDesc(icon_description) }}
                </div>
              </div>
            </li>
          </ul>
        </div>
        <div class="playerinfo__modal">
          <div class="playerinfo__profile">
            <div class="profile__row">
              <img class="profile__img" src="" />
            </div>
            <div class="profile__row">
              <div class="profile__name"></div>
              <div class="profile__team"></div>
              <div class="profile__national"></div>
              <div class="profile__position"></div>
            </div>
          </div>
        </div>
      </div>
      <div class="video-control">
        <div class="video-progress"></div>
        <div class="video-tools">
          <div class="video-tools__column">
            <div class="button-wrapper">
              <div class="play-button" @click="videoPlay">
                <img
                  class="icon"
                  v-if="this.playToggle"
                  src="@/assets/icons/pause.png"
                />
                <img class="icon" v-else src="@/assets/icons/play.png" />
              </div>
            </div>
            <div class="button-wrapper">
              <div class="playrate-button">
                <img class="icon rotate180" src="@/assets/icons/playrate.png" />
              </div>
            </div>
            <div class="button-wrapper">
              <div class="sound-button" @click="soundMute">
                <img
                  class="icon"
                  v-if="muteToggle"
                  src="@/assets/icons/mute.png"
                />
                <img class="icon" v-else src="@/assets/icons/sound.png" />
              </div>
            </div>
          </div>
          <div class="video-tools__column">
            <div class="timestamp">
              {{ videoTimestamp }}
            </div>
          </div>
          <div class="video-tools__column">
            <div class="button-wrapper">
              <div class="fullscreen-button">
                <img
                  class="icon icon-large2"
                  src="@/assets/icons/full-screen.png"
                />
              </div>
            </div>
            <div class="button-wrapper">
              <div class="setting-button">
                <img class="icon icon-large" src="@/assets/icons/setting.png" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Video from "@/components/Video.vue";
import {getMatchInfo} from "@/api/index";

export default {
  components: {
    Video,
  },
  data() {
    return {
      playToggle: false,
      muteToggle: false,
      team1OpenToggle: false,
      team2OpenToggle: true,
      videoTimestamp: "00:00 / 00:00",
      team1_name: "아르헨티나",
      team2_name: "프랑스",
      team1_winrate: 38,
      team2_winrate: 62,
      team1: [],
      team2: [],
      team1_open: false,
      team2_open: false,
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
      iconDesc_open: false,
    };
  },
  async mounted() {
    console.log(this.icon_description["승부욕"]);
    const video = document.querySelector("Video");
    // console.dir(video);
    // console.log(video.clientWidth, video.clientHeight);
    video.addEventListener("ended", ev => {
      // console.log(ev);
      this.playToggle = false;
    });
    video.addEventListener("timeupdate", ev => {
      // console.log(video.duration, video.currentTime);
      if (Math.round(video.currentTime) < 10) {
        this.videoTimestamp = `00:0${Math.round(
          video.currentTime,
        )} / 00:${Math.round(video.duration)}`;
      } else {
        this.videoTimestamp = `00:${Math.round(
          video.currentTime,
        )} / 00:${Math.round(video.duration)}`;
      }
    });
    // console.log(video.duration);
    this.stageResize();
    video.addEventListener("resize", this.stageResize);
    window.addEventListener("resize", this.stageResize);
    document.addEventListener("keydown", this.keydownEvent);
    document.body.style.width = "100vw";
    document.body.style.height = "100vh";
    document.body.style.cursor = "auto";
    document.body.style.background = "black";
    document.body.style.margin = "0";
    document.body.style.padding = "0";

    const match = {match_name: "ARG.FRA"};
    const MatchInfo = await getMatchInfo(match);
    console.log(MatchInfo.data[0]);

    for (let i = 0; i < Object.keys(MatchInfo.data[0]["number"]).length; i++) {
      this.team1.push({
        number: MatchInfo.data[0]["number"][i],
        name: MatchInfo.data[0]["name"][i],
        position: MatchInfo.data[0]["position"][i],
        height: MatchInfo.data[0]["height"][i],
        weight: MatchInfo.data[0]["weight"][i],
        club: MatchInfo.data[0]["club"][i],
        foot: MatchInfo.data[0]["foot"][i],
        icon1: MatchInfo.data[0]["특성1"][i],
        icon2: MatchInfo.data[0]["특성2"][i],
        icon3: MatchInfo.data[0]["특성3"][i],
        icon4: MatchInfo.data[0]["특성4"][i],
        icon5: MatchInfo.data[0]["특성5"][i],
        icon6: MatchInfo.data[0]["특성6"][i],
        icon7: MatchInfo.data[0]["특성7"][i],
      });
    }
    for (let i = 0; i < Object.keys(MatchInfo.data[1]["number"]).length; i++) {
      this.team2.push({
        number: MatchInfo.data[1]["number"][i],
        name: MatchInfo.data[1]["name"][i],
        position: MatchInfo.data[1]["position"][i],
        height: MatchInfo.data[1]["height"][i],
        weight: MatchInfo.data[1]["weight"][i],
        club: MatchInfo.data[1]["club"][i],
        foot: MatchInfo.data[1]["foot"][i],
        icon1: MatchInfo.data[1]["특성1"][i],
        icon2: MatchInfo.data[1]["특성2"][i],
        icon3: MatchInfo.data[1]["특성3"][i],
        icon4: MatchInfo.data[1]["특성4"][i],
        icon5: MatchInfo.data[1]["특성5"][i],
        icon6: MatchInfo.data[1]["특성6"][i],
        icon7: MatchInfo.data[1]["특성7"][i],
      });
    }
  },
  methods: {
    stageResize() {
      const video = document.querySelector("Video");
      // console.log(video.clientWidth, video.clientHeight);
      // console.dir(video);

      const modal = document.getElementById("modal-wrapper");
      // console.log(modal);

      modal.style.width = `${video.clientWidth}px`;
      modal.style.height = `${video.clientHeight}px`;

      const layout = document.getElementById("layout");
      const posY = (layout.clientHeight - video.clientHeight) / 2;
      const posX = (layout.clientWidth - video.clientWidth) / 2;
      modal.style.top = `${posY}px`;
      modal.style.left = `${posX}px`;
      // console.log(posY, posX);
    },
    videoPlay() {
      const video = document.querySelector("Video");
      this.playToggle = !this.playToggle;
      // console.log(video.paused, this.playToggle);

      if (video.paused) {
        video.play();
      } else {
        video.pause();
      }
    },
    soundMute() {
      this.muteToggle = !this.muteToggle;
      const video = document.querySelector("Video");
      video.muted = this.muteToggle;
    },
    keydownEvent(ev) {
      // console.log(ev.keyCode);
      if (ev.keyCode === 32) {
        this.videoPlay();
      }
    },
    openTeam1Modal() {
      this.team1_open = !this.team1_open;
    },
    openTeam2Modal() {
      this.team2_open = !this.team2_open;
    },
    openDesc(ev) {
      console.dir(ev.target.nextElementSibling);
      ev.target.nextElementSibling.style.display = "flex";
    },
    closeDesc(ev) {
      ev.target.nextElementSibling.style.display = "none";
    },
    videoData(ev) {
      console.log(ev);
    },
    clickPlayer(ev) {
      console.log(ev);
      const str = ev.target.parentNode.innerText;
      const regex = /[^0-9]/g;
      const result = str.replace(regex, "");
      const number = parseInt(result);
      console.log(number);
      const team = window.innerWidth / 2 >= ev.clientX ? "team1" : "team2";
      console.log(team);

      const profile = document.getElementsByClassName("profile__row");
      console.dir(profile[1].childNodes);
    },
  },
  filters: {
    matchingDesc(iconName, description) {
      console.log(iconName);
      const desc = description[iconName];
      return desc;
    },
  },
};
</script>

<style scoped>
/* 기본 설정 */
@import url("https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300&display=swap");
img {
  object-fit: cover;
}
div {
  box-sizing: border-box;
}
/* * {
  font-family: "Noto Sans KR", sans-serif;
} */
/* 컨테이너 크기 설정 */
#layout {
  position: relative;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}
#layout > div {
  max-width: 100vw;
  max-height: 100vh;
}
#modal-wrapper {
  position: absolute;
  left: 0;
  top: 0;
}
.left {
  left: 0;
}
.right {
  right: 0;
}
/* 상단 모달 설정 */
.info-header {
  position: relative;
  width: 100%;
  height: 20%;
}
/* 메인으로 나가는 버튼 */
.exit-button {
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  left: 10px;
  top: 25px;
  width: 30px;
  height: 30px;
  border-radius: 15px;
  background: rgba(0, 0, 0, 0.6);
}
.exit-button:after {
  position: relative;
  top: 2px;
  content: "\00d7";
  font-size: 30px;
  font-weight: 100;
  color: white;
}
/* 승률 모달 */
.match-winrate {
  width: 400px;
  height: 81px;
  position: absolute;
  top: 10px;
  right: 10px;
  background: rgba(0, 0, 0, 0.6);
  padding: 10px;
  border-radius: 1rem;
}
.match-info {
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}
.match-info span {
  color: white;
  font-size: 1rem;
}
.match-info span:nth-child(2) {
  position: absolute;
  left: 5px;
  font-size: 0.8rem;
}
.match-info span:nth-child(3) {
  position: absolute;
  right: 5px;
  font-size: 0.8rem;
}
.progress-bar__container {
  width: 100%;
  height: 2rem;
  border-radius: 2rem;
  overflow: hidden;
  transition: all 0.5s;
  will-change: transform;
  box-shadow: 0 0 5px hsla(0, 0%, 100%, 0.615);
  position: relative;
  margin-top: 10px;
}
.progress-bar {
  position: absolute;
  height: 100%;
  content: "";
  border-radius: inherit;
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  font-family: sans-serif;
}
.progress-bar:first-child {
  width: 38%;
  background-color: #e76f51;
  left: 0;
}
.progress-bar:nth-child(2) {
  width: 62%;
  background-color: #496adf;
  right: 0;
}
/* 중앙 모달 설정 */
.modal-content {
  width: 100%;
  height: 60%;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
}
/* 팀 정보 모달 */
.teaminfo-modal {
  position: absolute;
  top: 40%;
  width: 80px;
  height: 50px;
  display: flex;
  align-items: center;
  transition: all 0.5s ease;
}
.open-button {
  width: 100%;
  height: 100%;
  border-radius: 1rem;
  display: flex;
  align-items: center;
  justify-content: space-evenly;
  background: rgba(0, 0, 0, 0.5);
}
.teaminfo__lineup {
  transition: all 0.5s ease;
  display: flex;
  flex-direction: column;
  justify-content: center;
  position: absolute;
  overflow-x: hidden;
  width: 0;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  border-radius: 5%;
}
.teaminfo__player {
  display: none;
  width: 100%;
  height: 100%;
  flex-direction: column;
  align-items: center;
  justify-content: space-evenly;
}
.teaminfo__column {
  width: 90%;
  height: 6%;
  display: flex;
  align-items: center;
  justify-content: space-evenly;
  border-bottom: 0.5px solid rgba(125, 125, 125, 0.2);
  position: relative;
}

.teaminfo__column:hover {
  background: rgba(181, 181, 181, 0.5);
}

.teaminfo__column:first-child:hover {
  background: rgba(0, 0, 0, 0);
}

.teaminfo__column:first-child {
  opacity: 0.6;
}

.teaminfo__number,
.teaminfo__name,
.teaminfo__position,
.teaminfo__icon {
  color: white;
  display: flex;
  align-items: center;
  font-size: 90%;
  padding: 1%;
  height: 100%;
}
.teaminfo__number {
  width: 20%;
}
.teaminfo__name {
  width: 40%;
}
.teaminfo__position {
  width: 20%;
}
.teaminfo__icon {
  width: 20%;
  justify-content: center;
}
.teaminfo__iconImg {
  width: 100%;
  height: 100%;
  object-fit: contain;
}
.teaminfo__iconDesc {
  background: rgba(255, 255, 255, 0.616);
  color: black;
  box-shadow: 0 0 5px hsla(0, 0%, 41%, 0.615);
  font-size: 80%;
  text-align: center;
  align-items: center;
  justify-content: center;
  width: 70%;
  height: 70%;
  border-radius: 10px;
  position: absolute;
  right: 0;
  bottom: 100%;
  display: none;
}
.playerinfo__modal {
  display: none;
  width: 35%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  border-radius: 30px;
  z-index: 9998;
}
.playerinfo__profile {
  width: 100%;
  height: 50%;
}
.profile__row {
  width: 50%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.profile__img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}
.profile__name {
  width: 100%;
  height: 40%;
}
.profile__team {
  width: 100%;
  height: 20%;
}
.profile__national {
  width: 100%;
  height: 20%;
}
.profile__position {
  width: 100%;
  height: 20%;
}
/* 하단 비디오 컨트롤러 설정 */
.video-control {
  width: 100%;
  height: 20%;
}
.video-progress {
  width: 100%;
  height: 50%;
}
/* 비디오 컨트롤 아이콘 */
.video-tools {
  width: 100%;
  height: 50%;
  position: relative;
  padding: 10px 32px;
  display: flex;
  align-items: flex-end;
}
.video-tools__column {
  width: 115px;
  height: 27px;
  display: flex;
  align-items: center;
  padding: 0 5px;
}
.video-tools__column:first-child {
  box-sizing: initial;
  padding-right: 10px;
  border-right: 1px solid hsla(0, 0%, 100%, 0.5);
}
.video-tools__column:nth-child(2) {
  margin-left: 20px;
}
.video-tools__column:nth-child(3) {
  position: absolute;
  right: 10px;
}
.timestamp {
  color: white;
  text-align: center;
  font-size: 1rem;
}
.button-wrapper {
  position: relative;
  margin-right: 20px;
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
</style>
