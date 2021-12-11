; ModuleID = ""
target triple = "x86_64-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...) 

declare i32 @"scanf"(i8* %".1", ...) 

declare i8* @"malloc"(i32 %".1") 

declare void @"free"(i8* %".1") 

declare void @"exit"(i32 %".1") 

declare i32 @"isdigit"(i32 %".1") 

define i32 @"operatorCmp"(i8 %".1", i8 %".2") 
{
entry:
  %".4" = alloca i8
  store i8 %".1", i8* %".4"
  %".6" = alloca i8
  store i8 %".2", i8* %".6"
  %".8" = load i8, i8* %".4"
  %".9" = icmp eq i8 %".8", 43
  %".10" = load i8, i8* %".4"
  %".11" = icmp eq i8 %".10", 45
  %".12" = or i1 %".9", %".11"
  br i1 %".12", label %"entry.if", label %"entry.else"
entry.if:
  %".14" = load i8, i8* %".6"
  %".15" = icmp eq i8 %".14", 42
  %".16" = load i8, i8* %".6"
  %".17" = icmp eq i8 %".16", 47
  %".18" = or i1 %".15", %".17"
  %".19" = load i8, i8* %".6"
  %".20" = icmp eq i8 %".19", 40
  %".21" = or i1 %".18", %".20"
  br i1 %".21", label %"entry.if.if", label %"entry.if.else"
entry.else:
  br label %"entry.endif"
entry.endif:
  %".27" = load i8, i8* %".4"
  %".28" = icmp eq i8 %".27", 42
  %".29" = load i8, i8* %".4"
  %".30" = icmp eq i8 %".29", 47
  %".31" = or i1 %".28", %".30"
  br i1 %".31", label %"entry.endif.if", label %"entry.endif.else"
entry.if.if:
  ret i32 -1
entry.if.else:
  ret i32 1
entry.if.endif:
  br label %"entry.endif"
entry.endif.if:
  %".33" = load i8, i8* %".6"
  %".34" = icmp eq i8 %".33", 40
  br i1 %".34", label %"entry.endif.if.if", label %"entry.endif.if.else"
entry.endif.else:
  br label %"entry.endif.endif"
entry.endif.endif:
  %".40" = load i8, i8* %".4"
  %".41" = icmp eq i8 %".40", 40
  br i1 %".41", label %"entry.endif.endif.if", label %"entry.endif.endif.else"
entry.endif.if.if:
  ret i32 -1
entry.endif.if.else:
  ret i32 1
entry.endif.if.endif:
  br label %"entry.endif.endif"
entry.endif.endif.if:
  %".43" = load i8, i8* %".6"
  %".44" = icmp eq i8 %".43", 41
  br i1 %".44", label %"entry.endif.endif.if.if", label %"entry.endif.endif.if.else"
entry.endif.endif.else:
  br label %"entry.endif.endif.endif"
entry.endif.endif.endif:
  %".50" = load i8, i8* %".4"
  %".51" = icmp eq i8 %".50", 41
  br i1 %".51", label %"entry.endif.endif.endif.if", label %"entry.endif.endif.endif.else"
entry.endif.endif.if.if:
  ret i32 0
entry.endif.endif.if.else:
  ret i32 -1
entry.endif.endif.if.endif:
  br label %"entry.endif.endif.endif"
entry.endif.endif.endif.if:
  call void @"exit"(i32 -1)
  br label %"entry.endif.endif.endif.endif"
entry.endif.endif.endif.else:
  br label %"entry.endif.endif.endif.endif"
entry.endif.endif.endif.endif:
  %".56" = load i8, i8* %".4"
  %".57" = icmp eq i8 %".56", 0
  br i1 %".57", label %"entry.endif.endif.endif.endif.if", label %"entry.endif.endif.endif.endif.else"
entry.endif.endif.endif.endif.if:
  %".59" = load i8, i8* %".6"
  %".60" = icmp eq i8 %".59", 0
  br i1 %".60", label %"entry.endif.endif.endif.endif.if.if", label %"entry.endif.endif.endif.endif.if.else"
entry.endif.endif.endif.endif.else:
  br label %"entry.endif.endif.endif.endif.endif"
entry.endif.endif.endif.endif.endif:
entry.endif.endif.endif.endif.if.if:
  ret i32 0
entry.endif.endif.endif.endif.if.else:
  ret i32 -1
entry.endif.endif.endif.endif.if.endif:
  br label %"entry.endif.endif.endif.endif.endif"
}

