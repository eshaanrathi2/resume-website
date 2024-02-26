# Use Python image
FROM python:3.9

# Set working directory
WORKDIR /tests

# Copy requirements.txt and install dependencies
COPY src/tests/requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the test script
COPY src/tests/tests.py .

# Command to run the test script
# CMD ["python3", "tests.py"]