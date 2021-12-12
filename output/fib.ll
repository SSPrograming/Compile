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

define i32 @"fib"(i32 %".1") 
{
entry:
  %".3" = alloca i32
  store i32 %".1", i32* %".3"
  %".5" = load i32, i32* %".3"
  %".6" = icmp eq i32 %".5", 0
  br i1 %".6", label %"entry.if", label %"entry.else"
entry.if:
  ret i32 0
entry.else:
  %".9" = load i32, i32* %".3"
  %".10" = icmp eq i32 %".9", 1
  br i1 %".10", label %"entry.else.if", label %"entry.else.else"
entry.endif:
  %".15" = load i32, i32* %".3"
  %".16" = sub i32 %".15", 1
  %".17" = call i32 @"fib"(i32 %".16")
  %".18" = load i32, i32* %".3"
  %".19" = sub i32 %".18", 2
  %".20" = call i32 @"fib"(i32 %".19")
  %".21" = add i32 %".17", %".20"
  ret i32 %".21"
entry.else.if:
  ret i32 1
entry.else.else:
  br label %"entry.else.endif"
entry.else.endif:
  br label %"entry.endif"
}

define i32 @"main"() 
{
entry:
  %".2" = call i32 @"fib"(i32 10)
  %".3" = getelementptr inbounds [14 x i8], [14 x i8]* @"string", i32 0, i32 0
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i32 %".2")
  ret i32 0
}

@"string" = constant [14 x i8] c"fib(10) = %d\0a\00"