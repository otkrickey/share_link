import asyncio
import os
from typing import Any

import discord
from discord.ext import commands

from .logger import get_logger
from .task_manager import TaskManager
from .util import env

logger = get_logger(__name__)

__all__ = [
    "ShareLinkClient",
]


class ShareLinkClient(commands.Bot):
    bot: "ShareLinkClient"
    ready_event: asyncio.Event
    cogs: list[discord.CogMeta] = []

    def __new__(cls, *args: Any, **kwargs: Any) -> "ShareLinkClient":
        if not hasattr(cls, "bot"):
            cls.bot = commands.Bot.__new__(cls, *args, **kwargs)
        if not hasattr(cls, "ready_event"):
            cls.ready_event = asyncio.Event()
        return cls.bot

    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        commands.Bot.__init__(self, intents=intents)

    async def on_ready(self):
        assert isinstance(self.user, discord.ClientUser)
        logger.info(f"Logged in as {self.user} (ID: {self.user.id})")
        self.ready_event.set()

    @staticmethod
    async def get_client() -> "ShareLinkClient":
        await ShareLinkClient.ready_event.wait()
        return ShareLinkClient.bot

    @staticmethod
    async def wait_ready():
        await ShareLinkClient.ready_event.wait()

    async def run_bot(self):
        for cog in ShareLinkClient.cogs:
            logger.info(f"Adding cog: {cog.__name__}")
            self.add_cog(cog(self))
        TaskManager.get_loop().create_task(self.wait_exit())
        await self.start(env("BOT_DISCORD_TOKEN"))

    async def wait_exit(self):
        exit_event = TaskManager.get_exit_event()
        await exit_event.wait()
        await self.close()
        logger.info("discord client closed")

    @staticmethod
    def add_cogMeta(cog: discord.CogMeta) -> None:
        ShareLinkClient.cogs.append(cog)

    def load_cogs(self):
        for filename in os.listdir("./share_link/cogs"):
            if filename.endswith(".py"):
                self.load_extension(f"share_link.cogs.{filename[:-3]}")
                logger.info(f"Loaded cog: {filename[:-3]}")
