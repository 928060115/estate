# -*- coding:utf-8 -*-
"""
  @author:ly
  @file: estate_city.py
  @time: 2018/9/1317:05
  @version: v1.0
  @Dec: 获取所有链家城市信息
"""

from base.service.base_service import BaseService
from base.utils.tools import Tools
import os
from base.types.environment import Environment
from bs4 import BeautifulSoup


class EstateCitys(BaseService):
    __LIANJIA_CITY_URL = 'https://bj.lianjia.com/city/'

    def __init__(self, env):
        BaseService.__init__(self,env)

        page_home_path = Tools().get_save_data_path('estate')
        self.__data_path = os.path.join(page_home_path, 'city')
        if not os.path.exists(self.__data_path):
            os.makedirs(self.__data_path)

    def start(self):
        file_name = 'city.html'
        file_path = os.path.join(self.__data_path, file_name)
        source = None
        if os.path.exists(file_path):
            source = self._read(file_path)
        else:
            url = self.__LIANJIA_CITY_URL
            source = self._request(url=url)
            self._save(file_path, source)
        # self._parse(source)

    # def _parse(self,source):
    #     soup = BeautifulSoup.
    def test(self):
        url = self.__LIANJIA_CITY_URL
        print(self._request(url=url))

if __name__ == '__main__':
    EstateCitys(Environment.DEV).start()
