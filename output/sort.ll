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
  %"n" = alloca i32
  %".2" = getelementptr inbounds [3 x i8], [3 x i8]* @"str", i32 0, i32 0
  %".3" = call i32 (i8*, ...) @"scanf"(i8* %".2", i32* %"n")
  %"arr" = alloca i32*
  %".4" = load i32, i32* %"n"
  %".5" = mul i32 32, %".4"
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
  %".14" = load i32, i32* %"i"
  %".15" = load i32, i32* %"n"
  %".16" = icmp slt i32 %".14", %".15"
  br i1 %".16", label %"while_begin", label %"while_end"
while_begin:
  %".18" = load i32*, i32** %"arr"
  %".19" = load i32, i32* %"i"
  %".20" = ptrtoint i32* %".18" to i64
  %".21" = sext i32 %".19" to i64
  %".22" = mul i64 4, %".21"
  %".23" = add i64 %".20", %".22"
  %".24" = inttoptr i64 %".23" to i32*
  %".25" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.2", i32 0, i32 0
  %".26" = call i32 (i8*, ...) @"scanf"(i8* %".25", i32* %".24")
  %".27" = load i32, i32* %"i"
  %".28" = add i32 %".27", 1
  store i32 %".28", i32* %"i"
  %".30" = load i32, i32* %"i"
  %".31" = load i32, i32* %"n"
  %".32" = icmp slt i32 %".30", %".31"
  br i1 %".32", label %"while_begin", label %"while_end"
while_end:
  %".34" = load i32, i32* %"n"
  %".35" = load i32*, i32** %"arr"
  call void @"sort"(i32* %".35", i32 %".34")
  store i32 0, i32* %"i"
  br label %"while_cond.1"
while_cond.1:
  %".39" = load i32, i32* %"i"
  %".40" = load i32, i32* %"n"
  %".41" = icmp slt i32 %".39", %".40"
  br i1 %".41", label %"while_begin.1", label %"while_end.1"
while_begin.1:
  %".43" = load i32, i32* %"i"
  %".44" = load i32*, i32** %"arr"
  %".45" = getelementptr i32, i32* %".44", i32 %".43"
  %".46" = load i32, i32* %".45"
  %".47" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.3", i32 0, i32 0
  %".48" = call i32 (i8*, ...) @"printf"(i8* %".47", i32 %".46")
  %".49" = load i32, i32* %"i"
  %".50" = add i32 %".49", 1
  store i32 %".50", i32* %"i"
  %".52" = load i32, i32* %"i"
  %".53" = load i32, i32* %"n"
  %".54" = icmp slt i32 %".52", %".53"
  br i1 %".54", label %"while_begin.1", label %"while_end.1"
while_end.1:
  %".56" = getelementptr inbounds [2 x i8], [2 x i8]* @"str.4", i32 0, i32 0
  %".57" = call i32 (i8*, ...) @"printf"(i8* %".56")
  %".58" = load i32*, i32** %"arr"
  %".59" = bitcast i32* %".58" to i8*
  call void @"free"(i8* %".59")
  ret i32 0
}

@"str" = constant [3 x i8] c"%d\00"
@"str.1" = constant [8 x i8] c"n = %d\0a\00"
@"str.2" = constant [3 x i8] c"%d\00"
@"str.3" = constant [4 x i8] c"%d \00"
@"str.4" = constant [2 x i8] c"\0a\00"