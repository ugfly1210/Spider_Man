
# 关于response
# 1：编码问题   response.encoding='gbk'

# 2：json


# 关于SSL
# 一般用于公司内部，登录时需要携带公司发的证书及秘钥。一般内网或者和银行有关的需要携带整数访问网站
# 解决方案：
#   1：verify   # 不验证证书。
#   2：urllib3 模块下的disable_warnings
