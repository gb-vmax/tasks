# Bug Report

### Describe the bug

I'm experiencing an issue with parsing link destinations in MDX. When using angle-bracket enclosed destinations (like `<http://example.com>`), the parser doesn't seem to be handling them correctly. It appears that the logic for determining when an enclosed destination ends is broken.

### Reproduction

```mdx
[link text](<http://example.com>)
```

The parser should recognize the angle-bracket enclosed URL and parse it correctly, but it seems to be treating it incorrectly.

Also seeing issues with balanced parentheses in raw (non-enclosed) link destinations:

```mdx
[link](http://example.com/path(with)parens)
```

This should work since the parentheses are balanced, but the parser appears to be terminating the destination prematurely.

### Expected behavior

- Angle-bracket enclosed destinations should be parsed correctly regardless of their content
- Raw destinations with balanced parentheses should be handled properly
- The parser should correctly distinguish between enclosed and raw destination parsing modes

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest LTS

---
Repository: /testbed
