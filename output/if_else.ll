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
  %"a" = alloca i32
  %".2" = getelementptr inbounds [20 x i8], [20 x i8]* @"str", i32 0, i32 0
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2")
  %".4" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.1", i32 0, i32 0
  %".5" = call i32 (i8*, ...) @"scanf"(i8* %".4", i32* %"a")
  %".6" = load i32, i32* %"a"
  %".7" = icmp sgt i32 %".6", 10
  br i1 %".7", label %"entry.if", label %"entry.else"
entry.if:
  %".9" = load i32, i32* %"a"
  %".10" = getelementptr inbounds [9 x i8], [9 x i8]* @"str.2", i32 0, i32 0
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".10", i32 %".9")
  br label %"entry.endif"
entry.else:
  %".13" = load i32, i32* %"a"
  %".14" = icmp sle i32 %".13", 10
  %".15" = load i32, i32* %"a"
  %".16" = icmp sgt i32 %".15", 5
  %".17" = and i1 %".14", %".16"
  br i1 %".17", label %"entry.else.if", label %"entry.else.else"
entry.endif:
  ret i32 0
entry.else.if:
  %".19" = load i32, i32* %"a"
  %".20" = getelementptr inbounds [8 x i8], [8 x i8]* @"str.3", i32 0, i32 0
  %".21" = call i32 (i8*, ...) @"printf"(i8* %".20", i32 %".19")
  br label %"entry.else.endif"
entry.else.else:
  %".23" = load i32, i32* %"a"
  %".24" = icmp sgt i32 %".23", 1
  br i1 %".24", label %"entry.else.else.if", label %"entry.else.else.else"
entry.else.endif:
  br label %"entry.endif"
entry.else.else.if:
  %".26" = load i32, i32* %"a"
  %".27" = getelementptr inbounds [8 x i8], [8 x i8]* @"str.4", i32 0, i32 0
  %".28" = call i32 (i8*, ...) @"printf"(i8* %".27", i32 %".26")
  br label %"entry.else.else.endif"
entry.else.else.else:
  %".30" = load i32, i32* %"a"
  %".31" = icmp eq i32 %".30", 1
  br i1 %".31", label %"entry.else.else.else.if", label %"entry.else.else.else.else"
entry.else.else.endif:
  br label %"entry.else.endif"
entry.else.else.else.if:
  %".33" = load i32, i32* %"a"
  %".34" = getelementptr inbounds [8 x i8], [8 x i8]* @"str.5", i32 0, i32 0
  %".35" = call i32 (i8*, ...) @"printf"(i8* %".34", i32 %".33")
  br label %"entry.else.else.else.endif"
entry.else.else.else.else:
  %".37" = load i32, i32* %"a"
  %".38" = icmp sle i32 %".37", -1
  br i1 %".38", label %"entry.else.else.else.else.if", label %"entry.else.else.else.else.else"
entry.else.else.else.endif:
  br label %"entry.else.else.endif"
entry.else.else.else.else.if:
  %".40" = load i32, i32* %"a"
  %".41" = getelementptr inbounds [10 x i8], [10 x i8]* @"str.6", i32 0, i32 0
  %".42" = call i32 (i8*, ...) @"printf"(i8* %".41", i32 %".40")
  br label %"entry.else.else.else.else.endif"
entry.else.else.else.else.else:
  %".44" = load i32, i32* %"a"
  %".45" = getelementptr inbounds [8 x i8], [8 x i8]* @"str.7", i32 0, i32 0
  %".46" = call i32 (i8*, ...) @"printf"(i8* %".45", i32 %".44")
  br label %"entry.else.else.else.else.endif"
entry.else.else.else.else.endif:
  br label %"entry.else.else.else.endif"
}

@"str" = constant [20 x i8] c"\e8\af\b7\e8\be\93\e5\85\a5\e6\95\b0\e5\ad\97a = \00"
@"str.1" = constant [3 x i8] c"%d\00"
@"str.2" = constant [9 x i8] c"%d > 10\0a\00"
@"str.3" = constant [8 x i8] c"%d > 5\0a\00"
@"str.4" = constant [8 x i8] c"%d > 1\0a\00"
@"str.5" = constant [8 x i8] c"%d > 0\0a\00"
@"str.6" = constant [10 x i8] c"%d <= -1\0a\00"
@"str.7" = constant [8 x i8] c"%d = 0\0a\00"