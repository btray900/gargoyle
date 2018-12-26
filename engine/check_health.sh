#!/bin/sh
# wait for es before trying to create objects
# bt106c

while ! curl -s -XGET http://kibana:5601/api/status; do
  echo "Kibana at  http://kibana:5601/api/status not ready, waiting 300s ZZZZZZzzzzzzz" >&2
  sleep 300
done | 
  until grep -q green; do
    echo "oops....something went wrong. Check proxy or dns issues with this container to reach kibana or stop and re-up since python might go to fast.........."
  done

#/usr/bin/python /tmp/setup_dashboard.py
