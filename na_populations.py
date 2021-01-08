# -*- coding: utf-8 -*-
"""
@Author  : Looking
@Email   : 2392863668@qq.com
@Time    : 2021/1/8 21:16
"""

import pygal

wm = pygal.maps.world.World()
wm.title = "Populations of Countries in North America"
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

wm.render_to_file('americas.svg')
