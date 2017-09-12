#   目录
[TOC]

#   环境
>   测试URL: http://47.95.42.12:80/customer/service

#   业务
##  卡bin信息查询请求参数

字段名|变量名|必填|类型|说明|
---|---|---|---|---
业务类型|serviceType|是|varchar(32)|值为：QUERY_CARDBIN
代理商编号|agentNum|是|varchar(32)|由银行分配
银行卡号|bankCard|是|varchar(32)|
签名|sign|是|varchar(32)|详见签名规则

##  响应数据
字段名|变量名|必填|类型|说明|
---|---|---|---|---
返回码|return_code|是|varchar(32)|SUCCESS/ERROR_CODE 
返回信息|return_msg|是|varchar(255)|返回信息
联行号|alliedBankNo|否|varchar(255)|总行联行号
银行名称|bankName|否|varchar(255)|银行名称
签名|sign|是|varchar(32)|详见签名规则
