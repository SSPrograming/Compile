filename = main
cc = clang

all:
	llc $(filename).ll
	$(cc) $(filename).s -o $(filename).out
	./$(filename).out

test:
	make filename=main
	make filename=add
	make filename=arithmetic
	make filename=array
	make filename=break
	make filename=declare
	make filename=if_else
	make filename=sum
	make filename=basic_io
	make filename=sort
	make filename=evaluate
