# Bug Report

### Describe the bug

I'm experiencing an issue with destructuring assignment where side effects are not being properly detected in certain cases. When destructuring with a simple property access (single level), the bundler appears to be incorrectly treating it as having side effects, which affects tree-shaking behavior.

### Reproduction

```js
const obj = { value: 42 };

// This seems to be incorrectly flagged as having side effects
const { value } = obj;

console.log(value);
```

The issue appears when destructuring objects with direct property access. The bundler is being overly conservative and treating these operations as potentially having side effects even when they shouldn't.

### Expected behavior

Simple destructuring operations on plain objects without getters or complex access patterns should not be treated as having side effects. This should allow proper tree-shaking when the destructured values are unused.

### Additional context

This seems to affect how the bundler optimizes code during the tree-shaking phase. Code that should be eliminated as dead code is being kept because of incorrectly detected side effects.

---
Repository: /testbed
