package main

import (
	"fmt"
	"os"
)

type FileLogger struct {
	fileName string
}

func (l FileLogger) Log(message string) {
	file, err := os.OpenFile(l.fileName, os.O_APPEND|os.O_WRONLY, os.ModeAppend)

	// file not found
	if err != nil {
		file, err = os.Create(l.fileName)
	}

	defer file.Close()

	// append text to the file
	_, err = fmt.Fprintln(file, message)

	if err != nil {
		fmt.Println(err)
	}
}

func main() {
	logger := FileLogger{"log.txt"}
	logger.Log("Hello world!")
}
