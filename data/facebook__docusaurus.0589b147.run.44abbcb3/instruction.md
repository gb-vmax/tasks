# Bug Report

### Describe the bug

When using the `run()` method from the remark processor, the promise resolution doesn't work correctly. The method seems to hang or not resolve properly when called without a callback function.

### Reproduction

```js
const processor = remark();
const tree = {
  type: 'root',
  children: []
};

// This promise never resolves
processor.run(tree).then(result => {
  console.log('Should print result:', result);
});
```

### Expected behavior

The promise returned by `run()` should resolve with the transformed tree. When calling `processor.run(tree)` without a callback, it should return a promise that properly resolves with the resulting tree.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have started happening recently. The callback version might still work but the promise-based API appears broken.

---
Repository: /testbed
