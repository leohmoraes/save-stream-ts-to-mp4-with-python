import requests
import ffmpeg_streaming
from ffmpeg_streaming import Formats



#Link obtained with Chrome>Inspector>Network/Filter: m3u8
links = {
'https://...../index.m3u8',
'http.....index.m3u8'    
}

#code login created with Chrome->Inspector:CopyCurl -> After in Postman, import raw data -> Em button code, choice Python
def doLogin():
    url = "https://.....users/sign_in"

    payload='...'
    headers = {
    'authority': ',,,,',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'origin': '.....',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://...../sign_in',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': '.......'
    }

    return requests.request("POST", url, headers=headers, data=payload)


#downloading TLS and saving in Mp4
def convertMp4(urlVideo,seq):
    seq="{:0>2d}".format(seq)
    outputName="videos/Name - " + seq + ".mp4"

    print(seq, outputName, urlVideo)
    video = ffmpeg_streaming.input(urlVideo)
    stream = video.stream2file(Formats.h264())
    stream.output(outputName) #, monitor=monitor)


def start():
    i=0
    for link in links:
        i+=1
        convertMp4(link,i)

        
response=doLogin()
print(f"Status Login: {response.status_code}")
print(f"Qty Videos: {len(links)}")
start()



    
