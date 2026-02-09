# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where non-lazy continuation lines are being handled incorrectly. The parser seems to be treating lazy lines as non-lazy and vice versa, which causes unexpected behavior when parsing certain MDX constructs.

### Reproduction

```mdx
> This is a blockquote
> with multiple lines
> that should continue

Some regular text here
```

When parsing the above MDX content, the continuation lines in the blockquote are not being recognized properly. The parser appears to be inverting the lazy line check, causing lines that should continue the blockquote to be treated as if they shouldn't, and lines that shouldn't continue to be treated as if they should.

### Expected behavior

The parser should correctly identify which lines are lazy continuations and which are non-lazy continuations. Blockquote continuation lines should be properly recognized and processed according to the MDX specification.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest LTS

This seems like it might be related to the tokenization logic for line continuations. The behavior is inconsistent with previous versions.

---
Repository: /testbed
