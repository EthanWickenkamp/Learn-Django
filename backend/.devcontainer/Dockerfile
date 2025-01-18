FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    curl \
    wget \
    git \
    bash \
    # get basic commands because -slim
    pkg-config\
    build-essential\
    python3-dev\
    default-libmysqlclient-dev\
    #sql client dependencies
    && rm -rf /var/lib/apt/lists/*
    #remove leftover


WORKDIR /app 
#set working directory to app
#where docker will execute next commands

COPY requirements.txt .
#copy requirements into root of the workdir
RUN pip install --no-cache-dir -r requirements.txt
#install requirements that we just copied in
# no cache reduces image size, r flag is ?
COPY . .
# by copying all after pip install docker can use last cached layer if same requirements


#CMD ["bash"]
#done in compose instead?

EXPOSE 8000
# not necessary here but good practice to list ports used

