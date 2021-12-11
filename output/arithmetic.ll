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
  store i32 4, i32* %"a"
  store i32 2, i32* %"b"
  %".13" = load i32, i32* %"a"
  %".14" = load i32, i32* %"b"
  %".15" = sub i32 %".13", %".14"
  %".16" = load i32, i32* %"b"
  %".17" = load i32, i32* %"a"
  %".18" = getelementptr inbounds [14 x i8], [14 x i8]* @"string.1", i32 0, i32 0
  %".19" = call i32 (i8*, ...) @"printf"(i8* %".18", i32 %".17", i32 %".16", i32 %".15")
  store i32 3, i32* %"a"
  store i32 4, i32* %"b"
  %".22" = load i32, i32* %"a"
  %".23" = load i32, i32* %"b"
  %".24" = mul i32 %".22", %".23"
  %".25" = load i32, i32* %"b"
  %".26" = load i32, i32* %"a"
  %".27" = getelementptr inbounds [14 x i8], [14 x i8]* @"string.2", i32 0, i32 0
  %".28" = call i32 (i8*, ...) @"printf"(i8* %".27", i32 %".26", i32 %".25", i32 %".24")
  store i32 10000, i32* %"a"
  store i32 5000, i32* %"b"
  %".31" = load i32, i32* %"a"
  %".32" = load i32, i32* %"b"
  %".33" = sdiv i32 %".31", %".32"
  %".34" = load i32, i32* %"b"
  %".35" = load i32, i32* %"a"
  %".36" = getelementptr inbounds [14 x i8], [14 x i8]* @"string.3", i32 0, i32 0
  %".37" = call i32 (i8*, ...) @"printf"(i8* %".36", i32 %".35", i32 %".34", i32 %".33")
  ret i32 0
}

@"string" = constant [14 x i8] c"%d + %d = %d\0a\00"
@"string.1" = constant [14 x i8] c"%d - %d = %d\0a\00"
@"string.2" = constant [14 x i8] c"%d * %d = %d\0a\00"
@"string.3" = constant [14 x i8] c"%d / %d = %d\0a\00"