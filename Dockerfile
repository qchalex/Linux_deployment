FROM ubuntu:20.04

RUN mkdir -p /group4
RUN apt update && apt-get install -y curl && apt-get install -y python3 && apt-get install -y python3-pip

WORKDIR /group4

COPY requirements.txt .
COPY run.sh .
COPY collect.sh .
COPY transform.py .
COPY webapp/main.py .
COPY webapp/layout.py .
COPY webapp/sidebar.py .
COPY webapp/navbar.py .
COPY webapp/style/sidebar_style.py .

RUN python3 -m pip install -r requirements.txt
CMD ["bash", "run.sh"]
