# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 50
template = {
    "name": "Kepler",
    "type": "git",
    "url": "https://github.com/AlanDecode/Maverick-Theme-Kepler.git",
    "branch": "latest"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "kaygb/kaygb.github.io@master"
}

# 站点设置
site_name = "Kaygb's wiki"
# site_logo = "${static_prefix}logo.png"
site_logo = "https://kaygbcdn.170601.xyz/kaygbcom/blog-images/blog-images/static_image/kaygb-logo/tx_compressed.jpg"
site_build_date = "2020-02-24T13:00+08:00"
author = "珂泽"
email = "hi@kaygb.com"
author_homepage = "https://www.kaygb.com"
description = "珂泽的Wiki站点，用来记录零零散散的笔记！"
key_words = ['珂泽笔记','疯知识','风也的小站' ,'风也温柔', 'wiki', 'blog']
language = 'zh-CN'
external_links = [
    
    {
        "name": "HOME",
        "url": "https://www.kaygb.com",
        "brief": "HOME。"
    },
    {
        "name": "BLOG",
        "url": "https://blog.kaygb.com",
        "brief": "风也雨忆笙。"
    },
    {
        "name": "STATUS",
        "url": "https://status.eas1.cn",
        "brief": "服务监控。"
    },
    {
        "name": "GITHUB",
        "url": "https://github.com/kaygb",
        "brief": "GITHUB"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "#",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/kaygb",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "#",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<meta http-equiv="Cache-Control" content="no-cache" />
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
<link rel="icon" type="image/ico" href="https://kaygbcdn.170601.xyz/favicon.ico">
<link rel="stylesheet" href="//cdn.jsdelivr.net/gh/highlightjs/cdn-release@9.18.1/build/styles/atom-one-dark.min.css">

'''

footer_addon = r'''
<a href="http://beian.miit.gov.cn/" target="_blank" rel="noopener">豫ICP备19002054号-6</a>
'''

body_addon = r'''

''' 

valine = {
    "enable": False,
    "el": '#vcomments',
    "appId": "TUD3TUlDQQn2g7UVTa23Lieg-gzGzoHsz",
    "appKey": "SpPXP0VL2MDqcYLhEf9z0zMg",
}