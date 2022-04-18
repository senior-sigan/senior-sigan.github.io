---
title: "Эксперимент с картинками №6"
date: 2013-04-09T21:33:00+06:00
draft: false
tags: []
featured: false
summary: ""
canonical_url: "https://vk.com/wall38057738_925"
---

Сегодня был очень длинный день. Поэтому для поддержания себя в бодром состоянии, я написал следующий сценарий искажения фоток. Вас ждет снова много “вещественных” преобразований. Надеюсь, я придумаю как делать фотки пастельными, а не мерзео-эпилептическими. Итак, сегодня на очереди — применение функций от координат на насыщенность каналов. Кто хочет- может посмотреть исходники, я там замутил массив указателей на функции. Описания под картинками.

## X/Y

Значение канала * (x/y). Только вот незадача. Я не перевёл во float, поэтому видны резкие границы разделения.

![(int)(x/y)](/assets/imagemagick-experiments-6/gn61wklfmmftg3ep5atf.jpeg)

Теперь плавное использвание x/y.

![(float)(x/y)](/assets/imagemagick-experiments-6/c342x0p7a7z3kc62s79p.jpeg)

## Логарифм

Логарифм произведения координат `log(x*y)`. По-моему это самый прикольный результат.

![log(x*y)](/assets/imagemagick-experiments-6/n6v3rsl1vvo00ji4oqf9.jpeg)

А что если взять log(x/y)?

![log(x/y)](/assets/imagemagick-experiments-6/3gfyi9wnv7z6dwhif365.jpeg)

Ещё один экземпляр. (прим. времени — через 2 года уже не могу вспомнить, что тут за функция. Имя файла xyyx.)

![xyyx](/assets/imagemagick-experiments-6/0ndg0khoqxeudglswu9j.jpeg)

## Sin

Quant*sin(x*y). Советую открыть оригинал и приблизить. Зрелище ооооочень странное.

![Quant*sin(x*y)](/assets/imagemagick-experiments-6/wjjzi8e8uo52qqic5yco.jpeg)

Тоже синус, но с более слабыми коэффициентами.

![ ](/assets/imagemagick-experiments-6//dv0ospy750vqf5vs8stp.jpeg)

В следующей серии я покажу что будет если не менять цвет пикселей, а менять их местами.

## Исходники

https://github.com/senior-sigan/magick/blob/master/function.h
