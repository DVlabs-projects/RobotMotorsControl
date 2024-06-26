#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import curses
import time
import wiringpi
from wiringpi import GPIO

# Установим номера пинов GPIO  (orangepi 40pin gpio), с которыми будем работать
M1_RIGHT = 19 #PA07
M1_LEFT = 20 #PA08
M2_RIGHT = 22 #PA09
M2_LEFT = 23 #PA10

# Функция для подготовки пинов GPIO
def setup(*ports):
    wiringpi.wiringPiSetup()
    for port in ports:
        # Установка пина на вывод + низкий уровень "0"
        wiringpi.pinMode(port, GPIO.OUTPUT)
        wiringpi.digitalWrite(port, GPIO.LOW)

# Функция для установки низкого уровня на всех пинах (выключение)
def stop_all():
    wiringpi.digitalWrite(M1_LEFT, GPIO.LOW)
    wiringpi.digitalWrite(M1_RIGHT, GPIO.LOW)
    wiringpi.digitalWrite(M2_LEFT, GPIO.LOW)
    wiringpi.digitalWrite(M2_RIGHT, GPIO.LOW)

# Функция для управления вращением движков
def rotate(motor=1, mode='s'):
    # Выключаем все пины
    stop_all()
    # Для мотора 1
    if motor == 1:
        if mode == 'r':
	    # Устанавливаем высокий уровень на пине M1_RIGHT (4)
            wiringpi.digitalWrite(M1_RIGHT, GPIO.HIGH)
        elif mode == 'l':
	    # Устанавливаем высокий уровень на пине M1_LEFT (17)
            wiringpi.digitalWrite(M1_LEFT, GPIO.HIGH)
    # Для мотора 2
    elif motor == 2:
        if mode == 'r':
            wiringpi.digitalWrite(M2_RIGHT, GPIO.HIGH)
        elif mode == 'l':
            wiringpi.digitalWrite(M2_LEFT, GPIO.HIGH)

# Выполним инициализацию пинов GPIO
setup(M1_RIGHT, M1_LEFT, M2_RIGHT, M2_LEFT)

# Инициализация экрана (модуль curses)
stdscr = curses.initscr()
# Реагировать на нажатие клавиш без подтверждения при помощи ENTER
curses.cbreak()
# Разрешить использование стрелочек на клавиатуре
stdscr.keypad(1)
# Не блокировать программу по времени при опросе событий
stdscr.nodelay(1)

# Отобразим на экране данные по умолчанию
stdscr.addstr(0, 10, "Hit 'q' to quit")
stdscr.addstr(2, 10, "A - M1 Left, D - M1 Right")
stdscr.addstr(3, 10, "< - M2 Left, > - M2 Right")
stdscr.addstr(4, 10, "S - stop")
stdscr.refresh()

# Главный цикл
while True:
    # Получаем код нажатия клавиши и проверяем его
    key = stdscr.getch()
    if key != -1:
        # Если клавиша "стрелка влево" то вращаем движок 2 влево
        if key == curses.KEY_LEFT:
	    # Выводим на экран строку "M2 <---" в позиции 6, 10
            stdscr.addstr(6, 10, "M2 <---")
            rotate(2, 'l')
        # Если клавиша "стрелка вправо" то вращаем движок 2 вправо
        elif key == curses.KEY_RIGHT:
            stdscr.addstr(6, 10, "M2 --->")
            rotate(2, 'r')
        # Если клавиша "а" то вращаем движок 1 влево
        elif key == ord('a'):
            stdscr.addstr(6, 10, "M1 <---")
            rotate(1, 'l')
        # Если клавиша "d" то вращаем движок 1 вправо
        elif key == ord('d'):
            stdscr.addstr(6, 10, "M1 --->")
            rotate(1, 'r')
        # Если клавиша "s" то останов всех движков
        elif key == ord('s'):
            stdscr.addstr(6, 10, "STOP 12")
            stop_all()
        # Если клавиша "q" то выходим из программы
        elif key == ord('q'):
	    # Восстановление прежних настроек терминала
            stdscr.keypad(0)
            curses.echo()
            curses.endwin()
            # Очистка и выход
            os.system('clear')
            sys.exit()
        # Обновляем текст на экране и делаем небольшую задержку
        stdscr.refresh()
        time.sleep(0.01)
