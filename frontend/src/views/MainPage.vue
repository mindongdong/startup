<template>
  <div>
    <!-- <video
      id="my-player"
      class="video-js"
      controls
      preload="auto"
      width="100%"
      height="100%"
      data-setup="{}"
    >
      <source src="@/assets/video1.mp4" type="video/mp4" />
      <p class="vjs-no-js">
        To view this video please enable JavaScript, and consider upgrading to a
        web browser that
        <a href="https://videojs.com/html5-video-support/" target="_blank">
          supports HTML5 video
        </a>
      </p>
    </video> -->
    <div class="progress">
      <span class="bar"></span>
    </div>
    <div ref="canvas" id="canvas"></div>
  </div>
</template>

<script>
import * as THREE from "three";

let WIDTH = window.innerWidth;
let HEIGHT = window.innerHeight;

let scene, camera, renderer, controls;
let raycaster, pointer;
let imgBoxGroup = new THREE.Object3D();
let contentBoxGroup = new THREE.Object3D();

export default {
  data() {
    return {
      imgDepthNum: 100, //이미지 박스 사이 z값, 깊이
      imgTotalNum: 0, //총 이미지 박스 갯수
      contentDepthNum: 40, //이미지 박스 사이 z값, 깊이
      contentTotalNum: 0, //총 이미지 박스 갯수
      targetZNum: 0,
      distance: 100,
      mouseX: 0,
      mouseY: 0,
      moveX: 0,
      moveY: 0,
      moveZ: 0,
      scrolly: 0,
      pageNum: 0,
      perNum: 0,
      imgArr: [
        { img: require("@/assets/soccer_0.png") },
        { img: require("@/assets/soccer_1.png") },
        { img: require("@/assets/soccer_2.png") },
        { img: require("@/assets/soccer_3.png") },
      ],
      contentArr: [
        { contentImg: require("@/assets/content_1.jpeg") },
        { contentImg: require("@/assets/content_2.jpeg") },
        { contentImg: require("@/assets/content_3.jpeg") },
        { contentImg: require("@/assets/content_4.jpeg") },
      ],
    };
  },
  created() {
    this.imgTotalNum = this.imgArr.length; //전체 이미지 박스 갯수
    this.contentTotalNum = this.contentArr.length; //전체 콘텐츠 박스 갯수

    scene = new THREE.Scene();
    // scene.background = new THREE.Color("#000000"); //배경 컬러

    //카메라
    camera = new THREE.PerspectiveCamera(75, WIDTH / HEIGHT, 5, 1000);
    camera.position.set(0, 0, 50);

    renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setSize(WIDTH, HEIGHT);
    //그림자 활성화
    renderer.shadowMap.enabled = true;

    //헬퍼
    // const axes = new THREE.AxesHelper(150);
    // scene.add(axes);
    // const gridHelper = new THREE.GridHelper(240, 20);
    // scene.add(gridHelper);
    //body 스크롤 만들기

    //안개
    const near = 100;
    const far = 150;
    const color = "#ffffff";
    scene.fog = new THREE.Fog(color, near, far);

    //조명 넣기
    const light = new THREE.HemisphereLight(0xffffff, 0x080820, 0.8);
    light.position.set(100, 100, 0);
    scene.add(light);

    raycaster = new THREE.Raycaster();
    pointer = new THREE.Vector2();

    //이미지, 콘텐츠 박스 추가
    for (let i = 0; i < this.imgTotalNum; i++) {
      this.addImgBox(i);
    }
    for (let r = 0; r < this.contentArr.length; r++) {
      this.addContentBox(r);
    }

    scene.add(imgBoxGroup);
    scene.add(contentBoxGroup);
    this.addLight(15, 15, 20);
  },
  mounted() {
    // document.body.appendChild(renderer.domElement);
    this.$refs.canvas.appendChild(renderer.domElement);
    document.body.style.height = `${
      HEIGHT +
      this.imgTotalNum * this.imgDepthNum * 10 +
      this.contentTotalNum * this.contentDepthNum * 10
    }px`;
    document.body.style.background = "white";

    this.animate();
    window.addEventListener("resize", this.stageResize);
    window.addEventListener("scroll", this.scrollFunc);
    this.scrollFunc();
    // this.$refs.canvas.addEventListener("click", this.clickFunc);
    // this.$refs.canvas.addEventListener("wheel", this.scrollFunc);
    window.addEventListener("mousemove", (e) => {
      //console.log(e);
      this.mouseX = e.clientX;
      this.mouseY = e.clientY;
    });
    window.addEventListener("pointermove", this.onPointerMove);
    window.addEventListener("mousedown", this.onDocumentMouseDown);
  },
  methods: {
    addImgBox(i) {
      const texture = new THREE.TextureLoader().load(this.imgArr[i].img);
      // imageMap.wrapS = THREE.RepeatWrapping;
      // imageMap.wrapT = THREE.RepeatWrapping;
      // imageMap.mapping = THREE.CubeUVReflectionMapping;
      // imageMap.repeat.set(8, 8);

      const material = new THREE.SpriteMaterial({ map: texture });
      const boxMesh = new THREE.Sprite(material);
      boxMesh.scale.set(80, 80, 1);

      let z = -i * this.imgDepthNum;
      boxMesh.position.set(0, 0, z);
      boxMesh.name = `imageBox_${i}`;
      imgBoxGroup.add(boxMesh);
    },
    addContentBox(i) {
      const texture = new THREE.TextureLoader().load(
        this.contentArr[i].contentImg
      );
      console.log(WIDTH, HEIGHT);

      const material = new THREE.SpriteMaterial({ map: texture });
      const boxMesh = new THREE.Sprite(material);
      boxMesh.scale.set(48, 27, 1);

      // let z = -(this.imgDepthNum * this.imgTotalNum + this.contentDepthNum * i);
      // const posX = Math.floor(Math.random() * 120);
      // const posY = Math.floor(Math.random() * 120);
      // boxMesh.position.set(-60 + posX, -60 + posY, z);

      if (i == 0) {
        boxMesh.position.set(30, 20, -this.imgDepthNum * this.imgTotalNum);
      } else if (i == 1) {
        boxMesh.position.set(-30, 20, -this.imgDepthNum * this.imgTotalNum);
      } else if (i == 2) {
        boxMesh.position.set(30, -20, -this.imgDepthNum * this.imgTotalNum);
      } else if (i == 3) {
        boxMesh.position.set(-30, -20, -this.imgDepthNum * this.imgTotalNum);
      }
      boxMesh.name = `contentBox_${i}`;
      boxMesh.link = "/analysis";
      contentBoxGroup.add(boxMesh);
    },
    addLight(...pos) {
      const color = 0xffffff;
      const intensity = 0.4;
      const light = new THREE.PointLight(color, intensity);
      light.castShadow = true;

      light.position.set(...pos);

      // const helper = new THREE.PointLightHelper(light);
      // scene.add(helper);

      scene.add(light);
    },
    stageResize() {
      WIDTH = window.innerWidth;
      HEIGHT = window.innerHeight;

      camera.updateProjectionMatrix();
      renderer.setSize(WIDTH, HEIGHT);
      camera.aspect = WIDTH / HEIGHT;
    },
    // clickFunc(event) {
    //   console.log(event.pageX);
    //   console.log(WIDTH, HEIGHT);
    //   if (event.pageX < WIDTH / 2) {
    //     // console.log("좌");
    //     if (this.pageNum > 0) {
    //       this.pageNum -= 1;
    //     }
    //   } else {
    //     // console.log("우");
    //     if (this.pageNum < this.imgTotalNum - 1) {
    //       this.pageNum += 1;
    //     }
    //   }
    //   // console.log("this.pageNum :" + this.pageNum);
    //   this.targetNum = -(this.pageNum * this.distance);
    // },
    scrollFunc() {
      const progressBar = document.querySelector(".bar");
      this.scrolly = window.scrollY; //현재 스크롤 위치
      this.pageNum = Math.ceil(this.scrolly / 100); //스크롤 한번에 100 이동
      this.targetZNum = (this.imgDepthNum * this.pageNum) / 10;

      this.perNum = Math.ceil(
        (this.scrolly / (document.body.offsetHeight - window.innerHeight)) * 100
      );
      progressBar.style.width = this.perNum + "%";

      console.log(this.targetZNum, window.scrollY, this.pageNum);
    },
    animate() {
      // controls.update();
      this.moveZ += (this.targetZNum - this.moveZ) * 0.1;
      imgBoxGroup.position.z = this.moveZ;
      contentBoxGroup.position.z = this.moveZ;

      this.moveX += (this.mouseX - this.moveX - WIDTH / 2) * 0.1;
      this.moveY += (this.mouseY - this.moveY - WIDTH / 2) * 0.1;

      imgBoxGroup.position.x = -(this.moveX / 100);
      imgBoxGroup.position.y = this.moveY / 100;

      camera.lookAt(scene.position);
      camera.updateProjectionMatrix();
      renderer.render(scene, camera);
      requestAnimationFrame(this.animate);
    },
    onPointerMove(event) {
      pointer.x = (event.clientX / WIDTH) * 2 - 1;
      pointer.y = -(event.clientY / HEIGHT) * 2 + 1;

      raycaster.setFromCamera(pointer, camera);

      // 레이저 닿는 녀석 찾기
      const intersects = raycaster.intersectObjects(contentBoxGroup.children);

      //마우스 오버가 된 녀석들은 빨간색으로
      // for (let i = 0; i < intersects.length; i++) {
      //     intersects[i].object.material.color.set(0xff0000);
      // }

      if (intersects.length > 0) {
        document.querySelector("body").style.cursor = "pointer";
      } else {
        document.querySelector("body").style.cursor = "auto";
      }
    },
    onDocumentMouseDown(event) {
      const vector = new THREE.Vector3(pointer.x, pointer.y, 0.5);

      vector.unproject(camera);
      raycaster.setFromCamera(pointer, camera);
      const intersects = raycaster.intersectObjects(contentBoxGroup.children);

      if (intersects.length > 0) {
        const item = intersects[0].object;
        console.log(item);
        if (item.link) {
          this.$router.push(item.link);
        }
      }
    },
  },
};
</script>

<style scoped>
body {
  margin: 0;
  padding: 0;
  overflow-x: hidden;
}
#my-player {
  display: none;
}
#canvas {
  position: fixed;
  width: 100%;
  height: 100%;
  overflow: hidden;
}
.progress {
  position: fixed;
  width: 100vw;
  height: 1px;
  top: 0;
  background-color: #666666;
  z-index: 10;
}
.bar {
  position: absolute;
  width: 0;
  height: 1px;
  top: 0;
  background: yellow;
  transition: width 0.2s ease-out;
}
</style>
