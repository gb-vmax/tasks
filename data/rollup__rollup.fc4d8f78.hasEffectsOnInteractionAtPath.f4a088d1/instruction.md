# Bug Report

### Describe the bug

I'm experiencing an issue where object property access is incorrectly being flagged as having side effects. When accessing properties on objects (not calling methods), the bundler seems to be treating these accesses as if they could have side effects, which is causing unexpected behavior in tree-shaking and code optimization.

### Reproduction

```js
const obj = {
  foo: 'bar',
  nested: {
    value: 42
  }
};

// Simple property access
const x = obj.foo;

// Nested property access
const y = obj.nested.value;
```

These simple property reads should not be considered as having side effects, but the bundler is treating them as if they do. This affects dead code elimination and causes code that should be removed to be retained in the bundle.

### Expected behavior

Property access on regular objects (without method calls) should not be flagged as having side effects. Only method calls or property assignments should be considered as potentially having side effects.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
