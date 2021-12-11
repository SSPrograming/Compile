; ModuleID = ""
target triple = "x86_64-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...) 

declare i32 @"scanf"(i8* %".1", ...) 

declare i8* @"malloc"(i32 %".1") 

declare void @"free"(i8* %".1") 

declare void @"exit"(i32 %".1") 

declare i32 @"isdigit"(i32 %".1") 

declare i32 @"isspace"(i32 %".1") 

declare i32 @"getchar"() 

declare i64 @"strlen"(i8* %".1") 

define void @"sort"(i32* %".1", i32 %".2") 
{
entry:
  %".4" = alloca i32*
  store i32* %".1", i32** %".4"
  %".6" = alloca i32
  store i32 %".2", i32* %".6"
  %".8" = load i32, i32* %".6"
  %".9" = icmp slt i32 %".8", 0
  br i1 %".9", label %"entry.if", label %"entry.else"
entry.if:
  ret void
entry.else:
  br label %"entry.endif"
entry.endif:
  %"i" = alloca i32
  %".13" = load i32, i32* %".6"
  %".14" = sub i32 %".13", 1
  store i32 %".14", i32* %"i"
  %"j" = alloca i32
  store i32 0, i32* %"j"
  %"change" = alloca i32
  store i32 0, i32* %"change"
  br label %"while_cond"
while_cond:
  %".19" = load i32, i32* %"i"
  %".20" = icmp sge i32 %".19", 0
  br i1 %".20", label %"while_begin", label %"while_end"
while_begin:
  store i32 0, i32* %"j"
  br label %"while_cond.1"
while_end:
  ret void
while_cond.1:
  %".24" = load i32, i32* %"j"
  %".25" = load i32, i32* %"i"
  %".26" = icmp slt i32 %".24", %".25"
  br i1 %".26", label %"while_begin.1", label %"while_end.1"
while_begin.1:
  %".28" = load i32, i32* %"j"
  %".29" = load i32*, i32** %".4"
  %".30" = getelementptr i32, i32* %".29", i32 %".28"
  %".31" = load i32, i32* %".30"
  %".32" = load i32, i32* %"j"
  %".33" = add i32 %".32", 1
  %".34" = load i32*, i32** %".4"
  %".35" = getelementptr i32, i32* %".34", i32 %".33"
  %".36" = load i32, i32* %".35"
  %".37" = icmp sgt i32 %".31", %".36"
  br i1 %".37", label %"while_begin.1.if", label %"while_begin.1.else"
while_end.1:
  %".92" = load i32, i32* %"change"
  %".93" = icmp eq i32 %".92", 0
  br i1 %".93", label %"while_end.1.if", label %"while_end.1.else"
while_begin.1.if:
  %".39" = load i32, i32* %"j"
  %".40" = load i32*, i32** %".4"
  %".41" = getelementptr i32, i32* %".40", i32 %".39"
  %".42" = load i32, i32* %"j"
  %".43" = add i32 %".42", 1
  %".44" = load i32*, i32** %".4"
  %".45" = getelementptr i32, i32* %".44", i32 %".43"
  %".46" = load i32, i32* %".45"
  %".47" = load i32, i32* %"j"
  %".48" = load i32*, i32** %".4"
  %".49" = getelementptr i32, i32* %".48", i32 %".47"
  %".50" = load i32, i32* %".49"
  %".51" = add i32 %".46", %".50"
  store i32 %".51", i32* %".41"
  %".53" = load i32, i32* %"j"
  %".54" = add i32 %".53", 1
  %".55" = load i32*, i32** %".4"
  %".56" = getelementptr i32, i32* %".55", i32 %".54"
  %".57" = load i32, i32* %"j"
  %".58" = load i32*, i32** %".4"
  %".59" = getelementptr i32, i32* %".58", i32 %".57"
  %".60" = load i32, i32* %".59"
  %".61" = load i32, i32* %"j"
  %".62" = add i32 %".61", 1
  %".63" = load i32*, i32** %".4"
  %".64" = getelementptr i32, i32* %".63", i32 %".62"
  %".65" = load i32, i32* %".64"
  %".66" = sub i32 %".60", %".65"
  store i32 %".66", i32* %".56"
  %".68" = load i32, i32* %"j"
  %".69" = load i32*, i32** %".4"
  %".70" = getelementptr i32, i32* %".69", i32 %".68"
  %".71" = load i32, i32* %"j"
  %".72" = load i32*, i32** %".4"
  %".73" = getelementptr i32, i32* %".72", i32 %".71"
  %".74" = load i32, i32* %".73"
  %".75" = load i32, i32* %"j"
  %".76" = add i32 %".75", 1
  %".77" = load i32*, i32** %".4"
  %".78" = getelementptr i32, i32* %".77", i32 %".76"
  %".79" = load i32, i32* %".78"
  %".80" = sub i32 %".74", %".79"
  store i32 %".80", i32* %".70"
  store i32 1, i32* %"change"
  br label %"while_begin.1.endif"
while_begin.1.else:
  br label %"while_begin.1.endif"
while_begin.1.endif:
  %".85" = load i32, i32* %"j"
  %".86" = add i32 %".85", 1
  store i32 %".86", i32* %"j"
  %".88" = load i32, i32* %"j"
  %".89" = load i32, i32* %"i"
  %".90" = icmp slt i32 %".88", %".89"
  br i1 %".90", label %"while_begin.1", label %"while_end.1"
while_end.1.if:
  br label %"while_end"
while_end.1.else:
  br label %"while_end.1.endif"
while_end.1.endif:
  %".97" = load i32, i32* %"i"
  %".98" = sub i32 %".97", 1
  store i32 %".98", i32* %"i"
  %".100" = load i32, i32* %"i"
  %".101" = icmp sge i32 %".100", 0
  br i1 %".101", label %"while_begin", label %"while_end"
}

