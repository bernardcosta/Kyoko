# Kyoko

Kyoko is your local AI telegram bot based on open source LLM models. It a fully self-hosted model and bot.

## setup

1. Create a `.env` file based on this repo's `.example.env`
2. [Create a telegram bot](https://core.telegram.org/bots/tutorial#getting-ready)
    - Copy the bot token into the env var `TELEGRAM_TOKEN` in `.env` file
3. Find your [telegram user id](https://cobrasystems.nl/en/telegram-user-id/) and copy it to `OWNER_ID` env var
    - If this is not set the LLM will not be triggered and the telegram bot will be unresponsive
4. run docker services `docker-compose up`
5. Download an LLM model with `docker-compose exec ollama ollama run <model-name>`
    - you can choose any model from the [ollama library](https://github.com/ollama/ollama?tab=readme-ov-file#model-library)
6. Put the model name in the `.env` file for `OLLAMA_MODEL` env var.

For a custom model, you can create a `Modelfile` in the directory `/Modelfiles` and restart ollama container for the changes to take effect. Remember to change `OLLAMA_MODEL` env var to the model name you want to use. Follow the [ollama modelfile examples](https://github.com/ollama/ollama/blob/main/docs/modelfile.md#examples). **Note** whenever you want to run an `ollama` command always run them through the docker container with `docker compose exec ollamam <ollama-command>`

7. You can now go to your telegram bot and start chatting!