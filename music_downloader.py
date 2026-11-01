#pip install yt-dlp
#pip install imageio-ffmpeg

import yt_dlp

url = "https://www.youtube.com/watch?v=-HLgn5JpE6Y"

# configuration options (mimics command-line flags)


ydl_opts = {

"format": "bestaudio/best",
    # 'ffmpeg_location': r'C:\ffmpeg\bin',

    "postprocessors": [

{

"key": "FFmpegExtractAudio",

"preferredcodec": "mp3",

"preferredquality": "192", # You can change to '320' or '0'

}

],

}
#
# # use a context manager to handle the download
#
# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     ydl.download([url])
#     print("Download Completed")

# ydl_opts = {
#     "format": "bestvideo*+bestaudio/best",
#     "outtmpl": "%(title)s.%(ext)s",
# }

# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     ydl.download([url])