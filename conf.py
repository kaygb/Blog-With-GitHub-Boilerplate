# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template="Kepler"
enable_jsdelivr = {
    "enabled": False,
    "repo": ""
}

# 站点设置
site_name = "风知识"
# site_logo = "${static_prefix}logo.png"
site_logo = "https://cdn.v2ex.com/gravatar/4cc893d113dd74ceca73f9863f2c5446/"
site_build_date = "2020-02-24T13:00+08:00"
author = "风也温柔"
email = "kaygbtop@163.com"
author_homepage = "https://eas1.cn"
description = "风也温柔，但你更美！"
key_words = ['Maverick', '熊猫小A', 'Galileo', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "风也温柔",
        "url": "https://kaygb.top",
        "brief": "风也温柔的主页。"
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
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
