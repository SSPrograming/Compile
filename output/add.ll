; ModuleID = ""
target triple = "x86_64-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...) 

declare i32 @"scanf"(i8* %".1", ...) 

declare i8* @"malloc"(i32 %".1") 

declare void @"free"(i8* %".1") 

declare void @"exit"(i32 %".1") 

declare i32 @"isdigit"(i32 %".1") 

define i32 @"main"() 
{
entry:
  %"a" = alloca i32
  %"b" = alloca i32
  %".2" = getelementptr inbounds [25 x i8], [25 x i8]* @"str", i32 0, i32 0
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2")
  %".4" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.1", i32 0, i32 0
  %".5" = call i32 (i8*, ...) @"scanf"(i8* %".4", i32* %"a", i32* %"b")
  %".6" = load i32, i32* %"a"
  %".7" = load i32, i32* %"b"
  %".8" = add i32 %".6", %".7"
  %".9" = load i32, i32* %"b"
  %".10" = load i32, i32* %"a"
  %".11" = getelementptr inbounds [44 x i8], [44 x i8]* @"str.2", i32 0, i32 0
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".11", i32 %".10", i32 %".9", i32 %".8")
  ret i32 0
}

@"str" = constant [25 x i8] c"\e8\af\b7\e8\be\93\e5\85\a5\e4\b8\a4\e4\b8\aa\e6\95\b0\e5\ad\97\ef\bc\9a\00"
@"str.1" = constant [6 x i8] c"%d %d\00"
@"str.2" = constant [44 x i8] c"\e6\82\a8\e8\be\93\e5\85\a5\e7\9a\84\e6\95\b0\e5\ad\97\e7\9a\84\e5\92\8c\e6\98\af\ef\bc\9a%d + %d = %d\0a\00"