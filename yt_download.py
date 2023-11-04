import yt_dlp

def download_youtube_videos(urls, output_folder="./downloads"):
    ydl_opts = {
        'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
        'format': 'best[height=720]',
    }
    
    downloaded_files = []

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for url in urls:
            info_dict = ydl.extract_info(url, download=True)
            if 'entries' in info_dict:
                for entry in info_dict['entries']:
                    downloaded_files.append(entry['title'] + '.' + entry['ext'])
            else:
                downloaded_files.append(info_dict['title'] + '.' + info_dict['ext'])
    return downloaded_files

video_urls = []
video_urls.append(input())
output_folder = "./downloads" 
downloaded_files = download_youtube_videos(video_urls, output_folder)
print("Downloaded files:")
for file in downloaded_files:
    print(file)
