FROM python:3.12-slim

WORKDIR /app

COPY src/requirements.txt /app/src/requirements.txt
RUN pip install --no-cache-dir -r /app/src/requirements.txt

COPY src /app/src

EXPOSE 5000

CMD ["python", "src/app.py"]
