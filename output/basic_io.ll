; ModuleID = ""
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

@"str" = constant [3 x i8] c"%d\00"
@"str.1" = constant [4 x i8] c"%d\0a\00"
declare i32 @"printf"(i8* %".1", ...) 

declare i32 @"scanf"(i8* %".1", ...) 

define i32 @"main"() 
{
entry:
  %"n" = alloca i32
  %".2" = getelementptr inbounds [3 x i8], [3 x i8]* @"str", i32 0
  %".3" = bitcast [3 x i8]* %".2" to i8*
  %".4" = call i32 (i8*, ...) @"scanf"(i8* %".3", i32* %"n")
  %".5" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.1", i32 0
  %".6" = bitcast [4 x i8]* %".5" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", i32* %"n")
  ret i32 0
}
