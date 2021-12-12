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
  %".16" = fadd double %".14", %".15"
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
  %".24" = fsub double %".22", %".23"
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
  %".32" = fmul double %".30", %".31"
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
  %".40" = fdiv double %".38", %".39"
  ret double %".40"
entry.endif.endif.endif.else:
  br label %"entry.endif.endif.endif.endif"
entry.endif.endif.endif.endif:
  call void @"exit"(i32 -1)
  %".44" = sitofp i32 0 to double
  ret double %".44"
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
  %".145" = load i32, i32* %"opnd_p"
  %".146" = getelementptr [1024 x double], [1024 x double]* %"opnd", i32 0, i32 %".145"
  %".147" = load double, double* %".146"
  ret double %".147"
while_begin.if:
  %"number" = alloca i32
  store i32 0, i32* %"number"
  br label %"while_cond.1"
while_begin.else:
  %"cmpResult" = alloca i32
  %".61" = load i8*, i8** %".3"
  %".62" = load i8, i8* %".61"
  %".63" = load i32, i32* %"optr_p"
  %".64" = getelementptr [1024 x i8], [1024 x i8]* %"optr", i32 0, i32 %".63"
  %".65" = load i8, i8* %".64"
  %".66" = call i32 @"operatorCmp"(i8 %".65", i8 %".62")
  store i32 %".66", i32* %"cmpResult"
  %".68" = load i32, i32* %"cmpResult"
  %".69" = icmp eq i32 %".68", -1
  br i1 %".69", label %"while_begin.else.if", label %"while_begin.else.else"
while_begin.endif:
  %".142" = load i32, i32* %"optr_p"
  %".143" = icmp sgt i32 %".142", 0
  br i1 %".143", label %"while_begin", label %"while_end"
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
  %".56" = getelementptr [1024 x double], [1024 x double]* %"opnd", i32 0, i32 %".55"
  %".57" = load i32, i32* %"number"
  %".58" = sitofp i32 %".57" to double
  store double %".58", double* %".56"
  br label %"while_begin.endif"
while_begin.else.if:
  %".71" = load i32, i32* %"optr_p"
  %".72" = add i32 %".71", 1
  store i32 %".72", i32* %"optr_p"
  %".74" = load i32, i32* %"optr_p"
  %".75" = getelementptr [1024 x i8], [1024 x i8]* %"optr", i32 0, i32 %".74"
  %".76" = load i8*, i8** %".3"
  %".77" = load i8, i8* %".76"
  store i8 %".77", i8* %".75"
  %".79" = load i8*, i8** %".3"
  %".80" = ptrtoint i8* %".79" to i64
  %".81" = sext i32 1 to i64
  %".82" = mul i64 1, %".81"
  %".83" = add i64 %".80", %".82"
  %".84" = inttoptr i64 %".83" to i8*
  store i8* %".84", i8** %".3"
  br label %"while_begin.else.endif"
while_begin.else.else:
  br label %"while_begin.else.endif"
while_begin.else.endif:
  %".88" = load i32, i32* %"cmpResult"
  %".89" = icmp eq i32 %".88", 0
  br i1 %".89", label %"while_begin.else.endif.if", label %"while_begin.else.endif.else"
while_begin.else.endif.if:
  %".91" = load i32, i32* %"optr_p"
  %".92" = sub i32 %".91", 1
  store i32 %".92", i32* %"optr_p"
  %".94" = load i8*, i8** %".3"
  %".95" = ptrtoint i8* %".94" to i64
  %".96" = sext i32 1 to i64
  %".97" = mul i64 1, %".96"
  %".98" = add i64 %".95", %".97"
  %".99" = inttoptr i64 %".98" to i8*
  store i8* %".99", i8** %".3"
  br label %"while_begin.else.endif.endif"
while_begin.else.endif.else:
  br label %"while_begin.else.endif.endif"
while_begin.else.endif.endif:
  %".103" = load i32, i32* %"cmpResult"
  %".104" = icmp eq i32 %".103", 1
  br i1 %".104", label %"while_begin.else.endif.endif.if", label %"while_begin.else.endif.endif.else"
