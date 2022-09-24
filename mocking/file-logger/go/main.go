package main

import (
	"fmt"
	"os"
)

type FileStorage interface {
	AppendStringToFile(fileName string, message string) (err error)
}

type LocalFileStorage struct{}

func (s LocalFileStorage) AppendStringToFile(fileName string, message string) (err error) {
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
	fileName string
	storage  FileStorage
}

func (l *FileLogger) Log(message string) {
	err := l.storage.AppendStringToFile(l.fileName, message)

	if err != nil {
		fmt.Println(err)
	}
}

func main() {
	storage := LocalFileStorage{}
	logger := FileLogger{"log.txt", storage}
	logger.Log("Hello world!")
}
