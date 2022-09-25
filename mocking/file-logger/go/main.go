package main

// example usage of FileLogger
func main() {
	storage := &localFileStorage{}
	clock := realClock{}
	logger := FileLogger{storage, clock}
	logger.Log("Hello world!")
}
