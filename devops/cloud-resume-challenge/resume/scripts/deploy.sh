#!/bin/bash

set -euo pipefail

aws s3 sync ./website s3://$WEBSITE_BUCKET
