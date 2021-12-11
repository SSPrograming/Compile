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

define double @"calculate"(double %".1", i8 %".2", double %".3") 
{
entry:
  %".5" = alloca double
  store double %".1", double* %".5"
  %".7" = alloca i8
  store i8 %".2", i8* %".7"
  %".9" = alloca double
  store double %".3", double* %".9"
  %".11" = load i8, i8* %".7"
  %".12" = icmp eq i8 %".11", 43
  br i1 %".12", label %"entry.if", label %"entry.else"
entry.if:
  %".14" = load double, double* %".5"
  %".15" = load double, double* %".9"
  %".16" = add double %".14", %".15"
  ret double %".16"
entry.else:
  br label %"entry.endif"
entry.endif:
  %".19" = load i8, i8* %".7"
  %".20" = icmp eq i8 %".19", 45
  br i1 %".20", label %"entry.endif.if", label %"entry.endif.else"
entry.endif.if:
  %".22" = load double, double* %".5"
  %".23" = load double, double* %".9"
  %".24" = sub double %".22", %".23"
  ret double %".24"
entry.endif.else:
  br label %"entry.endif.endif"
entry.endif.endif:
  %".27" = load i8, i8* %".7"
  %".28" = icmp eq i8 %".27", 42
  br i1 %".28", label %"entry.endif.endif.if", label %"entry.endif.endif.else"
entry.endif.endif.if:
  %".30" = load double, double* %".5"
  %".31" = load double, double* %".9"
  %".32" = mul double %".30", %".31"
  ret double %".32"
entry.endif.endif.else:
  br label %"entry.endif.endif.endif"
entry.endif.endif.endif:
  %".35" = load i8, i8* %".7"
  %".36" = icmp eq i8 %".35", 47
  br i1 %".36", label %"entry.endif.endif.endif.if", label %"entry.endif.endif.endif.else"
entry.endif.endif.endif.if:
  %".38" = load double, double* %".5"
  %".39" = load double, double* %".9"
  %".40" = sdiv double %".38", %".39"
  ret double %".40"
entry.endif.endif.endif.else:
  br label %"entry.endif.endif.endif.endif"
entry.endif.endif.endif.endif:
  call void @"exit"(i32 -1)
}

