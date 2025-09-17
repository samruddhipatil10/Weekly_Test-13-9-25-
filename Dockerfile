FROM python:3.11-slim

# Set working dir
WORKDIR /app

# Copy & install dependencies first (cache)
COPY requirements.txt .
RUN python -m pip install --upgrade pip \
 && pip install -r requirements.txt

# Copy application code
COPY . .

# Expose port and run with gunicorn (good for production)
ENV PORT 5000
EXPOSE 5000
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000", "--workers", "2"]
