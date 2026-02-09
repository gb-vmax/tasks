# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking behavior in try-catch statements. It seems like try-catch blocks are being included in the bundle even when `tryCatchDeoptimization` is disabled in the treeshake configuration.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'esm'
  },
  treeshake: {
    tryCatchDeoptimization: false
  }
}

// src/index.js
function test() {
  try {
    console.log('This should be tree-shaken');
  } catch (e) {
    // unused
  }
}

// test() is never called
```

### Expected behavior

When `tryCatchDeoptimization` is set to `false`, unused try-catch blocks should be removed from the bundle during tree-shaking. The try block should only be included if it's actually referenced or has side effects.

### Actual behavior

The try-catch statement is being included in the final bundle regardless of the `tryCatchDeoptimization` setting. It appears the condition for including these blocks might be inverted.

### Environment

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
