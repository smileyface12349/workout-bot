# Using the bot

`!ping` Check the bot's response time

`!start` Start the workout messages in your current channel

`!stop` Stop playing workout messages


# Installation Instructions

1. Install the packages as specified in `requirements.txt`. You may want to make a virtual environment.
2. Make a bot user on [discord.com/developers](https://discord.com/developers) and copy its token.
3. Create a file `credentials.json` and put `{"token": "YOUR_TOKEN"}` in it.
4. Install [ffmpeg](https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl-shared.zip) and extract it to a folder called "ffmpeg". Check that `ffmpeg/bin/ffmpeg.exe` exists.
5. Run `main.py` and hope it all works!

# Config

You can configure:
- The audio file to use
- The delay between messages
- The path that ffmpeg is installed at

This is all configured within `config.json`
