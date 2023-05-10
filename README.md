# startup

## 프론트엔드

1. **frontend 폴더 대상으로 터미널 열기**

2. **라이브러리 설치**
```bash
npm install
```
3. **localhost 서버 열기**
```bash
npm run serve
```
## 백엔드

1. **backend 폴더 대상으로 터미널 열기**

2. **가상환경 열기 (임시로 cellcraft 가상환경 사용)**
```bash
conda activate snakemake
```
3. **localhost 서버 열기**
```bash
uvicorn app.main:app --reload
```
## 스트리밍 서버
```bash
node server.js
```

## main에서 Pull 받을 때, 해야하는 일
1. **frontend, socket-backend 폴더 안에 node_modules 폴더 삭제**

2. **frontend, socket-backend 폴더로 터미널 열고 아래 명령어 입력**
```bash
npm install
```