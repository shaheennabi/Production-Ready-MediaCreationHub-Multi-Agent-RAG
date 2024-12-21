FROM python:3.10-slim

WORKDIR /app

COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Load environment variables from GitHub secrets
ENV OPENAI_API_KEY=$OPENAI_API_KEY
ENV WEATHER_API_KEY=$WEATHER_API_KEY
ENV SERPER_API_KEY=$SERPER_API_KEY
ENV AMADEUS_API_KEY=$AMADEUS_API_KEY
ENV AMADEUS_API_SECRET=$AMADEUS_API_SECRET

# Expose the port Streamlit uses
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "deployment/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
