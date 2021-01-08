# -*- coding: utf-8 -*-
"""
@Author  : Looking
@Email   : 2392863668@qq.com
@Time    : 2021/1/8 20:22
"""

# 将数据加载到一个列表中
import json

import pygal

from countries import get_country_code

filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# 打印每个国家的人口数量
# print(json.dumps(pop_data, indent=2))
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

wm = pygal.maps.world.World()
wm.title = "World Population in 2010, by Country"
wm.add('2010', cc_populations)

wm.render_to_file('americas.svg')
