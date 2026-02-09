# Bug Report

### Describe the bug

Member expressions are incorrectly being treated as defined when they should be undefined. This is causing issues with optional chaining and nullish coalescing operators where the code doesn't properly handle undefined property accesses.

### Reproduction

```js
const obj = {};
const result = obj?.nonExistent?.deepProperty;

// Expected: undefined
// Actual: behaves as if the property exists
```

Another case:

```js
const data = { foo: undefined };
const value = data.foo ?? 'default';

// The nullish coalescing doesn't work correctly because
// the member expression is not properly detected as undefined
```

### Expected behavior

Member expressions that resolve to undefined should be correctly identified as undefined, allowing optional chaining and nullish coalescing to work properly. The `isUndefined` flag should accurately reflect whether a member expression evaluates to undefined.

### System Info

- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently and is breaking our builds where we rely on proper undefined handling for optional chaining patterns.

---
Repository: /testbed
