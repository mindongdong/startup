const express = require("express");
const router = express.Router();

const Ffmpeg = require("fluent-ffmpeg");
const { Configuration, OpenAIApi } = require("openai");
require("dotenv").config();

const configuration = new Configuration({
  organization: "org-6prUbbNPuulDEAau5LppDW5K",
  apiKey: process.env.OPENAI_API_KEY,
});

async function transcribe(buffer, startTime) {
  const openai = new OpenAIApi(configuration);
  const response = await openai.createTranscription(
    buffer, // The audio file to transcribe.
    "whisper-1", // The model to use for transcription.
    undefined, // The prompt to use for transcription.
    "json", // The format of the transcription.
    1, // Temperature
    "en" // Language
  );
  console.log(startTime);
  return response;
}

router.get("/", (req, res) => {
  const audioPath = "video/videoTest.mp4";
  const audioSegmentDuration = 10; // 10 seconds
  console.log("audio");

  // Extract audio from the video
  const audioStream = new Ffmpeg(audioPath)
    .noVideo()
    .audioCodec("pcm_s16le")
    .audioChannels(1)
    .audioFrequency(16000)
    .format("s16le");

  let buffer = Buffer.alloc(0);
  let segmentStartTime = 0;

  audioStream.on("data", async (chunk) => {
    buffer = Buffer.concat([buffer, chunk]);
    const segmentDurationInBuffer = buffer.length / 2 / 16000;
    try {
      if (segmentDurationInBuffer >= audioSegmentDuration) {
        // Send this audio segment to the Whisper API
        const testResult = await transcribe(buffer, segmentStartTime);
        console.log(testResult);
        res.send(testResult);

        // Update the buffer and segment start time
        buffer = Buffer.alloc(0);
        segmentStartTime += audioSegmentDuration;
      }
    } catch (error) {
      console.error(error);
    }
  });

  audioStream.on("end", async () => {
    // Send the remaining buffer to the Whisper API
    if (buffer.length > 0) {
      try {
        const testResult = await transcribe(buffer, segmentStartTime);
        console.log(testResult);
        res.send(testResult);
      } catch (error) {
        console.error(error);
      }
    }
  });
});

module.exports = router;
