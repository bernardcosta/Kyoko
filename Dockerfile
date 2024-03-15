FROM python:3.8-slim-buster
RUN apt-get -y update
RUN apt-get -y install git
RUN apt-get update \
 && apt-get install gcc -y \
 && apt-get clean
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python", "-m", "src.tgm"]