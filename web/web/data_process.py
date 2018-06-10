#coding:utf-8
import pandas as pd
import json
import numpy as np
#男女比例
sex_file_path = '/Users/zhangguoci/PycharmProjects/web/static/男女比例饼状图.xlsx'
sex_data = pd.read_excel(sex_file_path)
def sex_hand():
    man = sex_data['人数'][0]
    woman = sex_data['人数'][1]
    sex_dict = {}
    sex_dict['男'] = str(man)
    sex_dict['女'] = str(woman)
    sex_datas = [dict(name=key,value=value) for key,value in sex_dict.items()]
    print sex_datas
    json_sex = json.dumps(sex_datas)
    return json_sex
#专业分科
pre_file_path = '/Users/zhangguoci/PycharmProjects/web/static/专业分科+柱状图.xlsx'
def pre_hand():
    pre_data = pd.read_excel(pre_file_path)
    print pre_data.head()
    pre_name = ['哲学','经济学','法学','教育学','文学','历史学','理学','工学','农学','医学','管理学','艺术学','军事学']
    pre_nummber = []
    for i in range(len(pre_name)):
        pre_nummber.append(str(pre_data.loc[0][i]))
    pre_datas = [dict(name=pre_name[i],value=pre_nummber[i]) for i in range(len(pre_name))]
    json_pre_name = json.dumps(pre_name)
    json_pre_nummber = json.dumps(pre_nummber)
    json_pre_datas = json.dumps(pre_datas)
    return json_pre_name,json_pre_nummber,json_pre_datas
#地图分类
map_file_path = '/Users/zhangguoci/PycharmProjects/web/static/省份分布+中国地图.xlsx'
def map_hand():
    map_data = pd.read_excel(map_file_path)
    print map_data.head()
    print map_data.loc[18]
    map_dict = {}
    map_name = []
    map_nummber = []
    for i in range(len(map_data['省份'])):
        map_name.append(str(map_data.loc[i][0]))
        map_nummber.append(str(map_data.loc[i][1]))
    for i in range(len(map_name)):
        key = map_name[i]
        value = map_nummber[i]
        map_dict[key] = value
    print map_dict
    map_datas = [dict(name=key,value=value) for key,value in map_dict.items()]
    json_map_datas = json.dumps(map_datas)
    return json_map_datas
#年份
year_file_path = '/Users/zhangguoci/PycharmProjects/web/static/年份柱状图+折线图.xlsx'
def year_hand():
    year_data = pd.read_excel(year_file_path)
    print year_data.head(10)
    year_name = year_data['出生年份']
    year_name = [str(x) for x in year_name]
    print year_name
    year_nummber = year_data['人数']
    year_nummber = [str(x) for x in year_nummber]
    year_datas = [dict(name=year_name[i],value=year_nummber[i]) for i in range(len(year_name))]
    print year_nummber
    json_year_nummber = json.dumps(year_nummber)
    json_year_name = json.dumps(year_name)
    json_year_datas = json.dumps(year_datas)
    return json_year_nummber,json_year_name,json_year_datas
#月份
month_file_path = '/Users/zhangguoci/PycharmProjects/web/static/王彦君+南北方+月份+折线图.xlsx'
def month_hand():
    month_data = pd.read_excel(month_file_path)
    print month_data.head()
    north_data = list(month_data.loc[0])[1:]
    north_data = [str(x) for x in north_data]
    print north_data
    south_data = list(month_data.loc[1][1:])
    south_data = [str(x) for x in south_data]
    month_name = ['1','2','3','4','5','6','7','8','9','10','11','12']
    month_datas = [dict(name=month_name[i],value=str(int(south_data[i])+int(north_data[i]))) for i in range(len(month_name))]
    print south_data
    json_month_datas = json.dumps(month_datas)
    json_south_data = json.dumps(south_data)
    json_north_data = json.dumps(north_data)
    return json_south_data,json_north_data,json_month_datas
#地区
area_file_path = '/Users/zhangguoci/PycharmProjects/web/static/华北等区分布+饼状图.xlsx'
def area_hand():
    area_data = pd.read_excel(area_file_path)
    print area_data.head(10)
    area_name = ['华北','西北','东北','华中','华东','华南','西南']
    area_nummer = area_data['人数']
    area_nummer = [str(x) for x in list(area_nummer)]
    area_datas = [dict(name=area_name[i],value=area_nummer[i]) for i in range(len(area_name))]
    json_area_nummber = json.dumps(area_nummer)
    json_area_datas = json.dumps(area_datas)
    return json_area_nummber,json_area_datas

#执行
json_sex_data = sex_hand()
print(type(json_sex_data))
json_pre_name,json_pre_nummber,json_pre_datas = pre_hand()
print json_pre_name
json_map_datas = map_hand()
json_year_nummber,json_year_name,json_year_datas = year_hand()
json_south_data,json_north_data,json_month_datas = month_hand()
json_area_nummber,json_area_datas = area_hand()