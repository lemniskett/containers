#!/bin/sh

bundle exec rails db:migrate; 

mkdir -p /tmp/nginx/cache
mkdir -p /tmp/nginx/proxy
nginx -g 'daemon off;' &

bundle exec rails s -p 3000
