# 节点配置
1master，2slave，每slave 4segment+4mirror，其中1slave兼做standby
8核64G服务器3台
子节点故障会自动切换mirror，主节点故障需手动切换standby
