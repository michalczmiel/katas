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

func (s *InMemoryFileStorage) AppendStringToFile(fileName, message string) error {
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

type fakeClock struct {
	time time.Time
}

func (fakeClock fakeClock) Now() time.Time {
	return fakeClock.time
}

func TestLogWritesToFileWithCurrentDateOnWeekday(t *testing.T) {
	// given
	storage := &InMemoryFileStorage{}
	clock := fakeClock{time.Date(2022, 9, 22, 10, 0, 0, 0, time.UTC)}
	logger := FileLogger{storage, clock}

	// when
	logger.Log("First log")
	logger.Log("Second log")

	expectedFileName := "log20220922.txt"

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

func TestLogWritesToFileWithCurrentDateOnSaturday(t *testing.T) {
	// given
	storage := &InMemoryFileStorage{}
	clock := fakeClock{time.Date(2022, 9, 24, 10, 0, 0, 0, time.UTC)}
	logger := FileLogger{storage, clock}

	// when
	logger.Log("First log")
	logger.Log("Second log")

	expectedFileName := "weekend.txt"

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

func TestLogWritesToFileWithCurrentDateOnSunday(t *testing.T) {
	// given
	storage := &InMemoryFileStorage{}
	clock := fakeClock{time.Date(2022, 9, 25, 10, 0, 0, 0, time.UTC)}
	logger := FileLogger{storage, clock}

	// when
	logger.Log("First log")
	logger.Log("Second log")

	expectedFileName := "weekend.txt"

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
