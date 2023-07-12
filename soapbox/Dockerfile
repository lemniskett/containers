FROM tootsuite/mastodon:latest
USER root
ADD https://gitlab.com/soapbox-pub/soapbox/-/jobs/artifacts/develop/download?job=build-production /tmp/soapbox.zip
RUN apt install nginx -y
RUN set -ex; \
    wget 'https://gitlab.com/soapbox-pub/soapbox/-/jobs/artifacts/develop/download?job=build-production' -O /tmp/soapbox.zip; \
    apt install unzip -y; \
    unzip -o -d /opt/soapbox /tmp/soapbox.zip; \
    rm /tmp/soapbox.zip; \
    chown -R mastodon:mastodon /opt/soapbox
COPY ./mastodon-nginx.conf /etc/nginx/sites-enabled/default
USER mastodon
ENTRYPOINT ["/bin/sh"]
CMD ["-c", "bundle exec rails db:migrate; nginx -g 'daemon off;' & bundle exec rails s -p 3000"]
