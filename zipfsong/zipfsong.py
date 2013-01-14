#!/usr/bin/python
"""Solution to the zpifsong problem presented at http://www.spotify.com/se/jobs/tech/zipfsong/"""
__author__ = "Gustaf Hallberg"
__copyrights__ = "Copyright 2013, Gustaf Hallberg"
__email__ = "ghallberg@gmail.com"

import sys

def best_from_album(album, num_songs):
    def _cmp(x,y):
        x_name, x_track, x_score = x
        y_name, y_track, y_score = y

        score_result = cmp(x_score, y_score)
        if score_result != 0:
            return score_result
        else:
            return  cmp(y_track, x_track)

    def name(track):
        return track[0]

    zipfs= []
    for track_num, song_info in enumerate(album, 1):
        num_plays, track_name = song_info
        if track_num == 1:
            first_plays = num_plays

        pred_plays = first_plays*(1.0/track_num)

        quality = num_plays / pred_plays

        zipfs.append((track_name, track_num, quality))

    return [name(track) for track in
            list(reversed(sorted(zipfs, _cmp)))[:num_songs]]

if __name__ == '__main__':

    num_songs, songs_to_select = sys.stdin.readline().strip().split(" ")
    print("num: ", num_songs,"sel: ",songs_to_select)
    album = [row.strip().split(" ") for row in sys.stdin.readlines()]
    album = [(int(plays), name) for plays, name in album]

    for name in best_from_album(album, int(songs_to_select)):
        print(name)






