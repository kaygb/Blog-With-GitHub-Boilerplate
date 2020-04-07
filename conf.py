# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 50
template="Kepler"
enable_jsdelivr = {
    "enabled": True,
    "repo": "kaygb/kaygb.github.io@master"
}

# 站点设置
site_name = "疯知识"
# site_logo = "${static_prefix}logo.png"
site_logo = "https://gt.eas1.cn/avatar/4cc893d113dd74ceca73f9863f2c5446/"
site_build_date = "2020-02-24T13:00+08:00"
author = "风也"
email = "i@eas1.cn"
author_homepage = "https://eas1.cn"
description = "风也的Wiki站点，用来记录零零散散的笔记！"
key_words = ['疯知识','风也的小站' ,'风也温柔', 'wiki', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "BLOG",
        "url": "https://eas1.cn",
        "brief": "风也的小站。"
    },
    {
        "name": "BAIDU",
        "url": "https://baidu.kaygb.top",
        "brief": "帮你百度一下。"
    },
    {
        "name": "KTOOLS",
        "url": "https://tools.wgb.ink",
        "brief": "在线工具箱。"
    },
    {
        "name": "STATUS",
        "url": "https://status.kaygb.top",
        "brief": "风也温柔的服务监控。"
    },
    {
        "name": "GITHUB",
        "url": "https://github.com/kaygb/kaygb.github.io",
        "brief": "风也温柔的服务监控。"
    }
]
nav = [
    {
        "name": "HOME",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "ARCHIVES",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "ABOUT",
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
<link rel="icon" type="image/ico" href="//gt.eas1.cn/avatar/4cc893d113dd74ceca73f9863f2c5446/">

'''

footer_addon = r'''
<script type="text/javascript" src="//js.users.51.la/20664491.js"></script>

'''

body_addon = r'''

'''

