package main

import (
	"errors"
	"fmt"
	"os"
	"time"
)

type FileStorage interface {
	AppendStringToFile(fileName, message string) error
	FileExists(fileName string) bool
	RenameFile(oldPath, newPath string) error
	FileModificationTime(fileName string) (*time.Time, error)
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

func (s *localFileStorage) FileExists(fileName string) bool {
	_, err := os.Stat(fileName)

	if errors.Is(err, os.ErrNotExist) {
		return false
	}

	return true
}

func (s *localFileStorage) RenameFile(oldPath, newPath string) error {
	err := os.Rename(oldPath, newPath)

	return err
}

func (s *localFileStorage) FileModificationTime(fileName string) (*time.Time, error) {
	info, err := os.Stat(fileName)

	if err != nil {
		return nil, err
	}

	t := info.ModTime()

	return &t, nil
}
