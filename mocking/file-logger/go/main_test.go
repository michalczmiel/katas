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

func TestLog(t *testing.T) {
	// given
	storage := &InMemoryFileStorage{}
	clock := fakeClock{}
	logger := FileLogger{storage, clock}

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
