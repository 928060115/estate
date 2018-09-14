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
from lxml import etree
from bs4 import BeautifulSoup
from base.model.table_model import City


class EstateCitys(BaseService):
    __LIANJIA_CITY_URL = 'https://bj.lianjia.com/city/'

    def __init__(self, env):
        BaseService.__init__(self, env)

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
        self._parse_bybs4(source)

    def _parse(self, source):
        html = etree.HTML(source,parser=etree.HTMLParser(encoding='utf-8'))
        elements = html.xpath('.//*[@class="city_list_li city_list_li_selected"]')
        if not elements:
            return

        for element in elements:
            self._parse_element(element)

    def _parse_element(self, element):
        city = City()
        city.data_source = 'lianjia'
        city.city_province = element.xpath('.//div[@class="city_list_tit c_b"]/text()')[0].strip()
        citys = element.xpath('.//div[@class="city_province"]/ul/li')
        if not citys:
            return
        for item in citys:
            city.href = item.xpath('.//a/@href')[0]
            city.city_name = item.xpath('.//a/text()')[0].strip()
            self._save(city)

    def _parse_bybs4(self,source):
        soup = BeautifulSoup(source,'lxml',from_encoding='utf8')
        elements = soup.find_all('li',class_='city_list_li city_list_li_selected')
        if not elements:
            return

        for element in elements:
            self._parse_element_bybs4(element)

    def _parse_element_bybs4(self,element):
        data_source = 'lianjia'
        city_province = element.find('div',class_='city_list_tit c_b').get_text()
        citys = element.find_all('li')
        if not citys:
            return
        for item in citys:
            city = City()
            city.data_source = data_source
            city.city_province = city_province
            city.href = item.find('a').attrs['href']
            city.city_name = item.find('a').get_text()
            self._save(city)


    def _save(self, city):
        if not city:
            return

        exist_city = self._session.query(City).filter(City.city_name == city.city_name,City.data_source == 'lianjia').first()
        if not exist_city:
            self._session.add(city)
        self._session.commit()

    def test(self):
        url = self.__LIANJIA_CITY_URL
        print(self._request(url=url))


if __name__ == '__main__':
    EstateCitys(Environment.DEV).start()
