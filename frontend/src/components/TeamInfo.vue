<template>
  <div class="team-info">
    <div class="team-selector">
      <div
        class="team__icon"
        @click="
          detailToggle = false;
          teamHome = true;
        "
        @dblclick="flagClick"
      >
        <p class="team__icon--name" draggable="false">아르헨티나</p>
        <img
          class="team__icon--img"
          draggable="false"
          src="@/assets/flags/arg-flag.png"
        />
      </div>
      <div
        class="team__icon"
        @click="
          detailToggle = false;
          teamHome = false;
        "
        @dblclick="flagClick"
      >
        <p class="team__icon--name" draggable="false">프랑스</p>
        <img
          class="team__icon--img"
          draggable="false"
          src="@/assets/flags/fra-flag.png"
        />
      </div>
    </div>
    <div class="team__card" v-if="detailToggle">
      <div class="team__playerInfo" v-if="detailIndex == 0">
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
            src="@/assets/playerIcons/GK 능숙한 펀칭.png"
          />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/GK 적극적 크로스 수비.png"
          />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/스피드 드리블러.png"
          />
        </div>
        <img
          class="playerInfo__img"
          @click="imageClick"
          src="@/assets/player/arg_0.png"
        />
      </div>
      <div class="team__playerInfo" v-else-if="detailIndex == 1">
        <p class="playerInfo__name">N. 타글리아피코 (N. Tagliafico)</p>
        <div class="playerInfo__detail">
          <div class="playerInfo__detail--col">
            <p class="playerInfo__detailInfo">Ajax</p>
            <p class="playerInfo__detailInfo">아르헨티나</p>
            <p class="playerInfo__detailInfo">1992년 8월 31일</p>
            <p class="playerInfo__detailInfo">왼쪽 풀백(LB)</p>
          </div>
          <img class="playerInfo__icon" src="@/assets/playerIcons/강철몸.png" />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/슬라이딩 태클 선호.png"
          />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/아웃사이드 슈팅.크로스.png"
          />
        </div>
        <img
          class="playerInfo__img"
          @click="imageClick"
          src="@/assets/player/arg_1.png"
        />
      </div>
      <div class="team__playerInfo" v-else-if="detailIndex == 2">
        <p class="playerInfo__name">N. 오타멘디 (N. Otamendi)</p>
        <div class="playerInfo__detail">
          <div class="playerInfo__detail--col">
            <p class="playerInfo__detailInfo">Benfica</p>
            <p class="playerInfo__detailInfo">아르헨티나</p>
            <p class="playerInfo__detailInfo">1988년 2월 12일</p>
            <p class="playerInfo__detailInfo">센터백(CB)</p>
          </div>
          <img class="playerInfo__icon" src="@/assets/playerIcons/리더십.png" />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/장거리 스로인.png"
          />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/팀 플레이어.png"
          />
        </div>
        <img
          class="playerInfo__img"
          @click="imageClick"
          src="@/assets/player/arg_2.png"
        />
      </div>
      <div class="team__playerInfo" v-else-if="detailIndex == 3">
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
            src="@/assets/playerIcons/긴 패스 선호.png"
          />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/주발 선호.png"
          />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/패스 마스터.png"
          />
        </div>
        <img
          class="playerInfo__img"
          @click="imageClick"
          src="@/assets/player/arg_3.png"
        />
      </div>
      <div class="team__playerInfo" v-else-if="detailIndex == 4">
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
            src="@/assets/playerIcons/예리한 감아차기.png"
          />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/중거리 슛 선호.png"
          />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/칩슛 선호.png"
          />
        </div>
        <img
          class="playerInfo__img"
          @click="imageClick"
          src="@/assets/player/arg_4.png"
        />
      </div>
      <div class="team__playerInfo" v-else-if="detailIndex == 5">
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
            src="@/assets/playerIcons/플레이 메이커.png"
          />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/테크니컬 드리블러.png"
          />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/화려한 개인기.png"
          />
        </div>
        <img
          class="playerInfo__img"
          @click="imageClick"
          src="@/assets/player/arg_5.png"
        />
      </div>
      <div class="team__playerInfo" v-else-if="detailIndex == 6">
        <p class="playerInfo__name">E. 페르난데스 (E. Fernández)</p>
        <div class="playerInfo__detail">
          <div class="playerInfo__detail--col">
            <p class="playerInfo__detailInfo">Defensa y Justicia</p>
            <p class="playerInfo__detailInfo">아르헨티나</p>
            <p class="playerInfo__detailInfo">2000년 3월 12일</p>
            <p class="playerInfo__detailInfo">미드필더(MF)</p>
          </div>
          <img class="playerInfo__icon" src="@/assets/playerIcons/유리몸.png" />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/플레이 메이커.png"
          />
          <img class="playerInfo__icon" src="@/assets/playerIcons/승부욕.png" />
        </div>
        <img
          class="playerInfo__img"
          @click="imageClick"
          src="@/assets/player/arg_6.png"
        />
      </div>
      <div class="team__playerInfo" v-else-if="detailIndex == 7">
        <p class="playerInfo__name">R. 데 파울 (R. De Paul)</p>
        <div class="playerInfo__detail">
          <div class="playerInfo__detail--col">
            <p class="playerInfo__detailInfo">Atlético Madrid</p>
            <p class="playerInfo__detailInfo">아르헨티나</p>
            <p class="playerInfo__detailInfo">1994년 5월 24일</p>
            <p class="playerInfo__detailInfo">미드필더(MF)</p>
          </div>
          <img class="playerInfo__icon" src="@/assets/playerIcons/강철몸.png" />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/얼리 크로스 선호.png"
          />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/패스 마스터.png"
          />
        </div>
        <img
          class="playerInfo__img"
          @click="imageClick"
          src="@/assets/player/arg_7.png"
        />
      </div>
      <div class="team__playerInfo" v-else-if="detailIndex == 8">
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
            src="@/assets/playerIcons/개인 플레이 선호.png"
          />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/테크니컬 드리블러.png"
          />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/아웃사이드 슈팅.크로스.png"
          />
        </div>
        <img
          class="playerInfo__img"
          @click="imageClick"
          src="@/assets/player/arg_8.png"
        />
      </div>
      <div class="team__playerInfo" v-else-if="detailIndex == 9">
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
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/주발 선호.png"
          />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/중거리 슛 선호.png"
          />
        </div>
        <img
          class="playerInfo__img"
          @click="imageClick"
          src="@/assets/player/arg_9.png"
        />
      </div>
      <div class="team__playerInfo" v-else-if="detailIndex == 10">
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
            src="@/assets/playerIcons/화려한 개인기.png"
          />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/테크니컬 드리블러.png"
          />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/패스 마스터.png"
          />
        </div>
        <img
          class="playerInfo__img"
          @click="imageClick"
          src="@/assets/player/arg_10.png"
        />
      </div>
      <div>
        <img class="playerInfo__icon" src="@/assets/playerIcons/vs_white.png" />
      </div>
      <div class="team__playerInfo" v-if="detailIndex == 0">
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
            src="@/assets/playerIcons/GK 능숙한 펀칭.png"
          />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/GK 적극적 크로스 수비.png"
          />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/GK 침착한 일대일 수비.png"
          />
        </div>
        <img
          class="playerInfo__img"
          @click="imageClick"
          src="@/assets/player/fr_0.png"
        />
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
            src="@/assets/playerIcons/슬라이딩 태클 선호.png"
          />
          <img class="playerInfo__icon" src="@/assets/playerIcons/리더십.png" />
          <img class="playerInfo__icon" src="@/assets/playerIcons/강철몸.png" />
        </div>
        <img
          class="playerInfo__img"
          @click="imageClick"
          src="@/assets/player/fr_1.png"
        />
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
            src="@/assets/playerIcons/패스 마스터.png"
          />
          <img class="playerInfo__icon" src="@/assets/playerIcons/강철몸.png" />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/슬라이딩 태클 선호.png"
          />
        </div>
        <img
          class="playerInfo__img"
          @click="imageClick"
          src="@/assets/player/fr_2.png"
        />
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
            src="@/assets/playerIcons/장거리 스로인.png"
          />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/팀 플레이어.png"
          />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/긴 패스 선호.png"
          />
        </div>
        <img
          class="playerInfo__img"
          @click="imageClick"
          src="@/assets/player/fr_3.png"
        />
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
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/장거리 스로인.png"
          />
          <img class="playerInfo__icon" src="@/assets/playerIcons/강철몸.png" />
        </div>
        <img
          class="playerInfo__img"
          @click="imageClick"
          src="@/assets/player/fr_4.png"
        />
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
          <img class="playerInfo__icon" src="@/assets/playerIcons/리더십.png" />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/팀 플레이어.png"
          />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/플레이 메이커.png"
          />
        </div>
        <img
          class="playerInfo__img"
          @click="imageClick"
          src="@/assets/player/fr_5.png"
        />
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
            src="@/assets/playerIcons/긴 패스 선호.png"
          />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/선호 포지션 고집.png"
          />
          <img class="playerInfo__icon" src="@/assets/playerIcons/승부욕.png" />
        </div>
        <img
          class="playerInfo__img"
          @click="imageClick"
          src="@/assets/player/fr_6.png"
        />
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
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/화려한 개인기.png"
          />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/중거리 슛 선호.png"
          />
        </div>
        <img
          class="playerInfo__img"
          @click="imageClick"
          src="@/assets/player/fr_7.png"
        />
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
            src="@/assets/playerIcons/개인 플레이 선호.png"
          />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/예리한 감아차기.png"
          />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/패스 마스터.png"
          />
        </div>
        <img
          class="playerInfo__img"
          @click="imageClick"
          src="@/assets/player/fr_8.png"
        />
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
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/아웃사이드 슈팅.크로스.png"
          />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/화려한 개인기.png"
          />
        </div>
        <img
          class="playerInfo__img"
          @click="imageClick"
          src="@/assets/player/fr_9.png"
        />
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
            src="@/assets/playerIcons/파워 헤더.png"
          />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/트러블 메이커.png"
          />
          <img
            class="playerInfo__icon"
            src="@/assets/playerIcons/초 장거리 스로인.png"
          />
        </div>
        <img
          class="playerInfo__img"
          @click="imageClick"
          src="@/assets/player/fr_10.png"
        />
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
</template>

