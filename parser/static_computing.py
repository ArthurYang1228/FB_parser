import FB_parser
import math
import os

class static_computing:
    def __init__(self, x ,y):

        self.x = x
        self.y = y

    def mean(self, x):
        return sum(x) / len(x)

    def de_mean(self, x):
        x_bar = self.mean(x)
        return [x_i - x_bar for x_i in x]

    def variance(self, x):
        deviations = self.de_mean(x)
        variance_x = 0
        for d in deviations:
            variance_x += d ** 2
        variance_x /= len(x)
        return variance_x

    def dot(self, x, y):
        dot_product = sum(v_i * w_i for v_i, w_i in zip(x, y))
        dot_product /= (len(x))
        return dot_product

    def correlation(self, x  , y):
        variance_x = self.variance(x)
        variance_y = self.variance(y)
        sd_x = math.sqrt(variance_x)
        sd_y = math.sqrt(variance_y)
        dot_xy = self.dot(self.de_mean(x), self.de_mean(y))
        return dot_xy / (sd_x * sd_y)

if __name__ == '__main__':
    token = input("please get token from https://developers.facebook.com/tools/explorer/ and enter:")
    parser = FB_parser.FB_parser(token)
    posts_number = []
    friends_number = []
    for data in parser.data:
        if data['friend_number'] != 0:
            print(data)
            friends_number.append(data['friend_number'])
            posts_number.append(data['post_number'])

    computer = static_computing(friends_number, posts_number)
    print("相關係數:" , computer.correlation(posts_number, friends_number))
    os.system("pause")