# RobotMotorsControl
## Общее описание проекта 
Цель проекта научиться работать с git, создать скрипт для управления моторами привода робота.
## Описание работы с Git:
* Создание и клонирование репозитория:
1. Создана регистрация на GitHab
2. Создан репозиторий RobotMotorsControl на GitHab через меню Create a new repository в личном кабинете. 
3. Репозиторий склонирован в домашний каталог с помощью команды git clone https://github.com/DVlabs-projects/RobotMotorsControl.git
* Процесс сохранения изменений:
1. Создаем файл в репозитории командой nano motors_control.py
2. Редактируем файл в nano и сохраняем
3. Создаем добавление файла командой git add motors_control.py
4. Фиксируем изменения уомандой git commit
5. Отправляем изменения в репозиторий GitHab командой git push 
* Взаимодействие с ветками:
1. Создаем ветку motors_control_new командой git checkout -b motors_control_new
2. Проверяем результат командой git branch
3. Создаем новый файл motors_control_new.py командой nano motors_control_new.py
4. Создаем добавление файла командой git add motors_control_new.py 
5. Фиксируем изменения уомандой git commit
6. Отправляем изменения в репозиторий GitHab командой git push
7. Переходим в главную ветку git checkout master
8. Делаем слияние веток командой git merge motors_control_new
* Пул-реквест: создан пул-реквест добавления скрипта motors_control_new.py для управления моторами одноплатным ПК Orange pi
* Основные изменения и улучшения в коде: В скрипте motors_control.py реализовано управление моторами с помощью Raspberry Pi, 
 далее добавлен скрипт motors_control_new.py для управления моторами одноплатным ПК Orange pi, применяется библиотека wiringpi 
 для управления выводами gpio.

## Заключение
 Git это удобный инструмент для коллективной работы над проектами.