import asyncio
import logging
from datetime import datetime
from io import BytesIO

import humanize
import pytz
from discord import Embed, Color
from discord import File
from discord.ext import commands
from discord.commands import slash_command

from utils import solidity
from utils.cfg import cfg
from utils.deposit_pool_graph import get_graph
from utils.readable import etherscan_url, uptime
from utils.rocketpool import rp
from utils.shared_w3 import w3
from utils.slash_permissions import guilds
from utils.thegraph import get_average_commission
from utils.visibility import is_hidden

log = logging.getLogger("random")
log.setLevel(cfg["log_level"])


class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = Color.from_rgb(235, 142, 85)
    @slash_command(guild_ids=guilds)
    async def dev_time(self, ctx):
        """Timezones too confusing to you? Well worry no more, this command is here to help!"""
        embed = Embed(color=self.color)
        time_format = "%A %H:%M:%S %Z"

        dev_time = datetime.now(tz=pytz.timezone("UTC"))
        embed.add_field(name="Coordinated Universal Time", value=dev_time.strftime(time_format), inline=False)

        dev_time = datetime.now(tz=pytz.timezone("Australia/Lindeman"))
        embed.add_field(name="Time for most of the Dev Team", value=dev_time.strftime(time_format), inline=False)

        joe_time = datetime.now(tz=pytz.timezone("America/New_York"))
        embed.add_field(name="Joe's Time", value=joe_time.strftime(time_format), inline=False)

        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(Random(bot))
