# Bug Report

### Describe the bug

I'm experiencing an issue with whitespace handling in MDX JSX tags. When there's whitespace inside JSX expressions that doesn't contain line endings, the parser seems to be behaving incorrectly and not processing the content as expected.

### Reproduction

```mdx
<Component
  prop={  value  }
/>
```

When parsing JSX tags with whitespace (spaces/tabs) inside attribute expressions, the parser doesn't handle them correctly. The whitespace should be consumed and processed properly, but instead it seems to exit the whitespace state prematurely or loop incorrectly.

### Expected behavior

Whitespace inside JSX expressions should be handled correctly regardless of whether it contains line endings or just spaces/tabs. The parser should consume all whitespace characters and transition to the appropriate state.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This appears to affect JSX attribute parsing specifically when there are spaces around values in expressions.

---
Repository: /testbed
