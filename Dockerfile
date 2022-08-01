FROM python:3.9-slim-buster
LABEL maintainer="Mounir Abbas"
WORKDIR /app
ADD app.py .
ADD requirements.txt .
RUN apt-get upgrade -y
RUN pip install --upgrade pip
RUN pip3 install --upgrade setuptools wheel
RUN pip3 install --no-cache-dir -r requirements.txt

# RUN pip install uwsgi
EXPOSE 1097
CMD uvicorn app:app --reload --port 1097 --host 0.0.0.0
