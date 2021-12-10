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
  store i32 3, i32* %"n"
  %"a" = alloca [3 x i32]
  %".3" = getelementptr [3 x i32], [3 x i32]* %"a", i32 0, i32 0
  store i32 0, i32* %".3"
  %".5" = getelementptr [3 x i32], [3 x i32]* %"a", i32 0, i32 1
  %".6" = add i32 10, 2
  %".7" = sub i32 0, %".6"
  store i32 %".7", i32* %".5"
  %".9" = getelementptr [3 x i32], [3 x i32]* %"a", i32 0, i32 2
  %".10" = getelementptr [3 x i32], [3 x i32]* %"a", i32 0, i32 1
  %".11" = load i32, i32* %".10"
  store i32 %".11", i32* %".9"
  %".13" = getelementptr [3 x i32], [3 x i32]* %"a", i32 0, i32 0
  %".14" = load i32, i32* %".13"
  %".15" = getelementptr inbounds [11 x i8], [11 x i8]* @"str", i32 0, i32 0
  %".16" = call i32 (i8*, ...) @"printf"(i8* %".15", i32 %".14")
  %".17" = getelementptr [3 x i32], [3 x i32]* %"a", i32 0, i32 1
  %".18" = load i32, i32* %".17"
  %".19" = getelementptr inbounds [11 x i8], [11 x i8]* @"str.1", i32 0, i32 0
  %".20" = call i32 (i8*, ...) @"printf"(i8* %".19", i32 %".18")
  %".21" = getelementptr [3 x i32], [3 x i32]* %"a", i32 0, i32 2
  %".22" = load i32, i32* %".21"
  %".23" = getelementptr inbounds [11 x i8], [11 x i8]* @"str.2", i32 0, i32 0
  %".24" = call i32 (i8*, ...) @"printf"(i8* %".23", i32 %".22")
  %".25" = load i32, i32* %"n"
  %".26" = icmp sgt i32 %".25", 0
  %".27" = xor i1 %".26", -1
  br i1 %".27", label %"while_end", label %"while_begin"
while_begin:
  %".29" = load i32, i32* %"n"
  %".30" = getelementptr inbounds [17 x i8], [17 x i8]* @"str.3", i32 0, i32 0
  %".31" = call i32 (i8*, ...) @"printf"(i8* %".30", i32 %".29")
  %".32" = load i32, i32* %"n"
  %".33" = sub i32 %".32", 1
  store i32 %".33", i32* %"n"
  %".35" = load i32, i32* %"n"
  %".36" = icmp sgt i32 %".35", 0
  br i1 %".36", label %"while_begin", label %"while_end"
while_end:
  ret i32 0
}

@"str" = constant [11 x i8] c"a[0] = %d\0a\00"
@"str.1" = constant [11 x i8] c"a[1] = %d\0a\00"
@"str.2" = constant [11 x i8] c"a[2] = %d\0a\00"
@"str.3" = constant [17 x i8] c"while (n = %d) \0a\00"