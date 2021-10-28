import numpy as np
import matplotlib.pyplot as plt

def basicSimpson(f, a, b):
    step = 0.25*(b-a)
    f1, f2, f3, f4, f5 = f(a), f(a+step), f(a+2.*step), f(b-step), f(b)
    area = (b-a) * (f1+4.*f3+f5) / 6.
    error = 4. * (b-a) * abs(f1+f5-4.*(f2+f4)+6.*f3) / 45.
    return area, error

def partition(f, a, b, tolerance):
    global k, x, integralArray, errorArray
    integral, error = basicSimpson(f, a, b)
    if abs(error) > tolerance:
        midpoint = 0.5*(a+b)
        partition(f, a, midpoint, tolerance)
        partition(f, midpoint, b, tolerance)
    else:
        x[k], integralArray[k], errorArray[k] = a, integral, error
        k += 1
    return

def simpsonAdaptive(f, a, b, tolerance):
    global k, x, integralArray, errorArray
    k, x, integralArray, errorArray = 0, np.zeros(1000), np.zeros(1000), np.zeros(1000)
    partition(f,a,b,tolerance)
    x[k] = b
    print('number of intervals =', k)
    print('total integral =', sum(integralArray[0:k+1]))
    print('total error is below ', sum(errorArray[0:k+1]))
    xmesh = x[0:k+1]
    ymesh = f(xmesh)
    plt.figure()
    plt.plot(xmesh,ymesh,'ro')
    plt.plot(xmesh,ymesh-ymesh,'kx')
    xx = np.linspace(a,b,1000)
    plt.plot(xx,f(xx),'b-')
    plt.grid(True)
    plt.show()
    return

def fun(x):
    return np.sin(1/x)

simpsonAdaptive(fun, 0.01, 1, 1.e-4)
