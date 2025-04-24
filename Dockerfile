FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y libpq-dev gcc

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD [ "uvicorn", "src.main.server.server:app", "--host", "0.0.0.0", "--port", "8000" ]