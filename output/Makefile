filename = main

all:
	llc $(filename).ll
	gcc $(filename).s -o $(filename).out
	./$(filename).out
