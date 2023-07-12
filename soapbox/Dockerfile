FROM tootsuite/mastodon:latest
USER root
RUN apt install nginx curl -y
RUN set -ex; \
    curl -L 'https://gitlab.com/soapbox-pub/soapbox/-/jobs/artifacts/develop/download?job=build-production' -o /tmp/soapbox.zip; \
    apt install unzip -y; \
    unzip -o -d /opt/soapbox /tmp/soapbox.zip; \
    rm /tmp/soapbox.zip; \
    chown -R mastodon:mastodon /opt/soapbox
COPY ./mastodon-nginx.conf /etc/nginx/sites-enabled/default
COPY ./nginx.conf /etc/nginx/nginx.conf
USER mastodon
ENTRYPOINT ["/bin/sh", "/entrypoint.sh"]
