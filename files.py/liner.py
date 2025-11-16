import numpy as np

V = 39
eps = V * 0.0001  # 0.0039

a1 = (V+1)/2
b1 = (V+2)/4
c1 = (V+3)/5

a2 = (V+2)/5
b2 = (V+3)/3
c2 = (V+5)/4


def F(vec):
    x, y = vec
    return np.array([a1*x*x + b1*y*y - c1*x*y - V,
                     a2*x*x + b2*y*y + c2*x*y - V], dtype=float)


def J(vec):
    x, y = vec
    return np.array([[2*a1*x - c1*y,  2*b1*y - c1*x],
                     [2*a2*x + c2*y,  2*b2*y + c2*x]], dtype=float)


def newton(x0, eps=1e-3, maxiter=50):
    x = np.array(x0, dtype=float)
    for k in range(maxiter):
        Fx = F(x)
        normF = np.linalg.norm(Fx)
        print(f"k={k}, x={x}, ||F||={normF:.6g}")
        if normF < eps:
            break
        s = np.linalg.solve(J(x), -Fx)
        x = x + s
    return x


root = newton((1.0, 1.0), eps=eps)
print("Root approx:", root)
print("F(root):", F(root))
