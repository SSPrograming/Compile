; ModuleID = ""
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...) 

declare i32 @"scanf"(i8* %".1", ...) 

define i32 @"main"() 
{
entry:
  %"a" = alloca i32
  %"b" = alloca i32
  %".2" = getelementptr inbounds [25 x i8], [25 x i8]* @"str", i32 0
  %".3" = bitcast [25 x i8]* %".2" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3")
  %".5" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.1", i32 0
  %".6" = bitcast [6 x i8]* %".5" to i8*
  %".7" = call i32 (i8*, ...) @"scanf"(i8* %".6", i32* %"a", i32* %"b")
  %".8" = load i32, i32* %"a"
  %".9" = load i32, i32* %"b"
  %".10" = add i32 %".8", %".9"
  %".11" = load i32, i32* %"b"
  %".12" = load i32, i32* %"a"
  %".13" = getelementptr inbounds [44 x i8], [44 x i8]* @"str.2", i32 0
  %".14" = bitcast [44 x i8]* %".13" to i8*
  %".15" = call i32 (i8*, ...) @"printf"(i8* %".14", i32 %".12", i32 %".11", i32 %".10")
  ret i32 0
}

@"str" = constant [25 x i8] c"\e8\af\b7\e8\be\93\e5\85\a5\e4\b8\a4\e4\b8\aa\e6\95\b0\e5\ad\97\ef\bc\9a\00"
@"str.1" = constant [6 x i8] c"%d %d\00"
@"str.2" = constant [44 x i8] c"\e6\82\a8\e8\be\93\e5\85\a5\e7\9a\84\e6\95\b0\e5\ad\97\e7\9a\84\e5\92\8c\e6\98\af\ef\bc\9a%d + %d = %d\0a\00"