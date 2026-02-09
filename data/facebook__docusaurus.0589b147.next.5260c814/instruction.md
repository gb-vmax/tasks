# Bug Report

### Describe the bug

I'm experiencing an issue with middleware pipeline execution in remark. When using multiple middleware functions in a chain, the pipeline stops executing prematurely when one of the middleware functions returns an empty array or no output values.

### Reproduction

```js
const processor = remark()
  .use(function firstMiddleware() {
    return function (tree, file) {
      // Process and pass through
      return tree;
    };
  })
  .use(function secondMiddleware() {
    return function (tree, file) {
      // This middleware returns empty/no values
      return;
    };
  })
  .use(function thirdMiddleware() {
    return function (tree, file) {
      // This should still execute but doesn't
      console.log('Third middleware executed');
      return tree;
    };
  });

processor.process('# Test');
```

### Expected behavior

All middleware in the chain should execute sequentially, even if one of them returns undefined or an empty result. The third middleware should run and log the message.

### Actual behavior

The pipeline stops after the second middleware when it doesn't return explicit values. The third middleware never gets called.

This is breaking my plugin chain where some middleware functions perform side effects without modifying the tree. They should still allow the pipeline to continue.

---
Repository: /testbed