define i32 @"calculate"(i32 %".1", i8 %".2", i32 %".3") 
{
entry:
  %".5" = alloca i32
  store i32 %".1", i32* %".5"
  %".7" = alloca i8
  store i8 %".2", i8* %".7"
  %".9" = alloca i32
  store i32 %".3", i32* %".9"
  %".11" = load i8, i8* %".7"
  %".12" = icmp eq i8 %".11", 43
  br i1 %".12", label %"entry.if", label %"entry.else"
entry.if:
  %".14" = load i32, i32* %".5"
  %".15" = load i32, i32* %".9"
  %".16" = add i32 %".14", %".15"
  ret i32 %".16"
entry.else:
  br label %"entry.endif"
entry.endif:
  %".19" = load i8, i8* %".7"
  %".20" = icmp eq i8 %".19", 45
  br i1 %".20", label %"entry.endif.if", label %"entry.endif.else"
entry.endif.if:
  %".22" = load i32, i32* %".5"
  %".23" = load i32, i32* %".9"
  %".24" = sub i32 %".22", %".23"
  ret i32 %".24"
entry.endif.else:
  br label %"entry.endif.endif"
entry.endif.endif:
  %".27" = load i8, i8* %".7"
  %".28" = icmp eq i8 %".27", 42
  br i1 %".28", label %"entry.endif.endif.if", label %"entry.endif.endif.else"
entry.endif.endif.if:
  %".30" = load i32, i32* %".5"
  %".31" = load i32, i32* %".9"
  %".32" = mul i32 %".30", %".31"
  ret i32 %".32"
entry.endif.endif.else:
  br label %"entry.endif.endif.endif"
entry.endif.endif.endif:
  %".35" = load i8, i8* %".7"
  %".36" = icmp eq i8 %".35", 47
  br i1 %".36", label %"entry.endif.endif.endif.if", label %"entry.endif.endif.endif.else"
entry.endif.endif.endif.if:
  %".38" = load i32, i32* %".5"
  %".39" = load i32, i32* %".9"
  %".40" = sdiv i32 %".38", %".39"
  ret i32 %".40"
entry.endif.endif.endif.else:
  br label %"entry.endif.endif.endif.endif"
entry.endif.endif.endif.endif:
  call void @"exit"(i32 -1)
}

