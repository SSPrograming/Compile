; ModuleID = ""
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...) 

declare i32 @"scanf"(i8* %".1", ...) 

declare i8* @"malloc"(i32 %".1") 

declare void @"free"(i8* %".1") 

define i32 @"main"() 
{
entry:
  %"a" = alloca i32
  %".2" = getelementptr inbounds [20 x i8], [20 x i8]* @"str", i32 0
  %".3" = bitcast [20 x i8]* %".2" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3")
  %".5" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.1", i32 0
  %".6" = bitcast [3 x i8]* %".5" to i8*
  %".7" = call i32 (i8*, ...) @"scanf"(i8* %".6", i32* %"a")
  %".8" = load i32, i32* %"a"
  %".9" = icmp sgt i32 %".8", 10
  br i1 %".9", label %"entry.if", label %"entry.else"
entry.if:
  %".11" = load i32, i32* %"a"
  %".12" = getelementptr inbounds [9 x i8], [9 x i8]* @"str.2", i32 0
  %".13" = bitcast [9 x i8]* %".12" to i8*
  %".14" = call i32 (i8*, ...) @"printf"(i8* %".13", i32 %".11")
  br label %"entry.endif"
entry.else:
  %".16" = load i32, i32* %"a"
  %".17" = icmp sle i32 %".16", 10
  %".18" = load i32, i32* %"a"
  %".19" = icmp sgt i32 %".18", 5
  %".20" = and i1 %".17", %".19"
  br i1 %".20", label %"entry.else.if", label %"entry.else.else"
entry.endif:
  ret i32 0
entry.else.if:
  %".22" = load i32, i32* %"a"
  %".23" = getelementptr inbounds [8 x i8], [8 x i8]* @"str.3", i32 0
  %".24" = bitcast [8 x i8]* %".23" to i8*
  %".25" = call i32 (i8*, ...) @"printf"(i8* %".24", i32 %".22")
  br label %"entry.else.endif"
entry.else.else:
  %".27" = load i32, i32* %"a"
  %".28" = icmp sgt i32 %".27", 1
  br i1 %".28", label %"entry.else.else.if", label %"entry.else.else.else"
entry.else.endif:
  br label %"entry.endif"
entry.else.else.if:
  %".30" = load i32, i32* %"a"
  %".31" = getelementptr inbounds [8 x i8], [8 x i8]* @"str.4", i32 0
  %".32" = bitcast [8 x i8]* %".31" to i8*
  %".33" = call i32 (i8*, ...) @"printf"(i8* %".32", i32 %".30")
  br label %"entry.else.else.endif"
entry.else.else.else:
  %".35" = load i32, i32* %"a"
  %".36" = icmp eq i32 %".35", 1
  br i1 %".36", label %"entry.else.else.else.if", label %"entry.else.else.else.else"
entry.else.else.endif:
  br label %"entry.else.endif"
entry.else.else.else.if:
  %".38" = load i32, i32* %"a"
  %".39" = getelementptr inbounds [8 x i8], [8 x i8]* @"str.5", i32 0
  %".40" = bitcast [8 x i8]* %".39" to i8*
  %".41" = call i32 (i8*, ...) @"printf"(i8* %".40", i32 %".38")
  br label %"entry.else.else.else.endif"
entry.else.else.else.else:
  %".43" = load i32, i32* %"a"
  %".44" = icmp sle i32 %".43", -1
  br i1 %".44", label %"entry.else.else.else.else.if", label %"entry.else.else.else.else.else"
entry.else.else.else.endif:
  br label %"entry.else.else.endif"
entry.else.else.else.else.if:
  %".46" = load i32, i32* %"a"
  %".47" = getelementptr inbounds [10 x i8], [10 x i8]* @"str.6", i32 0
  %".48" = bitcast [10 x i8]* %".47" to i8*
  %".49" = call i32 (i8*, ...) @"printf"(i8* %".48", i32 %".46")
  br label %"entry.else.else.else.else.endif"
entry.else.else.else.else.else:
  %".51" = load i32, i32* %"a"
  %".52" = getelementptr inbounds [8 x i8], [8 x i8]* @"str.7", i32 0
  %".53" = bitcast [8 x i8]* %".52" to i8*
  %".54" = call i32 (i8*, ...) @"printf"(i8* %".53", i32 %".51")
  br label %"entry.else.else.else.else.endif"
entry.else.else.else.else.endif:
  br label %"entry.else.else.else.endif"
}

@"str" = constant [20 x i8] c"\e8\af\b7\e8\be\93\e5\85\a5\e6\95\b0\e5\ad\97a = \00"
@"str.1" = constant [3 x i8] c"%d\00"
@"str.2" = constant [9 x i8] c"%d > 10\0a\00"
@"str.3" = constant [8 x i8] c"%d > 5\0a\00"
@"str.4" = constant [8 x i8] c"%d > 1\0a\00"
@"str.5" = constant [8 x i8] c"%d > 0\0a\00"
@"str.6" = constant [10 x i8] c"%d <= -1\0a\00"
@"str.7" = constant [8 x i8] c"%d = 0\0a\00"