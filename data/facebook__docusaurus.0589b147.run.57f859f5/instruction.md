# Bug Report

### Describe the bug

The `run()` method is not correctly handling the callback-based API when using the two-argument form (tree and callback). When calling `run(tree, callback)`, the callback is never invoked and the promise path is taken instead.

### Reproduction

```js
const processor = unified()
  .use(somePlugin)

// This callback never gets called
processor.run(tree, (err, result) => {
  console.log('This is never executed')
})
```

The issue occurs when you pass a callback function as the second argument. The method should detect that `file` is actually a callback function and handle it appropriately, but it seems like the detection logic is inverted.

### Expected behavior

When calling `run(tree, callback)`, the callback should be invoked with the result. The two-argument form should work as documented in the API.

### System Info
- Package: @mdx-js/mdx@3.0.0
- Node version: 18.x

This is blocking our migration as we rely on the callback-based API in several places. Any workaround would be appreciated!

---
Repository: /testbed
