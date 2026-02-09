# Bug Report

### Describe the bug

When specifying blog post authors using object syntax in front matter, the author information is being incorrectly processed. Instead of properly handling the author object with fields like `name`, `url`, `imageURL`, etc., the entire object is being assigned to a `name` property, resulting in `{name: [object Object]}`.

### Reproduction

```yaml
---
title: My Blog Post
authors:
  - name: John Doe
    url: https://example.com
    imageURL: /img/avatar.jpg
---
```

When using the object syntax for authors, the author data gets mangled. The expected behavior is that the object should be passed through as-is with all its properties intact, but instead it seems to be wrapped incorrectly.

### Expected behavior

Author objects should be preserved with all their properties (name, url, imageURL, etc.) and not have the entire object assigned to a single property.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