while_begin.else.endif.endif.if:
  %"op_top" = alloca i8
  %".106" = load i32, i32* %"optr_p"
  %".107" = getelementptr [1024 x i8], [1024 x i8]* %"optr", i32 0, i32 %".106"
  %".108" = load i8, i8* %".107"
  store i8 %".108", i8* %"op_top"
  %".110" = load i32, i32* %"optr_p"
  %".111" = sub i32 %".110", 1
  store i32 %".111", i32* %"optr_p"
  %"number_2" = alloca double
  %".113" = load i32, i32* %"opnd_p"
  %".114" = getelementptr [1024 x double], [1024 x double]* %"opnd", i32 0, i32 %".113"
  %".115" = load double, double* %".114"
  store double %".115", double* %"number_2"
  %".117" = load i32, i32* %"opnd_p"
  %".118" = sub i32 %".117", 1
  store i32 %".118", i32* %"opnd_p"
  %"number_1" = alloca double
  %".120" = load i32, i32* %"opnd_p"
  %".121" = getelementptr [1024 x double], [1024 x double]* %"opnd", i32 0, i32 %".120"
  %".122" = load double, double* %".121"
  store double %".122", double* %"number_1"
  %".124" = load i32, i32* %"opnd_p"
  %".125" = sub i32 %".124", 1
  store i32 %".125", i32* %"opnd_p"
  %"cal_res" = alloca double
  %".127" = load double, double* %"number_2"
  %".128" = load i8, i8* %"op_top"
  %".129" = load double, double* %"number_1"
  %".130" = call double @"calculate"(double %".129", i8 %".128", double %".127")
  store double %".130", double* %"cal_res"
  %".132" = load i32, i32* %"opnd_p"
  %".133" = add i32 %".132", 1
  store i32 %".133", i32* %"opnd_p"
  %".135" = load i32, i32* %"opnd_p"
  %".136" = getelementptr [1024 x double], [1024 x double]* %"opnd", i32 0, i32 %".135"
  %".137" = load double, double* %"cal_res"
  store double %".137", double* %".136"
  br label %"while_begin.else.endif.endif.endif"
while_begin.else.endif.endif.else:
  br label %"while_begin.else.endif.endif.endif"
while_begin.else.endif.endif.endif:
  br label %"while_begin.endif"
}

define i32 @"main"() 
{
entry:
  %".2" = getelementptr inbounds [6 x i8], [6 x i8]* @"string", i32 0, i32 0
  %".3" = call double @"evaluate"(i8* %".2")
  %".4" = getelementptr inbounds [29 x i8], [29 x i8]* @"string.1", i32 0, i32 0
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4", double %".3")
  %".6" = getelementptr inbounds [6 x i8], [6 x i8]* @"string.2", i32 0, i32 0
  %".7" = call double @"evaluate"(i8* %".6")
  %".8" = getelementptr inbounds [29 x i8], [29 x i8]* @"string.3", i32 0, i32 0
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8", double %".7")
  %".10" = getelementptr inbounds [6 x i8], [6 x i8]* @"string.4", i32 0, i32 0
  %".11" = call double @"evaluate"(i8* %".10")
  %".12" = getelementptr inbounds [29 x i8], [29 x i8]* @"string.5", i32 0, i32 0
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".12", double %".11")
  %".14" = getelementptr inbounds [6 x i8], [6 x i8]* @"string.6", i32 0, i32 0
  %".15" = call double @"evaluate"(i8* %".14")
  %".16" = getelementptr inbounds [29 x i8], [29 x i8]* @"string.7", i32 0, i32 0
  %".17" = call i32 (i8*, ...) @"printf"(i8* %".16", double %".15")
  %".18" = getelementptr inbounds [8 x i8], [8 x i8]* @"string.8", i32 0, i32 0
  %".19" = call double @"evaluate"(i8* %".18")
  %".20" = getelementptr inbounds [31 x i8], [31 x i8]* @"string.9", i32 0, i32 0
  %".21" = call i32 (i8*, ...) @"printf"(i8* %".20", double %".19")
  %"str" = alloca [1024 x i8]
  %".22" = getelementptr inbounds [22 x i8], [22 x i8]* @"string.10", i32 0, i32 0
  %".23" = call i32 (i8*, ...) @"printf"(i8* %".22")
  %"c" = alloca i8
  store i8 97, i8* %"c"
  %"i" = alloca i32
  store i32 0, i32* %"i"
  br label %"while_cond"
while_cond:
  %".27" = load i8, i8* %"c"
  %".28" = icmp ne i8 %".27", 10
  br i1 %".28", label %"while_begin", label %"while_end"
while_begin:
  %".30" = call i32 @"getchar"()
  %".31" = trunc i32 %".30" to i8
  store i8 %".31", i8* %"c"
  %".33" = load i32, i32* %"i"
  %".34" = getelementptr [1024 x i8], [1024 x i8]* %"str", i32 0, i32 %".33"
  %".35" = load i8, i8* %"c"
  store i8 %".35", i8* %".34"
  %".37" = load i32, i32* %"i"
  %".38" = add i32 %".37", 1
  store i32 %".38", i32* %"i"
  %".40" = load i8, i8* %"c"
  %".41" = icmp ne i8 %".40", 10
  br i1 %".41", label %"while_begin", label %"while_end"
while_end:
  %".43" = load i32, i32* %"i"
  %".44" = sub i32 %".43", 1
  %".45" = getelementptr [1024 x i8], [1024 x i8]* %"str", i32 0, i32 %".44"
  store i8 0, i8* %".45"
  %"str_pro" = alloca [1024 x i8]
  %"len" = alloca i32
  %".47" = load [1024 x i8], [1024 x i8]* %"str"
  %".48" = getelementptr [1024 x i8], [1024 x i8]* %"str", i32 0, i32 0
  %".49" = call i64 @"strlen"(i8* %".48")
  %".50" = trunc i64 %".49" to i32
  store i32 %".50", i32* %"len"
  store i32 0, i32* %"i"
  %"j" = alloca i32
  store i32 0, i32* %"j"
  br label %"while_cond.1"
