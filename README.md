## Anti-YiGeDingLia

自动接到离“一个顶俩”最远的成语。

（实际上可以从任何一个词到另外一个词最近 / 最远）

### Data

来源：https://github.com/pwxcoo/chinese-xinhua/blob/master/archived/idiom-dirty.json

处理方式：

- 将“一个顶俩”加入数据中。

- 手动修改部分数据里的 bug（以 QQ 词库为准），**不保证修改后的数据声调正确，不保证修改后的数据除第一个字和最后一个字正确。**

- 使用 Python 处理数据，~~通过 Floyd 算法求出两点间最短路保存下来~~，把图存下来用 JS 跑 n 遍 BFS。

### Demo

https://ouuan.github.io/antiyigedinglia

### Q & A

Q: XXXX 读音不对！XXXX 词库里没有！

A: 如果本项目使用的词库与 QQ 词库不同，欢迎在 [issues](https://github.com/ouuan/Anti-YiGeDingLia/issues) 中提出。

Q: Demo 的源码在哪鸭？

A: F12 或我的博客 repo 里。