FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

CMD ["sh", "-c", "sleep 10 && alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port 8000 --reload"]
