#!/bin/bash
set -e

GIT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
REPOSITORY=asia.gcr.io
PROJECT_NAME=genfive
VERSION=$(git rev-parse --short HEAD)
APPLICATION=$(basename "$(git config --get remote.origin.url)" .git)

if [[ $GIT_BRANCH == "develop" ]]; then
    PROJECT_NAME=$PROJECT_NAME-dev
elif [[ $GIT_BRANCH == "uat" ]]; then
    PROJECT_NAME=$PROJECT_NAME-uat
elif [[ $GIT_BRANCH == "main" ]]; then
    PROJECT_NAME=$PROJECT_NAME-prod
else
    exit 0
fi

docker build -t ${REPOSITORY}/${PROJECT_NAME}/${APPLICATION}:latest .