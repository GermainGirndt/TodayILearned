#!/bin/bash

# check processes listening on port

# array of ports to check
ports=(53 80 443 5060 8080)

for port in "${ports[@]}"
do
    echo "Checking port: $port"

    echo "Using LSOF:"
    lsof -i :$port

    echo "Using NETSTAT:"
    netstat -tuln | grep :$port

    echo "----------------------------"
done
