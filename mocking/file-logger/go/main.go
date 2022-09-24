package main

import "fmt"

type FileLogger struct {
	fileName string
}

func (l FileLogger) Log(message string) {
	fmt.Println(message)
}

func main() {
	logger := FileLogger{"log.txt"}
	logger.Log("Hello world!")
}
