#!/bin/bash

set -euo pipefail

gunicorn --bind 0.0.0.0:5000 app.main:app
