#!/bin/sh
rm -rf .terraform
terraform init -upgrade
terraform providers lock -platform=darwin_arm64 -platform=linux_amd64 -platform=darwin_amd64
