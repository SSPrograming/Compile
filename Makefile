all:
	cd ./antlr && make
	cd ./llvm && make
	cd ./output && make

test:
	make filename=main
	make filename=add
	make filename=arithmetic
	make filename=array
	make filename=basic_io
	make filename=break
	make filename=declare
	make filename=if_else
	make filename=sum
	make filename=sort
	make filename=evaluate

