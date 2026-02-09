# Bug Report

### Describe the bug

I'm experiencing inconsistent behavior with page front matter validation in my Docusaurus site. Sometimes the front matter fields I define in my pages are being randomly dropped/ignored, causing pages to render incorrectly or with missing metadata.

### Reproduction

Create a page with front matter:

```md
---
title: My Page Title
description: My page description
custom_edit_url: https://github.com/example/repo
---

# Page content here
```

When building the site, sometimes the `title` is missing, sometimes the `description` disappears, and other times the `custom_edit_url` is gone. It seems completely random which field gets dropped.

### Expected behavior

All front matter fields that pass validation should be preserved and available to the page. The behavior should be deterministic - the same input should always produce the same output.

### Additional context

This is causing major issues in production because:
- Page titles randomly disappear from the browser tab
- SEO metadata is inconsistently applied
- Custom edit URLs sometimes don't show up

The issue appears to be non-deterministic - rebuilding the same site multiple times produces different results each time.

---
Repository: /testbed
