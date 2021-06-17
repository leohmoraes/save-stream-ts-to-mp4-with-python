import requests
import m3u8
import reg

##pip3 install request
##pip3 install m3u8
##pip3 install regex
## Run
## python3 m3u8info.py

"""
This script is used to change relative path in index.m3u8 to absolute url of the file
Write a file to each link of index, with the new url
"""

links = {
    'https://videos......m3u8',
    'https://videos....index.m3u8'
}


def getInfo(urlVideo,seq):
    seq="{:0>2d}".format(seq)
    playlist = m3u8.load(urlVideo)

    # /index.m3u8 
    playlist.base_path = re.sub(r"/index(.*).m3u8","", urlVideo) 

    # print(playlist.dumps())
    # for iframe_playlist in playlist.iframe_playlists:
        # print("uri", iframe_playlist.uri)
    
    # if you want to write a file from its content
    playlist.dump("m3u8/playlist-"+seq+".m3u8")
    print( "seq", seq, "playlist.base_uri",playlist.base_path, "url",urlVideo,)


def start():
    i=0
    for link in links:
        i+=1
        getInfo(link,i)

print(f"Qty of vídeos: {len(links)}")
start()
