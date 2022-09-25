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

type FileLogger struct {
	storage FileStorage
}

func (l *FileLogger) getFileName() string {
	currentTime := time.Now()

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
	logger := FileLogger{storage}
	logger.Log("Hello world!")
}
