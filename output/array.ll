; ModuleID = ""
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...) 

declare i32 @"scanf"(i8* %".1", ...) 

declare i8* @"malloc"(i32 %".1") 

declare void @"free"(i8* %".1") 

define i32 @"main"() 
{
entry:
  %"n" = alloca i32
  store i32 2, i32* %"n"
  %"a" = alloca [2 x i32]
  %".3" = getelementptr [2 x i32], [2 x i32]* %"a", i32 0
  %".4" = bitcast [2 x i32]* %".3" to i32*
  store i32 0, i32* %".4"
  %".6" = getelementptr [2 x i32], [2 x i32]* %"a", i32 1
  %".7" = bitcast [2 x i32]* %".6" to i32*
  store i32 10, i32* %".7"
  %".9" = getelementptr [2 x i32], [2 x i32]* %"a", i32 0
  %".10" = load [2 x i32], [2 x i32]* %".9"
  %".11" = getelementptr inbounds [11 x i8], [11 x i8]* @"str", i32 0
  %".12" = bitcast [11 x i8]* %".11" to i8*
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".12", [2 x i32] %".10")
  %".14" = getelementptr [2 x i32], [2 x i32]* %"a", i32 1
  %".15" = load [2 x i32], [2 x i32]* %".14"
  %".16" = getelementptr inbounds [11 x i8], [11 x i8]* @"str.1", i32 0
  %".17" = bitcast [11 x i8]* %".16" to i8*
  %".18" = call i32 (i8*, ...) @"printf"(i8* %".17", [2 x i32] %".15")
  ret i32 0
}

@"str" = constant [11 x i8] c"a[0] = %d\0a\00"
@"str.1" = constant [11 x i8] c"a[1] = %d\0a\00"