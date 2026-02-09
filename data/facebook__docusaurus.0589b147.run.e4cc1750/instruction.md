# Bug Report

### Describe the bug

When using the `run()` method with a callback function, the callback is being invoked with incorrect arguments in the success case. The first parameter passed to the callback should be `undefined` (or `void 0`) when there's no error, but it's receiving the error parameter instead.

### Reproduction

```js
processor.run(tree, file, (err, result, file) => {
  // Expected: err should be undefined on success
  // Actual: err contains the error parameter even on success
  console.log('Error:', err); // Should be undefined but isn't
  console.log('Result:', result);
});
```

### Expected behavior

When the transformation succeeds, the callback should be called with:
- First parameter: `undefined` (no error)
- Second parameter: the resulting tree
- Third parameter: the file

### Actual behavior

The callback receives the error parameter as the first argument even when the operation succeeds, which breaks the standard Node.js error-first callback convention.

---
Repository: /testbed
