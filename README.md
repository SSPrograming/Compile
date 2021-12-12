# 编译小组作业

&emsp;&emsp;本项目实现了将C编译为LLVM中间代码的简单编译器，词法解析和语法解析使用Antlr4，语义规则及中间代码生成使用Python。

## 依赖

1. java

   ```sh
   sudo apt install openjdk-17-jdk-headless
   ```

2. python3

   ```sh
   pip install antlr4-python3-runtime
   pip install llvmlite
   ```

3. clang 或 gcc

   ```sh
   sudo apt install clang # or gcc
   ```

4. make

   ```sh
   sudo apt install make
   ```

## 使用

1. 编译某一个`{name}.c`文件，编译过程`{name}.c -> {name}.ll -> {name}.s -> {name}.out`

   ```sh
   make filename={name}  # i.e. make filename=sort
   ```

   > `{name}.c`文件请置于`input`文件夹下

   > 生成文件位于`output`文件夹下

2. 编译并测试所有文件

   ```sh
   make test
   ```

   > 可以手动将需要测试的文件名加到`Makefile`和`output/Makefile`中的`testnames`

   > 请确保该测试文件名对应的`.c`文件已经置于`input`文件夹下

## 示例

1. `sort.c`：输入数组并输出排序结果

   ```sh
   $ make filename=sort
   # 以下为输出结果
   cd ./antlr && make
   cd ./src && java -jar ../lib/antlr-4.9.3-complete.jar -o ../../llvm/ -listener -visitor -Dlanguage=Python3 naiveC.g4
   python ./llvm/main.py ./input/sort.c ./output/sort.ll
   generate successfully：./input/sort.c -> ./output/sort.ll
   cd ./output && make run
   generate：./input/sort.ll -> ./output/sort.s
   llc sort.ll
   generate：./input/sort.sort -> ./output/sort.out
   clang sort.s -o sort.out
   ./sort.out
   初始 a = {2, 4, 6, 1, 4}
   排序 a = {1, 2, 4, 4, 6}
   请输入数组的元素个数：5
   n = 5
   请输入元素：1 6 1 2 5
   数组排序结果：1 1 2 5 6
   ```

2. `evaluate.c`：计算输入表达式的值

   ```sh
   $ make filename=evaluate
   # 中间输出结果同上
   ./evaluate.out
   表达式1：1 + 2 + 3 = 6.000000
   表达式2：1 * 2 + 3 = 5.000000
   表达式3：1 + 2 - 3 = 0.000000
   表达式4：1 - 2 / 3 = 0.333333
   表达式5：1 * (2 + 3) = 5.000000
   请输入表达式：1*(2+23)
   表达式计算结果为：1*(2+23) = 25.000000
   ```

   