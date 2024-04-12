import os
from pytube import YouTube, Playlist

def menu():
    os.system('cls')
    print("YouTube tool by Ema\n\n┌─────────────────────┬────────────────────────┬─────────────┐\n│ 1: Video downloader │ 2: Playlist downloader │ Enter: exit │\n├─────────────────────┴────────────────────────┴─────────────┘")
    choice=input("└ ")
    if choice == "1":
        video_download()
    elif choice == "2":
        playlist_download()
    elif choice == "":
        os.system('cls')
        exit()
    else:
        menu()
        
def on_progress(video_stream, total_size, bytes_remaining):
    total_size = video_stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent = (bytes_downloaded / total_size) * 100
    print("\r" + "▌" * int(percent) + " " * (100 - int(percent)) + " {}%".format(int(percent)), end='')

def convert_time(length):
    if length < 60:
        time = str(length+"sec~")
    elif length < 3600:
        time = str(round((length / 60),2))+" min~"
    else:
        time = str(round((length / 3600),2))+" hours~"
    return time

def video_download():
    os.system('cls')
    print("YT Video downloader\n")
    yt = YouTube(input("[+] Enter video URL: "), on_progress_callback=on_progress)
    print()
    path = input("[+] Enter download path (leave blank for current): ")
    print()
    videos=yt.streams.order_by('resolution')
    video=list(enumerate(videos))
    for i in video:
        print(i)
    download_option = int(input("[+] Choose format by number: "))
    download_video = videos[download_option]
    print("\n[!] Downloading:",yt.title,"| Duration:",convert_time(yt.length),"| Ctrl+C to quit")
    if path == "":
        download_video.download()
    else:
        download_video.download(path)
    input("\n\nDone! Press enter to exit ")
    menu()
    
def playlist_download():
    os.system('cls')
    print("YT Playlist downloader\n")
    playlist = Playlist(input("[+] Enter playlist URL: "))
    path = input("\n[+] Enter download path (leave blank for current): ")
    download_option = int(input("\n[+] Download options max quality available ( 1: Video mp4 | 2: Audio webm ): "))
    print("\n[!] Downloading:",playlist.title,"|",len(playlist.videos),"videos | Ctrl+C to quit")
    for video in playlist:
        yt = YouTube(video, on_progress_callback=on_progress)
        print("\n[-] Downloading",video,"| Duration:",convert_time(yt.length))
        if path == "":
            if download_option == 1:
                yt.streams.get_highest_resolution().download()
            elif download_option == 2:
                yt.streams.filter(only_audio=True).order_by('abr').desc().first().download()
        else:
            if download_option == 1:
                yt.streams.get_highest_resolution().download(path)
            elif download_option == 2:
                yt.streams.filter(only_audio=True).order_by('abr').desc().first().download(path)
        print()
    input("\nDone! Press enter to exit ")
    menu()

os.system('cls')
menu()
