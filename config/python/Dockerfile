FROM python:3.8
WORKDIR /app

COPY config/python/app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY config/python/app /app

CMD ["python", "app.py"]