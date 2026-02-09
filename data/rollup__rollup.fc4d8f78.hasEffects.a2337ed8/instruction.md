# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking in try-catch-finally statements. It seems like the bundler is incorrectly removing try-catch blocks that should be kept in the output.

### Reproduction

```js
// Input code
try {
  console.log('This should be included');
} catch (e) {
  // empty catch
}

// After bundling, the entire try-catch block is removed from output
// even though it has side effects
```

Also noticed that when a finalizer is present:

```js
try {
  sideEffect();
} catch (e) {
  // handle error
} finally {
  cleanup();
}

// The try block gets removed even though it contains side effects
```

### Expected behavior

Try-catch blocks with side effects in the try block should be preserved in the bundle. The presence of a finally block should not cause the try block to be incorrectly eliminated.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started recently, possibly related to tree-shaking optimizations for try-catch statements.

---
Repository: /testbed
