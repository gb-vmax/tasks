# Bug Report

### Describe the bug

I'm experiencing an issue with computed property keys in member expressions. When using non-literal computed properties (like variables or expressions), the property resolution seems to be returning incorrect values instead of `null`.

### Reproduction

```js
const obj = {
  foo: 'bar',
  baz: 'qux'
};

const key = 'foo';
// Using a variable as computed property key
const value = obj[key];

// The property key resolution is not working as expected
// It's returning a string representation of the expression instead of null
```

This affects scenarios where computed properties use variables, template literals, or other non-literal expressions. The bundler appears to be incorrectly resolving these dynamic property accesses at build time.

### Expected behavior

When a computed property key is not a literal value (string, number, etc.), the resolver should return `null` to indicate that the property cannot be statically resolved. Instead, it seems to be attempting to convert the expression itself to a string.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
