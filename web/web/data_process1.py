#coding:utf-8
import json
with open('/Users/zhangguoci/PycharmProjects/web/static/高性能计算_张文硕.txt','r') as f:
    line = f.readlines()
    name = [];nummber = []
    for i in range(len(line)):
        name.append(str(line[i].decode('gb2312')[0:3]))
        nummber.append(str(line[i].decode('gb2312')[3:]))
    name = name[1:];nummber = nummber[1:]
    json_name = json.dumps(name)
    json_nummber = json.dumps(nummber)
    datas = [dict(name=name[i],value=nummber[i]) for i in range(len(name))]
    json_datas = json.dumps(datas)