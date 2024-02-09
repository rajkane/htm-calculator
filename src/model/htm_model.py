"""
homogeneous transformation
@author: Daniel Torac
@year: 2024
"""

import math


class HomogeneousTransformation:
    """
    class HomogeneousTransformation
    """

    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__z = 0
        self.__alpha = 0
        self.__beta = 0
        self.__gamma = 0
        self.__x_delta = 0
        self.__y_delta = 0
        self.__z_delta = 0

    def set_point(self, x: float, y: float, z: float):
        """
        method setter set point in space

        :param x:
        :param y:
        :param z:

        """
        self.__x = x
        self.__y = y
        self.__z = z

    def set_transform_matrix(self, alpha: float, beta: float, gamma: float, x_delta: float, y_delta: float,
                             z_delta: float):
        """
        method setter set transform matrix

        :param alpha:
        :param beta:
        :param gamma:
        :param x_delta:
        :param y_delta:
        :param z_delta:

        """
        self.__alpha = alpha
        self.__beta = beta
        self.__gamma = gamma
        self.__x_delta = x_delta
        self.__y_delta = y_delta
        self.__z_delta = z_delta

    def __get_transform_matrix(self) -> list[list[float]]:
        """
        method getter get transform matrix

        :return: matrix
        """
        x_rot = [
            [1, 0, 0, self.__x_delta],
            [0, math.cos(math.radians(self.__alpha)), -math.sin(math.radians(self.__alpha)), self.__y_delta],
            [0, math.sin(math.radians(self.__alpha)), math.cos(math.radians(self.__alpha)), self.__z_delta],
            [0, 0, 0, 1]
        ]
        y_rot = [
            [math.cos(math.radians(self.__beta)), 0, math.sin(math.radians(self.__beta)), self.__x_delta],
            [0, 1, 0, self.__y_delta],
            [-math.sin(math.radians(self.__beta)), 0, math.cos(math.radians(self.__beta)), self.__z_delta],
            [0, 0, 0, 1]
        ]
        z_rot = [
            [math.cos(math.radians(self.__gamma)), -math.sin(math.radians(self.__gamma)), 0, self.__x_delta],
            [math.sin(math.radians(self.__gamma)), math.cos(math.radians(self.__gamma)), 0, self.__y_delta],
            [0, 0, 1, self.__z_delta],
            [0, 0, 0, 1]
        ]

        rot = []
        for i in range(3):
            for j in range(3):
                rot.append(x_rot[i][j] * y_rot[i][j] * z_rot[i][j])

        matrix = [
            [rot[0], rot[1], rot[2], self.__x_delta],
            [rot[3], rot[4], rot[5], self.__y_delta],
            [rot[6], rot[7], rot[8], self.__z_delta]
        ]

        return matrix

    def __get_point(self) -> list[float]:
        """
        method getter get point

        :return: [x, y, z, 1]
        """
        return [self.__x, self.__y, self.__z, 1]

    def get_result(self) -> list[float]:
        """
        method getter result

        :return: [x, y, z]
        """
        p = self.__get_point()

        tm = self.__get_transform_matrix()

        x = round(tm[0][0] * p[0] + tm[0][1] * p[1] + tm[0][2] * p[2] + tm[0][3] * p[3], 1)
        y = round(tm[1][0] * p[0] + tm[1][1] * p[1] + tm[1][2] * p[2] + tm[1][3] * p[3], 1)
        z = round(tm[2][0] * p[0] + tm[2][1] * p[1] + tm[2][2] * p[2] + tm[2][3] * p[3], 1)

        return [x, y, z]


"""if __name__ == "__main__":
    ht = HomogeneousTransformation()
    ht.set_point(x=280, y=350, z=400)
    ht.set_transform_matrix(
        alpha=0,
        beta=0,
        gamma=180,
        x_delta=0,
        y_delta=1280,
        z_delta=0
    )
    result = ht.get_result()
    print(result)"""
