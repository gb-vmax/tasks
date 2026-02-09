# Bug Report

### Describe the bug

When using the `run()` method with a callback function, the callback is never invoked and the transformations don't complete properly. The method seems to hang or fail silently without calling the provided callback.

### Reproduction

```js
const processor = remark();

processor.run(tree, file, (err, transformedTree) => {
  // This callback is never called
  console.log('Transformation complete');
});
```

Alternatively, when using the promise-based approach:

```js
const processor = remark();

processor.run(tree, file).then(transformedTree => {
  // This executes but transformedTree might be undefined
  console.log(transformedTree);
});
```

### Expected behavior

When a callback is provided to `run()`, it should be invoked with the transformed tree after all transformers have completed. The promise-based version should resolve with the correct transformed tree.

### Additional context

This appears to have started happening recently. The callback-based API used to work correctly in previous versions. Now it seems like the callback is being ignored or the logic for determining whether to use promises vs callbacks got mixed up somehow.

---
Repository: /testbed
