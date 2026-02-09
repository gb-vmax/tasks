# Bug Report

### Describe the bug

When creating VFile instances with custom options, properties that are part of the standard order array are getting overwritten unexpectedly. It seems like options are being applied twice - once during the initial loop through the order array, and then again in the final property assignment loop.

### Reproduction

```js
const vfile = new VFile({
  path: '/some/path.md',
  value: 'original content',
  customProp: 'custom value'
});

// Expected: customProp should be set
// Actual: standard properties like 'path' and 'value' get overwritten
```

When passing an options object with both standard properties (like `path`, `value`, `history`) and custom properties, the standard properties seem to be processed incorrectly in the second loop.

### Expected behavior

Custom properties should be added to the VFile instance without affecting the standard properties that were already set in the first loop. Standard properties should only be set once during initialization.

### System Info
- remark version: 15.0.1
- Node.js version: Latest

---
Repository: /testbed
