filename = main
cc = clang

all:
	llc $(filename).ll
	$(cc) $(filename).s -o $(filename).out
	./$(filename).out
