# -*- coding: utf-8 -*-
"""
@Author  : Looking
@Email   : 2392863668@qq.com
@Time    : 2021/1/8 20:22
"""

# 将数据加载到一个列表中
import json

from countries import get_country_code

filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# 打印每个国家的人口数量
# print(json.dumps(pop_data, indent=2))
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            print(code + "：" + str(population))
        else:
            print("ERROR - " + country_name)
