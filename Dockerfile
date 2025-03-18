# Base image
FROM python:3.9-slim-buster

# Build stage
FROM base as builder
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Runtime stage
FROM base
WORKDIR /app
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# Copy project files
COPY . .

# Environment variables
ENV FLASK_APP=app/api/app.py
ENV FLASK_ENV=production
ENV BLOCKCHAIN_NETWORK=http://ganache:8545

EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]