FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /harrp
COPY requirements.txt /harrp/
RUN pip install -r requirements.txt
COPY . /harrp/