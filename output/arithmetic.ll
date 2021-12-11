; ModuleID = ""
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...) 

declare i32 @"scanf"(i8* %".1", ...) 

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
  %".9" = getelementptr inbounds [14 x i8], [14 x i8]* @"str", i32 0
  %".10" = bitcast [14 x i8]* %".9" to i8*
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".10", i32 %".8", i32 %".7", i32 %".6")
  store i32 4, i32* %"a"
  store i32 2, i32* %"b"
  %".14" = load i32, i32* %"a"
  %".15" = load i32, i32* %"b"
  %".16" = sub i32 %".14", %".15"
  %".17" = load i32, i32* %"b"
  %".18" = load i32, i32* %"a"
  %".19" = getelementptr inbounds [14 x i8], [14 x i8]* @"str.1", i32 0
  %".20" = bitcast [14 x i8]* %".19" to i8*
  %".21" = call i32 (i8*, ...) @"printf"(i8* %".20", i32 %".18", i32 %".17", i32 %".16")
  store i32 3, i32* %"a"
  store i32 4, i32* %"b"
  %".24" = load i32, i32* %"a"
  %".25" = load i32, i32* %"b"
  %".26" = mul i32 %".24", %".25"
  %".27" = load i32, i32* %"b"
  %".28" = load i32, i32* %"a"
  %".29" = getelementptr inbounds [14 x i8], [14 x i8]* @"str.2", i32 0
  %".30" = bitcast [14 x i8]* %".29" to i8*
  %".31" = call i32 (i8*, ...) @"printf"(i8* %".30", i32 %".28", i32 %".27", i32 %".26")
  store i32 10000, i32* %"a"
  store i32 5000, i32* %"b"
  %".34" = load i32, i32* %"a"
  %".35" = load i32, i32* %"b"
  %".36" = sdiv i32 %".34", %".35"
  %".37" = load i32, i32* %"b"
  %".38" = load i32, i32* %"a"
  %".39" = getelementptr inbounds [14 x i8], [14 x i8]* @"str.3", i32 0
  %".40" = bitcast [14 x i8]* %".39" to i8*
  %".41" = call i32 (i8*, ...) @"printf"(i8* %".40", i32 %".38", i32 %".37", i32 %".36")
  ret i32 0
}

@"str" = constant [14 x i8] c"%d + %d = %d\0a\00"
@"str.1" = constant [14 x i8] c"%d - %d = %d\0a\00"
@"str.2" = constant [14 x i8] c"%d * %d = %d\0a\00"
@"str.3" = constant [14 x i8] c"%d / %d = %d\0a\00"