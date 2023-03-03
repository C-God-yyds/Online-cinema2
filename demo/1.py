from aip import AipSpeech
import os
def exccute_cmd():
    oldfile ="E://shankeda//v-online//data//1.m4a"
    newfile ="E://shankeda//v-online//data//1.pcm"
    cmd_str ="ffmpeg -y -i %s -acodec pcm_s16le -f s16le -ac 1 -ar 16000 %s" % (oldfile, newfile)
    os.system(cmd_str)
exccute_cmd()