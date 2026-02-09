# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking behavior when using try-catch statements. It seems like try-catch blocks are being incorrectly removed from the bundle even when they contain code that should be included.

### Reproduction

```js
// This code is being incorrectly tree-shaken
try {
  console.log('This should be included');
  someFunction();
} catch (e) {
  console.error(e);
}
```

When I bundle this code with `tryCatchDeoptimization` enabled, the entire try block gets removed even though it contains side effects. The opposite also seems to happen - empty try blocks are sometimes being kept in the output when they should be removed.

### Expected behavior

Try-catch blocks should be included in the bundle when:
1. The try block contains statements with side effects
2. The finalizer (finally block) has effects

Empty try blocks with no side effects should be removed during tree-shaking.

### Additional context

This appears to be related to the `tryCatchDeoptimization` option in the treeshake configuration. The logic for determining whether a try statement has effects seems inverted.

---
Repository: /testbed
