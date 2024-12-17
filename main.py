# -*- coding: utf-8 -*-

import WFC as WFC_module
from tkinter import *
from tkinter import ttk
from tkinter import font
import L_System as LS_module
import Voxel_Grid  as VG_module
import Perlin_Noise as PN_module
import Cellular_Automaton as CA_module
import Fractal_Generation as FG_module 
import Space_Partitioning as SP_module

window = Tk()
window.title("Main")
window.geometry("800x500")
window.resizable(width=False, height=False)

''' Method launch functions '''

def CA_run():
	CA_module.run()

def FG_run():
	FG_module.run()

def LS_run():
	LS_module.run()

def PN_run():
 	PN_module.run()

def SP_run():
	SP_module.run()	

def VG_run():
	VG_module.run()

def WFC_run():
	WFC_module.run()


''' Pages describing generation methods '''

tab_control = ttk.Notebook(window)
CA = ttk.Frame(tab_control)
FG = ttk.Frame(tab_control)
LS = ttk.Frame(tab_control)
PN = ttk.Frame(tab_control)
SP = ttk.Frame(tab_control)
VG = ttk.Frame(tab_control)
WFC =ttk.Frame(tab_control)

tab_control.add(CA, text='CA')
tab_control.add(FG, text='FG')
tab_control.add(LS, text='LS')
tab_control.add(PN, text='PN')
tab_control.add(SP, text='SP')
tab_control.add(VG, text='VG')
tab_control.add(WFC, text='WFC')

''' Font purpose '''

Title = font.Font(family= "Arial", size=13, weight="normal", slant="roman")
Description = font.Font(family= "Arial", size=10, weight="normal", slant="roman")

''' Алгоритмы клеточных автоматов (Cellular Automaton) '''

CA_line_Total = Label(CA, text='Алгоритмы клеточных автоматов (Cellular Automaton)', font= Title)
CA_line_Total.place(relx=.0, rely=.03)
CA_line_1 = Label(CA, text='Описание: Клеточный автомат — это математическая модель, где сетка клеток изменяется в зависимости от состояния соседей по определённым правилам. Каждый "цикл" может обновлять состояние клеток, создавая сложные структуры.', wraplength=750, justify="left", font= Description)
CA_line_1.place(relx=.0, rely=0.15)
CA_line_2 = Label(CA, text='Применение: Используется для создания сложных подземных пещер и биомов. Например, в Dwarf Fortress и Terraria этот метод применяется для генерации пещерных систем.', wraplength=750, justify="left", font= Description)
CA_line_2.place(relx=.0, rely=0.25)
CA_line_3 = Label(CA, text='Преимущества: Хорошо подходит для создания естественных, органичных структур, таких как пещеры или лабиринты.', wraplength=750, justify="left", font= Description)
CA_line_3.place(relx=.0, rely=0.35)

CA_button = ttk.Button(CA, text="Запустить", command= CA_run)
CA_button.place(relx=.0, rely=0.50)


''' Фрактальная генерация (Fractal Generation) '''

FG_line_Total = Label(FG, text='Фрактальная генерация (Fractal Generation)', font= Title)
FG_line_Total.place(relx=.0, rely=.03)
FG_line_1 = Label(FG, text='Описание: Фракталы — это структуры, которые повторяются на разных уровнях масштаба. Они могут генерировать сложные, самоподобные паттерны.', wraplength=750, justify="left", font= Description)
FG_line_1.place(relx=.0, rely=0.15)
FG_line_2 = Label(FG, text='Применение: Этот метод часто используется для создания ландшафтов, горных массивов или побережий. Фрактальные генераторы применяются в играх для создания естественных и сложных форм, например, деревьев или береговых линий.', wraplength=750, justify="left", font= Description)
FG_line_2.place(relx=.0, rely=0.25)
FG_line_3 = Label(FG, text='Преимущества: Способность создавать бесконечно сложные и детализированные структуры, которые хорошо имитируют природные объекты.', wraplength=750, justify="left", font= Description)
FG_line_3.place(relx=.0, rely=0.35)

FG_button = ttk.Button(FG, text="Запустить", command= FG_run)
FG_button.place(relx=.0, rely=0.50)


''' L-системы (Lindenmayer System) '''

LS_line_Total = Label(LS, text='L-системы (Lindenmayer System)', font= Title)
LS_line_Total.place(relx=.0, rely=.03)
LS_line_1 = Label(LS, text='Описание: L-система — это математическая система, использующая правила переписывания для создания рекурсивных структур. Её часто используют для моделирования роста растений или деревьев.', wraplength=750, justify="left", font= Description)
LS_line_1.place(relx=.0, rely=0.15)
LS_line_2 = Label(LS, text="Применение: В играх L-системы применяются для генерации деревьев, кустов или других растительных структур, например, в играх с открытым миром (No Man's Sky).", wraplength=750, justify="left", font= Description)
LS_line_2.place(relx=.0, rely=0.25)
LS_line_3 = Label(LS, text='Преимущества: Простой способ создания органичных и сложных форм.', wraplength=750, justify="left", font= Description)
LS_line_3.place(relx=.0, rely=0.35)

LS_button = ttk.Button(LS, text="Запустить", command= LS_run)
LS_button.place(relx=.0, rely=0.50)


