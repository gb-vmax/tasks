# Bug Report

### Describe the bug

I'm experiencing an issue where boolean literals are not being treated correctly in terms of side effects. When accessing properties directly on a boolean value, the bundler is incorrectly assuming there are no side effects, which leads to incorrect tree-shaking behavior.

### Reproduction

```js
const value = true;
const result = value.toString();
// The access to .toString() should be considered as having potential effects
// but it's being incorrectly optimized away
```

Another example:
```js
function test() {
  const bool = false;
  return bool.valueOf();
}
// The method call on the boolean is not being tracked properly
```

### Expected behavior

Direct property access on boolean literals (like `.toString()` or `.valueOf()`) should be recognized as having potential side effects and should not be incorrectly removed during the optimization phase.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently and is causing issues with code that relies on boolean methods being called properly.

---
Repository: /testbed
