from aip import AipSpeech
import os
def exccute_cmd():
    oldfile ="E://shankeda//v-online//data//1.m4a"
    newfile ="E://shankeda//v-online//data//1.pcm"
    cmd_str ="ffmpeg -y -i %s -acodec pcm_s16le -f s16le -ac 1 -ar 16000 %s" % (oldfile, newfile)
    os.system(cmd_str)
#exccute_cmd()
    APP_ID = '26068954'
    API_KEY = 'ibUaxGVGwqlpgB6HNPGLi3XB'
    SECRET_KEY = 'yLDYfo4GZYIcASP1lFsfTdprenmxu1Nk'
# 创建 aip 客户端
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


#def read_pcmfile(filepath):
    with open("E://shankeda//v-online//data//1.pcm", "rb") as fp:
        # 客户端调用 aip 接口，语音转文字
        res = client.asr(
            fp.read(),
            "pcm",
            16000,
            {
                'dev_pid': 1536
            }
        )
        print(res)
        return str(res.get("result"))
