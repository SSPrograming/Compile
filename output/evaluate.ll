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
  ret i32 0
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
  ret i32 0
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
  %".14" = load i32, i32* %"optr_p"
  %".15" = icmp sgt i32 %".14", 0
  br i1 %".15", label %"while_begin", label %"while_end"
while_begin:
  %".17" = load i8*, i8** %".3"
  %".18" = load i8, i8* %".17"
  %".19" = sext i8 %".18" to i32
  %".20" = call i32 @"isdigit"(i32 %".19")
  %".21" = icmp ne i32 %".20", 0
  br i1 %".21", label %"while_begin.if", label %"while_begin.else"
while_end:
  %".144" = load i32, i32* %"opnd_p"
  %".145" = getelementptr [1024 x i32], [1024 x i32]* %"opnd", i32 0, i32 %".144"
  %".146" = load i32, i32* %".145"
  ret i32 %".146"
while_begin.if:
  %"number" = alloca i32
  store i32 0, i32* %"number"
  br label %"while_cond.1"
while_begin.else:
  %"cmpResult" = alloca i32
  %".60" = load i8*, i8** %".3"
  %".61" = load i8, i8* %".60"
  %".62" = load i32, i32* %"optr_p"
  %".63" = getelementptr [1024 x i8], [1024 x i8]* %"optr", i32 0, i32 %".62"
  %".64" = load i8, i8* %".63"
  %".65" = call i32 @"operatorCmp"(i8 %".64", i8 %".61")
  store i32 %".65", i32* %"cmpResult"
  %".67" = load i32, i32* %"cmpResult"
  %".68" = icmp eq i32 %".67", -1
  br i1 %".68", label %"while_begin.else.if", label %"while_begin.else.else"
while_begin.endif:
  %".141" = load i32, i32* %"optr_p"
  %".142" = icmp sgt i32 %".141", 0
  br i1 %".142", label %"while_begin", label %"while_end"
while_cond.1:
  %".25" = load i8*, i8** %".3"
  %".26" = load i8, i8* %".25"
  %".27" = sext i8 %".26" to i32
  %".28" = call i32 @"isdigit"(i32 %".27")
  %".29" = icmp ne i32 %".28", 0
  br i1 %".29", label %"while_begin.1", label %"while_end.1"
while_begin.1:
  %".31" = load i32, i32* %"number"
  %".32" = mul i32 %".31", 10
  %".33" = load i8*, i8** %".3"
  %".34" = load i8, i8* %".33"
  %".35" = sub i8 %".34", 48
  %".36" = sext i8 %".35" to i32
  %".37" = add i32 %".32", %".36"
  store i32 %".37", i32* %"number"
  %".39" = load i8*, i8** %".3"
  %".40" = ptrtoint i8* %".39" to i64
  %".41" = sext i32 1 to i64
  %".42" = mul i64 1, %".41"
  %".43" = add i64 %".40", %".42"
  %".44" = inttoptr i64 %".43" to i8*
  store i8* %".44", i8** %".3"
  %".46" = load i8*, i8** %".3"
  %".47" = load i8, i8* %".46"
  %".48" = sext i8 %".47" to i32
  %".49" = call i32 @"isdigit"(i32 %".48")
  %".50" = icmp ne i32 %".49", 0
  br i1 %".50", label %"while_begin.1", label %"while_end.1"
while_end.1:
  %".52" = load i32, i32* %"opnd_p"
  %".53" = add i32 %".52", 1
  store i32 %".53", i32* %"opnd_p"
  %".55" = load i32, i32* %"opnd_p"
  %".56" = getelementptr [1024 x i32], [1024 x i32]* %"opnd", i32 0, i32 %".55"
  %".57" = load i32, i32* %"number"
  store i32 %".57", i32* %".56"
  br label %"while_begin.endif"
while_begin.else.if:
  %".70" = load i32, i32* %"optr_p"
  %".71" = add i32 %".70", 1
  store i32 %".71", i32* %"optr_p"
  %".73" = load i32, i32* %"optr_p"
  %".74" = getelementptr [1024 x i8], [1024 x i8]* %"optr", i32 0, i32 %".73"
  %".75" = load i8*, i8** %".3"
  %".76" = load i8, i8* %".75"
  store i8 %".76", i8* %".74"
  %".78" = load i8*, i8** %".3"
  %".79" = ptrtoint i8* %".78" to i64
  %".80" = sext i32 1 to i64
  %".81" = mul i64 1, %".80"
  %".82" = add i64 %".79", %".81"
  %".83" = inttoptr i64 %".82" to i8*
  store i8* %".83", i8** %".3"
  br label %"while_begin.else.endif"
while_begin.else.else:
  br label %"while_begin.else.endif"
while_begin.else.endif:
  %".87" = load i32, i32* %"cmpResult"
  %".88" = icmp eq i32 %".87", 0
  br i1 %".88", label %"while_begin.else.endif.if", label %"while_begin.else.endif.else"
