# Bug Report

### Describe the bug

I'm encountering an issue with member expression handling where computed property access is being incorrectly identified. When accessing object properties using bracket notation (computed), the code is treating them as if they were dot notation (non-computed), and vice versa.

### Reproduction

```js
const obj = {
  foo: 'bar',
  'computed-key': 'value'
}

// Bracket notation access (computed property)
obj['foo']  // Being treated as non-computed

// Dot notation access (non-computed property)
obj.foo  // Being treated as computed
```

This is causing issues with property resolution and code generation. The behavior seems inverted - computed properties are being flagged as non-computed and non-computed properties are being flagged as computed.

### Expected behavior

Bracket notation property access (`obj['key']`) should be identified as computed, while dot notation access (`obj.key`) should be identified as non-computed. The current behavior appears to have this logic reversed.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
