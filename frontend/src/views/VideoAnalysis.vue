<template>
  <div id="layout">
    <img class="background-image" src="@/assets/background.png" />
    <div class="contents-container">
      <div class="view-mode">
        <div
          class="view-mode__info"
          @click="infoToggle = !infoToggle"
          v-bind:class="{ yellow: !infoToggle }"
        ></div>
        <div
          class="view-mode__info"
          @click="infoToggle = !infoToggle"
          v-bind:class="{ yellow: infoToggle }"
        ></div>
        <div
          class="view-mode__chat"
          @click="chatToggle = !chatToggle"
          v-bind:class="{ blue: !chatToggle }"
        ></div>
        <div
          class="view-mode__chat"
          @click="chatToggle = !chatToggle"
          v-bind:class="{ blue: chatToggle }"
        ></div>
      </div>
      <Video></Video>
      <div class="team-info" v-bind:class="{ hide__bottom: infoToggle }">
        <div class="team-selector">
          <div
            class="team__icon"
            @click="
              detailToggle = false;
              teamHome = true;
            "
          >
            <p class="team__icon--name">아르헨티나</p>
            <img class="team__icon--img" src="@/assets/flags/arg-flag.png" />
          </div>
          <div
            class="team__icon"
            @click="
              detailToggle = false;
              teamHome = false;
            "
          >
            <p class="team__icon--name">프랑스</p>
            <img class="team__icon--img" src="@/assets/flags/fra-flag.png" />
          </div>
        </div>
        <div class="team__card" v-if="detailToggle">
          <div class="team__playerInfo" v-if="teamHome && detailIndex == 0">
            <p class="playerInfo__name">E. 마르티네스 (E. Martinez)</p>
            <div class="playerInfo__detail">
              <div class="playerInfo__detail--col">
                <p class="playerInfo__detailInfo">아스톤 빌라(Aston Villa)</p>
                <p class="playerInfo__detailInfo">아르헨티나</p>
                <p class="playerInfo__detailInfo">1992년 9월 2일</p>
                <p class="playerInfo__detailInfo">골키퍼(GK)</p>
              </div>
              <img
                class="playerInfo__icon"
                src="@/assets/playerIcons/스피드 드리블러.png"
              />
            </div>
            <img class="playerInfo__img" src="@/assets/player/arg_0.png" />
          </div>
          <div
            class="team__playerInfo"
            v-else-if="teamHome && detailIndex == 1"
          >
            <p class="playerInfo__name">N. 타글리아피코 (N. Tagliafico)</p>
            <div class="playerInfo__detail">
              <div class="playerInfo__detail--col">
                <p class="playerInfo__detailInfo">Ajax</p>
                <p class="playerInfo__detailInfo">아르헨티나</p>
                <p class="playerInfo__detailInfo">1992년 8월 31일</p>
                <p class="playerInfo__detailInfo">왼쪽 풀백(LB)</p>
              </div>
              <img
                class="playerInfo__icon"
                src="@/assets/playerIcons/스피드 드리블러.png"
              />
            </div>
            <img class="playerInfo__img" src="@/assets/player/arg_1.png" />
          </div>
          <div
            class="team__playerInfo"
            v-else-if="teamHome && detailIndex == 2"
          >
            <p class="playerInfo__name">N. 오타멘디 (N. Otamendi)</p>
            <div class="playerInfo__detail">
              <div class="playerInfo__detail--col">
                <p class="playerInfo__detailInfo">Benfica</p>
                <p class="playerInfo__detailInfo">아르헨티나</p>
                <p class="playerInfo__detailInfo">1988년 2월 12일</p>
                <p class="playerInfo__detailInfo">센터백(CB)</p>
              </div>
              <img
                class="playerInfo__icon"
                src="@/assets/playerIcons/스피드 드리블러.png"
              />
            </div>
            <img class="playerInfo__img" src="@/assets/player/arg_2.png" />
          </div>
          <div
            class="team__playerInfo"
            v-else-if="teamHome && detailIndex == 3"
          >
            <p class="playerInfo__name">C. 로메로 (C. Romero)</p>
            <div class="playerInfo__detail">
              <div class="playerInfo__detail--col">
                <p class="playerInfo__detailInfo">Tottenham Hotspur</p>
                <p class="playerInfo__detailInfo">아르헨티나</p>
                <p class="playerInfo__detailInfo">1998년 4월 27일</p>
                <p class="playerInfo__detailInfo">센터백(CB)</p>
              </div>
              <img
                class="playerInfo__icon"
                src="@/assets/playerIcons/스피드 드리블러.png"
              />
            </div>
            <img class="playerInfo__img" src="@/assets/player/arg_3.png" />
          </div>
          <div
            class="team__playerInfo"
            v-else-if="teamHome && detailIndex == 4"
          >
            <p class="playerInfo__name">N. 몰리나 (N. Molina)</p>
            <div class="playerInfo__detail">
              <div class="playerInfo__detail--col">
                <p class="playerInfo__detailInfo">Udinese</p>
                <p class="playerInfo__detailInfo">아르헨티나</p>
                <p class="playerInfo__detailInfo">1998년 7월 4일</p>
                <p class="playerInfo__detailInfo">오른쪽 풀백(RB)</p>
              </div>
              <img
                class="playerInfo__icon"
                src="@/assets/playerIcons/스피드 드리블러.png"
              />
            </div>
            <img class="playerInfo__img" src="@/assets/player/arg_4.png" />
          </div>
          <div
            class="team__playerInfo"
            v-else-if="teamHome && detailIndex == 5"
          >
            <p class="playerInfo__name">A. 막알리스테르 (A. Mac Allister)</p>
            <div class="playerInfo__detail">
              <div class="playerInfo__detail--col">
                <p class="playerInfo__detailInfo">Brighton & Hove Albion</p>
                <p class="playerInfo__detailInfo">아르헨티나</p>
                <p class="playerInfo__detailInfo">1999년 12월 24일</p>
                <p class="playerInfo__detailInfo">미드필더(MF)</p>
              </div>
              <img
                class="playerInfo__icon"
                src="@/assets/playerIcons/스피드 드리블러.png"
              />
            </div>
            <img class="playerInfo__img" src="@/assets/player/arg_5.png" />
          </div>
          <div
            class="team__playerInfo"
            v-else-if="teamHome && detailIndex == 6"
          >
            <p class="playerInfo__name">E. 페르난데스 (E. Fernández)</p>
            <div class="playerInfo__detail">
              <div class="playerInfo__detail--col">
                <p class="playerInfo__detailInfo">Defensa y Justicia</p>
                <p class="playerInfo__detailInfo">아르헨티나</p>
                <p class="playerInfo__detailInfo">2000년 3월 12일</p>
                <p class="playerInfo__detailInfo">미드필더(MF)</p>
              </div>
              <img
                class="playerInfo__icon"
                src="@/assets/playerIcons/스피드 드리블러.png"
              />
            </div>
            <img class="playerInfo__img" src="@/assets/player/arg_6.png" />
          </div>
          <div
            class="team__playerInfo"
            v-else-if="teamHome && detailIndex == 7"
          >
            <p class="playerInfo__name">R. 데 파울 (R. De Paul)</p>
            <div class="playerInfo__detail">
              <div class="playerInfo__detail--col">
                <p class="playerInfo__detailInfo">Atlético Madrid</p>
                <p class="playerInfo__detailInfo">아르헨티나</p>
                <p class="playerInfo__detailInfo">1994년 5월 24일</p>
                <p class="playerInfo__detailInfo">미드필더(MF)</p>
              </div>
              <img
                class="playerInfo__icon"
                src="@/assets/playerIcons/스피드 드리블러.png"
              />
            </div>
            <img class="playerInfo__img" src="@/assets/player/arg_7.png" />
          </div>
          <div
            class="team__playerInfo"
            v-else-if="teamHome && detailIndex == 8"
          >
            <p class="playerInfo__name">A. 디 마리아 (A. Di Maria)</p>
            <div class="playerInfo__detail">
              <div class="playerInfo__detail--col">
                <p class="playerInfo__detailInfo">Paris Saint-Germain</p>
                <p class="playerInfo__detailInfo">아르헨티나</p>
                <p class="playerInfo__detailInfo">1988년 2월 14일</p>
                <p class="playerInfo__detailInfo">미드필더(MF)</p>
              </div>
              <img
                class="playerInfo__icon"
                src="@/assets/playerIcons/스피드 드리블러.png"
              />
            </div>
            <img class="playerInfo__img" src="@/assets/player/arg_8.png" />
          </div>
          <div
            class="team__playerInfo"
            v-else-if="teamHome && detailIndex == 9"
          >
            <p class="playerInfo__name">J. 알바레스 (J. Alvarez)</p>
            <div class="playerInfo__detail">
              <div class="playerInfo__detail--col">
                <p class="playerInfo__detailInfo">River Plate</p>
                <p class="playerInfo__detailInfo">아르헨티나</p>
                <p class="playerInfo__detailInfo">2000년 7월 28일</p>
                <p class="playerInfo__detailInfo">스트라이커(ST)</p>
              </div>
              <img
                class="playerInfo__icon"
                src="@/assets/playerIcons/스피드 드리블러.png"
              />
            </div>
            <img class="playerInfo__img" src="@/assets/player/arg_9.png" />
          </div>
          <div
            class="team__playerInfo"
            v-else-if="teamHome && detailIndex == 10"
          >
            <p class="playerInfo__name">L. 메시 (L. Messi)</p>
            <div class="playerInfo__detail">
              <div class="playerInfo__detail--col">
                <p class="playerInfo__detailInfo">Paris Saint-Germain</p>
                <p class="playerInfo__detailInfo">아르헨티나</p>
                <p class="playerInfo__detailInfo">1987년 6월 24일</p>
                <p class="playerInfo__detailInfo">스트라이커(ST)</p>
              </div>
              <img
                class="playerInfo__icon"
                src="@/assets/playerIcons/스피드 드리블러.png"
              />
            </div>
            <img class="playerInfo__img" src="@/assets/player/arg_10.png" />
          </div>
          <div class="team__playerInfo" v-else-if="detailIndex == 0">
            <p class="playerInfo__name">H. 요리스 (H. Lloris)</p>
            <div class="playerInfo__detail">
              <div class="playerInfo__detail--col">
                <p class="playerInfo__detailInfo">Tottenham Hotspur</p>
                <p class="playerInfo__detailInfo">프랑스</p>
                <p class="playerInfo__detailInfo">1986년 12월 26일</p>
                <p class="playerInfo__detailInfo">골키퍼(GK)</p>
              </div>
              <img
                class="playerInfo__icon"
                src="@/assets/playerIcons/스피드 드리블러.png"
              />
            </div>
            <img class="playerInfo__img" src="@/assets/player/fr_0.png" />
          </div>
          <div class="team__playerInfo" v-else-if="detailIndex == 1">
            <p class="playerInfo__name">J. 쿤데 (J. Koundé)</p>
            <div class="playerInfo__detail">
              <div class="playerInfo__detail--col">
                <p class="playerInfo__detailInfo">Sevilla FC</p>
                <p class="playerInfo__detailInfo">프랑스</p>
                <p class="playerInfo__detailInfo">1998년 11월 12일</p>
                <p class="playerInfo__detailInfo">센터백(CB)</p>
              </div>
              <img
                class="playerInfo__icon"
                src="@/assets/playerIcons/스피드 드리블러.png"
              />
            </div>
            <img class="playerInfo__img" src="@/assets/player/fr_1.png" />
          </div>
          <div class="team__playerInfo" v-else-if="detailIndex == 2">
            <p class="playerInfo__name">R. 바란 (R. Varane)</p>
            <div class="playerInfo__detail">
              <div class="playerInfo__detail--col">
                <p class="playerInfo__detailInfo">Manchester United</p>
                <p class="playerInfo__detailInfo">프랑스</p>
                <p class="playerInfo__detailInfo">1993년 4월 25일</p>
                <p class="playerInfo__detailInfo">센터백(CB)</p>
              </div>
              <img
                class="playerInfo__icon"
                src="@/assets/playerIcons/스피드 드리블러.png"
              />
            </div>
            <img class="playerInfo__img" src="@/assets/player/fr_2.png" />
          </div>
          <div class="team__playerInfo" v-else-if="detailIndex == 3">
            <p class="playerInfo__name">D. 우파메카노 (D. Upamecano)</p>
            <div class="playerInfo__detail">
              <div class="playerInfo__detail--col">
                <p class="playerInfo__detailInfo">Bayern Munich</p>
                <p class="playerInfo__detailInfo">프랑스</p>
                <p class="playerInfo__detailInfo">1998년 10월 27일</p>
                <p class="playerInfo__detailInfo">센터백(CB)</p>
              </div>
              <img
                class="playerInfo__icon"
                src="@/assets/playerIcons/스피드 드리블러.png"
              />
            </div>
            <img class="playerInfo__img" src="@/assets/player/fr_3.png" />
          </div>
          <div class="team__playerInfo" v-else-if="detailIndex == 4">
            <p class="playerInfo__name">T. 에르난데스 (T. Hernandez)</p>
            <div class="playerInfo__detail">
              <div class="playerInfo__detail--col">
                <p class="playerInfo__detailInfo">AC Milan</p>
                <p class="playerInfo__detailInfo">프랑스</p>
                <p class="playerInfo__detailInfo">1997년 10월 29일</p>
                <p class="playerInfo__detailInfo">왼쪽 풀백(LB)</p>
              </div>
              <img
                class="playerInfo__icon"
                src="@/assets/playerIcons/스피드 드리블러.png"
              />
            </div>
            <img class="playerInfo__img" src="@/assets/player/fr_4.png" />
          </div>
          <div class="team__playerInfo" v-else-if="detailIndex == 5">
            <p class="playerInfo__name">A. 추아메니 (A. Tchouaméni)</p>
            <div class="playerInfo__detail">
              <div class="playerInfo__detail--col">
                <p class="playerInfo__detailInfo">AS Monaco</p>
                <p class="playerInfo__detailInfo">프랑스</p>
                <p class="playerInfo__detailInfo">2000년 1월 27일</p>
                <p class="playerInfo__detailInfo">미드필더(MF)</p>
              </div>
              <img
                class="playerInfo__icon"
                src="@/assets/playerIcons/스피드 드리블러.png"
              />
            </div>
            <img class="playerInfo__img" src="@/assets/player/fr_5.png" />
          </div>
          <div class="team__playerInfo" v-else-if="detailIndex == 6">
            <p class="playerInfo__name">A. 라비오 (A. Rabiot)</p>
            <div class="playerInfo__detail">
              <div class="playerInfo__detail--col">
                <p class="playerInfo__detailInfo">Juventus</p>
                <p class="playerInfo__detailInfo">프랑스</p>
                <p class="playerInfo__detailInfo">1995년 4월 3일</p>
                <p class="playerInfo__detailInfo">미드필더(MF)</p>
              </div>
              <img
                class="playerInfo__icon"
                src="@/assets/playerIcons/스피드 드리블러.png"
              />
            </div>
            <img class="playerInfo__img" src="@/assets/player/fr_6.png" />
          </div>
          <div class="team__playerInfo" v-else-if="detailIndex == 7">
            <p class="playerInfo__name">O. 뎀벨레 (O. Dembélé)</p>
            <div class="playerInfo__detail">
              <div class="playerInfo__detail--col">
                <p class="playerInfo__detailInfo">Barcelona</p>
                <p class="playerInfo__detailInfo">프랑스</p>
                <p class="playerInfo__detailInfo">1997년 5월 15일</p>
                <p class="playerInfo__detailInfo">윙어(WF)</p>
              </div>
              <img
                class="playerInfo__icon"
                src="@/assets/playerIcons/스피드 드리블러.png"
              />
            </div>
            <img class="playerInfo__img" src="@/assets/player/fr_7.png" />
          </div>
          <div class="team__playerInfo" v-else-if="detailIndex == 8">
            <p class="playerInfo__name">A. 그리즈만 (A. Griezmann)</p>
            <div class="playerInfo__detail">
              <div class="playerInfo__detail--col">
                <p class="playerInfo__detailInfo">Atletico Madrid</p>
                <p class="playerInfo__detailInfo">프랑스</p>
                <p class="playerInfo__detailInfo">1991년 3월 21일</p>
                <p class="playerInfo__detailInfo">스트라이커(ST)</p>
              </div>
              <img
                class="playerInfo__icon"
                src="@/assets/playerIcons/스피드 드리블러.png"
              />
            </div>
            <img class="playerInfo__img" src="@/assets/player/fr_8.png" />
          </div>
          <div class="team__playerInfo" v-else-if="detailIndex == 9">
            <p class="playerInfo__name">K. 음바페 (K. Mbappé)</p>
            <div class="playerInfo__detail">
              <div class="playerInfo__detail--col">
                <p class="playerInfo__detailInfo">Paris Saint-Germain</p>
                <p class="playerInfo__detailInfo">프랑스</p>
                <p class="playerInfo__detailInfo">1998년 12월 20일</p>
                <p class="playerInfo__detailInfo">스트라이커(ST)</p>
              </div>
              <img
                class="playerInfo__icon"
                src="@/assets/playerIcons/스피드 드리블러.png"
              />
            </div>
            <img class="playerInfo__img" src="@/assets/player/fr_9.png" />
          </div>
          <div class="team__playerInfo" v-else-if="detailIndex == 10">
            <p class="playerInfo__name">O. 지루 (O. Giroud)</p>
            <div class="playerInfo__detail">
              <div class="playerInfo__detail--col">
                <p class="playerInfo__detailInfo">AC Milan</p>
                <p class="playerInfo__detailInfo">프랑스</p>
                <p class="playerInfo__detailInfo">1986년 9월 30일</p>
                <p class="playerInfo__detailInfo">스트라이커(ST)</p>
              </div>
              <img
                class="playerInfo__icon"
                src="@/assets/playerIcons/스피드 드리블러.png"
              />
            </div>
            <img class="playerInfo__img" src="@/assets/player/fr_10.png" />
          </div>
        </div>
        <ul class="team__playerList" v-else-if="teamHome">
          <li
            class="playerList__player"
            @click="
              detailToggle = true;
              detailIndex = 0;
            "
          >
            <p class="playerList__name">23 E.마르티네스</p>
            <img class="playerList__img" src="@/assets/player/arg_0.png" />
          </li>
          <li
            class="playerList__player"
            @click="
              detailToggle = true;
              detailIndex = 1;
            "
          >
            <p class="playerList__name">3 N.타글리아피코</p>
            <img class="playerList__img" src="@/assets/player/arg_1.png" />
          </li>
          <li
            class="playerList__player"
            @click="
              detailToggle = true;
              detailIndex = 2;
            "
          >
            <p class="playerList__name">19 N.오타멘디</p>
            <img class="playerList__img" src="@/assets/player/arg_2.png" />
          </li>
          <li
            class="playerList__player"
            @click="
              detailToggle = true;
              detailIndex = 3;
            "
          >
            <p class="playerList__name">13 C.로메로</p>
            <img class="playerList__img" src="@/assets/player/arg_3.png" />
          </li>
          <li
            class="playerList__player"
            @click="
              detailToggle = true;
              detailIndex = 4;
            "
          >
            <p class="playerList__name">26 N.몰리나</p>
            <img class="playerList__img" src="@/assets/player/arg_4.png" />
          </li>
          <li
            class="playerList__player"
            @click="
              detailToggle = true;
              detailIndex = 5;
            "
          >
            <p class="playerList__name">20 A.막알리스테르</p>
            <img class="playerList__img" src="@/assets/player/arg_5.png" />
          </li>
          <li
            class="playerList__player"
            @click="
              detailToggle = true;
              detailIndex = 6;
            "
          >
            <p class="playerList__name">24 E.페르난데스</p>
            <img class="playerList__img" src="@/assets/player/arg_6.png" />
          </li>
          <li
            class="playerList__player"
            @click="
              detailToggle = true;
              detailIndex = 7;
            "
          >
            <p class="playerList__name">7 R.데 파울</p>
            <img class="playerList__img" src="@/assets/player/arg_7.png" />
          </li>
          <li
            class="playerList__player"
            @click="
              detailToggle = true;
              detailIndex = 8;
            "
          >
            <p class="playerList__name">11 A.디 마리아</p>
            <img class="playerList__img" src="@/assets/player/arg_8.png" />
          </li>
          <li
            class="playerList__player"
            @click="
              detailToggle = true;
              detailIndex = 9;
            "
          >
            <p class="playerList__name">9 J.알바레스</p>
            <img class="playerList__img" src="@/assets/player/arg_9.png" />
          </li>
          <li
            class="playerList__player"
            @click="
              detailToggle = true;
              detailIndex = 10;
            "
          >
            <p class="playerList__name">10 L.메시</p>
            <img class="playerList__img" src="@/assets/player/arg_10.png" />
          </li>
        </ul>
        <ul class="team__playerList" v-else>
          <li
            class="playerList__player"
            @click="
              detailToggle = true;
              detailIndex = 0;
            "
          >
            <p class="playerList__name">1 H.요리스</p>
            <img class="playerList__img" src="@/assets/player/fr_0.png" />
          </li>
          <li
            class="playerList__player"
            @click="
              detailToggle = true;
              detailIndex = 1;
            "
          >
            <p class="playerList__name">5 J.쿤데</p>
            <img class="playerList__img" src="@/assets/player/fr_1.png" />
          </li>
          <li
            class="playerList__player"
            @click="
              detailToggle = true;
              detailIndex = 2;
            "
          >
            <p class="playerList__name">4 R.바란</p>
            <img class="playerList__img" src="@/assets/player/fr_2.png" />
          </li>
          <li
            class="playerList__player"
            @click="
              detailToggle = true;
              detailIndex = 3;
            "
          >
            <p class="playerList__name">18 D.우파메카노</p>
            <img class="playerList__img" src="@/assets/player/fr_3.png" />
          </li>
          <li
            class="playerList__player"
            @click="
              detailToggle = true;
              detailIndex = 4;
            "
          >
            <p class="playerList__name">22 T.에르난데스</p>
            <img class="playerList__img" src="@/assets/player/fr_4.png" />
          </li>
          <li
            class="playerList__player"
            @click="
              detailToggle = true;
              detailIndex = 5;
            "
          >
            <p class="playerList__name">8 A.추아메니</p>
            <img class="playerList__img" src="@/assets/player/fr_5.png" />
          </li>
          <li
            class="playerList__player"
            @click="
              detailToggle = true;
              detailIndex = 6;
            "
          >
            <p class="playerList__name">14 A.라비오</p>
            <img class="playerList__img" src="@/assets/player/fr_6.png" />
          </li>
          <li
            class="playerList__player"
            @click="
              detailToggle = true;
              detailIndex = 7;
            "
          >
            <p class="playerList__name">11 O.뎀벨레</p>
            <img class="playerList__img" src="@/assets/player/fr_7.png" />
          </li>
          <li
            class="playerList__player"
            @click="
              detailToggle = true;
              detailIndex = 8;
            "
          >
            <p class="playerList__name">7 A.그리즈만</p>
            <img class="playerList__img" src="@/assets/player/fr_8.png" />
          </li>
          <li
            class="playerList__player"
            @click="
              detailToggle = true;
              detailIndex = 9;
            "
          >
            <p class="playerList__name">10 K.음바페</p>
            <img class="playerList__img" src="@/assets/player/fr_9.png" />
          </li>
          <li
            class="playerList__player"
            @click="
              detailToggle = true;
              detailIndex = 10;
            "
          >
            <p class="playerList__name">9 O.지루</p>
            <img class="playerList__img" src="@/assets/player/fr_10.png" />
          </li>
        </ul>
      </div>
      <div class="chat" v-bind:class="{ hide__right: chatToggle }">
        <div class="chat__header">
          <p class="chat__userInfo">이름 :</p>
          <input
            type="text"
            class="chat__userName"
            v-model="myName"
            placeholder="이름을 입력해주세요"
          />
          <div class="chat__userColor"></div>
          <div class="header__underLine"></div>
        </div>
        <div class="chat__content" ref="chat__content">
          <div
            class="chat__liveChat"
            v-for="(message, idx) in messages"
            :key="idx"
          >
            <div class="chat__userChat">
              <!-- v-if="message.user != 'Me'" -->
              <p>
                <span class="font__purple">{{ myName }}</span> :
                {{ message.text }}
              </p>
            </div>
            <!-- <div class="chat__myChat">
              v-else
              <span class="chat__sendTarget">[{{ message.user }}]</span
              ><br /><br />
              <p>{{ message.text }}</p>
            </div> -->
          </div>
        </div>
        <div class="chat__box">
          <div class="chat__target">
            <div
              class="chat__targetText"
              v-bind:class="{ select: !targetToggle }"
              @click="targetChange"
            >
              모두
            </div>
            <div
              class="chat__targetText"
              v-bind:class="{ select: targetToggle }"
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
import { io } from "socket.io-client";