while_begin.else.endif.if:
  %".90" = load i32, i32* %"optr_p"
  %".91" = sub i32 %".90", 1
  store i32 %".91", i32* %"optr_p"
  %".93" = load i8*, i8** %".3"
  %".94" = ptrtoint i8* %".93" to i64
  %".95" = sext i32 1 to i64
  %".96" = mul i64 1, %".95"
  %".97" = add i64 %".94", %".96"
  %".98" = inttoptr i64 %".97" to i8*
  store i8* %".98", i8** %".3"
  br label %"while_begin.else.endif.endif"
while_begin.else.endif.else:
  br label %"while_begin.else.endif.endif"
while_begin.else.endif.endif:
  %".102" = load i32, i32* %"cmpResult"
  %".103" = icmp eq i32 %".102", 1
  br i1 %".103", label %"while_begin.else.endif.endif.if", label %"while_begin.else.endif.endif.else"
while_begin.else.endif.endif.if:
  %"op_top" = alloca i8
  %".105" = load i32, i32* %"optr_p"
  %".106" = getelementptr [1024 x i8], [1024 x i8]* %"optr", i32 0, i32 %".105"
  %".107" = load i8, i8* %".106"
  store i8 %".107", i8* %"op_top"
  %".109" = load i32, i32* %"optr_p"
  %".110" = sub i32 %".109", 1
  store i32 %".110", i32* %"optr_p"
  %"number_2" = alloca i32
  %".112" = load i32, i32* %"opnd_p"
  %".113" = getelementptr [1024 x i32], [1024 x i32]* %"opnd", i32 0, i32 %".112"
  %".114" = load i32, i32* %".113"
  store i32 %".114", i32* %"number_2"
  %".116" = load i32, i32* %"opnd_p"
  %".117" = sub i32 %".116", 1
  store i32 %".117", i32* %"opnd_p"
  %"number_1" = alloca i32
  %".119" = load i32, i32* %"opnd_p"
  %".120" = getelementptr [1024 x i32], [1024 x i32]* %"opnd", i32 0, i32 %".119"
  %".121" = load i32, i32* %".120"
  store i32 %".121", i32* %"number_1"
  %".123" = load i32, i32* %"opnd_p"
  %".124" = sub i32 %".123", 1
  store i32 %".124", i32* %"opnd_p"
  %"cal_res" = alloca i32
  %".126" = load i32, i32* %"number_2"
  %".127" = load i8, i8* %"op_top"
  %".128" = load i32, i32* %"number_1"
  %".129" = call i32 @"calculate"(i32 %".128", i8 %".127", i32 %".126")
  store i32 %".129", i32* %"cal_res"
  %".131" = load i32, i32* %"opnd_p"
  %".132" = add i32 %".131", 1
  store i32 %".132", i32* %"opnd_p"
  %".134" = load i32, i32* %"opnd_p"
  %".135" = getelementptr [1024 x i32], [1024 x i32]* %"opnd", i32 0, i32 %".134"
  %".136" = load i32, i32* %"cal_res"
  store i32 %".136", i32* %".135"
  br label %"while_begin.else.endif.endif.endif"
while_begin.else.endif.endif.else:
  br label %"while_begin.else.endif.endif.endif"
while_begin.else.endif.endif.endif:
  br label %"while_begin.endif"
}

define i32 @"main"() 
{
entry:
  %"str" = alloca [1024 x i8]
  %".2" = load [1024 x i8], [1024 x i8]* %"str"
  %".3" = getelementptr inbounds [3 x i8], [3 x i8]* @"str", i32 0, i32 0
  %".4" = getelementptr [1024 x i8], [1024 x i8]* %"str", i32 0, i32 0
  %".5" = call i32 (i8*, ...) @"scanf"(i8* %".3", i8* %".4")
  %".6" = load [1024 x i8], [1024 x i8]* %"str"
  %".7" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.1", i32 0, i32 0
  %".8" = getelementptr [1024 x i8], [1024 x i8]* %"str", i32 0, i32 0
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".7", i8* %".8")
  %"res" = alloca i32
  %".10" = load [1024 x i8], [1024 x i8]* %"str"
  %".11" = getelementptr [1024 x i8], [1024 x i8]* %"str", i32 0, i32 0
  %".12" = call i32 @"evaluate"(i8* %".11")
  store i32 %".12", i32* %"res"
  %".14" = load i32, i32* %"res"
  %".15" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.2", i32 0, i32 0
  %".16" = call i32 (i8*, ...) @"printf"(i8* %".15", i32 %".14")
  ret i32 0
}

@"str" = constant [3 x i8] c"%s\00"
@"str.1" = constant [4 x i8] c"%s\0a\00"
@"str.2" = constant [4 x i8] c"%d\0a\00"