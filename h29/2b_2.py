#! usr/bin/env python
# -*- coding: utf-8 -*-

u = 0.25
def main():
    w = [0.125, 0.125, 0.25]
    o = [0, 0, 0, 0]
    xs = [[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]]
    ys = [-1, -1, -1, 1]
    while o != ys:
        for j in [0, 1, 2, 3]:
            o[j] = predict(w, xs[j])
            if o[j] != ys[j]:
                w = update(w, xs[j], ys[j])
        print(o)
    print(w)

def update(w, x, y):
    for i in range(len(w)):
        w[i] = w[i] + u * x[i] * y

    return w

def sum(f, a, b):
    if a > b:
        return 0
    else:
        return (f(a) + sum(f, a+1, b))

def predict(w, t):
    def product(i):
        return w[i] * t[i]

    a = sum(product, 0, len(w)-1)

    if a >= 0:
        return 1
    else:
        return -1

main()
