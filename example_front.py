# coding=utf-8

# Author: Shuxuan Xu <shuxuan.xu@postgrad.manchester.ac.uk>

from crawler import AQIseeker
from setting_parser import getCityTime

# if you want to extracted the AQI data from only one city:
this_page = AQIseeker('南京', '201703')
this_page.getData()
extracted_dict = this_page.metadict # get the data dict

# Or, suppose you want to get multiple datasets of various cities and months: 
city_time = {
    '南京':['201705', '201706', '201707'], 
    '上海':['201703','201704']
    }

for city in city_time.keys():
    for month in city_time[city]:
        temp_page = AQIseeker(city, month)
        temp_page.getData()
        temp_page.write2csv('output') # write the data to csv


# if you have a formatted setting script, such as 'city_time.txt':
city_time = getCityTime('city_time.txt')