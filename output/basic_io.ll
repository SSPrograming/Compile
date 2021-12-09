; ModuleID = ""
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...) 

declare i32 @"scanf"(i8* %".1", ...) 

define i32 @"main"() 
{
entry:
  %"n" = alloca i32
  %".2" = getelementptr inbounds [4 x i8], [4 x i8]* @"str", i32 0
  %".3" = bitcast [4 x i8]* %".2" to i8*
  %".4" = call i32 (i8*, ...) @"scanf"(i8* %".3", i32* %"n")
  %".5" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.1", i32 0
  %".6" = bitcast [6 x i8]* %".5" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", i32* %"n")
  ret i32 0
}

@"str" = constant [4 x i8] c"\22%d\22"
@"str.1" = constant [6 x i8] c"\22%d\5cn\22"