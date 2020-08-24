---
title: "Imagemagick Experiments 8"
date: 2013-05-04T20:53:00+06:00
draft: false
tags: []
featured: false
summary: ""
series: ["Эксперименты с картинками"]
canonical_url: "https://vk.com/wall38057738_954"
---

Привет!
Сегодня у нас уроки кирпичизма. Надеюсь m$oft не наедет на меня за использование прямоугольников. Итак, что будет если мы разобьем матрицу на много подматриц произвольной формы? А если при этом произведем какую-нибудь операцию над подматрицей? Так вот, написал я тут алгоритм, наверное очень тупо, так как картинку 1900*1200 он обрабатывает десяток секунд, который перемешивает каналы у данной подматрицы. Не переживайте, я разовью эту идею дальше и будет очень забавно.

## Генерация матриц

Существует 2 вида подматриц- синие зеленые и красны. Размер выбирается как случайное число.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/daegq1c3dbdvhgupp8y3.jpeg)

А здесь размер выбирается как половина от ширины матрицы. Очевидно прогрессия {{< katex >}}\frac{1}{2})^n{{< /katex >}}. Ну или почти такая. Не суть.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/g3il2xvxdvl1hbqfntk9.jpeg)

Теперь случайное перемешивание в подматрицах. Обычный рандом дает не очень клевый результат.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/pdr32slb9rdg286vfi8u.jpeg)

Тут волей случая первая подматрица оказалась очень большой. FIX IT!!!!
Вот то-то же. Нам нужен был true_random. Здесь выбирается средний размер квадратов с некоторой дельтой. Вот так красить машины надо. Это я понимаю искусство.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/0o59xkji5ryopzodz2t1.jpeg)

Теперь перекрасим няшку.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/r06gl4lyb2iufc2ltwur.jpeg)

> Тебя теперь интел засудит, у них вся реклама в таком стиле)

## Смешивание картинок

Нет времени объяснять, прямоугольники захватывают мир……………

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/swc95wnehq27ectw3t0c.jpeg)

От сложения няшек, няшность не возросла T_T.

## Исходники

https://github.com/senior-sigan/magick/blob/master/brick.h