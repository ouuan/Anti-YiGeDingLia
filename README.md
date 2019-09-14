## Anti-YiGeDingLia

查询从一个词出发的最近 / 最远不能接，以及最近循环。

（由于接龙优先级是字典序，很多时候都会优先接到口谐辞给 / 救过不给，一个顶俩较少。）

### Data

来源：https://github.com/pwxcoo/chinese-xinhua/blob/master/archived/idiom-dirty.json

处理方式：

- 手动修改部分数据里与 QQ 不同的读音，添加一些 QQ 里有的成语。

- 使用 Python 处理出数据，BFS 计算答案，把每个音节的输出存下来。

### Demo

https://ouuan.github.io/antiyigedinglia

### Q & A

Q: XXXX 读音不对！XXXX 词库里没有！

A: 如果本项目使用的词库与 QQ 词库不同，欢迎在 [issues](https://github.com/ouuan/Anti-YiGeDingLia/issues) 中提出。

Q: Demo 的源码在哪鸭？

A: F12 或我的博客 repo 里。