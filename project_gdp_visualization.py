# coding:utf-8
"""
综合项目:世行历史数据基本分类及其可视化
作者：付子萌
日期：2021/1/13
"""

import csv
import math
import pygal
import pygal_maps_world  # 导入需要使用的库


def read_csv_as_nested_dict(filename, keyfield, separator, quote):  # 读取原始csv文件的数据，格式为嵌套字典
    result = {}
    with open(filename, newline="")as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        for row in csvreader:
            rowid = row[keyfield]
            result[rowid] = row

    return result


pygal_countries = pygal.maps.world.COUNTRIES  # 读取pygal.maps.world中国家代码信息（为字典格式），其中键为pygal中各国代码，值为对应的具体国名(建议将其显示在屏幕上了解具体格式和数据内容）
gdp_countries = read_csv_as_nested_dict("isp_gdp.csv", "Country Name", ",", '"')#打开csv文件，以国家名为外层字典的键，，为分隔符，''为引用符


def reconcile_countries_by_name(plot_countries, gdp_countries):  # 返回在世行有GDP数据的绘图库国家代码字典，以及没有世行GDP数据的国家代码集合
    dict1 = {}#
    set1 = set()
    for i in plot_countries:
        country_name = plot_countries[i]
        result = country_name in gdp_countries
        if result == True:
            dict1[i] = country_name#如果世行中有该国家GDP数据，就写入字典
        if result == False:
            set1.add(i)#如果没有该国GDP数据，就写入集合
    tuple1 = (dict1, set1)#将列表和集合包括进一个元组中
    return tuple1


def build_map_dict_by_name(gdpinfo, plot_countries, year):
    tuple1 = reconcile_countries_by_name(plot_countries, gdp_countries)
    dict1 = tuple1[0]
    set1 = tuple1[1]
    set2 = set()
    dict2 = {}
    for i in dict1:
        countryname = dict1[i]
        dict3 = gdp_countries[countryname]
        value1 = dict3[year]
        if value1 == "":
            set2.add(i)
        else:
            value1 = float(value1)
            value1 = math.log10(value1)#为显示方便，利用math库进行转换对数格式
            dict2[i] = value1#导入各具体年份的GDP数据，键为国家代码，值为具体年份所对应的GDP数据
    tuple2 = (dict2, set1, set2)
    return (tuple2)


def render_world_map(gdpinfo, plot_countries, year, map_file):  # 将具体某年世界各国的GDP数据(包括缺少GDP数据以及只是在该年缺少GDP数据的国家)以地图形式可视化
    tuple2 = build_map_dict_by_name(gdpinfo, plot_countries, year)
    dict3 = tuple2[0]
    set1 = tuple2[1]
    set2 = tuple2[2]
    gdp_world_map = pygal.maps.world.World()
    gdp_world_map.title = "全球GDP分布图"
    gdp_world_map.add(year, dict3)
    gdp_world_map.add("missing from world bank", set1)
    gdp_world_map.add("no data at this year", set2)
    gdp_world_map.render_to_file(map_file)


def test_render_world_map(year):  # 测试函数
    """
    对各功能函数进行测试
    """
    gdpinfo = {
        "gdpfile": "isp_gdp.csv",
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2015,#限制范围为1960-2015年间
        "country_name": "Country Name",
        "country_code": "Country Code"#将国家代码与国家名字相对应
    }  # 定义数据字典

    pygal_countries = pygal.maps.world.COUNTRIES  # 获得绘图库pygal国家代码字典
    render_world_map(gdpinfo, pygal_countries, year, "qqisp_gdp_world_name_具体年份.svg")#生成查询年份的svg文件


print("欢迎使用世行GDP数据可视化查询")
print("----------------------")
year = input("请输入需查询的具体年份:")
test_render_world_map(year)