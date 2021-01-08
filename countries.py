# -*- coding: utf-8 -*-
"""
@Author  : Looking
@Email   : 2392863668@qq.com
@Time    : 2021/1/8 20:38
"""
# pip install pygal_maps_world
from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):
    """返回指定国家的国别码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None

