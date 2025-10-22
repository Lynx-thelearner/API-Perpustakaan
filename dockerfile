#image python
FROM python:3.11-slim

#set enviroment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    LANG=C.UTF-8 

#set work directory
WORKDIR /app

#copy requirements file
COPY requirements.txt pyproject.toml uv.lock ./

# install system dependencies for psycopg2
RUN apt-get update && apt-get install -y build-essential libpq-dev gcc && rm -rf /var/lib/apt/lists/*

#install dependencies
RUN uv pip install --no-cache-dir -r requirements.txt

#copy project
COPY . .

#buat memastikan bisa import folder app
ENV PYTHONPATH=/app

#run server di port 8000
EXPOSE 8000

#Run server
CMD ["uvicorn", "main:app","--host", "0.0.0.0", "--port", "8000"]

