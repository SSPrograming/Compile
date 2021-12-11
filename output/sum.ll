; ModuleID = ""
target triple = "x86_64-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...) 

declare i32 @"scanf"(i8* %".1", ...) 

declare i8* @"malloc"(i32 %".1") 

declare void @"free"(i8* %".1") 

declare void @"exit"(i32 %".1") 

declare i32 @"isdigit"(i32 %".1") 

define i32 @"sum"(i32* %".1", i32 %".2") 
{
entry:
  %".4" = alloca i32*
  store i32* %".1", i32** %".4"
  %".6" = alloca i32
  store i32 %".2", i32* %".6"
  %"_sum" = alloca i32
  store i32 0, i32* %"_sum"
  %".9" = load i32, i32* %".6"
  %".10" = sub i32 %".9", 1
  store i32 %".10", i32* %".6"
  br label %"while_cond"
while_cond:
  %".13" = load i32, i32* %".6"
  %".14" = icmp sge i32 %".13", 0
  br i1 %".14", label %"while_begin", label %"while_end"
while_begin:
  %".16" = load i32, i32* %"_sum"
  %".17" = load i32, i32* %".6"
  %".18" = load i32*, i32** %".4"
  %".19" = getelementptr i32, i32* %".18", i32 %".17"
  %".20" = load i32, i32* %".19"
  %".21" = add i32 %".16", %".20"
  store i32 %".21", i32* %"_sum"
  %".23" = load i32, i32* %".6"
  %".24" = sub i32 %".23", 1
  store i32 %".24", i32* %".6"
  %".26" = load i32, i32* %".6"
  %".27" = icmp sge i32 %".26", 0
  br i1 %".27", label %"while_begin", label %"while_end"
while_end:
  %".29" = load i32, i32* %"_sum"
  ret i32 %".29"
}

define i32 @"main"() 
{
entry:
  %"a" = alloca [3 x i32]
  %".2" = getelementptr [3 x i32], [3 x i32]* %"a", i32 0, i32 0
  store i32 0, i32* %".2"
  %".4" = getelementptr [3 x i32], [3 x i32]* %"a", i32 0, i32 1
  store i32 1, i32* %".4"
  %".6" = getelementptr [3 x i32], [3 x i32]* %"a", i32 0, i32 2
  store i32 2, i32* %".6"
  %".8" = load [3 x i32], [3 x i32]* %"a"
  %".9" = getelementptr [3 x i32], [3 x i32]* %"a", i32 0, i32 0
  %".10" = call i32 @"sum"(i32* %".9", i32 3)
  %".11" = getelementptr inbounds [19 x i8], [19 x i8]* @"str", i32 0, i32 0
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".11", i32 %".10")
  ret i32 0
}

@"str" = constant [19 x i8] c"sum(0, 1, 2) = %d\0a\00"