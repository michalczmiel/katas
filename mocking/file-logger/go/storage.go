package main

import (
	"errors"
	"fmt"
	"os"
	"time"
)

type FileStorage interface {
	AppendStringToFile(path, message string) error
	FileExists(path string) bool
	RenameFile(oldPath, newPath string) error
	FileModificationTime(path string) (*time.Time, error)
}

type localFileStorage struct{}

func (localFileStorage) AppendStringToFile(path, message string) error {
	file, err := os.OpenFile(path, os.O_APPEND|os.O_WRONLY, os.ModeAppend)

	// file not found, creating a new one
	if os.IsNotExist(err) {
		file, err = os.Create(path)
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

func (localFileStorage) FileExists(path string) bool {
	_, err := os.Stat(path)

	if errors.Is(err, os.ErrNotExist) {
		return false
	}

	return true
}

func (localFileStorage) RenameFile(oldPath, newPath string) error {
	err := os.Rename(oldPath, newPath)

	return err
}

func (localFileStorage) FileModificationTime(path string) (*time.Time, error) {
	info, err := os.Stat(path)

	if err != nil {
		return nil, err
	}

	t := info.ModTime()

	return &t, nil
}
