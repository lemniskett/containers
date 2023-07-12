#!/bin/sh

bundle exec rails db:migrate; 

mkdir -p /tmp/nginx/cache
nginx -g 'daemon off;' &

bundle exec rails s -p 3000