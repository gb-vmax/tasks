# Bug Report

### Describe the bug

I'm experiencing an issue where string literals are not being properly tracked for side effects during tree-shaking. It appears that accessing properties on string literals is incorrectly being marked as having side effects, which prevents proper dead code elimination.

### Reproduction

```js
// This code should be tree-shaken but isn't
const str = "hello";
const len = str.length;  // Accessing .length on a string literal

// Similarly, this should also be optimized away
const test = "world";
const char = test.charAt(0);
```

When bundling code that accesses properties or methods on string literals, the code is not being eliminated even when the result is unused. This results in larger bundle sizes than expected.

### Expected behavior

Accessing properties like `.length` on string literals should not be considered as having side effects. The bundler should be able to safely remove this code during tree-shaking when the result is not used.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems like a regression as this was working correctly in previous versions. The issue specifically affects string literal property access and method calls.

---
Repository: /testbed
