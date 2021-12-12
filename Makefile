filename = main

input = ./input
output = ./output
antlr = ./antlr
llvm = ./llvm

grammar = naiveC.g4


llvmfiles = \
	$(llvm)/naiveC.interp \
	$(llvm)/naiveC.tokens \
	$(llvm)/naiveCLexer.interp \
	$(llvm)/naiveCLexer.py \
	$(llvm)/naiveCLexer.tokens \
	$(llvm)/naiveCListener.py \
	$(llvm)/naiveCParser.py \
	$(llvm)/naiveCVisitor.py \
	

run: $(output)/$(filename).ll
	cd $(output) && make run


$(output)/$(filename).ll: $(llvmfiles) $(input)/$(filename).c
	python $(llvm)/main.py $(input)/$(filename).c $(output)/$(filename).ll

$(llvmfiles): $(antlr)/src/$(grammar)
	cd ./antlr && make

clean: 
	cd $(llvm) && rm -f naiveC*
	cd $(output) && rm -rf *.ll && make clean

testnames = \
	main \
	add \
	array \
	arithmetic \
	break \
	declare \
	if_else \
	sum \
	fib \
	basic_io \
	sort \
	evaluate \

testfiles = $(foreach testfile,$(testnames),$(input)/$(testfile).c)

test: $(llvmfiles) $(testfiles)
	for testname in $(testnames); do \
		python $(llvm)/main.py $(input)/$$testname.c $(output)/$$testname.ll; \
	done
	cd $(output) && make test
