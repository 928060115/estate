# -*- coding:utf-8 -*-
"""
  @author:ly
  @file: db_service.py
  @time: 2018/9/1316:10
  @version: v1.0
  @Dec: 连接数据库
"""
from base.model.db_account import DbAccount
from base.types.environment import Environment

db_info = {
    Environment.DEV:DbAccount('127.0.0.1','root','123456'),
    Environment.PRO:DbAccount('')
}

def get_session(env=Environment.DEV):
    session = db_info[env].session()
    return session