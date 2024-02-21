# Build Docker image
build-image:
    docker-compose build

# Run Docker container
run-docker:
    docker-compose up

# Run tests
test:
    pytest src/tests/

# Clean up containers
clean:
    docker-compose down

# Coverage (optional, needs additional setup)
coverage:
    pytest tests/ --cov=. --cov-report html

# Linting (optional, needs additional configuration)
lint:
    flake8 .

# Scorecards and metrics (more advanced, custom implementation needed)
scorecards:
    # Implement your custom script or tool here, leveraging test results and other data