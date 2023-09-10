---
layout: default
title: Engineering
description: I need more free time

eleventyNavigation:
  key: engineering
  #parent: 
  title: Engineering

navToMdOptions:
  # Show excerpts (if they exist in data, read more above)
  showExcerpt: false
  
#for later when you use a custom engineering tree  
# | sort(false, false, "data.title")
---

{{ collections.all | eleventyNavigation: "engineering" | eleventyNavigationToMarkdown: navToMdOptions}}

