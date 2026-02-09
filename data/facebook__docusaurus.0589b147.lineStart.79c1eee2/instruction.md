# Bug Report

### Describe the bug

I'm encountering an issue with lazy line parsing in MDX code blocks. When processing indented code blocks that span multiple lines, the parser seems to incorrectly handle lazy continuation lines. Lines that should be treated as lazy (not part of the code block) are being included in the block, and vice versa.

### Reproduction

```mdx
> This is a blockquote
    indented code here
    more code
```

When parsing the above MDX content, the indented code block continuation behavior is inverted. Lines that should be excluded from the code block are being included, while lines that should continue the block are being terminated early.

### Expected behavior

The parser should correctly identify lazy continuation lines and handle them appropriately:
- If a line is marked as lazy in the parser state, it should NOT be treated as part of the indented code block continuation
- If a line is NOT lazy, it should be allowed to continue the code block

Currently experiencing the opposite behavior where the lazy check logic appears to be reversed.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
