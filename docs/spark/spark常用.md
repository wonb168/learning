# 创建df
```
df = spark.createDataFrame(Seq(
  ("ming", 20, 15552211521L),
  ("hong", 19, 13287994007L),
  ("zhi", 21, 15552211523L)
)).toDF("name", "age", "phone")

df = spark.createDataFrame(Seq(
  (1),
  (1),
  (1)
)).toDF("id")
df=spark.makeRDD(Array(
      "{\"name\":1}",
      "{\"name\":2}",
      "{\"name\":3}"
    ))
df = spark.createDataFrame([{'name':1},
    {'name':2},
    {'name':3}
    ])    
df.show()
```
在当前目录下，查找所有内容包含‘abc'的文件

find . -type f | xargs grep -l '灵异'

或

find . -type f -exec grep -l 'abc' {} \;
# 遍历df
```
# def f(row):
#     print(row[0],row[1],row[2])
#     duplicate_data(row[0],row[1],row[2])

# df=spark.sql(sql)
# df.foreach(f)
```