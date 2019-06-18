"""浏览器---->服务器发送的请求格式如下：
	GET / HTTP/1.1       请求方式和参数
	Host: 127.0.0.1:8080    请求目标的ip
	Connection: keep-alive    长连接
	Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8  浏览器支持的格式
	Upgrade-Insecure-Requests: 1   ？？？
	# 下面是浏览器的版本信息
	User-Agent: Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36
	# 支持的压缩格式
	Accept-Encoding: gzip, deflate, sdch
	Accept-Language: zh-CN,zh;q=0.8
"""


# 浏览器 返回数据包含header和body  中间用空行分隔(\r\n)
