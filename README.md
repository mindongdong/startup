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