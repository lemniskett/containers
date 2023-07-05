FROM python:3.11-alpine
RUN apk add --no-cache postgresql-client
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY pg-database-s3-backup.py /usr/local/bin/pg-database-s3-backup
RUN chmod +x /usr/local/bin/pg-database-s3-backup
ENTRYPOINT [ "pg-database-s3-backup" ]