# Bug Report

### Describe the bug

I'm experiencing an issue with async middleware handling in remark. When a middleware function returns a Promise, the success and error callbacks seem to be inverted - successful resolutions are being treated as errors and vice versa.

### Reproduction

```js
const remark = require('remark');

const processor = remark().use(function() {
  return async function(tree) {
    // This async operation should succeed
    await Promise.resolve();
    return tree;
  };
});

processor.process('# Test', function(err, file) {
  if (err) {
    console.log('Error:', err); // This gets called even though operation succeeded
  } else {
    console.log('Success:', file); // This never gets called
  }
});
```

### Expected behavior

When a middleware function's Promise resolves successfully, it should call the success callback. When it rejects, it should call the error callback. Currently it seems to be doing the opposite.

Additionally, there seems to be an issue with how the callback detection works - middleware functions that expect exactly the same number of parameters as provided are not being recognized as callback-expecting functions.

### System Info
- remark version: 15.0.1
- Node.js version: 18.x

---
Repository: /testbed
