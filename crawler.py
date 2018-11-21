# coding=utf-8

# Author: Shuxuan Xu <shuxuan.xu@postgrad.manchester.ac.uk>

import time
import os

import requests_html
import numpy
import pandas

# fixed website;
# variable cities and times
class AQIcrawler():
    """
    class AQIcrawler(city, yyyymm, max_request=3)

    This tool is used to extract the AQI and relevant data from:
    https://www.aqistudy.cn/historydata/daydata.php

    Parameters:
    ----------
    'city': [str] the name of a city, in Chinese
    'yyyymm': [str] the year and the month. For instance, '201705' means May, 2017
    'max_request': the max attempts of the network requests sent by the crawler. Default is 3
    
    Attributes:
    ----------
    'AQIcrawer.URL': the target URL, according to the given city name and time
    'AQIcrawler.metadict': a dict to store the extracted data
    
    Methods:
    ----------
    'AQIcrawer.getRenderedPage()': return the rendered page
    'AQIcrawer.getData()': render the page and store the data in the metadict
    'AQIcrawer.write2csv(outputDir)': write the metadict to a csv file to the specified directory
    
    Example:
    ----------
    >>> this_page = AQIcrawler('南京', '201703', 5)
    >>> this_page.getData()
    >>> this_page.metadict

    {'AQI': [...],
    'CO': [...],
    'Date': [...],
    'Level': [...],
    'NO2': [...],
    'O3_8h': [...],
    'PM10': [...],
    'PM2.5': [...],
    'SO2': [...]}
    """
    _headers = [
        'Date',
        'AQI',
        'Level',
        'PM2.5',
        'PM10',
        'SO2',
        'CO',
        'NO2',
        'O3_8h'
        ]
    _domain = 'https://www.aqistudy.cn/historydata/daydata.php'

    def __init__(self, city, yyyymm, max_request=5):
        self.city = city
        self.yyyymm = yyyymm
        self.URL = self._domain + '?city=%s&month=%s' %(city, yyyymm) # get the URL of current city and month
        self.metadict = {header:[] for header in self._headers} # a dict to hold the extracted data
        self.max_request = max_request
        self.__requested = False # flag to log whether the request has been attempted
    

    def __isVoid(self):
        # check if the meta dict is empty
        length_array = [len(self.metadict[header]) for header in self._headers]
        length_array = numpy.asarray(length_array)
        isZero = length_array == 0
        if False in isZero:
            isVoid = False
        else:
            isVoid = True
        return isVoid


    def getRenderedPage(self):
        current_session = requests_html.HTMLSession()
        current_page = current_session.get(self.URL)
        current_page.html.render()
        time.sleep(0.5) # freeze for 0.5 sec to prevent from being turned down by the server
        return current_page


    def getData(self):
        current_request = 0
        while current_request < self.max_request and self.__isVoid() == True:
            current_request += 1
            print('Requesting attempts: %i/%i' %(current_request, self.max_request))
            rendered_page = self.getRenderedPage()
            table_objects = rendered_page.html.find('td') # search the table data tagged with 'td'
            days = len(table_objects) // 9
            for d in range(days):
                self.metadict['Date'].append(table_objects[d*9].text) # get date
                self.metadict['AQI'].append(table_objects[d*9+1].text) # get AQI
                self.metadict['Level'].append(table_objects[d*9+2].text) # get level
                self.metadict['PM2.5'].append(table_objects[d*9+3].text) # get PM2.5
                self.metadict['PM10'].append(table_objects[d*9+4].text) # get PM10
                self.metadict['SO2'].append(table_objects[d*9+5].text) # get SO2
                self.metadict['CO'].append(table_objects[d*9+6].text) # get CO
                self.metadict['NO2'].append(table_objects[d*9+7].text) # get NO2
                self.metadict['O3_8h'].append(table_objects[d*9+8].text) # get O3_8h
        self.__requested = True
        if current_request == self.max_request and self.__isVoid() == True:
            print('Request attempts reached the maximum setting yet no data presents')


    def write2csv(self, outputDir):
        if self.__requested == False:
            raise Exception('Request not sent yet')
        else:
            to_be_written = [self.metadict[header] for header in self._headers] # a 2d list
            to_be_written = numpy.asarray(to_be_written).T
            data_frame = pandas.DataFrame(to_be_written, columns=self._headers)
            csv_name = '%s_%s.csv' %(self.city, self.yyyymm) # generate a unique file name for the data
            data_frame.to_csv(os.path.join(outputDir, csv_name)) # write to csv
