# Bug Report

### Describe the bug

When using the `run()` method with a callback function, the callback is never invoked even though the transformation completes successfully. The promise-based usage works fine, but the callback-based API appears to be broken.

### Reproduction

```js
const processor = remark();

// This callback never gets called
processor.run(tree, file, (err, resultTree, resultFile) => {
  console.log('This never prints');
  // Expected to handle the transformed tree here
});
```

The callback should be invoked with the transformed tree after processing completes, but nothing happens. When using the promise-based API instead, everything works as expected:

```js
// This works fine
processor.run(tree, file).then(resultTree => {
  console.log('Promise resolved correctly');
});
```

### Expected behavior

The callback function should be invoked with `(error, tree, file)` after the transformation completes, similar to how it worked in previous versions.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
