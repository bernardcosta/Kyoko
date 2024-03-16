import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import os
import dotenv
from functools import wraps
import requests

dotenv.load_dotenv()
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.from_user.id
    if int(chat_id) == int(os.environ["OWNER_ID"]):
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Hi, I'm Kyoko your unfiltered GPT. I won't hold anything back from you :) How can I be of assistance?",
        )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        chat_id = update.message.from_user.id
        if int(chat_id) == int(os.environ["OWNER_ID"]):
            prompt = update.message.text
            logging.info("prompt: " + prompt)
            url = os.environ["OLLAMA_API_URL"] + "/chat"
            data = {
                "model": os.environ["OLLAMA_MODEL"],
                "messages": [{"role": "user", "content": str(prompt)}],
                "stream": False,
                "keep_alive": "10m"
            } 
            logging.info("Requesting Chat with Model...")
            response = requests.post(url=url, json=data, timeout=3200)
            response.raise_for_status()
            output = response.json()["message"]["content"]
            await context.bot.send_message(chat_id=update.effective_chat.id, text=output)

    except requests.exceptions.HTTPError as e:
        logging.error("Request Failed", str(e))
        output = "I'm sorry something went wrong. I canno't help you right now!"
        await context.bot.send_message(chat_id=update.effective_chat.id, text=output)


if __name__ == "__main__":
    application = ApplicationBuilder().token(os.environ["TELEGRAM_TOKEN"]).build()

    start_handler = CommandHandler("start", start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)

    application.run_polling()
