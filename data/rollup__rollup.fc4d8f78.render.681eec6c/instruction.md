# Bug Report

### Describe the bug

I'm experiencing an issue with sequence expressions where the rendering behavior seems incorrect. When I have a sequence expression like `(a, b, c)` and it gets processed, the output doesn't match what I expect.

### Reproduction

```js
// Input code with sequence expression
const result = (foo(), bar(), baz());

// After bundling, the output is malformed
// The last expression in the sequence is not being handled correctly
```

I noticed this when working with comma-separated expressions where the last expression should be treated specially (e.g., when it's used as a function callee), but it seems like the wrong expression is being identified as the "last" one.

### Expected behavior

The bundler should correctly identify and process the last expression in a sequence, especially when determining which expression needs special rendering context (like `isCalleeOfRenderedParent`).

For example:
```js
// This should work correctly
(sideEffect1(), sideEffect2(), actualFunction)()
```

The `actualFunction` should be recognized as the callee, but currently it seems like the logic is off by one or checking the wrong condition.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
