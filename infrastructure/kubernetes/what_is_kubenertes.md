## What is Kubernetes

Developed by Google and open-sourced.

The developers had more expertise in C++ and Java, but the community wasn’t that strong for C and GoLang was a langague with http support which was already used in Docker

Unexpected uses: US Army - Airplane, Raspberry PI, Satellite (Refence Tim Hockin Interview on YouTube)

Kubernetes comes from Ancient Greek and mean to steer (logo is a steering wheel)

Designed State Management: Feed the cluster services for a configuration, which will be run

Worker: Container Host. It has a Kublic (Public) services/ Kubernetes Services, which can communicate with the Kubernetes Cluster

App1.yaml = deployment file with a Pod configuration (smallest unit of deployment in Kubernetes Object Modal) in which you can have running containers from container images. This deployment file is fed into the API

What happens if a worker dies? The K8 Cluster Services is responsible for watching the workers and maintaining them

Features
High scalability
Availability without downtime
Disaster recovery - backup and restore

Kublet - Each node for talking with each other

Control container:
api - which is the endpoint for the Kubernetes cluster
Manager - Health checks and control
Scheduler - for loads ?
Etcd- backing storage - stores state
Virtual node

Node has many pods
Pod = abstraction over a container (for using diverse container technologies), which it’s on up address. It’s Edelmetall, can die easily - new ones get a new up adress, but the service remains the same

ConfigMap = external configuration, like environment variables. Password should be used using Secrets
Secret - base64 encoded format for passwords (is not encryption! is just for enabling use as binaries, certificates and special characters in the yaml file - echo -n "name" | base64)

Blueprint - for docker compose for STATELESS APPS (not databases)
Statefulset - state full apps like databases

Kubernetes is declarative, checks if is is equal SHOULD
