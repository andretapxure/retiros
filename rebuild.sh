#!/bin/bash
docker build -t andretapxure/retiros:latest .
docker push andretapxure/retiros:latest
docker-compose down
docker-compose up