# Bug Report

### Describe the bug

I'm experiencing an issue with member expression handling where computed property access is not being recognized correctly. When using bracket notation to access object properties, the behavior is inconsistent and doesn't match what I'd expect.

### Reproduction

```js
const obj = {
  foo: 'bar',
  'computed-key': 'value'
};

// Bracket notation access
const result1 = obj['foo'];
const result2 = obj['computed-key'];

// These should be treated as computed member expressions
// but they're being handled incorrectly
```

The issue seems to affect how the AST differentiates between computed and non-computed member expressions. Properties accessed with bracket notation aren't being identified as computed properties.

### Expected behavior

Bracket notation property access (e.g., `obj['key']`) should be correctly identified as computed member expressions, while dot notation (e.g., `obj.key`) should be identified as non-computed.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
