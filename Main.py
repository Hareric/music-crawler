#!/usr/bin/env python
# coding=utf-8

"""
this file show you how to crawl a playlist 
and save the mp3 files and music info file into disk 

you should provide follow infos : 
	1、play_list url
	2、your cookie in login state
	3、directory paths to save PlayListInfo josn files、musicInfo josn files and mp3 files
	  you can change those directory path in Constants.py

"""

from PlayListDownloader import *
from PlayListParser import *

# replace the placeHolder with your own cookie
cookie = 'palaceHolder'
# playlist url  example, change id param if you want to crawl other play lists
'''
3104928 张惠妹
47112384 周杰伦
759955 陈奕迅
'''
url = "http://music.163.com/api/playlist/detail?id=759955"

# download the play list as json text
playListDownloader = PlayListDownloader(timeout=5, cookie=cookie)
playListJsonText = playListDownloader.downloadPlayList(url)

# init the MP3Crawler with 10 work threads
crawler = MP3Crawler("MP3Crawler", 10)
crawler.start()

PlayListParser.init()
jsonData = PlayListParser.parser(playListJsonText)
# save the playListInfo
if PlayListParser.savePlayListInfo(jsonData):
    # save music Info and  mp3 files
    PlayListParser.downloadMusics(jsonData, crawler)
    # wait to complete
    crawler.waitUtilComplete()
else:
    crawler.stop()
