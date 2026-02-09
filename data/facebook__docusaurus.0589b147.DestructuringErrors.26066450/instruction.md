# Bug Report

### Describe the bug

I'm encountering an issue with destructuring assignment validation in MDX. It seems like shorthand property assignments in object destructuring are being incorrectly flagged or handled during parsing.

### Reproduction

```js
// This kind of destructuring pattern is causing issues
const obj = { x: 1 };
const { x } = obj;

// Specifically when used in MDX content with shorthand assignments
```

When parsing MDX content that contains object destructuring with shorthand properties, the parser appears to be treating valid destructuring patterns as errors or not handling them correctly.

### Expected behavior

Valid JavaScript destructuring syntax should be parsed correctly without throwing unexpected errors. Shorthand property assignments in destructuring patterns should work the same way they do in regular JavaScript.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This appears to have started happening recently. The destructuring error tracking seems to be initialized incorrectly, causing valid patterns to fail validation.

---
Repository: /testbed
