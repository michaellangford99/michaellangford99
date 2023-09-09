---
layout: widescreen
title: Hiking & Photography
description: Brought to you by a crappy Motorola
background_img: IMG_20230805_090053448-PANO.jpg

eleventyNavigation:
  key: hiking
  #parent: 
  title: Hiking & Photography

navToMdOptions:
  # Show excerpts (if they exist in data, read more above)
  showExcerpt: false
---

{% assign navPages = collections.all | eleventyNavigation: "hiking" %}

<ul>
{%- for post in collections.all -%}
  {%- for navPage in navPages -%}
    {%- if navPage.url == post.url -%}

<div class="card padding-top-">
<div class="card-body">
<a class="card-link" href="{{ post.url }}"><h5 class="card-title">{{post.data.title}}</h5></a>
<p class="card-text">{{post.data.description}}</p>
</div>
<img src={{post.url | append: post.data.background_img}} class="card-img-bottom" alt="...">
</div>

<div class="mt-md-4"></div>

    {%- endif -%}
  {%- endfor -%}
{%- endfor -%}
</ul>