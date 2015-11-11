#! /usr/bin/env python
# -*- coding: utf-8 -*-

# ZADANIE: wykonaj wykres funkcji f(x), gdzie x = <-10;10> z krokiem 0.5
# f(x) = x/-3 + a dla x <= 0
# f(x) = x*x/3 dla x >= 0

import pylab

x = pylab.arange(-10, 10.5, 0.5)  # lista argumentów x
a = int(raw_input("Podaj współczynnik a: "))
y1 = [i / -3 + a for i in x if i <= 0]

pylab.plot(x, y1)
pylab.title('Wykres f(x)')
pylab.grid(True)
pylab.show()