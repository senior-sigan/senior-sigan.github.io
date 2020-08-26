---
title: "Imagemagick Experiments 6"
date: 2013-04-09T21:33:00+06:00
draft: false
tags: []
featured: false
summary: ""
series: ["Эксперименты с картинками"]
canonical_url: "https://vk.com/wall38057738_925"
---

Сегодня был очень длинный день. Поэтому для поддержания себя в бодром состоянии, я написал следующий сценарий искажения фоток. Вас ждет снова много “вещественных” преобразований. Надеюсь, я придумаю как делать фотки пастельными, а не мерзео-эпилептическими. Итак, сегодня на очереди — применение функций от координат на насыщенность каналов. Кто хочет- может посмотреть исходники, я там замутил массив указателей на функции. Описания под картинками.

## X/Y

Значение канала * (x/y). Только вот незадача. Я не перевёл во float, поэтому видны резкие границы разделения.

{{< figure src="images/gn61wklfmmftg3ep5atf.jpeg" caption="(int)(x/y)" >}}

Теперь плавное использвание x/y.

{{< figure src="images/c342x0p7a7z3kc62s79p.jpeg" caption="(float)(x/y)">}}

## Логарифм

Логарифм произведения координат. По-моему это самый прикольный результат.

{{< figure src="images/n6v3rsl1vvo00ji4oqf9.jpeg" caption="log(x*y)" >}}

А что если взять log(x/y)?

{{< figure src="images/3gfyi9wnv7z6dwhif365.jpeg" caption="log(x/y)" >}}

Ещё один экземпляр. (прим. времени — через 2 года уже не могу вспомнить, что тут за функция. Имя файла xyyx.)

{{< figure src="images/0ndg0khoqxeudglswu9j.jpeg" caption="xyyx" >}}

## Sin

Quant*sin(x*y). Советую открыть оригинал и приблизить. Зрелище ооооочень странное.

{{< figure src="images/wjjzi8e8uo52qqic5yco.jpeg" caption="Quant*sin(x*y)" >}}

Тоже синус, но с более слабыми коэффициентами.

![Alt Text](images/dv0ospy750vqf5vs8stp.jpeg)

В следующей серии я покажу что будет если не менять цвет пикселей, а менять их местами.

## Исходники

https://github.com/senior-sigan/magick/blob/master/function.h
