FROM python:3.9-slim-bullseye

# Minimal system dependencies
RUN apt-get update && \
    apt-get install -y git curl ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app
WORKDIR /app

# Upgrade pip & install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Start the bot
CMD ["bash", "start.sh"]
