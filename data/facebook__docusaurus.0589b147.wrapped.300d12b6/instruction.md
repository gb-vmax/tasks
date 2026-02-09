# Bug Report

### Describe the bug

I'm encountering an issue with promise rejection handling in the remark middleware pipeline. When a middleware function returns a rejected promise, the error is not being properly caught and passed to the error handler. Instead, it seems to be silently swallowed or passed to the wrong callback.

### Reproduction

```js
const processor = remark()
  .use(function() {
    return async function(tree) {
      // This rejection should trigger the error callback
      throw new Error('Processing failed');
    };
  });

processor.process('# Test', function(err, file) {
  if (err) {
    console.log('Error caught:', err.message);
  } else {
    console.log('Success - this should not happen');
  }
});
```

### Expected behavior

When a middleware returns a rejected promise, the error should be passed to the done callback so it can be properly handled. The error handler should receive the error and be able to log or handle it appropriately.

### Actual behavior

The error doesn't seem to be properly propagated through the callback chain. The success path is being called even when an error occurs in the async middleware.

This is causing issues in our build pipeline where errors during markdown processing are not being reported correctly, leading to silent failures.

---
Repository: /testbed
