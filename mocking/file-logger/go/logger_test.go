package main

import (
	"reflect"
	"testing"
	"time"
)

type InMemoryFileStorage struct {
	Logs []string
	Log  map[string][]string
}

func (s *InMemoryFileStorage) AppendStringToFile(fileName string, message string) (err error) {
	s.Logs = append(s.Logs, message)

	if s.Log == nil {
		s.Log = make(map[string][]string)
	}

	if s.Log[fileName] == nil {
		s.Log[fileName] = []string{}
	}

	s.Log[fileName] = append(s.Log[fileName], message)

	return nil
}

type fakeClock struct{}

func (fakeClock) Now() time.Time {
	return time.Date(2022, 9, 24, 10, 0, 0, 0, time.UTC)
}

func TestLogWritesToFileWithCurrentDate(t *testing.T) {
	// given
	storage := &InMemoryFileStorage{}
	clock := fakeClock{}
	logger := FileLogger{storage, clock}

	// when
	logger.Log("First log")
	logger.Log("Second log")

	expectedFileName := "log20220924.txt"

	if storage.Log[expectedFileName] == nil {
		t.Log("File " + expectedFileName + " not created")
		t.Fail()
	}

	logs := storage.Log[expectedFileName]

	// then
	if len(logs) != 2 {
		t.Log("Two logs should have been logged but got", len(storage.Logs))
		t.Fail()
	}

	expected := []string{"First log", "Second log"}

	if !reflect.DeepEqual(logs, expected) {
		t.Log("Logs don't match")
		t.Fail()
	}

}
