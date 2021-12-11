filename = main
cc = gcc

all:
	llc $(filename).ll
	$(cc) $(filename).s -o $(filename).out
	./$(filename).out
