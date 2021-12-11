all:
	cd ./antlr && make
	cd ./llvm && make
	cd ./output && make

test:
	cd ./antlr && make
	cd ./llvm && make
	cd ./output && make test
