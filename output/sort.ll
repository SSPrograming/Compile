; ModuleID = ""
target triple = "x86_64-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...) 

declare i32 @"scanf"(i8* %".1", ...) 

declare i8* @"malloc"(i32 %".1") 

declare void @"free"(i8* %".1") 

declare void @"exit"(i32 %".1") 

declare i32 @"isdigit"(i32 %".1") 

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
  %".101" = load i32, i32* %"i"
  %".102" = icmp sge i32 %".101", 0
  %".103" = xor i1 %".102", -1
  br i1 %".103", label %"while_end.1", label %"while_begin"
while_begin:
  store i32 0, i32* %"j"
  br label %"while_cond.1"
while_cond.1:
  %".85" = load i32, i32* %"j"
  %".86" = load i32, i32* %"i"
  %".87" = icmp slt i32 %".85", %".86"
  %".88" = xor i1 %".87", -1
  br i1 %".88", label %"while_end", label %"while_begin.1"
while_begin.1:
  %".21" = load i32, i32* %"j"
  %".22" = load i32*, i32** %".4"
  %".23" = getelementptr i32, i32* %".22", i32 %".21"
  %".24" = load i32, i32* %".23"
  %".25" = load i32, i32* %"j"
  %".26" = add i32 %".25", 1
  %".27" = load i32*, i32** %".4"
  %".28" = getelementptr i32, i32* %".27", i32 %".26"
  %".29" = load i32, i32* %".28"
  %".30" = icmp sgt i32 %".24", %".29"
  br i1 %".30", label %"while_begin.1.if", label %"while_begin.1.else"
while_begin.1.if:
  %".32" = load i32, i32* %"j"
  %".33" = load i32*, i32** %".4"
  %".34" = getelementptr i32, i32* %".33", i32 %".32"
  %".35" = load i32, i32* %"j"
  %".36" = add i32 %".35", 1
  %".37" = load i32*, i32** %".4"
  %".38" = getelementptr i32, i32* %".37", i32 %".36"
  %".39" = load i32, i32* %".38"
  %".40" = load i32, i32* %"j"
  %".41" = load i32*, i32** %".4"
  %".42" = getelementptr i32, i32* %".41", i32 %".40"
  %".43" = load i32, i32* %".42"
  %".44" = add i32 %".39", %".43"
  store i32 %".44", i32* %".34"
  %".46" = load i32, i32* %"j"
  %".47" = add i32 %".46", 1
  %".48" = load i32*, i32** %".4"
  %".49" = getelementptr i32, i32* %".48", i32 %".47"
  %".50" = load i32, i32* %"j"
  %".51" = load i32*, i32** %".4"
  %".52" = getelementptr i32, i32* %".51", i32 %".50"
  %".53" = load i32, i32* %".52"
  %".54" = load i32, i32* %"j"
  %".55" = add i32 %".54", 1
  %".56" = load i32*, i32** %".4"
  %".57" = getelementptr i32, i32* %".56", i32 %".55"
  %".58" = load i32, i32* %".57"
  %".59" = sub i32 %".53", %".58"
  store i32 %".59", i32* %".49"
  %".61" = load i32, i32* %"j"
  %".62" = load i32*, i32** %".4"
  %".63" = getelementptr i32, i32* %".62", i32 %".61"
  %".64" = load i32, i32* %"j"
  %".65" = load i32*, i32** %".4"
  %".66" = getelementptr i32, i32* %".65", i32 %".64"
  %".67" = load i32, i32* %".66"
  %".68" = load i32, i32* %"j"
  %".69" = add i32 %".68", 1
  %".70" = load i32*, i32** %".4"
  %".71" = getelementptr i32, i32* %".70", i32 %".69"
  %".72" = load i32, i32* %".71"
  %".73" = sub i32 %".67", %".72"
  store i32 %".73", i32* %".63"
  store i32 1, i32* %"change"
  br label %"while_begin.1.endif"
while_begin.1.else:
  br label %"while_begin.1.endif"
while_begin.1.endif:
  %".78" = load i32, i32* %"j"
  %".79" = add i32 %".78", 1
  store i32 %".79", i32* %"j"
  %".81" = load i32, i32* %"j"
  %".82" = load i32, i32* %"i"
  %".83" = icmp slt i32 %".81", %".82"
  br i1 %".83", label %"while_begin.1", label %"while_end"
while_end:
  %".90" = load i32, i32* %"change"
  %".91" = icmp eq i32 %".90", 0
  br i1 %".91", label %"while_end.if", label %"while_end.else"
while_end.if:
  br label %"while_end.endif"
while_end.else:
  br label %"while_end.endif"
