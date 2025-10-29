# Game about space

Это простая игра про космический корабль в открытом космосе, который умеет стрелять. Игра написана на асинхронном коде Python.

![Gif](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExNG85am9qdzR5cGN4dDd2YW1nc25scXg4cXJpOTk0MWNmaDhud3NucyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IzOOd6AfigcOTQNwnF/giphy.gif)


## Оглавление

- [Требования](#требования)
- [Установка](#установка)
- [Запуск проекта](#запуск-проекта)
- [Цель проекта](#цель-проекта)


## Требования

- **Python**: 3.11 или выше


## Установка

- Python 3.11 должен быть установлен
- Скачайте код:
```bash
git clone https://github.com/VASILIYKAS/Async-python-Game-about-space.git
```
- Перейдите в папку с проектом используя команду `cd`.
- Рекомендуется создать виртуальное окружение. Для этого нужно выполнить команду: 
```bash
python -m venv .venv
```
- Активируйте виртуальное окружение:
```bash
.venv\Scripts\activate    # Для Windows
source .venv/bin/activate # Для Linux
```
- Установите зависимости:
```bash
pip install -r requirements.txt
``` 


## Запуск проекта

Для запуска необходимо запустить файл "main.py" в корне проекта, команда для запуска:
```powershell
python main.py
```

Скорость коробля и количество звезд на фоне можно изменить. \
По умолчанию количество звезд - 200 \
Скорость коробля - 2 \
Для этого в корне проекта создайте файл `.env` и укажите в нём свои значение:
```.env
COUNT_STARS=200
SPACESHIP_SPEED=2
```

Для того что бы остановить игру нажмите `CTRL+C`.

## Цель проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).