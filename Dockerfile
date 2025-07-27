# Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY app.py .

RUN pip install --no-cache-dir streamlit requests

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

# docker build --platform linux/amd64 -t wontheoscar/streamlit-ollama:latest .
# docker push wontheoscar/streamlit-ollama:latest
