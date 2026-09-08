const { Telegraf } = require("telegraf");
const http = require("http");

const bot = new Telegraf(process.env.BOT_TOKEN);

bot.start((ctx) => {
  ctx.reply(
    "স্বাগতম!\n\n" +
    "আমি একটি Telegram Group Management Bot।\n\n" +
    "/help - কমান্ডের তালিকা\n" +
    "/id - গ্রুপ বা ইউজারের ID\n" +
    "/rules - গ্রুপের নিয়ম"
  );
});

bot.help((ctx) => {
  ctx.reply(
    "📋 Bot Commands\n\n" +
    "/start - বট চালু\n" +
    "/help - সাহায্য\n" +
    "/id - ID দেখা\n" +
    "/rules - গ্রুপের নিয়ম"
  );
});

bot.command("id", (ctx) => {
  const chat = ctx.chat;
  const user = ctx.from;

  ctx.reply(
    `Chat ID: ${chat.id}\n` +
    `User ID: ${user.id}\n` +
    `Chat Type: ${chat.type}`
  );
});

bot.command("rules", (ctx) => {
  ctx.reply(
    "📜 গ্রুপের নিয়ম\n\n" +
    "১. সবাইকে সম্মান করতে হবে।\n" +
    "২. স্প্যাম করা যাবে না।\n" +
    "৩. অ্যাডমিনের নির্দেশ মানতে হবে।"
  );
});

// Render Web Service-এর জন্য HTTP server
const PORT = process.env.PORT || 3000;

const server = http.createServer((req, res) => {
  res.writeHead(200, { "Content-Type": "text/plain" });
  res.end("Telegram Group Management Bot is running!");
});

server.listen(PORT, () => {
  console.log(`HTTP server running on port ${PORT}`);
});

// Telegram bot চালু
bot.launch()
  .then(() => {
    console.log("🤖 Bot is running...");
  })
  .catch((error) => {
    console.error("Bot failed to start:", error);
  });

process.once("SIGINT", () => bot.stop("SIGINT"));
process.once("SIGTERM", () => bot.stop("SIGTERM"));
