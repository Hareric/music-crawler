# coding=utf-8

path = '陈奕迅'
singer_id = 7
class_id = 3
num = 10

import os
import random
import json


def get_all_file(root_path):
    list_dirs = os.walk(root_path)
    song_info_list = []
    for root, dirs, files in list_dirs:
        # for d in dirs:
        #     print os.path.join(root, d)
        for f in files:
            song_info_list.append(os.path.join(root, f))
    return song_info_list
# INSERT INTO `app_Music` (`name`, `src`, `lyric`, `music_id`, `listeners`) VALUES
# INSERT INTO `app_singerRmusic` (`singer_id`, `music_id`) VALUES

if __name__ == '__main__':
    songs_info = get_all_file(path)
    music_ids = []
    print "INSERT INTO `app_Music` (`name`, `src`, `lyric`, `music_id`, `listeners`) VALUES"
    for info in songs_info[:num]:
        line = open(info, 'r').readline()
        res = json.loads(line)
        # for k in res:
        #     print k
        #     print res[k]
        #     print '---------------'
        music_ids.append(res['id'])
        print " ('%s', '%s', '%s', %d, %d)," % (res['name'].encode("utf-8"), res['mp3Url'].encode("utf-8"), '该歌曲暂无歌词', res['id'], random.random()*10000)

    print "INSERT INTO `app_singerRmusic` (`singer_id`, `music_id`) VALUES"
    for music_id in music_ids:
        print " (%d, %d)," % (singer_id, music_id)

    print "INSERT INTO `app_musicRclass` (`class_id`, `music_id`) VALUES"
    for music_id in music_ids:
        print " (%d, %d)," % (class_id, music_id)
