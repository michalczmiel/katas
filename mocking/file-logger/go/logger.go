package main

import (
	"fmt"
	"time"
)

type FileLogger struct {
	storage FileStorage
	clock   Clock
}

func (l *FileLogger) getFileName() string {
	currentTime := l.clock.Now()

	day := currentTime.Weekday()

	var fileName string

	if day == time.Saturday || day == time.Sunday {
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
