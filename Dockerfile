FROM python:3.11-slim

# Install ffmpeg for yt-dlp to merge video and audio formats
RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg nodejs && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirement.txt and install Python dependencies
COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Start the application using gunicorn (specified in requirement.txt)
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "--timeout", "900", "app:app"]
