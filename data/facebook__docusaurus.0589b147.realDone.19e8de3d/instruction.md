# Bug Report

### Describe the bug

When using the MDX processor with callback-based transformers, the callback flow is broken. If you provide a `done` callback to the `run` method, it never gets called. Instead, the code seems to be trying to use a promise resolver that doesn't exist in callback mode.

### Reproduction

```js
const processor = unified()
  .use(remarkParse)
  .use(remarkMdx)
  // ... other plugins

processor.run(tree, file, (error, resultTree, resultFile) => {
  // This callback never executes
  console.log('Done processing:', resultTree);
});
```

### Expected behavior

When passing a callback function to `run()`, it should be invoked after the transformation completes. The callback should receive the error (if any), the transformed tree, and the file object.

Currently it seems like the logic is inverted - when you provide a callback, the code tries to use a promise resolver instead, and when you don't provide a callback (promise mode), it tries to call the callback.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
