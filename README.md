## Anti-YiGeDingLia

自动接到离“一个顶俩”最远的成语。

（实际上可以从任何一个词到另外一个词最近 / 最远）

### Data

来源：https://github.com/pwxcoo/chinese-xinhua/blob/master/archived/idiom-dirty.json

处理方式：

- 将“一个顶俩”加入数据中。

- 手动修改部分数据里的 bug，欢迎大家在 [issues](https://github.com/ouuan/Anti-YiGeDingLia/issues) 中提出更多 bug / 补充 / 删除成语（以 QQ 数据库为准，不一定是真正正确的读音）。**不保证修改后的数据声调正确。**

- 使用 Python 处理数据，通过 Floyd 算法求出两点间最短路保存下来。

### Demo

https://ouuan.github.io/antiyigedinglia