package main

import (
	"fmt"
)

const (
	DefaultWeekendFileName = "weekend.txt"
)

type FileLogger struct {
	storage FileStorage
	clock   Clock
}

func (l *FileLogger) getFileName() string {
	currentTime := l.clock.Now()

	if !IsWeekend(currentTime) {
		return "log" + currentTime.Format("20060102") + ".txt"
	}

	return DefaultWeekendFileName
}

func (l *FileLogger) Log(message string) {
	fileName := l.getFileName()

	err := l.storage.AppendStringToFile(fileName, message)

	if err != nil {
		fmt.Println(err)
	}
}
