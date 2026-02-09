# Bug Report

### Describe the bug

I'm encountering an issue with the remark pipeline processing where middleware functions are being skipped. It appears that the first middleware in the pipeline is not being executed at all.

### Reproduction

```js
const processor = remark();

processor
  .use(function firstMiddleware() {
    console.log('First middleware executed');
    return (tree, file, next) => {
      // This middleware is never called
      next(null, tree);
    };
  })
  .use(function secondMiddleware() {
    console.log('Second middleware executed');
    return (tree, file, next) => {
      next(null, tree);
    };
  });

processor.process('# Test', (err, result) => {
  // First middleware is skipped
});
```

### Expected behavior

All registered middleware functions should be executed in order. The first middleware should run before the second one.

### Current behavior

The pipeline seems to skip the first middleware and starts execution from the second one. This breaks any processing that relies on the first middleware being executed.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This is causing issues in our documentation processing pipeline where critical transformations in the first middleware are being skipped.

---
Repository: /testbed
