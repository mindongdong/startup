const { log } = require("console");
const express = require("express");
const router = express.Router();
const fs = require("fs");
const path = require("path");

router.get("/:videoName", (req, res) => {
  const videoName = req.params.videoName;
  const videoPath = path.join("video", videoName);

  console.log(videoPath);

  if (fs.existsSync(videoPath)) {
    res.sendFile(videoPath, { root: __dirname });
    console.log("sucess");
  } else {
    res.status(404).send("Video not found");
  }
});

// router.get("/:videoName", (req, res) => {
//   const videoName = req.params.videoName;
//   const videoPath = path.join("video", videoName);
//   const stat = fs.statSync(videoPath);
//   const fileSize = stat.size;
//   const range = req.headers.range;

//   if (range) {
//     const parts = range.replace(/bytes=/, "").split("-");
//     const start = parseInt(parts[0], 10);
//     const end = parts[1] ? parseInt(parts[1], 10) : fileSize - 1;
//     const chunksize = end - start + 1;
//     const file = fs.createReadStream(videoPath, { start, end });
//     const head = {
//       "Content-Range": `bytes ${start}-${end}/${fileSize}`,
//       "Accept-Ranges": "bytes",
//       "Content-Length": chunksize,
//       "Content-Type": "video/mp4",
//     };
//     res.writeHead(206, head);
//     file.pipe(res);
//   } else {
//     const head = {
//       "Content-Length": fileSize,
//       "Content-Type": "video/mp4",
//     };
//     res.writeHead(200, head);
//     fs.createReadStream(videoPath).pipe(res);
//   }
// });

module.exports = router;
