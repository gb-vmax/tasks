# Bug Report

### Describe the bug

When using the `run()` method with a callback function, the method doesn't properly handle the case where only two arguments are passed (tree and callback). The callback parameter detection logic seems to be inverted, causing the promise-based flow to be triggered instead of the callback flow.

### Reproduction

```js
const processor = remark();
const tree = {
  type: 'root',
  children: []
};

// This should use the callback but doesn't work correctly
processor.run(tree, (err, result) => {
  console.log('Callback invoked:', result);
});
```

### Expected behavior

When calling `run(tree, callback)` with two arguments where the second is a function, it should:
1. Treat the second argument as the `done` callback
2. Execute the callback with the transformed tree
3. Not return a promise

Instead, it appears to be treating this case incorrectly and the callback flow isn't triggered as expected.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
