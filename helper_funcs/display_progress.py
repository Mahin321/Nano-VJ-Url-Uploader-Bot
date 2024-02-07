import logging
import math
import os
import time
import shutil
from config import Config
from translation import Translation

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def progress_for_pyrogram(
    current,
    total,
    ud_type,
    message,
    start,
    direction="upload"  # Added parameter for progress direction
):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)

        # Choose symbols for progress bar based on direction
        if direction == "upload":
            filled_symbol = '●'
            empty_symbol = '○'
        elif direction == "download":
            filled_symbol = '●'
            empty_symbol = '○'

        # Calculate number of filled and empty symbols
        filled_count = math.floor(percentage / 5)
        empty_count = 20 - filled_count

        # Construct progress bar
        progress = f"[{filled_symbol * filled_count}{empty_symbol * empty_count}] \nP: {round(percentage, 2)}%\n"

        tmp = progress + f"{humanbytes(current)} of {humanbytes(total)}\nSpeed: {humanbytes(speed)}/s\nETA: {estimated_total_time}\n"
        try:
            await message.edit(
                text=f"{ud_type}\n {tmp}"
            )
        except:
            pass


def humanbytes(size):
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'


def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") + \
        ((str(hours) + "h, ") if hours else "") + \
        ((str(minutes) + "m, ") if minutes else "") + \
        ((str(seconds) + "s, ") if seconds else "") + \
        ((str(milliseconds) + "ms, ") if milliseconds else "")
    return tmp[:-2]
