BINARY_NAME=logger.out

build:
	go build -o ${BINARY_NAME} *.go

run: clean build
	./${BINARY_NAME}

.PHONY: clean
clean:
	go clean
	rm -rf ${BINARY_NAME}

.PHONY: test
test:
	go test
