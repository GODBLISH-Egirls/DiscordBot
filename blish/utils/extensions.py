"""Utilities for loading Discord extensions."""

from importlib import import_module
from inspect import isfunction
from pkgutil import ModuleInfo, walk_packages
from types import ModuleType


def ignore_module(module_info: ModuleInfo) -> bool:
    """Return whether the moduleinfo with name `name` should be ignored."""
    # `_` prefix indicates private, hence will be ignored
    return any(name.startswith("_") for name in module_info.name.split("."))


def get_module_names(module: ModuleType) -> frozenset[str]:
    """
    Return all valid extension names from the given module.

    Args:
        module (types.ModuleType): The module containing extensions.

    Returns:
        An immutable set of strings of valid extension names for use by
        :obj:`discord.ext.commands.Bot.load_extension`
    """
    modules = set()

    for module_info in walk_packages(module.__path__, f"{module.__name__}."):
        # Ignore module based on rule(s) defined in `ignore_module`
        if ignore_module(module_info):
            continue

        imported_module = import_module(module_info.name)
        if not isfunction(getattr(imported_module, "setup", None)):
            # any files without a setup function will be ignored
            continue

        modules.add(module_info.name)

    return frozenset(modules)
