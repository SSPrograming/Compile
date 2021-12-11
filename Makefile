all:
	cd ./antlr && make
	cd ./llvm && make
	cd ./output && make
	