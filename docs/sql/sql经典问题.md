1. 连续登录n天
比如从半年的每日登录记录中找出连续7天登录的所有用户。（假定已经处理成每天多次登录的为一条数据了）
```
select t.* from user_logon_history t;
```

USER_ID | USER_NAME |  LOGIN_DATE
--------|-----------|------------- 
1 | ZhangSan  |  4/1/2018 
1 | ZhangSan  |  4/2/2018
1 | ZhangSan  |  4/4/2018
1 | ZhangSan  |  4/5/2018
1 | ZhangSan  |  4/7/2018
2 | LiSi | 4/15/2018
2 | LiSi | 4/16/2018
2 | LiSi | 4/17/2018
3 | WangWu |  4/8/2018
3 | WangWu |  4/9/2018
3 | WangWu |  4/10/2018
3 | WangWu |  4/11/2018


- 问题分析  
首先，逐条循环的不予讨论，原因you known。
连续登录天，则其相邻日期相差为1。

- 基础解法：
如果未登录的日期也有记录（可用日期维表笛卡尔积获得），登录的标记1，否则标0，按日期顺序拼接所有的01标记，如果中间包含7个1的字符串则是。
该法需要补空档，增加了原始数据量，而且至少要3步（cross join；case when；like），且性能不理想不给sql了。

- 解法1  
对数据按日期顺序编号，如果连续则日期和序号的差值相同
该法不仅能找出7天及以上的用户，还能给出具体是哪几天
```
with tmp as(
    select user_id,user_name,login_date,login_date-(row_number() over (partition by user_id order by login_date)) as tmp_date
    from user_logon_history
)select user_id,tmp_date,count(*) from tmp group by ser_id,tmp_date having count(*)>=7
```
- 解法2  
对数据按日期顺序编号，如果连续7天，则第7天与当前天相差7
该法只能判断出有连续7天及以上的用户
```
with tmp as(
    select user_id,user_name,login_date,lead(login_date,7) over (partition by user_id order by login_date) as tmp_date
    from user_logon_history
)select user_id,tmp_date,count(*) from tmp 
where tmp_date-login_date=7
```
