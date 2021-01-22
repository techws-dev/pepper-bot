import environ
from bot import Bot

# read the .env file
env = environ.Env()
environ.Env.read_env()

# run the discord bot
def main():
    bot_token = env.str('BOT_TOKEN')

    pepper_bot = Bot()
    pepper_bot.run(bot_token)

if __name__ == "__main__":
    main()