
# -*- coding: utf-8 -*-

# This is a custom module for Hikka Userbot
# Author: Your Name
# Description: Creates a big heart from small hearts with the text "МАНЯ ❤️" inside.

from .. import loader, utils

class HeartCreatorMod(loader.Module):
    """Creates a big heart from small hearts with text inside."""
    strings = {"name": "HeartCreator"}

    async def heartcmd(self, message):
        """Creates a heart with a message inside.
        Usage: .heart
        """
        big_heart = [
            "💖💖💖       💖💖💖",
            "💖💖💖💖   💖💖💖💖",
            "💖💖💖💖💖💖💖💖💖",
            "  💖💖💖💖💖💖💖",
            "    💖💖💖💖💖",
            "      💖💖💖",
            "        💖"
        ]

        text_inside = [
            "  М  А  Н  Я  ",
            "       ❤️       "
        ]

        result = "❤️ <b>Big Heart for You</b> ❤️\n"
        for line in big_heart:
            result += f"<code>{line}</code>\n"

        result += "\n"

        for line in text_inside:
            result += f"<b>{line}</b>\n"

        await message.edit(result)
