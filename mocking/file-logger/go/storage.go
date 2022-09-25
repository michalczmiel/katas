package main

import (
	"fmt"
	"os"
)

type FileStorage interface {
	AppendStringToFile(fileName, message string) error
}

type localFileStorage struct{}

func (s *localFileStorage) AppendStringToFile(fileName, message string) error {
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
