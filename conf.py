# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "https://kaygb.github.io/wikisource"
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
    "repo": "kaygb/wikisource@master"
}

# 站点设置
site_name = "ICE WIKI"
# site_logo = "${static_prefix}logo.png"
site_logo = "https://cdn.jsdelivr.net/gh/kaygb/twentytwenty/tx.jpg"
site_build_date = "2020-02-24T13:00+08:00"
author = "珂泽"
email = "hi@vwmwv.cn"
author_homepage = "https://170601.xyz"
description = "珂泽的Wiki站点，用来记录零零散散的笔记！"
key_words = ['珂泽笔记','疯知识','风也的小站' ,'风也温柔', 'wiki', 'blog','7601']
language = 'zh-CN'
external_links = [
    
    {
        "name": "HOME",
        "url": "https://170601.xyz/",
        "brief": "HOME"
    },
    {
        "name": "GITHUB",
        "url": "https://github.com/kaygb",
        "brief": "GITHUB"
    }
]
nav = [
    {
        "name": "最新发布",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "全部文档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于本站",
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
<link rel="icon" type="image/ico" href="https://cdn.jsdelivr.net/gh/kaygb/twentytwenty/favicon.ico">
<link rel="stylesheet" href="//cdn.jsdelivr.net/gh/highlightjs/cdn-release@9.18.1/build/styles/atom-one-dark.min.css">

'''

footer_addon = r'''
<a href="http://beian.miit.gov.cn/" target="_blank" rel="noopener">豫ICP备19002054号-8</a>
'''

body_addon = r'''

''' 

valine = {
    "enable": False,
    "el": '#vcomments',
    "appId": "",
    "appKey": "",
}
