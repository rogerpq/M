FROM python:3.10-slim-buster
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y git curl python3-pip ffmpeg mediainfo p7zip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g npm@8.19.4 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
RUN python3 -m pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
ENV PATH="/home/StringGenBot/bin:$PATH"
CMD ["python3","-m","StringGenBot"]
