# Bug Report

### Describe the bug

I'm experiencing an issue with middleware execution order in the remark parser. It seems like middleware functions are being called in the wrong sequence or skipped entirely when processing markdown content.

### Reproduction

```js
const {remark} = require('remark');

const processor = remark()
  .use(function firstMiddleware() {
    return (tree) => {
      console.log('First middleware');
    };
  })
  .use(function secondMiddleware() {
    return (tree) => {
      console.log('Second middleware');
    };
  })
  .use(function thirdMiddleware() {
    return (tree) => {
      console.log('Third middleware');
    };
  });

processor.process('# Test');
```

### Expected behavior

The middleware should execute in order:
```
First middleware
Second middleware
Third middleware
```

### Actual behavior

The first middleware gets skipped or the execution order is incorrect. The middleware chain doesn't process all registered plugins properly.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have broken recently. The middleware pipeline isn't iterating through all the registered functions correctly.

---
Repository: /testbed
