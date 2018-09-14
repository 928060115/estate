# -*- coding:utf-8 -*-
"""
  @author:ly
  @file: table_model.py
  @time: 2018/9/1314:54
  @version: v1.0
  @Dec: 表字段
"""

from sqlalchemy import Column,Integer,String,DateTime
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
base = declarative_base()

class City(base):
    '''
    地产城市表
    '''

    __tablename__ = 't_city'

    # 表字段
    id = Column(Integer,primary_key=True)
    city_province = Column(String,default='')
    city_name = Column(String,default='')
    href = Column(String,default='')
    data_source = Column(String,default='')
