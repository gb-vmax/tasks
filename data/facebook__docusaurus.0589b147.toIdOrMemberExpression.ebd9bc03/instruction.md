# Bug Report

### Describe the bug

I'm experiencing an issue with member expression generation where the first identifier in a chain is being skipped. When trying to access nested properties, the resulting expression is missing the root object.

### Reproduction

```js
// When converting an array of identifiers to a member expression
const ids = ['foo', 'bar', 'baz'];
const result = toIdOrMemberExpression(ids);

// Expected: foo.bar.baz
// Actual: bar.baz (missing 'foo')
```

The first element in the identifier array seems to be ignored, causing the generated member expression to start from the second element instead of the first.

### Expected behavior

The function should include all identifiers in the chain, starting with the first one as the root object. For an input like `['a', 'b', 'c']`, it should generate `a.b.c`, not `b.c`.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
