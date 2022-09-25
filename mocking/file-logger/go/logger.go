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

func (FileLogger) formatWeekdayFile(currentTime *time.Time) string {
	return "log" + currentTime.Format("20060102") + ".txt"
}

func (FileLogger) formatPreviousWeekendFile(modTime *time.Time) string {
	return "weekend-" + modTime.Format("20060102") + ".txt"
}

func (l *FileLogger) getFileName() string {
	currentTime := l.clock.Now()

	if !IsWeekend(currentTime) {
		return l.formatWeekdayFile(&currentTime)
	}

	if !l.storage.FileExists(DefaultWeekendFileName) {
		return DefaultWeekendFileName
	}

	modTime, err := l.storage.FileModificationTime(DefaultWeekendFileName)

	if err != nil {
		panic("Couldn't get the modification time from " + DefaultWeekendFileName)
	}

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
		return DefaultWeekendFileName
	}

	var previousSaturday *time.Time

	if modTime.Weekday() == time.Saturday {
		previousSaturday = modTime
	} else {
		saturday := modTime.AddDate(0, 0, -1)

		previousSaturday = &saturday
	}

	newFileName := l.formatPreviousWeekendFile(previousSaturday)

	// rename the old file created in past weekend
	err = l.storage.RenameFile(DefaultWeekendFileName, newFileName)
	if err != nil {
		panic("Couldn't rename old " + DefaultWeekendFileName)
	}

	return DefaultWeekendFileName
}

func (l *FileLogger) Log(message string) {
	fileName := l.getFileName()

	err := l.storage.AppendStringToFile(fileName, message)

	if err != nil {
		fmt.Println(err)
	}
}
