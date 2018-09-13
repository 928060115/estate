# -*- coding:utf-8 -*-
"""
  @author:ly
  @file: environment.py
  @time: 2018/9/1316:13
  @version: v1.0
  @Dec: 
"""

from enum import unique, Enum

@unique
class Environment(Enum):
    DEV = 0,
    PRO = 1
