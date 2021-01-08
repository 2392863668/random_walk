# -*- coding: utf-8 -*-
"""
@Author  : Looking
@Email   : 2392863668@qq.com
@Time    : 2021/1/8 21:06
"""
import pygal

wm = pygal.maps.world.World()
wm.title = 'North, Central, and South America'
wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe',
                         'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')

