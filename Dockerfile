FROM python:3.9-slim
WORKDIR /app
COPY fetch_top_models.py /app/fetch_top_models.py
RUN pip install requests
CMD ["python", "fetch_top_models.py"]