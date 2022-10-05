def grad(x):
    return (x**2) - 1


def cost(x):
    return (1/3)*(x**3)-x


def myGD1(eta, x0):
                   x = [x0]
                   for it in range(100):
                                  x_new = x[-1] - eta*grad(x[-1])
                                  if abs(grad(x_new)) < 1e-3:
                                                 break
                                  x.append(x_new)
                   return (x, it)

(x1, it1) = myGD1(.1,.12 )
(x2, it2) = myGD1(-.33, .1)
print('Solution x1 = %f, cost = %f, obtained after %d iterations'%(x1[-1], cost(x1[-1]), it1))
print('Solution x2 = %f, cost = %f, obtained after %d iterations'%(x2[-1], cost(x2[-1]), it2))
