# Bug Report

### Describe the bug

When accessing `import.meta` properties, the bundler is incorrectly treating them as having side effects. This causes issues with tree-shaking and optimization, as code that simply reads `import.meta` properties gets retained even when it shouldn't be.

### Reproduction

```js
// This should be tree-shakeable but isn't
function checkEnvironment() {
  const url = import.meta.url;
  return url;
}

// If this function is never called, it should be removed during bundling
// but it's being kept in the output
```

Another example:
```js
if (import.meta.env) {
  // Code here is being treated as having side effects
  // even though just accessing import.meta.env shouldn't
}
```

### Expected behavior

Reading properties from `import.meta` (like `import.meta.url`, `import.meta.env`, etc.) should not be considered as having side effects. These are just property accesses and should be tree-shakeable when the values aren't used.

### Additional context

This seems to affect any code that accesses `import.meta` properties. The bundler is being overly conservative and treating these accesses as if they have side effects, which prevents proper dead code elimination.

---
Repository: /testbed
