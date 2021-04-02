![Apache Kylin权威指南](https://img1.doubanio.com/view/subject/l/public/s29345337.jpg)

# kylin核心思想

数据分析更多是各种聚类、汇总，而不是查询明细，如果这些汇总值是提前算好的，则不需大面积扫描明细数据临时汇总，直接返回结果。

kylin就是如此，预计算，以空间换时间。“点查”可以做到亚秒级返回结果。

kylin这种将所有维度聚合预计算的称为CUBE-“多维立方体”，以3×3×3的立方体为例，可以类比下3阶魔方：

![魔方](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1579169738493&di=7ab57facc0b4200177ce012d2bb6f839&imgtype=0&src=http%3A%2F%2Fpic.51yuansu.com%2Fpic3%2Fcover%2F01%2F28%2F53%2F592363399bec4_610.jpg)
![魔方2](https://images2015.cnblogs.com/blog/997232/201610/997232-20161015213701062-312799747.jpg)

由此可见，立方体的规模取决于维度，维度的数量和每个维度的基数，n阶维度有$$2^n$$种维度组合。

如abc三阶维度，则有()(a)(b)(c)(ab)(ac)(bc)(abc)8种组合。

每个维度如a有10个值，此为维度的基数。基数越大，cube越大。

$$2^n$$,当n越大，维度膨胀越厉害，但并不是每种维度组合都有意义，如果把所有维度组合比作一棵树，则去除一些组合称为维度“剪枝”



