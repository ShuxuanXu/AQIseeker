# coding=utf-8

# Author: Shuxuan Xu <shuxuan.xu@postgrad.manchester.ac.uk>

import collections

import numpy


def getAllMonths(time_tag): # take a time range tag and return a list of months
    start_tag, end_tag = time_tag.split('-') # format: 'yyyymm'
    if len(start_tag) != 6 or len(end_tag) != 6:
        raise Exception("The format of the time tag must be 'yyyymm'")
    start_tag2months = int(start_tag[:4]) * 12 + int(start_tag[4:])
    end_tag2months = int(end_tag[:4]) * 12 + int(end_tag[4:])
    total_months = end_tag2months - start_tag2months + 1
    if start_tag2months > end_tag2months:
        raise ValueError('The start time must be less than or equal to the end time')
    else:
        months = numpy.linspace(start_tag2months,end_tag2months,num=total_months, endpoint=True, dtype=int)
        yyyy = months // 12
        mm = months % 12
    months_str_list = []
    for i in range(months.size):
        if mm[i] == 0: # make sure months like '201800' replaced with '201712'
            yyyy[i] -= 1
            mm[i] = 12
        months_str = '%4i%02i' %(yyyy[i], mm[i])
        months_str_list.append(months_str)
    return months_str_list


def getCityTime(filename):
    fname = open(filename, mode='r', encoding='utf-8') # better specify encoding
    raw_text = [i.strip() for i in fname.readlines()]
    cities = [i.split()[0] for i in raw_text]
    time_tags = [i.split()[1] for i in raw_text]
    time_dict = collections.defaultdict()
    for i in range(len(cities)):
        time_dict[cities[i]] = getAllMonths(time_tags[i])
    return time_dict