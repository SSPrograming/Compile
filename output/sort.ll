; ModuleID = ""
target triple = "x86_64-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...) 

declare i32 @"scanf"(i8* %".1", ...) 

declare i8* @"malloc"(i32 %".1") 

declare void @"free"(i8* %".1") 

define void @"sort"(i32* %".1", i32 %".2") 
{
entry:
  %".4" = alloca i32*
  store i32* %".1", i32** %".4"
  %".6" = alloca i32
  store i32 %".2", i32* %".6"
  %"i" = alloca i32
  %".8" = load i32, i32* %".6"
  %".9" = sub i32 %".8", 1
  store i32 %".9", i32* %"i"
  %"j" = alloca i32
  store i32 0, i32* %"j"
  %"change" = alloca i32
  store i32 0, i32* %"change"
  br label %"while_cond"
while_cond:
  %".96" = load i32, i32* %"i"
  %".97" = icmp sge i32 %".96", 0
  %".98" = xor i1 %".97", -1
  br i1 %".98", label %"while_end.1", label %"while_begin"
while_begin:
  store i32 0, i32* %"j"
  br label %"while_cond.1"
while_cond.1:
  %".80" = load i32, i32* %"j"
  %".81" = load i32, i32* %"i"
  %".82" = icmp slt i32 %".80", %".81"
  %".83" = xor i1 %".82", -1
  br i1 %".83", label %"while_end", label %"while_begin.1"
while_begin.1:
  %".16" = load i32, i32* %"j"
  %".17" = load i32*, i32** %".4"
  %".18" = getelementptr i32, i32* %".17", i32 %".16"
  %".19" = load i32, i32* %".18"
  %".20" = load i32, i32* %"j"
  %".21" = add i32 %".20", 1
  %".22" = load i32*, i32** %".4"
  %".23" = getelementptr i32, i32* %".22", i32 %".21"
  %".24" = load i32, i32* %".23"
  %".25" = icmp sgt i32 %".19", %".24"
  br i1 %".25", label %"while_begin.1.if", label %"while_begin.1.else"
while_begin.1.if:
  %".27" = load i32, i32* %"j"
  %".28" = load i32*, i32** %".4"
  %".29" = getelementptr i32, i32* %".28", i32 %".27"
  %".30" = load i32, i32* %"j"
  %".31" = add i32 %".30", 1
  %".32" = load i32*, i32** %".4"
  %".33" = getelementptr i32, i32* %".32", i32 %".31"
  %".34" = load i32, i32* %".33"
  %".35" = load i32, i32* %"j"
  %".36" = load i32*, i32** %".4"
  %".37" = getelementptr i32, i32* %".36", i32 %".35"
  %".38" = load i32, i32* %".37"
  %".39" = add i32 %".34", %".38"
  store i32 %".39", i32* %".29"
  %".41" = load i32, i32* %"j"
  %".42" = add i32 %".41", 1
  %".43" = load i32*, i32** %".4"
  %".44" = getelementptr i32, i32* %".43", i32 %".42"
  %".45" = load i32, i32* %"j"
  %".46" = load i32*, i32** %".4"
  %".47" = getelementptr i32, i32* %".46", i32 %".45"
  %".48" = load i32, i32* %".47"
  %".49" = load i32, i32* %"j"
  %".50" = add i32 %".49", 1
  %".51" = load i32*, i32** %".4"
  %".52" = getelementptr i32, i32* %".51", i32 %".50"
  %".53" = load i32, i32* %".52"
  %".54" = sub i32 %".48", %".53"
  store i32 %".54", i32* %".44"
  %".56" = load i32, i32* %"j"
  %".57" = load i32*, i32** %".4"
  %".58" = getelementptr i32, i32* %".57", i32 %".56"
  %".59" = load i32, i32* %"j"
  %".60" = load i32*, i32** %".4"
  %".61" = getelementptr i32, i32* %".60", i32 %".59"
  %".62" = load i32, i32* %".61"
  %".63" = load i32, i32* %"j"
  %".64" = add i32 %".63", 1
  %".65" = load i32*, i32** %".4"
  %".66" = getelementptr i32, i32* %".65", i32 %".64"
  %".67" = load i32, i32* %".66"
  %".68" = sub i32 %".62", %".67"
  store i32 %".68", i32* %".58"
  store i32 1, i32* %"change"
  br label %"while_begin.1.endif"
while_begin.1.else:
  br label %"while_begin.1.endif"
while_begin.1.endif:
  %".73" = load i32, i32* %"j"
  %".74" = add i32 %".73", 1
  store i32 %".74", i32* %"j"
  %".76" = load i32, i32* %"j"
  %".77" = load i32, i32* %"i"
  %".78" = icmp slt i32 %".76", %".77"
  br i1 %".78", label %"while_begin.1", label %"while_end"
while_end:
  %".85" = load i32, i32* %"change"
  %".86" = icmp eq i32 %".85", 0
  br i1 %".86", label %"while_end.if", label %"while_end.else"
while_end.if:
  br label %"while_end.endif"
while_end.else:
  br label %"while_end.endif"
while_end.endif:
  %".90" = load i32, i32* %"i"
  %".91" = sub i32 %".90", 1
  store i32 %".91", i32* %"i"
  %".93" = load i32, i32* %"i"
  %".94" = icmp sge i32 %".93", 0
  br i1 %".94", label %"while_begin", label %"while_end.1"
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
  %".29" = load i32, i32* %"i"
  %".30" = load i32, i32* %"n"
  %".31" = icmp slt i32 %".29", %".30"
  %".32" = xor i1 %".31", -1
  br i1 %".32", label %"while_end", label %"while_begin"
while_begin:
  %".14" = load i32*, i32** %"arr"
  %".15" = ptrtoint i32* %".14" to i32
  %".16" = load i32, i32* %"i"
  %".17" = mul i32 4, %".16"
  %".18" = add i32 %".15", %".17"
  %".19" = inttoptr i32 %".18" to i32*
  %".20" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.2", i32 0, i32 0
  %".21" = call i32 (i8*, ...) @"scanf"(i8* %".20", i32* %".19")
  %".22" = load i32, i32* %"i"
  %".23" = add i32 %".22", 1
  store i32 %".23", i32* %"i"
  %".25" = load i32, i32* %"i"
  %".26" = load i32, i32* %"n"
  %".27" = icmp slt i32 %".25", %".26"
  br i1 %".27", label %"while_begin", label %"while_end"
while_end:
  %".34" = load i32, i32* %"n"
  %".35" = load i32*, i32** %"arr"
  call void @"sort"(i32* %".35", i32 %".34")
  store i32 0, i32* %"i"
  br label %"while_cond.1"
while_cond.1:
  %".52" = load i32, i32* %"i"
  %".53" = load i32, i32* %"n"
  %".54" = icmp slt i32 %".52", %".53"
  %".55" = xor i1 %".54", -1
  br i1 %".55", label %"while_end.1", label %"while_begin.1"
while_begin.1:
  %".39" = load i32, i32* %"i"
  %".40" = load i32*, i32** %"arr"
  %".41" = getelementptr i32, i32* %".40", i32 %".39"
  %".42" = load i32, i32* %".41"
  %".43" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.3", i32 0, i32 0
  %".44" = call i32 (i8*, ...) @"printf"(i8* %".43", i32 %".42")
  %".45" = load i32, i32* %"i"
  %".46" = add i32 %".45", 1
  store i32 %".46", i32* %"i"
  %".48" = load i32, i32* %"i"
  %".49" = load i32, i32* %"n"
  %".50" = icmp slt i32 %".48", %".49"
  br i1 %".50", label %"while_begin.1", label %"while_end.1"
while_end.1:
  %".57" = getelementptr inbounds [2 x i8], [2 x i8]* @"str.4", i32 0, i32 0
  %".58" = call i32 (i8*, ...) @"printf"(i8* %".57")
  %".59" = load i32*, i32** %"arr"
  %".60" = bitcast i32* %".59" to i8*
  call void @"free"(i8* %".60")
  ret i32 0
}

@"str" = constant [3 x i8] c"%d\00"
@"str.1" = constant [8 x i8] c"n = %d\0a\00"
@"str.2" = constant [4 x i8] c"%d \00"
@"str.3" = constant [4 x i8] c"%d \00"
@"str.4" = constant [2 x i8] c"\0a\00"