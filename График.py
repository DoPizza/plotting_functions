import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button, Slider
#линейная функция (L) :
def lineL(a, b, x):
    """Квадратичная фукнция"""
    return (a*x+b)
def addPlotL(graph_axes, a, b):
    """Добавить график к осям"""
    x = np.linspace(-50.0, 50.0, 1000)
    y = lineL(a, b, x)
    graph_axes.plot(x, y)
    plt.draw()
def onButtonAddClickedL(event):
    ''' Обработчик события для кнопки "Добавить"'''
    global slider_a
    global slider_b
    global graph_axes
    addPlotL(graph_axes, slider_a.val, slider_b.val)
###
#квадратичная функция (K):
def lineK(a, b, c, x):
    """Квадратичная фукнция"""
    return (a*x**2 + b*x+ c)
def addPlotK(graph_axes, a, b, c):
    """Добавить график к осям"""
    x = np.linspace(-50.0, 50.0, 1000)
    y = lineK(a, b, c, x)
    graph_axes.plot(x, y)
    plt.draw()
def onButtonAddClickedK(event):
    ''' Обработчик события для кнопки "Добавить"'''
    global slider_a
    global slider_b
    global slider_c
    global graph_axes
    addPlotK(graph_axes, slider_a.val, slider_b.val, slider_c.val)
###
#модульная функция (M):
def lineM(a, b, c, x):
    """Квадратичная фукнция"""
    return (a*np.abs(x+b)+ c)
def addPlotM(graph_axes, a, b, c):
    """Добавить график к осям"""
    x = np.linspace(-50.0, 50.0, 1000)
    y = lineM(a, b, c, x)
    graph_axes.plot(x, y)
    plt.draw()
def onButtonAddClickedM(event):
    ''' Обработчик события для кнопки "Добавить"'''
    global slider_a
    global slider_b
    global slider_c
    global graph_axes
    addPlotM(graph_axes, slider_a.val, slider_b.val, slider_c.val)
###
#обратная пропорциональная функция (G):
def lineG(a, b, c, x):
    """Квадратичная фукнция"""
    return (a /(x+b)+c)
def addPlotG(graph_axes, a, b, c):
    """Добавить график к осям"""
    x = np.linspace(-50.0, 50.0, 1001)
    with np.errstate(divide='ignore', invalid='ignore'):
        y = lineG(a, b, c, x)
        graph_axes.plot(x, y)
        plt.draw()
def onButtonAddClickedG(event):
    ''' Обработчик события для кнопки "Добавить"'''
    global slider_a
    global slider_b
    global slider_c
    global graph_axes
    addPlotG(graph_axes, slider_a.val, slider_b.val, slider_c.val)
###
#корневая функция (S):
def lineS(a, b, c, x):
    """Квадратичная фукнция"""
    return (a*np.sqrt(x+b)+c)
def addPlotS(graph_axes, a, b, c):
    """Добавить график к осям"""
    x = np.linspace(-50.0, 50.0, 10001)
    with np.errstate(divide='ignore', invalid='ignore'):
        y = lineS(a, b, c, x)
        graph_axes.plot(x, y)
        plt.draw()
def onButtonAddClickedS(event):
    ''' Обработчик события для кнопки "Добавить"'''
    global slider_a
    global slider_b
    global slider_c
    global graph_axes
    addPlotS(graph_axes, slider_a.val, slider_b.val, slider_c.val)
###
#кубическая функция (C):
def lineC(a, b, c, x):
    """Квадратичная фукнция"""
    return (a*(x+b)**3 + c)
def addPlotC(graph_axes, a, b, c):
    """Добавить график к осям"""
    x = np.linspace(-50.0, 50.0, 10001)
    with np.errstate(divide='ignore', invalid='ignore'):
        y = lineC(a, b, c, x)
        graph_axes.plot(x, y)
        plt.draw()
def onButtonAddClickedC(event):
    ''' Обработчик события для кнопки "Добавить"'''
    global slider_a
    global slider_b
    global slider_c
    global graph_axes
    addPlotC(graph_axes, slider_a.val, slider_b.val, slider_c.val)
