# Bug Report

### Describe the bug

I'm experiencing an issue with front matter validation where numeric values are not being properly converted to strings. When I use a number in my front matter, it's not being handled correctly anymore.

### Reproduction

```yaml
---
title: My Post
order: 5
date: 2024-01-15
---
```

When I have front matter like this with a numeric `order` field or a Date object, the validation seems to fail or behave unexpectedly. Previously this worked fine and numbers/dates would be automatically converted to strings, but now it's broken.

### Expected behavior

Numbers and Date objects in front matter should be automatically converted to strings during validation, just like they were before. The `order: 5` should become `"5"` and dates should be stringified.

### System Info

- Docusaurus version: latest
- Node version: 18.x

This seems like a regression - it was working in previous versions. Any help would be appreciated!

---
Repository: /testbed
