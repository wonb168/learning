# postgresql
驱动：
```
com.microsoft.sqlserver.jdbc.SQLServerDriver
org.postgresql.Driver
oracle.jdbc.OracleDriver
```
```
import psycopg2

conn = psycopg2.connect(dbname="apparel_poc", user="apparel_poc",password="密码", host="192.168.16.183", port="5432")
c = conn.cursor()
print(sql)
c.execute(sql)
conn.commit()

c.close()
conn.close() 


```
## 分片read_jdbc
