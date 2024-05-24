#!/bin/bash
crontab -l > mycron

echo "0 0 * * * /usr/bin/python3 /home/rajesh/face-module/face-model-hub > /app/cron.log 2>&1" >> mycron

crontab mycron
rm mycron

cron -f
