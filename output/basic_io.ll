; ModuleID = ""
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...) 

declare i32 @"scanf"(i8* %".1", ...) 

define i32 @"main"() 
{
entry:
  %"n" = alloca i32
  %".2" = getelementptr inbounds [3 x i8], [3 x i8]* @"str", i32 0
  %".3" = bitcast [3 x i8]* %".2" to i8*
  %".4" = call i32 (i8*, ...) @"scanf"(i8* %".3", i32* %"n")
  %".5" = load i32, i32* %"n"
  %".6" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.1", i32 0
  %".7" = bitcast [4 x i8]* %".6" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i32 %".5")
  ret i32 0
}

@"str" = constant [3 x i8] c"%d\00"
@"str.1" = constant [4 x i8] c"%d\0a\00"