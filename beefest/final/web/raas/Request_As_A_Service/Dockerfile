# Use an official PHP image as the base image
FROM php:7.4-apache

# Install cURL extension for PHP
RUN apt-get update && apt-get install -y libcurl4-openssl-dev && \
    docker-php-ext-install curl

# Copy PHP script to container
COPY src/index.php /var/www/html/
COPY src/admin.php /var/www/html/

# Copy flag to container
COPY src/flag.txt /fl4444444444444444444444444444444ggg.txt
RUN chown root:root /fl4444444444444444444444444444444ggg.txt

# Expose port 8085
EXPOSE 8085

# Configure Apache to listen on port 8085
RUN sed -i 's/80/8085/g' /etc/apache2/sites-available/000-default.conf /etc/apache2/ports.conf

# Start Apache web server
CMD ["apache2-foreground"]