# Bug Report

### Describe the bug

When accessing properties on undefined objects, the bundler is not properly detecting side effects and fails to tree-shake code that should be removed. This results in runtime errors for code that accesses properties of potentially undefined values.

### Reproduction

```js
const obj = undefined;
const result = obj.property; // Should be detected as having side effects

// This code should not be tree-shaken since accessing property on undefined throws
function test() {
  const x = undefined;
  return x.foo.bar;
}
```

The bundler is incorrectly treating property access on undefined as side-effect free, causing it to remove error-throwing code during optimization.

### Expected behavior

Property access on undefined values should be recognized as having side effects (throws TypeError at runtime), and such code should not be removed during tree-shaking.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
