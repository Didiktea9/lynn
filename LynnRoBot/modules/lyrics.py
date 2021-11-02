# Simple get lyrics plugin

"""
from __future__ import unicode_literals

import os
from asyncio import get_running_loop
from functools import partial
from io import BytesIO
from urllib.parse import urlparse

import ffmpeg
import youtube_dl
from pyrogram import filters

from LynnRoBot import aiohttpsession as session
from LynnRoBot import app, arq
from LynnRoBot.core.decorators.errors import capture_err
from LynnRoBot.utils.pastebin import paste

@app.on_message(filters.command("lyrics"))
async def lyrics_func(_, message):
    if len(message.command) < 2:
        return await message.reply_text("**Usage:**\n/lyrics [QUERY]")
    m = await message.reply_text("**Searching**")
    query = message.text.strip().split(None, 1)[1]
    song = await arq.lyrics(query)
    lyrics = song.result
    if len(lyrics) < 4095:
        return await m.edit(f"__{lyrics}__")
    lyrics = await paste(lyrics)
    await m.edit(f"**LYRICS_TOO_LONG:** [URL]({lyrics})")
