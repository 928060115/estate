# -*- coding:utf-8 -*-
"""
  @author:ly
  @file: db_account.py
  @time: 2018/9/1314:40
  @version: v1.0
  @Dec: 数据库帐号配置及连接
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DbAccount():
    __session = None

    def __init__(self, host, name='root', password='P@ssw0rd', port=3306, db_name='db_estate'):
        self.host = host
        self.name = name
        self.password = password
        self.port = port
        self.db_name = db_name

    def session(self):
        if self.__session:
            return self.__session

        url = 'mysql+mysqlconnector://%s:%s@%s:%d/%s?charset=utf8&auth_plugin=mysql_native_password' % (self.name, self.password, self.host, self.port, self.db_name)
        engine = create_engine(url,echo=True,encoding='utf8')
        DBSession = sessionmaker(bind=engine)

        self.__session = DBSession()

        return self.__session