package main

import (
	"fmt"
	"os"
	"time"
)

type FileStorage interface {
	AppendStringToFile(fileName string, message string) (err error)
}

type localFileStorage struct{}

func (s *localFileStorage) AppendStringToFile(fileName string, message string) (err error) {
	file, err := os.OpenFile(fileName, os.O_APPEND|os.O_WRONLY, os.ModeAppend)

	// file not found, creating a new one
	if os.IsNotExist(err) {
		file, err = os.Create(fileName)
	}

	if err != nil {
		return err
	}

	defer file.Close()

	// append text to the file
	_, err = fmt.Fprintln(file, message)

	if err != nil {
		fmt.Println(err)
		return err
	}

	return nil
}

type Clock interface {
	Now() time.Time
}

type realClock struct{}

func (realClock) Now() time.Time {
	return time.Now()
}

type FileLogger struct {
	storage FileStorage
	clock   Clock
}

func (l *FileLogger) getFileName() string {
	currentTime := l.clock.Now()

	fileName := "log" + currentTime.Format("20060102") + ".txt"

	return fileName
}

func (l *FileLogger) Log(message string) {
	fileName := l.getFileName()

	err := l.storage.AppendStringToFile(fileName, message)

	if err != nil {
		fmt.Println(err)
	}
}

func main() {
	storage := &localFileStorage{}
	clock := realClock{}
	logger := FileLogger{storage, clock}
	logger.Log("Hello world!")
}