<script>
export default {
  name: "Team",
  props: {},
  data() {
    return {
      teamHome: true,
      detailToggle: false,
      detailIndex: 0,
    };
  },
  methods: {
    flagClick(ev) {
      console.dir(ev.target);
      if (ev.target.localName === "p") {
        console.log(ev.target.innerText);
        if (ev.target.innerText === "아르헨티나") {
          for (let i = 0; i < 11; i++) {
            this.$refs.videoRef.$refs.analyzeRef.toggleBox(i);
          }
        } else if (ev.target.innerText === "프랑스") {
          for (let i = 11; i < 22; i++) {
            this.$refs.videoRef.$refs.analyzeRef.toggleBox(i);
          }
        }
      } else if (ev.target.localName === "img") {
        console.log(ev.target.parentNode.children[0].innerText);
        if (ev.target.parentNode.children[0].innerText === "아르헨티나") {
          for (let i = 0; i < 11; i++) {
            this.$refs.videoRef.$refs.analyzeRef.toggleBox(i);
          }
        } else if (ev.target.parentNode.children[0].innerText === "프랑스") {
          for (let i = 11; i < 22; i++) {
            this.$refs.videoRef.$refs.analyzeRef.toggleBox(i);
          }
        }
      } else if (ev.target.localName === "div") {
        console.log(ev.target.children[0].innerText);
        if (ev.target.children[0].innerText === "아르헨티나") {
          for (let i = 0; i < 11; i++) {
            this.$refs.videoRef.$refs.analyzeRef.toggleBox(i);
          }
        } else if (ev.target.children[0].innerText === "프랑스") {
          for (let i = 11; i < 22; i++) {
            this.$refs.videoRef.$refs.analyzeRef.toggleBox(i);
          }
        }
      }
    },
    imageClick(ev) {
      const url = ev.target.src;
      let match = url.match(/(arg|fr)_(\d+)\./);
      if (match) {
        let label = match[1];
        let number = parseInt(match[2]);
        console.log(label + "_" + number);
        if (label === "fr") {
          this.$refs.videoRef.$refs.analyzeRef.toggleBox(number + 11);
        } else {
          this.$refs.videoRef.$refs.analyzeRef.toggleBox(number);
        }
      }
    },
  },
};
</script>

<style scoped>
.team-info {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  background: #0a1931c5;
  border-radius: 1rem;
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
  width: 100%;
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
  margin-left: 1.3rem;
}
.playerInfo__detail {
  width: calc(100% - 13.5rem);
  height: calc(100% - 3.5rem);
  margin-left: 0.8rem;
  padding-left: 0.5rem;
  background: rgba(58, 65, 123, 0.378);
  border-radius: 1rem;
  display: flex;
  align-items: center;
  justify-items: space-evenly;
}
.playerInfo__detail--col {
  width: 80%;
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
  width: 5rem;
  height: 5rem;
  margin: 0.2rem;
}
.playerInfo__img {
  position: absolute;
  right: 0;
  bottom: 0;
  width: 12.5rem;
  height: 16rem;
  cursor: pointer;
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
  height: 10.5rem;
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
</style>
