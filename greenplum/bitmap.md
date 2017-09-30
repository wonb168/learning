# 用户画像标签筛选
## 解压
unzip gpdb-roaringbitmap-master.zip
## 编译
gcc -march=native -O3 -std=c11 -Wall -Wpointer-arith  -Wendif-labels -Wformat-security -fno-strict-aliasing -fwrapv -fexcess-precision=standard -fno-aggressive-loop-optimizations -Wno-unused-but-set-variable -Wno-address -fpic -D_GNU_SOURCE -I$GPHOME/include/postgresql/server -I$GPHOME/include/postgresql/internal -c -o roaringbitmap.o roaringbitmap.c

gcc -O3 -std=gnu99 -Wall -Wpointer-arith  -Wendif-labels -Wformat-security -fno-strict-aliasing -fwrapv -fexcess-precision=standard -fno-aggressive-loop-optimizations -Wno-unused-but-set-variable -Wno-address  -fpic -shared --enable-new-dtags -o roaringbitmap.so roaringbitmap.o
## 复制到每一个节点
cp ./roaringbitmap.so $GPHOME/lib/postgresql/

# 使用
create table test_bitmap(id int,bitmap roaringbitmap);
insert into test_bitmap select 1,rb_build(array[1,2]);
insert into test_bitmap select 2,rb_build_agg(e) from generate_series(1,100) e;
select rb_iterate(rb_and((select bitmap from test_bitmap where id=1),(select bitmap from test_bitmap where id=2)));
select rb_cardinality(rb_and_agg(bitmap)) from test_bitmap;
## 多标签查询
select rb_iterate(bitmap) from (select rb_and_agg(bitmap)  as bitmap from test_bitmap where id in (1,2,3,4,5,6,7,8)) foo

# 官方示例
CREATE TABLE t1 (id integer, bitmap roaringbitmap);
INSERT INTO t1 SELECT 1,RB_BUILD(ARRAY[1,2,3,4,5,6,7,8,9,200]);
INSERT INTO t1 SELECT 2,RB_BUILD_AGG(e) FROM GENERATE_SERIES(1,100) e;
## 查询

select * from t1
SELECT RB_OR(a.bitmap,b.bitmap) FORM (SELECT bitmap FROM t1 WHERE id = 1) AS a,
(SELECT bitmap FROM t1 WHERE id = 2) AS b;

SELECT RB_OR_AGG(bitmap) FROM t1;
SELECT RB_AND_AGG(bitmap) FROM t1;
SELECT RB_XOR_AGG(bitmap) FROM t1;
SELECT RB_BUILD_AGG(e) FROM GENERATE_SERIES(1,100) e;
SELECT RB_CARDINALITY(bitmap) FROM t1;
SELECT RB_ITERATE(bitmap) FROM t1 WHERE id = 1;
-- 构建数组
select RB_ITERATE(rb_build('{1,2,3,4,5}'));
-- and交集
select RB_ITERATE(rb_and(rb_build('{1,2,3}'),rb_build('{3,4,5}')));
-- or并集
select RB_ITERATE(rb_or(rb_build('{1,2,3}'),rb_build('{3,4,5}')));
-- xor异或
select RB_ITERATE(rb_xor(rb_build('{1,2,3}'),rb_build('{3,4,5}')));
-- andnot含前不含后
select RB_ITERATE(rb_andnot(rb_build('{1,2,3}'),rb_build('{3,4,5}')));
-- 基数（个数）
select rb_cardinality(rb_build('{1,2,3,14,15}'))
-- 交集的个数
select rb_and_cardinality(rb_build('{1,2,3}'),rb_build('{3,4,5}'))
-- 交集的个数
select rb_or_cardinality(rb_build('{1,2,3}'),rb_build('{3,4,5}'))
-- 异或的个数
select rb_xor_cardinality(rb_build('{1,2,3}'),rb_build('{3,4,5}'))
-- andnot的个数
select rb_andnot_cardinality(rb_build('{1,2,3}'),rb_build('{3,4,5}'))
-- 是否为null
select rb_is_empty(rb_build('{1,2,3,4,5}'));
-- 是否相等
select rb_equals(rb_build('{1,2,3}'),rb_build('{3,4,5}'));
-- 跳过[a,b)
select RB_ITERATE(rb_flip(rb_build('{1,2,3,4,5,6}'),2,4));
select RB_ITERATE(rb_flip(rb_build('{1,2,3,4,5,6}'),2,5));
-- 最小值
select rb_minimum(rb_build('{1,2,3}'));
-- 最大值
select rb_maximum(rb_build('{1,2,3}'));
-- 取元素
select rb_rank(rb_build('{1,2,3}'),2);
## list
select RB_ITERATE(rb_build_agg(1))
select rb_or_agg(rb_build('{1,2,3}'))
select rb_and_agg(rb_build('{1,2,3}'))
select rb_xor_agg(rb_build('{1,2,3}'))
select rb_or_cardinality_agg(rb_build('{1,2,3}'))
select rb_and_cardinality_agg(rb_build('{1,2,3}'))
select rb_xor_cardinality_agg(rb_build('{1,2,3}'))
