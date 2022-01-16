#!/bin/bash

set -euo pipefail

STACK_NAME="cloud-resume-challenge-static-website"

aws cloudformation describe-stacks --stack-name $STACK_NAME