define double @"evaluate"(i8* %".1") 
{
entry:
  %".3" = alloca i8*
  store i8* %".1", i8** %".3"
  %"opnd" = alloca [1024 x double]
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
  %".143" = load i32, i32* %"optr_p"
  %".144" = icmp sgt i32 %".143", 0
  %".145" = xor i1 %".144", -1
  br i1 %".145", label %"while_end.1", label %"while_begin"
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
  %".59" = load i8*, i8** %".3"
  %".60" = load i8, i8* %".59"
  %".61" = load i32, i32* %"optr_p"
  %".62" = getelementptr [1024 x i8], [1024 x i8]* %"optr", i32 0, i32 %".61"
  %".63" = load i8, i8* %".62"
  %".64" = call i32 @"operatorCmp"(i8 %".63", i8 %".60")
  store i32 %".64", i32* %"cmpResult"
  %".66" = load i32, i32* %"cmpResult"
  %".67" = icmp eq i32 %".66", -1
  br i1 %".67", label %"while_begin.else.if", label %"while_begin.else.else"
while_begin.endif:
  %".140" = load i32, i32* %"optr_p"
  %".141" = icmp sgt i32 %".140", 0
  br i1 %".141", label %"while_begin", label %"while_end.1"
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
  %".54" = getelementptr [1024 x double], [1024 x double]* %"opnd", i32 0, i32 %".53"
  %".55" = load i32, i32* %"number"
  %".56" = sitofp i32 %".55" to double
  store double %".56", double* %".54"
  br label %"while_begin.endif"
while_begin.else.if:
  %".69" = load i32, i32* %"optr_p"
  %".70" = add i32 %".69", 1
  store i32 %".70", i32* %"optr_p"
  %".72" = load i32, i32* %"optr_p"
  %".73" = getelementptr [1024 x i8], [1024 x i8]* %"optr", i32 0, i32 %".72"
  %".74" = load i8*, i8** %".3"
  %".75" = load i8, i8* %".74"
  store i8 %".75", i8* %".73"
  %".77" = load i8*, i8** %".3"
  %".78" = ptrtoint i8* %".77" to i64
  %".79" = sext i32 1 to i64
  %".80" = mul i64 1, %".79"
  %".81" = add i64 %".78", %".80"
  %".82" = inttoptr i64 %".81" to i8*
  store i8* %".82", i8** %".3"
  br label %"while_begin.else.endif"
while_begin.else.else:
  br label %"while_begin.else.endif"
while_begin.else.endif:
  %".86" = load i32, i32* %"cmpResult"
  %".87" = icmp eq i32 %".86", 0
  br i1 %".87", label %"while_begin.else.endif.if", label %"while_begin.else.endif.else"
while_begin.else.endif.if:
  %".89" = load i32, i32* %"optr_p"
  %".90" = sub i32 %".89", 1
  store i32 %".90", i32* %"optr_p"
  %".92" = load i8*, i8** %".3"
  %".93" = ptrtoint i8* %".92" to i64
  %".94" = sext i32 1 to i64
  %".95" = mul i64 1, %".94"
  %".96" = add i64 %".93", %".95"
  %".97" = inttoptr i64 %".96" to i8*
  store i8* %".97", i8** %".3"
  br label %"while_begin.else.endif.endif"
while_begin.else.endif.else:
  br label %"while_begin.else.endif.endif"
while_begin.else.endif.endif:
  %".101" = load i32, i32* %"cmpResult"
  %".102" = icmp eq i32 %".101", 1
  br i1 %".102", label %"while_begin.else.endif.endif.if", label %"while_begin.else.endif.endif.else"
while_begin.else.endif.endif.if:
  %"op_top" = alloca i8
  %".104" = load i32, i32* %"optr_p"
  %".105" = getelementptr [1024 x i8], [1024 x i8]* %"optr", i32 0, i32 %".104"
  %".106" = load i8, i8* %".105"
  store i8 %".106", i8* %"op_top"
  %".108" = load i32, i32* %"optr_p"
  %".109" = sub i32 %".108", 1
  store i32 %".109", i32* %"optr_p"
  %"number_2" = alloca double
  %".111" = load i32, i32* %"opnd_p"
  %".112" = getelementptr [1024 x double], [1024 x double]* %"opnd", i32 0, i32 %".111"
  %".113" = load double, double* %".112"
  store double %".113", double* %"number_2"
  %".115" = load i32, i32* %"opnd_p"
  %".116" = sub i32 %".115", 1
  store i32 %".116", i32* %"opnd_p"
  %"number_1" = alloca double
  %".118" = load i32, i32* %"opnd_p"
  %".119" = getelementptr [1024 x double], [1024 x double]* %"opnd", i32 0, i32 %".118"
  %".120" = load double, double* %".119"
  store double %".120", double* %"number_1"
  %".122" = load i32, i32* %"opnd_p"
  %".123" = sub i32 %".122", 1
  store i32 %".123", i32* %"opnd_p"
  %"cal_res" = alloca double
  %".125" = load double, double* %"number_2"
  %".126" = load i8, i8* %"op_top"
  %".127" = load double, double* %"number_1"
  %".128" = call double @"calculate"(double %".127", i8 %".126", double %".125")
  store double %".128", double* %"cal_res"
  %".130" = load i32, i32* %"opnd_p"
  %".131" = add i32 %".130", 1
  store i32 %".131", i32* %"opnd_p"
  %".133" = load i32, i32* %"opnd_p"
  %".134" = getelementptr [1024 x double], [1024 x double]* %"opnd", i32 0, i32 %".133"
  %".135" = load double, double* %"cal_res"
  store double %".135", double* %".134"
  br label %"while_begin.else.endif.endif.endif"
while_begin.else.endif.endif.else:
  br label %"while_begin.else.endif.endif.endif"
while_begin.else.endif.endif.endif:
  br label %"while_begin.endif"
while_end.1:
  %".147" = load i32, i32* %"opnd_p"
  %".148" = getelementptr [1024 x double], [1024 x double]* %"opnd", i32 0, i32 %".147"
  %".149" = load double, double* %".148"
  ret double %".149"
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
  %"res" = alloca double
  %".8" = load [1024 x i8], [1024 x i8]* %"str"
  %".9" = alloca [1024 x i8]
  store [1024 x i8] %".8", [1024 x i8]* %".9"
  %".11" = getelementptr [1024 x i8], [1024 x i8]* %".9", i32 0, i32 0
  %".12" = call double @"evaluate"(i8* %".11")
  store double %".12", double* %"res"
  %".14" = load double, double* %"res"
  %".15" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.1", i32 0, i32 0
  %".16" = call i32 (i8*, ...) @"printf"(i8* %".15", double %".14")
  ret i32 0
}

@"str" = constant [3 x i8] c"%s\00"
@"str.1" = constant [4 x i8] c"%d\0a\00"