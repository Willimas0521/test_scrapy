# Scrapy settings for an_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'an_spider'

SPIDER_MODULES = ['an_spider.spiders']
NEWSPIDER_MODULE = 'an_spider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'an_spider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cookie": "sessid=5868782A-A7D9-E56E-B542-E6C54BFFA9AA; aQQ_ajkguid=A450677A-8461-6976-94F8-30B738F00027; ctid=11; twe=2; _prev_stat_guid=A450677A-8461-6976-94F8-30B738F00027; _stat_guid=3B699A82-120E-404D-8708-5904AD60755B; id58=CpQMQ2IPGFM3L6n9vCzaAg==; _ga=GA1.2.1915822952.1645156430; 58tj_uuid=bca39606-bf93-48a3-ae6b-7760626bd1ba; als=0; ajk_member_verify=YwDdUG4D49d8xkeRKEJqV7hoMSeGvePeR%2BP9aCLTTt4%3D; ajk_member_verify2=MjI1NDE2NDc2fEZFRDJxVXZ8MQ%3D%3D; ajk_member_id=225416476; isp=true; ajk-appVersion=; new_uv=9; fzq_h=9f51045844a98ec1d859792c0c0cc02a_1647791483323_27329d49686e4cd2b6a2925fed7455f3_3752308661; _stat_rfpn=Ershou_Web_Property_List_FilterPage; xxzl_cid=289e15db88a24df7bf5a49b24040dcda; xzuid=6a41a52f-828d-401f-8c5d-22a7a0184800; obtain_by=1; ajkAuthTicket=TT=f3a9fa28824dfe726acd7c01e0fa672a&TS=1647791514254&PBODY=ALklFoPi04Xew1D2G6N8dinviaSz0D_Xz0yMndRyI1Rny5KMd5xSFG6EQXAZhyY6R43aYd5-FQ-ZjJc15oNLoruiANUC9yxmxA_rVzvxKIb7lZU-5l3-WwxDJ_f5LyneTI5Q3rjIPmZsUvYHc7XFBhjBYafxqZfOOm91ZSYlhF8&VER=2&CUID=CwXjdQPEjVdEO2J9uBXPcqS2r3T3qS61",
    "referer": "https://anjuke.com/",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"101\", \"Microsoft Edge\";v=\"101\"",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32"
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'an_spider.middlewares.AnSpiderSpiderMiddleware': 543,
#}



# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'an_spider.middlewares.ProxyMiddleware': 543,
#     'an_spider.middlewares.UAMiddleware': 544,
# }
# 修改为之前在middlewares中新定义的代理类

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'an_spider.pipelines.AnSpiderPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 添加调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 如果中断，再启动时从中断的地方开始
SCHEDULER_PERSIST = True
# 如果不配置，就会默认使用队列
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"

REDIS_HOST= '127.0.0.1'
REDIS_PORT = 6379


PROXIES = ['https://218.1.142.142:57114',
           'https://218.1.142.138:57114',
           'https://114.88.243.93:55443']

USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    "Dalvik/1.6.0 (Linux; U; Android 4.2.1; 2013022 MIUI/JHACNBL30.0)",
    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "AndroidDownloadManager",
    "Apache-HttpClient/UNAVAILABLE (java 1.4)",
    "Dalvik/1.6.0 (Linux; U; Android 4.3; SM-N7508V Build/JLS36C)",
    "Android50-AndroidPhone-8000-76-0-Statistics-wifi",
    "Dalvik/1.6.0 (Linux; U; Android 4.4.4; MI 3 MIUI/V7.2.1.0.KXCCNDA)",
    "Dalvik/1.6.0 (Linux; U; Android 4.4.2; Lenovo A3800-d Build/LenovoA3800-d)",
    "Lite 1.0 ( http://litesuits.com )",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0",
    "Mozilla/5.0 (Linux; U; Android 4.1.1; zh-cn; HTC T528t Build/JRO03H) "
    "AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30; 360browser(securitypay,securityinstalled); 360(android,uppayplugin); 360 Aphone Browser (2.0.4)",
]