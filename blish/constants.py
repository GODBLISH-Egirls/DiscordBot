'''
Loads bot configuration from YAML files.
By default, this simply loads the default
configuration located at `config-default.yml`.
'''
import dotenv
import os
from typing import Optional
import yaml

try:
    dotenv.load_dotenv()
except ModuleNotFoundError:
    pass

def _env_var_constructor(loader, node):
    """
    Implements a custom YAML tag for loading optional environment
    variables. If the environment variable is set, returns the
    value of it. Otherwise, returns `None`.

    Example usage in the YAML configuration:

        # Optional app configuration. Set `MY_APP_KEY` in the environment to use it.
        application:
            key: !ENV 'MY_APP_KEY'
    """

    default = None

    # Check if the node is a plain string value
    if node.id == 'scalar':
        value = loader.construct_scalar(node)
        key = str(value)
    else:
        # The node value is a list
        value = loader.construct_sequence(node)

        if len(value) >= 2:
            # If we have at least two values, then we have both a key and a default value
            default = value[1]
            key = value[0]
        else:
            # Otherwise, we just have a key
            key = value[0]

    return os.getenv(key, default)

yaml.SafeLoader.add_constructor("!ENV", _env_var_constructor)

with open('config-default.yml', encoding='UTF-8') as config_file:
    CONFIG_YAML = yaml.safe_load(config_file)

class YAMLInitializer(type):
    subsection = None

    def __getattr__(cls, name):
        name = name.lower()

        try:
            if cls.subsection is not None:
                return CONFIG_YAML[cls.section][cls.subsection][name]
            return CONFIG_YAML[cls.section][name]
        except KeyError as e:
            dotted_path = '.'.join(
                (cls.section, cls.subsection, name)
                if cls.subsection is not None else (cls.section, name)
            )
            print(f"Tried accessing configuration variable at `{dotted_path}`, but it could not be found.")
            raise AttributeError(repr(name)) from e

    def __getitem__(cls, name):
        return cls.__getattr__(name)

    def __iter__(cls):
        """Return generator of key: value pairs of current constants class' config values."""
        for name in cls.__annotations__:
            yield name, getattr(cls, name)

class BotConfig(metaclass=YAMLInitializer):
    section = 'bot'

    prefix: str
    sentry_dsn: Optional[str]
    token: str
    trace_loggers: Optional[str]

MAIN_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(MAIN_DIR, os.pardir))