define i32 @"main"() 
{
entry:
  %"a" = alloca [5 x i32]
  %".2" = getelementptr [5 x i32], [5 x i32]* %"a", i32 0, i32 0
  store i32 2, i32* %".2"
  %".4" = getelementptr [5 x i32], [5 x i32]* %"a", i32 0, i32 1
  store i32 4, i32* %".4"
  %".6" = getelementptr [5 x i32], [5 x i32]* %"a", i32 0, i32 2
  store i32 6, i32* %".6"
  %".8" = getelementptr [5 x i32], [5 x i32]* %"a", i32 0, i32 3
  store i32 1, i32* %".8"
  %".10" = getelementptr [5 x i32], [5 x i32]* %"a", i32 0, i32 4
  store i32 4, i32* %".10"
  %"k" = alloca i32
  store i32 0, i32* %"k"
  %".13" = getelementptr inbounds [13 x i8], [13 x i8]* @"string", i32 0, i32 0
  %".14" = call i32 (i8*, ...) @"printf"(i8* %".13")
  br label %"while_cond"
while_cond:
  %".16" = load i32, i32* %"k"
  %".17" = icmp slt i32 %".16", 5
  br i1 %".17", label %"while_begin", label %"while_end"
while_begin:
  %".19" = load i32, i32* %"k"
  %".20" = icmp eq i32 %".19", 4
  br i1 %".20", label %"while_begin.if", label %"while_begin.else"
while_end:
  %".40" = getelementptr inbounds [3 x i8], [3 x i8]* @"string.3", i32 0, i32 0
  %".41" = call i32 (i8*, ...) @"printf"(i8* %".40")
  %".42" = load [5 x i32], [5 x i32]* %"a"
  %".43" = getelementptr [5 x i32], [5 x i32]* %"a", i32 0, i32 0
  call void @"sort"(i32* %".43", i32 5)
  store i32 0, i32* %"k"
  %".46" = getelementptr inbounds [13 x i8], [13 x i8]* @"string.4", i32 0, i32 0
  %".47" = call i32 (i8*, ...) @"printf"(i8* %".46")
  br label %"while_cond.1"
while_begin.if:
  %".22" = load i32, i32* %"k"
  %".23" = getelementptr [5 x i32], [5 x i32]* %"a", i32 0, i32 %".22"
  %".24" = load i32, i32* %".23"
  %".25" = getelementptr inbounds [3 x i8], [3 x i8]* @"string.1", i32 0, i32 0
  %".26" = call i32 (i8*, ...) @"printf"(i8* %".25", i32 %".24")
  br label %"while_begin.endif"
while_begin.else:
  %".28" = load i32, i32* %"k"
  %".29" = getelementptr [5 x i32], [5 x i32]* %"a", i32 0, i32 %".28"
  %".30" = load i32, i32* %".29"
  %".31" = getelementptr inbounds [5 x i8], [5 x i8]* @"string.2", i32 0, i32 0
  %".32" = call i32 (i8*, ...) @"printf"(i8* %".31", i32 %".30")
  br label %"while_begin.endif"
while_begin.endif:
  %".34" = load i32, i32* %"k"
  %".35" = add i32 %".34", 1
  store i32 %".35", i32* %"k"
  %".37" = load i32, i32* %"k"
  %".38" = icmp slt i32 %".37", 5
  br i1 %".38", label %"while_begin", label %"while_end"
while_cond.1:
  %".49" = load i32, i32* %"k"
  %".50" = icmp slt i32 %".49", 5
  br i1 %".50", label %"while_begin.1", label %"while_end.1"
while_begin.1:
  %".52" = load i32, i32* %"k"
  %".53" = icmp eq i32 %".52", 4
  br i1 %".53", label %"while_begin.1.if", label %"while_begin.1.else"
while_end.1:
  %".73" = getelementptr inbounds [3 x i8], [3 x i8]* @"string.7", i32 0, i32 0
  %".74" = call i32 (i8*, ...) @"printf"(i8* %".73")
  %"n" = alloca i32
  %".75" = getelementptr inbounds [34 x i8], [34 x i8]* @"string.8", i32 0, i32 0
  %".76" = call i32 (i8*, ...) @"printf"(i8* %".75")
  %".77" = getelementptr inbounds [3 x i8], [3 x i8]* @"string.9", i32 0, i32 0
  %".78" = call i32 (i8*, ...) @"scanf"(i8* %".77", i32* %"n")
  %"arr" = alloca i32*
  %".79" = load i32, i32* %"n"
  %".80" = mul i32 32, %".79"
  %".81" = call i8* @"malloc"(i32 %".80")
  %".82" = bitcast i8* %".81" to i32*
  store i32* %".82", i32** %"arr"
  %"i" = alloca i32
  store i32 0, i32* %"i"
  %".85" = load i32, i32* %"n"
  %".86" = getelementptr inbounds [8 x i8], [8 x i8]* @"string.10", i32 0, i32 0
  %".87" = call i32 (i8*, ...) @"printf"(i8* %".86", i32 %".85")
  %".88" = getelementptr inbounds [19 x i8], [19 x i8]* @"string.11", i32 0, i32 0
  %".89" = call i32 (i8*, ...) @"printf"(i8* %".88")
  br label %"while_cond.2"
while_begin.1.if:
  %".55" = load i32, i32* %"k"
  %".56" = getelementptr [5 x i32], [5 x i32]* %"a", i32 0, i32 %".55"
  %".57" = load i32, i32* %".56"
  %".58" = getelementptr inbounds [3 x i8], [3 x i8]* @"string.5", i32 0, i32 0
  %".59" = call i32 (i8*, ...) @"printf"(i8* %".58", i32 %".57")
  br label %"while_begin.1.endif"
while_begin.1.else:
  %".61" = load i32, i32* %"k"
  %".62" = getelementptr [5 x i32], [5 x i32]* %"a", i32 0, i32 %".61"
  %".63" = load i32, i32* %".62"
  %".64" = getelementptr inbounds [5 x i8], [5 x i8]* @"string.6", i32 0, i32 0
  %".65" = call i32 (i8*, ...) @"printf"(i8* %".64", i32 %".63")
  br label %"while_begin.1.endif"
while_begin.1.endif:
  %".67" = load i32, i32* %"k"
  %".68" = add i32 %".67", 1
  store i32 %".68", i32* %"k"
  %".70" = load i32, i32* %"k"
  %".71" = icmp slt i32 %".70", 5
  br i1 %".71", label %"while_begin.1", label %"while_end.1"
while_cond.2:
  %".91" = load i32, i32* %"i"
  %".92" = load i32, i32* %"n"
  %".93" = icmp slt i32 %".91", %".92"
  br i1 %".93", label %"while_begin.2", label %"while_end.2"
while_begin.2:
  %".95" = load i32*, i32** %"arr"
  %".96" = load i32, i32* %"i"
  %".97" = ptrtoint i32* %".95" to i64
  %".98" = sext i32 %".96" to i64
  %".99" = mul i64 4, %".98"
  %".100" = add i64 %".97", %".99"
  %".101" = inttoptr i64 %".100" to i32*
  %".102" = getelementptr inbounds [3 x i8], [3 x i8]* @"string.12", i32 0, i32 0
  %".103" = call i32 (i8*, ...) @"scanf"(i8* %".102", i32* %".101")
  %".104" = load i32, i32* %"i"
  %".105" = add i32 %".104", 1
  store i32 %".105", i32* %"i"
  %".107" = load i32, i32* %"i"
  %".108" = load i32, i32* %"n"
  %".109" = icmp slt i32 %".107", %".108"
  br i1 %".109", label %"while_begin.2", label %"while_end.2"
while_end.2:
  %".111" = load i32, i32* %"n"
  %".112" = load i32*, i32** %"arr"
  call void @"sort"(i32* %".112", i32 %".111")
  %".114" = getelementptr inbounds [22 x i8], [22 x i8]* @"string.13", i32 0, i32 0
  %".115" = call i32 (i8*, ...) @"printf"(i8* %".114")
  store i32 0, i32* %"i"
  br label %"while_cond.3"
while_cond.3:
  %".118" = load i32, i32* %"i"
  %".119" = load i32, i32* %"n"
  %".120" = icmp slt i32 %".118", %".119"
  br i1 %".120", label %"while_begin.3", label %"while_end.3"
while_begin.3:
  %".122" = load i32, i32* %"i"
  %".123" = load i32*, i32** %"arr"
  %".124" = getelementptr i32, i32* %".123", i32 %".122"
  %".125" = load i32, i32* %".124"
  %".126" = getelementptr inbounds [4 x i8], [4 x i8]* @"string.14", i32 0, i32 0
  %".127" = call i32 (i8*, ...) @"printf"(i8* %".126", i32 %".125")
  %".128" = load i32, i32* %"i"
  %".129" = add i32 %".128", 1
  store i32 %".129", i32* %"i"
  %".131" = load i32, i32* %"i"
  %".132" = load i32, i32* %"n"
  %".133" = icmp slt i32 %".131", %".132"
  br i1 %".133", label %"while_begin.3", label %"while_end.3"
while_end.3:
  %".135" = getelementptr inbounds [2 x i8], [2 x i8]* @"string.15", i32 0, i32 0
  %".136" = call i32 (i8*, ...) @"printf"(i8* %".135")
  %".137" = load i32*, i32** %"arr"
  %".138" = bitcast i32* %".137" to i8*
  call void @"free"(i8* %".138")
  ret i32 0
}

