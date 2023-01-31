import asyncio
from types import ModuleType
from typing import Optional

from discord.ext import commands

from blish import handlers, interceptors, modules
from blish.utils.extensions import get_module_names


class Blish(commands.Bot):
    """A subclass of `discord.ext.commands.Bot` that implements bot-specific functions."""

    COGS_SUCCESSFULLY_LOADED_MESSAGE = lambda name, cogs: f"{name} cogs successfully \
loaded: {list(cogs)}"

    def __init__(self, *args, **kwargs):
        """Initialize the bot instance `blish`."""
        super().__init__(*args, **kwargs)

        self.all_handlers: Optional[frozenset[str]] = None
        self.all_interceptors: Optional[frozenset[str]] = None
        self.all_modules: Optional[frozenset[str]] = None

    async def setup_hook(self) -> None:
        """Default setup_hook method with `discord.ext.commands.Cog` setup"""
        await super().setup_hook()

        # Load all the handler Cogs
        self.all_handlers = await self._load_extensions(handlers)
        print(Blish.COGS_SUCCESSFULLY_LOADED_MESSAGE("Handler", self.all_handlers))

        # Load all the interceptor Cogs
        self.all_interceptors = await self._load_extensions(interceptors)
        print(Blish.COGS_SUCCESSFULLY_LOADED_MESSAGE("Interceptors", self.all_interceptors))

        # Load all the module Cogs
        self.all_modules = await self._load_extensions(modules)
        print(Blish.COGS_SUCCESSFULLY_LOADED_MESSAGE("Modules", self.all_modules))

    async def _load_extensions(self, module: ModuleType) -> frozenset[str]:
        """Extensions loader by creating an :obj:`asyncio.Task` for each load event."""
        background_tasks = set()
        extensions = get_module_names(module)

        for cog in extensions:
            task = asyncio.create_task(self.load_extension(cog))
            background_tasks.add(task)
            task.add_done_callback(background_tasks.discard)

        return extensions
