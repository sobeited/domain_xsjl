# -*- coding: utf-8 -*-

# Scrapy settings for domain_zhuce project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

import random

BOT_NAME = 'domain_zhuce'

SPIDER_MODULES = ['domain_zhuce.spiders']
NEWSPIDER_MODULE = 'domain_zhuce.spiders'


'''读取代理文件中的ip，写入PROXIES'''
PROXIES = []
for line in open('/Users/sunjian/Desktop/hc项目/proxy/hege_daili.txt'):
    line = line.strip()
    PROXIES.append({'ip_port':'%s' % line ,'user_pass':''})

# 随机cookie
def getCookie():
    cookie_list = [
    'source=bd-ymzc-ymcx2; CNZZDATA293207=cnzz_eid%3D1976693503-1458010182-http%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1458264075'
    ]
    cookie = random.choice(cookie_list)
    return cookie

# 定义ua列表
USER_AGENTS =[
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        #'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
    ]

RETRY_TIMES = 10
RETRY_HTTP_CODES = [ 500 , 503 , 504 , 400 , 403 , 404 , 408 ,302]


# 假如中间件
DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware' : 90 ,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware':None,
    'domain_zhuce.middlewares.RandomUserAgent':400,

    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    'domain_zhuce.middlewares.ProxyMiddleware': 100,
}

'''降低log级别，取消注释则输出抓取详情'''
LOG_LEVEL = 'INFO'

# 禁止cookie
COOKIES_ENABLED = False

# cookie debug
# COOKIES_DEBUG = False

# DEFAULT_REQUEST_HEADERS ，定义请求的头信息
DEFAULT_REQUEST_HEADERS = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Host':'panda.www.net.cn',
    'RA-Sid':'7739A016-20140918-030243-3adabf-48f828',
    'RA-Ver':'3.0.7',
    'Upgrade-Insecure-Requests':'1',
    'Cookie':'%s' % getCookie(),
}

# 禁止显示<urlopen error timed out>告警
DOWNLOAD_HANDLERS = {
  's3': None,
}

# 下载延迟，既下载两个页面之间的等待时间
DOWNLOAD_DELAY = 0.03

# 并发最大值
CONCURRENT_REQUESTS = 600

# 对单个网站的并发最大值
CONCURRENT_REQUESTS_PER_DOMAIN = 600

#启动自动限速
AUTOTHROTTLE_ENABLED = False

# 设置下载超时
DOWNLOAD_TIMEOUT = 60

#配置数据库
MYSQL_HOST = '127.0.0.1'
MYSQL_DBNAME = 'heichan'
MYSQL_USER = 'root'
MYSQL_PASSWD = ''


# #启用PIPELINES
# ITEM_PIPELINES = {
#     'domain_filter.pipelines.DomainFilterPipeline': 300,
#     'domain_filter.pipelines.MySQLDomainFilterPipeline': 400,
# }
