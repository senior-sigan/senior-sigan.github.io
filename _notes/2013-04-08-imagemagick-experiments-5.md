---
title: "Эксперимент с картинками №5"
date: 2013-04-08 21:02:00 +0600
draft: false
tags: []
featured: false
summary: ""
canonical_url: "https://vk.com/wall38057738_915"
---

Специально для любителей острых ощущений. Сейчас вы станете свидетелями того как каждый “пиксель” влияет на следующий с разными коэффициентами.

Для простоты в данном эксперименте значение цвета предыдущего пикселя просто складывается со следующим с некоторым коэффициентом.

![Коэффициент 0.5 — это только начало.](/assets/imagemagick-experiments-5/ebg2b8tcd487z4j66mdm.jpeg)

![Коэффициент 0.7](/assets/imagemagick-experiments-5/3hpe29jwkyr8nnhzqbbu.jpeg)

![Коэффициент 0.8](/assets/imagemagick-experiments-5/mnns10ld8i6w6qi74dka.jpeg)

![Коэффициент 0.9](/assets/imagemagick-experiments-5/z3ztngzwb2s0acopl55e.jpeg)

И самое весёлое 1.1. Почти белый шум. Как будто телевизор плохо показывает.

![Коэффициент 1.1](/assets/imagemagick-experiments-5/jpph1wq06ctxldsqcvgb.jpeg)

В следующей части мы применим некоторую функцию от координаты пикселя и его значением над изображением.

## Исходники

https://github.com/senior-sigan/magick/blob/master/dependence.h
