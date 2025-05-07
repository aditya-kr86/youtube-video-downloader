from yt_dlp import YoutubeDL
import os

output_dir = "downloads"
os.makedirs(output_dir, exist_ok=True)

def progress_hook(d):
    if d['status'] == 'downloading':
        print(f"\rDownloading: {d['_percent_str'].strip()} at {d['_speed_str']} ETA {d['_eta_str']}", end='')
    elif d['status'] == 'finished':
        print(f"\n✅ Finished downloading: {d['filename']}")
    elif d['status'] == 'error':
        print("\n❌ Download error")

def download_high_res_video(url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'noplaylist': True,
        'progress_hooks': [progress_hook],
        'merge_output_format': 'mp4',
        'quiet': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Main
url = input("Enter YouTube URL: ")
download_high_res_video(url)
