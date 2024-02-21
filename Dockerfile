# Use an Apache web server image
FROM httpd:latest

# Copy source code to (container) Apache's document root
COPY ./src/ /usr/local/apache2/htdocs/

# Overwrite (container) Apache's httpd.conf with the one in project directory.
COPY ./apache-config/httpd.conf /usr/local/apache2/conf/httpd.conf

# Expose port 80
EXPOSE 80