import cvxpy as cp
import numpy as np
import time

def opt(path, n, p):
    f=open(path)
    lmbda = cp.Variable(100)
    prices = np.array([])
    c = np.array([])
    C_matrix = np.array([])
    C2 = np.array([])
    C1 = np.array([])
    C0 = np.array([])
    w = cp.Variable((n))
    w1 = np.ones(n)/n
    MA_list = np.array([])
    smoo_0 = 0

    for i in range(n + p - 1 ):
        prices = np.append(prices, float(f.readline().split(",")[4]))  # .split(",")[4]

    for i in range(p):
        c = np.append(c, prices[n - 1 + i])
        C_matrix = np.append(C_matrix, prices[i:i + n])
        if i >= 2 and i <= p - 1:
            C2 = np.append(C2, prices[i:i + n])
        if i >= 1 and i <= p - 2:
            C1 = np.append(C1, prices[i:i + n])
        if i >= 0 and i <= p - 3:
            C0 = np.append(C0, prices[i:i + n])
    C_matrix = np.reshape(C_matrix, (p, n))
    C2 = np.reshape(C2, (p - 2, n))
    C1 = np.reshape(C1, (p - 2, n))
    C0 = np.reshape(C0, (p - 2, n))
    dC = (C2 - 2 * C1 + C0)
    error = cp.norm((C_matrix @ w) - c, 1) / p  # conv
    smoo = cp.norm(dC @ w, 1) / (p - 2)  # conv

    for i in range(n - 1, p + n - 1):
        MA_list = np.append(MA_list, np.dot(prices[i - n + 1:i + 1], w1))

    for i in range(2, len(MA_list)):
        smoo_0 += abs(MA_list[i] - 2 * MA_list[i - 1] + MA_list[i - 2])

    smoo_0 /= (p - 2)
    constr = [smoo <= smoo_0]
    prob = cp.Problem(cp.Minimize(error),constr)
    prob.solve()
    return w.value

#w = opt("C:\\Users\\hrvoj\\OneDrive\\Radna površina\\LAFRA\\futures-active_adjusted_1min_qucz81\\BTC_continuous_adjusted_1min.txt",50,7200)

#33-34 s!!!