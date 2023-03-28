<template>
  <div id="layout" ref="fullLayout">
    <img class="background-image" src="@/assets/background.png" />
    <div class="contents-container">
      <!-- <Video @loadedmetadata="videoData"></Video> -->
      <VideoTest @loadedmetadata="videoData"></VideoTest>
      <div class="modal-wrapper">
        <div class="info-header">
          <router-link to="/">
            <div class="exit-button"></div>
          </router-link>
          <div class="match-winrate">
            <div class="match-info">
              <img
                class="icon"
                @click="leftArrowClick"
                src="@/assets/icons/left-arrow.png"
              />
              <span>{{ data_name }}</span>
              <span>{{ team1_name }}</span>
              <span>{{ team2_name }}</span>
              <img
                class="icon"
                @click="rightArrowClick"
                src="@/assets/icons/right-arrow.png"
              />
            </div>
            <div class="progress-bar__container">
              <div class="progress-bar">
                <span class="progress-bar__text">{{ team1_winrate }}</span>
              </div>
              <div class="progress-bar">
                <span class="progress-bar__text">{{ team2_winrate }}</span>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-content">
          <!-- <div
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
              <div class="teaminfo__name">이름</div>
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
              <div class="teaminfo__name">이름</div>
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
        <div
          class="playerinfo__modal"
          v-bind:class="{open__show: playerInfo_open}"
        >
          <div class="exit-button" @click="playerInfo__toggle"></div>
          <div class="playerinfo__profile">
            <div class="profile__column">
              <div class="profile__row">
                <img class="profile__img" src="" />
              </div>
              <div class="profile__row">
                <div class="profile__name"></div>
                <div class="profile__position"></div>
                <div class="profile__group"></div>
                <div class="profile__icon">
                  <img src="" />
                  <img src="" />
                </div>
                <div class="profile__birth"></div>
                <div class="profile__body"></div>
                <div class="profile__foot"></div>
              </div>
            </div>
            <div class="profile__column">
              <div class="profile__icons">
                <img src="" />
                <img src="" />
                <img src="" />
              </div>
              <div class="profile__icons">
                <img src="" />
                <img src="" />
                <img src="" />
              </div>
            </div>
          </div>
        </div> -->
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
                  <img
                    class="icon rotate180"
                    src="@/assets/icons/playrate.png"
                  />
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
                  <img
                    class="icon icon-large"
                    src="@/assets/icons/setting.png"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
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
          <div class="chat__userChat"></div>
          <div class="chat__myChat"></div>
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
            <input class="chat__text" type="text" />
          </div>
          <div class="chat__send">
            <div class="chat__submit">전송</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import Video from "@/components/Video.vue";
import VideoTest from "@/components/VideoTest.vue";
import {getMatchInfo} from "@/api/index";

