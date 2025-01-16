FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    curl \
    wget \
    git \
    bash \
    && rm -rf /var/lib/apt/lists/*
# get basic commands because -slim

WORKDIR /app 
#set working directory to app

COPY . .
#copy all files to the root of workdir
RUN pip install --no-cache-dir -r requirements.txt
#install requirements that we just copied in

EXPOSE 8000
# not necessary? but good practice to list ports used

