---
layout: post
title: 教室报修管理系统（HGNUMAN）项目文档 
slug: how-to-use-hgnuman
date: 2021-07-15 11:46
status: publish
author: 珂泽
categories: 
  - 项目文档
tags: 
  - HGNUMAN
  - 教室报修管理系统
---

## 系统介绍

一款为校园内教室设备报修而设计的系统，包括两种角色：管理员和信息员 。~~包括三种角色（管理员，维修人员，普通用户）~~

报修流程：

1. 信息员登入系统，点击故障报修，选择故障对象的位置和故障分类，填写故障描述，上传故障照片。
2. 管理员通过后台导出故障数据提交给维修公司维修。
3. 信息员查看所报修对象是否维修完成，并在系统确认维修状态。



## 使用帮助

### 普通用户

注册账号或者使用管理员分配的账号登录到系统中

![hgnuman-help1](./images/hgnuman-help1.png)

![image-20210715150911713](images/image-20210715150911713.png)

点击左侧栏创建维修单，填写教室信息，故障描述，选择设备分类和所在教学楼。

![](images/hgnuman/xtys.gif)

![(images/hgnuman/xtys.gif)

上传照片，需要您使用系统相机拍照之后，点击上传图片按钮选择相应照片上传，上传完成会显示预览图片，点击创建即可。

创建完成之后，点击侧边栏我提交的维修单，即可看到维修单状态，请在所报修任务维修完成之后（一般一周之后），如已维修，请点击审核通过按钮，完成审核。每学期统计数据将以审核完成的数量为主发放学分。

> 信息员请自行审核报修任务是否维修完成

![image-20210715151422227](images/image-20210715151422227.png)

### 管理员

系统在第一次安装运行后，默认设置第一个注册的用户为管理员。

管理员可查看全部维修单，并导出维修单。

首次登录成功请在系统设置内设置系统域名用于数据导出的图片展示，如`https://mana.eas1.cn`(最后请不要添加斜杠)

系统初始化应包含以下步骤：

1. 添加校区

![image-20210715152245430](images/image-20210715152245430.png)

2. 添加教学楼和教室

![image-20210715152347359](images/image-20210715152347359.png)

![image-20210715152336394](images/image-20210715152336394.png)

3. 创建分类

![image-20210715152412011](images/image-20210715152412011.png)



#### 用户管理

默认情况下，系统允许用户自主修改个人信息，但不包括学工号，管理员可在用户管理界面修改用户所有信息包括学工号，可设置用户的权限角色。

![image-20210715152701796](images/image-20210715152701796.png)

![image-20210715152741758](images/image-20210715152741758.png)

#### 导出数据

系统支持选择时间区间进行数任务单数据的导出，默认选择不包括当天的前一周提交的所有维修单数据，点击提交导出请求按钮，将会进行处理，稍等片刻，从下方的表格处点击下载按钮即可下载。

![image-20210715152842355](images/image-20210715152842355.png)

> 导出时间与服务器性能和数据数量有关，在开发者设备测试时，7万条数据导出时间在十秒钟左右。

导出的EXCEL字段如下：

![image-20210715153354710](images/image-20210715153354710.png)

## 开发

### 普通部署

所需环境及软件：

- 64位Linux系统(建议Centos7，Ubuntu1804及以上)
- OpenJDK11  (下载地址：[Java Platform, Standard Edition 11 Reference Implementations](http://jdk.java.net/java-se-ri/11))

- Mysql8.0 （5.7 及以上）或MariaDB（推荐）
- nginx（可选）

在根目录创建文件夹，然后上传Jar包到服务器

```bash
cd /
mkdir hgnuman
// 上传jar包
```

然后使用以下命令运行：

```bash
sudo -u root nohup /usr/bin/java -jar /hgnuman/hgnuman.jar --server.port=8036 >> /hgnuman/hgnuman.log 2>&1 &
```

等待一分钟左右，访问：`http://ip:8036` 查看是否启动成功，系统日志科查看`/hgnuman/hgnuman.log`

### 使用Docker部署

创建文件夹

```bash
sudo mkdir /opt/hgnuman/app
sudo mkdir /opt/hgnuman/files
```

将jar包和antispanmy.xml到files目录下，并复制jar包到app目录下
进入app目录编写Dockerfile

```bash
vim Dockerfile
```
写入以下内容

```bash
# Docker image for hgnuman
# VERSION 1.3.0
# Author: kaygb
# 基础镜像使用openjdk11
FROM openjdk:11
# 作者
MAINTAINER kaygb <hi@kezez.com>
# VOLUME 指定临时文件目录为/tmp。
VOLUME /tmp
# 将jar包添加到容器中并更名为app.jar
ADD hgnuman-1.3.0-RELEASE.jar /opt/hgnuman/app.jar
RUN mkdir /opt/hgnuman/upload-files
RUN mkdir /opt/hgnuman/export
RUN mkdir /opt/hgnuman/import
# 运行jar包
RUN bash -c 'touch /opt/hgnuman/app.jar'
ENTRYPOINT ["java","-jar","/opt/hgnuman/app.jar","--server.port=8036",">>","/opt/hgnuman/log/hgnuman.log","2>&1","&"]
```
保存后构建容器镜像

```bash
sudo docker build -t hgnuman .
```

启动容器

```bash
sudo docker run -d -v /opt/hgnuman/files:/opt/hgnuman --net=host --privileged=true hgnuman
```

> 注意：如容器没有正常运行，请确认app.jar 在`/opt/hgnuman/files`中是否存在

更新系统（更新jar包）

```bash
sudo docker ps -a // 查看所有容器以及容器ID
sudo docker stop xxxxx(容器id） // 停止容器
sudo rm -r app.jar  // 删除旧包（或修改文件名称）
// 上传新的jar包

sudo docker start xxxxx(容器id)启动容器，更新完成。
```

> 查看日志命令：sudo docker logs hgnuman 


## 反馈

请查看关于页面。


> 最后更新时间：2022-01-10
