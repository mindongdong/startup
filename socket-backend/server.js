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
      "Please answer in Korean and in one sentence. Please be kind to me. You are a commentator who broadcasts soccer games. This video is the final match between Argentina and France in the 2022 World Cup. Currently, Argentina is winning 1-0 against France, and it is around the 30th minute of the first half.",
  });

  input_messages.forEach((message) => {
    if (message.user == "Me") {
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

    return { user: "AI", text: completion_text };
  } catch (error) {
    console.error(error);
  }
};

const AIchat = async (input_messages) => {
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
      "Please answer in one sentence in Korean. Please be kind to me. You are a commentator who broadcasts a soccer game. This video is the final match between Argentina and France in the 2022 World Cup. I'll tell you the commentary script, so please explain the situation intuitively.",
  });

  messages.push(input_messages);

  console.log(messages);

  try {
    const completion = await openai.createChatCompletion({
      model: "gpt-3.5-turbo",
      messages: messages,
    });

    const completion_text = completion.data.choices[0].message.content;
    console.log(completion_text);

    return { user: "AI", text: completion_text };
  } catch (error) {
    console.error(error);
  }
};

io.on("connection", (socket) => {
  console.log("User connected");
  // let count = 0;
  // const STT = [
  //   "Luis with the launch. Koundé helps it on. Was it great from Ousmane Dembele? He's having a nightmare. From his first touch in the game, it went straight out of play. He's given the penalty away, he can't keep the ball. He's looked a little within himself. Body language.",
  //   "Messi. Schimm is past Dembele. McAllister to Di Maria. He's made a mess of that cross. Too much space everywhere. But they're enjoying themselves, these Argentinians, at the minute. Everybody wants the ball. Playing with a lot of freedom. It's a problem wide for France on both sides.",
  //   "Not seeing anything from Antoine Griezmann, with or without the ball. That's been one of their biggest components at this tournament. And arguably one of the best players at the tournament. Definitely the best young player.",
  // ];
  // const interval = setInterval(async () => {
  //   count++;
  //   if (count == 3) count = 0;
  //   const AIcomment = await AIchat({ role: "user", content: STT[count] });
  //   const splitAIcomment = AIcomment.text.split(".");
  //   splitAIcomment.forEach((comment) => {
  //     setTimeout(() => {
  //       if (comment) io.emit("message", { user: "AI", text: comment });
  //     }, 1000);
  //   });
  //   console.log(STT[count]);
  // }, 10000);

  socket.on("message", async (messages) => {
    console.log("chat");
    const message = messages[messages.length - 1].text;
    const AIcomment = await soccerChat(messages);
    if (AIcomment) io.emit("message", AIcomment);
    // console.log(message);
  });

  socket.on("disconnect", () => {
    console.log("User disconnected");
    clearInterval(interval);
  });
});

app.get("/video", function (req, res) {
  // Ensure there is a range given for the video
  const range = req.headers.range;
  if (!range) {
    res.status(400).send("Requires Range header");
  }

  const videoPath = "video/videoTest.mp4";
  const videoSize = fs.statSync("video/videoTest.mp4").size;

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
