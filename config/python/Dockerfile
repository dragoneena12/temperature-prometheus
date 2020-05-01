FROM python:3.8
WORKDIR /app
EXPOSE 8000

COPY ./config/python/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./config/python/app /app

CMD ["python", "app.py"]