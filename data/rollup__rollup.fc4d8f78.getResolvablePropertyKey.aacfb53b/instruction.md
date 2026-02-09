# Bug Report

### Describe the bug

I'm experiencing an issue with member expression property resolution. When accessing object properties using bracket notation (computed properties), the property key is not being resolved correctly. Similarly, dot notation access seems to have the opposite problem.

### Reproduction

```js
const obj = {
  foo: 'bar',
  'computed-key': 'value'
}

// Bracket notation - property not resolved correctly
const a = obj['foo']

// Dot notation - also behaving unexpectedly  
const b = obj.computed
```

The property key resolution appears to be inverted - computed member expressions (bracket notation) are being treated as non-computed and vice versa.

### Expected behavior

- Bracket notation `obj['foo']` should correctly resolve the property key
- Dot notation `obj.foo` should correctly resolve the property name
- Both should work independently and return the correct values

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
