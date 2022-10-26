from pytube import Playlist

video = input('enter playlist')

pl = Playlist(video)

print(f'downloading{pl.title}')

for x in pl.videos:
    x.streams.get_highest_resolution().download()
    print(' done ' + x.title)