import requests
import ffmpeg_streaming
from ffmpeg_streaming import Formats


# Links obtained with Chrome > Inspector > Network / Filter: m3u8
links = [
    'https://...../index.m3u8',
    'http.....index.m3u8',
]


# Login code created with Chrome -> Inspector: Copy as cURL
# Then in Postman: import raw data -> Code button -> choose Python
def do_login():
    url = "https://.....users/sign_in"

    payload = '...'
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
        'cookie': '.......',
    }

    return requests.request("POST", url, headers=headers, data=payload)


# Downloading TS stream and saving as MP4
def convert_mp4(url_video, seq):
    seq_str = "{:0>2d}".format(seq)
    output_name = "videos/Name - " + seq_str + ".mp4"

    print(seq_str, output_name, url_video)
    video = ffmpeg_streaming.input(url_video)
    stream = video.stream2file(Formats.h264())
    stream.output(output_name)


def start():
    for i, link in enumerate(links, start=1):
        convert_mp4(link, i)


if __name__ == "__main__":
    response = do_login()
    print(f"Status Login: {response.status_code}")
    print(f"Qty Videos: {len(links)}")
    start()