while_end.endif:
  %".95" = load i32, i32* %"i"
  %".96" = sub i32 %".95", 1
  store i32 %".96", i32* %"i"
  %".98" = load i32, i32* %"i"
  %".99" = icmp sge i32 %".98", 0
  br i1 %".99", label %"while_begin", label %"while_end.1"
while_end.1:
  ret void
}

define i32 @"main"() 
{
entry:
  %"n" = alloca i32
  %".2" = getelementptr inbounds [3 x i8], [3 x i8]* @"str", i32 0, i32 0
  %".3" = call i32 (i8*, ...) @"scanf"(i8* %".2", i32* %"n")
  %"arr" = alloca i32*
  %".4" = load i32, i32* %"n"
  %".5" = mul i32 4, %".4"
  %".6" = call i8* @"malloc"(i32 %".5")
  %".7" = bitcast i8* %".6" to i32*
  store i32* %".7", i32** %"arr"
  %"i" = alloca i32
  store i32 0, i32* %"i"
  %".10" = load i32, i32* %"n"
  %".11" = getelementptr inbounds [8 x i8], [8 x i8]* @"str.1", i32 0, i32 0
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".11", i32 %".10")
  br label %"while_cond"
while_cond:
  %".36" = load i32, i32* %"i"
  %".37" = load i32, i32* %"n"
  %".38" = icmp slt i32 %".36", %".37"
  %".39" = xor i1 %".38", -1
  br i1 %".39", label %"while_end", label %"while_begin"
while_begin:
  %".14" = load i32*, i32** %"arr"
  %".15" = load i32, i32* %"i"
  %".16" = ptrtoint i32* %".14" to i64
  %".17" = sext i32 %".15" to i64
  %".18" = mul i64 4, %".17"
  %".19" = add i64 %".16", %".18"
  %".20" = inttoptr i64 %".19" to i32*
  %".21" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.2", i32 0, i32 0
  %".22" = call i32 (i8*, ...) @"scanf"(i8* %".21", i32* %".20")
  %".23" = load i32, i32* %"i"
  %".24" = load i32*, i32** %"arr"
  %".25" = getelementptr i32, i32* %".24", i32 %".23"
  %".26" = load i32, i32* %".25"
  %".27" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.3", i32 0, i32 0
  %".28" = call i32 (i8*, ...) @"printf"(i8* %".27", i32 %".26")
  %".29" = load i32, i32* %"i"
  %".30" = add i32 %".29", 1
  store i32 %".30", i32* %"i"
  %".32" = load i32, i32* %"i"
  %".33" = load i32, i32* %"n"
  %".34" = icmp slt i32 %".32", %".33"
  br i1 %".34", label %"while_begin", label %"while_end"
while_end:
  %".41" = load i32, i32* %"n"
  %".42" = load i32*, i32** %"arr"
  call void @"sort"(i32* %".42", i32 %".41")
  store i32 0, i32* %"i"
  br label %"while_cond.1"
while_cond.1:
  %".59" = load i32, i32* %"i"
  %".60" = load i32, i32* %"n"
  %".61" = icmp slt i32 %".59", %".60"
  %".62" = xor i1 %".61", -1
  br i1 %".62", label %"while_end.1", label %"while_begin.1"
while_begin.1:
  %".46" = load i32, i32* %"i"
  %".47" = load i32*, i32** %"arr"
  %".48" = getelementptr i32, i32* %".47", i32 %".46"
  %".49" = load i32, i32* %".48"
  %".50" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.4", i32 0, i32 0
  %".51" = call i32 (i8*, ...) @"printf"(i8* %".50", i32 %".49")
  %".52" = load i32, i32* %"i"
  %".53" = add i32 %".52", 1
  store i32 %".53", i32* %"i"
  %".55" = load i32, i32* %"i"
  %".56" = load i32, i32* %"n"
  %".57" = icmp slt i32 %".55", %".56"
  br i1 %".57", label %"while_begin.1", label %"while_end.1"
while_end.1:
  %".64" = getelementptr inbounds [2 x i8], [2 x i8]* @"str.5", i32 0, i32 0
  %".65" = call i32 (i8*, ...) @"printf"(i8* %".64")
  %".66" = load i32*, i32** %"arr"
  %".67" = bitcast i32* %".66" to i8*
  call void @"free"(i8* %".67")
  ret i32 0
}

@"str" = constant [3 x i8] c"%d\00"
@"str.1" = constant [8 x i8] c"n = %d\0a\00"
@"str.2" = constant [3 x i8] c"%d\00"
@"str.3" = constant [4 x i8] c"%d\0a\00"
@"str.4" = constant [4 x i8] c"%d \00"
@"str.5" = constant [2 x i8] c"\0a\00"