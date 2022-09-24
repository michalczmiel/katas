package main

import (
	"fmt"
	"os"
)

type FileLogger struct {
	fileName string
}

func (l FileLogger) Log(message string) {
	file, err := os.Create(l.fileName)

	if err != nil {
		fmt.Println(err)
	}

	defer file.Close()
}

func main() {
	logger := FileLogger{"log.txt"}
	logger.Log("Hello world!")
}
