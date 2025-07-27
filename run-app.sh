docker run -d \
  --restart unless-stopped \
  -p 8501:8501 \
  -e OLLAMA_API_URL="http://<Node-ip>:11434/api/generate" \
  wontheoscar/streamlit-ollama:latest