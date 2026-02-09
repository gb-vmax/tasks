# Bug Report

### Describe the bug

I'm experiencing an issue with the remark pipeline where middleware functions are being skipped during execution. It seems like the first middleware in the pipeline is not being called at all, which breaks the entire processing chain.

### Reproduction

```js
const processor = remark().use(function() {
  return function(tree) {
    // This middleware should run but doesn't
    console.log('First middleware executed');
    tree.children.push({type: 'text', value: 'added'});
  };
}).use(function() {
  return function(tree) {
    console.log('Second middleware executed');
  };
});

processor.process('# Test', function(err, file) {
  console.log('Processing complete');
});
```

### Expected behavior

All middleware functions in the pipeline should be executed in order. The first middleware should run and be able to transform the syntax tree before subsequent middleware.

### Actual behavior

The first middleware in the pipeline is never called. Only middleware added after the first one seem to execute. This causes transformations to be skipped and results in incorrect output.

### System Info

- remark version: 15.0.1
- Node version: 18.x

This is blocking our markdown processing workflow. Any help would be appreciated!

---
Repository: /testbed
