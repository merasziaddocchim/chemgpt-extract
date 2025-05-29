FROM python:3.10-slim

WORKDIR /app

# Install system dependencies for lxml, etc.
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libxml2 \
    libxslt1.1 \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY main.py .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
# Force rebuild: <today's date>
