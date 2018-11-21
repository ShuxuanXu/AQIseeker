# AQIseeker
A simple crawler to acquire the air quality data in China from<br>
[空气质量历史数据查询](https://www.aqistudy.cn/historydata/daydata.php)

## Dependency
<code>requests-html</code>

Install <code>requests-html</code> by using<br>
<code>pip install requests-html</code>

## How to use
### Acquire the data
<p>Import the crawler class<br>
<code>from crawler import AQIcrawler</code></p>

<p>
Acquire the data from the website<br>
    <code>this_page = AQIseeker('南京', '201703', 5) # '5' maximum request attempts (default=5)</code><br>
    <code>this_page.getData()</code><br>
    <code>this_page.metadict # access the dict that holds the data</code><br>
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
The parser will return a dictionary containing the city names (as indice) and the month list.
</p>