import time
from subprocess import check_call
from urllib.request import urlopen

CONTAINER_NAME = "flaskcontainer"
CONTAINER_PORT = 5000
HEALTH_ENDPOINT = f"http://127.0.0.1:{CONTAINER_PORT}/health"
IMAGE_NAME = "app"

check_call(f"docker run --rm --name={CONTAINER_NAME} -p {CONTAINER_PORT}:{CONTAINER_PORT} -d {IMAGE_NAME}".split())

# wait until server is ready
time.sleep(5)

# check if server has started and it's working
try:
    urlopen(HEALTH_ENDPOINT).read()
finally:
    check_call(f"docker kill {CONTAINER_NAME}".split())
