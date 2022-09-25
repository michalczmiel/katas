package main

import "time"

type clock interface {
	Now() time.Time
}

type realClock struct{}

func (realClock) Now() time.Time {
	return time.Now()
}

func IsWeekend(t time.Time) bool {
	day := t.Weekday()

	if day == time.Saturday || day == time.Sunday {
		return true
	}

	return false
}
