# Bug Report

### Describe the bug

When using `experimentalLogSideEffects` option, the side effect logging is triggered before actually checking if the node has side effects. This causes the logger to report side effects for nodes that don't actually have any side effects.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'es'
  },
  experimentalLogSideEffects: true
};

// src/index.js
const pureFunction = () => {
  return 42;
};

const result = pureFunction();
```

### Expected behavior

The logger should only report side effects for nodes that actually have side effects. Pure function calls and other side-effect-free code should not be logged as having side effects.

### Actual behavior

The logger reports side effects for the first node in the program body regardless of whether it actually has side effects or not.

---
Repository: /testbed
