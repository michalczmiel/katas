package main

import (
	"testing"
)

func TestLog(t *testing.T) {
	storage := LocalFileStorage{}
	logger := FileLogger{"log.txt", storage}
	logger.Log("Hello world!")
}
