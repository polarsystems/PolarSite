import os
import discord
from dotenv import load_dotenv
from quart import Quart, render_template, redirect, url_for
from quart_discord import DiscordOAuth2Session, requires_authorization, Unauthorized
from discord.ext import ipc

app = Quart(__name__) #

app.secret_key = b"sub2me"

load_dotenv()
app.config["DISCORD_CLIENT_ID"] = "906530431577522228"
app.config["DISCORD_CLIENT_SECRET"] = os.getenv("SEC")
app.config["DISCORD_REDIRECT_URI"] = "https://polardeveloper.org/m1"
app.config["DISCORD_BOT_TOKEN"] = os.getenv("TOKEN")

discord = DiscordOAuth2Session(app)

@app.route("/login/")
async def login():
    return await discord.create_session()

if __name__ == "__main__":
    app.run(debug=True)