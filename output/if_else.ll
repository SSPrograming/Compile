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

define i32 @"main"() 
{
entry:
  %"a" = alloca i32
  store i32 20, i32* %"a"
  %".3" = getelementptr inbounds [5 x i8], [5 x i8]* @"string", i32 0, i32 0
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3")
  %".5" = load i32, i32* %"a"
  %".6" = icmp sgt i32 %".5", 10
  br i1 %".6", label %"entry.if", label %"entry.else"
entry.if:
  %".8" = load i32, i32* %"a"
  %".9" = getelementptr inbounds [9 x i8], [9 x i8]* @"string.1", i32 0, i32 0
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", i32 %".8")
  br label %"entry.endif"
entry.else:
  %".12" = load i32, i32* %"a"
  %".13" = icmp sle i32 %".12", 10
  %".14" = load i32, i32* %"a"
  %".15" = icmp sgt i32 %".14", 5
  %".16" = and i1 %".13", %".15"
  br i1 %".16", label %"entry.else.if", label %"entry.else.else"
entry.endif:
  ret i32 0
entry.else.if:
  %".18" = load i32, i32* %"a"
  %".19" = getelementptr inbounds [8 x i8], [8 x i8]* @"string.2", i32 0, i32 0
  %".20" = call i32 (i8*, ...) @"printf"(i8* %".19", i32 %".18")
  br label %"entry.else.endif"
entry.else.else:
  %".22" = load i32, i32* %"a"
  %".23" = icmp sgt i32 %".22", 1
  br i1 %".23", label %"entry.else.else.if", label %"entry.else.else.else"
entry.else.endif:
  br label %"entry.endif"
entry.else.else.if:
  %".25" = load i32, i32* %"a"
  %".26" = getelementptr inbounds [8 x i8], [8 x i8]* @"string.3", i32 0, i32 0
  %".27" = call i32 (i8*, ...) @"printf"(i8* %".26", i32 %".25")
  br label %"entry.else.else.endif"
entry.else.else.else:
  %".29" = load i32, i32* %"a"
  %".30" = icmp eq i32 %".29", 1
  br i1 %".30", label %"entry.else.else.else.if", label %"entry.else.else.else.else"
entry.else.else.endif:
  br label %"entry.else.endif"
entry.else.else.else.if:
  %".32" = load i32, i32* %"a"
  %".33" = getelementptr inbounds [8 x i8], [8 x i8]* @"string.4", i32 0, i32 0
  %".34" = call i32 (i8*, ...) @"printf"(i8* %".33", i32 %".32")
  br label %"entry.else.else.else.endif"
entry.else.else.else.else:
  %".36" = load i32, i32* %"a"
  %".37" = icmp sle i32 %".36", -1
  br i1 %".37", label %"entry.else.else.else.else.if", label %"entry.else.else.else.else.else"
entry.else.else.else.endif:
  br label %"entry.else.else.endif"
entry.else.else.else.else.if:
  %".39" = load i32, i32* %"a"
  %".40" = getelementptr inbounds [10 x i8], [10 x i8]* @"string.5", i32 0, i32 0
  %".41" = call i32 (i8*, ...) @"printf"(i8* %".40", i32 %".39")
  br label %"entry.else.else.else.else.endif"
entry.else.else.else.else.else:
  %".43" = load i32, i32* %"a"
  %".44" = getelementptr inbounds [8 x i8], [8 x i8]* @"string.6", i32 0, i32 0
  %".45" = call i32 (i8*, ...) @"printf"(i8* %".44", i32 %".43")
  br label %"entry.else.else.else.else.endif"
entry.else.else.else.else.endif:
  br label %"entry.else.else.else.endif"
}

@"string" = constant [5 x i8] c"a = \00"
@"string.1" = constant [9 x i8] c"%d > 10\0a\00"
@"string.2" = constant [8 x i8] c"%d > 5\0a\00"
@"string.3" = constant [8 x i8] c"%d > 1\0a\00"
@"string.4" = constant [8 x i8] c"%d > 0\0a\00"
@"string.5" = constant [10 x i8] c"%d <= -1\0a\00"
@"string.6" = constant [8 x i8] c"%d = 0\0a\00"