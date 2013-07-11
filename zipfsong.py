import operator

def zipfsong():
    quality_list = {}
    song_list = []
    request = raw_input()
    total_songs = int(request.split(" ")[0])
    songs_to_pick = int(request.split(" ")[1])
    for i in xrange(0, total_songs):
        song = raw_input()
        song_list.append(song)
    for song in song_list:
        song_details = song.split(' ')
        song_index = float(song_list.index(song)+1)
        fi = float(song_details[0])
        zi = 1/(song_index)
        song_name = song_details[1]
        quality_list[song_name] = fi/zi
    top_list = sorted(quality_list.iteritems(), key=operator.itemgetter(1))[::-1]
    top_song_names = []
    for i in xrange(0,songs_to_pick):
        top_song_names.append(top_list[i][0].rstrip('\n'))
    for song in top_song_names:
        print song

if __name__ == "__main__":
    zipfsong()
