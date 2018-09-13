# -*- coding:utf-8 -*-
"""
  @author:ly
  @file: tools.py
  @time: 2018/9/1316:21
  @version: v1.0
  @Dec: 工具类
"""
import argparse
import random
from os import path
from base.types.environment import Environment


class Tools():

    def __init__(self):
        self.__user_agents = [
            'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
            'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
            'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;',
            'Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)',
            'Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11',
            'Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11'
        ]

    def get_save_data_path(self, name=None):
        data_path = self.get_data_path()
        tmp_path = path.join(data_path, 'estate')

        if not name:
            return tmp_path
        return path.join(data_path, name)

    def get_data_path(self):
        home_path = path.expanduser('~')
        return path.join(home_path, 'data')

    def get_environment(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-e', type=str, default='dev', help='运行环境')
        parser.add_argument('-s', type=int, default=0, help='抓取数据开始index')
        parser.add_argument('-f', type=bool, default=False, help='是否抓取所有城市地产信息')
        env, unparsed = parser.parse_known_args()

        runtime_env = None
        if env.e == 'pro':
            runtime_env = Environment.PRO
        else:
            runtime_env = Environment.DEV

        return runtime_env, env.s, env.f

    def get_random_agent(self):
        last_index = len(self.__user_agents) - 1
        return self.__user_agents[random.randint(0, last_index)]
