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

![Alt text](IMG_20230805_090053448-PANO.jpg "  ")

{{ collections.all | eleventyNavigation: "hiking" | eleventyNavigationToMarkdown: navToMdOptions}}
