FROM python:3.10-slim

# Встановлюємо системні залежності (включаючи Git)
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["sh", "-c", "gunicorn portfolio_project.wsgi --bind 0.0.0.0:8000"]