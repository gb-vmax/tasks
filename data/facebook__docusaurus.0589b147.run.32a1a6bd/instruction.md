# Bug Report

### Describe the bug

I'm experiencing an issue with the remark pipeline processing where middleware functions are being skipped. It appears that the first middleware in the pipeline is not being executed at all.

### Reproduction

```js
const processor = remark()
  .use(function firstPlugin() {
    return function (tree) {
      // This plugin never gets called
      console.log('First plugin executed');
    };
  })
  .use(function secondPlugin() {
    return function (tree) {
      console.log('Second plugin executed');
    };
  });

processor.process('# Hello', function (err, file) {
  console.log('Processing complete');
});
```

### Expected behavior

All registered middleware/plugins should be executed in order. The first plugin should run before the second plugin.

### Actual behavior

The first middleware in the pipeline is skipped entirely. Only subsequent middleware functions are being executed. This breaks any processing that relies on the first plugin to transform the content.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
