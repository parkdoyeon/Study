# https://programmers.co.kr/learn/courses/30/lessons/42579
# album = dict.fromkeys(genres, 0)
#     album_bysong = dict.fromkeys(zip(genres, )
#     for i in range(len(genres)):
#         album[genres[i]] += plays[i]
#         album_bysong[genres[i]] += [(plays[i], i)]
#     toptwo = sorted(album.values())[:2]
    
#     answer = []
#     for i in range(2):
#         for key in album.keys():
#             if toptwo[i] == album[key]:
#                 album_bysong[key].sort()
#                 answer.extend([song[1] for song in album_bysong[key][:2]])
#                 break



genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 500, 2500]

albumrank = dict.fromkeys(genres, 0)
album_songs = { g : list() for g in genres }
for i in range(len(plays)):
    albumrank[genres[i]] += plays[i]
    album_songs[genres[i]] += [(plays[i], i)]
albumrank_tuple = [(albumrank[g], g) for g in albumrank.keys()]
albumrank_tuple.sort(reverse=True)
print(album_songs)
answer = []
for play, genre in albumrank_tuple:
    count = 1
    album_songs[genre].sort(key=lambda x: (x[0], -x[1]))
    print(album_songs[genre])
    while count < 3 and len(album_songs[genre]) > 0:
        answer.append(album_songs[genre].pop()[1])
        count += 1

print(answer)
