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

def solution(genres, plays):
    genre_play_dict = defaultdict(lambda: 0)
    for genre, play in zip(genres, plays):
        genre_play_dict[genre] += play

    genre_rank = [genre for genre, play in sorted(genre_play_dict.items(), key=itemgetter(1), reverse=True)]

    final_dict = defaultdict(lambda: [])
    for i, genre_play_tuple in enumerate(zip(genres, plays)):
        final_dict[genre_play_tuple[0]].append((genre_play_tuple[1], i))
    print(final_dict)
    answer = []
    for genre in genre_rank:
        one_genre_list = sorted(final_dict[genre], key=itemgetter(0), reverse=True)
        if len(one_genre_list) > 1:
            answer.append(one_genre_list[0][1])
            answer.append(one_genre_list[1][1])
        else:
            answer.append(one_genre_list[0][1])

    return answer


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
