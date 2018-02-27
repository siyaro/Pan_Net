FROM python:2.7

COPY getweather.py /app/getweather.py
ENV HOME=/app
WORKDIR /app

RUN pip install pyowm

CMD ["python",  "/app/getweather.py", ">/dev/null"]
