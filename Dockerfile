FROM ubuntu:20.04

RUN apt update && apt-get install -y curl && apt-get install -y python3 && apt-get install -y python3-pip

WORKDIR /group4
COPY . /group4

RUN python3 -m pip install -r requirements.txt
CMD ["bash", "launch.sh"]
