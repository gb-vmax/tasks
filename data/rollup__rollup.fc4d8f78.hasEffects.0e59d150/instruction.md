# Bug Report

### Describe the bug

While loops with side effects in the test condition are being incorrectly removed during tree-shaking. The bundler is treating while statements as having no effects when they actually do, causing critical code to be eliminated from the final bundle.

### Reproduction

```js
let counter = 0;

while (sideEffectFunction()) {
  doSomething();
}

// The while loop gets removed even though sideEffectFunction() 
// has side effects that should be preserved
```

Another case:

```js
let i = 0;
while (i++ < 10) {
  // loop body
}
// The entire loop is being tree-shaken out
```

### Expected behavior

While statements should be included in the bundle when:
1. The test condition has side effects (like function calls with side effects, assignments, etc.)
2. The loop body has side effects

Currently it seems like while loops are being dropped even when they contain important side effects.

### System Info
- Rollup version: latest main branch
- Node version: 18.x

---
Repository: /testbed
