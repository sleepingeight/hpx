#!/bin/bash
LOG_FILE=$1
if [ -z "$LOG_FILE" ]; then
    echo "Usage: $0 <log_file>"
    exit 1
fi

echo "timestamp,mem_used_mb,mem_avail_mb" > "$LOG_FILE"
while true; do
  # Get used and available memory in MB from 'free -m'
  # $3 is used, $7 is available
  STATS=$(free -m | awk '/^Mem:/{print $3 "," $7}')
  TIMESTAMP=$(date +%s)
  echo "$TIMESTAMP,$STATS" >> "$LOG_FILE"
  sleep 5
done
