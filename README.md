# News Classifier As Service (2020)
# Author: Winnie Yeung

Deploy NLP model for news classification using Flask, Docker, Kubernetes

Goal:
- Deploy ML learning model for inferencing using Docker and Kubernetes

How to use:
- Train NLP model using scikit-learn baseline 
- Package environement and dependencies in Docker
- Deploy using Kubernetes (Ingress, Serving)
- Use API to send text in, preprocess and output prediction

Kubernetes Terminology:
- Ingress: External load balancer
- Serving: Internal load balancer
- Pod : Container

Data:
- BBC News Article - 5 News Category classfication
- kaggle datasets download -d yufengdev/bbc-fulltext-and-category

Resources:
- https://mlfromscratch.com/deployment-introduction/#/
