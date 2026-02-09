# Bug Report

### Describe the bug

When specifying blog post authors as strings in the front matter, they're no longer being converted to the proper author object format with a `key` property. This breaks author lookups from the authors map.

### Reproduction

```yaml
---
title: My Blog Post
authors: john_doe
---
```

Previously, the string `'john_doe'` would be normalized to `{key: 'john_doe'}` to allow looking up the full author details from the authors configuration file. Now it seems to be passed through as-is, which causes issues when the code expects an object with a `key` property.

### Expected behavior

When an author is specified as a string in the front matter, it should be treated as a key to lookup the author's full information from the authors map. The string should be automatically converted to an object like `{key: 'john_doe'}`.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
