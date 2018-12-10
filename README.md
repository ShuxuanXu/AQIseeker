# AQIseeker
A simple objectified crawler to acquire the air quality data in China from<br>
[空气质量历史数据查询](https://www.aqistudy.cn/historydata/daydata.php)<br>
An objectfied crawler enables users to acquire AQI data in a free way and couple the crawler into users' own codes<br>

## Dependency
<code>requests-html</code>

Install <code>requests-html</code> by using<br>
<code>pip install requests-html</code>

## How to use
### Acquire the data
<p>Import the crawler class<br>
<code>from crawler import AQIseeker</code></p>

<p>
Acquire the data from the website<br>
    <code>this_page = AQIseeker('南京', '201703', 5) # '5' maximum request attempts (default=5)</code><br>
    <code>this_page.getData()</code><br>
    <code>this_page.metadict # access the dict that holds the data</code><br>
    <code># Note that one crawler instance can only retrieve the data of ONE specified city in ONE given month
</p>


### Acquire the data of multiple cities and months
<p>The crawler class accepts any valid input and attempts to get the data from the website. Though the user is totally free to call the class in their own ways, a simple parser is provided to handle such demand</p>

<p>
Create a text file 'some_cities.txt' to hold some contents like below<br>
    <code>南京 201701-201706</code><br>
    <code>上海 201609-201703</code><br>
    <code>北京 201610-201705</code><br>
the format should be
    <code>city_name yyyymm-yyyymm</code><br>
</p>

<p>
Import a parser<br>
    <code>from setting_parser import getCityTime</code><br>
    <code>city_time_dict = getCityTime('some_cities.txt') # return a dict</code><br>
The parser will return a dictionary containing the city names (as indice) and the month list. Please refer to 'example_front.py' for the usage of the parser and the crawler
</p>

### Planned update
- [x] Base class of the crawler
- [x] A parser for formatted txt file
- [ ] Language support of city names in English
- [ ] Provide an alternative method to acquire data from multiple cities and months from a dict/str
- [ ] Improve the performance by introducing parellel operation

---古老语言的分割线---<br>

# 介绍： AQIseeker
一个简单的对象化爬虫，用于从以下网页爬取空气质量数据<br>
[空气质量历史数据查询](https://www.aqistudy.cn/historydata/daydata.php)<br>
对象化的爬虫允许用户更自由地获取特定城市和时间的空气质量数据，并且更方便插入用户自己的代码<br>

## 依赖
<code>requests-html</code>

安装 <code>requests-html</code><br>
<code>pip install requests-html</code>

## 使用方法
### 获取数据
<p>import爬虫的类<br>
<code>from crawler import AQIseeker</code></p>

<p>
从网站获取数据<br>
    <code>this_page = AQIseeker('南京', '201703', 5) # '5' 最大请求次数 (默认=5)</code><br>
    <code>this_page.getData()</code><br>
    <code>this_page.metadict # 获取的数据会存放在字典metadict中</code><br>
</p>


### 获取多个城市和时间的数据
<p>只要是符合格式的城市名和时间表达式，该爬虫都可以处理。用户可以根据自己的需求请求多个数据，也可以使用此处提供的固定文本格式和文本处理工具一次性定义多个城市和时间</p>

<p>
创建一个txt文件'some_cities.txt'（文件名可以随意），文件中的内容如下 <br>
    <code>南京 201701-201706</code><br>
    <code>上海 201609-201703</code><br>
    <code>北京 201610-201705</code><br>
文本格式应为
    <code>city_name yyyymm-yyyymm</code><br>
</p>

<p>
import提供的文本处理工具<br>
    <code>from setting_parser import getCityTime</code><br>
    <code>city_time_dict = getCityTime('some_cities.txt') # 返回一个字典</code><br>
该工具会返回一个包含城市名（作为keys）和月份列表（作为values）的字典，之后可以使用爬虫来获取数据。可以参考'example_front.py'
</p>

### 计划更新
- [x] 本爬虫的基础类
- [x] 格式化文本的处理工具， 用于批量获取数据
- [ ] 对中文城市名的英语支持
- [ ] 允许从字典/字符串获取多个城市/月份的数据
- [ ] 使用平行操作改善爬虫性能