''' Шум Перлина (Perlin Noise) '''

PN_line_Total = Label(PN, text='Шум Перлина (Perlin Noise)', font= Title)
PN_line_Total.place(relx=.0, rely=.03)
PN_line_1 = Label(PN, text='Описание: Шум Перлина — это математическая функция, используемая для создания реалистичных плавных изменений высот и текстур. В отличие от простого случайного шума, который создаёт резкие изменения, шум Перлина создаёт сглаженные переходы.', wraplength=750, justify="left", font= Description)
PN_line_1.place(relx=.0, rely=0.15)
PN_line_2 = Label(PN, text='Применение: Часто используется для генерации террейна, облаков, текстур воды и других естественных ландшафтов. В таких играх, как Minecraft, этот метод применяется для создания природных форм, например, холмов и гор.', wraplength=750, justify="left", font= Description)
PN_line_2.place(relx=.0, rely=0.25)
PN_line_3 = Label(PN, text='Преимущества: Плавные переходы и вариативность высот, возможность настройки детализации.', wraplength=750, justify="left", font= Description)
PN_line_3.place(relx=.0, rely=0.35)

PN_button = ttk.Button(PN, text="Запустить", command= PN_run)
PN_button.place(relx=.0, rely=0.50)


''' Алгоритмы деления пространства (Space Partitioning Algorithms) '''

SP_line_Total = Label(SP, text='Алгоритмы деления пространства (Space Partitioning Algorithms)', font= Title)
SP_line_Total.place(relx=.0, rely=.03)
SP_line_1 = Label(SP, text='Описание: Эти алгоритмы разделяют игровое пространство на регионы или зоны, которые могут быть заселены объектами или структурами. Пример — бинарное разбиение пространства (BSP, Binary Space Partitioning), где пространство делится на две части, а затем на подпространства, что помогает создать комнаты или уровни.', wraplength=750, justify="left", font= Description)
SP_line_1.place(relx=.0, rely=0.15)
SP_line_2 = Label(SP, text='Применение: BSP часто используется для генерации случайных подземелий и уровней в таких играх, как The Binding of Isaac или Rogue. Это позволяет легко структурировать мир на логические зоны.', wraplength=750, justify="left", font= Description)
SP_line_2.place(relx=.0, rely=0.28)
SP_line_3 = Label(SP, text='Преимущества: Управляемая структура, возможность создания сложных лабиринтов и помещений.', wraplength=750, justify="left", font= Description)
SP_line_3.place(relx=.0, rely=0.40)

SP_button = ttk.Button(SP, text="Запустить", command= SP_run)
SP_button.place(relx=.0, rely=0.50)


''' Воксельные алгоритмы (Voxel-based Algorithms) '''

VG_line_Total = Label(VG, text='Воксельные алгоритмы (Voxel-based Algorithms)', font= Title)
VG_line_Total.place(relx=.0, rely=.03)
VG_line_1 = Label(VG, text='Описание: Воксели — это объёмные пиксели, которые используются для построения трёхмерных структур. Алгоритмы работы с вокселями позволяют генерировать сложные 3D-среды.', wraplength=750, justify="left", font= Description)
VG_line_1.place(relx=.0, rely=0.15)
VG_line_2 = Label(VG, text='Применение: Например, в Minecraft весь мир состоит из вокселей (блоков), которые могут содержать информацию о типе материала, высоте, цвете и т.д.', wraplength=750, justify="left", font= Description)
VG_line_2.place(relx=.0, rely=0.25)
VG_line_3 = Label(VG, text='Преимущества: Позволяет легко манипулировать объёмными пространствами, что важно для разрушения или построения объектов.', wraplength=750, justify="left", font= Description)
VG_line_3.place(relx=.0, rely=0.35)

VG_button = ttk.Button(VG, text="Запустить", command= VG_run)
VG_button.place(relx=.0, rely=0.50)


''' Коллапс волновой функции (Wave Function Collapse (WFC)) '''

WFC_line_Total = Label(WFC, text='Коллапс волновой функции (Wave Function Collapse (WFC))', font= Title)
WFC_line_Total.place(relx=.0, rely=.03)
WFC_line_1 = Label(WFC, text='Описание: WFC — это относительно новый метод, который использует подход из квантовой физики. Он работает на принципе ограничения возможных вариантов на основе соседей клетки. С каждым шагом алгоритм "схлопывает" варианты, оставляя только совместимые структуры.', wraplength=750, justify="left", font= Description)
WFC_line_1.place(relx=.0, rely=0.15)
WFC_line_2 = Label(WFC, text='Применение: Применяется для процедурной генерации текстур, объектов и даже уровней, где важно сохранять заданные правила расположения.', wraplength=750, justify="left", font= Description)
WFC_line_2.place(relx=.0, rely=0.25)
WFC_line_3 = Label(WFC, text='Преимущества: Обеспечивает создание структур с высокой степенью целостности и согласованности, даже при случайной генерации.', wraplength=750, justify="left", font= Description)
WFC_line_3.place(relx=.0, rely=0.35)

WFC_button = ttk.Button(WFC, text="Запустить", command= WFC_run)
WFC_button.place(relx=.0, rely=0.50)



tab_control.pack(expand=1, fill='both')
window.mainloop()