export default {
  components: {
    // Video,
    VideoTest,
  },
  data() {
    return {
      playToggle: false,
      muteToggle: false,
      team1OpenToggle: false,
      team2OpenToggle: true,
      team1_open: false,
      team2_open: false,
      iconDesc_open: false,
      playerInfo_open: false,
      videoTimestamp: "00:00 / 00:00",
      data_name: "승리확률",
      team1_name: "아르헨티나",
      team2_name: "프랑스",
      team1_winrate: 38,
      team2_winrate: 62,
      team1: [],
      team2: [],
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
      class_color: {
        0: "font__white",
        1: "font__skyBlue",
        2: "font__purple",
        3: "font__yellow",
      },
      markingPlayer: [
        ["L. 메시", "H. 요리스"],
        ["S. 아궤로", "N. 캉테"],
        ["S. 아궤로", "N. 캉테"],
        ["S. 아궤로", "N. 캉테"],
        ["S. 아궤로", "N. 캉테"],
        ["S. 아궤로", "N. 캉테"],
        ["N. 오타멘디", "A. 그리즈만"],
        ["E. 바네가", "B. 마튀이디"],
        ["E. 바네가", "B. 마튀이디"],
        ["E. 바네가", "B. 마튀이디"],
        ["N. 탈리아피코", "O. 지루"],
        ["N. 탈리아피코", "O. 지루"],
        ["F. 파지오", "K. 음바페"],
        ["F. 파지오", "K. 음바페"],
        [],
      ],
      dataList: [
        {
          name: "승리 확률",
          team1__percent: 42,
          team2__percent: 58,
        },
        {
          name: "점유율",
          team1__percent: 60,
          team2__percent: 40,
        },
        {
          name: "볼 경합 성공률",
          team1__percent: 52,
          team2__percent: 48,
        },
      ],
      currentData: 0,
      targetToggle: false,
    };
  },
  async mounted() {
    const video = document.querySelector("Video");
    // console.dir(video);
    // console.log(video.clientWidth, video.clientHeight);

    video.addEventListener("ended", ev => {
      // console.log(ev);
      this.playToggle = false;
    });
    video.addEventListener("timeupdate", ev => {
      // console.log(Math.round(video.currentTime));
      // console.log(
      //   this.markingPlayer[Math.round(video.currentTime)][0],
      //   this.markingPlayer[Math.round(video.currentTime)][1],
      // );
      const teamInfo = document.getElementsByClassName("teaminfo__lineup");
      this.team1.forEach((ele, i) => {
        if (
          ele["name"] == this.markingPlayer[Math.round(video.currentTime)][0]
        ) {
          console.log(ele["name"], i);
          teamInfo[0].childNodes[0].childNodes.forEach(ele => {
            ele.style.background = "";
          });
          teamInfo[0].childNodes[0].childNodes[i + 1].style.background =
            "rgba(255, 255, 114, 0.450)";
        }
      });
      this.team2.forEach((ele, i) => {
        if (
          ele["name"] == this.markingPlayer[Math.round(video.currentTime)][1]
        ) {
          console.log(ele["name"], i);
          teamInfo[1].childNodes[0].childNodes.forEach(ele => {
            ele.style.background = "";
          });
          teamInfo[1].childNodes[0].childNodes[i + 1].style.background =
            "rgba(135, 207, 235, 0.494)";
        }
      });
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
    window.addEventListener("resize", this.stageResize);
    this.stageResize();
    document.addEventListener("keydown", this.keydownEvent);
    // document.body.style.width = "100vw";
    // document.body.style.height = "100vh";
    // document.body.style.cursor = "auto";
    // document.body.style.background = "black";
    // document.body.style.margin = "0";
    // document.body.style.padding = "0";

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
        birth: MatchInfo.data[0]["birth"][i],
        class: MatchInfo.data[0]["class"][i],
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
        birth: MatchInfo.data[1]["birth"][i],
        class: MatchInfo.data[1]["class"][i],
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

      const modal = document.querySelector(".modal-wrapper");

      modal.style.width = `${video.clientWidth}px`;
      modal.style.height = `${video.clientHeight}px`;
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
      ev.target.nextElementSibling.style.display = "flex";
    },
    closeDesc(ev) {
      ev.target.nextElementSibling.style.display = "none";
    },
    videoData(ev) {
      console.log(ev);
    },
    playerInfo__toggle() {
      this.playerInfo_open = false;
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
      console.log(this.team2);
      const profile = document.getElementsByClassName("profile__row");
      const icons = document.getElementsByClassName("profile__column");
      this.playerInfo_open = true;
      if (team == "team1") {
        profile[0].childNodes[0].src = require("@/assets/player/messi.png");
        profile[1].childNodes[3].childNodes[0].src = require("@/assets/flags/arg-flag.png");
        profile[1].childNodes[3].childNodes[1].src = require("@/assets/flags/바르셀로나.svg");
        icons[1].childNodes[0].childNodes[2].classList.remove("hide");
        icons[1].childNodes[1].childNodes[2].classList.remove("hide");
        icons[1].childNodes[0].childNodes[0].src = require("@/assets/playerIcons/주발 선호.png");
        icons[1].childNodes[0].childNodes[1].src = require("@/assets/playerIcons/중거리 슛 선호.png");
        icons[1].childNodes[0].childNodes[2].src = require("@/assets/playerIcons/아웃사이드 슈팅.크로스.png");
        icons[1].childNodes[1].childNodes[0].src = require("@/assets/playerIcons/테크니컬 드리블러.png");
        icons[1].childNodes[1].childNodes[1].src = require("@/assets/playerIcons/예리한 감아차기.png");
        icons[1].childNodes[1].childNodes[2].src = require("@/assets/playerIcons/플레이 메이커.png");
        for (let info in this.team1) {
          if (this.team1[info]["number"] == number) {
            profile[1].childNodes[0].classList.remove(
              "font__white",
              "font__skyBlue",
              "font__purple",
              "font__yellow",
            );
            profile[1].childNodes[0].classList.add(
              this.class_color[this.team1[info]["class"]],
            );
            profile[1].childNodes[0].innerText = this.team1[info]["name"];
            profile[1].childNodes[1].innerText =
              this.team1[info]["position"] +
              "(" +
              this.position_description[this.team1[info]["position"]] +
              ")";
            profile[1].childNodes[2].innerText =
              this.team1_name + " | " + this.team1[info]["club"];
            profile[1].childNodes[4].innerText =
              this.team1[info]["height"] +
              "cm" +
              " | " +
              this.team1[info]["weight"] +
              "kg";
            profile[1].childNodes[5].innerText =
              this.team1[info]["foot"] == "right" ? "오른발잡이" : "왼발잡이";
            profile[1].childNodes[6].innerText = this.team1[info]["birth"];
          }
        }
      } else if (team == "team2") {
        profile[0].childNodes[0].src = require("@/assets/player/tolisso.png");
        profile[1].childNodes[3].childNodes[0].src = require("@/assets/flags/fra-flag.png");
        profile[1].childNodes[3].childNodes[1].src = require("@/assets/flags/바이언.svg");
        icons[1].childNodes[0].childNodes[0].src = require("@/assets/playerIcons/긴 패스 선호.png");
        icons[1].childNodes[0].childNodes[1].src = require("@/assets/playerIcons/중거리 슛 선호.png");
        icons[1].childNodes[0].childNodes[2].classList.add("hide");
        icons[1].childNodes[1].childNodes[0].src = require("@/assets/playerIcons/파워 헤더.png");
        icons[1].childNodes[1].childNodes[1].src = require("@/assets/playerIcons/팀 플레이어.png");
        icons[1].childNodes[1].childNodes[2].classList.add("hide");
        for (let info in this.team2) {
          if (this.team2[info]["number"] == number) {
            profile[1].childNodes[0].classList.remove(
              "font__white",
              "font__skyBlue",
              "font__purple",
              "font__yellow",
            );
            profile[1].childNodes[0].classList.add(
              this.class_color[this.team2[info]["class"]],
            );
            profile[1].childNodes[0].innerText = this.team2[info]["name"];
            profile[1].childNodes[1].innerText =
              this.team2[info]["position"] +
              "(" +
              this.position_description[this.team2[info]["position"]] +
              ")";
            profile[1].childNodes[2].innerText =
              this.team2_name + " | " + this.team2[info]["club"];
            profile[1].childNodes[4].innerText =
              this.team2[info]["height"] +
              "cm" +
              " | " +
              this.team2[info]["weight"] +
              "kg";
            profile[1].childNodes[5].innerText =
              this.team2[info]["foot"] == "right" ? "오른발잡이" : "왼발잡이";
            profile[1].childNodes[6].innerText = this.team2[info]["birth"];
          }
        }
      }
    },
    leftArrowClick() {
      this.currentData -= 1;
      if (this.currentData == -1) {
        this.currentData = 2;
      }
      const progress = document.getElementsByClassName("progress-bar");

      this.data_name = this.dataList[this.currentData]["name"];
      this.team1_winrate = this.dataList[this.currentData]["team1__percent"];
      this.team2_winrate = this.dataList[this.currentData]["team2__percent"];
      progress[0].style.width =
        this.dataList[this.currentData]["team1__percent"] + "%";
      progress[1].style.width =
        this.dataList[this.currentData]["team2__percent"] + "%";
    },
    rightArrowClick() {
      this.currentData += 1;
      if (this.currentData == 3) {
        this.currentData = 0;
      }
      const progress = document.getElementsByClassName("progress-bar");

      this.data_name = this.dataList[this.currentData]["name"];
      this.team1_winrate = this.dataList[this.currentData]["team1__percent"];
      this.team2_winrate = this.dataList[this.currentData]["team2__percent"];
      progress[0].style.width =
        this.dataList[this.currentData]["team1__percent"] + "%";
      progress[1].style.width =
        this.dataList[this.currentData]["team2__percent"] + "%";
    },
    targetChange(target) {
      if (target) {
        this.targetToggle = false;
      } else {
        this.targetToggle = true;
      }
    },
  },
  filters: {
    matchingDesc(iconName, description) {
      // console.log(iconName);
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
.modal-wrapper {
  position: absolute;
  left: 1rem;
  top: 1rem;
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
  cursor: pointer;
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  left: 1rem;
  top: 2rem;
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
.match-info span:nth-child(3) {
  position: absolute;
  left: 5px;
  font-size: 0.8rem;
}
.match-info span:nth-child(4) {
  position: absolute;
  right: 5px;
  font-size: 0.8rem;
}
.match-info img {
  width: 15px;
  height: 15px;
  margin: 0 10px;
  object-fit: contain;
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
  transition: all 0.5s;
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
  width: 42%;
  background-color: #e76f51;
  left: 0;
}
.progress-bar:nth-child(2) {
  width: 58%;
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
}
.playerInfo__detailInfo {
  font-size: 0.9rem;
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
.select {
  background: #496adf;
}
.chat__input {
  width: 90%;
  height: 7rem;
}
.chat__text {
  width: 95%;
  height: 90%;
  border-radius: 6px;
  border: none;
  vertical-align: text-top;
  background: rgba(255, 255, 255, 0.6);
}
.chat__text:focus {
  outline: none;
}
.chat__send {
  width: 90%;
  height: 2.5rem;
  display: flex;
  justify-content: flex-end;
}
.chat__submit {
  width: 4rem;
  height: 2rem;
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
