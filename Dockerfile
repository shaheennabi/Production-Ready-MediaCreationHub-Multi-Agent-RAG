# Use an official Python runtime as a base image
FROM python:3.10-slim

WORKDIR /app

COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Load environment variables from .env
ENV OPENAI_API_KEY="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"
ENV WEATHER_API_KEY="5efe50e8064b44d78ca212221241812"
ENV SERPER_API_KEY="21b4dba604da2c9ab1ac2d9162af4fcc03ac516c"
ENV AMADEUS_API_KEY="HyWEEA7FyjASEf1c9OjJv0h1aGB1SvJX"
ENV AMADEUS_API_SECRET="kRmmzV3hqLFW9Z9j"

# Expose the port Streamlit uses
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "deployment/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
