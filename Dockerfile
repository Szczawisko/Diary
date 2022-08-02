FROM python:3
WORKDIR /site
COPY requirements.txt /site/
RUN pip install -r requirements.txt
COPY . /site/