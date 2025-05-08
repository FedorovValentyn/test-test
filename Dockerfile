FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["gunicorn", "portfolio_project.wsgi", "--bind", "0.0.0.0:8000"]