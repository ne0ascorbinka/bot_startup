import json
from pyrogram import Client, filters
from pyrogram.types import Message

with open("config.json") as file:
    data = json.load(file)

def get_client():
    api_id = data["api_id"]
    api_hash = data["api_hash"]
    bot_token = data["bot_token"]
    name = data["bot_name"]
    return Client(name,
                  api_id=api_id,
                  api_hash=api_hash,
                  bot_token=bot_token)

app = get_client()
greeter = get_client()

@app.on_message(filters.command("start"))
async def start_handler(client: Client, message: Message):
    message.reply("__Hello!__")

async def notify_admin():
    async with greeter:
        await greeter.send_message(data["admin"], "Started!")

def main():

    #greeter.run(notify_admin())
    print("Started!")
    app.run()


if __name__ == "__main__":
    main()