@"string" = constant [13 x i8] c"\e5\88\9d\e5\a7\8b a = {\00"
@"string.1" = constant [3 x i8] c"%d\00"
@"string.2" = constant [5 x i8] c"%d, \00"
@"string.3" = constant [3 x i8] c"}\0a\00"
@"string.4" = constant [13 x i8] c"\e6\8e\92\e5\ba\8f a = {\00"
@"string.5" = constant [3 x i8] c"%d\00"
@"string.6" = constant [5 x i8] c"%d, \00"
@"string.7" = constant [3 x i8] c"}\0a\00"
@"string.8" = constant [34 x i8] c"\e8\af\b7\e8\be\93\e5\85\a5\e6\95\b0\e7\bb\84\e7\9a\84\e5\85\83\e7\b4\a0\e4\b8\aa\e6\95\b0\ef\bc\9a\00"
@"string.9" = constant [3 x i8] c"%d\00"
@"string.10" = constant [8 x i8] c"n = %d\0a\00"
@"string.11" = constant [19 x i8] c"\e8\af\b7\e8\be\93\e5\85\a5\e5\85\83\e7\b4\a0\ef\bc\9a\00"
@"string.12" = constant [3 x i8] c"%d\00"
@"string.13" = constant [22 x i8] c"\e6\95\b0\e7\bb\84\e6\8e\92\e5\ba\8f\e7\bb\93\e6\9e\9c\ef\bc\9a\00"
@"string.14" = constant [4 x i8] c"%d \00"
@"string.15" = constant [2 x i8] c"\0a\00"