

file = open("songs.txt","r")
songs_cont = file.readlines()


count_songs = len(songs_cont)

def time_song(song):
    return song.split(";")[2]

sorted_songs = sorted(songs_cont,key=time_song, reverse=True)
print(sorted_songs)
print(sorted_songs[0].split(";")[0])

dict= {}
for song in songs_cont:
    dict[song.split(";")[1]] = 0

for song in songs_cont:
    dict[song.split(";")[1]] += 1
print(dict)

teams_sort = sorted(dict)
print(teams_sort[0])

