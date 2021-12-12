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
  store i32 1, i32* %"a"
  %"b" = alloca i32
  store i32 2, i32* %"b"
  %".4" = load i32, i32* %"a"
  %".5" = load i32, i32* %"b"
  %".6" = add i32 %".4", %".5"
  %".7" = load i32, i32* %"b"
  %".8" = load i32, i32* %"a"
  %".9" = getelementptr inbounds [14 x i8], [14 x i8]* @"string", i32 0, i32 0
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", i32 %".8", i32 %".7", i32 %".6")
  ret i32 0
}

@"string" = constant [14 x i8] c"%d + %d = %d\0a\00"