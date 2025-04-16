from flask import Flask, render_template, request, send_file
import yt_dlp
from pathlib import Path
import os
from io import BytesIO

app = Flask(__name__)
download_dir = Path(__file__).parent / 'downloads'
download_dir.mkdir(exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/downloadVideo', methods=['GET'])
def downloadVideo():
    videoLink = request.args.get('videoLink')
    filepath = download_video(videoLink)

    if filepath and os.path.exists(filepath):
        try:
            # Read the file into memory first
            with open(filepath, 'rb') as f:
                file_bytes = BytesIO(f.read())

            # Delete the original file now that we have it in memory
            os.remove(filepath)
            print(f"Deleted file: {filepath}")

            # Send the file to the client from memory
            file_bytes.seek(0)
            return send_file(file_bytes, as_attachment=True, download_name=os.path.basename(filepath))

        except Exception as e:
            return f"Error handling file: {e}"

    return "An error occurred during download."

def download_video(url):
    try:
        ydl_opts = {
            'format': 'bestvideo[height<=1080]+bestaudio/best',
            'outtmpl': str(download_dir / '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

            # Check for merged .mp4 or fallback
            if os.path.exists(filename):
                return filename
            else:
                alt_filename = os.path.splitext(filename)[0] + '.mp4'
                return alt_filename if os.path.exists(alt_filename) else None

    except Exception as e:
        print(f"Download error: {e}")
        return None


if __name__ == '__main__':
    app.run(debug=True)
