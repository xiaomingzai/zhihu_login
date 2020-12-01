# encoding:utf8

import requests

# 会话管理
session = requests.session()

# 客户端
session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
# 版本
session.headers['X-Zse-83'] = '3_2.0'
# 发包数据的格式
session.headers['Content-Type'] = 'application/x-www-form-urlencoded'

# session.headers['cookie'] = '_xsrf=4BY16ki1WlppCMOIxeVbNs910AjmP575; _zap=c80ef9d0-cf9d-4713-9dbc-a6050857315a;'\
#                             ' d_c0="ABCduF8uRRKPTpDG_EoBrPmEJarAxdCFaJU=|1606660313"; Hm_lvt_98beee57fd2ef70ccd'\
#                             'd5ca52b9740c49=1606488515,1606488614,1606489686,1606653240; Hm_lpvt_98beee57fd2ef70'\
#                             'ccdd5ca52b9740c49=1606660355; capsion_ticket="2|1:0|10:1606660347|14:capsion_ticke'\
#                             't|44:MGIwNzk0ZmExYmQ4NDlmNWJjNmIzNjM4MTQxNjhhMWI=|fbf8c624a74515cf498316b09a7b961a4'\
#                             'd15d2e8779613d7763688a1c37ad916"; KLBRSID=b33d76655747159914ef8c32323d16fd|1606660357|1606660129'


print(session.cookies)
result = session.post('https://www.zhihu.com/udid')  # {"show_captcha":false}  不需要验证码。，缺少时会提示“请输入验证码”
print(result.text)
print(session.cookies)




#session.headers['grant_type'] = 'password'
# 请求是否显示验证码，缺少时会提示“缺少验证码票据”
result = session.get('https://www.zhihu.com/api/v3/oauth/captcha?lang=cn')
print(result.text)
print(session.cookies)


# 参数，参数值来自登录接口Form Data>view source
params = 'aR79k4U0cT2tXqYq8LPG6vHmxq2pkLnmtbSBDgg9kLtxgeSmhbfGiqX1jbfVoG398LF0gQN0cT2tuqYq8LkMQbwGivwOgUxGw9e0g4e8kCV92vgBzh3qk4R92LkYFhVGwqoVJbCGST2tECx9BLkBEJXmST2tXCLBG_e0gAX1F93OUqNq8LfmAhrqc_txr7NKEqYhHUcmoqVOUu3q8Lk0r6rq68FpSX20m8tyPU9qkLnm2LfBpwNmkveMcBtxgMtBTGY8Q6L8o_2Ye8x0ZutqoAUqQ0FXoTS888FqbQXyb72xUqNqTgt924_BkC3VUbSBtq3qk478gGpucUO1PD3ZJCe8Xq2tgqNMsvSMS79hoL2xeXty18FqSiUqr_LxgRVmZ9oMgGL1eBtxg_NMwGoM2JXMXq2tguVKKvwGEJHM3BtxgRF0zuFqrH9BrXxpggY8BTxyNguq6X2fS828G8OBFgr8Xq2tHgSVKbOBDBe8'

# 发包
result = session.post('https://www.zhihu.com/api/v3/oauth/sign_in',data=params)
print(result.text)
#print(result.content.decode('utf8'))