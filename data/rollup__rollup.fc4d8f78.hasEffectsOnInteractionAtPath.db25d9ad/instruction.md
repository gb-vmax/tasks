# Bug Report

### Describe the bug

I'm experiencing an issue where binary expressions are being incorrectly tree-shaken from the output bundle. When accessing properties on the result of a binary expression, the entire expression gets removed during the build process even though it's actually needed.

### Reproduction

```js
const obj = (a || b).someProperty;
```

When bundling code like this, the binary expression `(a || b)` is being eliminated from the output, causing runtime errors when trying to access `.someProperty`.

This seems to happen specifically when:
1. You have a binary expression (like `||`, `&&`, etc.)
2. You're accessing a property on the result of that expression
3. The bundler's tree-shaking is enabled

### Expected behavior

The binary expression should be preserved in the output since it's needed to compute the value before the property access. The bundler should recognize that accessing properties on a binary expression result means the expression has side effects and cannot be removed.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
