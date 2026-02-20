import requests
import m3u8
import re

# pip3 install requests
# pip3 install m3u8
# pip3 install regex
# Run:
# python3 m3u8info.py

"""
This script changes relative paths in index.m3u8 to absolute URLs.
It writes one file per link with the updated URLs.
"""

links = [
    'https://videos......m3u8',
    'https://videos....index.m3u8',
]


def get_info(url_video, seq):
    seq_str = "{:0>2d}".format(seq)
    playlist = m3u8.load(url_video)

    # Strip /index.m3u8 to get the base path
    playlist.base_path = re.sub(r"/index(.*).m3u8", "", url_video)

    playlist.dump("m3u8/playlist-" + seq_str + ".m3u8")
    print("seq", seq_str, "playlist.base_path", playlist.base_path, "url", url_video)


def start():
    for i, link in enumerate(links, start=1):
        get_info(link, i)


if __name__ == "__main__":
    print(f"Qty of videos: {len(links)}")
    start()

