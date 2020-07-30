# vaex: 秒开 100GB 数据！甩了 Pandas 几条街啊
```
sudo pip install vaex 
```

1. 将数据转换为内存映射文件格式
如Apache Arrow、Apache Parque 或HDF5。一旦数据成为内存映射格式，使用Vaex打开它是瞬间的（数据的磁盘大小超过100GB）。
2. 读取为df 
df=vaex.open('*.hdf5')
Vaex打开内存映射文件时，实际上没有数据读取。Vaex只读取文件元数据，比如磁盘上数据的位置、数据结构（行数、列数、列名和类型）、文件描述等等。
```
import vaex
df = vaex.example()  # open the example dataset provided with vaex
```
