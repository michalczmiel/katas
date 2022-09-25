package main

import (
	"fmt"
)

type FileLogger struct {
	storage FileStorage
	clock   Clock
}

func (l *FileLogger) getFileName() string {
	currentTime := l.clock.Now()

	var fileName string

	if IsWeekend(currentTime) {
		fileName = "weekend.txt"
	} else {
		fileName = "log" + currentTime.Format("20060102") + ".txt"
	}

	return fileName
}

func (l *FileLogger) Log(message string) {
	fileName := l.getFileName()

	err := l.storage.AppendStringToFile(fileName, message)

	if err != nil {
		fmt.Println(err)
	}
}
