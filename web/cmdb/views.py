# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse
from web.data_process import *
from web.data_process1 import *
# Create your views here.
def index(request):
    return render(request,'pie-simple.html',{'json_sex_data':json_sex_data})
def map(request):
    return render(request,'index.html',{'json_map_datas':json_map_datas})
def line(request):
    return render(request,'line-style.html',{'json_pre_name':json_pre_name,'json_pre_nummber':json_pre_nummber})
def za(request):
    return render(request,'1.html',{'json_year_name':json_year_name,
                                    'json_year_nummber':json_year_nummber,
                                    'json_south_data':json_south_data,
                                    'json_north_data':json_north_data,
                                    'json_area_nummber':json_area_nummber,
                                    'json_sex_data':json_sex_data,
                                    'json_pre_name':json_pre_name,
                                    'json_pre_nummber':json_pre_nummber,
                                    'json_pre_datas':json_pre_datas,
                                    'json_area_datas':json_area_datas,
                                    'json_month_datas':json_month_datas,
                                    'json_year_datas':json_year_datas,
                                    'json_nummber':json_nummber,
                                    'json_name':json_name,
                                    'json_datas':json_datas})

def a(request):
    return render(request,'3.html')

