# Bug Report

### Describe the bug

After a recent update, I'm encountering an issue with MDX ESM block handling. When MDX files contain empty ESM blocks (import/export statements with no actual content), the parser seems to be returning unexpected values instead of empty strings.

### Reproduction

```mdx
---
title: Example
---

import {}

# My Content

Some text here.
```

When parsing this MDX content, the empty import statement is not being handled correctly. Previously, empty ESM blocks would be converted to empty strings, but now they're being processed differently which breaks downstream code that expects string values.

### Expected behavior

Empty ESM blocks should be consistently handled and converted to empty strings (or at minimum, handled in a way that doesn't break existing parsing logic). The parser should gracefully handle cases where `node.value` exists but is empty or falsy.

### System Info
- remark-mdx version: 3.0.0

This seems to have started happening recently and is affecting MDX files that have empty or incomplete import/export statements.

---
Repository: /testbed
