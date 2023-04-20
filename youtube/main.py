from pytube.captions import os

# url = input('Enter a YouTube URL: ')
# url = 'https://www.youtube.com/watch?v=m4ZVHMoPcnc'
# url = "https://www.youtube.com/watch?v=g2o22C3CRfU&list=PL0vfts4VzfNiI1BsIK5u7LpPaIDKMJIDN&index=2"
url = "https://youtube.com/playlist?list=PL0vfts4VzfNiI1BsIK5u7LpPaIDKMJIDN"

# yt = youtube.get_data(url)

def print_video_info(yt):
    print('Title: ', yt.title)
    print('Views: ', yt.views)
    print('Length: ', yt.length)
    print('Rating: ', yt.rating)
    print('Description: ', yt.description)
    print('Keywords: ', yt.keywords)
    print('Author: ', yt.author)
    print('Streams: ', yt.streams)


def print_playlist_info(pl):
    print('Title: ', pl.title)
    print('Owner: ', pl.owner_url)
    print('Video Count: ', pl.video_count)
    print('Videos: ', pl.videos)


# 메뉴를 출력하고 사용자로부터 원하는 타입을 입력 받는다.
# type = youtube.stream_type_menu()

# 사용자가 입력한 값을 이용해, 해당 타입의 스트림을 출력
# stream = youtube.stream_menu(yt, type)

# 스트림을 다운로드
# youtube.download(stream)

# pl = youtube.get_playlist(url)

# for url in pl.video_urls[:3]:
#     yt = youtube.get_data(url)
#     print_video_info(yt)

# print_playlist_info(pl)
