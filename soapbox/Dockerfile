FROM tootsuite/mastodon:latest
USER root
RUN apt install nginx curl -y
RUN set -ex; \
    curl -L 'https://gitlab.com/soapbox-pub/soapbox/-/jobs/artifacts/develop/download?job=build-production' -o /tmp/soapbox.zip; \
    apt install unzip -y; \
    unzip -o -d /opt/soapbox /tmp/soapbox.zip; \
    rm /tmp/soapbox.zip; \
    chown -R mastodon:mastodon /opt/soapbox /var/log/nginx /var/lib/nginx
COPY ./mastodon-nginx.conf /etc/nginx/sites-enabled/default
COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./entrypoint.sh /entrypoint.sh
USER mastodon
ENTRYPOINT ["/entrypoint.sh"]
