import datetime
import hashlib
import json
import random

import requests

'''
    param init
'''
url = "http://47.95.42.12:80/gateway"
key = "acc503c56b0c4fd399f7f7093d25223c"

service_type = "WECHAT_SCANNED"
mch_id = "C149628461779610201"
out_trade_no = str(random.choice(range(1000000)))
device_info = "SN1234567890098765"
body = "Python_Code"
attach = "北京"
total_fee = "1"
spbill_create_ip = "127.0.0.1"
notify_url = "http://www.baidu.com";
start = datetime.datetime.now()
expire = start + datetime.timedelta(minutes=10)
time_start = start.strftime("%Y%m%d%H%M%S")
time_expire = expire.strftime("%Y%m%d%H%M%S")
op_user_id = mch_id
nonce_str = str(random.choice(range(1000)))
print("time_start", time_start)
print("time_expire", time_expire)
param = {}
param["service_type"] = service_type
param["mch_id"] = mch_id
param["out_trade_no"] = out_trade_no
param["device_info"] = device_info
param["body"] = body
param["attach"] = attach
param["total_fee"] = total_fee
param["spbill_create_ip"] = spbill_create_ip
param["notify_url"] = notify_url
param["time_start"] = time_start
param["time_expire"] = time_expire
param["op_user_id"] = op_user_id
param["nonce_str"] = nonce_str
print(param)

'''
    build sign
'''
keys = param.keys()
sortKeys = sorted(keys)
firstKey = sortKeys[0]
sb = firstKey + "=" + param[firstKey]
del sortKeys[0]
for k in sortKeys:
    if param[k] != "":
        sb = sb + "&" + str(k) + "=" + str(param[k])
sb = sb + key
print(sb)
m = hashlib.md5()
m.update(sb.encode("utf-8"))
sign = str(m.hexdigest()).upper()
print(sign)
param['sign'] = sign

'''
    request
'''
header = {}
para = json.dumps(param)
resp = requests.post(url, data=para, headers=header)
print("响应结果json类型", resp.text)
print("响应状态码", resp.status_code)
print("响应头", resp.headers['Content-Type'])
json_resp = resp.json()
print(json_resp)
return_code = json_resp["return_code"]
return_msg = json_resp["return_msg"]
result_code = json_resp["result_code"]
print("返回码：", return_code, "返回信息：", return_msg)
if "SUCCESS" == return_code:
    if "SUCCESS" == "SUCCESS":
        code_url = json_resp["code_url"]
        print("交易URL", code_url)
