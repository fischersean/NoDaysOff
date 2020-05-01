FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY . /app
WORKDIR /app

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt

