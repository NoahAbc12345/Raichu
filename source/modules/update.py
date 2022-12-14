import ast
import discord
import os
import subprocess
import sys

from discord.ext import commands


class Update(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.name == "GitHub" and message.author.discriminator == "0000":
            if message.embeds[0].title.startswith("[Raichu:master]"):
                await self.bot.change_presence(status=discord.Status.do_not_disturb)
                await message.add_reaction("\U0001F6D1")

                subprocess.call(["git", "pull", "origin", "master"])
                if os.name == "posix":
                    main_path = f'[\'{sys.argv[0]}\']'
                elif os.name == "nt":
                    main_path = f'[\'"{sys.argv[0]}"\']'
                main_path = ast.literal_eval(main_path)

                await message.add_reaction("\U0000267B")
                
                if os.name == "posix":
                    os.execv(sys.executable, ["python3"] + main_path)
                if os.name == "nt":
                    os.execv(sys.executable, ["python"] + main_path)

async def setup(bot: commands.Bot):
    await bot.add_cog(Update(bot))
