#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# название программы DoubleSin
import math
import numpy
import matplotlib.pyplot as mpp
# импортируем модули

if __name__ == '__main__': 
    arguments = numpy.r_[0:200:0.1] # создаем массив аргументов
    mpp.plot(
        arguments, # передаем аргументы
        [math.sin(a) * math.sin(a/20.0) for a in arguments] # создаем и передаем массив значений 
    )
    mpp.show() # показываем график
