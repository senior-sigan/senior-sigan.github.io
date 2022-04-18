---
layout: page
title: Archive
permalink: /archive
---
<ul class="archive">
{% for note in site.notes reversed %}
<li>
    <a href="{{ note.url }}{%- if site.use_html_extension -%}.html{%- endif -%}" class="internal-link">{{note.title}}</a>
    <span>({{ note.date | date: "%B %Y" }})</span>
</li>
{% endfor %}
</ul>