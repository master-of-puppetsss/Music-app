FROM python:3.8

# set work directory
WORKDIR /usr/src/app
RUN mkdir /usr/src/app/staticfiles

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

## update apt
RUN apt-get update && apt-get install -y postgresql gcc python3-dev musl-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .






