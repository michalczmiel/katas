package main

import (
	"reflect"
	"testing"
)

type InMemoryFileStorage struct {
	Logs []string
}

func (s *InMemoryFileStorage) AppendStringToFile(fileName string, message string) (err error) {
	s.Logs = append(s.Logs, message)

	return nil
}

func TestLog(t *testing.T) {
	// given
	storage := &InMemoryFileStorage{}
	logger := FileLogger{storage}

	// when
	logger.Log("First log")
	logger.Log("Second log")

	// then
	if len(storage.Logs) != 2 {
		t.Log("Two logs should have been logged but got", len(storage.Logs))
		t.Fail()
	}

	expected := []string{"First log", "Second log"}

	if !reflect.DeepEqual(storage.Logs, expected) {
		t.Log("Logs don't match")
		t.Fail()
	}

}
