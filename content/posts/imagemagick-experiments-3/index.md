---
title: "Imagemagick Experiments 3"
date: 2013-04-03T15:54:00+06:00
draft: false
tags: []
featured: false
summary: ""
series: ["Эксперименты с картинками"]
canonical_url: "https://vk.com/wall38057738_904"
---

Нет времени объяснять-через 20 минут начинается тренировка. Просто выкладываю новую порцию картинок. Теперь я произвёл случайное перемешивание каналов.

Берем 3 канала RGB. Существует всего {{< katex >}}3! = 6{{< /katex >}} возможных перестановок. Каждую перестановку выбираем с равными вероятностями {{< katex >}}\frac{1}{6}{{< /katex >}}. То есть равномерное дискретное распределение. Ожидается, что картинка становится почти монохромной. Так и оказалось.

![Перемешивание цветов. Увеличьте фотографию, для усиления эффекта.](https://dev-to-uploads.s3.amazonaws.com/i/mvhog1p7ji8o5405se7z.jpeg)

![Перемешивание цветов. Увеличьте фотографию, для усиления эффекта.](https://dev-to-uploads.s3.amazonaws.com/i/uc1hy1u30ivo9z3i1jhe.jpeg)

## Мультик-преобразование

Следующее преобразование- берем яркость канала, если она больше половины яркости, то делаем её максимальной, иначе минимальной. Я забыл как называется этот эффект, кто знает фотошоп скажите.

Усиление каналов. Получаем вроде всего 8 цветов — red green blue black white cyan magenta yellow.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/mcu487go6pep9wfagsox.jpeg)

Няшке опять не везет. Но когда-нибудь я найду эффект, который сделает картинку фееричной.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/91qkynvbr9uh1jbyh0ow.jpeg)

## Исходники

https://gist.github.com/senior-sigan/5301188