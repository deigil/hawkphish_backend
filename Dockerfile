FROM python:3.10.12

# Set work directory
WORKDIR /app

# Install dependencies
COPY req.txt /djangoapp/
RUN pip install --no-cache-dir -r req.txt

# Copy project
COPY . .

