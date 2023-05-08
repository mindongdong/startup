const express = require("express");
const http = require("http");

const { Server } = require("socket.io");
const { soccerChat } = require("./ai-chat");

const app = express();
const server = http.createServer(app);
const io = new Server(server, {
  cors: {
    origin: "*",
  },
});

const config = {
  listenIp: "0.0.0.0",
  listenPort: 3000,
};

const videoRouter = require("./router/video.js");
const audioRouter = require("./router/audio.js");

io.on("connection", (socket) => {
  console.log("User connected");

  socket.on("message", async (messages) => {
    console.log("chat");
    const AIcomment = await soccerChat(messages);
    if (AIcomment) io.emit("message", AIcomment);
    // const message = messages[messages.length - 1].text;
    // console.log(message);
  });

  socket.on("disconnect", () => {
    console.log("User disconnected");
  });
});

server.listen(config.listenPort, () => {
  console.log("Server is running on http://localhost:3000");
});

app.use("/video", videoRouter);
app.use("/audio", audioRouter);
