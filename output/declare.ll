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

define void @"test"() 
{
entry:
  %".2" = getelementptr inbounds [6 x i8], [6 x i8]* @"string", i32 0, i32 0
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2")
  ret void
}

define i32 @"main"() 
{
entry:
  call void @"test"()
  ret i32 0
}

@"string" = constant [6 x i8] c"test\0a\00"