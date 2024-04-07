import argparse
import numpy as np
from sympy.solvers import solve
from sympy import Symbol, Poly
import itertools
import operator
import matplotlib.pyplot as plt
from sklearn import datasets

class linear_regression():

    def __init__(self, x, y):
        super(linear_regression, self).__init__()
        self.x = x
        self.y = y
        
        self.mean_x, self.mean_y = self.mean()
        print(self.ll())
    
    def mean(self):
        x_ = list(itertools.accumulate(self.x, operator.add))[len(self.x) - 1]/len(self.x) 
        y_ = list(itertools.accumulate(self.y, operator.add))[len(self.y) - 1]/len(self.y)
        return x_, y_

    def Sxy(self):
        ans = 0
        for i in range(len(self.x)):
            ans += (self.x[i] - self.mean_x)*(self.y[i] - self.mean_y)

        return ans

    def Sxx(self):
        ans = 0
        for i in range(len(self.x)):
            ans += (self.x[i] - self.mean_x) ** 2
        return ans

    def calculate_a(self):
        return self.mean_y - self.calculate_b()*self.mean_x

    def calculate_b(self):
        return self.Sxy()/self.Sxx()
    
    def ll(self):
        x = Symbol('x')
        return Poly(self.calculate_a() + self.calculate_b()*x, x)
    
    def return_a_b(self):
        return self.calculate_a(), self.calculate_b()

    def predict(self, val):
        return self.calculate_a() + self.calculate_b() * val


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument("--view", help="show results", type=int)
    opt = parser.parse_args()
    return opt

if __name__ == "__main__":
    opt = parse_opt()
    x = [56, 75, 61, 61, 67, 72, 62, 61]
    y = [21, 39, 34, 21, 32, 24, 29, 24]
    ll = linear_regression(x, y)
    if opt.view == 1:
        plt.figure()
        plt.scatter(x ,y)
        a, b = ll.return_a_b()
        x = np.linspace(0, 24, num = 24)
        fx = []
        for i in range(len(x)):
            fx.append(a + b*i)
        print(fx)
        plt.plot(x, fx)
        plt.grid()
        plt.show()
    else:
        a, b = ll.return_a_b()
        x = Symbol('x')
        print(Poly(a + b*x, x))

    


