=== 思路 ===
本题主要是在加权有向图这个数据结构上实现特定的操作，主要代码在directedgraph.cpp和shortestpath.cpp中。
主要操作有：
* 判断A-B-C类似的路径是否直接可达以及距离
* 查找A-B的满足特定条件的路径，包括不超过N跳或者不超过距离M的路径
* A-B的最小路径

测试代码在test.cpp中，10个测试用例对应10个题目。增加测试用例非常方便。

=== 编译与执行 === 
make
./bin/test

或者 ./bin/test ./testdata.dat
