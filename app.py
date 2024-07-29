from pathlib import Path
from flask import Flask, render_template, request, send_from_directory
import yt_dlp

app = Flask(__name__)

# Define the download directory using pathlib
download_dir = Path(__file__).parent / 'downloads'
download_dir.mkdir(exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/downloadVideo', methods=['GET'])
def downloadVideo():
    videoLink = request.args.get('videoLink')
    result = download_video(videoLink)
    return result

def download_video(url):
    ydl_opts = {
        'format': 'bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': str(download_dir / '%(title)s.%(ext)s'),
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            return "Download completed!"
    except Exception as e:
        return f"An error occurred: {e}"

@app.route('/downloads/<filename>')
def download_file(filename):
    return send_from_directory(download_dir, filename)

if __name__ == '__main__':
    app.run(debug=True)
