const express = require("express");
const http = require("http");
const { Server } = require("socket.io");
const fs = require("fs");
const { Configuration, OpenAIApi } = require("openai");
require("dotenv").config();

const app = express();
const server = http.createServer(app);
const io = new Server(server, {
  cors: {
    origin: "*",
  },
});

const soccerChat = async (input_messages) => {
  const configuration = new Configuration({
    organization: "org-6prUbbNPuulDEAau5LppDW5K",
    apiKey: process.env.OPENAI_API_KEY,
  });
  const openai = new OpenAIApi(configuration);

  const messages = [];
  // for (const [input_text, completion_text] of history) {
  //   messages.push({ role: "user", content: input_text });
  //   messages.push({ role: "assistant", content: completion_text });
  // }
  messages.push({
    role: "system",
    content:
      "Please answer in Korean and in one sentence. You are a commentator who broadcasts soccer games. The video that is being broadcast now is the round of 16 match between Argentina and France at the 2018 World Cup.",
  });
  
  input_messages.forEach(message => {
    if(message.user == "Me"){
      messages.push({ role: "user", content: message.text });
    } else {
      messages.push({ role: "assistant", content: message.text });
    }
  });

  console.log(messages);

  try {
    const completion = await openai.createChatCompletion({
      model: "gpt-3.5-turbo",
      messages: messages,
    });

    const completion_text = completion.data.choices[0].message.content;
    console.log(completion_text);

    return {user: "AI", text: completion_text};
  } catch (error) {
    console.error(error);
  }
};

io.on("connection", (socket) => {
  console.log("User connected");

  socket.on("message", async (messages) => {
    const message = messages[messages.length-1].text
    const AIcomment = await soccerChat(messages);
    if(AIcomment) io.emit("message", AIcomment);
    console.log(message);
  });

  socket.on("disconnect", () => {
    console.log("User disconnected");
  });
});

app.get("/video", function (req, res) {
  // Ensure there is a range given for the video
  const range = req.headers.range;
  if (!range) {
    res.status(400).send("Requires Range header");
  }

  const videoPath = "video/video.mp4";
  const videoSize = fs.statSync("video/video.mp4").size;

  const CHUNK_SIZE = 10 ** 6; // 1MB
  const start = Number(range.replace(/\D/g, ""));
  const end = Math.min(start + CHUNK_SIZE, videoSize - 1);

  // Create headers
  const contentLength = end - start + 1;
  const headers = {
    "Content-Range": `bytes ${start}-${end}/${videoSize}`,
    "Accept-Ranges": "bytes",
    "Content-Length": contentLength,
    "Content-Type": "video/mp4",
  };

  // HTTP Status 206 for Partial Content
  res.writeHead(206, headers);

  // create video read stream for this particular chunk
  const videoStream = fs.createReadStream(videoPath, { start, end });

  // Stream the video chunk to the client
  videoStream.pipe(res);
});

server.listen(3000, () => {
  console.log("Server is running on http://localhost:3000");
});