define i32 @"evaluate"(i8* %".1") 
{
entry:
  %".3" = alloca i8*
  store i8* %".1", i8** %".3"
  %"opnd" = alloca [1024 x i32]
  %"optr" = alloca [1024 x i8]
  %"opnd_p" = alloca i32
  store i32 0, i32* %"opnd_p"
  %"optr_p" = alloca i32
  store i32 0, i32* %"optr_p"
  %".7" = load i32, i32* %"optr_p"
  %".8" = add i32 %".7", 1
  store i32 %".8", i32* %"optr_p"
  %".10" = load i32, i32* %"optr_p"
  %".11" = getelementptr [1024 x i8], [1024 x i8]* %"optr", i32 0, i32 %".10"
  store i8 0, i8* %".11"
  br label %"while_cond"
while_cond:
  %".142" = load i32, i32* %"optr_p"
  %".143" = icmp sgt i32 %".142", 0
  %".144" = xor i1 %".143", -1
  br i1 %".144", label %"while_end.1", label %"while_begin"
while_begin:
  %".14" = load i8*, i8** %".3"
  %".15" = load i8, i8* %".14"
  %".16" = sext i8 %".15" to i32
  %".17" = call i32 @"isdigit"(i32 %".16")
  %".18" = icmp ne i32 %".17", 0
  br i1 %".18", label %"while_begin.if", label %"while_begin.else"
while_begin.if:
  %"number" = alloca i32
  store i32 0, i32* %"number"
  br label %"while_cond.1"
while_begin.else:
  %"cmpResult" = alloca i32
  %".58" = load i8*, i8** %".3"
  %".59" = load i8, i8* %".58"
  %".60" = load i32, i32* %"optr_p"
  %".61" = getelementptr [1024 x i8], [1024 x i8]* %"optr", i32 0, i32 %".60"
  %".62" = load i8, i8* %".61"
  %".63" = call i32 @"operatorCmp"(i8 %".62", i8 %".59")
  store i32 %".63", i32* %"cmpResult"
  %".65" = load i32, i32* %"cmpResult"
  %".66" = icmp eq i32 %".65", -1
  br i1 %".66", label %"while_begin.else.if", label %"while_begin.else.else"
while_begin.endif:
  %".139" = load i32, i32* %"optr_p"
  %".140" = icmp sgt i32 %".139", 0
  br i1 %".140", label %"while_begin", label %"while_end.1"
while_cond.1:
  %".43" = load i8*, i8** %".3"
  %".44" = load i8, i8* %".43"
  %".45" = sext i8 %".44" to i32
  %".46" = call i32 @"isdigit"(i32 %".45")
  %".47" = icmp ne i32 %".46", 0
  %".48" = xor i1 %".47", -1
  br i1 %".48", label %"while_end", label %"while_begin.1"
while_begin.1:
  %".22" = load i32, i32* %"number"
  %".23" = mul i32 %".22", 10
  %".24" = load i8*, i8** %".3"
  %".25" = load i8, i8* %".24"
  %".26" = sub i8 %".25", 48
  %".27" = sext i8 %".26" to i32
  %".28" = add i32 %".23", %".27"
  store i32 %".28", i32* %"number"
  %".30" = load i8*, i8** %".3"
  %".31" = ptrtoint i8* %".30" to i64
  %".32" = sext i32 1 to i64
  %".33" = mul i64 1, %".32"
  %".34" = add i64 %".31", %".33"
  %".35" = inttoptr i64 %".34" to i8*
  store i8* %".35", i8** %".3"
  %".37" = load i8*, i8** %".3"
  %".38" = load i8, i8* %".37"
  %".39" = sext i8 %".38" to i32
  %".40" = call i32 @"isdigit"(i32 %".39")
  %".41" = icmp ne i32 %".40", 0
  br i1 %".41", label %"while_begin.1", label %"while_end"
while_end:
  %".50" = load i32, i32* %"opnd_p"
  %".51" = add i32 %".50", 1
  store i32 %".51", i32* %"opnd_p"
  %".53" = load i32, i32* %"opnd_p"
  %".54" = getelementptr [1024 x i32], [1024 x i32]* %"opnd", i32 0, i32 %".53"
  %".55" = load i32, i32* %"number"
  store i32 %".55", i32* %".54"
  br label %"while_begin.endif"
while_begin.else.if:
  %".68" = load i32, i32* %"optr_p"
  %".69" = add i32 %".68", 1
  store i32 %".69", i32* %"optr_p"
  %".71" = load i32, i32* %"optr_p"
  %".72" = getelementptr [1024 x i8], [1024 x i8]* %"optr", i32 0, i32 %".71"
  %".73" = load i8*, i8** %".3"
  %".74" = load i8, i8* %".73"
  store i8 %".74", i8* %".72"
  %".76" = load i8*, i8** %".3"
  %".77" = ptrtoint i8* %".76" to i64
  %".78" = sext i32 1 to i64
  %".79" = mul i64 1, %".78"
  %".80" = add i64 %".77", %".79"
  %".81" = inttoptr i64 %".80" to i8*
  store i8* %".81", i8** %".3"
  br label %"while_begin.else.endif"
while_begin.else.else:
  br label %"while_begin.else.endif"
while_begin.else.endif:
  %".85" = load i32, i32* %"cmpResult"
  %".86" = icmp eq i32 %".85", 0
  br i1 %".86", label %"while_begin.else.endif.if", label %"while_begin.else.endif.else"
while_begin.else.endif.if:
  %".88" = load i32, i32* %"optr_p"
  %".89" = sub i32 %".88", 1
  store i32 %".89", i32* %"optr_p"
  %".91" = load i8*, i8** %".3"
  %".92" = ptrtoint i8* %".91" to i64
  %".93" = sext i32 1 to i64
  %".94" = mul i64 1, %".93"
  %".95" = add i64 %".92", %".94"
  %".96" = inttoptr i64 %".95" to i8*
  store i8* %".96", i8** %".3"
  br label %"while_begin.else.endif.endif"
while_begin.else.endif.else:
  br label %"while_begin.else.endif.endif"
while_begin.else.endif.endif:
  %".100" = load i32, i32* %"cmpResult"
  %".101" = icmp eq i32 %".100", 1
  br i1 %".101", label %"while_begin.else.endif.endif.if", label %"while_begin.else.endif.endif.else"
while_begin.else.endif.endif.if:
  %"op_top" = alloca i8
  %".103" = load i32, i32* %"optr_p"
  %".104" = getelementptr [1024 x i8], [1024 x i8]* %"optr", i32 0, i32 %".103"
  %".105" = load i8, i8* %".104"
  store i8 %".105", i8* %"op_top"
  %".107" = load i32, i32* %"optr_p"
  %".108" = sub i32 %".107", 1
  store i32 %".108", i32* %"optr_p"
  %"number_2" = alloca i32
  %".110" = load i32, i32* %"opnd_p"
  %".111" = getelementptr [1024 x i32], [1024 x i32]* %"opnd", i32 0, i32 %".110"
  %".112" = load i32, i32* %".111"
  store i32 %".112", i32* %"number_2"
  %".114" = load i32, i32* %"opnd_p"
  %".115" = sub i32 %".114", 1
  store i32 %".115", i32* %"opnd_p"
  %"number_1" = alloca i32
  %".117" = load i32, i32* %"opnd_p"
  %".118" = getelementptr [1024 x i32], [1024 x i32]* %"opnd", i32 0, i32 %".117"
  %".119" = load i32, i32* %".118"
  store i32 %".119", i32* %"number_1"
  %".121" = load i32, i32* %"opnd_p"
  %".122" = sub i32 %".121", 1
  store i32 %".122", i32* %"opnd_p"
  %"cal_res" = alloca i32
  %".124" = load i32, i32* %"number_2"
  %".125" = load i8, i8* %"op_top"
  %".126" = load i32, i32* %"number_1"
  %".127" = call i32 @"calculate"(i32 %".126", i8 %".125", i32 %".124")
  store i32 %".127", i32* %"cal_res"
  %".129" = load i32, i32* %"opnd_p"
  %".130" = add i32 %".129", 1
  store i32 %".130", i32* %"opnd_p"
  %".132" = load i32, i32* %"opnd_p"
  %".133" = getelementptr [1024 x i32], [1024 x i32]* %"opnd", i32 0, i32 %".132"
  %".134" = load i32, i32* %"cal_res"
  store i32 %".134", i32* %".133"
  br label %"while_begin.else.endif.endif.endif"
while_begin.else.endif.endif.else:
  br label %"while_begin.else.endif.endif.endif"
while_begin.else.endif.endif.endif:
  br label %"while_begin.endif"
while_end.1:
  %".146" = load i32, i32* %"opnd_p"
  %".147" = getelementptr [1024 x i32], [1024 x i32]* %"opnd", i32 0, i32 %".146"
  %".148" = load i32, i32* %".147"
  ret i32 %".148"
}

