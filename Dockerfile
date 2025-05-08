FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["sh", "-c", "gunicorn portfolio_project.wsgi --bind 0.0.0.0:${PORT}"]