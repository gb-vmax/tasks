# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking in for-loops where code that should be removed is being kept in the bundle. Specifically, when a for-loop contains side-effect-free initialization or test conditions, the entire loop is being retained even though it shouldn't be.

### Reproduction

```js
// This for-loop should be tree-shaken out completely
for (let i = 0; i < 10; i++) {
  // empty body or side-effect-free code
}

// Another example - loop with pure init/test
for (let x = pureFunction(); x < limit; x++) {
  const unused = x * 2;
}
```

### Expected behavior

For-loops with no side effects in their init, test, or update expressions should be properly tree-shaken when the loop body has no effects. The bundler should recognize that these loops can be safely removed from the output.

Currently it seems like the loop is being included even when all parts are side-effect-free.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
