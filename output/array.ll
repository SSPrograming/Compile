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
  %"n" = alloca i32
  %"a" = alloca [3 x i32]
  %".2" = getelementptr [3 x i32], [3 x i32]* %"a", i32 0, i32 0
  store i32 0, i32* %".2"
  %".4" = getelementptr [3 x i32], [3 x i32]* %"a", i32 0, i32 1
  %".5" = add i32 10, 2
  %".6" = sub i32 0, %".5"
  store i32 %".6", i32* %".4"
  %".8" = getelementptr [3 x i32], [3 x i32]* %"a", i32 0, i32 2
  %".9" = getelementptr [3 x i32], [3 x i32]* %"a", i32 0, i32 1
  %".10" = load i32, i32* %".9"
  store i32 %".10", i32* %".8"
  %".12" = getelementptr [3 x i32], [3 x i32]* %"a", i32 0, i32 0
  %".13" = load i32, i32* %".12"
  %".14" = getelementptr inbounds [11 x i8], [11 x i8]* @"str", i32 0, i32 0
  %".15" = call i32 (i8*, ...) @"printf"(i8* %".14", i32 %".13")
  %".16" = getelementptr [3 x i32], [3 x i32]* %"a", i32 0, i32 1
  %".17" = load i32, i32* %".16"
  %".18" = getelementptr inbounds [11 x i8], [11 x i8]* @"str.1", i32 0, i32 0
  %".19" = call i32 (i8*, ...) @"printf"(i8* %".18", i32 %".17")
  %".20" = getelementptr [3 x i32], [3 x i32]* %"a", i32 0, i32 2
  %".21" = load i32, i32* %".20"
  %".22" = getelementptr inbounds [11 x i8], [11 x i8]* @"str.2", i32 0, i32 0
  %".23" = call i32 (i8*, ...) @"printf"(i8* %".22", i32 %".21")
  store i32 5, i32* %"n"
  %"b" = alloca i32*
  %".25" = load i32, i32* %"n"
  %".26" = call i8* @"malloc"(i32 %".25")
  %".27" = bitcast i8* %".26" to i32*
  store i32* %".27", i32** %"b"
  %".29" = load i32*, i32** %"b"
  %".30" = getelementptr i32, i32* %".29", i32 0
  store i32 0, i32* %".30"
  %".32" = load i32*, i32** %"b"
  %".33" = getelementptr i32, i32* %".32", i32 1
  store i32 4, i32* %".33"
  %".35" = load i32*, i32** %"b"
  %".36" = getelementptr i32, i32* %".35", i32 2
  store i32 2, i32* %".36"
  %".38" = load i32*, i32** %"b"
  %".39" = getelementptr i32, i32* %".38", i32 4
  store i32 4, i32* %".39"
  %".41" = load i32*, i32** %"b"
  %".42" = getelementptr i32, i32* %".41", i32 5
  store i32 6, i32* %".42"
  br label %"while_cond"
while_cond:
  %".45" = load i32, i32* %"n"
  %".46" = add i32 %".45", 1
  %".47" = icmp sgt i32 %".46", 0
  br i1 %".47", label %"while_begin", label %"while_end"
while_begin:
  %".49" = load i32, i32* %"n"
  %".50" = load i32*, i32** %"b"
  %".51" = getelementptr i32, i32* %".50", i32 %".49"
  %".52" = load i32, i32* %".51"
  %".53" = load i32, i32* %"n"
  %".54" = getelementptr inbounds [12 x i8], [12 x i8]* @"str.3", i32 0, i32 0
  %".55" = call i32 (i8*, ...) @"printf"(i8* %".54", i32 %".53", i32 %".52")
  %".56" = load i32, i32* %"n"
  %".57" = sub i32 %".56", 1
  store i32 %".57", i32* %"n"
  %".59" = load i32, i32* %"n"
  %".60" = add i32 %".59", 1
  %".61" = icmp sgt i32 %".60", 0
  br i1 %".61", label %"while_begin", label %"while_end"
while_end:
  %".63" = load i32*, i32** %"b"
  %".64" = bitcast i32* %".63" to i8*
  call void @"free"(i8* %".64")
  ret i32 0
}

@"str" = constant [11 x i8] c"a[0] = %d\0a\00"
@"str.1" = constant [11 x i8] c"a[1] = %d\0a\00"
@"str.2" = constant [11 x i8] c"a[2] = %d\0a\00"
@"str.3" = constant [12 x i8] c"b[%d] = %d\0a\00"