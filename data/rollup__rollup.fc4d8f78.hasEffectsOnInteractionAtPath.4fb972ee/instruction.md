# Bug Report

### Describe the bug

Accessing properties on undefined values is not being detected as having side effects during tree-shaking analysis. This causes code that should be retained (because it would throw a runtime error) to be incorrectly removed from the bundle.

### Reproduction

```js
const obj = undefined;

// This should throw "Cannot read property 'foo' of undefined" at runtime
// but is being tree-shaken out as if it has no effects
obj.foo;
```

When bundling code that accesses properties on undefined values, the bundler treats these accesses as side-effect-free and removes them. However, these operations would actually throw a TypeError at runtime and should be preserved.

### Expected behavior

Property access on undefined values should be recognized as having side effects (since they throw errors at runtime), and the code should be retained in the bundle rather than being tree-shaken away.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
