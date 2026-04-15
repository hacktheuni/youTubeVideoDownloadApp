# YT Downloader Pro 🎮

Welcome to **YT Downloader Pro**, an aesthetically pleasing, feature-rich web application built with Flask and `yt-dlp`. 
It allows users to quickly download YouTube videos or extract audio directly from URLs, all wrapped in a sleek, customized Gaming Dark Theme UI.

## Features ✨
- **Dynamic Quality Selection**: Download video files exactly how you need them. Choose between `Best Quality`, `1080p`, `720p`, `480p`, or simply grab the `Audio Only`.
- **Sleek UI**: A beautiful, Cyberpunk-inspired frosted-glass UI crafted with vanilla CSS.
- **Background Merging**: Automatically leverages `ffmpeg` completely behind the scenes to accurately merge high-quality video variants with audio so your output is a clean `.mp4`.
- **Easy Setup**: Fully containerized using Docker, avoiding any tricky local dependency issues.

## Prerequisites 🛠️
You have two ways to run this project:
- **Docker** (Highly Recommended)
- Native **Python 3.11+** with `ffmpeg` installed on your machine.

---

## 🐳 Quick Start (Using Docker)

Using Docker is the easiest way to ensure `yt-dlp` and `ffmpeg` act predictably without setting up your own machine environments. 

**1. Clone or download the repository**, then open your terminal to the project directory.

**2. Build the Docker Image:**
```bash
docker build -t yt-downloader-app .
```
*(Note: This might take a minute or two as it installs Python and `ffmpeg`)*

**3. Run the Container:**
```bash
docker run -p 5000:5000 yt-downloader-app
```
**4. Access the Application:**
Open your browser and navigate to -> [http://localhost:5000](http://localhost:5000)

---

## 🐍 Manual Start (Using Python)

If you have `ffmpeg` installed on your computer and prefer running the code locally without a container:

**1. Create a virtual environment & install dependencies:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirement.txt
```

**2. Run the application:**
```bash
python3 app.py
```

**3. Access the Application:**
Navigate to -> [http://localhost:5000](http://localhost:5000)

---

## Technologies Used
* **Backend:** Flask / Python
* **Extraction:** `yt-dlp`
* **Processing:** `ffmpeg`
* **Frontend:** HTML5 / CSS3 (No external CSS frameworks)
* **Serving:** Gunicorn

## Disclaimer
This application is made for educational purposes. Please respect copyright laws and the terms of service of any platform you are extracting media from.
