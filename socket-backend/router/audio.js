const express = require("express");
const router = express.Router();
const fs = require("fs");
const path = require("path");

router.get("/:audioName", (req, res) => {
  const audioName = req.params.audioName;
  const audioPath = path.join("audio", audioName);
  console.log("audioPath: ", audioPath);

  // Check if the file exists
  if (!fs.existsSync(audioPath)) {
    res.status(404).send("File not found");
    return;
  }

  fs.stat(audioPath, (err, stat) => {
    if (err) {
      console.error(err);
      res.status(500).send("Internal Server Error");
      return;
    }

    const fileSize = stat.size;
    const range = req.headers.range;
    const mimeType = "audio/mpeg"; // This should be set according to the audio file type

    if (range) {
      const parts = range.replace(/bytes=/, "").split("-");
      const start = parseInt(parts[0], 10);
      const end = parts[1] ? parseInt(parts[1], 10) : fileSize - 1;
      const chunksize = end - start + 1;
      const file = fs.createReadStream(audioPath, { start, end });
      const head = {
        "Content-Range": `bytes ${start}-${end}/${fileSize}`,
        "Accept-Ranges": "bytes",
        "Content-Length": chunksize,
        "Content-Type": mimeType,
      };
      res.writeHead(206, head);
      file.pipe(res);
    } else {
      const head = {
        "Content-Length": fileSize,
        "Content-Type": mimeType,
      };
      res.writeHead(200, head);
      fs.createReadStream(audioPath).pipe(res);
    }
  });
});

module.exports = router;
