#!/bin/bash

echo "This is a silly script" > /tmp/silly.txt

#update/install apache2
sudo yum -y update 
sudo yum -y install httpd
sudo systemctl enable httpd
sudo systemctl start httpd
