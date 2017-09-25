#   目录
[TOC]
#   方案概述
##  业务实现流程
接入流程：
[点击查看微信APP接入流程](https://pay.weixin.qq.com/wiki/doc/api/app/app.php?chapter=8_5)

#   环境
>   测试URL：http://bjrcb-test-pay.291501.com/gateway

#   说明
>   在微信开放平台提交APP注册认证通过后，获得的APPID 这个操作如未完成的话 申请不成功，请知晓
#   业务
##  请求数据
POST JSON 内容体进行请求

字段名| 变量名| 必填|类型|说明|
---|---|---|---|---|
业务类型|service_type|是|varchar(32)|类型：WECHAT_APP
应用ID|appid|是|varchar(32)|微信开放平台的应用APPID
商户号|mch_id|是|varchar(32)|商户号，由银行分配
设备号|device_info|否|varchar(32)|终端设备号
商品描述|body|是|varchar(32)|商品描述
商品详情|detail|否|varchar(999)|商品详情
附加数据|attach|否|varchar(32)|附加数据，原样返回
商户订单号|out_trade_no|是|varchar(32)|商户系统的订单号
货币类型|fee_type|否|varchar(32)|默认CNY
总金额|total_fee|是|varchar(32)|金额，单位：分
终端IP|spbill_create_ip|是|varchar(32)|生成订单机器的IP
交易开始时间|time_start|否|varchar(32)|格式yyyymmddhhmmss
交易时间|time_expire|否|varchar(32)|格式yyyymmddhhmmss
商品标记|goods_tag|否|varchar(32)|商品标记信息
通知地址|notify_url|是|varchar(255)|异步通知地址
商品ID|product_id|否|varchar(32)|商品id
操作人|op_user_id|否|varchar(32)|操作者
指定支付方式|limit_pay|否|varchar(32)|no_credit-不使用信用卡支付
交易类型|trade_type|是|varchar(32)|APP
随机字符串|nonce_str|是|varchar(32)|随机字符串
签名|sign|是|varchar(32)|详见签名规则

##  返回数据
数据按JSON的格式实时返回

字段名| 变量名| 必填|类型|说明|
---|---|---|---|---|
返回状态码|return_code|是|varchar(16)|SUCCESS/ERROR_CODE
返回信息|return_msg|否|varchar(128)|返回信息
公众号ID|appid|是|varchar(32)|微信公众号id
商户号|mch_id|是|varchar(32)|商户号，银行分配
随机字符串|nonce_str|是|varchar(32)|随机字符串
业务结果|result_code|是|varchar(16)|数据与trade_state同步，建议以trade_state做为订单状态的判断
错误代码|err_code|否|varchar(32)|错误码
错误代码描述|err_code_des|否|varchar(128)|错误代码描述
交易类型|trade_type|否|varchar(32)|交易类型
平台订单号|transaction_id|是|varchar(32)|银行平台订单号
商户订单号|out_trade_no|是|varchar(32)|下游平台订单号
支付信息|pay_json|是|varchar(500)|Js调起微信需要的信息
预支付交易会话标识|prepay_id|是|varchar(60)|预支付交易会话标识
签名|sign|是|varchar(32)|详见签名规则

##  调起支付
>   下游获取到银行的预支付交易会话标识, 带着此标识调起微信支付进行支付

详细信息请参照:[微信APP调起支付](https://pay.weixin.qq.com/wiki/doc/api/app/app.php?chapter=9_12&index=2)

#   异步通知
文档参考微信_交易异步通知接口