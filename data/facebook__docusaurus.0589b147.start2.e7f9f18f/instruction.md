# Bug Report

### Describe the bug

I'm experiencing an issue with blank line parsing in MDX content. When there are spaces before a blank line, the parser seems to be handling them incorrectly. The behavior appears to be inverted - lines with leading spaces are being processed differently than expected.

### Reproduction

```mdx
Some content here

  
More content after blank line with spaces
```

When parsing MDX content that has blank lines with leading whitespace, the tokenizer doesn't handle them properly. It looks like the logic for checking whether to process spaces is backwards.

### Expected behavior

Blank lines with leading whitespace should be tokenized the same way as regular blank lines. The `linePrefix` should be applied when there are markdown spaces, not when there aren't any.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

This seems to have broken recently - content that was parsing fine before now fails when there are spaces at the beginning of blank lines.

---
Repository: /testbed
