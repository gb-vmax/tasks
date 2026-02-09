# Bug Report

### Describe the bug

I'm encountering an issue with optional chaining expressions where side effects are being incorrectly evaluated. When using optional chaining (`?.`) in my code, expressions that should be treated as having no side effects are being flagged as having side effects, or vice versa.

This seems to affect tree-shaking behavior - code that should be removed as dead code is being kept in the bundle, or code with actual side effects might be getting removed when it shouldn't be.

### Reproduction

```js
// Example 1: Optional chaining with function calls
const result = obj?.method?.();

// Example 2: Nested optional chaining
const value = data?.user?.profile?.name;

// Example 3: Optional chaining with side effects
const output = obj?.fn?.();
```

The bundler is not correctly determining whether these optional chaining expressions have side effects, which impacts the final bundle output.

### Expected behavior

Optional chaining expressions should correctly report whether they have side effects based on the underlying expression behavior. This should properly handle cases where:
- The chain short-circuits (returns undefined)
- The expression has actual side effects
- The expression is pure and can be safely removed

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
