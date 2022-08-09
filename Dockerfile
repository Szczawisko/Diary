FROM python:3
WORKDIR /site
COPY requirements.txt /site/
RUN pip install -r requirements.txt
COPY . /site/

CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000