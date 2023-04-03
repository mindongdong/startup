const { Configuration, OpenAIApi } = require("openai");
require("dotenv").config();

const configuration = new Configuration({
  organization: "org-6prUbbNPuulDEAau5LppDW5K",
  apiKey: process.env.OPENAI_API_KEY,
});

const soccerChat = async (input_messages) => {
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

module.exports = { soccerChat };
