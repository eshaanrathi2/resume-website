# Use an Apache web server image
FROM httpd:latest

# Copy source code to Apache's document root
COPY ./src/ /usr/local/apache2/htdocs/

# Expose port 80
EXPOSE 80