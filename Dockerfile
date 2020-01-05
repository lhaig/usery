# Dockerfile
FROM python:3.6-slim
MAINTAINER Lance Haig
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usery/logs
WORKDIR /usery
COPY requirements.txt /usery/
# Get pip to download and install requirements:
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application folder inside the container
COPY . /usery/

# COPY startup script into known file location in container
COPY docker-entrypoint.sh /docker-entrypoint.sh

# Enable creating a logs volume mapping
VOLUME ["$WORKDIR/logs/"]

# EXPOSE port 8000 to allow communication to/from server
# EXPOSE 8000

# CMD specifcies the command to execute to start the server running.
CMD ["/docker-entrypoint.sh"]
# done!