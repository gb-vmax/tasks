# Bug Report

### Describe the bug

When using multiple markdown extensions with remark, the last extension in the array is being ignored and not applied to the parser. Only the extensions before the last one are processed correctly.

### Reproduction

```js
const remark = require('remark');

const extension1 = { /* first extension config */ };
const extension2 = { /* second extension config */ };
const extension3 = { /* third extension config */ };

const processor = remark().use({
  extensions: [extension1, extension2, extension3]
});

// Only extension1 and extension2 are applied
// extension3 is completely ignored
```

### Expected behavior

All extensions passed in the array should be processed and applied to the parser, including the last one.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
