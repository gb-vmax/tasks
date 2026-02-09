# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where certain markdown constructs are not being processed correctly. It seems like the tokenizer is skipping valid constructs or processing them in the wrong order.

### Reproduction

```mdx
# Test Document

Some content here with **bold text** and _italic text_.

- List item 1
- List item 2
- List item 3

More content after the list.
```

When parsing this MDX content, some elements are being incorrectly parsed or skipped entirely. The issue appears to be related to how the tokenizer handles construct fallbacks when one construct fails.

### Expected behavior

All markdown constructs should be properly tokenized and parsed. When one construct fails to match, the tokenizer should correctly try the next available construct in the list.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
