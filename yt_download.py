import yt_dlp

def download_youtube_videos(urls, output_folder="./downloads"):
    ydl_opts = {
        'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
        'format': 'best[ext=mp4][height<=?1080]',
        'postprocessors': [
            {
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }
        ],
    }

    downloaded_videos = []

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for url in urls:
            info_dict = ydl.extract_info(url, download=True)
            if 'entries' in info_dict:
                for entry in info_dict['entries']:
                    video_height = entry['height']
                    video_name = entry['title'] + '.' + entry['ext']
                    downloaded_videos.append({'name': video_name, 'height': video_height})
            else:
                video_height = info_dict['height']
                video_name = info_dict['title'] + '.' + info_dict['ext']
                downloaded_videos.append({'name': video_name, 'height': video_height})

    return downloaded_videos

if __name__ == "__main__":
    video_urls = []
    video_urls.append(input())

    output_folder = "./downloads"
    downloaded_videos = download_youtube_videos(video_urls, output_folder)

    print("Downloaded videos:")
    for video_info in downloaded_videos:
        print(f"Name: {video_info['name']}, Height: {video_info['height']} pixels")
