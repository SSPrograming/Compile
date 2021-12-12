filename = main
CC = clang
CFLAGS = -O2

run: $(filename).out
	./$(filename).out

$(filename).out: $(filename).s
	$(CC) $(filename).s -o $(filename).out
	$(info generate：./input/$(filename).sort -> ./output/$(filename).out )

$(filename).s: $(filename).ll
	llc $(filename).ll
	$(info generate：./input/$(filename).ll -> ./output/$(filename).s )

clean:
	rm -f *.s *.out

testnames = \
	main \
	add \
	array \
	arithmetic \
	break \
	declare \
	if_else \
	sum \
	basic_io \
	sort \
	evaluate \

testfiles =  $(foreach testfile,$(testnames),$(testfile).ll)

test: $(testfiles)
	for testname in $(testnames); do \
		llc $$testname.ll -o $$testname.s; \
		echo 'generate successfully：./input/'$$testname'.ll -> ./output/'$$testname'.s'; \
	done
	for testname in $(testnames); do \
		gcc $$testname.s -o $$testname.out $(CFLAGS); \
		echo 'generate successfully：./input/'$$testname'.s -> ./output/'$$testname'.out'; \
	done
	for testname in $(testnames); do \
		echo '-------------------------------'; \
		echo '* run：'$$testname; \
		./$$testname.out; \
		echo '* finish：'$$testname; \
	done
