# Bug Report

### Describe the bug

When using MDX text expressions (inline expressions with `{}`), the markdown serialization is broken. Text expressions are not being handled correctly during the markdown-to-AST conversion process.

### Reproduction

```js
const mdxContent = `
Some text with {inlineExpression} in the middle.

Another paragraph with {anotherExpression}.
`

// Try to parse and serialize back to markdown
// The inline expressions are not properly handled
```

### Expected behavior

Inline MDX expressions should be correctly serialized when converting back to markdown format. The expressions should be preserved in their original form.

### Additional context

This appears to affect text expressions specifically - flow expressions (block-level) seem to work fine. The issue is with inline/phrasing content that contains curly braces.

---
Repository: /testbed
