package main

import (
	"reflect"
	"testing"
	"time"
)

type InMemoryFileStorage struct {
	Logs             map[string][]string
	ModificationTime map[string]time.Time
}

func (s *InMemoryFileStorage) AppendStringToFile(path, message string) error {
	logs, exist := s.Logs[path]

	if !exist {
		s.Logs[path] = []string{}
	}

	s.Logs[path] = append(logs, message)

	return nil
}

func (s *InMemoryFileStorage) FileExists(path string) bool {
	_, exist := s.Logs[path]

	return exist
}

func (s *InMemoryFileStorage) RenameFile(oldPath, newPath string) error {
	logs, exist := s.Logs[oldPath]

	if !exist {
		return nil
	}

	s.Logs[newPath] = logs

	delete(s.Logs, oldPath)
	delete(s.ModificationTime, oldPath)

	return nil
}

func (s *InMemoryFileStorage) FileModificationTime(path string) (*time.Time, error) {
	modTime, exist := s.ModificationTime[path]

	if !exist {
		modTime = time.Date(2022, 9, 24, 8, 0, 0, 0, time.UTC)
	}

	return &modTime, nil
}

func NewEmptyInMemoryFileStorage() *InMemoryFileStorage {
	return &InMemoryFileStorage{Logs: make(map[string][]string)}
}

type fakeClock struct {
	time time.Time
}

func (c fakeClock) Now() time.Time {
	return c.time
}

func TestLogWritesToNewFileWithCurrentDateOnWeekday(t *testing.T) {
	// given
	storage := NewEmptyInMemoryFileStorage()
	clock := fakeClock{time.Date(2022, 9, 22, 10, 0, 0, 0, time.UTC)}
	logger := FileLogger{storage, clock}

	// when
	logger.Log("First log")
	logger.Log("Second log")

	expected := map[string][]string{
		"log20220922.txt": {"First log", "Second log"},
	}

	if !reflect.DeepEqual(storage.Logs, expected) {
		t.Log("Logs don't match")
		t.Logf("Expected: %v", expected)
		t.Logf("Received: %v", storage.Logs)
		t.Fail()
	}
}

func TestLogWritesToExistingFileWithCurrentDateOnWeekday(t *testing.T) {
	// given
	mockedLogs := map[string][]string{
		"log20220922.txt": {"First log"},
	}
	storage := &InMemoryFileStorage{Logs: mockedLogs}
	clock := fakeClock{time.Date(2022, 9, 22, 10, 0, 0, 0, time.UTC)}
	logger := FileLogger{storage, clock}

	// when
	logger.Log("Second log")

	expected := map[string][]string{
		"log20220922.txt": {"First log", "Second log"},
	}

	if !reflect.DeepEqual(storage.Logs, expected) {
		t.Log("Logs don't match")
		t.Logf("Expected: %v", expected)
		t.Logf("Received: %v", storage.Logs)
		t.Fail()
	}
}

func TestLogWritesToNewFileWithCurrentDateOnSaturday(t *testing.T) {
	// given
	storage := NewEmptyInMemoryFileStorage()
	clock := fakeClock{time.Date(2022, 9, 24, 10, 0, 0, 0, time.UTC)}
	logger := FileLogger{storage, clock}

	// when
	logger.Log("First log")
	logger.Log("Second log")

	expected := map[string][]string{
		"weekend.txt": {"First log", "Second log"},
	}

	if !reflect.DeepEqual(storage.Logs, expected) {
		t.Log("Logs don't match")
		t.Logf("Expected: %v", expected)
		t.Logf("Received: %v", storage.Logs)
		t.Fail()
	}
}

func TestLogWritesToExistingFileWithCurrentDateOnSaturday(t *testing.T) {
	// given
	storage := NewEmptyInMemoryFileStorage()
	clock := fakeClock{time.Date(2022, 9, 24, 10, 0, 0, 0, time.UTC)}
	logger := FileLogger{storage, clock}

	// when
	logger.Log("First log")
	logger.Log("Second log")

	expected := map[string][]string{
		"weekend.txt": {"First log", "Second log"},
	}

	if !reflect.DeepEqual(storage.Logs, expected) {
		t.Log("Logs don't match")
		t.Logf("Expected: %v", expected)
		t.Logf("Received: %v", storage.Logs)
		t.Fail()
	}
}

func TestLogWritesToNewFileWithCurrentDateOnSunday(t *testing.T) {
	// given
	mockedLogs := map[string][]string{
		"weekend.txt": {"First log"},
	}
	storage := &InMemoryFileStorage{Logs: mockedLogs}
	clock := fakeClock{time.Date(2022, 9, 25, 10, 0, 0, 0, time.UTC)}
	logger := FileLogger{storage, clock}

	// when
	logger.Log("Second log")

	expected := map[string][]string{
		"weekend.txt": {"First log", "Second log"},
	}

	if !reflect.DeepEqual(storage.Logs, expected) {
		t.Log("Logs don't match")
		t.Logf("Expected: %v", expected)
		t.Logf("Received: %v", storage.Logs)
		t.Fail()
	}
}

func TestLogRenamesThePreviousWeekendFile(t *testing.T) {
	// given
	mockedLogs := map[string][]string{
		"weekend.txt": {},
	}

	mockedModificationTime := map[string]time.Time{
		"weekend.txt": time.Date(2022, 9, 18, 10, 0, 0, 0, time.UTC),
	}

	storage := &InMemoryFileStorage{Logs: mockedLogs, ModificationTime: mockedModificationTime}

	clock := fakeClock{time.Date(2022, 9, 25, 10, 0, 0, 0, time.UTC)}
	logger := FileLogger{storage, clock}

	// when
	logger.Log("First log")
	logger.Log("Second log")

	expected := map[string][]string{
		"weekend.txt":          {"First log", "Second log"},
		"weekend-20220917.txt": {},
	}

	if !reflect.DeepEqual(storage.Logs, expected) {
		t.Log("Logs don't match")
		t.Logf("Expected: %v", expected)
		t.Logf("Received: %v", storage.Logs)
		t.Fail()
	}
}
