# Bug Report

### Describe the bug

Functions with `@__NO_SIDE_EFFECTS__` annotations are being incorrectly treated as having side effects, which prevents proper tree-shaking. This causes functions that should be removed during dead code elimination to remain in the bundle.

### Reproduction

```js
// This function should be tree-shaken when unused
/* @__NO_SIDE_EFFECTS__ */
function pureHelper() {
  return { value: 42 };
}

// Even though it's marked as pure and never called,
// it's not being removed from the bundle
```

The annotation is being respected in reverse - functions marked as having no side effects are treated as if they do have side effects, and vice versa.

### Expected behavior

Functions annotated with `@__NO_SIDE_EFFECTS__` should be recognized as side-effect-free and eligible for tree-shaking when they're not used. The bundler should remove these functions during optimization if they have no references.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
