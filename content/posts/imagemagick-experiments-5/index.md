---
title: "Imagemagick Experiments 5"
date: 2013-04-08T21:02:00+06:00
draft: false
tags: []
featured: false
summary: ""
series: ["Эксперименты с картинками"]
canonical_url: "https://vk.com/wall38057738_915"
---

Специально для любителей острых ощущений. Сейчас вы станете свидетелями того как каждый “пиксель” влияет на следующий с разными коэффициентами.

Для простоты в данном эксперименте значение цвета предыдущего пикселя просто складывается со следующим с некоторым коэффициентом.

{{< figure src="https://dev-to-uploads.s3.amazonaws.com/i/ebg2b8tcd487z4j66mdm.jpeg" caption="Коэффициент 0.5 — это только начало.">}}

{{< figure src="https://dev-to-uploads.s3.amazonaws.com/i/3hpe29jwkyr8nnhzqbbu.jpeg" caption="Коэффициент 0.7">}}

{{< figure src="https://dev-to-uploads.s3.amazonaws.com/i/mnns10ld8i6w6qi74dka.jpeg" caption="Коэффициент 0.8">}}

{{< figure src="https://dev-to-uploads.s3.amazonaws.com/i/z3ztngzwb2s0acopl55e.jpeg" caption="Коэффициент 0.9">}}

И самое весёлое 1.1. Почти белый шум. Как будто телевизор плохо показывает.

{{< figure src="https://dev-to-uploads.s3.amazonaws.com/i/jpph1wq06ctxldsqcvgb.jpeg" caption="Коэффициент 1.1">}}

В следующей части мы применим некоторую функцию от координаты пикселя и его значением над изображением.

## Исходники

https://github.com/senior-sigan/magick/blob/master/dependence.h
