import matplotlib.pyplot as plt


def linear_regression(data):
    sx,sy,sxx,sxy=0,0,0,0
    for x,y in data:
        sx+=x
        sy+=y
        sxx+=x*x
        sxy+=x*y
    n=len(data)
    b=(n*sxy-sx*sy)/(n*sxx-sx*sx)
    a=(sy-b*sx)/n
    return a,b

def plot(data,a,b):
    for x,y in data:
        plt.scatter(x,y,color='blue')
    l=min(data,key=lambda x:x[0])[0]
    r=max(data,key=lambda x:x[0])[0]
    plt.plot([l,r],[a*l+b,a*r+b],color='green')
    plt.title(F'Linear Regression with y={a:.3f}x+{b:.3f}')
    plt.show()
        



if __name__ == '__main__':
    data=[(5,40) , (7,120) , (12,180), (16,210), (20,240)]
    a,b=linear_regression(data)
    plot(data,a,b)