# Bug Report

### Describe the bug

I'm experiencing an issue with front matter validation where numeric values in YAML front matter are not being converted to strings as expected. When I have a numeric value in my front matter that should be treated as a string, it's remaining as a number instead of being converted.

### Reproduction

```yaml
---
title: My Post
id: 12345
---
```

In this case, the `id` field with value `12345` should be converted to the string `"12345"`, but it's staying as a number. This is causing issues downstream where string values are expected.

### Expected behavior

Numeric values in front matter should be automatically converted to strings when the schema expects a string type. This was working correctly before and the conversion should happen transparently.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
