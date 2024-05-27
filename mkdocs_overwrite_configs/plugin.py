import logging

import os
import json

from mkdocs.plugins import BasePlugin

logging.getLogger(__name__)


class OverwriteConfigsPlugin(BasePlugin):

    def __init__(self):
        self._logger = logging.getLogger("mkdocs.overwrite-configs")
        self._logger.setLevel(logging.INFO)

    def on_config(self, config):
        theme = self.config.get("theme")
        if theme and theme.get("palette"):
            config["theme"]["palette"] = []
            palette = theme["palette"]
            if type(palette) == list:
                for item in palette:
                    config["theme"]["palette"].append(item)
                    self._logger.info(f"Added palette item: {item}")

        return config
