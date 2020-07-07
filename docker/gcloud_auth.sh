#!/bin/bash

# Source: https://cloud.google.com/container-registry/docs/advanced-authentication#gcloud-helper

# Step 1: Log into gcloud
gcloud auth login

# Step 2: Configure authentication with service account credentials

#Service ID:
service_id='focus-chain-120819@appspot.gserviceaccount.com'

#Key File:
key_file='focus-chain-120819-b9c907122d1a.json'

gcloud auth activate-service-account ${service_id} --key-file=${key_file}

# Step 3: configure Docker
gcloud auth configure-docker
#sudo gcloud auth configure-docker (if docker is running with sudo)

# Step 4: generate one-time access token
gcloud auth print-access-token | sudo docker login -u oauth2accesstoken --password-stdin https://gcr.io


