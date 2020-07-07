#!/bin/bash
ADDRESS=gcr.io
PROJECT_ID=focus-chain-120819
REPOSITORY=auto
VERSION=v5


#ID="$(sudo docker images | grep ${REPOSITORY} | head -n 1 | awk '{print $3}')"
#echo $ID
sudo docker build -t quickstart-image -f Dockerfile ../app
sudo docker tag quickstart-image gcr.io/${PROJECT_ID}/quickstart-image:${VERSION}
#sudo docker tag ${ID} $ADDRESS/${PROJECT_ID}/${REPOSITORY}:${VERSION}
sudo docker push gcr.io/${PROJECT_ID}/quickstart-image:${VERSION}
#sudo docker push $ADDRESS/${PROJECT_ID}/${REPOSITORY}:${VERSION}


