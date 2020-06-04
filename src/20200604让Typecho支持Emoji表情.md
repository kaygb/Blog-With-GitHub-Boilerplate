---
layout: post
title: 让Typecho支持Emoji表情
slug: 20200604-typecho-emoji
date: 2020-06-04 10:33
status: publish
author: 风也
categories: 
  - 编程笔记
  - TYPECHO
tags: 
  - typecho
  - emoji
excerpt: 让Typecho支持Emoji表情
---

Typecho默认不支持emoji表情是由于编码的问题，只需要将默认的数据库编码utf8修改为utf8mb4即可，不过utf8mb4编码在PHP5.5以后才支持。

Emoji是一种在Unicode位于u1F601-u1F64F区段的字符。这个显然超过了目前常用的UTF-8字符集的编码范围u0000-uFFFF。在MySQL中，UTF-8只支持最多3个字节，而emoji是4个字节。这就导致如果你不修改数据库的话，typecho是无法支持Emoji表情的。

当然好消息是utf8mb4其实是完全兼容utf-8，修改后不会影响现有数据及后期数据。

1.修改数据库编码

在PhpMyadmin中选择typecho数据库，操作-->排序规则-->选择utf8mb4_unicode_ci然后执行。

2.修改表编码

执行以下sql语句
~~~sql
alter table typecho_comments convert to character set utf8mb4 collate utf8mb4_unicode_ci;
alter table typecho_contents convert to character set utf8mb4 collate utf8mb4_unicode_ci;
alter table typecho_fields convert to character set utf8mb4 collate utf8mb4_unicode_ci;
alter table typecho_metas convert to character set utf8mb4 collate utf8mb4_unicode_ci;
alter table typecho_options convert to character set utf8mb4 collate utf8mb4_unicode_ci;
alter table typecho_relationships convert to character set utf8mb4 collate utf8mb4_unicode_ci;
alter table typecho_users convert to character set utf8mb4 collate utf8mb4_unicode_ci;
~~~
3.修改typecho配置文件config.inc.php

拉到最下面找到这一行
~~~php
'charset'   =>  'utf8', 
~~~
修改为
~~~php
'charset'   =>  'utf8mb4', 
~~~
Typecho就可以使用emoji表情了,赶紧评论试试吧,搜索emoji表情还真不少.

😷😀😂🤣😃😄😅🚚😊😋😎😍😘😗😙😚🙂🤗💰🙏💪👕☎🐁🚀📡🍎💯📺🚴

本文转载来源：旧日的足迹
原文链接：https://jrdzj.cc/2020-03-07.html