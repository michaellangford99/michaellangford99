---
layout: default
title: ECE477 Drone
description:
top_bar: This was going to be the nav bar but now I might get rid of this lol.
left_sidebar: I haven't written hardly any code yet
right_sidebar: and what I have written is truly awful

eleventyNavigation:
  key: drone
  parent: engineering

navToMdOptions:
  # Show excerpts (if they exist in data, read more above)
  showExcerpt: false
---

https://youtu.be/MRFakSWxx5s

#TODO: Put videos and maybe some photo gallery here

{% assign navPages = collections.all | eleventyNavigation: "drone" %}

<ul>
{%- for post in collections.all -%}
  {%- for navPage in navPages -%}
    {%- if navPage.url == post.url -%}

<div class="card padding-top-">
<div class="card-body">
<a class="card-link" href="{{ post.url }}"><h5 class="card-title">{{post.data.title}}</h5></a>
<p class="card-text">{{post.data.description}}</p>
</div>
<!--<img src={{post.url | append: post.data.background_img}} class="card-img-bottom" alt="..."> -->
</div>

<div class="mt-md-4"></div>

    {%- endif -%}
  {%- endfor -%}
{%- endfor -%}
</ul>