export default {
  components: {
    Video,
  },
  data() {
    return {
      targetToggle: true,
      messages: [], // Store messages
      newMessage: "", // User input for new message
      socket: null, // WebSocket connection
      infoToggle: false,
      chatToggle: false,
      detailToggle: false,
      detailIndex: 0,
      teamHome: true,
      myName: "메시",
    };
  },
  async mounted() {
    // Initialize WebSocket connection
    this.socket = io("http://localhost:3000");

    // Add received message to messages array
    this.socket.on("message", (message) => {
      this.messages.push(message);
    });

    const video = document.querySelector("Video");

    video.addEventListener("ended", (ev) => {
      // console.log(ev);
      this.playToggle = false;
    });
    video.addEventListener("timeupdate", (ev) => {
      if (Math.round(video.currentTime) < 10) {
        this.videoTimestamp = `00:0${Math.round(
          video.currentTime
        )} / 00:${Math.round(video.duration)}`;
      } else {
        this.videoTimestamp = `00:${Math.round(
          video.currentTime
        )} / 00:${Math.round(video.duration)}`;
      }
    });
    // console.log(video.duration);
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
          // this.socket.emit("message", {
          //   user: "Me",
          //   text: this.newMessage.trim(),
          // });
          this.messages.push({
            user: "Me",
            text: this.newMessage.trim(),
          });
          this.socket.emit("message", this.messages);
          this.newMessage = "";
          this.$refs.chat__content.scrollTop =
            this.$refs.chat__content.scrollHeight;
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
  width: calc(100% - 2rem);
  height: 0;
  padding-bottom: 56.25%;
  background: rgba(255, 255, 255, 0.224);
  border-radius: 1rem;
}
.view-mode {
  position: absolute;
  top: -2.5rem;
  left: calc(50% - 3rem);
  width: 6rem;
  height: 2rem;
  display: flex;
  align-items: center;
  justify-content: space-around;
}
.view-mode__info,
.view-mode__chat {
  width: 1rem;
  height: 1rem;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.224);
  cursor: pointer;
}
.team-info {
  position: absolute;
  bottom: 1rem;
  left: 1rem;
  width: calc(100% - 3rem - 248px);
  height: calc(881px - 42.5rem);
  border-radius: 1rem;
  display: flex;
  align-items: center;
  transition: bottom 1s;
  background: #08133a84;
  background: #0a1931c5;
  /* opacity: 0.88; */
  z-index: 9998;
}
.team-selector {
  display: flex;
  height: 100%;
  flex-direction: column;
  justify-content: space-evenly;
  /* align-items: center; */
}
.team__container {
  width: 50%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.team__card {
  width: 89%;
  height: 95%;
  display: flex;
  align-items: center;
}
.team__playerInfo {
  width: 100%;
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
  width: 5rem;
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
  width: 89%;
  height: 95%;
  overflow-x: auto;
  white-space: nowrap;
  display: flex;
  align-items: center;
}
.playerList__player {
  width: 7rem;
  height: 9rem;
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
  width: 248px;
  height: calc(881px - 4rem);
  height: calc(100% - 2rem);
  border-radius: 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  transition: right 1s;
  background: #08133a84;
  background: #0a1931c5;
  /* opacity: 0.98; */
  z-index: 9998;
}
.chat__header {
  width: 100%;
  padding: 0 1rem;
  margin-top: 0.5rem;
  height: 3.5rem;
  display: flex;
  justify-content: space-around;
  align-items: center;
  position: relative;
}
.chat__userInfo {
  height: 1.2rem;
  display: flex;
  justify-content: left;
  align-items: center;
  font-size: 1rem;
}
.chat__userName {
  max-width: 60%;
  height: 1.2rem;
  white-space: nowrap;
  overflow-x: hidden;
  font-size: 1rem;
  display: flex;
  align-items: center;
  border: none;
  background: rgba(0, 0, 0, 0);
  color: white;
}
.chat__userColor {
  width: 1.2rem;
  height: 1.2rem;
  border-radius: 50%;
  cursor: pointer;
  background: rgb(200, 20, 255);
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
  /* scroll-behavior: smooth;
  scroll-snap-type: y proximity; */
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
  min-height: 1rem;
  width: fit-content;
  max-width: 100%;
  padding: 0.3rem 0.8rem;
  border-radius: 6px 0 6px 0;
  background: rgba(0, 0, 0, 0.5);
  background: #26323800;
  /* border: 2px solid rgba(0, 0, 0, 0.2); */
  color: #fff;
  color: rgba(255, 255, 255, 0.9);
  font-size: 1rem;
  line-height: 1.3rem;
}
.chat__myChat {
  margin: 0 0 0 auto;
  margin-bottom: 1rem;
  text-align: right;
}
/* .chat__userChat:after {
  content: "";
  position: absolute;
  border: 10px solid transparent;
  border-top: 10px solid rgba(0, 0, 0, 0.2);
  border-left: none;
  bottom: -22px;
  left: 10px;
}
.chat__myChat:after {
  content: "";
  position: absolute;
  border: 10px solid transparent;
  border-top: 10px solid rgba(0, 0, 0, 0.2);
  border-right: none;
  bottom: -22px;
  right: 10px;
} */
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
.chat__text:focus,
.chat__userName:focus {
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
.yellow {
  background: #f2ae00;
}
.blue {
  background: skyblue;
}
.hide {
  display: none;
}
.hide__bottom {
  bottom: -100%;
}
.hide__right {
  right: -100%;
}
</style>
