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
	delete(s.ModificationTime, oldPath)

	return nil
}

func (s *InMemoryFileStorage) FileModificationTime(fileName string) (*time.Time, error) {
	modTime, exist := s.ModificationTime[fileName]

	if !exist {
		modTime = time.Date(2022, 9, 24, 8, 0, 0, 0, time.UTC)
	}

	return &modTime, nil
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

func TestLogRenamesThePreviousWeekendFile(t *testing.T) {
	// given
	mockedLogs := map[string][]string{
		"weekend.txt": {},
	}

	mockedModificationTime := map[string]time.Time{
		"weekend.txt": time.Date(2022, 9, 17, 10, 0, 0, 0, time.UTC),
	}

	storage := &InMemoryFileStorage{Logs: mockedLogs, ModificationTime: mockedModificationTime}

	clock := fakeClock{time.Date(2022, 9, 25, 10, 0, 0, 0, time.UTC)}
	logger := FileLogger{storage, clock}

	// when
	logger.Log("First log")
	logger.Log("Second log")

	expected := map[string][]string{
		"weekend.txt":         {"First log", "Second log"},
		"weekend20220917.txt": {},
	}

	if !reflect.DeepEqual(storage.Logs, expected) {
		t.Log("Logs don't match")
		t.Logf("Expected: %v", expected)
		t.Logf("Received: %v", storage.Logs)
		t.Fail()
	}

}
