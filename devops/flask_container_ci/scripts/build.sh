#!/bin/bash

set -euo pipefail

IMAGE_NAME=app

docker build -t "$IMAGE_NAME:latest" .