define i32 @"main"() 
{
entry:
  %"str" = alloca [1024 x i8]
  %".2" = load [1024 x i8], [1024 x i8]* %"str"
  %".3" = getelementptr inbounds [3 x i8], [3 x i8]* @"str", i32 0, i32 0
  %".4" = alloca [1024 x i8]
  store [1024 x i8] %".2", [1024 x i8]* %".4"
  %".6" = getelementptr [1024 x i8], [1024 x i8]* %".4", i32 0, i32 0
  %".7" = call i32 (i8*, ...) @"scanf"(i8* %".3", i8* %".6")
  %"res" = alloca i32
  %".8" = load [1024 x i8], [1024 x i8]* %"str"
  %".9" = alloca [1024 x i8]
  store [1024 x i8] %".8", [1024 x i8]* %".9"
  %".11" = getelementptr [1024 x i8], [1024 x i8]* %".9", i32 0, i32 0
  %".12" = call i32 @"evaluate"(i8* %".11")
  store i32 %".12", i32* %"res"
  %".14" = load i32, i32* %"res"
  %".15" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.1", i32 0, i32 0
  %".16" = call i32 (i8*, ...) @"printf"(i8* %".15", i32 %".14")
  ret i32 0
}

@"str" = constant [3 x i8] c"%s\00"
@"str.1" = constant [4 x i8] c"%d\0a\00"