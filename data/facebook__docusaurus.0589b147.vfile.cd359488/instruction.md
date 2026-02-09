# Bug Report

### Describe the bug

I'm experiencing an issue with file processing where VFile objects are being double-wrapped or incorrectly converted. When passing an existing VFile object to a function that should preserve it, the object gets unnecessarily re-instantiated instead of being returned as-is.

### Reproduction

```js
const existingVFile = new VFile('test content');
const result = vfile(existingVFile);

// Expected: result should be the same VFile instance
// Actual: result is a newly created VFile wrapping the existing one
```

The problem seems to occur when:
1. You create a VFile object
2. Pass it to a function that checks if it's already a VFile
3. Instead of returning the original object, it gets wrapped again

### Expected behavior

When passing an existing VFile object to `vfile()`, it should return the original object unchanged, not create a new VFile instance from it. This is causing issues with object identity checks and potentially duplicating data.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
