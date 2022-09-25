package main

import (
	"reflect"
	"testing"
	"time"
)

type InMemoryFileStorage struct {
	Logs map[string][]string
}

func (s *InMemoryFileStorage) AppendStringToFile(fileName, message string) error {
	if s.Logs == nil {
		s.Logs = make(map[string][]string)
	}

	logs, exist := s.Logs[fileName]

	if !exist {
		s.Logs[fileName] = []string{}
	}

	s.Logs[fileName] = append(logs, message)

	return nil
}

func (s *InMemoryFileStorage) FileExists(fileName string) bool {
	if s.Logs == nil {
		return false
	}

	_, exist := s.Logs[fileName]

	return exist
}

func (s *InMemoryFileStorage) RenameFile(oldPath, newPath string) error {
	if s.Logs == nil {
		return nil
	}

	logs, exist := s.Logs[oldPath]

	if !exist {
		return nil
	}

	s.Logs[newPath] = logs
	delete(s.Logs, oldPath)

	return nil
}

func (s *InMemoryFileStorage) FileModificationTime(fileName string) (*time.Time, error) {
	// TODO: make it dynamic
	t := time.Date(2022, 9, 22, 10, 0, 0, 0, time.UTC)

	return &t, nil
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

	logs, exist := storage.Logs[expectedFileName]

	if !exist {
		t.Log("File " + expectedFileName + " not created")
		t.Fail()
	}

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

	logs, exist := storage.Logs[expectedFileName]

	if !exist {
		t.Log("File " + expectedFileName + " not created")
		t.Fail()
	}

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

	logs, exist := storage.Logs[expectedFileName]

	if !exist {
		t.Log("File " + expectedFileName + " not created")
		t.Fail()
	}

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
