FROM python:3.10-slim

COPY ./Gateway /Gateway
RUN pip install -r /Gateway/requirements.txt
RUN mkdir -p /.mitmproxy
RUN chmod 777 /.mitmproxy


CMD mitmdump -s /Gateway/app.py -p 8000 --listen-host 0.0.0.0