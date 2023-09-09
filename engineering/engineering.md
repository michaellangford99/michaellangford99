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
---

{{ collections.all | eleventyNavigation: "engineering" | eleventyNavigationToMarkdown: navToMdOptions}}
