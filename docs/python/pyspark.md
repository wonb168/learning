# pyspark
## 加序号
```
from pyspark.sql.functions import monotonically_increasing_id
df2=df.withColumn('id',monotonically_increasing_id())
df2 = df.withColumn('id', F.row_number().over())
df2.show()
```
# 创建df
```

from pyspark.sql.types import LongType, StructField, StructType
data=data = [('a', 1, 18), ('b', 2, 22), ('c', 3, 20)]
df = spark.createDataFrame(data)
# 直接变df，原df都到1列了
# zipped_rdd = df.rdd.zipWithIndex()
# spark.createDataFrame(zipped_rdd).show() 

# 取出原结构并增加1列
new_schema = StructType(df.schema.fields+[StructField('id',LongType(),True)])
rdd=df.rdd.zipWithIndex().map(lambda x: (list(x[0]) + [x[1]]))
df2=spark.createDataFrame(rdd, new_schema)

```
## 函数
```
from pyspark.sql.types import LongType, StructField, StructType

def dfZipWithIndex (df, offset=1, colName="rowId"):
    '''
        Enumerates dataframe rows is native order, like rdd.ZipWithIndex(), but on a dataframe 
        and preserves a schema

        :param df: source dataframe
        :param offset: adjustment to zipWithIndex()'s index
        :param colName: name of the index column
    '''

    new_schema = StructType(
                    [StructField(colName,LongType(),True)]        # new added field in front
                    + df.schema.fields                            # previous schema
                )

    zipped_rdd = df.rdd.zipWithIndex()

    new_rdd = zipped_rdd.map(lambda (row,rowId): ([rowId +offset] + list(row)))

    return spark.createDataFrame(new_rdd, new_schema)
    ```