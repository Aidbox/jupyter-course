#!/bin/bash

ssh-keygen -t rsa -b 4096 -f jwtRS256.key
openssl rsa -in jwtRS256.key -pubout -outform PEM -out jwtRS256.key.pub

