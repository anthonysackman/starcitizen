#!/bin/bash
echo "start.sh initialized"

 sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

cd /root/prod/app

sudo docker-compose up --build -d 
