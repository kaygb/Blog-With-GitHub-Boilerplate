---
layout: post
title: C语言中的break和continue
slug: 20200301-C-break-and-continue
date: 2020-03-01 17:11
status: publish
author: 风也
categories: 
  - 编程笔记
  - C语言
tags: 
  - C语言
  - break
  - continue
excerpt: 
---

## break

在循环语句中的意思是，循环到了这一轮满足了条件，就执行break跳出循环，即满足之后不再继续执行这个循环
### 实例

~~~c
#include <stdio.h>
int main()
{
int a = 10;

    for ( int i = 0; i < a; i++)
    {
        /* code */
        if (i == 5)
        {
            /* code */
            printf("break\n");
            break;
        }
        printf("i=%d\n",i);
        
    }
}

~~~
输出：
![](./images/Snipaste_2020-03-01_17-19-49.png)

## continue

循环到这一伦满足了条件，则这一轮不执行。

### 实例

~~~c
#include <stdio.h>
int main()
{
    int a = 10;

    for ( int i = 0; i < a; i++)
    {
        /* code */
        if (i == 5)
        {
            continue;
        }
        printf("i=%d\n",i);
        
    }

}
~~~

输出：
![](./images/Snipaste_2020-03-01_17-25-47.png)

## 关系
![](images/Snipaste_2020-03-01_17-38-08.png)