###
if __name__ == "__main__":
    # Начальные параметры графика
    current_a = 1
    current_b = 0
    current_c = 0
    # Создадим окно с графиком
    fig, graph_axes = plt.subplots(figsize=(8, 7))
    graph_axes.grid()
    plt.xlim(-9, 9)
    plt.ylim(-6, 6)
    plt.axhline(y=0, color='k')     # Ось X
    plt.axvline(x=0, color='k')     # Ось Y
    graph_axes.set_title("График")
    str = '\nУкажите значения параметров и нажмите на соответствующую формулу,'
    str += '\n после чего построиться функция.'
    graph_axes.set_xlabel("Ось x" + str)  # Добавим название оси X
    graph_axes.set_ylabel("Ось y")  # Добавим название оси Y
    # Выделим область, которую будет занимать график
    fig.subplots_adjust(left=0.07, right=0.95, top=0.95, bottom=0.4)
    # Создадим ось для кнопки "y = ax + b"
    axes_button_addL = plt.axes([0.025, 0.04, 0.15, 0.06])
    # Создадим кнопку "y = ax + b"
    button_addL = Button(axes_button_addL, '$y = ax + b$')
    button_addL.on_clicked(onButtonAddClickedL)

    # Создадим ось для кнопки "y = ax^2 + bx + c"
    axes_button_addK = plt.axes([0.185, 0.04, 0.15, 0.06])
    # Создадим кнопку "y = ax^2 + bx + c"
    button_addK = Button(axes_button_addK, '$y = a x^2+ bx+ c$')
    button_addK.on_clicked(onButtonAddClickedK)

    # Создадим ось для кнопки "y = a|x + b| + c"
    axes_button_addM = plt.axes([0.345, 0.04, 0.15, 0.06])
    # Создадим кнопку "y = a|x + b| + c"
    button_addM = Button(axes_button_addM, '$y = a|x + b| + c$')
    button_addM.on_clicked(onButtonAddClickedM)

    # Создадим ось для кнопки "y = a/(x + b) + c"
    axes_button_addG = plt.axes([0.505, 0.04, 0.15, 0.06])
    # Создадим кнопку "y = a/(x + b) + c"
    button_addG = Button(axes_button_addG, '$y = a :(x + b) + c$')
    button_addG.on_clicked(onButtonAddClickedG)

    # Создадим ось для кнопки "y = a√(x+b)+c"
    axes_button_addS = plt.axes([0.665, 0.04, 0.15, 0.06])
    # Создадим кнопку "y = a√(x+b)+c"
    button_addS = Button(axes_button_addS, '$y = a√(x+b)+c$')
    button_addS.on_clicked(onButtonAddClickedS)

    # Создадим ось для кнопки "y = a(x + b)^3 + c"
    axes_button_addC = plt.axes([0.825, 0.04, 0.15, 0.06])
    # Создадим кнопку "y = a(x + b)^3 + c"
    button_addC = Button(axes_button_addC, '$y = a(x + b)^3 + c$')
    button_addC.on_clicked(onButtonAddClickedC)

    # Создадим слайдер для задания параметра a
    axes_slider_a = plt.axes([0.05, 0.22, 0.85, 0.04])
    slider_a = Slider(axes_slider_a,
                          label='a',
                          valmin=-5.0,
                          valmax=5.0,
                          valinit=1,
                          valstep=0.5,
                          valfmt='%1.2f')
    # Создадим слайдер для задания параметра b
    axes_slider_b = plt.axes([0.05, 0.17, 0.85, 0.04])
    slider_b = Slider(axes_slider_b,
                       label='b',
                       valmin=-10.0,
                       valmax=10.0,
                       valinit=0.0,
                       valstep=0.5,
                       valfmt='%1.2f')
    # Создадим слайдер для задания параметра c
    axes_slider_c = plt.axes([0.05, 0.12, 0.85, 0.04])
    slider_c = Slider(axes_slider_c,
                       label='c',
                       valmin=-10.0,
                       valmax=10.0,
                       valinit=0.0,
                       valstep=0.5,
                       valfmt='%1.2f')

    plt.show()
