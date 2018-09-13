# -*- coding:utf-8 -*-
"""
  @author:ly
  @file: base_service.py
  @time: 2018/9/1315:06
  @version: v1.0
  @Dec: 
"""

from base.service.db_service import get_session
from base.utils.tools import Tools
import requests
import codecs
import os


class BaseService():
    _http_header = {
        'Connection': 'keep-alive',
        'Referer': '',
        'User_Agent': ''
    }

    def __init__(self, env):
        self._env = env
        self._session = get_session(env)
        self._http_header['User_Agent'] = Tools().get_random_agent()

    def _request(self, url, data=None, method='GET'):
        print('---------------开始下载页面%s' % url)
        result = None
        try:
            if method == 'POST':
                response = requests.post(url=url, data=data, headers=self._http_header)
            else:
                response = requests.get(url=url, data=data, headers=self._http_header)
            result = response.text
        except:
            response.status_code

        return result

    def _save(self,file_path,content,encoding='utf-8'):
        with codecs.open(file_path,'w',encoding) as f:
            f.write(content)

    def _read(self,file_path,encoding='utf-8'):
        if not os.path.exists(file_path):
            return None
        with codecs.open(file_path,'r',encoding) as f:
            content = f.read()
            return content

    def __del__(self):
        self._session.close()