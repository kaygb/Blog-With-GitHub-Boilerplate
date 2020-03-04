---
layout: post
title: CSS中position:fixed实现div居中
slug: 20200304-css-fixed-align-center
date: 2020-03-04 11:48
status: publish
author: 风也温柔
categories: 
  - 编程笔记
  - WEB前端
tags: 
  - css
  - fixed居中
  - div
excerpt: div居中
---

~~~css
div{
position:fixed;
margin:auto;
left:0;
right:0;
top:0;
bottom:0;
width:200px;
height:150px;
}
~~~

如果只需要左右居中，那么把`bottom:0; top:0;` 删掉

如果只需要上下居中，那么把`left:0; 或者 right:0;` 删掉