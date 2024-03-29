#!/bin/bash

set -euo pipefail

TEMPLATE_FILE="template.yaml"
STACK_NAME="cloud-resume-challenge-static-website"

aws cloudformation deploy --template-file $TEMPLATE_FILE --stack-name $STACK_NAME
