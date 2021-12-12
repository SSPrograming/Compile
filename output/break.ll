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
  %"n" = alloca i32
  store i32 0, i32* %"n"
  br label %"while_cond"
while_cond:
  %".4" = icmp ne i32 1, 0
  br i1 %".4", label %"while_begin", label %"while_end"
while_begin:
  %".6" = load i32, i32* %"n"
  %".7" = icmp sgt i32 %".6", 5
  br i1 %".7", label %"while_begin.if", label %"while_begin.else"
while_end:
  ret i32 0
while_begin.if:
  br label %"while_end"
while_begin.else:
  %".10" = load i32, i32* %"n"
  %".11" = getelementptr inbounds [4 x i8], [4 x i8]* @"string", i32 0, i32 0
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".11", i32 %".10")
  %".13" = load i32, i32* %"n"
  %".14" = add i32 %".13", 1
  store i32 %".14", i32* %"n"
  br label %"while_begin"
while_begin.endif:
  %".17" = icmp ne i32 1, 0
  br i1 %".17", label %"while_begin", label %"while_end"
}

@"string" = constant [4 x i8] c"%d\0a\00"