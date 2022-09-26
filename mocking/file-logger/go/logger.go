package main

import (
	"fmt"
	"time"
)

const (
	DefaultWeekendFileName = "weekend.txt"
)

type FileLogger struct {
	storage FileStorage
	clock   clock
}

func formatWeekdayFile(currentTime *time.Time) string {
	return "log" + currentTime.Format("20060102") + ".txt"
}

func formatPreviousWeekendFile(modTime *time.Time) string {
	return "weekend-" + modTime.Format("20060102") + ".txt"
}

func wasFileModifiedThisWeekend(currentTime, modTime *time.Time) bool {
	var currentWeekBeginning time.Time

	if currentTime.Weekday() == time.Saturday {
		year, month, day := currentTime.Date()
		currentWeekBeginning = time.Date(year, month, day, 0, 0, 0, 0, time.UTC)
	} else {
		year, month, day := currentTime.Date()
		currentWeekBeginning = time.Date(year, month, day-1, 0, 0, 0, 0, time.UTC)
	}

	// check if file was created during this weekend
	if modTime.After(currentWeekBeginning) {
		return true
	}

	return false
}

func (l *FileLogger) getFileName() (error, string) {
	currentTime := l.clock.Now()

	if !IsWeekend(currentTime) {
		return nil, formatWeekdayFile(&currentTime)
	}

	if !l.storage.FileExists(DefaultWeekendFileName) {
		return nil, DefaultWeekendFileName
	}

	modTime, err := l.storage.FileModificationTime(DefaultWeekendFileName)

	if err != nil {
		fmt.Printf("Couldn't get the modification time from %v", DefaultWeekendFileName)
		return err, ""
	}

	if wasFileModifiedThisWeekend(&currentTime, modTime) {
		return nil, DefaultWeekendFileName
	}

	var previousSaturday *time.Time

	if modTime.Weekday() == time.Saturday {
		previousSaturday = modTime
	} else {
		saturday := modTime.AddDate(0, 0, -1)

		previousSaturday = &saturday
	}

	newFileName := formatPreviousWeekendFile(previousSaturday)

	// rename the old file created in past weekend
	err = l.storage.RenameFile(DefaultWeekendFileName, newFileName)
	if err != nil {
		fmt.Printf("Couldn't rename old %v", DefaultWeekendFileName)
		return err, ""
	}

	return nil, DefaultWeekendFileName
}

func (l *FileLogger) Log(message string) {
	err, fileName := l.getFileName()

	if err != nil {
		panic("Couldn't open or create a file" + fileName)
	}

	err = l.storage.AppendStringToFile(fileName, message)

	if err != nil {
		panic("Couldn't write to a file " + fileName)
	}
}
