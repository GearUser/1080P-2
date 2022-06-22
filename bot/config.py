#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = config("APP_ID", cast=int)
    API_HASH = config("API_HASH")
    BOT_TOKEN = config("BOT_TOKEN")
    DEV = 1322549723
    OWNER = config("OWNER")
    FFMPEG = config(
        "FFMPEG",
        default='''ffmpeg -i "{}" -pix_fmt yuv420p10le -r 24000/1001 -s 1920x1080 -preset slow -c:v libx265 -crf 21 -x265-params ref=6:limit-refs=0:limit-modes:me=3:rd=4:subme=4:rc-lookahead=120:aq-mode=3:aq-strength=0.70:deblock=-1:-1:qcomp=0.63:cbqpoffs=-2:crqpoffs=-2:psy-rd=0.60:psy-rdoq=1.30:min-keyint=24:keyint=240:rdoq-level=2:bframes=8:b-adapt=2:frame-threads=3 -map 0:v -c:a libopus -b:a 112k -map 0:a -c:s copy -map 0:s? "{}"''',
    )
    THUMB = config(
        "THUMBNAIL", default="www.google.com"
    )
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
