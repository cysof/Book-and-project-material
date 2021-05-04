 FROM python:3
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /apps
 WORKDIR /apps
 COPY requirements.txt /apps/
 RUN pip install -r requirements.txt
 COPY . /apps/
