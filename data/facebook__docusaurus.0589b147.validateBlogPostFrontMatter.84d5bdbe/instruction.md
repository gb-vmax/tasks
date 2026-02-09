# Bug Report

### Describe the bug

I'm experiencing an issue with blog post frontmatter where nested object values are being flattened into the parent object, causing unexpected behavior. When I have a frontmatter field that contains an object value, all the properties from that nested object get merged into the root level of the frontmatter.

### Reproduction

```yaml
---
title: My Blog Post
metadata:
  description: This is a description
  keywords: test
author: John Doe
---
```

After processing, the frontmatter ends up with `description` and `keywords` at the root level instead of being nested under `metadata`. This breaks the expected structure and can cause conflicts if there are already fields with those names at the root level.

### Expected behavior

The frontmatter should preserve the original structure. Nested objects should remain nested and not be flattened. The `metadata` object should stay as a single object with its own properties, not have its properties spread into the parent.

Also noticed that fields starting with underscore (like `_internal`) are being silently dropped, which might be intentional but wasn't documented anywhere I could find.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
