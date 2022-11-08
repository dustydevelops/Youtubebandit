# pip install youtube_dl
''' when you run this, it will download mp3 files associated to every Youtube url that you put in videoUrls.txt'''

import youtube_dl


videoLinks= []

# open file and read the content in a list
with open(r'C:\Users\dusti\PycharmProjects\youtubeBandit2\videoUrls.txt', 'r') as fp:
    for line in fp:
        # remove linebreak from a current name
        # linebreak is the last character of each line
        x = line[:-1]

        # add current item to the list
        videoLinks.append(x)

# display list
print(videoLinks)


def download_ytvid_as_mp3(video_url):

    video_info = youtube_dl.YoutubeDL().extract_info(url=video_url, download=False)
    filename = f"{video_info['title']}.mp3"
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': filename,
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    print("Download complete... {}".format(filename))



iteration=0

while True:
    try:
        video_url = videoLinks[iteration]
        video_info = youtube_dl.YoutubeDL().extract_info(url=video_url, download=False)
        song = video_info['title']
        print(song)
        download_ytvid_as_mp3(video_url)

        iteration = iteration + 1

        if videoLinks[iteration] == videoLinks[-1]:
            break
    except:

        print('---------------ERROR downloading :::',song )
        iteration = iteration + 1
        pass


