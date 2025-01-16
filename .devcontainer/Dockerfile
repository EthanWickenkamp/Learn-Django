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

COPY requirements.txt .
#copy requirements to the root


RUN pip install --no-cache-dir -r requirements.txt
#install requirements

COPY . .
#copy all files into container directory

EXPOSE 8000
# not necessary? but good practice to list ports used
# WORKDIR /learn
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#start django development server on port 8000
# doesent work?


#NOW I CAN EDIT
