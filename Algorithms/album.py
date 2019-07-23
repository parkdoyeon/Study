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

albumrank = sorted([(v,k) for k,v in dict(zip(genres, plays)).items()], reverse=True)
album_bysong = { key : list() for key in genres }
for i in range(len(genres)):
    album_bysong[genres[i]] += [[plays[i],i]]


answer = []
for g in albumrank:
    album_bysong[g[1]].sort(key=lambda x: (x[0], -x[1]))
    print(album_bysong)
    count = 1
    while count < 3 and len(album_bysong[g[1]]) > 0:
        answer.append(album_bysong[g[1]].pop()[1])
        count += 1

print(answer)
