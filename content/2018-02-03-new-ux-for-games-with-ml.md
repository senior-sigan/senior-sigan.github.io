---
title: "New UX for Games With ML"
date: 2018-02-03 12:00:00 +0600
draft: false
tags: ["gamedev"]
featured: false
summary: ""
---

> TL;DR; ML создает способы, с помощью которых виртуальная реальность сможет нас почувствовать. Мы в свою очередь через VR/AR и так её достаточно хорошо ощущаем, но она о нас практически ничего не знает. Будущее UX в том, чтобы дать виртуальной реальности возможности ощущать нас.

У нас уже есть [ML](https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D1%88%D0%B8%D0%BD%D0%BD%D0%BE%D0%B5_%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5), [AR](https://ru.wikipedia.org/wiki/%D0%94%D0%BE%D0%BF%D0%BE%D0%BB%D0%BD%D0%B5%D0%BD%D0%BD%D0%B0%D1%8F_%D1%80%D0%B5%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C), [VR](https://ru.wikipedia.org/wiki/%D0%92%D0%B8%D1%80%D1%82%D1%83%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F_%D1%80%D0%B5%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C) и другие новые [модные технологии](https://en.wikipedia.org/wiki/Emerging_technologies). Если с последними двумя ясно что делать в играх, то что можно делать с ML? Там всякое компьютерное зрение, генерация контента, предсказание чего-нибудь. Где же новые игры, что используют ML?
Я предлагаю пофантазировать и придумать либо новые жанры игр, либо новые способы управления.

![ ](/assets/new-ux-for-games-with-ml/3lgbyd7zs7xc9p7jl76u.png)

## Новое управление

Это довольно скучно управлять игрой с помощью клавиатуры, джойстика или мыши. Это придумали еще в 80-ые годы. Прошло почти 40 лет(sic!) с тех времён. Мы с вами насмотрелись фантастических фильмов и не только, где управляют игрой силой мысли через нейроинтерфейс. Но в домашних условиях вряд ли получится присоединить электроды к голове, поэтому пока что отложим эту тему. И все же у нас есть веб камера, возможно даже несколько, и микрофон. Два интерфейса, которые не популярно использовать в играх. Но сейчас в 2к18 году мы уже так много всего умеем делать с изображением и звуком, надо этим воспользоваться. Начинаем генерировать идеи.

## Управление мимикой лица

![Apple анонсировали emoji, повторяющие мимику человека](/assets/new-ux-for-games-with-ml/mitr6sbjctaqwxtdncvv.png)

Начнём с простого. Можно сделать обычный Dance revolution для мимики. Представьте, падает то emoji улыбающейся какахи, что в слайде у Apple, и вам нужно успеть тоже улыбнуться. Конечно, если посмотреть на emoji, то возникает вопрос — “А что человек реально такое может изобразить?”. Уморительно же.

![ ](/assets/new-ux-for-games-with-ml/bwpkocrg67fuohnsgace.jpeg)

А еще если это всё делать на вечеринках и снимать видео как кто-то играет, то получится очень смешно и всем будет что вспомнить. Можно будет устроить соревнование, кто быстрее может менять мимику, точнее чью мимику компьютер лучше распознаёт.

## Управление направлением лица

Мимика по факту представляет собой кнопки нашей игры, а нам нужны еще и заменители джойстика или “стрелочек”, чтобы указывать направления.

Я совсем недавно наткнулся на классную демку, где управляют самолетиком с помощью направления лица и стреляют, открывая рот. Можно ещё реализовать это как наклон головы на несколько градусов.

{% youtube cGR30llvamU %}

Кстати, такую игру где надо управлять глазами, лицом, ртом можно использовать для тренировки концентрации. Если ты отвлечешься, то потеряешь управление и проиграешь. Интересный момент, не так ли?

## Управление позами

Если у нас будет достаточно простой способ получать информацию о положении человека в пространстве, о том где его рука-нога-голова, то можно делать, очевидно, всякие спортивные игры, танцы, теннис. На сколько я знаю, такие уже есть, но они используют _специальные_ приспособления. Идея в том, чтобы это происходило автомагически по данным камеры. Это может работать даже на смартфонах.

Естественно, существуют исследования о сегментации тела, определении позы по видео. И уже есть успешные реализации, можете сами посмотреть: {% youtube pW6nZXeWlGM %}

- [OSVOS: One-Shot Video Object Segmentation](http://people.ee.ethz.ch/~cvlsegmentation/osvos/) — сегментация целого тела на видео, паркур6 все дела.
- [Realtime_Multi-Person_Pose_Estimation](https://github.com/ZheC/Realtime_Multi-Person_Pose_Estimation) — а тут уже интереснее, тут строят скелетный каркас человека. Примеры показывают как на танцующих людях это работает.

## Голосовое управление

Как минимум, приложение, в котором надо отдавать команды голосом, будет очень веселое. Представьте, приложение управления таксистом: “поворачивай налево, да не туда, а сюда, быстрее” или командование армией. Кстати вспомнил 3 и 4 серии из аниме [“No game, no life”](https://online.anidub.com/anime/full/8944-net-igry-net-zhizni-no-game-no-life-01-iz-12.html) , где главные герои играли в шахматы и отдавали команды фигурам, а от их решительности и убедительности фигуры решали — ходить или нет. Думаю, построив модель распознавания эмоции и намеренности, можно получить игру, которая будет реагировать на наши эмоции. Научные статьи [можно найти](https://scirate.com/search?utf8=%E2%9C%93&q=emotion+voice#results).

## MMORPG игры в дополненной реальности

Это уже на грани фантастики, даже аниме есть, где применяется эта технология, и вышло оно в 2017 году, называется [Sword Art Online, Ordinal Scale](https://online.anidub.com/anime_movie/10301-mastera-mecha-onlayn-poryadkovyy-rang-gekijouban-sword-art-online-ordinal-scale-movie.html). В нём люди носят специальные “очки” и с помощью них дополняют реальность и играют в ней в MMORPG! Но это же фантастика, как такое сделать? Всё очень просто(нет).

Для этого вам понадобится: модель сегментации изображения, чтобы выделить на нем человека; модель построения 3D mesh поверхности по 2D изображению или видео; алгоритм замены одежды или частей 3d поверхности; вывод через очки дополненной реальности на глаз маски, которая будет видеться поверх человека или любого другого объекта. Profit! Вы сделали первую в мире MMORPG в дополненной реальности, где люди бегают в доспехах. Я полагаю, как минимум вычисление mesh и применение маски будет готово для применения в ближайшее время, [уже есть статьи](https://github.com/timzhang642/3D-Machine-Learning). А вот с очками, надо попросить Google выпустить новый образец.

## Вывод

Все наши размышления над применением ML для создания новых способов управления не совсем уж и смешные или глупые. Мы этими новыми методами решаем следующую проблему VR и AR — мы улучшаем то, как человек может войти в виртуальную реальность. До сих пор VR/AR это только 3D-очки, GPS, очки специальные. Но методы ввода и взаимодействия с виртуальной реальностью остались в целом теми же: клавиатура и мышь, да тачскрин. Что это означает? А то что мы можем ощущать виртуальную реальность через очки, слышать её и даже ощущать через, например, вибрации джойстика, то сама виртуальность не может до нас прикоснуться, кроме как через кнопки. Нам нужны методы, которыми мы наделим её тоже некоторыми способностями: понимать в какой мы позе стоим, куда смотрим, какое у нас выражение лица, какой у нас голос, на сколько мы решительны, как двигаемся. И прелесть в том, что уже сейчас мы можем начать это делать. И я думаю, что за этим будущее UX.

...

Частично содержимое этой статьи рассказывал на Омском IT-субботнике.

{% youtube nSZWvW8SALk %}

[Слайды презентации.](https://docs.google.com/presentation/d/e/2PACX-1vSf4kSoa0vfBmnr3tpnoM_fJ-QjdKBWSZkS6kV2yYjfzfzO-LBDJn7sCV7bioA4Ta4C-1KqnLowo0eD/pub?start=false&loop=false&delayms=3000)