while_cond.1:
  %".55" = load i32, i32* %"i"
  %".56" = load i32, i32* %"len"
  %".57" = icmp slt i32 %".55", %".56"
  br i1 %".57", label %"while_begin.1", label %"while_end.1"
while_begin.1:
  %".59" = load i32, i32* %"i"
  %".60" = getelementptr [1024 x i8], [1024 x i8]* %"str", i32 0, i32 %".59"
  %".61" = load i8, i8* %".60"
  %".62" = sext i8 %".61" to i32
  %".63" = call i32 @"isspace"(i32 %".62")
  %".64" = icmp ne i32 %".63", 0
  br i1 %".64", label %"while_begin.1.if", label %"while_begin.1.else"
while_end.1:
  %".87" = load i32, i32* %"j"
  %".88" = getelementptr [1024 x i8], [1024 x i8]* %"str_pro", i32 0, i32 %".87"
  store i8 0, i8* %".88"
  %"res" = alloca double
  %".90" = load [1024 x i8], [1024 x i8]* %"str_pro"
  %".91" = getelementptr [1024 x i8], [1024 x i8]* %"str_pro", i32 0, i32 0
  %".92" = call double @"evaluate"(i8* %".91")
  store double %".92", double* %"res"
  %".94" = load double, double* %"res"
  %".95" = load [1024 x i8], [1024 x i8]* %"str_pro"
  %".96" = getelementptr inbounds [36 x i8], [36 x i8]* @"string.11", i32 0, i32 0
  %".97" = getelementptr [1024 x i8], [1024 x i8]* %"str_pro", i32 0, i32 0
  %".98" = call i32 (i8*, ...) @"printf"(i8* %".96", i8* %".97", double %".94")
  ret i32 0
while_begin.1.if:
  %".66" = load i32, i32* %"i"
  %".67" = add i32 %".66", 1
  store i32 %".67", i32* %"i"
  br label %"while_begin.1.endif"
while_begin.1.else:
  %".70" = load i32, i32* %"j"
  %".71" = getelementptr [1024 x i8], [1024 x i8]* %"str_pro", i32 0, i32 %".70"
  %".72" = load i32, i32* %"i"
  %".73" = getelementptr [1024 x i8], [1024 x i8]* %"str", i32 0, i32 %".72"
  %".74" = load i8, i8* %".73"
  store i8 %".74", i8* %".71"
  %".76" = load i32, i32* %"i"
  %".77" = add i32 %".76", 1
  store i32 %".77", i32* %"i"
  %".79" = load i32, i32* %"j"
  %".80" = add i32 %".79", 1
  store i32 %".80", i32* %"j"
  br label %"while_begin.1.endif"
while_begin.1.endif:
  %".83" = load i32, i32* %"i"
  %".84" = load i32, i32* %"len"
  %".85" = icmp slt i32 %".83", %".84"
  br i1 %".85", label %"while_begin.1", label %"while_end.1"
}

@"string" = constant [6 x i8] c"1+2+3\00"
@"string.1" = constant [29 x i8] c"\e8\a1\a8\e8\be\be\e5\bc\8f1\ef\bc\9a1 + 2 + 3 = %f\0a\00"
@"string.2" = constant [6 x i8] c"1*2+3\00"
@"string.3" = constant [29 x i8] c"\e8\a1\a8\e8\be\be\e5\bc\8f2\ef\bc\9a1 * 2 + 3 = %f\0a\00"
@"string.4" = constant [6 x i8] c"1+2-3\00"
@"string.5" = constant [29 x i8] c"\e8\a1\a8\e8\be\be\e5\bc\8f3\ef\bc\9a1 + 2 - 3 = %f\0a\00"
@"string.6" = constant [6 x i8] c"1-2/3\00"
@"string.7" = constant [29 x i8] c"\e8\a1\a8\e8\be\be\e5\bc\8f4\ef\bc\9a1 - 2 / 3 = %f\0a\00"
@"string.8" = constant [8 x i8] c"1*(2+3)\00"
@"string.9" = constant [31 x i8] c"\e8\a1\a8\e8\be\be\e5\bc\8f5\ef\bc\9a1 * (2 + 3) = %f\0a\00"
@"string.10" = constant [22 x i8] c"\e8\af\b7\e8\be\93\e5\85\a5\e8\a1\a8\e8\be\be\e5\bc\8f\ef\bc\9a\00"
@"string.11" = constant [36 x i8] c"\e8\a1\a8\e8\be\be\e5\bc\8f\e8\ae\a1\e7\ae\97\e7\bb\93\e6\9e\9c\e4\b8\ba\ef\bc\9a%s = %f\0a\00"