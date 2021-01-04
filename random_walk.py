from random import choice


class RandomWalk():
    """生成随机漫步数据的类"""

    def __init__(self, num_points=5000):
        """初始化随机漫步属性"""
        self.num_points = num_points

        # 所有随机漫步都开始于 （0，0）
        self.x_values = [0]
        self.y_values = [0]
