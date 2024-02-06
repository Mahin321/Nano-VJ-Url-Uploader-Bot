import logging
import math
import os
import time

from config import Config
from translation import Translation

# Setup logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Function to track upload/download progress for Pyrogram
async def progress_for_pyrogram(
    current,
    total,
    ud_type,
    message,
    start
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

        # Choose symbols for progress bar based on ud_type
        filled_symbol = '■'
        empty_symbol = '□'

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

# Main function
def main():
    # Example usage of the functions
    start_time = time.time()
    total_upload_size = 1024 * 1024 * 10  # 10 MB for upload
    total_download_size = 1024 * 1024 * 20  # 20 MB for download
    for current_upload_size, current_download_size in zip(range(0, total_upload_size, 1024), range(0, total_download_size, 1024)):
        # Assuming "Uploading" as ud_type for upload progress
        await progress_for_pyrogram(current_upload_size, total_upload_size, "Uploading", "ᴛʜᴀɴᴋꜱ ғᴏʀ ᴜꜱɪɴɢ ᴍᴇ", start_time)
        # Assuming "Downloading" as ud_type for download progress
        await progress_for_pyrogram(current_download_size, total_download_size, "Downloading", "ᴛʜᴀɴᴋꜱ ғᴏʀ ᴜꜱɪɴɢ ᴍᴇ", start_time)
        time.sleep(0.1)

if __name__ == "__main__":
    main()
